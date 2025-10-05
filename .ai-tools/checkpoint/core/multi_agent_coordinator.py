#!/usr/bin/env python3
"""
Multi-Agent Checkpoint Coordinator for Claude Code Multi-Agent Framework

Manages checkpoint coordination across multiple agents working in parallel.
Ensures safe parallel execution with conflict detection and resolution.

Part of Framework v3.7.0 - Advanced Checkpoint System

Features:
- Per-agent checkpoint isolation
- Parallel agent execution safety
- Conflict detection and resolution
- Agent state synchronization
- Coordinated rollback across agents
"""

import json
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from pathlib import Path
from datetime import datetime
from enum import Enum

from .checkpoint_engine import CheckpointEngine, CheckpointLevel, CheckpointMetadata

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConflictResolutionStrategy(Enum):
    """Conflict resolution strategies"""
    INTERACTIVE = "interactive"
    AUTO_MERGE = "auto_merge"
    MANUAL = "manual"
    ABORT = "abort"


@dataclass
class AgentCheckpointState:
    """State of checkpoints for a specific agent"""
    agent_type: str
    active_checkpoints: List[str] = field(default_factory=list)
    last_checkpoint_id: Optional[str] = None
    last_checkpoint_timestamp: Optional[str] = None
    modified_files: Set[str] = field(default_factory=set)
    execution_count: int = 0


@dataclass
class ConflictInfo:
    """Information about a detected conflict"""
    conflict_type: str
    agents_involved: List[str]
    conflicting_files: List[str]
    description: str
    severity: str  # "low", "medium", "high", "critical"


class MultiAgentCoordinator:
    """
    Coordinates checkpoint operations across multiple agents.

    Features:
    - Track per-agent checkpoint state
    - Detect conflicts between agents
    - Coordinate parallel execution
    - Manage agent isolation
    """

    def __init__(self, checkpoint_engine: CheckpointEngine, config: Optional[Dict] = None):
        """
        Initialize multi-agent coordinator.

        Args:
            checkpoint_engine: CheckpointEngine instance
            config: Optional configuration override
        """
        self.checkpoint_engine = checkpoint_engine
        self.config = config or checkpoint_engine.config.get("multiAgentCoordination", {})

        # Agent state tracking
        self.agent_states: Dict[str, AgentCheckpointState] = {}

        # Conflict tracking
        self.detected_conflicts: List[ConflictInfo] = []

        # Coordination lock (file-based for simplicity)
        self.coordination_file = checkpoint_engine.storage_base / "agent_coordination.json"

        # Load coordination state
        self._load_coordination_state()

        logger.info("Multi-Agent Coordinator initialized")

    def _load_coordination_state(self):
        """Load coordination state from storage"""
        if self.coordination_file.exists():
            try:
                with open(self.coordination_file, 'r') as f:
                    data = json.load(f)

                # Restore agent states
                for agent_type, state_data in data.get("agent_states", {}).items():
                    self.agent_states[agent_type] = AgentCheckpointState(
                        agent_type=agent_type,
                        active_checkpoints=state_data.get("active_checkpoints", []),
                        last_checkpoint_id=state_data.get("last_checkpoint_id"),
                        last_checkpoint_timestamp=state_data.get("last_checkpoint_timestamp"),
                        modified_files=set(state_data.get("modified_files", [])),
                        execution_count=state_data.get("execution_count", 0)
                    )

            except Exception as e:
                logger.warning(f"Error loading coordination state: {e}")

    def _save_coordination_state(self):
        """Save coordination state to storage"""
        try:
            data = {
                "version": "3.7.0",
                "last_updated": datetime.now().isoformat(),
                "agent_states": {}
            }

            # Serialize agent states
            for agent_type, state in self.agent_states.items():
                data["agent_states"][agent_type] = {
                    "active_checkpoints": state.active_checkpoints,
                    "last_checkpoint_id": state.last_checkpoint_id,
                    "last_checkpoint_timestamp": state.last_checkpoint_timestamp,
                    "modified_files": list(state.modified_files),
                    "execution_count": state.execution_count
                }

            with open(self.coordination_file, 'w') as f:
                json.dump(data, f, indent=2)

        except Exception as e:
            logger.error(f"Error saving coordination state: {e}")

    def pre_agent_execution_checkpoint(
        self,
        agent_type: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> Optional[str]:
        """
        Create checkpoint before agent execution.

        Args:
            agent_type: Type of agent about to execute
            description: Optional description
            tags: Optional tags

        Returns:
            Checkpoint ID if successful
        """
        if not self.config.get("enabled", True):
            return None

        logger.info(f"Creating pre-execution checkpoint for {agent_type}")

        # Check for conflicts with other agents
        if self.config.get("parallel_agent_safety", True):
            conflicts = self._detect_conflicts(agent_type)
            if conflicts:
                logger.warning(f"Detected {len(conflicts)} conflicts before {agent_type} execution")
                self.detected_conflicts.extend(conflicts)

                # Handle conflicts based on strategy
                if not self._resolve_conflicts(conflicts):
                    logger.error(f"Could not resolve conflicts for {agent_type}")
                    return None

        # Create checkpoint
        checkpoint_id = self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.AGENT_EXECUTION,
            label=f"before_{agent_type}_{datetime.now().strftime('%H%M%S')}",
            description=description or f"Before {agent_type} execution",
            agent_type=agent_type,
            tags=(tags or []) + ["pre-agent", agent_type]
        )

        if checkpoint_id:
            # Update agent state
            self._update_agent_state(
                agent_type,
                checkpoint_id=checkpoint_id,
                execution_count=self.agent_states.get(agent_type, AgentCheckpointState(agent_type)).execution_count + 1
            )

        return checkpoint_id

    def post_agent_execution_checkpoint(
        self,
        agent_type: str,
        success: bool = True,
        modified_files: Optional[List[str]] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> Optional[str]:
        """
        Create checkpoint after agent execution.

        Args:
            agent_type: Type of agent that executed
            success: Whether execution was successful
            modified_files: Files modified during execution
            description: Optional description
            tags: Optional tags

        Returns:
            Checkpoint ID if successful
        """
        if not self.config.get("enabled", True):
            return None

        status = "success" if success else "failure"
        logger.info(f"Creating post-execution checkpoint for {agent_type} ({status})")

        # Create checkpoint
        checkpoint_id = self.checkpoint_engine.create_checkpoint(
            level=CheckpointLevel.AGENT_EXECUTION,
            label=f"after_{agent_type}_{status}_{datetime.now().strftime('%H%M%S')}",
            description=description or f"After {agent_type} execution ({status})",
            agent_type=agent_type,
            tags=(tags or []) + ["post-agent", agent_type, status]
        )

        if checkpoint_id:
            # Update agent state with modified files
            self._update_agent_state(
                agent_type,
                checkpoint_id=checkpoint_id,
                modified_files=set(modified_files or [])
            )

        return checkpoint_id

    def _update_agent_state(
        self,
        agent_type: str,
        checkpoint_id: Optional[str] = None,
        modified_files: Optional[Set[str]] = None,
        execution_count: Optional[int] = None
    ):
        """Update agent state tracking"""
        if agent_type not in self.agent_states:
            self.agent_states[agent_type] = AgentCheckpointState(agent_type=agent_type)

        state = self.agent_states[agent_type]

        if checkpoint_id:
            state.active_checkpoints.append(checkpoint_id)
            state.last_checkpoint_id = checkpoint_id
            state.last_checkpoint_timestamp = datetime.now().isoformat()

        if modified_files is not None:
            state.modified_files.update(modified_files)

        if execution_count is not None:
            state.execution_count = execution_count

        self._save_coordination_state()

    def _detect_conflicts(self, agent_type: str) -> List[ConflictInfo]:
        """
        Detect conflicts with other agents.

        Args:
            agent_type: Agent type to check conflicts for

        Returns:
            List of detected conflicts
        """
        if not self.config.get("conflict_detection", {}).get("enabled", True):
            return []

        conflicts = []

        # Get modified files for this agent (predicted or known)
        current_agent_files = self.agent_states.get(agent_type, AgentCheckpointState(agent_type)).modified_files

        # Check against other active agents
        for other_agent_type, other_state in self.agent_states.items():
            if other_agent_type == agent_type:
                continue

            # Check for file conflicts
            if self.config.get("agent_isolation", True):
                overlapping_files = current_agent_files.intersection(other_state.modified_files)

                if overlapping_files:
                    conflicts.append(ConflictInfo(
                        conflict_type="file_overlap",
                        agents_involved=[agent_type, other_agent_type],
                        conflicting_files=list(overlapping_files),
                        description=f"{agent_type} and {other_agent_type} are modifying the same files",
                        severity="medium"
                    ))

        return conflicts

    def _resolve_conflicts(self, conflicts: List[ConflictInfo]) -> bool:
        """
        Resolve detected conflicts.

        Args:
            conflicts: List of conflicts to resolve

        Returns:
            True if conflicts resolved, False otherwise
        """
        strategy = ConflictResolutionStrategy(
            self.config.get("conflict_detection", {}).get("conflict_resolution", "interactive")
        )

        if strategy == ConflictResolutionStrategy.AUTO_MERGE:
            # Auto-merge if enabled
            if not self.config.get("conflict_detection", {}).get("auto_merge", False):
                logger.warning("Auto-merge disabled, conflicts remain unresolved")
                return False

            logger.info(f"Auto-merging {len(conflicts)} conflicts")
            # TODO: Implement auto-merge logic
            return True

        elif strategy == ConflictResolutionStrategy.MANUAL:
            # Require manual resolution
            logger.warning(f"Manual conflict resolution required for {len(conflicts)} conflicts")
            if self.config.get("conflict_detection", {}).get("require_manual_resolution", True):
                return False
            return True

        elif strategy == ConflictResolutionStrategy.INTERACTIVE:
            # Interactive resolution (default)
            logger.info(f"Interactive conflict resolution for {len(conflicts)} conflicts")
            # For now, log and allow with warning
            return True

        elif strategy == ConflictResolutionStrategy.ABORT:
            # Abort on any conflict
            logger.error(f"Aborting due to {len(conflicts)} conflicts")
            return False

        return False

    def get_agent_checkpoint_history(self, agent_type: str, limit: int = 10) -> List[CheckpointMetadata]:
        """
        Get checkpoint history for a specific agent.

        Args:
            agent_type: Agent type to get history for
            limit: Maximum number of checkpoints

        Returns:
            List of checkpoint metadata
        """
        agent_state = self.agent_states.get(agent_type)
        if not agent_state:
            return []

        checkpoints = []
        for cp_id in agent_state.active_checkpoints[-limit:]:
            metadata = self.checkpoint_engine.get_checkpoint_metadata(cp_id)
            if metadata:
                checkpoints.append(metadata)

        return checkpoints

    def coordinated_rollback(
        self,
        target_checkpoint_id: str,
        affected_agents: Optional[List[str]] = None
    ) -> Dict[str, bool]:
        """
        Perform coordinated rollback across multiple agents.

        Args:
            target_checkpoint_id: Target checkpoint to rollback to
            affected_agents: Optional list of agents to rollback (None = all)

        Returns:
            Dictionary mapping agent_type to rollback success status
        """
        logger.info(f"Coordinated rollback to {target_checkpoint_id}")

        # Get target checkpoint metadata
        target_metadata = self.checkpoint_engine.get_checkpoint_metadata(target_checkpoint_id)
        if not target_metadata:
            logger.error(f"Target checkpoint not found: {target_checkpoint_id}")
            return {}

        # Determine affected agents
        agents = affected_agents or list(self.agent_states.keys())

        results = {}
        for agent_type in agents:
            # Rollback for each agent
            result = self.checkpoint_engine.rollback_to_checkpoint(target_checkpoint_id)
            results[agent_type] = result.success

            if result.success:
                logger.info(f"✅ Rolled back {agent_type} to {target_checkpoint_id}")
            else:
                logger.error(f"❌ Failed to rollback {agent_type}: {result.message}")

        return results

    def get_coordination_status(self) -> Dict:
        """Get current coordination status"""
        return {
            "active_agents": len(self.agent_states),
            "total_checkpoints": sum(len(state.active_checkpoints) for state in self.agent_states.values()),
            "detected_conflicts": len(self.detected_conflicts),
            "agent_states": {
                agent_type: {
                    "execution_count": state.execution_count,
                    "last_checkpoint": state.last_checkpoint_id,
                    "modified_files_count": len(state.modified_files)
                }
                for agent_type, state in self.agent_states.items()
            }
        }


# CLI Interface
if __name__ == "__main__":
    from checkpoint_engine import CheckpointEngine

    # Initialize
    engine = CheckpointEngine()
    coordinator = MultiAgentCoordinator(engine)

    print("\n=== Testing Multi-Agent Coordination ===")

    # Test pre-agent checkpoint
    print("\n1. Creating pre-agent checkpoint for backend-engineer")
    cp_id_1 = coordinator.pre_agent_execution_checkpoint(
        agent_type="backend-engineer",
        description="Testing backend agent execution"
    )
    print(f"Created: {cp_id_1}")

    # Test post-agent checkpoint
    print("\n2. Creating post-agent checkpoint for backend-engineer")
    cp_id_2 = coordinator.post_agent_execution_checkpoint(
        agent_type="backend-engineer",
        success=True,
        modified_files=["src/api/auth.py", "src/models/user.py"]
    )
    print(f"Created: {cp_id_2}")

    # Test another agent
    print("\n3. Creating checkpoint for frontend-engineer")
    cp_id_3 = coordinator.pre_agent_execution_checkpoint(
        agent_type="frontend-engineer",
        description="Testing frontend agent execution"
    )
    print(f"Created: {cp_id_3}")

    # Get coordination status
    print("\n4. Coordination Status")
    status = coordinator.get_coordination_status()
    print(json.dumps(status, indent=2))

    print("\n=== Multi-Agent Coordinator Test Complete ===")
