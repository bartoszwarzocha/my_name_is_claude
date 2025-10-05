#!/usr/bin/env python3
"""
Budget Management System for Claude Code Multi-Agent Framework

Features:
- Multi-level budget tracking (daily/weekly/monthly)
- Alert thresholds and notifications
- Auto-downgrade recommendations
- Budget forecasting
- Spending reports and analytics

Part of Framework v3.6.0 - Intelligent Model Configuration System
"""

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BudgetPeriod(Enum):
    """Budget period types"""
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CUSTOM = "custom"


class AlertLevel(Enum):
    """Budget alert levels"""
    INFO = "info"           # 50% of budget
    WARNING = "warning"     # 75% of budget
    CRITICAL = "critical"   # 90% of budget
    EXCEEDED = "exceeded"   # 100% of budget


@dataclass
class BudgetConfig:
    """Budget configuration"""
    period: str
    limit: float  # USD
    alert_thresholds: Dict[str, float]  # AlertLevel -> percentage
    auto_downgrade: bool = True
    rollover_unused: bool = False


@dataclass
class BudgetStatus:
    """Current budget status"""
    period: str
    period_start: str
    period_end: str
    budget_limit: float
    current_spending: float
    remaining_budget: float
    percentage_used: float
    alert_level: str
    forecasted_spending: Optional[float] = None
    days_remaining: Optional[int] = None


@dataclass
class BudgetAlert:
    """Budget alert notification"""
    timestamp: str
    level: str
    period: str
    budget_limit: float
    current_spending: float
    percentage_used: float
    message: str
    recommendations: List[str]


class BudgetManager:
    """
    Comprehensive budget management system for AI cost control.

    Features:
    - Multi-period budget tracking (daily/weekly/monthly)
    - Configurable alert thresholds
    - Automatic downgrade recommendations
    - Budget forecasting based on usage patterns
    - Spending reports and analytics
    """

    def __init__(self, config_path: Optional[str] = None, cost_tracker=None):
        """
        Initialize budget manager.

        Args:
            config_path: Path to budget configuration file
            cost_tracker: CostTracker instance for accessing spending data
        """
        self.config_path = config_path or self._get_default_config_path()
        self.cost_tracker = cost_tracker

        # Load budget configuration
        self.budgets = self._load_budget_config()

        # Alert history
        self.alert_history: List[BudgetAlert] = []

        # Default alert thresholds (percentage of budget)
        self.default_thresholds = {
            AlertLevel.INFO.value: 0.50,
            AlertLevel.WARNING.value: 0.75,
            AlertLevel.CRITICAL.value: 0.90,
            AlertLevel.EXCEEDED.value: 1.00
        }

    def _get_default_config_path(self) -> str:
        """Get default configuration file path"""
        framework_root = Path(__file__).parent.parent.parent.parent
        return str(framework_root / ".claude" / "config" / "cost-optimization.json")

    def _load_budget_config(self) -> Dict[str, BudgetConfig]:
        """Load budget configuration from file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    data = json.load(f)

                budgets = {}
                for period, config in data.get("budget_limits", {}).items():
                    budgets[period] = BudgetConfig(
                        period=period,
                        limit=config.get("limit", 0.0),
                        alert_thresholds=config.get("alert_thresholds", self.default_thresholds),
                        auto_downgrade=config.get("auto_downgrade", True),
                        rollover_unused=config.get("rollover_unused", False)
                    )

                return budgets

        except Exception as e:
            logger.warning(f"Could not load budget config: {e}")

        # Return default configuration
        return self._get_default_budgets()

    def _get_default_budgets(self) -> Dict[str, BudgetConfig]:
        """Get default budget configuration"""
        return {
            BudgetPeriod.DAILY.value: BudgetConfig(
                period=BudgetPeriod.DAILY.value,
                limit=10.0,
                alert_thresholds=self.default_thresholds.copy()
            ),
            BudgetPeriod.WEEKLY.value: BudgetConfig(
                period=BudgetPeriod.WEEKLY.value,
                limit=50.0,
                alert_thresholds=self.default_thresholds.copy()
            ),
            BudgetPeriod.MONTHLY.value: BudgetConfig(
                period=BudgetPeriod.MONTHLY.value,
                limit=200.0,
                alert_thresholds=self.default_thresholds.copy()
            )
        }

    def check_budget(
        self,
        period: BudgetPeriod = BudgetPeriod.DAILY
    ) -> BudgetStatus:
        """
        Check current budget status for specified period.

        Args:
            period: Budget period to check

        Returns:
            BudgetStatus with current spending and alerts
        """
        budget_config = self.budgets.get(period.value)
        if not budget_config:
            raise ValueError(f"No budget configured for period: {period.value}")

        # Get period date range
        period_start, period_end = self._get_period_range(period)

        # Get current spending from cost tracker
        current_spending = self._get_period_spending(period_start, period_end)

        # Calculate metrics
        remaining_budget = budget_config.limit - current_spending
        percentage_used = (current_spending / budget_config.limit * 100) if budget_config.limit > 0 else 0

        # Determine alert level
        alert_level = self._determine_alert_level(percentage_used, budget_config)

        # Calculate forecast
        forecasted_spending = self._forecast_spending(period, period_start, period_end, current_spending)

        # Calculate days remaining in period
        days_remaining = (period_end - datetime.now()).days

        status = BudgetStatus(
            period=period.value,
            period_start=period_start.isoformat(),
            period_end=period_end.isoformat(),
            budget_limit=budget_config.limit,
            current_spending=current_spending,
            remaining_budget=remaining_budget,
            percentage_used=percentage_used,
            alert_level=alert_level.value,
            forecasted_spending=forecasted_spending,
            days_remaining=days_remaining
        )

        # Generate alert if needed
        if alert_level != AlertLevel.INFO:
            self._generate_alert(status, budget_config)

        return status

    def _get_period_range(self, period: BudgetPeriod) -> Tuple[datetime, datetime]:
        """Get start and end dates for budget period"""
        now = datetime.now()

        if period == BudgetPeriod.DAILY:
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=1)

        elif period == BudgetPeriod.WEEKLY:
            # Week starts on Monday
            start = now - timedelta(days=now.weekday())
            start = start.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=7)

        elif period == BudgetPeriod.MONTHLY:
            # Month starts on 1st
            start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            # End is first day of next month
            if now.month == 12:
                end = start.replace(year=now.year + 1, month=1)
            else:
                end = start.replace(month=now.month + 1)

        else:
            # Custom period - default to daily
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=1)

        return start, end

    def _get_period_spending(self, start: datetime, end: datetime) -> float:
        """Get total spending for period from cost tracker"""
        if not self.cost_tracker:
            logger.warning("No cost tracker available, returning 0")
            return 0.0

        try:
            # Get cost summaries for date range
            summaries = self.cost_tracker.get_summary(
                dimension=self.cost_tracker.CostDimension.DATE,
                start_date=start,
                end_date=end
            )

            total_spending = sum(s.total_cost for s in summaries)
            return total_spending

        except Exception as e:
            logger.error(f"Error getting period spending: {e}")
            return 0.0

    def _determine_alert_level(
        self,
        percentage_used: float,
        budget_config: BudgetConfig
    ) -> AlertLevel:
        """Determine alert level based on usage percentage"""
        thresholds = budget_config.alert_thresholds

        if percentage_used >= thresholds.get(AlertLevel.EXCEEDED.value, 1.0) * 100:
            return AlertLevel.EXCEEDED
        elif percentage_used >= thresholds.get(AlertLevel.CRITICAL.value, 0.9) * 100:
            return AlertLevel.CRITICAL
        elif percentage_used >= thresholds.get(AlertLevel.WARNING.value, 0.75) * 100:
            return AlertLevel.WARNING
        elif percentage_used >= thresholds.get(AlertLevel.INFO.value, 0.5) * 100:
            return AlertLevel.INFO
        else:
            return AlertLevel.INFO

    def _forecast_spending(
        self,
        period: BudgetPeriod,
        period_start: datetime,
        period_end: datetime,
        current_spending: float
    ) -> float:
        """Forecast total spending for period based on current rate"""
        now = datetime.now()

        # Calculate time elapsed and remaining
        total_duration = (period_end - period_start).total_seconds()
        elapsed_duration = (now - period_start).total_seconds()

        if elapsed_duration <= 0:
            return current_spending

        # Calculate spending rate (USD per second)
        spending_rate = current_spending / elapsed_duration

        # Forecast total spending
        forecasted_total = spending_rate * total_duration

        return forecasted_total

    def _generate_alert(self, status: BudgetStatus, budget_config: BudgetConfig):
        """Generate budget alert with recommendations"""
        alert_level = AlertLevel(status.alert_level)

        # Create alert message
        if alert_level == AlertLevel.EXCEEDED:
            message = f"🚨 BUDGET EXCEEDED: {status.period} budget limit of ${status.budget_limit:.2f} exceeded (${status.current_spending:.2f} spent)"
        elif alert_level == AlertLevel.CRITICAL:
            message = f"⚠️ CRITICAL: {status.percentage_used:.1f}% of {status.period} budget used (${status.current_spending:.2f} / ${status.budget_limit:.2f})"
        elif alert_level == AlertLevel.WARNING:
            message = f"⚠️ WARNING: {status.percentage_used:.1f}% of {status.period} budget used (${status.current_spending:.2f} / ${status.budget_limit:.2f})"
        else:
            message = f"ℹ️ INFO: {status.percentage_used:.1f}% of {status.period} budget used (${status.current_spending:.2f} / ${status.budget_limit:.2f})"

        # Generate recommendations
        recommendations = self._generate_recommendations(status, budget_config, alert_level)

        alert = BudgetAlert(
            timestamp=datetime.now().isoformat(),
            level=alert_level.value,
            period=status.period,
            budget_limit=status.budget_limit,
            current_spending=status.current_spending,
            percentage_used=status.percentage_used,
            message=message,
            recommendations=recommendations
        )

        self.alert_history.append(alert)
        logger.warning(message)
        for rec in recommendations:
            logger.info(f"  → {rec}")

        return alert

    def _generate_recommendations(
        self,
        status: BudgetStatus,
        budget_config: BudgetConfig,
        alert_level: AlertLevel
    ) -> List[str]:
        """Generate cost optimization recommendations"""
        recommendations = []

        if alert_level == AlertLevel.EXCEEDED:
            recommendations.append("IMMEDIATE: Budget exceeded - all AI operations will use cheapest model (Haiku)")
            recommendations.append("Consider increasing budget limit or reducing AI usage")
            recommendations.append("Review recent high-cost operations for optimization opportunities")

        elif alert_level == AlertLevel.CRITICAL:
            if budget_config.auto_downgrade:
                recommendations.append("AUTO-DOWNGRADE ACTIVE: Switching to cost-optimized models")
                recommendations.append("Opus → Sonnet, Sonnet → Haiku for remaining operations")

            recommendations.append(f"Only ${status.remaining_budget:.2f} remaining in budget")
            recommendations.append("Prioritize essential operations only")

            if status.forecasted_spending and status.forecasted_spending > status.budget_limit:
                overage = status.forecasted_spending - status.budget_limit
                recommendations.append(f"FORECAST: Budget will exceed by ${overage:.2f} at current rate")

        elif alert_level == AlertLevel.WARNING:
            recommendations.append("Consider enabling auto-downgrade for cost optimization")
            recommendations.append("Review agent model assignments for potential savings")
            recommendations.append("Use Fast performance profile for non-critical tasks")

            if status.forecasted_spending:
                recommendations.append(f"Forecasted total: ${status.forecasted_spending:.2f}")

        else:  # INFO
            recommendations.append(f"${status.remaining_budget:.2f} remaining in {status.period} budget")
            if status.days_remaining:
                daily_budget = status.remaining_budget / max(status.days_remaining, 1)
                recommendations.append(f"~${daily_budget:.2f} available per day for remainder of period")

        return recommendations

    def should_downgrade_model(self, period: BudgetPeriod = BudgetPeriod.DAILY) -> bool:
        """Check if auto-downgrade should be triggered"""
        budget_config = self.budgets.get(period.value)
        if not budget_config or not budget_config.auto_downgrade:
            return False

        status = self.check_budget(period)
        alert_level = AlertLevel(status.alert_level)

        # Downgrade if critical or exceeded
        return alert_level in [AlertLevel.CRITICAL, AlertLevel.EXCEEDED]

    def get_budget_report(self, include_all_periods: bool = True) -> Dict:
        """Generate comprehensive budget report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "periods": {}
        }

        periods_to_check = [BudgetPeriod.DAILY, BudgetPeriod.WEEKLY, BudgetPeriod.MONTHLY] if include_all_periods else [BudgetPeriod.DAILY]

        for period in periods_to_check:
            try:
                status = self.check_budget(period)
                report["periods"][period.value] = asdict(status)
            except Exception as e:
                logger.error(f"Error checking {period.value} budget: {e}")

        # Add alert summary
        report["alert_summary"] = {
            "total_alerts": len(self.alert_history),
            "critical_alerts": len([a for a in self.alert_history if a.level == AlertLevel.CRITICAL.value]),
            "exceeded_alerts": len([a for a in self.alert_history if a.level == AlertLevel.EXCEEDED.value])
        }

        return report

    def export_alerts(self, output_file: str):
        """Export alert history to JSON file"""
        data = {
            "export_timestamp": datetime.now().isoformat(),
            "alert_count": len(self.alert_history),
            "alerts": [asdict(a) for a in self.alert_history]
        }

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        logger.info(f"Exported {len(self.alert_history)} alerts to {output_file}")


# Example usage and testing
if __name__ == "__main__":
    # Mock cost tracker for testing
    class MockCostTracker:
        class CostDimension(Enum):
            DATE = "date"

        def get_summary(self, dimension, start_date=None, end_date=None):
            from dataclasses import dataclass

            @dataclass
            class MockSummary:
                total_cost: float = 7.5  # Simulated spending

            return [MockSummary()]

    manager = BudgetManager(cost_tracker=MockCostTracker())

    print("\n=== Budget Status Check ===")
    status = manager.check_budget(BudgetPeriod.DAILY)
    print(f"Period: {status.period}")
    print(f"Budget: ${status.budget_limit:.2f}")
    print(f"Spent: ${status.current_spending:.2f} ({status.percentage_used:.1f}%)")
    print(f"Remaining: ${status.remaining_budget:.2f}")
    print(f"Alert Level: {status.alert_level}")

    if status.forecasted_spending:
        print(f"Forecasted Total: ${status.forecasted_spending:.2f}")

    print("\n=== Budget Report ===")
    report = manager.get_budget_report()
    print(json.dumps(report, indent=2))
