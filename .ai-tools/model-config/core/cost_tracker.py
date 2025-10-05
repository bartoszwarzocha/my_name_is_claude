#!/usr/bin/env python3
"""
Cost Tracking System for Claude Code Multi-Agent Framework

Tracks costs across multiple dimensions:
- Per-agent cost tracking
- Per-project cost tracking
- Per-session cost tracking
- Token usage statistics
- Model usage distribution

Part of Framework v3.6.0 - Intelligent Model Configuration System
"""

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from pathlib import Path
from enum import Enum
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CostDimension(Enum):
    """Cost tracking dimensions"""
    AGENT = "agent"
    PROJECT = "project"
    SESSION = "session"
    MODEL = "model"
    DATE = "date"


@dataclass
class TokenUsage:
    """Token usage record"""
    input_tokens: int
    output_tokens: int
    total_tokens: int
    model_type: str


@dataclass
class CostRecord:
    """Individual cost record"""
    timestamp: str
    agent_type: str
    model_type: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float
    project_id: Optional[str] = None
    session_id: Optional[str] = None
    task_description: Optional[str] = None


@dataclass
class CostSummary:
    """Aggregated cost summary"""
    dimension: str
    dimension_value: str
    total_cost: float
    total_tokens: int
    input_tokens: int
    output_tokens: int
    model_distribution: Dict[str, int]
    record_count: int
    average_cost_per_operation: float
    time_period: str


class CostTracker:
    """
    Comprehensive cost tracking system for AI model usage.

    Features:
    - Real-time cost tracking
    - Multi-dimensional analysis (agent, project, session, model, date)
    - Token usage statistics
    - Cost breakdown by model type
    - Historical trend analysis
    - Export capabilities for reporting
    """

    def __init__(self, data_dir: Optional[str] = None):
        """Initialize cost tracker with data directory"""
        self.data_dir = data_dir or self._get_default_data_dir()
        self._ensure_data_directory()

        # Cost records database (in-memory + persistent)
        self.cost_records: List[CostRecord] = []
        self._load_historical_records()

        # Model pricing (USD per 1M tokens)
        self.model_costs = {
            "claude-opus-4": {"input": 15.0, "output": 75.0},
            "claude-sonnet-4-5": {"input": 3.0, "output": 15.0},
            "claude-haiku-4": {"input": 0.25, "output": 1.25}
        }

    def _get_default_data_dir(self) -> str:
        """Get default data directory"""
        framework_root = Path(__file__).parent.parent.parent.parent
        data_dir = framework_root / ".ai-tools" / "model-config" / "data"
        return str(data_dir)

    def _ensure_data_directory(self):
        """Ensure data directory exists"""
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "daily"), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "monthly"), exist_ok=True)

    def _load_historical_records(self):
        """Load historical cost records from disk"""
        try:
            # Load current session records
            current_file = os.path.join(self.data_dir, "current_session.json")
            if os.path.exists(current_file):
                with open(current_file, 'r') as f:
                    data = json.load(f)
                    self.cost_records = [CostRecord(**record) for record in data.get("records", [])]
                    logger.info(f"Loaded {len(self.cost_records)} historical cost records")
        except Exception as e:
            logger.warning(f"Could not load historical records: {e}")
            self.cost_records = []

    def track_usage(
        self,
        agent_type: str,
        model_type: str,
        input_tokens: int,
        output_tokens: int,
        project_id: Optional[str] = None,
        session_id: Optional[str] = None,
        task_description: Optional[str] = None
    ) -> CostRecord:
        """
        Track AI model usage and calculate costs.

        Args:
            agent_type: Agent that used the model
            model_type: Model used (opus/sonnet/haiku)
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            project_id: Optional project identifier
            session_id: Optional session identifier
            task_description: Optional task description

        Returns:
            CostRecord with cost breakdown
        """
        # Calculate costs
        costs = self.model_costs.get(model_type, self.model_costs["claude-sonnet-4-5"])

        input_cost = (input_tokens / 1_000_000) * costs["input"]
        output_cost = (output_tokens / 1_000_000) * costs["output"]
        total_cost = input_cost + output_cost
        total_tokens = input_tokens + output_tokens

        # Create cost record
        record = CostRecord(
            timestamp=datetime.now().isoformat(),
            agent_type=agent_type,
            model_type=model_type,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            input_cost=input_cost,
            output_cost=output_cost,
            total_cost=total_cost,
            project_id=project_id,
            session_id=session_id,
            task_description=task_description
        )

        # Add to records
        self.cost_records.append(record)

        # Persist to disk
        self._save_current_session()

        # Archive daily if needed
        self._archive_if_needed()

        logger.info(f"Tracked: {agent_type} used {model_type} - ${total_cost:.4f} ({total_tokens} tokens)")

        return record

    def get_summary(
        self,
        dimension: CostDimension,
        dimension_value: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[CostSummary]:
        """
        Get cost summary for specified dimension and time period.

        Args:
            dimension: Dimension to summarize by (agent/project/session/model/date)
            dimension_value: Optional specific value to filter by
            start_date: Optional start date for filtering
            end_date: Optional end date for filtering

        Returns:
            List of CostSummary objects
        """
        # Filter records by date range
        filtered_records = self._filter_by_date_range(start_date, end_date)

        # Filter by dimension value if specified
        if dimension_value:
            filtered_records = self._filter_by_dimension(filtered_records, dimension, dimension_value)

        # Group by dimension
        grouped = self._group_by_dimension(filtered_records, dimension)

        # Create summaries
        summaries = []
        for key, records in grouped.items():
            summary = self._create_summary(dimension, key, records, start_date, end_date)
            summaries.append(summary)

        # Sort by total cost descending
        summaries.sort(key=lambda x: x.total_cost, reverse=True)

        return summaries

    def _filter_by_date_range(
        self,
        start_date: Optional[datetime],
        end_date: Optional[datetime]
    ) -> List[CostRecord]:
        """Filter records by date range"""
        if not start_date and not end_date:
            return self.cost_records

        filtered = []
        for record in self.cost_records:
            record_date = datetime.fromisoformat(record.timestamp)

            if start_date and record_date < start_date:
                continue
            if end_date and record_date > end_date:
                continue

            filtered.append(record)

        return filtered

    def _filter_by_dimension(
        self,
        records: List[CostRecord],
        dimension: CostDimension,
        value: str
    ) -> List[CostRecord]:
        """Filter records by dimension value"""
        if dimension == CostDimension.AGENT:
            return [r for r in records if r.agent_type == value]
        elif dimension == CostDimension.PROJECT:
            return [r for r in records if r.project_id == value]
        elif dimension == CostDimension.SESSION:
            return [r for r in records if r.session_id == value]
        elif dimension == CostDimension.MODEL:
            return [r for r in records if r.model_type == value]
        else:
            return records

    def _group_by_dimension(
        self,
        records: List[CostRecord],
        dimension: CostDimension
    ) -> Dict[str, List[CostRecord]]:
        """Group records by dimension"""
        grouped: Dict[str, List[CostRecord]] = {}

        for record in records:
            if dimension == CostDimension.AGENT:
                key = record.agent_type
            elif dimension == CostDimension.PROJECT:
                key = record.project_id or "unknown"
            elif dimension == CostDimension.SESSION:
                key = record.session_id or "unknown"
            elif dimension == CostDimension.MODEL:
                key = record.model_type
            elif dimension == CostDimension.DATE:
                # Group by date (YYYY-MM-DD)
                key = record.timestamp[:10]
            else:
                key = "unknown"

            if key not in grouped:
                grouped[key] = []
            grouped[key].append(record)

        return grouped

    def _create_summary(
        self,
        dimension: CostDimension,
        key: str,
        records: List[CostRecord],
        start_date: Optional[datetime],
        end_date: Optional[datetime]
    ) -> CostSummary:
        """Create cost summary from records"""
        total_cost = sum(r.total_cost for r in records)
        total_tokens = sum(r.total_tokens for r in records)
        input_tokens = sum(r.input_tokens for r in records)
        output_tokens = sum(r.output_tokens for r in records)

        # Model distribution
        model_dist: Dict[str, int] = {}
        for record in records:
            model = record.model_type
            model_dist[model] = model_dist.get(model, 0) + 1

        # Average cost per operation
        avg_cost = total_cost / len(records) if records else 0.0

        # Time period string
        if start_date and end_date:
            time_period = f"{start_date.date()} to {end_date.date()}"
        elif start_date:
            time_period = f"From {start_date.date()}"
        elif end_date:
            time_period = f"Until {end_date.date()}"
        else:
            time_period = "All time"

        return CostSummary(
            dimension=dimension.value,
            dimension_value=key,
            total_cost=total_cost,
            total_tokens=total_tokens,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            model_distribution=model_dist,
            record_count=len(records),
            average_cost_per_operation=avg_cost,
            time_period=time_period
        )

    def get_daily_costs(self, days: int = 7) -> Dict[str, float]:
        """Get daily costs for last N days"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        summaries = self.get_summary(
            CostDimension.DATE,
            start_date=start_date,
            end_date=end_date
        )

        return {s.dimension_value: s.total_cost for s in summaries}

    def get_agent_costs(self, project_id: Optional[str] = None) -> Dict[str, float]:
        """Get costs by agent type"""
        summaries = self.get_summary(CostDimension.AGENT)

        # Filter by project if specified
        if project_id:
            summaries = [s for s in summaries if self._summary_matches_project(s, project_id)]

        return {s.dimension_value: s.total_cost for s in summaries}

    def get_model_distribution(self) -> Dict[str, Dict[str, any]]:
        """Get usage distribution by model type"""
        summaries = self.get_summary(CostDimension.MODEL)

        distribution = {}
        total_cost = sum(s.total_cost for s in summaries)
        total_operations = sum(s.record_count for s in summaries)

        for summary in summaries:
            distribution[summary.dimension_value] = {
                "total_cost": summary.total_cost,
                "operations": summary.record_count,
                "percentage_cost": (summary.total_cost / total_cost * 100) if total_cost > 0 else 0,
                "percentage_operations": (summary.record_count / total_operations * 100) if total_operations > 0 else 0,
                "avg_cost_per_operation": summary.average_cost_per_operation
            }

        return distribution

    def _summary_matches_project(self, summary: CostSummary, project_id: str) -> bool:
        """Check if summary contains records for project"""
        # This is a simplified check - in practice would need to filter records
        return True  # TODO: Implement proper filtering

    def _save_current_session(self):
        """Save current session records to disk"""
        try:
            current_file = os.path.join(self.data_dir, "current_session.json")
            data = {
                "session_start": datetime.now().isoformat(),
                "record_count": len(self.cost_records),
                "records": [asdict(r) for r in self.cost_records]
            }

            with open(current_file, 'w') as f:
                json.dump(data, f, indent=2)

        except Exception as e:
            logger.error(f"Error saving current session: {e}")

    def _archive_if_needed(self):
        """Archive old records to daily/monthly files"""
        # Archive records older than 1 day to daily files
        now = datetime.now()
        cutoff = now - timedelta(days=1)

        to_archive = []
        to_keep = []

        for record in self.cost_records:
            record_date = datetime.fromisoformat(record.timestamp)
            if record_date < cutoff:
                to_archive.append(record)
            else:
                to_keep.append(record)

        if to_archive:
            self._archive_records(to_archive)
            self.cost_records = to_keep
            logger.info(f"Archived {len(to_archive)} old cost records")

    def _archive_records(self, records: List[CostRecord]):
        """Archive records to daily file"""
        # Group by date
        by_date: Dict[str, List[CostRecord]] = {}
        for record in records:
            date = record.timestamp[:10]  # YYYY-MM-DD
            if date not in by_date:
                by_date[date] = []
            by_date[date].append(record)

        # Save to daily files
        for date, date_records in by_date.items():
            daily_file = os.path.join(self.data_dir, "daily", f"{date}.json")

            try:
                # Load existing if present
                existing = []
                if os.path.exists(daily_file):
                    with open(daily_file, 'r') as f:
                        data = json.load(f)
                        existing = [CostRecord(**r) for r in data.get("records", [])]

                # Merge and save
                all_records = existing + date_records
                data = {
                    "date": date,
                    "record_count": len(all_records),
                    "total_cost": sum(r.total_cost for r in all_records),
                    "records": [asdict(r) for r in all_records]
                }

                with open(daily_file, 'w') as f:
                    json.dump(data, f, indent=2)

            except Exception as e:
                logger.error(f"Error archiving to {daily_file}: {e}")

    def export_to_csv(self, output_file: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        """Export cost records to CSV file"""
        import csv

        records = self._filter_by_date_range(start_date, end_date)

        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow([
                "Timestamp", "Agent Type", "Model Type",
                "Input Tokens", "Output Tokens", "Total Tokens",
                "Input Cost", "Output Cost", "Total Cost",
                "Project ID", "Session ID", "Task Description"
            ])

            # Records
            for record in records:
                writer.writerow([
                    record.timestamp, record.agent_type, record.model_type,
                    record.input_tokens, record.output_tokens, record.total_tokens,
                    f"{record.input_cost:.6f}", f"{record.output_cost:.6f}", f"{record.total_cost:.6f}",
                    record.project_id or "", record.session_id or "", record.task_description or ""
                ])

        logger.info(f"Exported {len(records)} records to {output_file}")


# Example usage and testing
if __name__ == "__main__":
    tracker = CostTracker()

    # Test tracking
    print("\n=== Testing Cost Tracking ===")

    # Track some usage
    record1 = tracker.track_usage(
        agent_type="software-architect",
        model_type="claude-opus-4",
        input_tokens=50000,
        output_tokens=15000,
        project_id="my-project",
        task_description="Architecture design"
    )
    print(f"Record 1: ${record1.total_cost:.4f}")

    record2 = tracker.track_usage(
        agent_type="backend-engineer",
        model_type="claude-sonnet-4-5",
        input_tokens=30000,
        output_tokens=10000,
        project_id="my-project",
        task_description="API implementation"
    )
    print(f"Record 2: ${record2.total_cost:.4f}")

    # Get summaries
    print("\n=== Agent Cost Summary ===")
    agent_summaries = tracker.get_summary(CostDimension.AGENT)
    for summary in agent_summaries:
        print(f"{summary.dimension_value}: ${summary.total_cost:.4f} ({summary.record_count} operations)")

    print("\n=== Model Distribution ===")
    model_dist = tracker.get_model_distribution()
    for model, stats in model_dist.items():
        print(f"{model}:")
        print(f"  Cost: ${stats['total_cost']:.4f} ({stats['percentage_cost']:.1f}%)")
        print(f"  Operations: {stats['operations']} ({stats['percentage_operations']:.1f}%)")
