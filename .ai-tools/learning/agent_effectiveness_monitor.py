#!/usr/bin/env python3
"""
Agent Effectiveness Monitoring System
Tracks agent performance and success rates in project context
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
try:
    from .project_adaptive_learning import ProjectAdaptiveLearning
except ImportError:
    from project_adaptive_learning import ProjectAdaptiveLearning


class AgentEffectivenessMonitor:
    """
    System for monitoring and analyzing agent effectiveness
    in specific project contexts.
    """

    def __init__(self, project_root: str = None):
        """Initialize agent effectiveness monitor."""
        self.learning_system = ProjectAdaptiveLearning(project_root)
        self.effectiveness_file = self.learning_system.effectiveness_file

    def record_agent_usage(self, agent_name: str, task_type: str,
                          success: bool, task_details: Dict = None,
                          completion_time: float = None,
                          quality_score: float = None):
        """
        Record agent usage with detailed success metrics.

        Args:
            agent_name: Name of the agent used
            task_type: Type of task performed
            success: Whether the task was successful
            task_details: Additional details about the task
            completion_time: Time taken to complete task (in minutes)
            quality_score: Quality score (0-1) if available
        """
        context = {
            "task_type": task_type,
            "completion_time": completion_time,
            "quality_score": quality_score,
            "task_details": task_details or {}
        }

        # Remove None values
        context = {k: v for k, v in context.items() if v is not None}

        self.learning_system.update_agent_effectiveness(
            agent_name=agent_name,
            task_success=success,
            task_context=context
        )

    def get_agent_performance(self, agent_name: str) -> Dict:
        """
        Get comprehensive performance metrics for specific agent.

        Args:
            agent_name: Name of the agent to analyze

        Returns:
            Dict containing detailed performance metrics
        """
        data = self.learning_system._read_json_file(self.effectiveness_file)
        agent_metrics = data.get('agent_metrics', {})

        if agent_name not in agent_metrics:
            return {
                "status": "No data available",
                "agent": agent_name
            }

        metrics = agent_metrics[agent_name]
        contexts = metrics.get('contexts', [])

        performance = {
            "agent_name": agent_name,
            "overall_metrics": {
                "total_uses": metrics.get('total_uses', 0),
                "successes": metrics.get('successes', 0),
                "failures": metrics.get('failures', 0),
                "success_rate": metrics.get('success_rate', 0.0),
                "first_used": metrics.get('first_used'),
                "last_used": metrics.get('last_used')
            },
            "performance_by_task_type": self._analyze_performance_by_task_type(contexts),
            "quality_metrics": self._analyze_quality_metrics(contexts),
            "efficiency_metrics": self._analyze_efficiency_metrics(contexts),
            "recent_performance": self._analyze_recent_performance(contexts),
            "improvement_trends": self._analyze_improvement_trends(contexts)
        }

        return performance

    def _analyze_performance_by_task_type(self, contexts: List[Dict]) -> Dict:
        """Analyze agent performance broken down by task type."""
        task_performance = {}

        for context in contexts:
            task_type = context.get('task_type', 'unknown')
            success = context.get('success', False)

            if task_type not in task_performance:
                task_performance[task_type] = {
                    'total': 0,
                    'successes': 0,
                    'success_rate': 0.0
                }

            task_performance[task_type]['total'] += 1
            if success:
                task_performance[task_type]['successes'] += 1

            # Calculate success rate
            task_performance[task_type]['success_rate'] = (
                task_performance[task_type]['successes'] /
                task_performance[task_type]['total']
            )

        return task_performance

    def _analyze_quality_metrics(self, contexts: List[Dict]) -> Dict:
        """Analyze quality scores if available."""
        quality_scores = [
            context.get('quality_score')
            for context in contexts
            if context.get('quality_score') is not None
        ]

        if not quality_scores:
            return {"status": "No quality data available"}

        return {
            "average_quality": sum(quality_scores) / len(quality_scores),
            "min_quality": min(quality_scores),
            "max_quality": max(quality_scores),
            "quality_samples": len(quality_scores),
            "quality_trend": self._calculate_quality_trend(contexts)
        }

    def _analyze_efficiency_metrics(self, contexts: List[Dict]) -> Dict:
        """Analyze completion time efficiency."""
        completion_times = [
            context.get('completion_time')
            for context in contexts
            if context.get('completion_time') is not None
        ]

        if not completion_times:
            return {"status": "No timing data available"}

        return {
            "average_completion_time": sum(completion_times) / len(completion_times),
            "min_completion_time": min(completion_times),
            "max_completion_time": max(completion_times),
            "timing_samples": len(completion_times),
            "efficiency_trend": self._calculate_efficiency_trend(contexts)
        }

    def _analyze_recent_performance(self, contexts: List[Dict], days: int = 7) -> Dict:
        """Analyze performance in recent period."""
        cutoff_date = datetime.now() - timedelta(days=days)

        recent_contexts = [
            context for context in contexts
            if self._parse_timestamp(context.get('timestamp')) > cutoff_date
        ]

        if not recent_contexts:
            return {"status": f"No data from last {days} days"}

        successes = sum(1 for context in recent_contexts if context.get('success', False))
        total = len(recent_contexts)

        return {
            "period_days": days,
            "recent_uses": total,
            "recent_successes": successes,
            "recent_success_rate": successes / total if total > 0 else 0,
            "activity_level": "high" if total >= days else "low"
        }

    def _analyze_improvement_trends(self, contexts: List[Dict]) -> Dict:
        """Analyze whether agent performance is improving over time."""
        if len(contexts) < 10:  # Need sufficient data
            return {"status": "Insufficient data for trend analysis"}

        # Sort by timestamp
        sorted_contexts = sorted(
            contexts,
            key=lambda x: self._parse_timestamp(x.get('timestamp'))
        )

        # Split into early and recent periods
        mid_point = len(sorted_contexts) // 2
        early_contexts = sorted_contexts[:mid_point]
        recent_contexts = sorted_contexts[mid_point:]

        early_success_rate = sum(1 for c in early_contexts if c.get('success', False)) / len(early_contexts)
        recent_success_rate = sum(1 for c in recent_contexts if c.get('success', False)) / len(recent_contexts)

        improvement = recent_success_rate - early_success_rate

        return {
            "early_period": {
                "tasks": len(early_contexts),
                "success_rate": early_success_rate
            },
            "recent_period": {
                "tasks": len(recent_contexts),
                "success_rate": recent_success_rate
            },
            "improvement": improvement,
            "trend": "improving" if improvement > 0.1 else ("declining" if improvement < -0.1 else "stable")
        }

    def _calculate_quality_trend(self, contexts: List[Dict]) -> str:
        """Calculate trend in quality scores."""
        quality_contexts = [
            context for context in contexts
            if context.get('quality_score') is not None
        ]

        if len(quality_contexts) < 5:
            return "insufficient_data"

        # Sort by timestamp
        sorted_contexts = sorted(
            quality_contexts,
            key=lambda x: self._parse_timestamp(x.get('timestamp'))
        )

        # Compare early vs recent quality
        mid_point = len(sorted_contexts) // 2
        early_quality = sum(c.get('quality_score', 0) for c in sorted_contexts[:mid_point]) / mid_point
        recent_quality = sum(c.get('quality_score', 0) for c in sorted_contexts[mid_point:]) / (len(sorted_contexts) - mid_point)

        improvement = recent_quality - early_quality

        if improvement > 0.1:
            return "improving"
        elif improvement < -0.1:
            return "declining"
        else:
            return "stable"

    def _calculate_efficiency_trend(self, contexts: List[Dict]) -> str:
        """Calculate trend in completion times (lower is better)."""
        timing_contexts = [
            context for context in contexts
            if context.get('completion_time') is not None
        ]

        if len(timing_contexts) < 5:
            return "insufficient_data"

        # Sort by timestamp
        sorted_contexts = sorted(
            timing_contexts,
            key=lambda x: self._parse_timestamp(x.get('timestamp'))
        )

        # Compare early vs recent completion times
        mid_point = len(sorted_contexts) // 2
        early_time = sum(c.get('completion_time', 0) for c in sorted_contexts[:mid_point]) / mid_point
        recent_time = sum(c.get('completion_time', 0) for c in sorted_contexts[mid_point:]) / (len(sorted_contexts) - mid_point)

        # For efficiency, lower completion time is better
        improvement = early_time - recent_time

        if improvement > 5:  # 5 minutes improvement
            return "improving"
        elif improvement < -5:  # 5 minutes worse
            return "declining"
        else:
            return "stable"

    def _parse_timestamp(self, timestamp_str: str) -> datetime:
        """Parse ISO format timestamp string."""
        if not timestamp_str:
            return datetime.min

        try:
            return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        except ValueError:
            return datetime.min

    def get_all_agents_ranking(self, task_type: str = None) -> List[Tuple[str, Dict]]:
        """
        Get ranking of all agents by effectiveness.

        Args:
            task_type: Optional filter by task type

        Returns:
            List of tuples (agent_name, metrics) sorted by effectiveness
        """
        data = self.learning_system._read_json_file(self.effectiveness_file)
        agent_metrics = data.get('agent_metrics', {})

        ranked_agents = []

        for agent_name, metrics in agent_metrics.items():
            # Filter by task type if specified
            if task_type:
                contexts = metrics.get('contexts', [])
                task_contexts = [c for c in contexts if c.get('task_type') == task_type]

                if not task_contexts:
                    continue

                # Recalculate metrics for this task type
                successes = sum(1 for c in task_contexts if c.get('success', False))
                total = len(task_contexts)
                success_rate = successes / total if total > 0 else 0

                task_metrics = {
                    "total_uses": total,
                    "success_rate": success_rate,
                    "successes": successes,
                    "task_type": task_type
                }
            else:
                task_metrics = metrics

            # Calculate effectiveness score
            effectiveness_score = self._calculate_effectiveness_score(task_metrics)

            ranked_agents.append((agent_name, {
                "effectiveness_score": effectiveness_score,
                "metrics": task_metrics
            }))

        # Sort by effectiveness score
        ranked_agents.sort(key=lambda x: x[1]["effectiveness_score"], reverse=True)

        return ranked_agents

    def _calculate_effectiveness_score(self, metrics: Dict) -> float:
        """Calculate overall effectiveness score for ranking."""
        success_rate = metrics.get('success_rate', 0)
        total_uses = metrics.get('total_uses', 0)

        # Base score from success rate
        score = success_rate

        # Boost score based on usage frequency (more data = more reliable)
        reliability_factor = min(total_uses / 10, 1)  # Cap at 1.0
        score += reliability_factor * 0.2  # Up to 0.2 bonus

        # Penalize agents with very low usage
        if total_uses < 3:
            score *= 0.5

        return score

    def get_effectiveness_summary(self) -> Dict:
        """Get summary of all agent effectiveness data."""
        data = self.learning_system._read_json_file(self.effectiveness_file)
        agent_metrics = data.get('agent_metrics', {})

        if not agent_metrics:
            return {"status": "No effectiveness data available"}

        total_agents = len(agent_metrics)
        total_tasks = sum(metrics.get('total_uses', 0) for metrics in agent_metrics.values())
        total_successes = sum(metrics.get('successes', 0) for metrics in agent_metrics.values())

        # Find best and worst performing agents
        rankings = self.get_all_agents_ranking()
        best_agent = rankings[0] if rankings else None
        worst_agent = rankings[-1] if rankings else None

        summary = {
            "total_tracked_agents": total_agents,
            "total_tasks_monitored": total_tasks,
            "overall_success_rate": total_successes / total_tasks if total_tasks > 0 else 0,
            "best_performing_agent": {
                "name": best_agent[0],
                "effectiveness_score": best_agent[1]["effectiveness_score"]
            } if best_agent else None,
            "worst_performing_agent": {
                "name": worst_agent[0],
                "effectiveness_score": worst_agent[1]["effectiveness_score"]
            } if worst_agent else None,
            "agents_by_usage": sorted(
                [(name, metrics.get('total_uses', 0))
                 for name, metrics in agent_metrics.items()],
                key=lambda x: x[1], reverse=True
            )[:5]  # Top 5 most used agents
        }

        return summary


# Example usage and testing
if __name__ == "__main__":
    monitor = AgentEffectivenessMonitor()

    # Example: Record agent usage
    monitor.record_agent_usage(
        agent_name="frontend-engineer",
        task_type="development",
        success=True,
        task_details={"component": "user-interface", "complexity": "medium"},
        completion_time=45.0,
        quality_score=0.85
    )

    # Get agent performance
    performance = monitor.get_agent_performance("frontend-engineer")
    print("Agent Performance:", json.dumps(performance, indent=2))

    # Get rankings
    rankings = monitor.get_all_agents_ranking()
    print("Agent Rankings:", [(name, metrics["effectiveness_score"]) for name, metrics in rankings[:5]])

    # Get summary
    summary = monitor.get_effectiveness_summary()
    print("Effectiveness Summary:", json.dumps(summary, indent=2))