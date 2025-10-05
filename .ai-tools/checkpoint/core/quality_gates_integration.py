#!/usr/bin/env python3
"""
Quality Gates Integration for Advanced Checkpoint System

Integrates checkpoint system with framework quality gates.
Automatically creates checkpoints before quality validations.

Part of Framework v3.7.0 - Advanced Checkpoint System

Features:
- Auto-checkpoint before quality gates
- Integration with pre-commit, pre-push, pre-deploy gates
- Optional rollback on gate failure
- Quality gate execution tracking
- Checkpoint-based gate history
"""

import json
import logging
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
from enum import Enum

from .checkpoint_engine import CheckpointEngine, CheckpointLevel, RollbackResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QualityGateType(Enum):
    """Quality gate types"""
    PRE_COMMIT = "pre-commit"
    PRE_PUSH = "pre-push"
    PRE_DEPLOY = "pre-deploy"
    CUSTOM = "custom"


@dataclass
class QualityGateResult:
    """Result of quality gate execution"""
    gate_type: str
    success: bool
    checkpoint_id: Optional[str] = None
    errors: List[str] = None
    warnings: List[str] = None
    execution_time_seconds: float = 0.0
    message: str = ""

    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.warnings is None:
            self.warnings = []


class QualityGatesIntegration:
    """
    Integrates checkpoint system with quality gates.

    Features:
    - Auto-checkpoint before gates
    - Gate execution tracking
    - Rollback on failure
    - Quality history
    """

    def __init__(self, checkpoint_engine: CheckpointEngine, config: Optional[Dict] = None):
        """
        Initialize quality gates integration.

        Args:
            checkpoint_engine: CheckpointEngine instance
            config: Optional configuration override
        """
        self.checkpoint_engine = checkpoint_engine
        self.config = config or checkpoint_engine.config.get("integrations", {}).get("quality_gates", {})

        # Gate execution history
        self.gate_history_file = checkpoint_engine.storage_base / "quality_gate_history.json"
        self.gate_history = self._load_gate_history()

        logger.info("Quality Gates Integration initialized")

    def _load_gate_history(self) -> Dict:
        """Load quality gate execution history"""
        if self.gate_history_file.exists():
            try:
                with open(self.gate_history_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Error loading gate history: {e}")

        return {
            "version": "3.7.0",
            "gates": {}
        }

    def _save_gate_history(self):
        """Save quality gate execution history"""
        try:
            with open(self.gate_history_file, 'w') as f:
                json.dump(self.gate_history, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving gate history: {e}")

    def execute_quality_gate(
        self,
        gate_type: QualityGateType,
        gate_command: Optional[str] = None,
        description: Optional[str] = None,
        rollback_on_failure: Optional[bool] = None
    ) -> QualityGateResult:
        """
        Execute quality gate with checkpoint integration.

        Args:
            gate_type: Type of quality gate
            gate_command: Command to execute (optional)
            description: Gate description
            rollback_on_failure: Whether to rollback on failure (default from config)

        Returns:
            QualityGateResult with execution details
        """
        logger.info(f"Executing quality gate: {gate_type.value}")

        start_time = datetime.now()
        checkpoint_id = None
        errors = []
        warnings = []

        # Create checkpoint before gate if enabled
        if self.config.get("auto_checkpoint_before_gates", True):
            checkpoint_id = self._create_pre_gate_checkpoint(gate_type, description)
            if not checkpoint_id:
                warnings.append("Failed to create pre-gate checkpoint")

        # Execute quality gate
        gate_success = False
        try:
            if gate_command:
                # Execute custom gate command
                gate_success, gate_errors = self._execute_gate_command(gate_command)
                errors.extend(gate_errors)
            else:
                # Execute standard gate
                gate_success, gate_errors = self._execute_standard_gate(gate_type)
                errors.extend(gate_errors)

        except Exception as e:
            logger.error(f"Error executing quality gate: {e}")
            errors.append(str(e))
            gate_success = False

        # Calculate execution time
        execution_time = (datetime.now() - start_time).total_seconds()

        # Handle failure
        if not gate_success:
            # Determine rollback policy
            should_rollback = rollback_on_failure if rollback_on_failure is not None else self.config.get("rollback_on_gate_failure", False)

            if should_rollback and checkpoint_id:
                logger.warning(f"Quality gate failed - rolling back to checkpoint {checkpoint_id}")
                rollback_result = self.checkpoint_engine.rollback_to_checkpoint(checkpoint_id)
                if rollback_result.success:
                    warnings.append(f"Rolled back to checkpoint: {checkpoint_id}")
                else:
                    errors.append(f"Rollback failed: {rollback_result.message}")

        # Record in history
        self._record_gate_execution(
            gate_type=gate_type,
            success=gate_success,
            checkpoint_id=checkpoint_id,
            execution_time=execution_time,
            errors=errors
        )

        # Build result message
        message = f"✅ Quality gate '{gate_type.value}' passed" if gate_success else f"❌ Quality gate '{gate_type.value}' failed"
        if checkpoint_id:
            message += f" (checkpoint: {checkpoint_id[:8]})"

        result = QualityGateResult(
            gate_type=gate_type.value,
            success=gate_success,
            checkpoint_id=checkpoint_id,
            errors=errors,
            warnings=warnings,
            execution_time_seconds=execution_time,
            message=message
        )

        logger.info(message)
        return result

    def _create_pre_gate_checkpoint(self, gate_type: QualityGateType, description: Optional[str]) -> Optional[str]:
        """Create checkpoint before quality gate"""
        label = f"before_{gate_type.value}_{datetime.now().strftime('%H%M%S')}"

        checkpoint_id = self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.QUALITY_GATE,
            label=label,
            description=description or f"Before {gate_type.value} quality gate",
            tags=["quality-gate", gate_type.value, "pre-gate"]
        )

        if checkpoint_id:
            logger.info(f"Created pre-gate checkpoint: {checkpoint_id}")

        return checkpoint_id

    def _execute_gate_command(self, command: str) -> tuple[bool, List[str]]:
        """
        Execute custom gate command.

        Args:
            command: Shell command to execute

        Returns:
            (success, errors)
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode == 0:
                return True, []
            else:
                errors = result.stderr.strip().split("\n") if result.stderr else ["Command failed"]
                return False, errors

        except subprocess.TimeoutExpired:
            return False, ["Quality gate command timed out (5 minutes)"]
        except Exception as e:
            return False, [f"Error executing gate command: {str(e)}"]

    def _execute_standard_gate(self, gate_type: QualityGateType) -> tuple[bool, List[str]]:
        """
        Execute standard quality gate.

        Args:
            gate_type: Type of quality gate

        Returns:
            (success, errors)
        """
        # Map gate types to standard commands
        gate_commands = {
            QualityGateType.PRE_COMMIT: [
                "git diff --check",  # Check for whitespace errors
                "git status --porcelain"  # Check for uncommitted changes
            ],
            QualityGateType.PRE_PUSH: [
                "git log --oneline -5",  # Verify commits
            ],
            QualityGateType.PRE_DEPLOY: [
                "git status --porcelain",  # Check clean state
            ]
        }

        commands = gate_commands.get(gate_type, [])
        if not commands:
            return True, []  # No standard gate defined, pass by default

        errors = []
        for cmd in commands:
            success, cmd_errors = self._execute_gate_command(cmd)
            if not success:
                errors.extend(cmd_errors)

        return len(errors) == 0, errors

    def _record_gate_execution(
        self,
        gate_type: QualityGateType,
        success: bool,
        checkpoint_id: Optional[str],
        execution_time: float,
        errors: List[str]
    ):
        """Record quality gate execution in history"""
        gate_name = gate_type.value

        if gate_name not in self.gate_history["gates"]:
            self.gate_history["gates"][gate_name] = {
                "executions": [],
                "success_count": 0,
                "failure_count": 0,
                "total_execution_time": 0.0
            }

        gate_data = self.gate_history["gates"][gate_name]

        # Add execution record
        gate_data["executions"].append({
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "checkpoint_id": checkpoint_id,
            "execution_time": execution_time,
            "error_count": len(errors)
        })

        # Update statistics
        if success:
            gate_data["success_count"] += 1
        else:
            gate_data["failure_count"] += 1

        gate_data["total_execution_time"] += execution_time

        # Keep only last 100 executions
        if len(gate_data["executions"]) > 100:
            gate_data["executions"] = gate_data["executions"][-100:]

        self._save_gate_history()

    def get_gate_statistics(self, gate_type: Optional[QualityGateType] = None) -> Dict:
        """
        Get quality gate statistics.

        Args:
            gate_type: Optional gate type to filter by

        Returns:
            Statistics dictionary
        """
        if gate_type:
            gate_name = gate_type.value
            if gate_name in self.gate_history["gates"]:
                data = self.gate_history["gates"][gate_name]
                return {
                    gate_name: {
                        "success_count": data["success_count"],
                        "failure_count": data["failure_count"],
                        "success_rate": data["success_count"] / (data["success_count"] + data["failure_count"]) if (data["success_count"] + data["failure_count"]) > 0 else 0.0,
                        "average_execution_time": data["total_execution_time"] / len(data["executions"]) if data["executions"] else 0.0,
                        "total_executions": len(data["executions"])
                    }
                }
            return {}

        # Return statistics for all gates
        stats = {}
        for gate_name, data in self.gate_history["gates"].items():
            total = data["success_count"] + data["failure_count"]
            stats[gate_name] = {
                "success_count": data["success_count"],
                "failure_count": data["failure_count"],
                "success_rate": data["success_count"] / total if total > 0 else 0.0,
                "average_execution_time": data["total_execution_time"] / len(data["executions"]) if data["executions"] else 0.0,
                "total_executions": len(data["executions"])
            }

        return stats

    def pre_commit_gate(self, description: Optional[str] = None) -> QualityGateResult:
        """Execute pre-commit quality gate"""
        return self.execute_quality_gate(
            gate_type=QualityGateType.PRE_COMMIT,
            description=description
        )

    def pre_push_gate(self, description: Optional[str] = None) -> QualityGateResult:
        """Execute pre-push quality gate"""
        return self.execute_quality_gate(
            gate_type=QualityGateType.PRE_PUSH,
            description=description
        )

    def pre_deploy_gate(self, description: Optional[str] = None) -> QualityGateResult:
        """Execute pre-deploy quality gate"""
        return self.execute_quality_gate(
            gate_type=QualityGateType.PRE_DEPLOY,
            description=description
        )


# CLI Interface
if __name__ == "__main__":
    from checkpoint_engine import CheckpointEngine

    # Initialize
    engine = CheckpointEngine()
    quality_gates = QualityGatesIntegration(engine)

    print("\n=== Testing Quality Gates Integration ===")

    # Test pre-commit gate
    print("\n1. Executing pre-commit quality gate")
    result = quality_gates.pre_commit_gate(description="Testing pre-commit gate")
    print(f"Result: {result.message}")
    print(f"  - Success: {result.success}")
    print(f"  - Checkpoint: {result.checkpoint_id}")
    print(f"  - Execution time: {result.execution_time_seconds:.2f}s")
    print(f"  - Errors: {len(result.errors)}")

    # Test custom gate
    print("\n2. Executing custom quality gate")
    result = quality_gates.execute_quality_gate(
        gate_type=QualityGateType.CUSTOM,
        gate_command="echo 'Running custom quality checks' && exit 0",
        description="Custom validation checks"
    )
    print(f"Result: {result.message}")

    # Get statistics
    print("\n3. Quality Gate Statistics")
    stats = quality_gates.get_gate_statistics()
    print(json.dumps(stats, indent=2))

    print("\n=== Quality Gates Integration Test Complete ===")
