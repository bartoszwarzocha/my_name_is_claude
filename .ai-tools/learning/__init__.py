"""
AI Tools Learning System
Project-adaptive learning for single-project deployments
"""

from .project_adaptive_learning import ProjectAdaptiveLearning
from .user_choice_tracker import UserChoiceTracker
from .agent_effectiveness_monitor import AgentEffectivenessMonitor
from .incremental_model_updater import IncrementalModelUpdater

__version__ = "1.0.0"
__author__ = "Claude Code Multi-Agent Framework"

# Main learning system components
__all__ = [
    "ProjectAdaptiveLearning",
    "UserChoiceTracker",
    "AgentEffectivenessMonitor",
    "IncrementalModelUpdater"
]