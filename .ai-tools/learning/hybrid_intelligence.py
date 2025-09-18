#!/usr/bin/env python3
"""
Hybrid Intelligence System
Combines universal patterns with project-specific adaptive learning
"""

import json
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
from datetime import datetime

try:
    from .universal_patterns import UniversalPatternsSystem
    from .project_adaptive_learning import ProjectAdaptiveLearning
    from .user_choice_tracker import UserChoiceTracker
    from .agent_effectiveness_monitor import AgentEffectivenessMonitor
    from .incremental_model_updater import IncrementalModelUpdater
except ImportError:
    from universal_patterns import UniversalPatternsSystem
    from project_adaptive_learning import ProjectAdaptiveLearning
    from user_choice_tracker import UserChoiceTracker
    from agent_effectiveness_monitor import AgentEffectivenessMonitor
    from incremental_model_updater import IncrementalModelUpdater


class HybridIntelligenceSystem:
    """
    Advanced system that combines universal industry patterns with
    project-specific adaptive learning for optimal agent recommendations.
    """

    def __init__(self, project_root: str = None):
        """Initialize hybrid intelligence system."""
        self.project_root = project_root or self._find_project_root()

        # Initialize universal patterns system
        self.universal_system = UniversalPatternsSystem()

        # Initialize project-specific learning components
        self.adaptive_learning = ProjectAdaptiveLearning(self.project_root)
        self.choice_tracker = UserChoiceTracker(self.project_root)
        self.effectiveness_monitor = AgentEffectivenessMonitor(self.project_root)
        self.model_updater = IncrementalModelUpdater(self.project_root)

        # Hybrid intelligence configuration
        self.config = self._load_hybrid_config()

        # Learning state tracking
        self.learning_enabled = self._check_learning_readiness()

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def _load_hybrid_config(self) -> Dict[str, Any]:
        """Load hybrid intelligence configuration."""
        return {
            "universal_weight": 0.6,  # Weight for universal patterns
            "adaptive_weight": 0.4,   # Weight for adaptive learning
            "confidence_threshold": 0.5,
            "max_recommendations": 10,
            "learning_boost_factor": 1.2,  # Boost for agents with good learning data
            "universal_decay_factor": 0.9,  # Decay universal weight as learning improves
            "context_sensitivity": 0.8,
            "domain_specialization_bonus": 0.1,
            "effectiveness_threshold": 0.7,
            "alignment_threshold": 0.75
        }

    def _check_learning_readiness(self) -> bool:
        """Check if adaptive learning has sufficient data."""
        model_status = self.model_updater.get_model_status()
        return model_status.get('learning_data_available', {}).get('ready_for_learning', False)

    def get_hybrid_recommendations(self, project_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get hybrid recommendations combining universal patterns with adaptive learning.

        Args:
            project_context: Project context including technologies, domain, complexity

        Returns:
            List of agent recommendations with confidence scores and reasoning
        """
        # Get universal recommendations
        universal_recs = self.universal_system.get_universal_recommendations(project_context)

        if self.learning_enabled:
            # Get adaptive learning recommendations
            adaptive_recs = self._get_adaptive_recommendations(project_context)

            # Combine recommendations using hybrid approach
            combined_recs = self._combine_recommendations(
                universal_recs, adaptive_recs, project_context
            )
        else:
            # Use only universal patterns with initial project context
            combined_recs = self._format_universal_only(universal_recs, project_context)

        # Apply final filtering and ranking
        final_recs = self._finalize_recommendations(combined_recs, project_context)

        return final_recs

    def _get_adaptive_recommendations(self, context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """Get recommendations from adaptive learning system."""
        try:
            # Get base adaptive recommendations
            adaptive_agents = self.model_updater.get_personalized_recommendations(
                agents=self._get_available_agents(),
                context=context,
                top_k=15
            )

            recommendations = []
            for agent, confidence in adaptive_agents:
                reasoning = "Personalized based on your project patterns"

                # Enhance with effectiveness data
                performance = self.effectiveness_monitor.get_agent_performance(agent)
                if performance.get('overall_metrics', {}).get('total_uses', 0) > 0:
                    success_rate = performance['overall_metrics']['success_rate']
                    if success_rate >= self.config['effectiveness_threshold']:
                        confidence = min(confidence * 1.2, 1.0)  # Boost for effective agents
                        reasoning += f" (proven {success_rate:.0%} success rate)"

                recommendations.append((agent, confidence, reasoning))

            return recommendations

        except Exception as e:
            print(f"Warning: Adaptive recommendations failed: {e}")
            return []

    def _get_available_agents(self) -> List[str]:
        """Get list of available agents."""
        # This would typically come from the agent selector system
        # For now, return a comprehensive list
        return [
            'frontend-engineer', 'backend-engineer', 'api-engineer', 'data-engineer',
            'qa-engineer', 'security-engineer', 'deployment-engineer', 'devops-architect',
            'software-architect', 'ux-designer', 'product-manager', 'business-analyst',
            'database-administrator', 'cloud-engineer', 'automation-engineer',
            'performance-engineer', 'monitoring-engineer', 'compliance-auditor',
            'graphics-3d-engineer', 'graphics-2d-engineer', 'math-specialist',
            'electronics-engineer', 'embedded-engineer', 'desktop-specialist',
            'mobile-developer', 'project-owner', 'session-manager'
        ]

    def _combine_recommendations(self, universal_recs: List[Tuple[str, float, str]],
                               adaptive_recs: List[Tuple[str, float, str]],
                               context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Combine universal and adaptive recommendations."""
        agent_scores = {}

        # Calculate adaptive learning strength
        learning_stats = self.choice_tracker.get_choice_statistics()
        total_choices = learning_stats.get('total_choices', 0)
        alignment_rate = learning_stats.get('alignment_statistics', {}).get('overall_alignment_rate', 0)

        # Adjust weights based on learning quality
        if total_choices >= 10 and alignment_rate >= self.config['alignment_threshold']:
            # Strong adaptive learning - increase adaptive weight
            universal_weight = self.config['universal_weight'] * self.config['universal_decay_factor']
            adaptive_weight = self.config['adaptive_weight'] * 1.3
        elif total_choices >= 5:
            # Moderate adaptive learning - balanced weights
            universal_weight = self.config['universal_weight']
            adaptive_weight = self.config['adaptive_weight']
        else:
            # Weak adaptive learning - rely more on universal patterns
            universal_weight = self.config['universal_weight'] * 1.2
            adaptive_weight = self.config['adaptive_weight'] * 0.7

        # Normalize weights
        total_weight = universal_weight + adaptive_weight
        universal_weight /= total_weight
        adaptive_weight /= total_weight

        # Process universal recommendations
        for agent, confidence, reasoning in universal_recs:
            if agent not in agent_scores:
                agent_scores[agent] = {
                    'universal_score': 0,
                    'adaptive_score': 0,
                    'universal_reasons': [],
                    'adaptive_reasons': [],
                    'combined_score': 0,
                    'recommendation_sources': set()
                }

            agent_scores[agent]['universal_score'] = confidence
            agent_scores[agent]['universal_reasons'].append(reasoning)
            agent_scores[agent]['recommendation_sources'].add('universal')

        # Process adaptive recommendations
        for agent, confidence, reasoning in adaptive_recs:
            if agent not in agent_scores:
                agent_scores[agent] = {
                    'universal_score': 0,
                    'adaptive_score': 0,
                    'universal_reasons': [],
                    'adaptive_reasons': [],
                    'combined_score': 0,
                    'recommendation_sources': set()
                }

            agent_scores[agent]['adaptive_score'] = confidence
            agent_scores[agent]['adaptive_reasons'].append(reasoning)
            agent_scores[agent]['recommendation_sources'].add('adaptive')

        # Calculate combined scores
        for agent, scores in agent_scores.items():
            # Hybrid score combination
            combined_score = (
                scores['universal_score'] * universal_weight +
                scores['adaptive_score'] * adaptive_weight
            )

            # Bonus for agents recommended by both systems
            if len(scores['recommendation_sources']) > 1:
                combined_score *= 1.15

            # Domain specialization bonus
            if self._is_domain_specialist(agent, context):
                combined_score += self.config['domain_specialization_bonus']

            scores['combined_score'] = min(combined_score, 1.0)

        # Convert to final format
        recommendations = []
        for agent, scores in agent_scores.items():
            if scores['combined_score'] >= self.config['confidence_threshold']:
                # Combine reasoning from both sources
                all_reasons = scores['universal_reasons'] + scores['adaptive_reasons']
                combined_reasoning = "; ".join(all_reasons[:3])  # Top 3 reasons

                recommendations.append({
                    'agent': agent,
                    'confidence': scores['combined_score'],
                    'reasoning': combined_reasoning,
                    'universal_score': scores['universal_score'],
                    'adaptive_score': scores['adaptive_score'],
                    'sources': list(scores['recommendation_sources']),
                    'hybrid_enhanced': True
                })

        return recommendations

    def _format_universal_only(self, universal_recs: List[Tuple[str, float, str]],
                              context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Format universal-only recommendations."""
        recommendations = []

        for agent, confidence, reasoning in universal_recs:
            if confidence >= self.config['confidence_threshold']:
                # Add domain specialization bonus
                if self._is_domain_specialist(agent, context):
                    confidence += self.config['domain_specialization_bonus']

                recommendations.append({
                    'agent': agent,
                    'confidence': min(confidence, 1.0),
                    'reasoning': reasoning,
                    'universal_score': confidence,
                    'adaptive_score': 0,
                    'sources': ['universal'],
                    'hybrid_enhanced': False
                })

        return recommendations

    def _is_domain_specialist(self, agent: str, context: Dict[str, Any]) -> bool:
        """Check if agent is a specialist for the current domain."""
        domain = context.get('domain', '').lower()

        domain_specialists = {
            'fintech': ['security-engineer', 'compliance-auditor', 'backend-engineer'],
            'healthcare': ['security-engineer', 'compliance-auditor', 'data-engineer'],
            'gaming': ['graphics-3d-engineer', 'performance-engineer', 'math-specialist'],
            'ecommerce': ['security-engineer', 'performance-engineer', 'api-engineer'],
            'enterprise': ['software-architect', 'security-engineer', 'devops-architect']
        }

        return agent in domain_specialists.get(domain, [])

    def _finalize_recommendations(self, recommendations: List[Dict[str, Any]],
                                context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply final filtering and ranking to recommendations."""
        # Sort by confidence score
        recommendations.sort(key=lambda x: x['confidence'], reverse=True)

        # Apply context-specific adjustments
        adjusted_recs = self._apply_context_adjustments(recommendations, context)

        # Limit to max recommendations
        final_recs = adjusted_recs[:self.config['max_recommendations']]

        # Add hybrid intelligence metadata
        for rec in final_recs:
            rec.update({
                'hybrid_intelligence': True,
                'learning_enabled': self.learning_enabled,
                'universal_weight': self.config['universal_weight'],
                'adaptive_weight': self.config['adaptive_weight'],
                'recommendation_timestamp': datetime.now().isoformat()
            })

        return final_recs

    def _apply_context_adjustments(self, recommendations: List[Dict[str, Any]],
                                 context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply context-specific adjustments to recommendations."""
        adjusted = []

        project_phase = context.get('project_phase', 'development')
        complexity = context.get('complexity', 'medium')
        urgency = context.get('urgency', 'normal')

        for rec in recommendations:
            agent = rec['agent']
            confidence = rec['confidence']

            # Project phase adjustments
            if project_phase == 'initialization' and agent in ['project-owner', 'software-architect']:
                confidence *= 1.2
            elif project_phase == 'development' and agent in ['backend-engineer', 'frontend-engineer']:
                confidence *= 1.1
            elif project_phase == 'testing' and agent in ['qa-engineer', 'automation-engineer']:
                confidence *= 1.15
            elif project_phase == 'deployment' and agent in ['deployment-engineer', 'devops-architect']:
                confidence *= 1.2

            # Complexity adjustments
            if complexity == 'high' and agent in ['software-architect', 'performance-engineer']:
                confidence *= 1.1
            elif complexity == 'low' and agent in ['backend-engineer', 'frontend-engineer']:
                confidence *= 1.05

            # Urgency adjustments
            if urgency == 'high' and agent in ['backend-engineer', 'frontend-engineer', 'qa-engineer']:
                confidence *= 1.1

            rec['confidence'] = min(confidence, 1.0)
            adjusted.append(rec)

        return adjusted

    def record_feedback(self, recommended_agents: List[str], selected_agent: str,
                       context: Dict[str, Any] = None):
        """Record user feedback for both systems."""
        # Record for adaptive learning
        try:
            task_type = context.get('task_type', 'development') if context else 'development'
            project_phase = context.get('project_phase', 'development') if context else 'development'

            self.choice_tracker.record_choice(
                recommended_agents=recommended_agents,
                selected_agent=selected_agent,
                task_type=task_type,
                project_phase=project_phase
            )

            # Update learning model
            self.model_updater.update_model()

            # Re-evaluate learning readiness
            self.learning_enabled = self._check_learning_readiness()

        except Exception as e:
            print(f"Warning: Failed to record adaptive learning feedback: {e}")

    def record_task_outcome(self, agent_name: str, success: bool,
                           context: Dict[str, Any] = None):
        """Record task outcome for effectiveness tracking."""
        try:
            task_type = context.get('task_type', 'development') if context else 'development'
            completion_time = context.get('completion_time') if context else None
            quality_score = context.get('quality_score') if context else None

            self.effectiveness_monitor.record_agent_usage(
                agent_name=agent_name,
                task_type=task_type,
                success=success,
                completion_time=completion_time,
                quality_score=quality_score
            )

        except Exception as e:
            print(f"Warning: Failed to record task outcome: {e}")

    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive status of hybrid intelligence system."""
        try:
            learning_status = self.choice_tracker.get_choice_statistics()
            effectiveness_status = self.effectiveness_monitor.get_effectiveness_summary()

            return {
                "hybrid_intelligence_enabled": True,
                "learning_enabled": self.learning_enabled,
                "universal_patterns": {
                    "patterns_count": len(self.universal_system.patterns),
                    "best_practices_count": len(self.universal_system.best_practices),
                    "supported_domains": list(self.universal_system.domain_rules.keys())
                },
                "adaptive_learning": {
                    "total_interactions": learning_status.get('total_choices', 0),
                    "alignment_rate": learning_status.get('alignment_statistics', {}).get('overall_alignment_rate', 0),
                    "learning_quality": "strong" if learning_status.get('total_choices', 0) >= 10 else "developing"
                },
                "effectiveness_tracking": {
                    "tracked_agents": effectiveness_status.get('total_tracked_agents', 0),
                    "total_tasks": effectiveness_status.get('total_tasks_monitored', 0),
                    "overall_success_rate": effectiveness_status.get('overall_success_rate', 0)
                },
                "configuration": self.config,
                "last_updated": datetime.now().isoformat()
            }

        except Exception as e:
            return {
                "hybrid_intelligence_enabled": False,
                "error": str(e),
                "last_updated": datetime.now().isoformat()
            }

    def get_insights_and_suggestions(self) -> Dict[str, Any]:
        """Get insights and suggestions for improving recommendations."""
        insights = {
            "system_performance": {},
            "learning_insights": {},
            "universal_coverage": {},
            "suggestions": []
        }

        try:
            # System performance insights
            status = self.get_system_status()
            learning_quality = status.get('adaptive_learning', {}).get('learning_quality', 'developing')

            insights["system_performance"] = {
                "learning_quality": learning_quality,
                "recommendation_mode": "hybrid" if self.learning_enabled else "universal_only",
                "data_sufficiency": "sufficient" if self.learning_enabled else "collecting"
            }

            # Learning insights
            if self.learning_enabled:
                learning_stats = self.choice_tracker.get_choice_statistics()
                alignment_rate = learning_stats.get('alignment_statistics', {}).get('overall_alignment_rate', 0)

                insights["learning_insights"] = {
                    "alignment_trend": "improving" if alignment_rate > 0.7 else "developing",
                    "personalization_strength": alignment_rate,
                    "learning_acceleration": "active" if learning_stats.get('total_choices', 0) > 5 else "initial"
                }

            # Universal coverage insights
            export = self.universal_system.export_universal_knowledge()
            insights["universal_coverage"] = {
                "technology_coverage": len(export.get('technology_coverage', [])),
                "domain_coverage": len(export.get('supported_domains', [])),
                "patterns_available": export.get('patterns_count', 0)
            }

            # Generate suggestions
            if not self.learning_enabled:
                insights["suggestions"].append({
                    "type": "learning_activation",
                    "message": "Continue using the system to activate adaptive learning",
                    "priority": "medium"
                })

            if self.learning_enabled and alignment_rate < 0.6:
                insights["suggestions"].append({
                    "type": "learning_improvement",
                    "message": "System is still learning your preferences - continue providing feedback",
                    "priority": "low"
                })

            if self.learning_enabled and alignment_rate > 0.8:
                insights["suggestions"].append({
                    "type": "system_excellence",
                    "message": "Hybrid intelligence system is performing excellently",
                    "priority": "info"
                })

        except Exception as e:
            insights["error"] = str(e)

        return insights


if __name__ == "__main__":
    # Demo usage
    hybrid_system = HybridIntelligenceSystem()

    # Test context
    test_context = {
        'technologies': ['react', 'node.js', 'postgresql', 'docker', 'aws'],
        'domain': 'ecommerce',
        'complexity': 'medium',
        'project_phase': 'development',
        'task_type': 'development',
        'has_frontend': True,
        'has_backend': True,
        'has_database': True,
        'has_deployment': True
    }

    print("🧠 Hybrid Intelligence System Demo")
    print("=" * 40)

    # Get recommendations
    recommendations = hybrid_system.get_hybrid_recommendations(test_context)

    print(f"\nTop Recommendations:")
    for i, rec in enumerate(recommendations[:5], 1):
        sources = ', '.join(rec['sources'])
        print(f"{i}. {rec['agent']}: {rec['confidence']:.2f}")
        print(f"   Sources: {sources}")
        print(f"   Reasoning: {rec['reasoning'][:100]}...")

    # System status
    print(f"\nSystem Status:")
    status = hybrid_system.get_system_status()
    print(f"Learning Enabled: {status['learning_enabled']}")
    print(f"Universal Patterns: {status['universal_patterns']['patterns_count']}")
    print(f"Supported Domains: {len(status['universal_patterns']['supported_domains'])}")

    # Insights
    print(f"\nSystem Insights:")
    insights = hybrid_system.get_insights_and_suggestions()
    print(f"Recommendation Mode: {insights['system_performance']['recommendation_mode']}")
    print(f"Learning Quality: {insights['system_performance']['learning_quality']}")

    for suggestion in insights.get('suggestions', []):
        print(f"💡 {suggestion['type']}: {suggestion['message']}")