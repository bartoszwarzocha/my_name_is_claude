#!/usr/bin/env python3
"""
Update Metrics Hook - My Name Is Claude Framework v3.4.0

Updates performance and usage metrics after agent execution.

META: priority: low
META: timeout: 30
META: category: agent-lifecycle/post-agent
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    get_project_root, ensure_directory, load_json, save_json
)


def get_metrics_file() -> Path:
    """
    Get metrics file path

    Returns:
        Path to metrics file
    """
    project_root = get_project_root()
    metrics_dir = project_root / 'project_archive' / 'logs'
    ensure_directory(str(metrics_dir))
    return metrics_dir / 'hooks-metrics.json'


def load_metrics() -> dict:
    """
    Load existing metrics

    Returns:
        Metrics dictionary
    """
    metrics_file = get_metrics_file()

    if metrics_file.exists():
        try:
            return load_json(str(metrics_file))
        except:
            pass

    # Initialize default metrics
    return {
        'version': '3.4.0',
        'agent_executions': {},
        'hook_executions': {},
        'daily_stats': {},
        'totals': {
            'total_agent_executions': 0,
            'total_hook_executions': 0,
            'total_failures': 0,
            'total_warnings': 0
        }
    }


def save_metrics(metrics: dict):
    """
    Save metrics to file

    Args:
        metrics: Metrics dictionary
    """
    metrics_file = get_metrics_file()
    save_json(str(metrics_file), metrics)


def update_agent_metrics(metrics: dict, agent_name: str, context: dict) -> dict:
    """
    Update agent-specific metrics

    Args:
        metrics: Current metrics
        agent_name: Name of the agent
        context: Hook context

    Returns:
        Updated metrics
    """
    if not agent_name:
        return metrics

    # Initialize agent metrics if needed
    if agent_name not in metrics['agent_executions']:
        metrics['agent_executions'][agent_name] = {
            'total_executions': 0,
            'successful_executions': 0,
            'failed_executions': 0,
            'total_execution_time': 0.0,
            'last_execution': None
        }

    agent_metrics = metrics['agent_executions'][agent_name]

    # Update metrics
    agent_metrics['total_executions'] += 1
    agent_metrics['last_execution'] = datetime.now().isoformat()

    # Track success/failure if available in context
    result_data = context.get('result_data', {})
    if result_data.get('success', True):
        agent_metrics['successful_executions'] += 1
    else:
        agent_metrics['failed_executions'] += 1

    # Track execution time if available
    execution_time = context.get('execution_time', 0)
    agent_metrics['total_execution_time'] += execution_time

    return metrics


def update_daily_stats(metrics: dict) -> dict:
    """
    Update daily statistics

    Args:
        metrics: Current metrics

    Returns:
        Updated metrics
    """
    today = datetime.now().strftime('%Y-%m-%d')

    if today not in metrics['daily_stats']:
        metrics['daily_stats'][today] = {
            'agent_executions': 0,
            'hook_executions': 0,
            'failures': 0,
            'warnings': 0
        }

    daily = metrics['daily_stats'][today]
    daily['agent_executions'] += 1

    # Count hooks executed today
    daily['hook_executions'] = daily.get('hook_executions', 0) + 1

    return metrics


def update_totals(metrics: dict) -> dict:
    """
    Update total counters

    Args:
        metrics: Current metrics

    Returns:
        Updated metrics
    """
    totals = metrics['totals']
    totals['total_agent_executions'] += 1

    return metrics


def cleanup_old_metrics(metrics: dict, retention_days: int = 90) -> dict:
    """
    Clean up old daily stats

    Args:
        metrics: Current metrics
        retention_days: Number of days to retain

    Returns:
        Cleaned metrics
    """
    from datetime import datetime, timedelta

    cutoff_date = datetime.now() - timedelta(days=retention_days)
    cutoff_str = cutoff_date.strftime('%Y-%m-%d')

    # Remove old daily stats
    old_dates = [
        date for date in metrics['daily_stats'].keys()
        if date < cutoff_str
    ]

    for date in old_dates:
        del metrics['daily_stats'][date]

    return metrics


def generate_metrics_summary(metrics: dict) -> dict:
    """
    Generate metrics summary

    Args:
        metrics: Current metrics

    Returns:
        Summary dictionary
    """
    totals = metrics['totals']

    # Calculate success rate
    total_executions = totals['total_agent_executions']
    if total_executions > 0:
        success_rate = (
            (total_executions - totals['total_failures']) / total_executions * 100
        )
    else:
        success_rate = 100.0

    # Find most used agent
    most_used_agent = None
    max_executions = 0
    for agent_name, agent_metrics in metrics['agent_executions'].items():
        if agent_metrics['total_executions'] > max_executions:
            max_executions = agent_metrics['total_executions']
            most_used_agent = agent_name

    return {
        'total_executions': total_executions,
        'total_failures': totals['total_failures'],
        'success_rate': round(success_rate, 2),
        'most_used_agent': most_used_agent,
        'most_used_agent_count': max_executions,
        'agents_tracked': len(metrics['agent_executions']),
        'days_tracked': len(metrics['daily_stats'])
    }


def main():
    """Main hook execution"""
    logger = HookLogger("update-metrics")
    context = get_hook_context()

    with HookContext("update-metrics", context):
        try:
            logger.info("Updating metrics")

            # Load current metrics
            metrics = load_metrics()

            # Update agent metrics
            agent_name = context.get('agent_name', '')
            if agent_name:
                metrics = update_agent_metrics(metrics, agent_name, context)
                logger.info(f"Updated metrics for agent: {agent_name}")

            # Update daily stats
            metrics = update_daily_stats(metrics)

            # Update totals
            metrics = update_totals(metrics)

            # Cleanup old metrics
            metrics = cleanup_old_metrics(metrics)

            # Save metrics
            save_metrics(metrics)

            # Generate summary
            summary = generate_metrics_summary(metrics)

            logger.info(f"Metrics updated - Total executions: {summary['total_executions']}")
            logger.info(f"Success rate: {summary['success_rate']}%")

            set_hook_result(
                success=True,
                message="Metrics updated successfully",
                data={'summary': summary}
            )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            # Metrics update failure is not critical
            set_hook_result(
                success=True,  # Don't block on metrics failure
                message=f"Metrics update had warning: {e}"
            )


if __name__ == '__main__':
    main()
