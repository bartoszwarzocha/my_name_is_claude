#!/usr/bin/env python3
"""
Project Adaptive Learning System
Implementation of local learning for single-project deployments
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
import uuid


class ProjectAdaptiveLearning:
    """
    Core system for project-specific learning that adapts to user behavior
    and project evolution without requiring cross-project data.
    """

    def __init__(self, project_root: str = None):
        """Initialize the adaptive learning system."""
        if project_root is None:
            project_root = self._find_project_root()

        self.project_root = Path(project_root)
        self.learning_dir = self.project_root / ".ai-tools" / "learning"
        self.data_dir = self.learning_dir / "data"
        self.models_dir = self.learning_dir / "models"
        self.analytics_dir = self.learning_dir / "analytics"

        # Initialize data files
        self.user_choices_file = self.data_dir / "user_choices.json"
        self.effectiveness_file = self.data_dir / "agent_effectiveness.json"
        self.evolution_file = self.data_dir / "project_evolution.json"
        self.insights_file = self.analytics_dir / "learning_insights.json"

        # Initialize project ID
        self.project_id = self._get_or_create_project_id()

        # Initialize data files if they don't exist
        self._initialize_data_files()

    def _find_project_root(self) -> str:
        """Find the project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent

        # Fallback to current directory
        return str(Path.cwd())

    def _get_or_create_project_id(self) -> str:
        """Get or create unique project identifier."""
        project_id_file = self.learning_dir / "project_id.txt"

        if project_id_file.exists():
            return project_id_file.read_text().strip()

        project_id = str(uuid.uuid4())[:8]  # Short unique ID
        project_id_file.write_text(project_id)
        return project_id

    def _initialize_data_files(self):
        """Initialize all data files with project metadata."""
        current_time = datetime.now().isoformat()

        # Initialize user choices file
        if not self.user_choices_file.exists():
            self._write_json_file(self.user_choices_file, {
                "version": "1.0",
                "project_id": self.project_id,
                "created_at": current_time,
                "last_updated": current_time,
                "user_choices": []
            })

        # Initialize agent effectiveness file
        if not self.effectiveness_file.exists():
            self._write_json_file(self.effectiveness_file, {
                "version": "1.0",
                "project_id": self.project_id,
                "created_at": current_time,
                "last_updated": current_time,
                "agent_metrics": {}
            })

        # Initialize project evolution file
        if not self.evolution_file.exists():
            self._write_json_file(self.evolution_file, {
                "version": "1.0",
                "project_id": self.project_id,
                "created_at": current_time,
                "last_updated": current_time,
                "evolution_timeline": [],
                "technology_changes": [],
                "complexity_metrics": []
            })

        # Initialize learning insights file
        if not self.insights_file.exists():
            self._write_json_file(self.insights_file, {
                "version": "1.0",
                "project_id": self.project_id,
                "created_at": current_time,
                "last_updated": current_time,
                "learning_summary": {},
                "patterns": [],
                "recommendations": []
            })

    def _read_json_file(self, file_path: Path) -> Dict:
        """Safely read JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Error reading {file_path}: {e}")
            return {}

    def _write_json_file(self, file_path: Path, data: Dict):
        """Safely write JSON file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        data['last_updated'] = datetime.now().isoformat()

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def learn_from_user_choice(self, recommended_agents: List[str],
                             selected_agent: str, context: Dict = None):
        """
        Learn from user selections vs AI recommendations.

        Args:
            recommended_agents: List of agents recommended by AI
            selected_agent: Agent actually selected by user
            context: Additional context (task type, project phase, etc.)
        """
        data = self._read_json_file(self.user_choices_file)

        choice_entry = {
            "timestamp": datetime.now().isoformat(),
            "recommended": recommended_agents,
            "selected": selected_agent,
            "context": context or {},
            "alignment": selected_agent in recommended_agents,
            "position_in_recommendations": recommended_agents.index(selected_agent) if selected_agent in recommended_agents else -1
        }

        data['user_choices'].append(choice_entry)
        self._write_json_file(self.user_choices_file, data)

        # Update learning insights
        self._update_learning_insights()

    def update_agent_effectiveness(self, agent_name: str, task_success: bool,
                                 task_context: Dict = None):
        """
        Track agent success rates in project context.

        Args:
            agent_name: Name of the agent used
            task_success: Whether the task was successful
            task_context: Context about the task (type, complexity, etc.)
        """
        data = self._read_json_file(self.effectiveness_file)

        if agent_name not in data['agent_metrics']:
            data['agent_metrics'][agent_name] = {
                "total_uses": 0,
                "successes": 0,
                "failures": 0,
                "success_rate": 0.0,
                "contexts": [],
                "first_used": datetime.now().isoformat(),
                "last_used": None
            }

        agent_data = data['agent_metrics'][agent_name]
        agent_data['total_uses'] += 1
        agent_data['last_used'] = datetime.now().isoformat()

        if task_success:
            agent_data['successes'] += 1
        else:
            agent_data['failures'] += 1

        agent_data['success_rate'] = agent_data['successes'] / agent_data['total_uses']

        # Add context information
        if task_context:
            task_context['timestamp'] = datetime.now().isoformat()
            task_context['success'] = task_success
            agent_data['contexts'].append(task_context)

            # Keep only last 50 contexts to manage file size
            if len(agent_data['contexts']) > 50:
                agent_data['contexts'] = agent_data['contexts'][-50:]

        self._write_json_file(self.effectiveness_file, data)

        # Update learning insights
        self._update_learning_insights()

    def track_project_evolution(self, change_type: str, details: Dict):
        """
        Monitor project evolution over time.

        Args:
            change_type: Type of change (technology_added, complexity_increased, etc.)
            details: Details about the change
        """
        data = self._read_json_file(self.evolution_file)

        evolution_entry = {
            "timestamp": datetime.now().isoformat(),
            "change_type": change_type,
            "details": details
        }

        data['evolution_timeline'].append(evolution_entry)

        # Track specific types of changes
        if change_type == "technology_change":
            data['technology_changes'].append(evolution_entry)
        elif change_type == "complexity_change":
            data['complexity_metrics'].append(evolution_entry)

        self._write_json_file(self.evolution_file, data)

        # Update learning insights
        self._update_learning_insights()

    def get_user_preferences(self) -> Dict:
        """Get learned user preferences."""
        data = self._read_json_file(self.user_choices_file)
        choices = data.get('user_choices', [])

        if not choices:
            return {}

        preferences = {
            "preferred_agents": {},
            "rejection_patterns": {},
            "context_preferences": {}
        }

        for choice in choices:
            selected = choice['selected']
            recommended = choice['recommended']

            # Track preferred agents
            if selected not in preferences["preferred_agents"]:
                preferences["preferred_agents"][selected] = 0
            preferences["preferred_agents"][selected] += 1

            # Track rejection patterns
            for rejected in recommended:
                if rejected != selected:
                    if rejected not in preferences["rejection_patterns"]:
                        preferences["rejection_patterns"][rejected] = 0
                    preferences["rejection_patterns"][rejected] += 1

        return preferences

    def get_agent_recommendations(self, context: Dict = None) -> List[str]:
        """Get personalized agent recommendations based on learning."""
        preferences = self.get_user_preferences()
        effectiveness_data = self._read_json_file(self.effectiveness_file)

        # Score agents based on user preferences and effectiveness
        agent_scores = {}

        # Factor in user preferences
        for agent, count in preferences.get("preferred_agents", {}).items():
            agent_scores[agent] = agent_scores.get(agent, 0) + count * 0.3

        # Factor in agent effectiveness
        for agent, metrics in effectiveness_data.get("agent_metrics", {}).items():
            success_rate = metrics.get("success_rate", 0)
            total_uses = metrics.get("total_uses", 0)

            # Weight by success rate and usage frequency
            score = success_rate * (1 + min(total_uses / 10, 1))
            agent_scores[agent] = agent_scores.get(agent, 0) + score * 0.4

        # Sort by score and return top recommendations
        sorted_agents = sorted(agent_scores.items(), key=lambda x: x[1], reverse=True)
        return [agent for agent, score in sorted_agents[:5]]

    def _update_learning_insights(self):
        """Update learning insights based on collected data."""
        insights_data = self._read_json_file(self.insights_file)

        # Collect learning summary
        user_data = self._read_json_file(self.user_choices_file)
        effectiveness_data = self._read_json_file(self.effectiveness_file)
        evolution_data = self._read_json_file(self.evolution_file)

        insights_data['learning_summary'] = {
            "total_user_choices": len(user_data.get('user_choices', [])),
            "tracked_agents": len(effectiveness_data.get('agent_metrics', {})),
            "evolution_events": len(evolution_data.get('evolution_timeline', [])),
            "learning_accuracy": self._calculate_learning_accuracy()
        }

        # Extract patterns
        patterns = []

        # User preference patterns
        preferences = self.get_user_preferences()
        if preferences.get("preferred_agents"):
            top_agent = max(preferences["preferred_agents"].items(), key=lambda x: x[1])
            patterns.append(f"User consistently prefers {top_agent[0]} agent")

        # Agent effectiveness patterns
        for agent, metrics in effectiveness_data.get("agent_metrics", {}).items():
            success_rate = metrics.get("success_rate", 0)
            if success_rate > 0.8 and metrics.get("total_uses", 0) > 3:
                patterns.append(f"{agent} shows high effectiveness ({success_rate:.1%}) in this project")

        insights_data['patterns'] = patterns

        # Generate recommendations
        recommendations = []

        # Recommend based on effectiveness
        effective_agents = [
            agent for agent, metrics in effectiveness_data.get("agent_metrics", {}).items()
            if metrics.get("success_rate", 0) > 0.75 and metrics.get("total_uses", 0) > 2
        ]

        if effective_agents:
            recommendations.append(f"Consider prioritizing these effective agents: {', '.join(effective_agents)}")

        insights_data['recommendations'] = recommendations

        self._write_json_file(self.insights_file, insights_data)

    def _calculate_learning_accuracy(self) -> float:
        """Calculate how well the system is learning user preferences."""
        data = self._read_json_file(self.user_choices_file)
        choices = data.get('user_choices', [])

        if len(choices) < 3:  # Need some data to measure accuracy
            return 0.0

        # Calculate accuracy as alignment between recommendations and selections
        alignments = [choice.get('alignment', False) for choice in choices[-10:]]  # Last 10 choices
        return sum(alignments) / len(alignments) if alignments else 0.0

    def get_learning_status(self) -> Dict:
        """Get current learning system status."""
        return {
            "project_id": self.project_id,
            "data_files_exist": all([
                self.user_choices_file.exists(),
                self.effectiveness_file.exists(),
                self.evolution_file.exists(),
                self.insights_file.exists()
            ]),
            "learning_insights": self._read_json_file(self.insights_file),
            "data_directory": str(self.data_dir)
        }


if __name__ == "__main__":
    # Demo usage
    learning_system = ProjectAdaptiveLearning()
    status = learning_system.get_learning_status()
    print(f"Learning System Status: {json.dumps(status, indent=2)}")