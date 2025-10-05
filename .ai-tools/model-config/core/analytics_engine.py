#!/usr/bin/env python3
"""
Analytics Engine for Claude Code Multi-Agent Framework Cost Intelligence

Features:
- Real-time cost dashboards and visualizations
- ROI analysis and cost optimization insights
- Usage pattern analysis and trends
- Agent efficiency metrics
- Predictive cost analytics

Part of Framework v3.6.0 - Intelligent Model Configuration System
"""

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class UsagePattern:
    """Usage pattern analysis"""
    pattern_type: str
    pattern_description: str
    frequency: int
    total_cost: float
    average_cost: float
    recommendation: str


@dataclass
class AgentEfficiency:
    """Agent efficiency metrics"""
    agent_type: str
    total_operations: int
    total_cost: float
    average_cost_per_operation: float
    preferred_model: str
    model_distribution: Dict[str, int]
    efficiency_score: float  # 0-100
    optimization_opportunities: List[str]


@dataclass
class CostTrend:
    """Cost trend analysis"""
    period: str
    trend_direction: str  # "increasing", "decreasing", "stable"
    percentage_change: float
    current_average: float
    previous_average: float
    forecast_next_period: float


@dataclass
class ROIAnalysis:
    """Return on Investment analysis"""
    total_cost: float
    estimated_time_saved_hours: float
    estimated_labor_cost_saved: float
    roi_percentage: float
    breakeven_point: str
    recommendations: List[str]


class AnalyticsEngine:
    """
    Advanced analytics engine for cost intelligence and optimization.

    Features:
    - Real-time cost dashboard data
    - Usage pattern analysis
    - Agent efficiency tracking
    - Cost trend analysis
    - ROI calculations
    - Predictive analytics
    """

    def __init__(self, cost_tracker=None):
        """
        Initialize analytics engine.

        Args:
            cost_tracker: CostTracker instance for accessing cost data
        """
        self.cost_tracker = cost_tracker

        # Analytics cache
        self.cache = {
            "last_analysis": None,
            "patterns": [],
            "trends": [],
            "agent_efficiency": {}
        }

    def generate_dashboard_data(self, days: int = 7) -> Dict:
        """
        Generate comprehensive dashboard data.

        Args:
            days: Number of days to analyze

        Returns:
            Dictionary with dashboard metrics and visualizations
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        dashboard = {
            "timestamp": datetime.now().isoformat(),
            "period": f"Last {days} days",
            "summary": self._get_summary_metrics(start_date, end_date),
            "daily_costs": self._get_daily_cost_series(days),
            "agent_breakdown": self._get_agent_cost_breakdown(start_date, end_date),
            "model_distribution": self._get_model_usage_distribution(start_date, end_date),
            "top_agents": self._get_top_agents_by_cost(start_date, end_date, limit=10),
            "efficiency_metrics": self._get_efficiency_metrics(start_date, end_date),
            "trends": self._analyze_cost_trends(days),
            "recommendations": self._generate_optimization_recommendations(start_date, end_date)
        }

        return dashboard

    def _get_summary_metrics(self, start_date: datetime, end_date: datetime) -> Dict:
        """Get high-level summary metrics"""
        if not self.cost_tracker:
            return {}

        try:
            # Get all costs for period
            summaries = self.cost_tracker.get_summary(
                dimension=self.cost_tracker.CostDimension.DATE,
                start_date=start_date,
                end_date=end_date
            )

            total_cost = sum(s.total_cost for s in summaries)
            total_operations = sum(s.record_count for s in summaries)
            total_tokens = sum(s.total_tokens for s in summaries)

            avg_cost_per_operation = total_cost / total_operations if total_operations > 0 else 0
            avg_cost_per_day = total_cost / max((end_date - start_date).days, 1)

            return {
                "total_cost": total_cost,
                "total_operations": total_operations,
                "total_tokens": total_tokens,
                "average_cost_per_operation": avg_cost_per_operation,
                "average_cost_per_day": avg_cost_per_day
            }

        except Exception as e:
            logger.error(f"Error getting summary metrics: {e}")
            return {}

    def _get_daily_cost_series(self, days: int) -> List[Dict]:
        """Get daily cost time series for charting"""
        if not self.cost_tracker:
            return []

        try:
            daily_costs = self.cost_tracker.get_daily_costs(days=days)

            series = []
            for date, cost in sorted(daily_costs.items()):
                series.append({
                    "date": date,
                    "cost": cost
                })

            return series

        except Exception as e:
            logger.error(f"Error getting daily costs: {e}")
            return []

    def _get_agent_cost_breakdown(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """Get cost breakdown by agent type"""
        if not self.cost_tracker:
            return []

        try:
            summaries = self.cost_tracker.get_summary(
                dimension=self.cost_tracker.CostDimension.AGENT,
                start_date=start_date,
                end_date=end_date
            )

            breakdown = []
            total_cost = sum(s.total_cost for s in summaries)

            for summary in summaries:
                percentage = (summary.total_cost / total_cost * 100) if total_cost > 0 else 0

                breakdown.append({
                    "agent_type": summary.dimension_value,
                    "cost": summary.total_cost,
                    "percentage": percentage,
                    "operations": summary.record_count,
                    "avg_cost": summary.average_cost_per_operation
                })

            return sorted(breakdown, key=lambda x: x["cost"], reverse=True)

        except Exception as e:
            logger.error(f"Error getting agent breakdown: {e}")
            return []

    def _get_model_usage_distribution(self, start_date: datetime, end_date: datetime) -> Dict:
        """Get model usage distribution"""
        if not self.cost_tracker:
            return {}

        try:
            return self.cost_tracker.get_model_distribution()

        except Exception as e:
            logger.error(f"Error getting model distribution: {e}")
            return {}

    def _get_top_agents_by_cost(
        self,
        start_date: datetime,
        end_date: datetime,
        limit: int = 10
    ) -> List[Dict]:
        """Get top N agents by total cost"""
        breakdown = self._get_agent_cost_breakdown(start_date, end_date)
        return breakdown[:limit]

    def _get_efficiency_metrics(self, start_date: datetime, end_date: datetime) -> Dict:
        """Calculate efficiency metrics"""
        if not self.cost_tracker:
            return {}

        try:
            summaries = self.cost_tracker.get_summary(
                dimension=self.cost_tracker.CostDimension.AGENT,
                start_date=start_date,
                end_date=end_date
            )

            total_cost = sum(s.total_cost for s in summaries)
            total_operations = sum(s.record_count for s in summaries)

            return {
                "overall_efficiency": total_operations / total_cost if total_cost > 0 else 0,
                "cost_per_operation": total_cost / total_operations if total_operations > 0 else 0,
                "total_value_operations": total_operations
            }

        except Exception as e:
            logger.error(f"Error calculating efficiency: {e}")
            return {}

    def analyze_agent_efficiency(self, agent_type: str, days: int = 30) -> AgentEfficiency:
        """
        Analyze efficiency of specific agent.

        Args:
            agent_type: Agent to analyze
            days: Analysis period in days

        Returns:
            AgentEfficiency with detailed metrics
        """
        if not self.cost_tracker:
            raise ValueError("Cost tracker not available")

        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Get agent-specific data
        summaries = self.cost_tracker.get_summary(
            dimension=self.cost_tracker.CostDimension.AGENT,
            dimension_value=agent_type,
            start_date=start_date,
            end_date=end_date
        )

        if not summaries:
            raise ValueError(f"No data found for agent: {agent_type}")

        summary = summaries[0]  # Should only be one for specific agent

        # Calculate efficiency score (0-100)
        # Based on: cost per operation vs. average, model usage optimization
        efficiency_score = self._calculate_efficiency_score(summary)

        # Generate optimization opportunities
        opportunities = self._identify_optimization_opportunities(summary)

        # Determine preferred model
        preferred_model = max(summary.model_distribution.items(), key=lambda x: x[1])[0] if summary.model_distribution else "unknown"

        return AgentEfficiency(
            agent_type=agent_type,
            total_operations=summary.record_count,
            total_cost=summary.total_cost,
            average_cost_per_operation=summary.average_cost_per_operation,
            preferred_model=preferred_model,
            model_distribution=summary.model_distribution,
            efficiency_score=efficiency_score,
            optimization_opportunities=opportunities
        )

    def _calculate_efficiency_score(self, summary) -> float:
        """Calculate efficiency score for agent (0-100)"""
        # Baseline: 50
        score = 50.0

        # Adjust based on cost per operation
        # Lower cost = higher efficiency
        if summary.average_cost_per_operation < 0.01:
            score += 20
        elif summary.average_cost_per_operation < 0.05:
            score += 10
        elif summary.average_cost_per_operation > 0.20:
            score -= 20

        # Adjust based on model usage
        # Using cheaper models = higher efficiency
        if summary.model_distribution:
            haiku_percentage = summary.model_distribution.get("claude-haiku-4", 0) / sum(summary.model_distribution.values())
            score += haiku_percentage * 20

        # Ensure 0-100 range
        return max(0, min(100, score))

    def _identify_optimization_opportunities(self, summary) -> List[str]:
        """Identify optimization opportunities for agent"""
        opportunities = []

        # High cost per operation
        if summary.average_cost_per_operation > 0.10:
            opportunities.append("High cost per operation - consider using cheaper models for simple tasks")

        # Model distribution analysis
        if summary.model_distribution:
            opus_count = summary.model_distribution.get("claude-opus-4", 0)
            total_count = sum(summary.model_distribution.values())

            if opus_count / total_count > 0.5:
                opportunities.append("Heavy Opus usage - evaluate if Sonnet can handle some tasks")

        # Low operation count
        if summary.record_count < 10:
            opportunities.append("Low usage - may not have sufficient data for optimization")

        return opportunities

    def _analyze_cost_trends(self, days: int = 30) -> List[CostTrend]:
        """Analyze cost trends over time"""
        if not self.cost_tracker:
            return []

        try:
            # Get daily costs
            daily_costs = self.cost_tracker.get_daily_costs(days=days)

            if len(daily_costs) < 7:
                return []  # Need at least a week of data

            # Split into two periods for comparison
            mid_point = len(daily_costs) // 2
            sorted_dates = sorted(daily_costs.keys())

            first_half = sorted_dates[:mid_point]
            second_half = sorted_dates[mid_point:]

            first_half_avg = sum(daily_costs[d] for d in first_half) / len(first_half)
            second_half_avg = sum(daily_costs[d] for d in second_half) / len(second_half)

            # Calculate trend
            percentage_change = ((second_half_avg - first_half_avg) / first_half_avg * 100) if first_half_avg > 0 else 0

            if percentage_change > 10:
                trend_direction = "increasing"
            elif percentage_change < -10:
                trend_direction = "decreasing"
            else:
                trend_direction = "stable"

            # Simple forecast (linear extrapolation)
            forecast = second_half_avg * (1 + percentage_change / 100)

            trend = CostTrend(
                period=f"Last {days} days",
                trend_direction=trend_direction,
                percentage_change=percentage_change,
                current_average=second_half_avg,
                previous_average=first_half_avg,
                forecast_next_period=forecast
            )

            return [trend]

        except Exception as e:
            logger.error(f"Error analyzing trends: {e}")
            return []

    def calculate_roi(
        self,
        total_cost: float,
        time_period_days: int,
        hourly_rate: float = 75.0
    ) -> ROIAnalysis:
        """
        Calculate Return on Investment for AI assistance.

        Args:
            total_cost: Total cost of AI usage
            time_period_days: Period in days
            hourly_rate: Developer hourly rate for comparison

        Returns:
            ROIAnalysis with ROI metrics
        """
        # Estimate time saved (conservative: 2 hours per day with AI)
        estimated_time_saved_hours = time_period_days * 2

        # Calculate labor cost equivalent
        estimated_labor_cost_saved = estimated_time_saved_hours * hourly_rate

        # Calculate ROI
        roi_percentage = ((estimated_labor_cost_saved - total_cost) / total_cost * 100) if total_cost > 0 else 0

        # Calculate breakeven
        breakeven_days = (total_cost / (hourly_rate * 2)) if hourly_rate > 0 else 0
        breakeven_point = f"{breakeven_days:.1f} days"

        # Generate recommendations
        recommendations = []
        if roi_percentage > 100:
            recommendations.append(f"Excellent ROI: {roi_percentage:.0f}% return on investment")
            recommendations.append("Continue current usage patterns")
        elif roi_percentage > 0:
            recommendations.append(f"Positive ROI: {roi_percentage:.0f}% return on investment")
            recommendations.append("Look for optimization opportunities to increase ROI")
        else:
            recommendations.append(f"Negative ROI: {roi_percentage:.0f}%")
            recommendations.append("Review usage patterns and reduce unnecessary AI operations")

        return ROIAnalysis(
            total_cost=total_cost,
            estimated_time_saved_hours=estimated_time_saved_hours,
            estimated_labor_cost_saved=estimated_labor_cost_saved,
            roi_percentage=roi_percentage,
            breakeven_point=breakeven_point,
            recommendations=recommendations
        )

    def _generate_optimization_recommendations(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> List[str]:
        """Generate cost optimization recommendations"""
        recommendations = []

        if not self.cost_tracker:
            return recommendations

        try:
            # Get model distribution
            model_dist = self._get_model_usage_distribution(start_date, end_date)

            # Analyze Opus usage
            opus_stats = model_dist.get("claude-opus-4", {})
            if opus_stats:
                opus_percentage = opus_stats.get("percentage_cost", 0)
                if opus_percentage > 50:
                    recommendations.append(f"Opus accounts for {opus_percentage:.1f}% of costs - evaluate if Sonnet can handle some tasks")

            # Analyze agent costs
            agent_breakdown = self._get_agent_cost_breakdown(start_date, end_date)
            if agent_breakdown:
                top_agent = agent_breakdown[0]
                if top_agent["percentage"] > 40:
                    recommendations.append(f"{top_agent['agent_type']} accounts for {top_agent['percentage']:.1f}% of costs - optimize its usage")

            # Check for cost trends
            trends = self._analyze_cost_trends()
            if trends and trends[0].trend_direction == "increasing":
                recommendations.append(f"Costs trending up {trends[0].percentage_change:.1f}% - review recent changes")

            # General recommendations
            if not recommendations:
                recommendations.append("Cost patterns look healthy - continue monitoring")

        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")

        return recommendations

    def export_analytics_report(self, output_file: str, days: int = 30):
        """Export comprehensive analytics report to JSON"""
        report = {
            "report_timestamp": datetime.now().isoformat(),
            "analysis_period_days": days,
            "dashboard": self.generate_dashboard_data(days=days),
            "trends": [asdict(t) for t in self._analyze_cost_trends(days=days)]
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"Exported analytics report to {output_file}")


# Example usage and testing
if __name__ == "__main__":
    # Mock cost tracker for testing
    class MockCostTracker:
        from enum import Enum

        class CostDimension(Enum):
            DATE = "date"
            AGENT = "agent"

        def get_summary(self, dimension, dimension_value=None, start_date=None, end_date=None):
            from dataclasses import dataclass

            @dataclass
            class MockSummary:
                total_cost: float = 10.5
                record_count: int = 50
                total_tokens: int = 100000
                average_cost_per_operation: float = 0.21
                dimension_value: str = "software-architect"
                model_distribution: Dict = None

                def __post_init__(self):
                    if self.model_distribution is None:
                        self.model_distribution = {
                            "claude-opus-4": 30,
                            "claude-sonnet-4-5": 15,
                            "claude-haiku-4": 5
                        }

            return [MockSummary()]

        def get_daily_costs(self, days=7):
            from datetime import datetime, timedelta
            costs = {}
            for i in range(days):
                date = (datetime.now() - timedelta(days=days-i-1)).strftime("%Y-%m-%d")
                costs[date] = 1.5 + (i * 0.1)  # Simulated increasing trend
            return costs

        def get_model_distribution(self):
            return {
                "claude-opus-4": {
                    "total_cost": 6.0,
                    "operations": 30,
                    "percentage_cost": 57.0,
                    "percentage_operations": 60.0
                },
                "claude-sonnet-4-5": {
                    "total_cost": 3.5,
                    "operations": 15,
                    "percentage_cost": 33.0,
                    "percentage_operations": 30.0
                }
            }

    engine = AnalyticsEngine(cost_tracker=MockCostTracker())

    print("\n=== Dashboard Data ===")
    dashboard = engine.generate_dashboard_data(days=7)
    print(json.dumps(dashboard["summary"], indent=2))

    print("\n=== ROI Analysis ===")
    roi = engine.calculate_roi(total_cost=100.0, time_period_days=30, hourly_rate=75.0)
    print(f"Total Cost: ${roi.total_cost:.2f}")
    print(f"Estimated Time Saved: {roi.estimated_time_saved_hours} hours")
    print(f"Estimated Labor Cost Saved: ${roi.estimated_labor_cost_saved:.2f}")
    print(f"ROI: {roi.roi_percentage:.1f}%")
    print(f"Breakeven: {roi.breakeven_point}")
    print("Recommendations:")
    for rec in roi.recommendations:
        print(f"  - {rec}")
