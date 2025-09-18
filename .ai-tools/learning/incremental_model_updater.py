#!/usr/bin/env python3
"""
Incremental Model Updates System
Progressively improves recommendation accuracy based on project-specific learning
"""

import json
import os
import pickle
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
try:
    from .project_adaptive_learning import ProjectAdaptiveLearning
    from .user_choice_tracker import UserChoiceTracker
    from .agent_effectiveness_monitor import AgentEffectivenessMonitor
except ImportError:
    from project_adaptive_learning import ProjectAdaptiveLearning
    from user_choice_tracker import UserChoiceTracker
    from agent_effectiveness_monitor import AgentEffectivenessMonitor


class IncrementalModelUpdater:
    """
    System for incrementally updating recommendation models based on
    project-specific feedback and performance data.
    """

    def __init__(self, project_root: str = None):
        """Initialize incremental model updater."""
        self.learning_system = ProjectAdaptiveLearning(project_root)
        self.choice_tracker = UserChoiceTracker(project_root)
        self.effectiveness_monitor = AgentEffectivenessMonitor(project_root)

        self.models_dir = self.learning_system.models_dir
        self.adaptation_file = self.models_dir / "local_adaptation.pkl"
        self.model_config_file = self.models_dir / "model_config.json"

        # Initialize model state
        self._initialize_model_state()

    def _initialize_model_state(self):
        """Initialize or load existing model state."""
        if self.adaptation_file.exists():
            self.model_weights = self._load_model_weights()
        else:
            self.model_weights = self._create_initial_weights()

        if self.model_config_file.exists():
            self.model_config = self._load_json_file(self.model_config_file)
        else:
            self.model_config = self._create_initial_config()
            self._save_json_file(self.model_config_file, self.model_config)

    def _create_initial_weights(self) -> Dict:
        """Create initial model weights."""
        return {
            "agent_preferences": {},  # User's agent preference weights
            "context_weights": {},    # Context-based weight adjustments
            "effectiveness_weights": {},  # Agent effectiveness adjustments
            "task_type_weights": {},  # Task type specific weights
            "temporal_decay": 0.95,   # How much to decay old data
            "learning_rate": 0.1      # How quickly to adapt
        }

    def _create_initial_config(self) -> Dict:
        """Create initial model configuration."""
        return {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "update_frequency": "on_feedback",  # When to update weights
            "minimum_data_points": 5,  # Minimum data before learning
            "confidence_threshold": 0.6,  # Confidence threshold for recommendations
            "max_history_days": 90,  # How long to keep historical data
            "adaptation_parameters": {
                "user_preference_weight": 0.4,
                "effectiveness_weight": 0.3,
                "context_weight": 0.2,
                "recency_weight": 0.1
            }
        }

    def update_model(self, force_update: bool = False):
        """
        Update model weights based on latest feedback data.

        Args:
            force_update: Force update even if not enough new data
        """
        # Check if update is needed
        if not force_update and not self._should_update_model():
            return {"status": "No update needed", "reason": "Insufficient new data"}

        print("Updating model weights based on project-specific learning...")

        # Get latest data
        user_patterns = self.choice_tracker.analyze_user_patterns()
        effectiveness_data = self._get_effectiveness_data()
        context_patterns = self._analyze_context_patterns()

        # Update different weight categories
        self._update_user_preference_weights(user_patterns)
        self._update_effectiveness_weights(effectiveness_data)
        self._update_context_weights(context_patterns)
        self._update_temporal_weights()

        # Save updated weights
        self._save_model_weights()

        # Update configuration
        self.model_config['last_updated'] = datetime.now().isoformat()
        self._save_json_file(self.model_config_file, self.model_config)

        return {
            "status": "Model updated successfully",
            "updated_at": self.model_config['last_updated'],
            "weights_summary": self._get_weights_summary()
        }

    def _should_update_model(self) -> bool:
        """Determine if model should be updated."""
        # Check if minimum data points are available
        user_data = self.learning_system._read_json_file(
            self.learning_system.user_choices_file
        )
        choices_count = len(user_data.get('user_choices', []))

        if choices_count < self.model_config['minimum_data_points']:
            return False

        # Check if enough time has passed since last update
        last_updated = self.model_config.get('last_updated')
        if last_updated:
            last_update_time = datetime.fromisoformat(last_updated)
            if datetime.now() - last_update_time < timedelta(hours=1):
                return False

        return True

    def _update_user_preference_weights(self, user_patterns: Dict):
        """Update weights based on user preference patterns."""
        preferred_agents = user_patterns.get('preferred_agents', {})
        rejected_agents = user_patterns.get('rejected_agents', {})

        learning_rate = self.model_weights['learning_rate']

        # Update preference weights
        for agent, data in preferred_agents.items():
            current_weight = self.model_weights['agent_preferences'].get(agent, 0.5)
            preference_strength = data['percentage'] / 100.0

            # Incremental update
            new_weight = current_weight + learning_rate * (preference_strength - current_weight)
            self.model_weights['agent_preferences'][agent] = min(1.0, max(0.0, new_weight))

        # Penalize rejected agents
        for agent, data in rejected_agents.items():
            current_weight = self.model_weights['agent_preferences'].get(agent, 0.5)
            rejection_strength = data['rejection_rate'] / 100.0

            # Decrease weight based on rejection rate
            penalty = learning_rate * rejection_strength
            new_weight = current_weight - penalty
            self.model_weights['agent_preferences'][agent] = min(1.0, max(0.1, new_weight))

    def _update_effectiveness_weights(self, effectiveness_data: Dict):
        """Update weights based on agent effectiveness."""
        learning_rate = self.model_weights['learning_rate']

        for agent, metrics in effectiveness_data.items():
            success_rate = metrics.get('success_rate', 0.5)
            total_uses = metrics.get('total_uses', 0)

            # Weight adjustment based on effectiveness
            current_weight = self.model_weights['effectiveness_weights'].get(agent, 0.5)

            # Factor in reliability (more uses = more reliable data)
            reliability = min(total_uses / 10.0, 1.0)
            adjusted_success_rate = success_rate * reliability

            # Incremental update
            new_weight = current_weight + learning_rate * (adjusted_success_rate - current_weight)
            self.model_weights['effectiveness_weights'][agent] = min(1.0, max(0.1, new_weight))

    def _update_context_weights(self, context_patterns: Dict):
        """Update weights based on context patterns."""
        learning_rate = self.model_weights['learning_rate']

        for context_key, agent_counts in context_patterns.items():
            if context_key not in self.model_weights['context_weights']:
                self.model_weights['context_weights'][context_key] = {}

            total_uses = sum(agent_counts.values())

            for agent, count in agent_counts.items():
                context_preference = count / total_uses

                current_weight = self.model_weights['context_weights'][context_key].get(agent, 0.5)
                new_weight = current_weight + learning_rate * (context_preference - current_weight)

                self.model_weights['context_weights'][context_key][agent] = min(1.0, max(0.1, new_weight))

    def _update_temporal_weights(self):
        """Apply temporal decay to older weights."""
        decay_rate = self.model_weights['temporal_decay']

        # Apply decay to all weight categories
        for agent in self.model_weights['agent_preferences']:
            self.model_weights['agent_preferences'][agent] *= decay_rate

        for agent in self.model_weights['effectiveness_weights']:
            self.model_weights['effectiveness_weights'][agent] *= decay_rate

    def _get_effectiveness_data(self) -> Dict:
        """Get effectiveness data for all agents."""
        effectiveness_file = self.learning_system.effectiveness_file
        data = self.learning_system._read_json_file(effectiveness_file)
        return data.get('agent_metrics', {})

    def _analyze_context_patterns(self) -> Dict:
        """Analyze context patterns from user choices."""
        user_data = self.learning_system._read_json_file(
            self.learning_system.user_choices_file
        )
        choices = user_data.get('user_choices', [])

        context_patterns = {}

        for choice in choices:
            context = choice.get('context', {})
            selected = choice.get('selected')

            for key, value in context.items():
                if value:
                    context_key = f"{key}:{value}"
                    if context_key not in context_patterns:
                        context_patterns[context_key] = {}

                    if selected not in context_patterns[context_key]:
                        context_patterns[context_key][selected] = 0
                    context_patterns[context_key][selected] += 1

        return context_patterns

    def get_personalized_recommendations(self, agents: List[str],
                                       context: Dict = None,
                                       top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Get personalized recommendations with confidence scores.

        Args:
            agents: List of available agents
            context: Current context (task_type, project_phase, etc.)
            top_k: Number of top recommendations to return

        Returns:
            List of tuples (agent_name, confidence_score)
        """
        agent_scores = {}

        for agent in agents:
            score = self._calculate_agent_score(agent, context)
            agent_scores[agent] = score

        # Sort by score and return top k
        sorted_agents = sorted(agent_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_agents[:top_k]

    def _calculate_agent_score(self, agent: str, context: Dict = None) -> float:
        """Calculate personalized score for an agent."""
        weights = self.model_config['adaptation_parameters']

        # Base score
        score = 0.5

        # User preference component
        preference_weight = self.model_weights['agent_preferences'].get(agent, 0.5)
        score += weights['user_preference_weight'] * preference_weight

        # Effectiveness component
        effectiveness_weight = self.model_weights['effectiveness_weights'].get(agent, 0.5)
        score += weights['effectiveness_weight'] * effectiveness_weight

        # Context component
        if context:
            context_score = self._calculate_context_score(agent, context)
            score += weights['context_weight'] * context_score

        # Recency component (favor recently successful agents)
        recency_score = self._calculate_recency_score(agent)
        score += weights['recency_weight'] * recency_score

        return min(1.0, max(0.0, score))

    def _calculate_context_score(self, agent: str, context: Dict) -> float:
        """Calculate context-based score for agent."""
        context_weights = self.model_weights.get('context_weights', {})
        scores = []

        for key, value in context.items():
            if value:
                context_key = f"{key}:{value}"
                if context_key in context_weights:
                    agent_weight = context_weights[context_key].get(agent, 0.5)
                    scores.append(agent_weight)

        return sum(scores) / len(scores) if scores else 0.5

    def _calculate_recency_score(self, agent: str) -> float:
        """Calculate recency-based score (recent success gets higher score)."""
        effectiveness_data = self._get_effectiveness_data()
        agent_data = effectiveness_data.get(agent, {})

        contexts = agent_data.get('contexts', [])
        if not contexts:
            return 0.5

        # Check recent performance (last 7 days)
        recent_contexts = [
            c for c in contexts
            if self._is_recent_context(c.get('timestamp'), days=7)
        ]

        if not recent_contexts:
            return 0.3  # Lower score for agents not used recently

        # Calculate success rate in recent period
        recent_successes = sum(1 for c in recent_contexts if c.get('success', False))
        recent_success_rate = recent_successes / len(recent_contexts)

        return recent_success_rate

    def _is_recent_context(self, timestamp_str: str, days: int = 7) -> bool:
        """Check if timestamp is within recent period."""
        if not timestamp_str:
            return False

        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            cutoff = datetime.now() - timedelta(days=days)
            return timestamp > cutoff
        except ValueError:
            return False

    def _get_weights_summary(self) -> Dict:
        """Get summary of current model weights."""
        return {
            "agent_preferences_count": len(self.model_weights.get('agent_preferences', {})),
            "effectiveness_weights_count": len(self.model_weights.get('effectiveness_weights', {})),
            "context_patterns_count": len(self.model_weights.get('context_weights', {})),
            "learning_rate": self.model_weights.get('learning_rate', 0.1),
            "temporal_decay": self.model_weights.get('temporal_decay', 0.95)
        }

    def _load_model_weights(self) -> Dict:
        """Load model weights from file."""
        try:
            with open(self.adaptation_file, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Warning: Error loading model weights: {e}")
            return self._create_initial_weights()

    def _save_model_weights(self):
        """Save model weights to file."""
        self.models_dir.mkdir(parents=True, exist_ok=True)
        with open(self.adaptation_file, 'wb') as f:
            pickle.dump(self.model_weights, f)

    def _load_json_file(self, file_path: Path) -> Dict:
        """Load JSON file safely."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Error loading {file_path}: {e}")
            return {}

    def _save_json_file(self, file_path: Path, data: Dict):
        """Save JSON file safely."""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_model_status(self) -> Dict:
        """Get current model status and statistics."""
        return {
            "model_initialized": self.adaptation_file.exists(),
            "last_updated": self.model_config.get('last_updated'),
            "weights_summary": self._get_weights_summary(),
            "configuration": self.model_config,
            "learning_data_available": self._check_learning_data_availability()
        }

    def _check_learning_data_availability(self) -> Dict:
        """Check availability of learning data."""
        user_data = self.learning_system._read_json_file(
            self.learning_system.user_choices_file
        )
        effectiveness_data = self._get_effectiveness_data()

        return {
            "user_choices": len(user_data.get('user_choices', [])),
            "agent_effectiveness_records": len(effectiveness_data),
            "minimum_data_threshold": self.model_config['minimum_data_points'],
            "ready_for_learning": len(user_data.get('user_choices', [])) >= self.model_config['minimum_data_points']
        }

    def reset_model(self):
        """Reset model to initial state."""
        self.model_weights = self._create_initial_weights()
        self.model_config = self._create_initial_config()

        self._save_model_weights()
        self._save_json_file(self.model_config_file, self.model_config)

        return {"status": "Model reset to initial state"}


# Example usage and testing
if __name__ == "__main__":
    updater = IncrementalModelUpdater()

    # Check model status
    status = updater.get_model_status()
    print("Model Status:", json.dumps(status, indent=2))

    # Force update model
    update_result = updater.update_model(force_update=True)
    print("Update Result:", json.dumps(update_result, indent=2))

    # Get personalized recommendations
    recommendations = updater.get_personalized_recommendations(
        agents=["frontend-engineer", "backend-engineer", "ux-designer"],
        context={"task_type": "development", "project_phase": "implementation"},
        top_k=3
    )
    print("Personalized Recommendations:", recommendations)