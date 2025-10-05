#!/usr/bin/env python3
"""
Hook Registry System - My Name Is Claude Framework v3.4.0

Hook registration, discovery, and management system for dynamic hook loading.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project structure
2. Integrate with existing plugin/extension systems
3. Follow project-specific validation patterns
"""

import os
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Set, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class HookMetadata:
    """Metadata for a registered hook"""
    name: str
    path: str
    category: str
    priority: str
    timeout: int
    description: str = ""
    version: str = "1.0.0"
    author: str = ""
    dependencies: List[str] = None
    enabled: bool = True
    checksum: str = ""
    registered_at: str = ""
    last_modified: str = ""

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if not self.registered_at:
            self.registered_at = datetime.now().isoformat()


class HookRegistry:
    """
    Central registry for hook discovery and management
    """

    def __init__(self, hooks_dir: Optional[str] = None, registry_file: Optional[str] = None):
        """
        Initialize hook registry

        Args:
            hooks_dir: Root directory for hooks
            registry_file: Path to registry database file
        """
        self.hooks_dir = Path(hooks_dir or self._get_default_hooks_dir())
        self.registry_file = Path(registry_file or self.hooks_dir / 'core' / 'hook_registry.json')
        self.registry: Dict[str, HookMetadata] = {}
        self._load_registry()

    def _get_default_hooks_dir(self) -> str:
        """Get default hooks directory"""
        current_dir = Path.cwd()
        while current_dir != current_dir.parent:
            hooks_dir = current_dir / '.claude' / 'hooks'
            if hooks_dir.exists():
                return str(hooks_dir)
            current_dir = current_dir.parent
        return '.claude/hooks'

    def _load_registry(self):
        """Load registry from file"""
        if self.registry_file.exists():
            try:
                with open(self.registry_file, 'r') as f:
                    data = json.load(f)
                    self.registry = {
                        name: HookMetadata(**meta)
                        for name, meta in data.items()
                    }
                logger.info(f"Loaded {len(self.registry)} hooks from registry")
            except Exception as e:
                logger.error(f"Failed to load registry: {e}")
                self.registry = {}
        else:
            logger.info("Registry file not found, starting with empty registry")
            self.registry = {}

    def _save_registry(self):
        """Save registry to file"""
        try:
            self.registry_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.registry_file, 'w') as f:
                data = {
                    name: asdict(meta)
                    for name, meta in self.registry.items()
                }
                json.dump(data, f, indent=2)
            logger.info(f"Saved {len(self.registry)} hooks to registry")
        except Exception as e:
            logger.error(f"Failed to save registry: {e}")

    def register_hook(
        self,
        name: str,
        path: str,
        category: str,
        priority: str = "medium",
        timeout: int = 60,
        description: str = "",
        version: str = "1.0.0",
        author: str = "",
        dependencies: Optional[List[str]] = None,
        enabled: bool = True
    ) -> bool:
        """
        Register a new hook

        Args:
            name: Unique hook name
            path: Relative path to hook script
            category: Hook category (e.g., 'agent-lifecycle/pre-agent')
            priority: Execution priority (critical, high, medium, low)
            timeout: Execution timeout in seconds
            description: Hook description
            version: Hook version
            author: Hook author
            dependencies: List of required dependencies
            enabled: Whether hook is enabled

        Returns:
            True if registration successful
        """
        if name in self.registry:
            logger.warning(f"Hook {name} already registered, updating...")

        # Calculate checksum
        hook_file = self.hooks_dir / path
        checksum = ""
        if hook_file.exists():
            checksum = self._calculate_checksum(hook_file)
        else:
            logger.warning(f"Hook file not found: {hook_file}")

        # Create metadata
        metadata = HookMetadata(
            name=name,
            path=path,
            category=category,
            priority=priority,
            timeout=timeout,
            description=description,
            version=version,
            author=author,
            dependencies=dependencies or [],
            enabled=enabled,
            checksum=checksum,
            last_modified=datetime.now().isoformat()
        )

        self.registry[name] = metadata
        self._save_registry()

        logger.info(f"✅ Registered hook: {name}")
        return True

    def unregister_hook(self, name: str) -> bool:
        """
        Unregister a hook

        Args:
            name: Hook name to unregister

        Returns:
            True if unregistration successful
        """
        if name not in self.registry:
            logger.warning(f"Hook {name} not found in registry")
            return False

        del self.registry[name]
        self._save_registry()

        logger.info(f"🗑️  Unregistered hook: {name}")
        return True

    def discover_hooks(self, rescan: bool = False) -> Dict[str, HookMetadata]:
        """
        Discover hooks by scanning hooks directory

        Args:
            rescan: Force rescan even if hooks already registered

        Returns:
            Dictionary of discovered hooks
        """
        logger.info("Discovering hooks...")

        discovered = {}

        # Scan all hook categories
        categories = [
            'agent-lifecycle/pre-agent',
            'agent-lifecycle/post-agent',
            'quality-gates/pre-commit',
            'quality-gates/pre-push',
            'quality-gates/pre-deploy',
            'quality-gates/post-deploy',
            'documentation',
            'performance'
        ]

        for category in categories:
            category_path = self.hooks_dir / category
            if not category_path.exists():
                continue

            # Find all Python files
            for hook_file in category_path.glob('*.py'):
                if hook_file.name.startswith('_'):
                    continue

                hook_name = hook_file.stem
                relative_path = str(hook_file.relative_to(self.hooks_dir))

                # Skip if already registered and not rescanning
                if not rescan and hook_name in self.registry:
                    continue

                # Extract metadata from file
                metadata = self._extract_hook_metadata(hook_file, category)
                metadata.path = relative_path

                discovered[hook_name] = metadata

                # Auto-register if new
                if hook_name not in self.registry:
                    self.register_hook(
                        name=hook_name,
                        path=relative_path,
                        category=metadata.category,
                        priority=metadata.priority,
                        timeout=metadata.timeout,
                        description=metadata.description,
                        version=metadata.version,
                        author=metadata.author,
                        dependencies=metadata.dependencies
                    )

        logger.info(f"Discovered {len(discovered)} hooks")
        return discovered

    def get_hooks_by_category(self, category: str) -> List[HookMetadata]:
        """
        Get all hooks in a category

        Args:
            category: Hook category

        Returns:
            List of hook metadata
        """
        return [
            meta for meta in self.registry.values()
            if meta.category == category and meta.enabled
        ]

    def get_hooks_by_priority(self, priority: str) -> List[HookMetadata]:
        """
        Get all hooks with specific priority

        Args:
            priority: Hook priority

        Returns:
            List of hook metadata
        """
        return [
            meta for meta in self.registry.values()
            if meta.priority == priority and meta.enabled
        ]

    def get_hook(self, name: str) -> Optional[HookMetadata]:
        """
        Get hook metadata by name

        Args:
            name: Hook name

        Returns:
            Hook metadata or None
        """
        return self.registry.get(name)

    def enable_hook(self, name: str) -> bool:
        """Enable a hook"""
        if name not in self.registry:
            logger.warning(f"Hook {name} not found")
            return False

        self.registry[name].enabled = True
        self._save_registry()
        logger.info(f"✅ Enabled hook: {name}")
        return True

    def disable_hook(self, name: str) -> bool:
        """Disable a hook"""
        if name not in self.registry:
            logger.warning(f"Hook {name} not found")
            return False

        self.registry[name].enabled = False
        self._save_registry()
        logger.info(f"⏸️  Disabled hook: {name}")
        return True

    def validate_hook(self, name: str) -> Dict[str, Any]:
        """
        Validate a hook

        Args:
            name: Hook name

        Returns:
            Validation results
        """
        if name not in self.registry:
            return {'valid': False, 'error': 'Hook not found in registry'}

        metadata = self.registry[name]
        hook_file = self.hooks_dir / metadata.path

        # Check file exists
        if not hook_file.exists():
            return {'valid': False, 'error': 'Hook file not found'}

        # Check checksum
        current_checksum = self._calculate_checksum(hook_file)
        if metadata.checksum and current_checksum != metadata.checksum:
            return {
                'valid': False,
                'error': 'Hook file modified (checksum mismatch)',
                'expected_checksum': metadata.checksum,
                'actual_checksum': current_checksum
            }

        # Check dependencies
        missing_deps = self._check_dependencies(metadata.dependencies)
        if missing_deps:
            return {
                'valid': False,
                'error': 'Missing dependencies',
                'missing': missing_deps
            }

        # Check executable permissions
        if not os.access(hook_file, os.X_OK):
            return {
                'valid': True,
                'warning': 'Hook file not executable',
                'fix': f'chmod +x {hook_file}'
            }

        return {'valid': True}

    def list_hooks(self, category: Optional[str] = None, enabled_only: bool = False) -> List[str]:
        """
        List all registered hooks

        Args:
            category: Filter by category
            enabled_only: Only show enabled hooks

        Returns:
            List of hook names
        """
        hooks = self.registry.values()

        if category:
            hooks = [h for h in hooks if h.category == category]

        if enabled_only:
            hooks = [h for h in hooks if h.enabled]

        return [h.name for h in hooks]

    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum of file"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _extract_hook_metadata(self, hook_file: Path, category: str) -> HookMetadata:
        """
        Extract metadata from hook file docstring

        Args:
            hook_file: Path to hook file
            category: Hook category

        Returns:
            Hook metadata
        """
        # Default metadata
        metadata = HookMetadata(
            name=hook_file.stem,
            path=str(hook_file),
            category=category,
            priority='medium',
            timeout=60
        )

        try:
            with open(hook_file, 'r') as f:
                content = f.read()

                # Look for metadata in docstring or comments
                # Format: # META: key: value
                for line in content.split('\n'):
                    if line.strip().startswith('# META:'):
                        parts = line.replace('# META:', '').strip().split(':', 1)
                        if len(parts) == 2:
                            key, value = parts
                            key = key.strip().lower()
                            value = value.strip()

                            if key == 'priority':
                                metadata.priority = value
                            elif key == 'timeout':
                                metadata.timeout = int(value)
                            elif key == 'description':
                                metadata.description = value
                            elif key == 'version':
                                metadata.version = value
                            elif key == 'author':
                                metadata.author = value
                            elif key == 'dependencies':
                                metadata.dependencies = [d.strip() for d in value.split(',')]

        except Exception as e:
            logger.warning(f"Failed to extract metadata from {hook_file}: {e}")

        return metadata

    def _check_dependencies(self, dependencies: List[str]) -> List[str]:
        """
        Check if dependencies are available

        Args:
            dependencies: List of required dependencies

        Returns:
            List of missing dependencies
        """
        missing = []
        for dep in dependencies:
            try:
                __import__(dep)
            except ImportError:
                missing.append(dep)
        return missing


def main():
    """CLI entry point for hook registry"""
    import argparse

    parser = argparse.ArgumentParser(description='Hook Registry Management')
    parser.add_argument('command', choices=[
        'list', 'discover', 'register', 'unregister',
        'enable', 'disable', 'validate'
    ])
    parser.add_argument('--name', help='Hook name')
    parser.add_argument('--path', help='Hook path')
    parser.add_argument('--category', help='Hook category')
    parser.add_argument('--priority', help='Hook priority')
    parser.add_argument('--timeout', type=int, help='Hook timeout')
    parser.add_argument('--rescan', action='store_true', help='Force rescan')
    parser.add_argument('--enabled-only', action='store_true', help='Show only enabled hooks')

    args = parser.parse_args()

    # Initialize registry
    registry = HookRegistry()

    # Execute command
    if args.command == 'list':
        hooks = registry.list_hooks(
            category=args.category,
            enabled_only=args.enabled_only
        )
        print(json.dumps(hooks, indent=2))

    elif args.command == 'discover':
        discovered = registry.discover_hooks(rescan=args.rescan)
        print(f"Discovered {len(discovered)} hooks")
        print(json.dumps(list(discovered.keys()), indent=2))

    elif args.command == 'register':
        if not args.name or not args.path or not args.category:
            print("Error: --name, --path, and --category are required")
            return

        success = registry.register_hook(
            name=args.name,
            path=args.path,
            category=args.category,
            priority=args.priority or 'medium',
            timeout=args.timeout or 60
        )
        print(f"Registration {'successful' if success else 'failed'}")

    elif args.command == 'unregister':
        if not args.name:
            print("Error: --name is required")
            return

        success = registry.unregister_hook(args.name)
        print(f"Unregistration {'successful' if success else 'failed'}")

    elif args.command == 'enable':
        if not args.name:
            print("Error: --name is required")
            return

        success = registry.enable_hook(args.name)
        print(f"Enable {'successful' if success else 'failed'}")

    elif args.command == 'disable':
        if not args.name:
            print("Error: --name is required")
            return

        success = registry.disable_hook(args.name)
        print(f"Disable {'successful' if success else 'failed'}")

    elif args.command == 'validate':
        if not args.name:
            print("Error: --name is required")
            return

        result = registry.validate_hook(args.name)
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
