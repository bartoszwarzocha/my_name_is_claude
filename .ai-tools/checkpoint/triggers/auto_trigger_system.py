#!/usr/bin/env python3
"""
Auto-Trigger System for Advanced Checkpoint System

Automatically creates checkpoints at strategic moments during development.
Monitors for triggering events and executes appropriate checkpoint creation.

Part of Framework v3.7.0 - Advanced Checkpoint System

Features:
- Pre/post agent execution triggers
- Quality gate triggers (pre-commit, pre-push, pre-deploy)
- Refactoring detection triggers
- Critical operation triggers
- Configurable trigger rules
- Integration with multi-agent coordinator
"""

import json
import logging
import re
from typing import Dict, List, Optional, Callable
from pathlib import Path
from datetime import datetime
from enum import Enum

from ..core.checkpoint_engine import CheckpointEngine, CheckpointLevel
from ..core.multi_agent_coordinator import MultiAgentCoordinator
from ..core.quality_gates_integration import QualityGatesIntegration, QualityGateType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TriggerType(Enum):
    """Auto-trigger types"""
    PRE_AGENT_EXECUTION = "pre_agent_execution"
    POST_AGENT_SUCCESS = "post_agent_success"
    POST_AGENT_FAILURE = "post_agent_failure"
    PRE_QUALITY_GATE = "pre_quality_gate"
    PRE_COMMIT = "pre_commit"
    PRE_PUSH = "pre_push"
    PRE_REFACTORING = "pre_refactoring"
    CRITICAL_OPERATION = "critical_operation"


class AutoTriggerSystem:
    """
    Automatic checkpoint triggering system.

    Features:
    - Monitor development lifecycle events
    - Trigger checkpoints automatically
    - Configurable trigger rules
    - Integration with coordinators
    """

    def __init__(
        self,
        checkpoint_engine: CheckpointEngine,
        multi_agent_coordinator: Optional[MultiAgentCoordinator] = None,
        quality_gates: Optional[QualityGatesIntegration] = None,
        config: Optional[Dict] = None
    ):
        """
        Initialize auto-trigger system.

        Args:
            checkpoint_engine: CheckpointEngine instance
            multi_agent_coordinator: Optional MultiAgentCoordinator
            quality_gates: Optional QualityGatesIntegration
            config: Optional configuration override
        """
        self.checkpoint_engine = checkpoint_engine
        self.coordinator = multi_agent_coordinator or MultiAgentCoordinator(checkpoint_engine)
        self.quality_gates = quality_gates or QualityGatesIntegration(checkpoint_engine)

        self.config = config or checkpoint_engine.config.get("autoTriggers", {})

        # Trigger registry
        self.triggers: Dict[TriggerType, Callable] = {}
        self._register_triggers()

        # Trigger execution history
        self.trigger_history_file = checkpoint_engine.storage_base / "trigger_history.json"
        self.trigger_history = self._load_trigger_history()

        logger.info("Auto-Trigger System initialized")

    def _load_trigger_history(self) -> Dict:
        """Load trigger execution history"""
        if self.trigger_history_file.exists():
            try:
                with open(self.trigger_history_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Error loading trigger history: {e}")

        return {
            "version": "3.7.0",
            "triggers": {}
        }

    def _save_trigger_history(self):
        """Save trigger execution history"""
        try:
            with open(self.trigger_history_file, 'w') as f:
                json.dump(self.trigger_history, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving trigger history: {e}")

    def _register_triggers(self):
        """Register all trigger handlers"""
        self.triggers = {
            TriggerType.PRE_AGENT_EXECUTION: self._handle_pre_agent_execution,
            TriggerType.POST_AGENT_SUCCESS: self._handle_post_agent_success,
            TriggerType.POST_AGENT_FAILURE: self._handle_post_agent_failure,
            TriggerType.PRE_QUALITY_GATE: self._handle_pre_quality_gate,
            TriggerType.PRE_COMMIT: self._handle_pre_commit,
            TriggerType.PRE_PUSH: self._handle_pre_push,
            TriggerType.PRE_REFACTORING: self._handle_pre_refactoring,
            TriggerType.CRITICAL_OPERATION: self._handle_critical_operation,
        }

    def trigger(
        self,
        trigger_type: TriggerType,
        context: Optional[Dict] = None
    ) -> Optional[str]:
        """
        Execute a trigger.

        Args:
            trigger_type: Type of trigger to execute
            context: Optional context information

        Returns:
            Checkpoint ID if created, None otherwise
        """
        # Check if trigger is enabled
        trigger_config = self.config.get(trigger_type.value, {})
        if not trigger_config.get("enabled", False):
            logger.debug(f"Trigger {trigger_type.value} is disabled")
            return None

        logger.info(f"Executing trigger: {trigger_type.value}")

        # Execute trigger handler
        handler = self.triggers.get(trigger_type)
        if not handler:
            logger.warning(f"No handler for trigger: {trigger_type.value}")
            return None

        try:
            checkpoint_id = handler(context or {}, trigger_config)

            # Record in history
            self._record_trigger_execution(trigger_type, checkpoint_id, success=True)

            return checkpoint_id

        except Exception as e:
            logger.error(f"Error executing trigger {trigger_type.value}: {e}")
            self._record_trigger_execution(trigger_type, None, success=False, error=str(e))
            return None

    def _handle_pre_agent_execution(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle pre-agent execution trigger"""
        agent_type = context.get("agent_type")
        if not agent_type:
            logger.warning("No agent_type in context for pre-agent trigger")
            return None

        # Check if agent is excluded
        exclude_agents = config.get("exclude_agents", [])
        if agent_type in exclude_agents:
            logger.debug(f"Agent {agent_type} is excluded from pre-agent triggers")
            return None

        # Check if this agent matches the filter
        allowed_agents = config.get("agents", ["all"])
        if "all" not in allowed_agents and agent_type not in allowed_agents:
            logger.debug(f"Agent {agent_type} not in allowed agents list")
            return None

        # Create checkpoint via coordinator
        return self.coordinator.pre_agent_execution_checkpoint(
            agent_type=agent_type,
            description=context.get("description"),
            tags=context.get("tags")
        )

    def _handle_post_agent_success(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle post-agent success trigger"""
        agent_type = context.get("agent_type")
        if not agent_type:
            logger.warning("No agent_type in context for post-agent trigger")
            return None

        # Check if agent matches filter
        allowed_agents = config.get("agents", ["all"])
        if "all" not in allowed_agents and agent_type not in allowed_agents:
            return None

        # Create checkpoint via coordinator
        return self.coordinator.post_agent_execution_checkpoint(
            agent_type=agent_type,
            success=True,
            modified_files=context.get("modified_files"),
            description=context.get("description"),
            tags=context.get("tags")
        )

    def _handle_post_agent_failure(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle post-agent failure trigger"""
        agent_type = context.get("agent_type")
        if not agent_type:
            return None

        # Create checkpoint via coordinator
        return self.coordinator.post_agent_execution_checkpoint(
            agent_type=agent_type,
            success=False,
            modified_files=context.get("modified_files"),
            description=context.get("description", "Agent execution failed"),
            tags=(context.get("tags", []) + ["failure"])
        )

    def _handle_pre_quality_gate(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle pre-quality gate trigger"""
        gate_name = context.get("gate_name")
        if not gate_name:
            logger.warning("No gate_name in context for pre-quality-gate trigger")
            return None

        # Check if gate is in configured list
        allowed_gates = config.get("quality_gates", [])
        if gate_name not in allowed_gates:
            logger.debug(f"Quality gate {gate_name} not in configured gates")
            return None

        # Map gate name to type
        gate_type_map = {
            "pre-commit": QualityGateType.PRE_COMMIT,
            "pre-push": QualityGateType.PRE_PUSH,
            "pre-deploy": QualityGateType.PRE_DEPLOY
        }

        gate_type = gate_type_map.get(gate_name, QualityGateType.CUSTOM)

        # Create checkpoint
        label_format = config.get("label_format", "before_{gate_name}_{timestamp}")
        label = label_format.format(
            gate_name=gate_name,
            timestamp=datetime.now().strftime("%H%M%S")
        )

        return self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.QUALITY_GATE,
            label=label,
            description=context.get("description", f"Before {gate_name} quality gate"),
            tags=["quality-gate", gate_name]
        )

    def _handle_pre_commit(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle pre-commit trigger"""
        # Create checkpoint via quality gates
        result = self.quality_gates.pre_commit_gate(
            description=context.get("description", "Pre-commit checkpoint")
        )

        return result.checkpoint_id if result.success else None

    def _handle_pre_push(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle pre-push trigger"""
        # Create checkpoint via quality gates
        result = self.quality_gates.pre_push_gate(
            description=context.get("description", "Pre-push checkpoint")
        )

        return result.checkpoint_id if result.success else None

    def _handle_pre_refactoring(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle pre-refactoring trigger"""
        description = context.get("description", "")
        keywords = config.get("keywords", [])

        # Check if description contains refactoring keywords
        description_lower = description.lower()
        if not any(keyword in description_lower for keyword in keywords):
            logger.debug("No refactoring keywords detected")
            return None

        # Create checkpoint
        label_format = config.get("label_format", "before_refactoring_{timestamp}")
        label = label_format.format(timestamp=datetime.now().strftime("%H%M%S"))

        return self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.AGENT_EXECUTION,
            label=label,
            description=description or "Before refactoring",
            tags=["refactoring", "pre-refactoring"]
        )

    def _handle_critical_operation(self, context: Dict, config: Dict) -> Optional[str]:
        """Handle critical operation trigger"""
        operation = context.get("operation")
        if not operation:
            logger.warning("No operation specified for critical operation trigger")
            return None

        # Check if operation is in configured list
        allowed_operations = config.get("operations", [])
        if operation not in allowed_operations:
            logger.debug(f"Operation {operation} not in configured critical operations")
            return None

        # Create checkpoint
        label_format = config.get("label_format", "before_{operation}_{timestamp}")
        label = label_format.format(
            operation=operation,
            timestamp=datetime.now().strftime("%H%M%S")
        )

        return self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.MANUAL,
            label=label,
            description=context.get("description", f"Before critical operation: {operation}"),
            tags=["critical", operation]
        )

    def _record_trigger_execution(
        self,
        trigger_type: TriggerType,
        checkpoint_id: Optional[str],
        success: bool,
        error: Optional[str] = None
    ):
        """Record trigger execution in history"""
        trigger_name = trigger_type.value

        if trigger_name not in self.trigger_history["triggers"]:
            self.trigger_history["triggers"][trigger_name] = {
                "executions": [],
                "success_count": 0,
                "failure_count": 0
            }

        trigger_data = self.trigger_history["triggers"][trigger_name]

        # Add execution record
        trigger_data["executions"].append({
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "checkpoint_id": checkpoint_id,
            "error": error
        })

        # Update statistics
        if success:
            trigger_data["success_count"] += 1
        else:
            trigger_data["failure_count"] += 1

        # Keep only last 100 executions
        if len(trigger_data["executions"]) > 100:
            trigger_data["executions"] = trigger_data["executions"][-100:]

        self._save_trigger_history()

    def get_trigger_statistics(self, trigger_type: Optional[TriggerType] = None) -> Dict:
        """
        Get trigger execution statistics.

        Args:
            trigger_type: Optional trigger type to filter by

        Returns:
            Statistics dictionary
        """
        if trigger_type:
            trigger_name = trigger_type.value
            if trigger_name in self.trigger_history["triggers"]:
                data = self.trigger_history["triggers"][trigger_name]
                total = data["success_count"] + data["failure_count"]
                return {
                    trigger_name: {
                        "success_count": data["success_count"],
                        "failure_count": data["failure_count"],
                        "success_rate": data["success_count"] / total if total > 0 else 0.0,
                        "total_executions": len(data["executions"])
                    }
                }
            return {}

        # Return statistics for all triggers
        stats = {}
        for trigger_name, data in self.trigger_history["triggers"].items():
            total = data["success_count"] + data["failure_count"]
            stats[trigger_name] = {
                "success_count": data["success_count"],
                "failure_count": data["failure_count"],
                "success_rate": data["success_count"] / total if total > 0 else 0.0,
                "total_executions": len(data["executions"])
            }

        return stats

    def enable_all_triggers(self):
        """Enable all configured triggers"""
        for trigger_type in TriggerType:
            trigger_config = self.config.get(trigger_type.value, {})
            trigger_config["enabled"] = True
        logger.info("All triggers enabled")

    def disable_all_triggers(self):
        """Disable all triggers"""
        for trigger_type in TriggerType:
            trigger_config = self.config.get(trigger_type.value, {})
            trigger_config["enabled"] = False
        logger.info("All triggers disabled")


# CLI Interface
if __name__ == "__main__":
    from ..core.checkpoint_engine import CheckpointEngine

    # Initialize
    engine = CheckpointEngine()
    auto_trigger = AutoTriggerSystem(engine)

    print("\n=== Testing Auto-Trigger System ===")

    # Test pre-agent execution trigger
    print("\n1. Testing pre-agent execution trigger")
    cp_id = auto_trigger.trigger(
        TriggerType.PRE_AGENT_EXECUTION,
        context={"agent_type": "backend-engineer", "description": "Test agent execution"}
    )
    print(f"Created checkpoint: {cp_id}")

    # Test post-agent success trigger
    print("\n2. Testing post-agent success trigger")
    cp_id = auto_trigger.trigger(
        TriggerType.POST_AGENT_SUCCESS,
        context={
            "agent_type": "backend-engineer",
            "modified_files": ["src/api/auth.py"],
            "description": "Implemented authentication"
        }
    )
    print(f"Created checkpoint: {cp_id}")

    # Test pre-refactoring trigger
    print("\n3. Testing pre-refactoring trigger")
    cp_id = auto_trigger.trigger(
        TriggerType.PRE_REFACTORING,
        context={"description": "Refactor authentication module"}
    )
    print(f"Created checkpoint: {cp_id}")

    # Get trigger statistics
    print("\n4. Trigger Statistics")
    stats = auto_trigger.get_trigger_statistics()
    print(json.dumps(stats, indent=2))

    print("\n=== Auto-Trigger System Test Complete ===")
