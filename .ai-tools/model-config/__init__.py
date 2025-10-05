"""
Intelligent Model Configuration System for Claude Code Multi-Agent Framework

Provides intelligent model selection, cost tracking, budget management,
and analytics for AI-powered development.

Part of Framework v3.6.0

Main Components:
- ModelConfigManager: Main orchestrator for all features
- IntelligentModelSelector: Smart model selection engine
- CostTracker: Multi-dimensional cost tracking
- BudgetManager: Budget monitoring and alerts
- AnalyticsEngine: Advanced cost analytics and ROI

Quick Start:
    >>> from model_config import ModelConfigManager, PerformanceProfile
    >>>
    >>> manager = ModelConfigManager()
    >>>
    >>> # Select optimal model
    >>> recommendation = manager.select_model(
    ...     agent_type="software-architect",
    ...     task_description="Design microservices architecture",
    ...     performance_profile=PerformanceProfile.QUALITY
    ... )
    >>>
    >>> # Track usage
    >>> manager.track_usage(
    ...     agent_type="software-architect",
    ...     model_type=recommendation.model.value,
    ...     input_tokens=50000,
    ...     output_tokens=15000
    ... )
    >>>
    >>> # Check budget
    >>> status = manager.check_budget()
    >>> print(f"Budget remaining: ${status.remaining_budget:.2f}")
    >>>
    >>> # Get analytics
    >>> dashboard = manager.get_dashboard(days=7)
    >>> print(f"Total cost: ${dashboard['summary']['total_cost']:.2f}")

For detailed documentation, see:
- Main README: .ai-tools/model-config/README.md
- User Guide: docs/ai-tools/model-configuration.md
- Quick Start: docs/getting-started/v3.6.0-features-guide.md
"""

# Main orchestrator
from .model_config_manager import ModelConfigManager

# Core components
from .core.model_selector import (
    IntelligentModelSelector,
    ModelType,
    PerformanceProfile,
    ModelRecommendation
)

from .core.cost_tracker import (
    CostTracker,
    CostDimension,
    CostRecord,
    CostSummary,
    TokenUsage
)

from .core.budget_manager import (
    BudgetManager,
    BudgetPeriod,
    BudgetConfig,
    BudgetStatus,
    BudgetAlert,
    AlertLevel
)

from .core.analytics_engine import (
    AnalyticsEngine,
    UsagePattern,
    AgentEfficiency,
    CostTrend,
    ROIAnalysis
)

# Version info
__version__ = "3.6.0"
__author__ = "Claude Code Multi-Agent Framework Team"

# Public API
__all__ = [
    # Main manager
    "ModelConfigManager",

    # Model selection
    "IntelligentModelSelector",
    "ModelType",
    "PerformanceProfile",
    "ModelRecommendation",

    # Cost tracking
    "CostTracker",
    "CostDimension",
    "CostRecord",
    "CostSummary",
    "TokenUsage",

    # Budget management
    "BudgetManager",
    "BudgetPeriod",
    "BudgetConfig",
    "BudgetStatus",
    "BudgetAlert",
    "AlertLevel",

    # Analytics
    "AnalyticsEngine",
    "UsagePattern",
    "AgentEfficiency",
    "CostTrend",
    "ROIAnalysis",

    # Version
    "__version__",
]
