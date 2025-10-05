#!/usr/bin/env python3
"""
Notification System - My Name Is Claude Framework v3.5.0

Multi-channel notification system for background task events.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to available notification channels
2. Integrate with project communication systems
3. Follow project-specific notification preferences
"""

import os
import sys
import json
import smtplib
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import platform

logger = logging.getLogger(__name__)


@dataclass
class NotificationEvent:
    """Notification event data"""
    event_type: str
    severity: str  # info, warning, error, critical
    title: str
    message: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)


class NotificationChannel:
    """Base class for notification channels"""

    def __init__(self, config: Dict):
        self.config = config
        self.enabled = config.get('enabled', False)
        self.min_severity = config.get('min_severity', 'info')
        self.severity_levels = ['info', 'warning', 'error', 'critical']

    def should_notify(self, event: NotificationEvent) -> bool:
        """Check if notification should be sent"""
        if not self.enabled:
            return False

        event_level = self.severity_levels.index(event.severity)
        min_level = self.severity_levels.index(self.min_severity)
        return event_level >= min_level

    def send(self, event: NotificationEvent) -> bool:
        """Send notification (to be implemented by subclasses)"""
        raise NotImplementedError


class ConsoleChannel(NotificationChannel):
    """Console notification channel"""

    def send(self, event: NotificationEvent) -> bool:
        """Send console notification"""
        try:
            # Format message with severity indicator
            severity_icons = {
                'info': 'ℹ️ ',
                'warning': '⚠️ ',
                'error': '❌',
                'critical': '🚨'
            }

            icon = severity_icons.get(event.severity, '')
            formatted_message = f"{icon} [{event.severity.upper()}] {event.title}: {event.message}"

            # Log at appropriate level
            if event.severity == 'info':
                logger.info(formatted_message)
            elif event.severity == 'warning':
                logger.warning(formatted_message)
            elif event.severity in ['error', 'critical']:
                logger.error(formatted_message)

            return True
        except Exception as e:
            logger.error(f"Failed to send console notification: {e}")
            return False


class DesktopChannel(NotificationChannel):
    """Desktop notification channel"""

    def __init__(self, config: Dict):
        super().__init__(config)
        self.system = platform.system().lower()
        self.platform_config = config.get('platform_specific', {})

    def send(self, event: NotificationEvent) -> bool:
        """Send desktop notification"""
        try:
            # Build notification command based on platform
            if self.system == 'linux':
                return self._send_linux(event)
            elif self.system == 'darwin':
                return self._send_macos(event)
            elif self.system == 'windows':
                return self._send_windows(event)
            else:
                logger.warning(f"Unsupported platform for desktop notifications: {self.system}")
                return False
        except Exception as e:
            logger.error(f"Failed to send desktop notification: {e}")
            return False

    def _send_linux(self, event: NotificationEvent) -> bool:
        """Send Linux notification using notify-send"""
        try:
            urgency_map = {
                'info': 'low',
                'warning': 'normal',
                'error': 'critical',
                'critical': 'critical'
            }
            urgency = urgency_map.get(event.severity, 'normal')

            # Escape quotes in message
            message = event.message.replace('"', '\\"')
            title = event.title.replace('"', '\\"')

            cmd = f'notify-send -u {urgency} "{title}" "{message}"'
            os.system(cmd)
            return True
        except Exception as e:
            logger.debug(f"Linux desktop notification failed: {e}")
            return False

    def _send_macos(self, event: NotificationEvent) -> bool:
        """Send macOS notification using osascript"""
        try:
            # Escape quotes in message
            message = event.message.replace('"', '\\"')
            title = event.title.replace('"', '\\"')

            cmd = f'osascript -e \'display notification "{message}" with title "{title}"\''
            os.system(cmd)
            return True
        except Exception as e:
            logger.debug(f"macOS desktop notification failed: {e}")
            return False

    def _send_windows(self, event: NotificationEvent) -> bool:
        """Send Windows notification using win10toast"""
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()

            # Map severity to icon
            icon_path = None  # Can specify custom icon path
            duration = 10 if event.severity in ['error', 'critical'] else 5

            toaster.show_toast(
                event.title,
                event.message,
                icon_path=icon_path,
                duration=duration,
                threaded=True
            )
            return True
        except ImportError:
            logger.debug("win10toast not available for Windows notifications")
            return False
        except Exception as e:
            logger.debug(f"Windows desktop notification failed: {e}")
            return False


class FileChannel(NotificationChannel):
    """File-based notification channel (log to file)"""

    def __init__(self, config: Dict):
        super().__init__(config)
        self.log_file = Path(config.get('log_file', 'project_archive/logs/background-tasks.log'))
        self.rotation_config = config.get('rotation', {})
        self.max_size_mb = self.rotation_config.get('max_size_mb', 10)
        self.max_files = self.rotation_config.get('max_files', 5)

        # Ensure log directory exists
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def send(self, event: NotificationEvent) -> bool:
        """Write notification to log file"""
        try:
            # Check if rotation needed
            self._rotate_if_needed()

            # Format log entry
            log_entry = {
                'timestamp': event.timestamp,
                'severity': event.severity,
                'event_type': event.event_type,
                'title': event.title,
                'message': event.message,
                'metadata': event.metadata
            }

            # Append to log file
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')

            return True
        except Exception as e:
            logger.error(f"Failed to write to log file: {e}")
            return False

    def _rotate_if_needed(self):
        """Rotate log file if it exceeds max size"""
        try:
            if not self.log_file.exists():
                return

            # Check file size
            size_mb = self.log_file.stat().st_size / (1024 * 1024)
            if size_mb < self.max_size_mb:
                return

            # Rotate files
            for i in range(self.max_files - 1, 0, -1):
                old_file = self.log_file.parent / f"{self.log_file.stem}.{i}{self.log_file.suffix}"
                new_file = self.log_file.parent / f"{self.log_file.stem}.{i + 1}{self.log_file.suffix}"

                if old_file.exists():
                    if new_file.exists():
                        new_file.unlink()
                    old_file.rename(new_file)

            # Move current log to .1
            first_backup = self.log_file.parent / f"{self.log_file.stem}.1{self.log_file.suffix}"
            if first_backup.exists():
                first_backup.unlink()
            self.log_file.rename(first_backup)

            logger.info(f"Rotated log file: {self.log_file}")
        except Exception as e:
            logger.error(f"Failed to rotate log file: {e}")


class EmailChannel(NotificationChannel):
    """Email notification channel"""

    def __init__(self, config: Dict):
        super().__init__(config)
        self.smtp_server = config.get('smtp_server', '')
        self.smtp_port = config.get('smtp_port', 587)
        self.from_email = config.get('from_email', '')
        self.to_email = config.get('to_email', '')
        self.username = config.get('username', self.from_email)
        self.password = config.get('password', '')

        # Validate configuration
        if self.enabled and not all([self.smtp_server, self.from_email, self.to_email]):
            logger.warning("Email notification enabled but missing required configuration")
            self.enabled = False

    def send(self, event: NotificationEvent) -> bool:
        """Send email notification"""
        if not self.enabled:
            return False

        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"[{event.severity.upper()}] {event.title}"
            msg['From'] = self.from_email
            msg['To'] = self.to_email

            # Create HTML and text versions
            text_body = self._format_text_body(event)
            html_body = self._format_html_body(event)

            msg.attach(MIMEText(text_body, 'plain'))
            msg.attach(MIMEText(html_body, 'html'))

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                if self.password:
                    server.login(self.username, self.password)
                server.send_message(msg)

            logger.info(f"Sent email notification to {self.to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email notification: {e}")
            return False

    def _format_text_body(self, event: NotificationEvent) -> str:
        """Format plain text email body"""
        body = f"""
Background Task Notification

Severity: {event.severity.upper()}
Event: {event.event_type}
Time: {event.timestamp}

{event.title}

{event.message}
"""
        if event.metadata:
            body += "\n\nAdditional Information:\n"
            for key, value in event.metadata.items():
                body += f"  {key}: {value}\n"

        return body

    def _format_html_body(self, event: NotificationEvent) -> str:
        """Format HTML email body"""
        severity_colors = {
            'info': '#3498db',
            'warning': '#f39c12',
            'error': '#e74c3c',
            'critical': '#c0392b'
        }
        color = severity_colors.get(event.severity, '#3498db')

        html = f"""
        <html>
          <head>
            <style>
              body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
              .header {{ background-color: {color}; color: white; padding: 10px; }}
              .content {{ padding: 20px; }}
              .metadata {{ background-color: #f4f4f4; padding: 10px; margin-top: 20px; }}
              .metadata table {{ width: 100%; }}
              .metadata td {{ padding: 5px; }}
            </style>
          </head>
          <body>
            <div class="header">
              <h2>{event.title}</h2>
            </div>
            <div class="content">
              <p><strong>Severity:</strong> {event.severity.upper()}</p>
              <p><strong>Event Type:</strong> {event.event_type}</p>
              <p><strong>Time:</strong> {event.timestamp}</p>
              <p>{event.message}</p>
        """

        if event.metadata:
            html += """
              <div class="metadata">
                <h3>Additional Information</h3>
                <table>
            """
            for key, value in event.metadata.items():
                html += f"<tr><td><strong>{key}:</strong></td><td>{value}</td></tr>"
            html += """
                </table>
              </div>
            """

        html += """
            </div>
          </body>
        </html>
        """
        return html


class NotificationSystem:
    """
    Multi-channel notification system
    """

    def __init__(self, config: Dict):
        """
        Initialize notification system

        Args:
            config: Notification configuration
        """
        self.config = config
        self.enabled = config.get('enabled', True)
        self.channels: Dict[str, NotificationChannel] = {}
        self.templates = config.get('notification_templates', {})

        # Initialize channels
        self._init_channels()

    def _init_channels(self):
        """Initialize notification channels"""
        channels_config = self.config.get('channels', {})

        # Console channel
        if 'console' in channels_config:
            self.channels['console'] = ConsoleChannel(channels_config['console'])

        # Desktop channel
        if 'desktop' in channels_config:
            self.channels['desktop'] = DesktopChannel(channels_config['desktop'])

        # File channel
        if 'file' in channels_config:
            self.channels['file'] = FileChannel(channels_config['file'])

        # Email channel
        if 'email' in channels_config:
            self.channels['email'] = EmailChannel(channels_config['email'])

        logger.info(f"Initialized {len(self.channels)} notification channels")

    def notify(
        self,
        event_type: str,
        severity: str,
        title: str,
        message: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Send notification through all appropriate channels

        Args:
            event_type: Type of event
            severity: Severity level (info, warning, error, critical)
            title: Notification title
            message: Notification message
            metadata: Additional metadata

        Returns:
            True if at least one channel succeeded
        """
        if not self.enabled:
            return False

        # Create event
        event = NotificationEvent(
            event_type=event_type,
            severity=severity,
            title=title,
            message=message,
            metadata=metadata or {}
        )

        # Send through all channels
        success = False
        for channel_name, channel in self.channels.items():
            if channel.should_notify(event):
                try:
                    if channel.send(event):
                        success = True
                        logger.debug(f"Sent notification via {channel_name}")
                except Exception as e:
                    logger.error(f"Failed to send notification via {channel_name}: {e}")

        return success

    def notify_from_template(
        self,
        template_name: str,
        severity: str,
        **kwargs
    ) -> bool:
        """
        Send notification using a template

        Args:
            template_name: Name of template
            severity: Severity level
            **kwargs: Template variables

        Returns:
            True if notification sent
        """
        template = self.templates.get(template_name)
        if not template:
            logger.warning(f"Template not found: {template_name}")
            return False

        try:
            # Format template
            message = template.format(**kwargs)

            # Extract title from message (first line)
            lines = message.split('\n', 1)
            title = lines[0] if lines else message
            full_message = lines[1] if len(lines) > 1 else message

            return self.notify(
                event_type=template_name,
                severity=severity,
                title=title,
                message=full_message,
                metadata=kwargs
            )
        except Exception as e:
            logger.error(f"Failed to format template {template_name}: {e}")
            return False

    def task_started(self, task_name: str, task_id: str):
        """Notify that a task started"""
        return self.notify_from_template(
            'task_started',
            'info',
            task_name=task_name,
            task_id=task_id
        )

    def task_completed(self, task_name: str, duration: float):
        """Notify that a task completed"""
        return self.notify_from_template(
            'task_completed',
            'info',
            task_name=task_name,
            duration=f"{duration:.1f}"
        )

    def task_failed(self, task_name: str, error: str):
        """Notify that a task failed"""
        return self.notify_from_template(
            'task_failed',
            'error',
            task_name=task_name,
            error=error[:200]  # Limit error message length
        )

    def task_timeout(self, task_name: str, timeout: float):
        """Notify that a task timed out"""
        return self.notify_from_template(
            'task_timeout',
            'warning',
            task_name=task_name,
            timeout=f"{timeout:.0f}"
        )

    def high_resource_usage(self, resource: str, percent: float):
        """Notify about high resource usage"""
        return self.notify_from_template(
            'high_resource_usage',
            'warning',
            resource=resource,
            percent=f"{percent:.1f}"
        )


def main():
    """CLI for notification system testing"""
    import argparse

    parser = argparse.ArgumentParser(description='Notification System Test')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--severity', choices=['info', 'warning', 'error', 'critical'], default='info')
    parser.add_argument('--title', required=True, help='Notification title')
    parser.add_argument('--message', required=True, help='Notification message')

    args = parser.parse_args()

    # Load config
    if args.config and Path(args.config).exists():
        with open(args.config, 'r') as f:
            config = json.load(f).get('notification_system', {})
    else:
        config = {
            'enabled': True,
            'channels': {
                'console': {'enabled': True, 'min_severity': 'info'}
            }
        }

    # Create notification system
    notifier = NotificationSystem(config)

    # Send test notification
    success = notifier.notify(
        event_type='test',
        severity=args.severity,
        title=args.title,
        message=args.message
    )

    print(f"Notification {'sent' if success else 'failed'}")


if __name__ == '__main__':
    main()
