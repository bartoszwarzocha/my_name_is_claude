#!/usr/bin/env python3
"""
Learning System Integration
Integrates adaptive learning with existing AI agent selection system
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path to import from core modules
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

# Try relative imports first, fall back to direct imports
try:
    from .project_adaptive_learning import ProjectAdaptiveLearning
    from .user_choice_tracker import UserChoiceTracker
    from .agent_effectiveness_monitor import AgentEffectivenessMonitor
    from .incremental_model_updater import IncrementalModelUpdater
except ImportError:
    from project_adaptive_learning import ProjectAdaptiveLearning
    from user_choice_tracker import UserChoiceTracker
    from agent_effectiveness_monitor import AgentEffectivenessMonitor
    from incremental_model_updater import IncrementalModelUpdater


class AdaptiveLearningIntegration:
    """
    Integration layer that enhances existing AI agent selection
    with project-specific adaptive learning capabilities.
    """

    def __init__(self, project_root: str = None):
        """Initialize the adaptive learning integration."""
        self.project_root = project_root or self._find_project_root()

        # Initialize all learning components
        self.learning_system = ProjectAdaptiveLearning(self.project_root)
        self.choice_tracker = UserChoiceTracker(self.project_root)
        self.effectiveness_monitor = AgentEffectivenessMonitor(self.project_root)
        self.model_updater = IncrementalModelUpdater(self.project_root)

        # Check if learning system is ready
        self.learning_enabled = self._check_learning_readiness()

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def _check_learning_readiness(self) -> bool:
        """Check if learning system has sufficient data to operate."""
        model_status = self.model_updater.get_model_status()
        return model_status.get('learning_data_available', {}).get('ready_for_learning', False)

    def enhance_agent_recommendations(self, base_recommendations: list,
                                    context: dict = None) -> list:
        """
        Enhance base AI recommendations with learned preferences.

        Args:
            base_recommendations: Original AI recommendations
            context: Current task context

        Returns:
            Enhanced recommendations list
        """
        if not self.learning_enabled:
            return base_recommendations

        try:
            # Get personalized recommendations
            personalized = self.model_updater.get_personalized_recommendations(
                agents=base_recommendations,
                context=context,
                top_k=len(base_recommendations)
            )

            # Extract agent names in order of personalized preference
            enhanced_recommendations = [agent for agent, score in personalized]

            # Add any base recommendations that weren't in personalized results
            for agent in base_recommendations:
                if agent not in enhanced_recommendations:
                    enhanced_recommendations.append(agent)

            return enhanced_recommendations

        except Exception as e:
            print(f"Warning: Error in adaptive learning enhancement: {e}")
            return base_recommendations

    def record_user_selection(self, recommended_agents: list, selected_agent: str,
                             task_type: str = None, project_phase: str = None):
        """
        Record user selection for learning.

        Args:
            recommended_agents: List of agents that were recommended
            selected_agent: Agent that user actually selected
            task_type: Type of task being performed
            project_phase: Current project phase
        """
        try:
            self.choice_tracker.record_choice(
                recommended_agents=recommended_agents,
                selected_agent=selected_agent,
                task_type=task_type,
                project_phase=project_phase
            )

            # Update model if enough new data is available
            self.model_updater.update_model()

            # Enable learning if we now have enough data
            if not self.learning_enabled:
                self.learning_enabled = self._check_learning_readiness()

        except Exception as e:
            print(f"Warning: Error recording user selection: {e}")

    def record_task_outcome(self, agent_name: str, task_type: str,
                           success: bool, completion_time: float = None,
                           quality_score: float = None):
        """
        Record task outcome for effectiveness tracking.

        Args:
            agent_name: Name of agent used
            task_type: Type of task performed
            success: Whether task was successful
            completion_time: Time taken (in minutes)
            quality_score: Quality score (0-1)
        """
        try:
            self.effectiveness_monitor.record_agent_usage(
                agent_name=agent_name,
                task_type=task_type,
                success=success,
                completion_time=completion_time,
                quality_score=quality_score
            )

            # Update model after recording effectiveness data
            self.model_updater.update_model()

        except Exception as e:
            print(f"Warning: Error recording task outcome: {e}")

    def get_learning_status(self) -> dict:
        """Get comprehensive status of the learning system."""
        try:
            return {
                "learning_enabled": self.learning_enabled,
                "project_id": self.learning_system.project_id,
                "choice_statistics": self.choice_tracker.get_choice_statistics(),
                "effectiveness_summary": self.effectiveness_monitor.get_effectiveness_summary(),
                "model_status": self.model_updater.get_model_status()
            }
        except Exception as e:
            return {
                "error": f"Error getting learning status: {e}",
                "learning_enabled": False
            }

    def get_agent_insights(self, agent_name: str) -> dict:
        """Get detailed insights for specific agent."""
        try:
            return {
                "performance": self.effectiveness_monitor.get_agent_performance(agent_name),
                "user_preference": self._get_user_preference_for_agent(agent_name)
            }
        except Exception as e:
            return {"error": f"Error getting agent insights: {e}"}

    def _get_user_preference_for_agent(self, agent_name: str) -> dict:
        """Get user preference data for specific agent."""
        patterns = self.choice_tracker.analyze_user_patterns()

        preferred = patterns.get('preferred_agents', {}).get(agent_name, {})
        rejected = patterns.get('rejected_agents', {}).get(agent_name, {})

        return {
            "preference_data": preferred,
            "rejection_data": rejected,
            "overall_sentiment": "preferred" if preferred else ("rejected" if rejected else "neutral")
        }

    def export_learning_data(self) -> dict:
        """Export anonymized learning data for analysis."""
        try:
            return {
                "project_metadata": {
                    "project_id": self.learning_system.project_id,
                    "learning_enabled": self.learning_enabled
                },
                "anonymized_patterns": {
                    "user_choice_patterns": self._anonymize_choice_patterns(),
                    "agent_effectiveness_patterns": self._anonymize_effectiveness_patterns(),
                    "context_patterns": self._anonymize_context_patterns()
                },
                "model_insights": {
                    "weights_summary": self.model_updater._get_weights_summary(),
                    "learning_accuracy": self._calculate_overall_learning_accuracy()
                }
            }
        except Exception as e:
            return {"error": f"Error exporting learning data: {e}"}

    def _anonymize_choice_patterns(self) -> dict:
        """Create anonymized version of choice patterns."""
        patterns = self.choice_tracker.analyze_user_patterns()

        # Remove specific agent names, keep only pattern structure
        anonymized = {
            "total_choices": patterns.get('total_choices', 0),
            "alignment_rate": patterns.get('alignment_rate', 0),
            "preference_distribution": len(patterns.get('preferred_agents', {})),
            "rejection_distribution": len(patterns.get('rejected_agents', {}))
        }

        return anonymized

    def _anonymize_effectiveness_patterns(self) -> dict:
        """Create anonymized version of effectiveness patterns."""
        summary = self.effectiveness_monitor.get_effectiveness_summary()

        return {
            "total_agents_tracked": summary.get('total_tracked_agents', 0),
            "total_tasks_monitored": summary.get('total_tasks_monitored', 0),
            "overall_success_rate": summary.get('overall_success_rate', 0)
        }

    def _anonymize_context_patterns(self) -> dict:
        """Create anonymized version of context patterns."""
        # Get context patterns without revealing specific project details
        patterns = self.choice_tracker.analyze_user_patterns()
        context_patterns = patterns.get('context_patterns', {})

        anonymized = {
            "total_context_types": len(context_patterns),
            "context_diversity": sum(len(agents) for agents in context_patterns.values())
        }

        return anonymized

    def _calculate_overall_learning_accuracy(self) -> float:
        """Calculate overall learning system accuracy."""
        try:
            choice_stats = self.choice_tracker.get_choice_statistics()
            alignment_stats = choice_stats.get('alignment_statistics', {})
            return alignment_stats.get('overall_alignment_rate', 0.0)
        except:
            return 0.0

    def suggest_improvements(self) -> list:
        """Suggest improvements based on learning data analysis."""
        suggestions = []

        try:
            # Analyze current state
            status = self.get_learning_status()

            if not status.get('learning_enabled'):
                suggestions.append({
                    "type": "data_collection",
                    "message": "Continue using the system to collect learning data",
                    "priority": "high"
                })

            # Check alignment rate
            choice_stats = status.get('choice_statistics', {})
            alignment_stats = choice_stats.get('alignment_statistics', {})
            alignment_rate = alignment_stats.get('overall_alignment_rate', 0)

            if alignment_rate < 0.6:
                suggestions.append({
                    "type": "recommendation_accuracy",
                    "message": "Low alignment rate - system is still learning your preferences",
                    "priority": "medium"
                })
            elif alignment_rate > 0.8:
                suggestions.append({
                    "type": "system_performance",
                    "message": "High alignment rate - system has learned your preferences well",
                    "priority": "info"
                })

            # Check agent usage diversity
            effectiveness_summary = status.get('effectiveness_summary', {})
            agents_tracked = effectiveness_summary.get('total_tracked_agents', 0)

            if agents_tracked < 3:
                suggestions.append({
                    "type": "agent_diversity",
                    "message": "Try using different agent types to improve learning coverage",
                    "priority": "medium"
                })

        except Exception as e:
            suggestions.append({
                "type": "error",
                "message": f"Error analyzing system: {e}",
                "priority": "low"
            })

        return suggestions


# Utility function for easy integration
def create_learning_integration(project_root: str = None) -> AdaptiveLearningIntegration:
    """Create and return learning integration instance."""
    return AdaptiveLearningIntegration(project_root)


if __name__ == "__main__":
    # Demo usage
    integration = create_learning_integration()

    print("Learning System Status:")
    status = integration.get_learning_status()
    print(f"Learning Enabled: {status.get('learning_enabled')}")
    print(f"Project ID: {status.get('project_id')}")

    suggestions = integration.suggest_improvements()
    print(f"\\nSuggestions: {len(suggestions)}")
    for suggestion in suggestions:
        print(f"- {suggestion['type']}: {suggestion['message']}")