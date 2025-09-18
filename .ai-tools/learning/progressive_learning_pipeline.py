#!/usr/bin/env python3
"""
Progressive Learning Pipeline
Phase 3: Template-based start with rapid adaptation and evolution tracking
"""

import json
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict

try:
    from .industry_templates import IndustryTemplateSystem, ProjectTemplate, TemplateRecommendation
    from .hybrid_intelligence import HybridIntelligenceSystem
    from .project_adaptive_learning import ProjectAdaptiveLearning
    from .user_choice_tracker import UserChoiceTracker
    from .agent_effectiveness_monitor import AgentEffectivenessMonitor
except ImportError:
    from industry_templates import IndustryTemplateSystem, ProjectTemplate, TemplateRecommendation
    from hybrid_intelligence import HybridIntelligenceSystem
    from project_adaptive_learning import ProjectAdaptiveLearning
    from user_choice_tracker import UserChoiceTracker
    from agent_effectiveness_monitor import AgentEffectivenessMonitor


@dataclass
class LearningMilestone:
    """Represents a learning milestone in the progressive pipeline"""
    milestone_id: str
    name: str
    description: str
    criteria: Dict[str, Any]
    achieved_at: Optional[str] = None
    confidence: float = 0.0


@dataclass
class TemplateEvolution:
    """Tracks how project evolves from initial template"""
    evolution_id: str
    original_template_id: str
    current_state: Dict[str, Any]
    divergence_points: List[Dict[str, Any]]
    adaptation_history: List[Dict[str, Any]]
    learning_insights: Dict[str, Any]
    evolution_score: float = 0.0


class ProgressiveLearningPipeline:
    """
    Advanced learning pipeline that starts with industry templates and rapidly
    adapts to project-specific needs through progressive learning stages.
    """

    def __init__(self, project_root: str = None):
        """Initialize progressive learning pipeline."""
        self.project_root = project_root or self._find_project_root()

        # Initialize component systems
        self.template_system = IndustryTemplateSystem()
        self.hybrid_intelligence = HybridIntelligenceSystem(self.project_root)
        self.adaptive_learning = ProjectAdaptiveLearning(self.project_root)
        self.choice_tracker = UserChoiceTracker(self.project_root)
        self.effectiveness_monitor = AgentEffectivenessMonitor(self.project_root)

        # Progressive learning configuration
        self.config = self._load_pipeline_config()

        # Learning state management
        self.learning_pipeline_dir = Path(self.project_root) / ".ai-tools" / "learning" / "pipeline"
        self.learning_pipeline_dir.mkdir(parents=True, exist_ok=True)

        self.current_template = None
        self.learning_milestones = self._initialize_learning_milestones()
        self.template_evolution = self._load_or_create_evolution()

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def _load_pipeline_config(self) -> Dict[str, Any]:
        """Load progressive learning pipeline configuration."""
        return {
            "rapid_adaptation_threshold": 3,  # Interactions needed for rapid adaptation
            "template_divergence_threshold": 0.3,  # When to flag significant divergence
            "learning_acceleration_factor": 1.5,  # Boost learning from template context
            "evolution_tracking_window": 30,  # Days to track evolution patterns
            "milestone_confidence_threshold": 0.8,  # Confidence needed for milestone achievement
            "adaptation_boost_factor": 1.3,  # Boost for template-aligned choices
            "divergence_penalty_factor": 0.9,  # Penalty for anti-template choices
            "template_validation_period": 7,  # Days to validate template effectiveness
        }

    def _initialize_learning_milestones(self) -> List[LearningMilestone]:
        """Initialize learning milestones for progressive pipeline."""
        return [
            LearningMilestone(
                milestone_id="template_selection",
                name="Template Selection",
                description="Successfully selected and initialized with industry template",
                criteria={"template_selected": True, "initial_setup": True}
            ),
            LearningMilestone(
                milestone_id="rapid_adaptation",
                name="Rapid Adaptation",
                description="Quick learning from first user interactions",
                criteria={"user_interactions": 3, "alignment_rate": 0.7}
            ),
            LearningMilestone(
                milestone_id="template_validation",
                name="Template Validation",
                description="Template proven effective for project context",
                criteria={"validation_period_days": 7, "template_alignment": 0.8}
            ),
            LearningMilestone(
                milestone_id="pattern_divergence",
                name="Pattern Divergence Detection",
                description="Identified areas where project diverges from template",
                criteria={"divergence_detected": True, "custom_patterns": 3}
            ),
            LearningMilestone(
                milestone_id="hybrid_optimization",
                name="Hybrid Optimization",
                description="Optimal balance between template and adaptive learning",
                criteria={"learning_quality": "excellent", "template_integration": 0.9}
            ),
            LearningMilestone(
                milestone_id="custom_excellence",
                name="Custom Excellence",
                description="Developed project-specific patterns beyond template",
                criteria={"custom_patterns": 10, "effectiveness_improvement": 0.2}
            )
        ]

    def _load_or_create_evolution(self) -> TemplateEvolution:
        """Load existing evolution or create new one."""
        evolution_file = self.learning_pipeline_dir / "template_evolution.json"

        if evolution_file.exists():
            try:
                with open(evolution_file, 'r') as f:
                    data = json.load(f)
                    return TemplateEvolution(**data)
            except Exception as e:
                print(f"Warning: Error loading evolution data: {e}")

        # Create new evolution tracking
        return TemplateEvolution(
            evolution_id=f"evolution_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            original_template_id="",
            current_state={},
            divergence_points=[],
            adaptation_history=[],
            learning_insights={}
        )

    def bootstrap_with_template(self, project_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Bootstrap project with industry template for immediate value.

        Args:
            project_context: Project context for template selection

        Returns:
            Bootstrap result with template, recommendations, and setup info
        """
        print("🚀 Starting Smart Bootstrap with Industry Template...")

        # Get template recommendations
        template_recommendations = self.template_system.recommend_templates(project_context)

        if not template_recommendations:
            return {
                "status": "no_template_found",
                "message": "No suitable template found, falling back to hybrid intelligence",
                "fallback_recommendations": self.hybrid_intelligence.get_hybrid_recommendations(project_context)
            }

        # Select best template
        best_template_rec = template_recommendations[0]
        self.current_template = best_template_rec.template

        # Initialize evolution tracking
        self.template_evolution.original_template_id = self.current_template.template_id
        self.template_evolution.current_state = {
            "template_id": self.current_template.template_id,
            "selected_at": datetime.now().isoformat(),
            "project_context": project_context,
            "initial_agents": self.current_template.required_agents + self.current_template.recommended_agents
        }

        # Generate template-based recommendations with hybrid enhancement
        template_recommendations = self._generate_template_recommendations(project_context)

        # Mark template selection milestone
        self._achieve_milestone("template_selection")

        # Save evolution state
        self._save_evolution_state()

        bootstrap_result = {
            "status": "template_selected",
            "template": {
                "id": self.current_template.template_id,
                "name": self.current_template.name,
                "industry": self.current_template.industry,
                "confidence": best_template_rec.confidence,
                "match_score": best_template_rec.match_score
            },
            "recommendations": template_recommendations,
            "reasoning": best_template_rec.reasoning,
            "customization_suggestions": best_template_rec.customization_suggestions,
            "learning_milestones": [
                {"name": m.name, "achieved": m.achieved_at is not None}
                for m in self.learning_milestones
            ],
            "next_steps": self._generate_next_steps()
        }

        print(f"✅ Bootstrap complete with {self.current_template.name} template")
        return bootstrap_result

    def _generate_template_recommendations(self, project_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate agent recommendations based on selected template with hybrid enhancement."""
        if not self.current_template:
            return []

        # Start with template recommendations
        template_agents = []

        # Required agents (high confidence)
        for agent in self.current_template.required_agents:
            template_agents.append({
                "agent": agent,
                "confidence": 0.95,
                "reasoning": f"Required for {self.current_template.industry} industry template",
                "source": "template_required",
                "priority": "high"
            })

        # Recommended agents (medium confidence)
        for agent in self.current_template.recommended_agents:
            template_agents.append({
                "agent": agent,
                "confidence": 0.8,
                "reasoning": f"Recommended for {self.current_template.industry} template",
                "source": "template_recommended",
                "priority": "medium"
            })

        # Optional agents (lower confidence, contextual)
        context_score = self._calculate_context_relevance(project_context)
        for agent in self.current_template.optional_agents:
            if context_score > 0.7:  # Only include if high context relevance
                template_agents.append({
                    "agent": agent,
                    "confidence": 0.6 * context_score,
                    "reasoning": f"Optional for {self.current_template.industry} template, relevant to context",
                    "source": "template_optional",
                    "priority": "low"
                })

        # Enhance with hybrid intelligence if available
        try:
            hybrid_recs = self.hybrid_intelligence.get_hybrid_recommendations(project_context)

            # Integrate hybrid recommendations with template boost
            enhanced_agents = []
            template_agent_names = set(agent["agent"] for agent in template_agents)

            for template_agent in template_agents:
                agent_name = template_agent["agent"]

                # Find matching hybrid recommendation
                hybrid_match = next((r for r in hybrid_recs if r["agent"] == agent_name), None)

                if hybrid_match:
                    # Boost confidence for template-hybrid consensus
                    boosted_confidence = min(
                        (template_agent["confidence"] + hybrid_match["confidence"]) / 2 * 1.2,
                        1.0
                    )
                    enhanced_agents.append({
                        **template_agent,
                        "confidence": boosted_confidence,
                        "reasoning": f"{template_agent['reasoning']}; {hybrid_match['reasoning']}",
                        "source": "template_hybrid",
                        "hybrid_enhanced": True
                    })
                else:
                    enhanced_agents.append(template_agent)

            # Add high-confidence hybrid recommendations not in template
            for hybrid_rec in hybrid_recs[:3]:  # Top 3 hybrid recommendations
                if hybrid_rec["agent"] not in template_agent_names and hybrid_rec["confidence"] > 0.8:
                    enhanced_agents.append({
                        "agent": hybrid_rec["agent"],
                        "confidence": hybrid_rec["confidence"] * 0.9,  # Slight reduction as not in template
                        "reasoning": f"High-confidence hybrid recommendation: {hybrid_rec['reasoning']}",
                        "source": "hybrid_addition",
                        "priority": "medium",
                        "hybrid_enhanced": True
                    })

            template_agents = enhanced_agents

        except Exception as e:
            print(f"Warning: Hybrid enhancement failed: {e}")

        # Sort by confidence and priority
        priority_order = {"high": 3, "medium": 2, "low": 1}
        template_agents.sort(key=lambda x: (priority_order.get(x.get("priority", "medium"), 2), x["confidence"]), reverse=True)

        return template_agents[:10]  # Return top 10 recommendations

    def _calculate_context_relevance(self, context: Dict[str, Any]) -> float:
        """Calculate how relevant the context is for optional agents."""
        relevance_score = 0.5  # Base score

        # Technology alignment
        context_tech = set(context.get('technologies', []))
        template_tech = set(
            self.current_template.primary_technologies +
            self.current_template.secondary_technologies
        )

        if context_tech & template_tech:  # Intersection
            tech_overlap = len(context_tech & template_tech) / len(context_tech | template_tech)
            relevance_score += 0.3 * tech_overlap

        # Complexity alignment
        if context.get('complexity') == self.current_template.typical_complexity:
            relevance_score += 0.2

        return min(relevance_score, 1.0)

    def record_learning_interaction(self, recommended_agents: List[str], selected_agent: str,
                                  context: Dict[str, Any] = None):
        """
        Record learning interaction with template-aware enhancement.

        Args:
            recommended_agents: Agents that were recommended
            selected_agent: Agent actually selected by user
            context: Additional context about the interaction
        """
        # Record in hybrid intelligence system
        self.hybrid_intelligence.record_feedback(
            recommended_agents=recommended_agents,
            selected_agent=selected_agent,
            context=context or {}
        )

        # Template-specific learning analysis
        if self.current_template:
            self._analyze_template_alignment(recommended_agents, selected_agent, context)

        # Check for milestone achievements
        self._check_milestone_achievements()

        # Update evolution tracking
        self._update_evolution_tracking(recommended_agents, selected_agent, context)

        print(f"📚 Progressive learning interaction recorded: {selected_agent}")

    def _analyze_template_alignment(self, recommended_agents: List[str], selected_agent: str,
                                  context: Dict[str, Any]):
        """Analyze alignment between user choice and template expectations."""
        template_agents = set(
            self.current_template.required_agents +
            self.current_template.recommended_agents +
            self.current_template.optional_agents
        )

        alignment_analysis = {
            "timestamp": datetime.now().isoformat(),
            "selected_agent": selected_agent,
            "template_alignment": selected_agent in template_agents,
            "agent_category": self._categorize_template_agent(selected_agent),
            "context": context or {}
        }

        # Check for divergence patterns
        if not alignment_analysis["template_alignment"]:
            divergence_point = {
                "timestamp": datetime.now().isoformat(),
                "selected_agent": selected_agent,
                "recommended_agents": recommended_agents,
                "context": context or {},
                "divergence_type": "agent_selection",
                "significance": self._calculate_divergence_significance(selected_agent, context)
            }

            self.template_evolution.divergence_points.append(divergence_point)

            # Check if this indicates a significant pattern shift
            if len(self.template_evolution.divergence_points) >= 3:
                recent_divergences = self.template_evolution.divergence_points[-3:]
                if self._detect_divergence_pattern(recent_divergences):
                    self._achieve_milestone("pattern_divergence")

        # Add to adaptation history
        self.template_evolution.adaptation_history.append(alignment_analysis)

        # Keep history manageable
        if len(self.template_evolution.adaptation_history) > 50:
            self.template_evolution.adaptation_history = self.template_evolution.adaptation_history[-50:]

    def _categorize_template_agent(self, agent: str) -> str:
        """Categorize agent relative to current template."""
        if not self.current_template:
            return "unknown"

        if agent in self.current_template.required_agents:
            return "required"
        elif agent in self.current_template.recommended_agents:
            return "recommended"
        elif agent in self.current_template.optional_agents:
            return "optional"
        else:
            return "external"

    def _calculate_divergence_significance(self, selected_agent: str, context: Dict[str, Any]) -> float:
        """Calculate significance of divergence from template."""
        significance = 0.5

        # Higher significance if consistently choosing external agents
        external_choices = sum(
            1 for choice in self.template_evolution.adaptation_history[-10:]
            if choice.get("agent_category") == "external"
        )

        if external_choices >= 3:
            significance += 0.3

        # Context-based significance
        if context and context.get('task_type') in self.current_template.learning_focus_areas:
            significance += 0.2

        return min(significance, 1.0)

    def _detect_divergence_pattern(self, divergences: List[Dict[str, Any]]) -> bool:
        """Detect if there's a significant pattern in divergences."""
        if len(divergences) < 3:
            return False

        # Check for consistent divergence in specific contexts
        contexts = [d.get("context", {}).get("task_type") for d in divergences]
        if len(set(contexts)) == 1 and contexts[0]:  # Same context type
            return True

        # Check for consistent agent category divergences
        selected_agents = [d["selected_agent"] for d in divergences]
        if len(set(selected_agents)) <= 2:  # Consistently selecting same few agents
            return True

        return False

    def _check_milestone_achievements(self):
        """Check and achieve learning milestones."""
        for milestone in self.learning_milestones:
            if milestone.achieved_at:
                continue  # Already achieved

            if self._evaluate_milestone_criteria(milestone):
                self._achieve_milestone(milestone.milestone_id)

    def _evaluate_milestone_criteria(self, milestone: LearningMilestone) -> bool:
        """Evaluate if milestone criteria are met."""
        criteria = milestone.criteria

        if milestone.milestone_id == "rapid_adaptation":
            choice_stats = self.choice_tracker.get_choice_statistics()
            total_choices = choice_stats.get('total_choices', 0)
            alignment_rate = choice_stats.get('alignment_statistics', {}).get('overall_alignment_rate', 0)

            return (total_choices >= criteria.get('user_interactions', 3) and
                    alignment_rate >= criteria.get('alignment_rate', 0.7))

        elif milestone.milestone_id == "template_validation":
            if not self.current_template:
                return False

            # Check if template has been used for validation period
            template_start = self.template_evolution.current_state.get('selected_at')
            if template_start:
                start_time = datetime.fromisoformat(template_start)
                days_since_start = (datetime.now() - start_time).days

                if days_since_start >= criteria.get('validation_period_days', 7):
                    # Check template alignment rate
                    template_aligned_choices = sum(
                        1 for choice in self.template_evolution.adaptation_history
                        if choice.get('template_alignment', False)
                    )
                    total_choices = len(self.template_evolution.adaptation_history)

                    if total_choices > 0:
                        alignment_rate = template_aligned_choices / total_choices
                        return alignment_rate >= criteria.get('template_alignment', 0.8)

        elif milestone.milestone_id == "pattern_divergence":
            return len(self.template_evolution.divergence_points) >= criteria.get('custom_patterns', 3)

        elif milestone.milestone_id == "hybrid_optimization":
            # Check hybrid intelligence performance
            hybrid_status = self.hybrid_intelligence.get_system_status()
            learning_quality = hybrid_status.get('adaptive_learning', {}).get('learning_quality', 'developing')

            return learning_quality == 'excellent'  # or other quality threshold

        elif milestone.milestone_id == "custom_excellence":
            # Check for development of custom patterns beyond template
            custom_patterns = sum(
                1 for choice in self.template_evolution.adaptation_history
                if choice.get('agent_category') == 'external'
            )

            return custom_patterns >= criteria.get('custom_patterns', 10)

        return False

    def _achieve_milestone(self, milestone_id: str):
        """Mark milestone as achieved."""
        for milestone in self.learning_milestones:
            if milestone.milestone_id == milestone_id:
                milestone.achieved_at = datetime.now().isoformat()
                milestone.confidence = 1.0

                print(f"🎯 Learning milestone achieved: {milestone.name}")

                # Save milestone achievement
                self._save_pipeline_state()
                break

    def _update_evolution_tracking(self, recommended_agents: List[str], selected_agent: str,
                                 context: Dict[str, Any]):
        """Update template evolution tracking."""
        current_time = datetime.now()

        # Calculate evolution metrics
        self.template_evolution.evolution_score = self._calculate_evolution_score()

        # Generate learning insights
        self.template_evolution.learning_insights = self._generate_evolution_insights()

        # Save evolution state
        self._save_evolution_state()

    def _calculate_evolution_score(self) -> float:
        """Calculate how much the project has evolved from the original template."""
        if not self.template_evolution.adaptation_history:
            return 0.0

        total_interactions = len(self.template_evolution.adaptation_history)
        template_aligned = sum(
            1 for choice in self.template_evolution.adaptation_history
            if choice.get('template_alignment', False)
        )

        # Evolution score: higher when more divergence, but balanced with learning quality
        divergence_rate = 1 - (template_aligned / total_interactions) if total_interactions > 0 else 0
        learning_quality = self._get_current_learning_quality()

        evolution_score = (divergence_rate * 0.6 + learning_quality * 0.4)

        return min(evolution_score, 1.0)

    def _generate_evolution_insights(self) -> Dict[str, Any]:
        """Generate insights about template evolution."""
        insights = {
            "generated_at": datetime.now().isoformat(),
            "template_effectiveness": self._assess_template_effectiveness(),
            "divergence_patterns": self._analyze_divergence_patterns(),
            "learning_acceleration": self._measure_learning_acceleration(),
            "custom_pattern_development": self._identify_custom_patterns()
        }

        return insights

    def _assess_template_effectiveness(self) -> Dict[str, Any]:
        """Assess how effective the selected template has been."""
        if not self.template_evolution.adaptation_history:
            return {"status": "insufficient_data"}

        total_choices = len(self.template_evolution.adaptation_history)
        aligned_choices = sum(
            1 for choice in self.template_evolution.adaptation_history
            if choice.get('template_alignment', False)
        )

        alignment_rate = aligned_choices / total_choices if total_choices > 0 else 0

        effectiveness = {
            "alignment_rate": alignment_rate,
            "total_interactions": total_choices,
            "template_confidence": self.current_template.confidence if self.current_template else 0,
            "assessment": self._categorize_effectiveness(alignment_rate)
        }

        return effectiveness

    def _categorize_effectiveness(self, alignment_rate: float) -> str:
        """Categorize template effectiveness based on alignment rate."""
        if alignment_rate >= 0.8:
            return "excellent"
        elif alignment_rate >= 0.6:
            return "good"
        elif alignment_rate >= 0.4:
            return "moderate"
        else:
            return "poor"

    def _analyze_divergence_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in template divergences."""
        if not self.template_evolution.divergence_points:
            return {"status": "no_divergences"}

        # Group by divergence type and context
        divergence_analysis = {
            "total_divergences": len(self.template_evolution.divergence_points),
            "divergence_types": {},
            "context_patterns": {},
            "temporal_patterns": self._analyze_temporal_divergences()
        }

        for divergence in self.template_evolution.divergence_points:
            div_type = divergence.get("divergence_type", "unknown")
            context_type = divergence.get("context", {}).get("task_type", "unknown")

            divergence_analysis["divergence_types"][div_type] = divergence_analysis["divergence_types"].get(div_type, 0) + 1
            divergence_analysis["context_patterns"][context_type] = divergence_analysis["context_patterns"].get(context_type, 0) + 1

        return divergence_analysis

    def _analyze_temporal_divergences(self) -> Dict[str, Any]:
        """Analyze temporal patterns in divergences."""
        if len(self.template_evolution.divergence_points) < 2:
            return {"status": "insufficient_data"}

        # Sort by timestamp
        sorted_divergences = sorted(
            self.template_evolution.divergence_points,
            key=lambda x: x.get("timestamp", "")
        )

        # Analyze frequency over time
        now = datetime.now()
        recent_divergences = [
            d for d in sorted_divergences
            if (now - datetime.fromisoformat(d.get("timestamp", now.isoformat()))).days <= 7
        ]

        return {
            "recent_divergences": len(recent_divergences),
            "total_divergences": len(sorted_divergences),
            "divergence_acceleration": len(recent_divergences) / min(len(sorted_divergences), 7),
            "trend": "increasing" if len(recent_divergences) > len(sorted_divergences) / 2 else "stable"
        }

    def _measure_learning_acceleration(self) -> Dict[str, Any]:
        """Measure how quickly learning is progressing."""
        choice_stats = self.choice_tracker.get_choice_statistics()

        total_choices = choice_stats.get('total_choices', 0)
        alignment_rate = choice_stats.get('alignment_statistics', {}).get('overall_alignment_rate', 0)

        # Measure improvement trend
        if total_choices >= 6:
            recent_choices = self.template_evolution.adaptation_history[-3:]
            early_choices = self.template_evolution.adaptation_history[:3]

            recent_alignment = sum(1 for c in recent_choices if c.get('template_alignment', False)) / 3
            early_alignment = sum(1 for c in early_choices if c.get('template_alignment', False)) / 3

            improvement = recent_alignment - early_alignment
        else:
            improvement = 0

        return {
            "total_interactions": total_choices,
            "current_alignment_rate": alignment_rate,
            "learning_improvement": improvement,
            "acceleration_status": "fast" if improvement > 0.2 else ("moderate" if improvement > 0 else "slow")
        }

    def _identify_custom_patterns(self) -> Dict[str, Any]:
        """Identify custom patterns that have emerged beyond template."""
        custom_patterns = {
            "external_agents": {},
            "context_specializations": {},
            "unique_combinations": []
        }

        # Analyze external agent usage
        for choice in self.template_evolution.adaptation_history:
            if choice.get("agent_category") == "external":
                agent = choice.get("selected_agent")
                context_type = choice.get("context", {}).get("task_type", "general")

                if agent not in custom_patterns["external_agents"]:
                    custom_patterns["external_agents"][agent] = {"count": 0, "contexts": []}

                custom_patterns["external_agents"][agent]["count"] += 1
                if context_type not in custom_patterns["external_agents"][agent]["contexts"]:
                    custom_patterns["external_agents"][agent]["contexts"].append(context_type)

        # Analyze context specializations
        context_agents = {}
        for choice in self.template_evolution.adaptation_history:
            context_type = choice.get("context", {}).get("task_type", "general")
            agent = choice.get("selected_agent")

            if context_type not in context_agents:
                context_agents[context_type] = {}

            context_agents[context_type][agent] = context_agents[context_type].get(agent, 0) + 1

        custom_patterns["context_specializations"] = context_agents

        return custom_patterns

    def _get_current_learning_quality(self) -> float:
        """Get current learning system quality score."""
        try:
            status = self.hybrid_intelligence.get_system_status()
            learning_stats = status.get('adaptive_learning', {})

            alignment_rate = learning_stats.get('alignment_rate', 0)
            total_interactions = learning_stats.get('total_interactions', 0)

            # Quality based on alignment and data sufficiency
            quality_score = alignment_rate * min(total_interactions / 10, 1.0)

            return quality_score
        except:
            return 0.5

    def _generate_next_steps(self) -> List[str]:
        """Generate next steps for progressive learning."""
        steps = []

        # Check milestone status and suggest actions
        achieved_milestones = sum(1 for m in self.learning_milestones if m.achieved_at)

        if achieved_milestones == 0:
            steps.append("Start using the system to begin rapid adaptation phase")
            steps.append("Provide feedback on agent recommendations to accelerate learning")

        elif achieved_milestones < 3:
            steps.append("Continue using the system to validate template effectiveness")
            steps.append("Try different types of tasks to explore template coverage")

        else:
            steps.append("System is learning well - continue to develop custom patterns")
            steps.append("Consider exploring advanced features and specialized agents")

        return steps

    def _save_pipeline_state(self):
        """Save pipeline state including milestones."""
        state_file = self.learning_pipeline_dir / "pipeline_state.json"

        state = {
            "milestones": [asdict(m) for m in self.learning_milestones],
            "current_template_id": self.current_template.template_id if self.current_template else None,
            "config": self.config,
            "last_updated": datetime.now().isoformat()
        }

        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def _save_evolution_state(self):
        """Save template evolution state."""
        evolution_file = self.learning_pipeline_dir / "template_evolution.json"

        with open(evolution_file, 'w') as f:
            json.dump(asdict(self.template_evolution), f, indent=2)

    def get_pipeline_status(self) -> Dict[str, Any]:
        """Get comprehensive pipeline status."""
        return {
            "pipeline_active": self.current_template is not None,
            "current_template": {
                "id": self.current_template.template_id,
                "name": self.current_template.name,
                "industry": self.current_template.industry
            } if self.current_template else None,
            "learning_milestones": [
                {
                    "id": m.milestone_id,
                    "name": m.name,
                    "description": m.description,
                    "achieved": m.achieved_at is not None,
                    "achieved_at": m.achieved_at,
                    "confidence": m.confidence
                }
                for m in self.learning_milestones
            ],
            "evolution_metrics": {
                "evolution_score": self.template_evolution.evolution_score,
                "total_adaptations": len(self.template_evolution.adaptation_history),
                "divergence_points": len(self.template_evolution.divergence_points),
                "learning_insights": self.template_evolution.learning_insights
            },
            "next_steps": self._generate_next_steps(),
            "status_timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Demo usage
    pipeline = ProgressiveLearningPipeline()

    # Test bootstrap
    test_context = {
        'domain': 'ecommerce',
        'technologies': ['react', 'node.js', 'postgresql'],
        'complexity': 'medium',
        'team_size': 'small'
    }

    print("🚀 Progressive Learning Pipeline Demo")
    print("=" * 45)

    # Bootstrap with template
    result = pipeline.bootstrap_with_template(test_context)

    print(f"Bootstrap Status: {result['status']}")
    if result['status'] == 'template_selected':
        print(f"Template: {result['template']['name']}")
        print(f"Confidence: {result['template']['confidence']:.2f}")
        print(f"Recommendations: {len(result['recommendations'])}")

    # Get status
    status = pipeline.get_pipeline_status()
    print(f"\nPipeline Status:")
    print(f"Active: {status['pipeline_active']}")
    print(f"Milestones Achieved: {sum(1 for m in status['learning_milestones'] if m['achieved'])}/{len(status['learning_milestones'])}")
    print(f"Evolution Score: {status['evolution_metrics']['evolution_score']:.2f}")