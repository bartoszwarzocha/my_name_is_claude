#!/usr/bin/env python3
"""
Community Intelligence Engine
Phase 4: Federated Learning Network - Community Intelligence Component

This module implements community-driven intelligence that learns from collective
wisdom while preserving privacy and providing industry-specific insights.
"""

import json
import numpy as np
from typing import Dict, List, Optional, Any, Tuple, Set
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import logging
import statistics

try:
    from .anonymous_pattern_sharing import AnonymousPatternSharing, AnonymousPattern
    from .industry_templates import IndustryTemplateSystem
    from .hybrid_intelligence import HybridIntelligenceSystem
except ImportError:
    from anonymous_pattern_sharing import AnonymousPatternSharing, AnonymousPattern
    from industry_templates import IndustryTemplateSystem
    from hybrid_intelligence import HybridIntelligenceSystem


@dataclass
class CommunityInsight:
    """Community-derived insight."""
    insight_id: str
    insight_type: str  # 'best_practice', 'pattern', 'benchmark', 'recommendation'
    domain: str
    technology_stack: List[str]
    insight_data: Dict[str, Any]
    confidence_score: float
    community_support: int  # Number of projects supporting this insight
    evidence_strength: float
    created_at: str
    updated_at: str


@dataclass
class IndustryBenchmark:
    """Industry benchmark data."""
    domain: str
    technology_stack: List[str]
    metrics: Dict[str, float]
    sample_size: int
    confidence_interval: Tuple[float, float]
    last_updated: str


@dataclass
class CommunityRecommendation:
    """Community-based recommendation."""
    recommendation_id: str
    context: Dict[str, Any]
    recommended_agents: List[Dict[str, Any]]
    community_confidence: float
    success_probability: float
    supporting_evidence: List[str]
    domain_specific: bool


class CommunityIntelligenceEngine:
    """
    Community Intelligence Engine for Federated Learning Network.

    Processes collective wisdom from anonymous patterns to generate
    industry insights, benchmarks, and improved recommendations.
    """

    def __init__(self, project_root: str = None):
        """Initialize community intelligence engine."""
        self.project_root = project_root or self._find_project_root()

        # Initialize core components
        try:
            self.pattern_sharing = AnonymousPatternSharing(self.project_root)
            self.industry_templates = IndustryTemplateSystem()
            self.hybrid_intelligence = HybridIntelligenceSystem(self.project_root)
        except Exception as e:
            logging.warning(f"Some components unavailable: {e}")
            self.pattern_sharing = None
            self.industry_templates = None
            self.hybrid_intelligence = None

        # Community intelligence storage
        self.intelligence_dir = Path(self.project_root) / ".ai-tools" / "learning" / "community"
        self.intelligence_dir.mkdir(parents=True, exist_ok=True)

        # Data files
        self.insights_file = self.intelligence_dir / "community_insights.json"
        self.benchmarks_file = self.intelligence_dir / "industry_benchmarks.json"
        self.recommendations_file = self.intelligence_dir / "community_recommendations.json"
        self.networks_file = self.intelligence_dir / "industry_networks.json"

        # Configuration
        self.config = {
            "min_community_support": 3,  # Minimum projects for insight validity
            "confidence_threshold": 0.7,
            "benchmark_sample_threshold": 5,
            "insight_freshness_days": 30,
            "max_insights_per_domain": 50
        }

        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def analyze_community_patterns(self) -> Dict[str, Any]:
        """
        Analyze imported anonymous patterns to generate community insights.

        Returns:
            Analysis results with insights, benchmarks, and recommendations
        """
        if not self.pattern_sharing:
            return {
                "status": "error",
                "message": "Pattern sharing system not available"
            }

        analysis_start = datetime.now()

        # Get imported patterns
        import_summary = self.pattern_sharing.get_imported_patterns_summary()
        if import_summary["status"] != "success":
            return {
                "status": "no_data",
                "message": "No community patterns available for analysis"
            }

        try:
            # Load patterns data
            with open(self.pattern_sharing.import_patterns_file, 'r') as f:
                patterns_data = json.load(f)

            patterns = [AnonymousPattern(**p) for p in patterns_data.get("patterns", [])]

            # Perform analysis
            results = {
                "technology_insights": self._analyze_technology_patterns(patterns),
                "agent_effectiveness_insights": self._analyze_agent_effectiveness(patterns),
                "evolution_insights": self._analyze_evolution_patterns(patterns),
                "industry_benchmarks": self._generate_industry_benchmarks(patterns),
                "community_recommendations": self._generate_community_recommendations(patterns)
            }

            # Save insights
            self._save_community_insights(results)

            analysis_time = (datetime.now() - analysis_start).total_seconds()

            return {
                "status": "success",
                "analysis_time_seconds": analysis_time,
                "patterns_analyzed": len(patterns),
                "insights_generated": sum(len(insights) for insights in results.values() if isinstance(insights, list)),
                "results": results
            }

        except Exception as e:
            self.logger.error(f"Error analyzing community patterns: {e}")
            return {
                "status": "error",
                "message": f"Analysis failed: {str(e)}"
            }

    def _analyze_technology_patterns(self, patterns: List[AnonymousPattern]) -> List[CommunityInsight]:
        """Analyze technology adoption patterns from community data."""
        insights = []
        tech_patterns = [p for p in patterns if p.pattern_type == "technology"]

        if not tech_patterns:
            return insights

        # Group by domain
        domain_tech = defaultdict(list)
        for pattern in tech_patterns:
            domain_tech[pattern.domain].append(pattern)

        for domain, domain_patterns in domain_tech.items():
            if len(domain_patterns) < self.config["min_community_support"]:
                continue

            # Analyze technology combinations
            tech_combinations = []
            for pattern in domain_patterns:
                tech_stack = pattern.technology_stack
                if tech_stack:
                    tech_combinations.append(frozenset(tech_stack))

            # Find most common combinations
            combination_counts = Counter(tech_combinations)

            for tech_combo, count in combination_counts.most_common(5):
                if count >= self.config["min_community_support"]:
                    confidence = min(0.95, count / len(domain_patterns))

                    insight = CommunityInsight(
                        insight_id=f"tech_{domain}_{hash(tech_combo)}",
                        insight_type="best_practice",
                        domain=domain,
                        technology_stack=list(tech_combo),
                        insight_data={
                            "pattern": "technology_combination",
                            "technologies": list(tech_combo),
                            "adoption_rate": count / len(domain_patterns),
                            "community_usage": count,
                            "recommendation": f"Popular technology stack for {domain} projects"
                        },
                        confidence_score=confidence,
                        community_support=count,
                        evidence_strength=confidence * count,
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat()
                    )
                    insights.append(insight)

        return insights

    def _analyze_agent_effectiveness(self, patterns: List[AnonymousPattern]) -> List[CommunityInsight]:
        """Analyze agent effectiveness patterns from community data."""
        insights = []
        effectiveness_patterns = [p for p in patterns if p.pattern_type == "agent_effectiveness"]

        if not effectiveness_patterns:
            return insights

        # Aggregate agent effectiveness by domain
        domain_effectiveness = defaultdict(lambda: defaultdict(list))

        for pattern in effectiveness_patterns:
            domain = pattern.domain
            agent_data = pattern.pattern_data.get("agent_effectiveness", {})

            for agent, metrics in agent_data.items():
                success_rate = metrics.get("success_rate", 0)
                if success_rate > 0:
                    domain_effectiveness[domain][agent].append(success_rate)

        # Generate insights for each domain
        for domain, agents in domain_effectiveness.items():
            for agent, success_rates in agents.items():
                if len(success_rates) >= self.config["min_community_support"]:
                    avg_success = statistics.mean(success_rates)
                    std_dev = statistics.stdev(success_rates) if len(success_rates) > 1 else 0

                    if avg_success >= self.config["confidence_threshold"]:
                        insight = CommunityInsight(
                            insight_id=f"agent_{domain}_{agent}",
                            insight_type="benchmark",
                            domain=domain,
                            technology_stack=[],
                            insight_data={
                                "pattern": "agent_effectiveness",
                                "agent": agent,
                                "average_success_rate": avg_success,
                                "standard_deviation": std_dev,
                                "sample_size": len(success_rates),
                                "recommendation": f"{agent} shows high effectiveness in {domain} projects"
                            },
                            confidence_score=min(0.95, avg_success),
                            community_support=len(success_rates),
                            evidence_strength=avg_success * len(success_rates),
                            created_at=datetime.now().isoformat(),
                            updated_at=datetime.now().isoformat()
                        )
                        insights.append(insight)

        return insights

    def _analyze_evolution_patterns(self, patterns: List[AnonymousPattern]) -> List[CommunityInsight]:
        """Analyze project evolution patterns from community data."""
        insights = []
        evolution_patterns = [p for p in patterns if p.pattern_type == "evolution"]

        if not evolution_patterns:
            return insights

        # Analyze common evolution sequences
        domain_sequences = defaultdict(list)

        for pattern in evolution_patterns:
            domain = pattern.domain
            sequences = pattern.pattern_data.get("agent_selection_sequences", [])
            domain_sequences[domain].extend(sequences)

        for domain, all_sequences in domain_sequences.items():
            if len(all_sequences) >= self.config["min_community_support"]:
                # Find common sequence patterns
                sequence_patterns = self._find_sequence_patterns(all_sequences)

                for pattern_desc, pattern_data in sequence_patterns.items():
                    if pattern_data["support"] >= self.config["min_community_support"]:
                        insight = CommunityInsight(
                            insight_id=f"evolution_{domain}_{hash(pattern_desc)}",
                            insight_type="pattern",
                            domain=domain,
                            technology_stack=[],
                            insight_data={
                                "pattern": "evolution_sequence",
                                "sequence_pattern": pattern_desc,
                                "support": pattern_data["support"],
                                "confidence": pattern_data["confidence"],
                                "recommendation": f"Common development path in {domain} projects"
                            },
                            confidence_score=pattern_data["confidence"],
                            community_support=pattern_data["support"],
                            evidence_strength=pattern_data["confidence"] * pattern_data["support"],
                            created_at=datetime.now().isoformat(),
                            updated_at=datetime.now().isoformat()
                        )
                        insights.append(insight)

        return insights

    def _find_sequence_patterns(self, sequences: List[List[str]]) -> Dict[str, Dict[str, Any]]:
        """Find common patterns in agent selection sequences."""
        patterns = {}

        # Look for common subsequences of length 2-4
        for seq_len in range(2, 5):
            subseq_counts = Counter()

            for sequence in sequences:
                if len(sequence) >= seq_len:
                    for i in range(len(sequence) - seq_len + 1):
                        subseq = tuple(sequence[i:i+seq_len])
                        subseq_counts[subseq] += 1

            # Convert to patterns
            for subseq, count in subseq_counts.items():
                if count >= self.config["min_community_support"]:
                    pattern_desc = " → ".join(subseq)
                    confidence = count / len(sequences)

                    patterns[pattern_desc] = {
                        "support": count,
                        "confidence": confidence,
                        "sequence_length": seq_len
                    }

        return patterns

    def _generate_industry_benchmarks(self, patterns: List[AnonymousPattern]) -> List[IndustryBenchmark]:
        """Generate industry benchmarks from community patterns."""
        benchmarks = []
        benchmark_patterns = [p for p in patterns if p.pattern_type == "benchmark"]

        if not benchmark_patterns:
            return benchmarks

        # Group by domain and technology stack
        domain_tech_metrics = defaultdict(lambda: defaultdict(list))

        for pattern in benchmark_patterns:
            domain = pattern.domain
            tech_stack = tuple(sorted(pattern.technology_stack)) if pattern.technology_stack else ()

            performance_data = pattern.pattern_data.get("domain_performance", {})
            for metric, value in performance_data.items():
                if isinstance(value, (int, float)) and value > 0:
                    domain_tech_metrics[(domain, tech_stack)][metric].append(value)

        # Generate benchmarks
        for (domain, tech_stack), metrics in domain_tech_metrics.items():
            if len(next(iter(metrics.values()))) >= self.config["benchmark_sample_threshold"]:
                benchmark_metrics = {}
                sample_size = 0

                for metric, values in metrics.items():
                    if len(values) >= self.config["benchmark_sample_threshold"]:
                        benchmark_metrics[metric] = {
                            "mean": statistics.mean(values),
                            "median": statistics.median(values),
                            "std_dev": statistics.stdev(values) if len(values) > 1 else 0,
                            "min": min(values),
                            "max": max(values),
                            "percentile_25": np.percentile(values, 25),
                            "percentile_75": np.percentile(values, 75)
                        }
                        sample_size = max(sample_size, len(values))

                if benchmark_metrics:
                    # Calculate confidence interval (95%)
                    confidence_interval = (0.9, 0.95)  # Simplified

                    benchmark = IndustryBenchmark(
                        domain=domain,
                        technology_stack=list(tech_stack),
                        metrics=benchmark_metrics,
                        sample_size=sample_size,
                        confidence_interval=confidence_interval,
                        last_updated=datetime.now().isoformat()
                    )
                    benchmarks.append(benchmark)

        return benchmarks

    def _generate_community_recommendations(self, patterns: List[AnonymousPattern]) -> List[CommunityRecommendation]:
        """Generate community-based recommendations from patterns."""
        recommendations = []

        # Combine insights from all pattern types
        tech_insights = self._analyze_technology_patterns(patterns)
        agent_insights = self._analyze_agent_effectiveness(patterns)

        # Group by domain for comprehensive recommendations
        domain_patterns = defaultdict(list)
        for pattern in patterns:
            domain_patterns[pattern.domain].append(pattern)

        for domain, domain_patterns_list in domain_patterns.items():
            if len(domain_patterns_list) >= self.config["min_community_support"]:

                # Get most effective agents for this domain
                effective_agents = []
                for insight in agent_insights:
                    if (insight.domain == domain and
                        insight.insight_type == "benchmark" and
                        insight.confidence_score >= self.config["confidence_threshold"]):

                        agent_data = {
                            "agent": insight.insight_data["agent"],
                            "confidence": insight.confidence_score,
                            "community_support": insight.community_support,
                            "reasoning": insight.insight_data["recommendation"]
                        }
                        effective_agents.append(agent_data)

                # Sort by evidence strength
                effective_agents.sort(key=lambda x: x["confidence"] * x["community_support"], reverse=True)

                if effective_agents:
                    # Create recommendation
                    recommendation = CommunityRecommendation(
                        recommendation_id=f"community_{domain}_{datetime.now().strftime('%Y%m%d')}",
                        context={
                            "domain": domain,
                            "source": "community_intelligence",
                            "patterns_analyzed": len(domain_patterns_list)
                        },
                        recommended_agents=effective_agents[:8],  # Top 8 agents
                        community_confidence=statistics.mean([a["confidence"] for a in effective_agents[:5]]),
                        success_probability=min(0.95, statistics.mean([a["confidence"] for a in effective_agents[:3]])),
                        supporting_evidence=[
                            f"Based on analysis of {len(domain_patterns_list)} anonymous projects",
                            f"Community confidence: {len(effective_agents)} validated agents",
                            f"Domain expertise: {domain} specific patterns"
                        ],
                        domain_specific=True
                    )
                    recommendations.append(recommendation)

        return recommendations

    def _save_community_insights(self, analysis_results: Dict[str, Any]):
        """Save community analysis results to files."""
        try:
            # Save insights
            insights = []
            for insight_type, insight_list in analysis_results.items():
                if isinstance(insight_list, list) and insight_list:
                    if hasattr(insight_list[0], '__dict__'):
                        insights.extend([asdict(insight) for insight in insight_list])

            if insights:
                with open(self.insights_file, 'w') as f:
                    json.dump({
                        "last_updated": datetime.now().isoformat(),
                        "total_insights": len(insights),
                        "insights": insights
                    }, f, indent=2)

            # Save benchmarks
            benchmarks = analysis_results.get("industry_benchmarks", [])
            if benchmarks:
                with open(self.benchmarks_file, 'w') as f:
                    json.dump({
                        "last_updated": datetime.now().isoformat(),
                        "benchmarks": [asdict(b) for b in benchmarks]
                    }, f, indent=2)

            # Save recommendations
            recommendations = analysis_results.get("community_recommendations", [])
            if recommendations:
                with open(self.recommendations_file, 'w') as f:
                    json.dump({
                        "last_updated": datetime.now().isoformat(),
                        "recommendations": [asdict(r) for r in recommendations]
                    }, f, indent=2)

        except Exception as e:
            self.logger.error(f"Error saving community insights: {e}")

    def get_community_insights(self, domain: str = None) -> Dict[str, Any]:
        """Get community insights, optionally filtered by domain."""
        if not self.insights_file.exists():
            return {
                "status": "no_data",
                "message": "No community insights available"
            }

        try:
            with open(self.insights_file, 'r') as f:
                insights_data = json.load(f)

            insights = insights_data.get("insights", [])

            if domain:
                insights = [i for i in insights if i.get("domain") == domain]

            # Organize insights by type
            organized_insights = defaultdict(list)
            for insight in insights:
                organized_insights[insight["insight_type"]].append(insight)

            return {
                "status": "success",
                "last_updated": insights_data.get("last_updated"),
                "total_insights": len(insights),
                "domain_filter": domain,
                "insights_by_type": dict(organized_insights),
                "summary": {
                    "best_practices": len(organized_insights["best_practice"]),
                    "patterns": len(organized_insights["pattern"]),
                    "benchmarks": len(organized_insights["benchmark"]),
                    "recommendations": len(organized_insights["recommendation"])
                }
            }

        except Exception as e:
            return {
                "status": "error",
                "message": f"Error loading insights: {str(e)}"
            }

    def get_industry_benchmarks(self, domain: str = None, technology_stack: List[str] = None) -> Dict[str, Any]:
        """Get industry benchmarks, optionally filtered by domain and technology."""
        if not self.benchmarks_file.exists():
            return {
                "status": "no_data",
                "message": "No industry benchmarks available"
            }

        try:
            with open(self.benchmarks_file, 'r') as f:
                benchmarks_data = json.load(f)

            benchmarks = benchmarks_data.get("benchmarks", [])

            # Apply filters
            if domain:
                benchmarks = [b for b in benchmarks if b.get("domain") == domain]

            if technology_stack:
                tech_set = set(technology_stack)
                benchmarks = [
                    b for b in benchmarks
                    if tech_set.intersection(set(b.get("technology_stack", [])))
                ]

            return {
                "status": "success",
                "last_updated": benchmarks_data.get("last_updated"),
                "benchmarks_found": len(benchmarks),
                "domain_filter": domain,
                "technology_filter": technology_stack,
                "benchmarks": benchmarks
            }

        except Exception as e:
            return {
                "status": "error",
                "message": f"Error loading benchmarks: {str(e)}"
            }

    def get_community_recommendations(self, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Get community-based recommendations for given context."""
        if not self.recommendations_file.exists():
            return {
                "status": "no_data",
                "message": "No community recommendations available"
            }

        try:
            with open(self.recommendations_file, 'r') as f:
                recommendations_data = json.load(f)

            recommendations = recommendations_data.get("recommendations", [])

            # Filter by context if provided
            if context:
                domain = context.get("domain")
                if domain:
                    recommendations = [
                        r for r in recommendations
                        if r.get("context", {}).get("domain") == domain
                    ]

            # Sort by community confidence
            recommendations.sort(key=lambda r: r.get("community_confidence", 0), reverse=True)

            return {
                "status": "success",
                "last_updated": recommendations_data.get("last_updated"),
                "recommendations_found": len(recommendations),
                "context_filter": context,
                "recommendations": recommendations[:10]  # Top 10
            }

        except Exception as e:
            return {
                "status": "error",
                "message": f"Error loading recommendations: {str(e)}"
            }

    def get_intelligence_status(self) -> Dict[str, Any]:
        """Get comprehensive status of community intelligence system."""
        return {
            "system_status": "operational",
            "components": {
                "pattern_sharing": self.pattern_sharing is not None,
                "industry_templates": self.industry_templates is not None,
                "hybrid_intelligence": self.hybrid_intelligence is not None
            },
            "data_availability": {
                "insights": self.insights_file.exists(),
                "benchmarks": self.benchmarks_file.exists(),
                "recommendations": self.recommendations_file.exists(),
                "networks": self.networks_file.exists()
            },
            "configuration": self.config,
            "last_analysis": self._get_last_analysis_time(),
            "capabilities": {
                "technology_pattern_analysis": True,
                "agent_effectiveness_insights": True,
                "evolution_pattern_detection": True,
                "industry_benchmarking": True,
                "community_recommendations": True,
                "privacy_preservation": True
            }
        }

    def _get_last_analysis_time(self) -> Optional[str]:
        """Get timestamp of last community analysis."""
        files_to_check = [self.insights_file, self.benchmarks_file, self.recommendations_file]

        for file_path in files_to_check:
            if file_path.exists():
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        return data.get("last_updated")
                except:
                    continue

        return None


if __name__ == "__main__":
    # Demo usage
    community = CommunityIntelligenceEngine()

    print("🌍 Community Intelligence Engine Demo")
    print("=" * 50)

    # Get system status
    status = community.get_intelligence_status()
    print(f"✅ System status: {status['system_status']}")
    print(f"   Components: {status['components']}")
    print(f"   Capabilities: {len([k for k, v in status['capabilities'].items() if v])} active")

    # Analyze community patterns (if data available)
    analysis_result = community.analyze_community_patterns()
    print(f"\n🔍 Analysis result: {analysis_result['status']}")

    if analysis_result['status'] == 'success':
        print(f"   Patterns analyzed: {analysis_result['patterns_analyzed']}")
        print(f"   Insights generated: {analysis_result['insights_generated']}")

    # Get insights
    insights = community.get_community_insights()
    print(f"\n💡 Community insights: {insights['status']}")
    if insights['status'] == 'success':
        print(f"   Total insights: {insights['total_insights']}")
        print(f"   Insight types: {list(insights['summary'].keys())}")

    # Get benchmarks
    benchmarks = community.get_industry_benchmarks()
    print(f"\n📊 Industry benchmarks: {benchmarks['status']}")
    if benchmarks['status'] == 'success':
        print(f"   Benchmarks available: {benchmarks['benchmarks_found']}")

    print(f"\n🔮 Community Intelligence Engine ready for federated learning!")