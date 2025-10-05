#!/usr/bin/env python3
"""
Intelligent Model Selector for Claude Code Multi-Agent Framework

Automatically selects optimal Claude model (Opus, Sonnet, Haiku) based on:
- Agent type and competencies
- Task complexity analysis
- Budget constraints and availability
- Performance profile preferences
- Historical performance data

Part of Framework v3.6.0 - Intelligent Model Configuration System
"""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from enum import Enum
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelType(Enum):
    """Available Claude model types"""
    OPUS = "claude-opus-4"
    SONNET = "claude-sonnet-4-5"
    HAIKU = "claude-haiku-4"


class PerformanceProfile(Enum):
    """Performance optimization profiles"""
    FAST = "fast"           # Prioritize speed (Haiku/Sonnet)
    BALANCED = "balanced"   # Optimize cost-quality ratio (Sonnet)
    QUALITY = "quality"     # Prioritize accuracy (Opus/Sonnet)


@dataclass
class ModelRecommendation:
    """Model selection recommendation with reasoning"""
    model: ModelType
    confidence: float  # 0.0 to 1.0
    reasoning: List[str]
    estimated_cost: float  # USD per 1M tokens
    fallback_model: Optional[ModelType] = None
    budget_alert: Optional[str] = None


class IntelligentModelSelector:
    """
    Intelligent model selection engine with budget awareness and performance profiling.

    Features:
    - Agent-specific model optimization
    - Task complexity analysis
    - Budget-aware model selection
    - Performance profile support
    - Automatic fallback strategies
    """

    def __init__(self, config_path: Optional[str] = None):
        """Initialize model selector with configuration"""
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_configuration()

        # Model pricing (USD per 1M tokens - approximate)
        self.model_costs = {
            ModelType.OPUS: {"input": 15.0, "output": 75.0},
            ModelType.SONNET: {"input": 3.0, "output": 15.0},
            ModelType.HAIKU: {"input": 0.25, "output": 1.25}
        }

        # Agent type to model mapping (default preferences)
        self.agent_model_preferences = self._load_agent_preferences()

        # Task complexity indicators
        self.complexity_indicators = {
            "high": ["architecture", "design", "security-analysis", "performance-optimization"],
            "medium": ["implementation", "testing", "refactoring", "code-review"],
            "low": ["formatting", "documentation", "simple-fix", "validation"]
        }

    def _get_default_config_path(self) -> str:
        """Get default configuration file path"""
        framework_root = Path(__file__).parent.parent.parent.parent
        return str(framework_root / ".claude" / "config" / "model-profiles.json")

    def _load_configuration(self) -> Dict:
        """Load model configuration from file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            else:
                logger.warning(f"Configuration file not found: {self.config_path}")
                return self._get_default_configuration()
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return self._get_default_configuration()

    def _get_default_configuration(self) -> Dict:
        """Return default configuration if file not found"""
        return {
            "version": "3.6.0",
            "default_profile": "balanced",
            "profiles": {
                "fast": {"primary_model": "sonnet", "fallback": "haiku"},
                "balanced": {"primary_model": "sonnet", "fallback": "haiku"},
                "quality": {"primary_model": "opus", "fallback": "sonnet"}
            }
        }

    def _load_agent_preferences(self) -> Dict[str, ModelType]:
        """Load agent-specific model preferences"""
        try:
            framework_root = Path(__file__).parent.parent.parent.parent
            mapping_path = framework_root / ".claude" / "config" / "agent-model-mapping.json"

            if os.path.exists(mapping_path):
                with open(mapping_path, 'r') as f:
                    mapping = json.load(f)

                # Convert string model names to ModelType enum
                preferences = {}
                for agent_name, config in mapping.get("agents", {}).items():
                    model_name = config.get("default_model", "sonnet").lower()
                    if "opus" in model_name:
                        preferences[agent_name] = ModelType.OPUS
                    elif "haiku" in model_name:
                        preferences[agent_name] = ModelType.HAIKU
                    else:
                        preferences[agent_name] = ModelType.SONNET

                return preferences

        except Exception as e:
            logger.warning(f"Could not load agent preferences: {e}")

        # Default preferences for core agent types
        return {
            "software-architect": ModelType.OPUS,
            "enterprise-architect": ModelType.OPUS,
            "security-engineer": ModelType.OPUS,
            "performance-engineer": ModelType.SONNET,
            "frontend-engineer": ModelType.SONNET,
            "backend-engineer": ModelType.SONNET,
            "qa-engineer": ModelType.SONNET,
            "deployment-engineer": ModelType.HAIKU,
        }

    def select_model(
        self,
        agent_type: str,
        task_description: Optional[str] = None,
        budget_remaining: Optional[float] = None,
        performance_profile: Optional[PerformanceProfile] = None,
        estimated_tokens: int = 10000
    ) -> ModelRecommendation:
        """
        Select optimal model based on context and constraints.

        Args:
            agent_type: Type of agent requesting model (e.g., "software-architect")
            task_description: Optional description of task for complexity analysis
            budget_remaining: Optional remaining budget in USD
            performance_profile: Optional performance profile preference
            estimated_tokens: Estimated token usage for cost calculation

        Returns:
            ModelRecommendation with selected model and reasoning
        """
        reasoning = []

        # Step 1: Get base model preference for agent type
        base_model = self._get_agent_preference(agent_type)
        reasoning.append(f"Agent '{agent_type}' base preference: {base_model.value}")

        # Step 2: Analyze task complexity if provided
        complexity = "medium"  # default
        if task_description:
            complexity = self._analyze_task_complexity(task_description)
            reasoning.append(f"Task complexity: {complexity}")

        # Step 3: Apply performance profile if specified
        profile = performance_profile or PerformanceProfile.BALANCED
        profile_model = self._apply_performance_profile(base_model, profile, complexity)
        if profile_model != base_model:
            reasoning.append(f"Performance profile '{profile.value}' adjusted to: {profile_model.value}")
            base_model = profile_model

        # Step 4: Check budget constraints
        selected_model = base_model
        budget_alert = None

        if budget_remaining is not None:
            estimated_cost = self._estimate_cost(base_model, estimated_tokens)

            if estimated_cost > budget_remaining:
                # Need to downgrade
                fallback = self._get_fallback_model(base_model)
                fallback_cost = self._estimate_cost(fallback, estimated_tokens)

                if fallback_cost <= budget_remaining:
                    selected_model = fallback
                    reasoning.append(f"Budget constraint: downgraded to {fallback.value}")
                    budget_alert = f"Insufficient budget for {base_model.value}, using {fallback.value}"
                else:
                    budget_alert = f"WARNING: Even cheapest model exceeds budget ({fallback_cost:.4f} > {budget_remaining:.4f})"
            elif estimated_cost > budget_remaining * 0.5:
                budget_alert = f"Using >50% of remaining budget ({estimated_cost:.4f} of {budget_remaining:.4f})"

        # Step 5: Calculate final cost estimate
        final_cost = self._estimate_cost(selected_model, estimated_tokens)

        # Step 6: Determine confidence level
        confidence = self._calculate_confidence(
            agent_type, task_description, complexity,
            selected_model, base_model
        )

        # Step 7: Determine fallback model
        fallback_model = self._get_fallback_model(selected_model)

        return ModelRecommendation(
            model=selected_model,
            confidence=confidence,
            reasoning=reasoning,
            estimated_cost=final_cost,
            fallback_model=fallback_model,
            budget_alert=budget_alert
        )

    def _get_agent_preference(self, agent_type: str) -> ModelType:
        """Get model preference for specific agent type"""
        # Normalize agent name
        agent_name = agent_type.lower().replace("_", "-")

        # Check exact match
        if agent_name in self.agent_model_preferences:
            return self.agent_model_preferences[agent_name]

        # Check partial matches for agent categories
        if "architect" in agent_name or "design" in agent_name:
            return ModelType.OPUS
        elif "engineer" in agent_name or "developer" in agent_name:
            return ModelType.SONNET
        elif "analyst" in agent_name or "manager" in agent_name:
            return ModelType.SONNET
        else:
            return ModelType.SONNET  # default

    def _analyze_task_complexity(self, task_description: str) -> str:
        """Analyze task complexity from description"""
        task_lower = task_description.lower()

        # Check for high complexity indicators
        high_count = sum(1 for indicator in self.complexity_indicators["high"]
                        if indicator in task_lower)

        # Check for low complexity indicators
        low_count = sum(1 for indicator in self.complexity_indicators["low"]
                       if indicator in task_lower)

        if high_count > 0:
            return "high"
        elif low_count > 0:
            return "low"
        else:
            return "medium"

    def _apply_performance_profile(
        self,
        base_model: ModelType,
        profile: PerformanceProfile,
        complexity: str
    ) -> ModelType:
        """Apply performance profile to adjust model selection"""
        if profile == PerformanceProfile.FAST:
            # Prioritize speed - use Haiku or Sonnet
            if complexity == "low":
                return ModelType.HAIKU
            else:
                return ModelType.SONNET

        elif profile == PerformanceProfile.QUALITY:
            # Prioritize quality - use Opus or Sonnet
            if complexity == "high":
                return ModelType.OPUS
            else:
                return ModelType.SONNET

        else:  # BALANCED
            # Use base model recommendation
            return base_model

    def _get_fallback_model(self, model: ModelType) -> ModelType:
        """Get fallback model for budget constraints"""
        if model == ModelType.OPUS:
            return ModelType.SONNET
        elif model == ModelType.SONNET:
            return ModelType.HAIKU
        else:
            return ModelType.HAIKU  # already cheapest

    def _estimate_cost(self, model: ModelType, estimated_tokens: int) -> float:
        """Estimate cost for model and token count"""
        costs = self.model_costs[model]
        # Assume 70% input, 30% output token distribution
        input_cost = (estimated_tokens * 0.7 / 1_000_000) * costs["input"]
        output_cost = (estimated_tokens * 0.3 / 1_000_000) * costs["output"]
        return input_cost + output_cost

    def _calculate_confidence(
        self,
        agent_type: str,
        task_description: Optional[str],
        complexity: str,
        selected_model: ModelType,
        base_model: ModelType
    ) -> float:
        """Calculate confidence in model selection"""
        confidence = 0.8  # base confidence

        # Increase confidence if model matches agent preference
        if selected_model == base_model:
            confidence += 0.1

        # Increase confidence if we have task description
        if task_description:
            confidence += 0.05

        # Adjust based on complexity match
        if complexity == "high" and selected_model == ModelType.OPUS:
            confidence += 0.05
        elif complexity == "low" and selected_model == ModelType.HAIKU:
            confidence += 0.05

        return min(confidence, 1.0)

    def get_model_info(self, model: ModelType) -> Dict:
        """Get detailed information about a specific model"""
        return {
            "name": model.value,
            "type": model.name.lower(),
            "pricing": self.model_costs[model],
            "use_cases": self._get_model_use_cases(model),
            "strengths": self._get_model_strengths(model)
        }

    def _get_model_use_cases(self, model: ModelType) -> List[str]:
        """Get typical use cases for model"""
        use_cases = {
            ModelType.OPUS: [
                "Complex architecture design",
                "Security threat modeling",
                "Performance optimization analysis",
                "Enterprise-scale system design"
            ],
            ModelType.SONNET: [
                "Feature implementation",
                "Code review and refactoring",
                "API design and development",
                "Testing strategy development"
            ],
            ModelType.HAIKU: [
                "Code formatting",
                "Simple bug fixes",
                "Documentation updates",
                "Quick validations"
            ]
        }
        return use_cases.get(model, [])

    def _get_model_strengths(self, model: ModelType) -> List[str]:
        """Get model strengths"""
        strengths = {
            ModelType.OPUS: [
                "Highest quality output",
                "Complex reasoning",
                "Detailed analysis",
                "Architectural thinking"
            ],
            ModelType.SONNET: [
                "Balanced cost-quality",
                "Fast responses",
                "Good code generation",
                "Practical solutions"
            ],
            ModelType.HAIKU: [
                "Fastest responses",
                "Lowest cost",
                "Simple tasks",
                "High throughput"
            ]
        }
        return strengths.get(model, [])


# Example usage and testing
if __name__ == "__main__":
    selector = IntelligentModelSelector()

    # Test 1: Architect with complex task
    print("\n=== Test 1: Software Architect - Complex Architecture Design ===")
    rec = selector.select_model(
        agent_type="software-architect",
        task_description="Design scalable microservices architecture for enterprise system",
        budget_remaining=1.0,
        performance_profile=PerformanceProfile.QUALITY,
        estimated_tokens=50000
    )
    print(f"Model: {rec.model.value}")
    print(f"Confidence: {rec.confidence:.2f}")
    print(f"Cost: ${rec.estimated_cost:.4f}")
    print(f"Reasoning: {', '.join(rec.reasoning)}")

    # Test 2: Engineer with medium task and limited budget
    print("\n=== Test 2: Backend Engineer - Limited Budget ===")
    rec = selector.select_model(
        agent_type="backend-engineer",
        task_description="Implement REST API endpoints with validation",
        budget_remaining=0.05,
        performance_profile=PerformanceProfile.BALANCED,
        estimated_tokens=30000
    )
    print(f"Model: {rec.model.value}")
    print(f"Confidence: {rec.confidence:.2f}")
    print(f"Cost: ${rec.estimated_cost:.4f}")
    print(f"Budget Alert: {rec.budget_alert}")
    print(f"Reasoning: {', '.join(rec.reasoning)}")

    # Test 3: Simple task with FAST profile
    print("\n=== Test 3: QA Engineer - Fast Profile ===")
    rec = selector.select_model(
        agent_type="qa-engineer",
        task_description="Format test output and fix simple linting issues",
        budget_remaining=10.0,
        performance_profile=PerformanceProfile.FAST,
        estimated_tokens=10000
    )
    print(f"Model: {rec.model.value}")
    print(f"Confidence: {rec.confidence:.2f}")
    print(f"Cost: ${rec.estimated_cost:.4f}")
    print(f"Reasoning: {', '.join(rec.reasoning)}")
