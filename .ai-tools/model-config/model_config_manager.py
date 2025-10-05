#!/usr/bin/env python3
"""
Intelligent Model Configuration Manager for Claude Code Multi-Agent Framework

Main orchestrator integrating all model configuration components:
- Intelligent model selection
- Cost tracking and analytics
- Budget management
- Performance optimization

Part of Framework v3.6.0 - Intelligent Model Configuration System

Usage:
    from model_config import ModelConfigManager

    manager = ModelConfigManager()

    # Select optimal model
    recommendation = manager.select_model(
        agent_type="software-architect",
        task_description="Design microservices architecture",
        estimated_tokens=50000
    )

    # Track usage
    manager.track_usage(
        agent_type="software-architect",
        model_type=recommendation.model.value,
        input_tokens=40000,
        output_tokens=10000
    )

    # Check budget status
    status = manager.check_budget()

    # Get analytics
    dashboard = manager.get_dashboard()
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import logging

# Import core components
from .core.model_selector import (
    IntelligentModelSelector,
    ModelType,
    PerformanceProfile,
    ModelRecommendation
)
from .core.cost_tracker import CostTracker, CostDimension, CostSummary
from .core.budget_manager import BudgetManager, BudgetPeriod, BudgetStatus
from .core.analytics_engine import (
    AnalyticsEngine,
    AgentEfficiency,
    CostTrend,
    ROIAnalysis
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelConfigManager:
    """
    Central manager for intelligent model configuration and cost optimization.

    Features:
    - Intelligent model selection based on agent type and task complexity
    - Real-time cost tracking across multiple dimensions
    - Budget management with alerts and auto-downgrade
    - Advanced analytics and ROI calculations
    - Export capabilities for reporting

    Example:
        >>> manager = ModelConfigManager()
        >>> recommendation = manager.select_model("software-architect", "Design system architecture")
        >>> manager.track_usage("software-architect", recommendation.model.value, 50000, 15000)
        >>> status = manager.check_budget()
        >>> print(f"Budget remaining: ${status.remaining_budget:.2f}")
    """

    def __init__(
        self,
        config_dir: Optional[str] = None,
        enable_auto_downgrade: bool = True
    ):
        """
        Initialize Model Configuration Manager.

        Args:
            config_dir: Optional configuration directory path
            enable_auto_downgrade: Enable automatic model downgrade when budget is low
        """
        self.config_dir = config_dir or self._get_default_config_dir()
        self.enable_auto_downgrade = enable_auto_downgrade

        # Initialize core components
        logger.info("Initializing Model Configuration Manager v3.6.0")

        self.model_selector = IntelligentModelSelector()
        self.cost_tracker = CostTracker()
        self.budget_manager = BudgetManager(cost_tracker=self.cost_tracker)
        self.analytics_engine = AnalyticsEngine(cost_tracker=self.cost_tracker)

        logger.info("Model Configuration Manager initialized successfully")

    def _get_default_config_dir(self) -> str:
        """Get default configuration directory"""
        framework_root = Path(__file__).parent.parent.parent
        return str(framework_root / ".claude" / "config")

    def select_model(
        self,
        agent_type: str,
        task_description: Optional[str] = None,
        performance_profile: Optional[PerformanceProfile] = None,
        estimated_tokens: int = 10000
    ) -> ModelRecommendation:
        """
        Select optimal model for agent and task.

        Args:
            agent_type: Type of agent (e.g., "software-architect")
            task_description: Optional task description for complexity analysis
            performance_profile: Optional performance profile (FAST/BALANCED/QUALITY)
            estimated_tokens: Estimated token usage

        Returns:
            ModelRecommendation with selected model and reasoning

        Example:
            >>> rec = manager.select_model(
            ...     agent_type="backend-engineer",
            ...     task_description="Implement REST API",
            ...     performance_profile=PerformanceProfile.BALANCED
            ... )
            >>> print(f"Use {rec.model.value} (${rec.estimated_cost:.4f})")
        """
        # Check budget status
        budget_status = self.budget_manager.check_budget(BudgetPeriod.DAILY)
        budget_remaining = budget_status.remaining_budget

        # Check if auto-downgrade should be triggered
        should_downgrade = self.enable_auto_downgrade and self.budget_manager.should_downgrade_model()

        if should_downgrade:
            logger.warning("Auto-downgrade triggered due to budget constraints")
            # Force FAST profile to use cheaper models
            performance_profile = PerformanceProfile.FAST

        # Get model recommendation
        recommendation = self.model_selector.select_model(
            agent_type=agent_type,
            task_description=task_description,
            budget_remaining=budget_remaining,
            performance_profile=performance_profile,
            estimated_tokens=estimated_tokens
        )

        logger.info(
            f"Model selected for {agent_type}: {recommendation.model.value} "
            f"(confidence: {recommendation.confidence:.2f}, cost: ${recommendation.estimated_cost:.4f})"
        )

        return recommendation

    def track_usage(
        self,
        agent_type: str,
        model_type: str,
        input_tokens: int,
        output_tokens: int,
        project_id: Optional[str] = None,
        session_id: Optional[str] = None,
        task_description: Optional[str] = None
    ):
        """
        Track AI model usage and update cost records.

        Args:
            agent_type: Agent that used the model
            model_type: Model used (e.g., "claude-opus-4")
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            project_id: Optional project identifier
            session_id: Optional session identifier
            task_description: Optional task description

        Returns:
            CostRecord with cost details

        Example:
            >>> record = manager.track_usage(
            ...     agent_type="software-architect",
            ...     model_type="claude-opus-4",
            ...     input_tokens=50000,
            ...     output_tokens=15000
            ... )
            >>> print(f"Cost: ${record.total_cost:.4f}")
        """
        record = self.cost_tracker.track_usage(
            agent_type=agent_type,
            model_type=model_type,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            project_id=project_id,
            session_id=session_id,
            task_description=task_description
        )

        # Check budget after tracking
        self.check_budget()

        return record

    def check_budget(self, period: BudgetPeriod = BudgetPeriod.DAILY) -> BudgetStatus:
        """
        Check current budget status.

        Args:
            period: Budget period to check (DAILY/WEEKLY/MONTHLY)

        Returns:
            BudgetStatus with current spending and alerts

        Example:
            >>> status = manager.check_budget(BudgetPeriod.DAILY)
            >>> print(f"Used {status.percentage_used:.1f}% of budget")
            >>> print(f"Remaining: ${status.remaining_budget:.2f}")
        """
        return self.budget_manager.check_budget(period)

    def get_dashboard(self, days: int = 7) -> Dict:
        """
        Get comprehensive analytics dashboard.

        Args:
            days: Number of days to analyze

        Returns:
            Dictionary with dashboard metrics and visualizations

        Example:
            >>> dashboard = manager.get_dashboard(days=7)
            >>> print(f"Total cost: ${dashboard['summary']['total_cost']:.2f}")
            >>> print(f"Operations: {dashboard['summary']['total_operations']}")
        """
        return self.analytics_engine.generate_dashboard_data(days=days)

    def get_agent_efficiency(self, agent_type: str, days: int = 30) -> AgentEfficiency:
        """
        Analyze efficiency of specific agent.

        Args:
            agent_type: Agent to analyze
            days: Analysis period in days

        Returns:
            AgentEfficiency with detailed metrics

        Example:
            >>> efficiency = manager.get_agent_efficiency("software-architect")
            >>> print(f"Efficiency score: {efficiency.efficiency_score:.1f}/100")
            >>> for opp in efficiency.optimization_opportunities:
            ...     print(f"- {opp}")
        """
        return self.analytics_engine.analyze_agent_efficiency(agent_type, days=days)

    def calculate_roi(
        self,
        time_period_days: int = 30,
        hourly_rate: float = 75.0
    ) -> ROIAnalysis:
        """
        Calculate Return on Investment for AI usage.

        Args:
            time_period_days: Period in days
            hourly_rate: Developer hourly rate for comparison

        Returns:
            ROIAnalysis with ROI metrics

        Example:
            >>> roi = manager.calculate_roi(time_period_days=30, hourly_rate=75.0)
            >>> print(f"ROI: {roi.roi_percentage:.1f}%")
            >>> print(f"Break-even: {roi.breakeven_point}")
        """
        # Get total cost for period
        end_date = datetime.now()
        start_date = end_date - timedelta(days=time_period_days)

        summaries = self.cost_tracker.get_summary(
            dimension=CostDimension.DATE,
            start_date=start_date,
            end_date=end_date
        )

        total_cost = sum(s.total_cost for s in summaries)

        return self.analytics_engine.calculate_roi(
            total_cost=total_cost,
            time_period_days=time_period_days,
            hourly_rate=hourly_rate
        )

    def get_budget_report(self) -> Dict:
        """
        Generate comprehensive budget report.

        Returns:
            Dictionary with budget status for all periods

        Example:
            >>> report = manager.get_budget_report()
            >>> for period, status in report['periods'].items():
            ...     print(f"{period}: ${status['current_spending']:.2f} / ${status['budget_limit']:.2f}")
        """
        return self.budget_manager.get_budget_report()

    def export_analytics(self, output_file: str, days: int = 30):
        """
        Export comprehensive analytics report.

        Args:
            output_file: Output file path
            days: Analysis period in days

        Example:
            >>> manager.export_analytics("analytics_report.json", days=30)
        """
        self.analytics_engine.export_analytics_report(output_file, days=days)

    def export_cost_history(self, output_file: str, days: Optional[int] = None):
        """
        Export cost history to CSV.

        Args:
            output_file: Output file path
            days: Optional number of days to export

        Example:
            >>> manager.export_cost_history("cost_history.csv", days=30)
        """
        from datetime import timedelta

        if days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
        else:
            start_date = None
            end_date = None

        self.cost_tracker.export_to_csv(output_file, start_date=start_date, end_date=end_date)

    def get_optimization_recommendations(self, days: int = 7) -> List[str]:
        """
        Get cost optimization recommendations.

        Args:
            days: Analysis period in days

        Returns:
            List of optimization recommendations

        Example:
            >>> recommendations = manager.get_optimization_recommendations(days=7)
            >>> for rec in recommendations:
            ...     print(f"💡 {rec}")
        """
        dashboard = self.get_dashboard(days=days)
        return dashboard.get("recommendations", [])

    def reset_daily_budget(self):
        """Reset daily budget (typically called at midnight)"""
        logger.info("Resetting daily budget")
        # Budget manager handles this automatically through date-based filtering

    def get_model_info(self, model_type: ModelType) -> Dict:
        """
        Get detailed information about a specific model.

        Args:
            model_type: Model type to query

        Returns:
            Dictionary with model information

        Example:
            >>> info = manager.get_model_info(ModelType.OPUS)
            >>> print(f"Model: {info['name']}")
            >>> print(f"Use cases: {', '.join(info['use_cases'])}")
        """
        return self.model_selector.get_model_info(model_type)

    def get_status_summary(self) -> Dict:
        """
        Get quick status summary.

        Returns:
            Dictionary with current system status

        Example:
            >>> status = manager.get_status_summary()
            >>> print(f"Daily budget: {status['budget']['daily']['percentage_used']:.1f}% used")
            >>> print(f"Auto-downgrade: {status['auto_downgrade']}")
        """
        daily_budget = self.check_budget(BudgetPeriod.DAILY)
        weekly_budget = self.check_budget(BudgetPeriod.WEEKLY)

        return {
            "timestamp": datetime.now().isoformat(),
            "version": "3.6.0",
            "auto_downgrade": self.enable_auto_downgrade,
            "budget": {
                "daily": {
                    "percentage_used": daily_budget.percentage_used,
                    "remaining": daily_budget.remaining_budget,
                    "alert_level": daily_budget.alert_level
                },
                "weekly": {
                    "percentage_used": weekly_budget.percentage_used,
                    "remaining": weekly_budget.remaining_budget,
                    "alert_level": weekly_budget.alert_level
                }
            },
            "should_downgrade": self.budget_manager.should_downgrade_model()
        }


# CLI Interface
def main():
    """Command-line interface for Model Configuration Manager"""
    import argparse
    from datetime import timedelta

    parser = argparse.ArgumentParser(
        description="Intelligent Model Configuration Manager v3.6.0"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show current status summary"
    )

    parser.add_argument(
        "--budget",
        action="store_true",
        help="Show budget report"
    )

    parser.add_argument(
        "--dashboard",
        type=int,
        metavar="DAYS",
        help="Generate dashboard for specified days"
    )

    parser.add_argument(
        "--export-analytics",
        metavar="FILE",
        help="Export analytics report to file"
    )

    parser.add_argument(
        "--export-costs",
        metavar="FILE",
        help="Export cost history to CSV"
    )

    parser.add_argument(
        "--recommendations",
        action="store_true",
        help="Show optimization recommendations"
    )

    args = parser.parse_args()

    # Initialize manager
    manager = ModelConfigManager()

    # Execute commands
    if args.status:
        print("\n=== Model Configuration Manager Status ===")
        status = manager.get_status_summary()
        print(json.dumps(status, indent=2))

    elif args.budget:
        print("\n=== Budget Report ===")
        report = manager.get_budget_report()
        print(json.dumps(report, indent=2))

    elif args.dashboard:
        print(f"\n=== Dashboard ({args.dashboard} days) ===")
        dashboard = manager.get_dashboard(days=args.dashboard)
        print(json.dumps(dashboard, indent=2))

    elif args.export_analytics:
        manager.export_analytics(args.export_analytics)
        print(f"Analytics exported to {args.export_analytics}")

    elif args.export_costs:
        manager.export_cost_history(args.export_costs)
        print(f"Cost history exported to {args.export_costs}")

    elif args.recommendations:
        print("\n=== Optimization Recommendations ===")
        recommendations = manager.get_optimization_recommendations(days=7)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
