#!/usr/bin/env python3
"""
User Choice Tracking System
Tracks user selections vs AI recommendations to improve personalization
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
try:
    from .project_adaptive_learning import ProjectAdaptiveLearning
except ImportError:
    from project_adaptive_learning import ProjectAdaptiveLearning


class UserChoiceTracker:
    """
    Specialized system for tracking and analyzing user choice patterns
    to improve agent recommendation accuracy.
    """

    def __init__(self, project_root: str = None):
        """Initialize user choice tracker."""
        self.learning_system = ProjectAdaptiveLearning(project_root)
        self.choices_file = self.learning_system.user_choices_file

    def record_choice(self, recommended_agents: List[str], selected_agent: str,
                     task_type: str = None, project_phase: str = None,
                     user_feedback: str = None):
        """
        Record a user choice with rich context.

        Args:
            recommended_agents: List of AI-recommended agents
            selected_agent: Agent actually chosen by user
            task_type: Type of task (development, debugging, architecture, etc.)
            project_phase: Project phase (initialization, development, maintenance)
            user_feedback: Optional user feedback about the choice
        """
        context = {
            "task_type": task_type,
            "project_phase": project_phase,
            "user_feedback": user_feedback
        }

        # Remove None values from context
        context = {k: v for k, v in context.items() if v is not None}

        self.learning_system.learn_from_user_choice(
            recommended_agents=recommended_agents,
            selected_agent=selected_agent,
            context=context
        )

    def analyze_user_patterns(self) -> Dict:
        """
        Analyze user choice patterns to understand preferences.

        Returns:
            Dict containing analysis of user behavior patterns
        """
        data = self.learning_system._read_json_file(self.choices_file)
        choices = data.get('user_choices', [])

        if not choices:
            return {"status": "No data available", "patterns": []}

        analysis = {
            "total_choices": len(choices),
            "alignment_rate": self._calculate_alignment_rate(choices),
            "preferred_agents": self._find_preferred_agents(choices),
            "rejected_agents": self._find_rejected_agents(choices),
            "context_patterns": self._analyze_context_patterns(choices),
            "learning_trends": self._analyze_learning_trends(choices)
        }

        return analysis

    def _calculate_alignment_rate(self, choices: List[Dict]) -> float:
        """Calculate how often user follows AI recommendations."""
        if not choices:
            return 0.0

        alignments = [choice.get('alignment', False) for choice in choices]
        return sum(alignments) / len(alignments)

    def _find_preferred_agents(self, choices: List[Dict]) -> Dict:
        """Find agents user prefers to select."""
        agent_counts = {}
        total_choices = len(choices)

        for choice in choices:
            selected = choice.get('selected')
            if selected:
                agent_counts[selected] = agent_counts.get(selected, 0) + 1

        # Calculate preferences as percentages
        preferences = {
            agent: {
                "count": count,
                "percentage": (count / total_choices) * 100
            }
            for agent, count in agent_counts.items()
        }

        # Sort by count
        return dict(sorted(preferences.items(), key=lambda x: x[1]['count'], reverse=True))

    def _find_rejected_agents(self, choices: List[Dict]) -> Dict:
        """Find agents user tends to reject when recommended."""
        rejection_counts = {}
        recommendation_counts = {}

        for choice in choices:
            recommended = choice.get('recommended', [])
            selected = choice.get('selected')

            for agent in recommended:
                recommendation_counts[agent] = recommendation_counts.get(agent, 0) + 1
                if agent != selected:
                    rejection_counts[agent] = rejection_counts.get(agent, 0) + 1

        # Calculate rejection rates
        rejection_rates = {}
        for agent, rejections in rejection_counts.items():
            total_recommendations = recommendation_counts.get(agent, 1)
            rejection_rate = (rejections / total_recommendations) * 100
            rejection_rates[agent] = {
                "rejections": rejections,
                "total_recommendations": total_recommendations,
                "rejection_rate": rejection_rate
            }

        # Sort by rejection rate
        return dict(sorted(rejection_rates.items(), key=lambda x: x[1]['rejection_rate'], reverse=True))

    def _analyze_context_patterns(self, choices: List[Dict]) -> Dict:
        """Analyze patterns based on task context."""
        context_patterns = {}

        for choice in choices:
            context = choice.get('context', {})
            selected = choice.get('selected')

            for context_key, context_value in context.items():
                if context_value:
                    pattern_key = f"{context_key}:{context_value}"
                    if pattern_key not in context_patterns:
                        context_patterns[pattern_key] = {}

                    agent = selected
                    if agent not in context_patterns[pattern_key]:
                        context_patterns[pattern_key][agent] = 0
                    context_patterns[pattern_key][agent] += 1

        return context_patterns

    def _analyze_learning_trends(self, choices: List[Dict]) -> Dict:
        """Analyze how user choices change over time."""
        if len(choices) < 5:  # Need sufficient data
            return {"status": "Insufficient data for trend analysis"}

        # Divide choices into early and recent periods
        mid_point = len(choices) // 2
        early_choices = choices[:mid_point]
        recent_choices = choices[mid_point:]

        early_alignment = self._calculate_alignment_rate(early_choices)
        recent_alignment = self._calculate_alignment_rate(recent_choices)

        trend = {
            "early_period": {
                "choices": len(early_choices),
                "alignment_rate": early_alignment
            },
            "recent_period": {
                "choices": len(recent_choices),
                "alignment_rate": recent_alignment
            },
            "improvement": recent_alignment - early_alignment,
            "learning_direction": "improving" if recent_alignment > early_alignment else "declining"
        }

        return trend

    def get_personalized_recommendations(self, task_type: str = None,
                                       project_phase: str = None,
                                       exclude_agents: List[str] = None) -> List[str]:
        """
        Get personalized agent recommendations based on user history.

        Args:
            task_type: Type of current task
            project_phase: Current project phase
            exclude_agents: Agents to exclude from recommendations

        Returns:
            List of recommended agents ordered by preference
        """
        # Get base recommendations from learning system
        base_recommendations = self.learning_system.get_agent_recommendations()

        # Analyze user patterns
        patterns = self.analyze_user_patterns()

        # Adjust recommendations based on user patterns
        personalized_recommendations = []

        # Start with user's most preferred agents
        preferred_agents = patterns.get('preferred_agents', {})
        for agent in sorted(preferred_agents.keys(),
                          key=lambda x: preferred_agents[x]['count'],
                          reverse=True):
            if agent not in personalized_recommendations:
                personalized_recommendations.append(agent)

        # Add base recommendations that aren't already included
        for agent in base_recommendations:
            if agent not in personalized_recommendations:
                personalized_recommendations.append(agent)

        # Remove excluded agents
        if exclude_agents:
            personalized_recommendations = [
                agent for agent in personalized_recommendations
                if agent not in exclude_agents
            ]

        # Filter by rejection patterns - remove highly rejected agents
        rejected_agents = patterns.get('rejected_agents', {})
        filtered_recommendations = []

        for agent in personalized_recommendations:
            rejection_data = rejected_agents.get(agent, {})
            rejection_rate = rejection_data.get('rejection_rate', 0)

            # Include agent if rejection rate is not too high
            if rejection_rate < 70:  # Threshold for high rejection
                filtered_recommendations.append(agent)

        return filtered_recommendations[:10]  # Return top 10 recommendations

    def get_choice_statistics(self) -> Dict:
        """Get statistical summary of user choices."""
        data = self.learning_system._read_json_file(self.choices_file)
        choices = data.get('user_choices', [])

        if not choices:
            return {"status": "No choice data available"}

        stats = {
            "total_choices": len(choices),
            "date_range": {
                "first_choice": choices[0].get('timestamp') if choices else None,
                "latest_choice": choices[-1].get('timestamp') if choices else None
            },
            "alignment_statistics": {
                "overall_alignment_rate": self._calculate_alignment_rate(choices),
                "recent_alignment_rate": self._calculate_alignment_rate(choices[-10:]) if len(choices) >= 10 else None
            },
            "choice_diversity": len(set(choice.get('selected') for choice in choices)),
            "most_recent_trends": self._get_recent_trends(choices)
        }

        return stats

    def _get_recent_trends(self, choices: List[Dict], recent_count: int = 5) -> Dict:
        """Analyze trends in most recent choices."""
        if len(choices) < recent_count:
            return {"status": f"Need at least {recent_count} choices for trend analysis"}

        recent_choices = choices[-recent_count:]

        trends = {
            "recent_agents": [choice.get('selected') for choice in recent_choices],
            "recent_alignment": self._calculate_alignment_rate(recent_choices),
            "agent_consistency": len(set(choice.get('selected') for choice in recent_choices)),
            "context_focus": self._analyze_recent_context_focus(recent_choices)
        }

        return trends

    def _analyze_recent_context_focus(self, recent_choices: List[Dict]) -> Dict:
        """Analyze what types of tasks user has been working on recently."""
        context_focus = {}

        for choice in recent_choices:
            context = choice.get('context', {})
            for key, value in context.items():
                if value:
                    focus_key = f"{key}:{value}"
                    context_focus[focus_key] = context_focus.get(focus_key, 0) + 1

        return context_focus


# Example usage and testing
if __name__ == "__main__":
    tracker = UserChoiceTracker()

    # Example: Record a user choice
    tracker.record_choice(
        recommended_agents=["frontend-engineer", "ux-designer", "api-engineer"],
        selected_agent="frontend-engineer",
        task_type="development",
        project_phase="implementation",
        user_feedback="Good recommendation"
    )

    # Analyze patterns
    patterns = tracker.analyze_user_patterns()
    print("User Patterns:", json.dumps(patterns, indent=2))

    # Get personalized recommendations
    recommendations = tracker.get_personalized_recommendations(
        task_type="development",
        project_phase="implementation"
    )
    print("Personalized Recommendations:", recommendations)