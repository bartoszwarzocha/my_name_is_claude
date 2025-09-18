#!/usr/bin/env python3
"""
Smart Bootstrap System
Phase 3: Complete smart bootstrap system with industry templates,
rapid adaptation, and progressive learning pipeline
"""

import json
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict

try:
    from .industry_templates import IndustryTemplateSystem, ProjectTemplate, TemplateRecommendation
    from .progressive_learning_pipeline import ProgressiveLearningPipeline, LearningMilestone, TemplateEvolution
    from .hybrid_intelligence import HybridIntelligenceSystem
    from .universal_patterns import UniversalPatternsSystem
    from .project_adaptive_learning import ProjectAdaptiveLearning
except ImportError:
    from industry_templates import IndustryTemplateSystem, ProjectTemplate, TemplateRecommendation
    from progressive_learning_pipeline import ProgressiveLearningPipeline, LearningMilestone, TemplateEvolution
    from hybrid_intelligence import HybridIntelligenceSystem
    from universal_patterns import UniversalPatternsSystem
    from project_adaptive_learning import ProjectAdaptiveLearning


@dataclass
class BootstrapResult:
    """Complete bootstrap result with all system information"""
    status: str
    mode: str  # template, hybrid, fallback
    template_info: Optional[Dict[str, Any]]
    recommendations: List[Dict[str, Any]]
    learning_pipeline: Dict[str, Any]
    system_capabilities: Dict[str, Any]
    next_steps: List[str]
    bootstrap_metadata: Dict[str, Any]


class SmartBootstrapSystem:
    """
    Complete Smart Bootstrap System that provides intelligent project startup
    with industry templates, immediate value, and rapid adaptation capabilities.
    """

    def __init__(self, project_root: str = None):
        """Initialize smart bootstrap system."""
        self.project_root = project_root or self._find_project_root()

        # Initialize all subsystems
        try:
            self.template_system = IndustryTemplateSystem()
            self.progressive_pipeline = ProgressiveLearningPipeline(self.project_root)
            self.hybrid_intelligence = HybridIntelligenceSystem(self.project_root)
            self.universal_patterns = UniversalPatternsSystem()
            self.adaptive_learning = ProjectAdaptiveLearning(self.project_root)

            self.systems_available = {
                "templates": True,
                "progressive_learning": True,
                "hybrid_intelligence": True,
                "universal_patterns": True,
                "adaptive_learning": True
            }

        except Exception as e:
            print(f"Warning: Some systems unavailable: {e}")
            self.systems_available = {
                "templates": False,
                "progressive_learning": False,
                "hybrid_intelligence": False,
                "universal_patterns": False,
                "adaptive_learning": False
            }

        # Bootstrap configuration
        self.config = self._load_bootstrap_config()

        # Bootstrap state
        self.bootstrap_dir = Path(self.project_root) / ".ai-tools" / "learning" / "bootstrap"
        self.bootstrap_dir.mkdir(parents=True, exist_ok=True)

        self.current_bootstrap = self._load_or_create_bootstrap_state()

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def _load_bootstrap_config(self) -> Dict[str, Any]:
        """Load smart bootstrap configuration."""
        return {
            "template_confidence_threshold": 0.7,  # Minimum confidence for template selection
            "hybrid_fallback_enabled": True,       # Fall back to hybrid intelligence
            "universal_fallback_enabled": True,    # Fall back to universal patterns
            "rapid_adaptation_enabled": True,      # Enable rapid adaptation features
            "learning_acceleration_factor": 1.5,   # Accelerate learning with templates
            "template_customization_enabled": True, # Allow template customization
            "progressive_milestones_enabled": True, # Track learning milestones
            "bootstrap_analytics_enabled": True,   # Track bootstrap effectiveness
            "quick_start_mode": True,              # Optimize for quick project start
            "expert_guidance_enabled": True       # Provide expert guidance and tips
        }

    def _load_or_create_bootstrap_state(self) -> Dict[str, Any]:
        """Load existing bootstrap state or create new one."""
        state_file = self.bootstrap_dir / "bootstrap_state.json"

        if state_file.exists():
            try:
                with open(state_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Error loading bootstrap state: {e}")

        # Create new bootstrap state
        return {
            "bootstrap_id": f"bootstrap_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "bootstrap_history": [],
            "current_mode": None,
            "active_template": None,
            "learning_progress": {},
            "system_performance": {}
        }

    def bootstrap_project(self, project_context: Dict[str, Any],
                         preferences: Dict[str, Any] = None) -> BootstrapResult:
        """
        Perform complete smart bootstrap of the project.

        Args:
            project_context: Project context (domain, technologies, complexity, etc.)
            preferences: User preferences for bootstrap process

        Returns:
            Complete bootstrap result with recommendations and setup info
        """
        print("🚀 Starting Smart Bootstrap System...")

        bootstrap_start = datetime.now()
        preferences = preferences or {}

        # Determine best bootstrap mode
        bootstrap_mode = self._determine_bootstrap_mode(project_context, preferences)

        # Perform bootstrap based on selected mode
        if bootstrap_mode == "template" and self.systems_available["templates"]:
            result = self._bootstrap_with_template(project_context, preferences)
        elif bootstrap_mode == "hybrid" and self.systems_available["hybrid_intelligence"]:
            result = self._bootstrap_with_hybrid_intelligence(project_context, preferences)
        elif bootstrap_mode == "universal" and self.systems_available["universal_patterns"]:
            result = self._bootstrap_with_universal_patterns(project_context, preferences)
        else:
            result = self._bootstrap_with_fallback(project_context, preferences)

        # Enhance result with system capabilities and metadata
        result = self._enhance_bootstrap_result(result, project_context, preferences, bootstrap_start)

        # Save bootstrap state
        self._save_bootstrap_state(result)

        # Log bootstrap completion
        bootstrap_time = (datetime.now() - bootstrap_start).total_seconds()
        print(f"✅ Smart Bootstrap completed in {bootstrap_time:.2f}s - Mode: {result.mode}")

        return result

    def _determine_bootstrap_mode(self, project_context: Dict[str, Any],
                                preferences: Dict[str, Any]) -> str:
        """Determine the best bootstrap mode for the project."""
        # User preference override
        if preferences.get('bootstrap_mode'):
            return preferences['bootstrap_mode']

        # Template mode conditions
        if self.systems_available["templates"]:
            # Check if we have a good template match
            try:
                template_recs = self.template_system.recommend_templates(project_context)
                if template_recs and template_recs[0].confidence >= self.config['template_confidence_threshold']:
                    return "template"
            except Exception as e:
                print(f"Template evaluation failed: {e}")

        # Hybrid mode conditions
        if self.systems_available["hybrid_intelligence"]:
            try:
                hybrid_status = self.hybrid_intelligence.get_system_status()
                if hybrid_status.get('hybrid_intelligence_enabled', False):
                    return "hybrid"
            except Exception as e:
                print(f"Hybrid intelligence evaluation failed: {e}")

        # Universal patterns mode
        if self.systems_available["universal_patterns"]:
            return "universal"

        # Fallback mode
        return "fallback"

    def _bootstrap_with_template(self, project_context: Dict[str, Any],
                               preferences: Dict[str, Any]) -> BootstrapResult:
        """Bootstrap using industry template system."""
        print("🏭 Bootstrapping with Industry Template System...")

        # Get template bootstrap
        bootstrap_result = self.progressive_pipeline.bootstrap_with_template(project_context)

        if bootstrap_result['status'] != 'template_selected':
            # Fall back to hybrid intelligence
            return self._bootstrap_with_hybrid_intelligence(project_context, preferences)

        # Create comprehensive result
        result = BootstrapResult(
            status="success",
            mode="template",
            template_info=bootstrap_result['template'],
            recommendations=bootstrap_result['recommendations'],
            learning_pipeline={
                "active": True,
                "milestones": bootstrap_result['learning_milestones'],
                "next_steps": bootstrap_result['next_steps']
            },
            system_capabilities=self._get_system_capabilities(),
            next_steps=self._generate_template_next_steps(bootstrap_result),
            bootstrap_metadata={
                "template_match_score": bootstrap_result['template']['match_score'],
                "customization_suggestions": bootstrap_result.get('customization_suggestions', []),
                "reasoning": bootstrap_result.get('reasoning', [])
            }
        )

        return result

    def _bootstrap_with_hybrid_intelligence(self, project_context: Dict[str, Any],
                                          preferences: Dict[str, Any]) -> BootstrapResult:
        """Bootstrap using hybrid intelligence system."""
        print("🧠 Bootstrapping with Hybrid Intelligence System...")

        try:
            # Get hybrid recommendations
            hybrid_recommendations = self.hybrid_intelligence.get_hybrid_recommendations(project_context)

            # Convert to standard format
            recommendations = [
                {
                    "agent": rec["agent"],
                    "confidence": rec["confidence"],
                    "reasoning": rec["reasoning"],
                    "source": "hybrid_intelligence",
                    "priority": self._calculate_priority(rec["confidence"]),
                    "universal_score": rec.get("universal_score", 0),
                    "adaptive_score": rec.get("adaptive_score", 0),
                    "hybrid_enhanced": rec.get("hybrid_enhanced", True)
                }
                for rec in hybrid_recommendations
            ]

            # Get system status for learning pipeline info
            hybrid_status = self.hybrid_intelligence.get_system_status()

            result = BootstrapResult(
                status="success",
                mode="hybrid",
                template_info=None,
                recommendations=recommendations,
                learning_pipeline={
                    "active": True,
                    "learning_enabled": hybrid_status.get('learning_enabled', False),
                    "universal_patterns": hybrid_status.get('universal_patterns', {}),
                    "adaptive_learning": hybrid_status.get('adaptive_learning', {})
                },
                system_capabilities=self._get_system_capabilities(),
                next_steps=self._generate_hybrid_next_steps(hybrid_status),
                bootstrap_metadata={
                    "recommendation_count": len(recommendations),
                    "learning_mode": "hybrid",
                    "system_status": "operational"
                }
            )

            return result

        except Exception as e:
            print(f"Hybrid intelligence bootstrap failed: {e}")
            return self._bootstrap_with_universal_patterns(project_context, preferences)

    def _bootstrap_with_universal_patterns(self, project_context: Dict[str, Any],
                                         preferences: Dict[str, Any]) -> BootstrapResult:
        """Bootstrap using universal patterns system."""
        print("🔵 Bootstrapping with Universal Patterns System...")

        try:
            # Get universal recommendations
            universal_recommendations = self.universal_patterns.get_universal_recommendations(project_context)

            # Convert to standard format
            recommendations = [
                {
                    "agent": agent,
                    "confidence": confidence,
                    "reasoning": reasoning,
                    "source": "universal_patterns",
                    "priority": self._calculate_priority(confidence),
                    "universal_score": confidence,
                    "adaptive_score": 0,
                    "hybrid_enhanced": False
                }
                for agent, confidence, reasoning in universal_recommendations
            ]

            result = BootstrapResult(
                status="success",
                mode="universal",
                template_info=None,
                recommendations=recommendations,
                learning_pipeline={
                    "active": False,
                    "mode": "universal_only",
                    "adaptive_learning_available": self.systems_available["adaptive_learning"]
                },
                system_capabilities=self._get_system_capabilities(),
                next_steps=self._generate_universal_next_steps(),
                bootstrap_metadata={
                    "recommendation_count": len(recommendations),
                    "pattern_matching": "universal",
                    "learning_mode": "pattern_based"
                }
            )

            return result

        except Exception as e:
            print(f"Universal patterns bootstrap failed: {e}")
            return self._bootstrap_with_fallback(project_context, preferences)

    def _bootstrap_with_fallback(self, project_context: Dict[str, Any],
                                preferences: Dict[str, Any]) -> BootstrapResult:
        """Bootstrap using fallback recommendations."""
        print("🔄 Bootstrapping with Fallback System...")

        # Basic fallback recommendations based on project context
        fallback_recommendations = self._generate_fallback_recommendations(project_context)

        result = BootstrapResult(
            status="fallback",
            mode="fallback",
            template_info=None,
            recommendations=fallback_recommendations,
            learning_pipeline={
                "active": False,
                "mode": "fallback",
                "message": "Basic recommendations - upgrade systems for enhanced capabilities"
            },
            system_capabilities=self._get_system_capabilities(),
            next_steps=self._generate_fallback_next_steps(),
            bootstrap_metadata={
                "recommendation_count": len(fallback_recommendations),
                "fallback_reason": "No advanced systems available",
                "upgrade_suggestions": ["Install ML dependencies", "Enable hybrid intelligence"]
            }
        )

        return result

    def _generate_fallback_recommendations(self, project_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate basic fallback recommendations."""
        recommendations = []

        # Basic recommendations based on simple heuristics
        has_frontend = project_context.get('has_frontend', False) or \
                      any(tech in ['react', 'angular', 'vue', 'html', 'css']
                          for tech in project_context.get('technologies', []))

        has_backend = project_context.get('has_backend', False) or \
                     any(tech in ['node.js', 'python', 'java', 'go', 'rust']
                         for tech in project_context.get('technologies', []))

        domain = project_context.get('domain', 'general')

        if has_frontend:
            recommendations.append({
                "agent": "frontend-engineer",
                "confidence": 0.8,
                "reasoning": "Frontend development detected",
                "source": "fallback_heuristic",
                "priority": "high"
            })

        if has_backend:
            recommendations.append({
                "agent": "backend-engineer",
                "confidence": 0.8,
                "reasoning": "Backend development detected",
                "source": "fallback_heuristic",
                "priority": "high"
            })

        if domain in ['fintech', 'healthcare', 'enterprise']:
            recommendations.append({
                "agent": "security-engineer",
                "confidence": 0.9,
                "reasoning": f"Security critical for {domain} domain",
                "source": "fallback_heuristic",
                "priority": "high"
            })

        # Always recommend QA for quality
        recommendations.append({
            "agent": "qa-engineer",
            "confidence": 0.7,
            "reasoning": "Quality assurance recommended for all projects",
            "source": "fallback_heuristic",
            "priority": "medium"
        })

        return recommendations

    def _calculate_priority(self, confidence: float) -> str:
        """Calculate priority based on confidence score."""
        if confidence >= 0.8:
            return "high"
        elif confidence >= 0.6:
            return "medium"
        else:
            return "low"

    def _enhance_bootstrap_result(self, result: BootstrapResult, project_context: Dict[str, Any],
                                preferences: Dict[str, Any], bootstrap_start: datetime) -> BootstrapResult:
        """Enhance bootstrap result with additional information."""

        # Add system capabilities
        result.system_capabilities = self._get_system_capabilities()

        # Add expert guidance if enabled
        if self.config["expert_guidance_enabled"]:
            result.next_steps.extend(self._generate_expert_guidance(result, project_context))

        # Add performance metrics
        bootstrap_time = (datetime.now() - bootstrap_start).total_seconds()
        result.bootstrap_metadata.update({
            "bootstrap_time_seconds": bootstrap_time,
            "systems_available": self.systems_available,
            "config_used": self.config,
            "timestamp": datetime.now().isoformat()
        })

        return result

    def _get_system_capabilities(self) -> Dict[str, Any]:
        """Get comprehensive system capabilities."""
        capabilities = {
            "smart_bootstrap": True,
            "industry_templates": self.systems_available["templates"],
            "progressive_learning": self.systems_available["progressive_learning"],
            "hybrid_intelligence": self.systems_available["hybrid_intelligence"],
            "universal_patterns": self.systems_available["universal_patterns"],
            "adaptive_learning": self.systems_available["adaptive_learning"]
        }

        # Add detailed capabilities for available systems
        if self.systems_available["templates"]:
            template_export = self.template_system.export_template_knowledge()
            capabilities["template_details"] = {
                "total_templates": template_export["total_templates"],
                "industries_covered": template_export["industries_covered"],
                "technologies_covered": template_export["technologies_covered"]
            }

        if self.systems_available["hybrid_intelligence"]:
            try:
                hybrid_status = self.hybrid_intelligence.get_system_status()
                capabilities["hybrid_details"] = {
                    "learning_enabled": hybrid_status.get("learning_enabled", False),
                    "universal_patterns": hybrid_status.get("universal_patterns", {}),
                    "recommendation_mode": "hybrid"
                }
            except Exception as e:
                capabilities["hybrid_details"] = {"error": str(e)}

        return capabilities

    def _generate_template_next_steps(self, bootstrap_result: Dict[str, Any]) -> List[str]:
        """Generate next steps for template bootstrap."""
        steps = []
        steps.extend(bootstrap_result.get('next_steps', []))

        # Add template-specific steps
        steps.extend([
            "Explore the recommended agents based on your industry template",
            "Start with required agents, then add recommended ones as needed",
            "Use the system regularly to enable rapid adaptation and learning",
            "Monitor learning milestones to track your progress"
        ])

        if bootstrap_result.get('customization_suggestions'):
            steps.append("Review customization suggestions to optimize template for your project")

        return steps

    def _generate_hybrid_next_steps(self, hybrid_status: Dict[str, Any]) -> List[str]:
        """Generate next steps for hybrid bootstrap."""
        steps = []

        if hybrid_status.get('learning_enabled'):
            steps.extend([
                "Continue using the system to improve hybrid intelligence",
                "Provide feedback on agent recommendations",
                "System combines universal patterns with your preferences"
            ])
        else:
            steps.extend([
                "Start using the system to enable adaptive learning",
                "System currently uses universal patterns - will learn your preferences",
                "Provide feedback to accelerate personalization"
            ])

        steps.extend([
            "Take advantage of industry best practices built into the system",
            "System will adapt to your project's unique needs over time"
        ])

        return steps

    def _generate_universal_next_steps(self) -> List[str]:
        """Generate next steps for universal patterns bootstrap."""
        return [
            "System is using universal industry patterns and best practices",
            "Consider upgrading to hybrid intelligence for personalized learning",
            "Provide consistent feedback to enable adaptive learning",
            "Universal patterns provide solid foundation for your project"
        ]

    def _generate_fallback_next_steps(self) -> List[str]:
        """Generate next steps for fallback bootstrap."""
        return [
            "Install ML dependencies to enable advanced AI capabilities",
            "Upgrade to hybrid intelligence system for better recommendations",
            "Current recommendations based on basic heuristics",
            "Consider enabling industry templates for domain-specific expertise"
        ]

    def _generate_expert_guidance(self, result: BootstrapResult, project_context: Dict[str, Any]) -> List[str]:
        """Generate expert guidance based on bootstrap result."""
        guidance = []

        # Mode-specific guidance
        if result.mode == "template":
            guidance.append("💡 Expert tip: Industry templates provide proven patterns - follow the recommended sequence")
            if result.template_info:
                industry = result.template_info.get('industry', 'general')
                if industry == 'fintech':
                    guidance.append("🔒 FinTech tip: Start with security and compliance agents for regulatory requirements")
                elif industry == 'healthcare':
                    guidance.append("🏥 Healthcare tip: Prioritize HIPAA compliance and data privacy from day one")
                elif industry == 'ecommerce':
                    guidance.append("🛒 E-commerce tip: Focus on security, performance, and user experience agents")

        elif result.mode == "hybrid":
            guidance.append("🧠 Expert tip: Hybrid intelligence learns your preferences - consistent feedback improves accuracy")

        # General guidance based on project characteristics
        complexity = project_context.get('complexity', 'medium')
        if complexity == 'high':
            guidance.append("⚡ Complexity tip: High complexity projects benefit from architecture and performance specialists")

        domain = project_context.get('domain')
        if domain in ['fintech', 'healthcare', 'government']:
            guidance.append("🛡️ Security tip: Regulated industries require security-first approach from project start")

        return guidance

    def _save_bootstrap_state(self, result: BootstrapResult):
        """Save bootstrap state and results."""
        # Update current bootstrap state
        self.current_bootstrap.update({
            "last_bootstrap": datetime.now().isoformat(),
            "current_mode": result.mode,
            "active_template": result.template_info.get('id') if result.template_info else None,
            "bootstrap_count": self.current_bootstrap.get('bootstrap_count', 0) + 1
        })

        # Add to bootstrap history
        bootstrap_entry = {
            "timestamp": datetime.now().isoformat(),
            "mode": result.mode,
            "status": result.status,
            "recommendation_count": len(result.recommendations),
            "template_id": result.template_info.get('id') if result.template_info else None,
            "metadata": result.bootstrap_metadata
        }

        self.current_bootstrap["bootstrap_history"].append(bootstrap_entry)

        # Keep history manageable
        if len(self.current_bootstrap["bootstrap_history"]) > 10:
            self.current_bootstrap["bootstrap_history"] = self.current_bootstrap["bootstrap_history"][-10:]

        # Save state
        state_file = self.bootstrap_dir / "bootstrap_state.json"
        with open(state_file, 'w') as f:
            json.dump(self.current_bootstrap, f, indent=2)

    def get_bootstrap_analytics(self) -> Dict[str, Any]:
        """Get analytics about bootstrap system usage."""
        return {
            "current_state": self.current_bootstrap,
            "system_capabilities": self._get_system_capabilities(),
            "bootstrap_modes_available": [
                mode for mode, available in {
                    "template": self.systems_available["templates"],
                    "hybrid": self.systems_available["hybrid_intelligence"],
                    "universal": self.systems_available["universal_patterns"],
                    "fallback": True
                }.items() if available
            ],
            "configuration": self.config,
            "analytics_timestamp": datetime.now().isoformat()
        }

    def reset_bootstrap_state(self) -> Dict[str, str]:
        """Reset bootstrap state (useful for testing or fresh start)."""
        self.current_bootstrap = {
            "bootstrap_id": f"bootstrap_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "bootstrap_history": [],
            "current_mode": None,
            "active_template": None,
            "learning_progress": {},
            "system_performance": {}
        }

        self._save_bootstrap_state(BootstrapResult(
            status="reset", mode="reset", template_info=None,
            recommendations=[], learning_pipeline={},
            system_capabilities={}, next_steps=[], bootstrap_metadata={}
        ))

        return {"status": "reset", "message": "Bootstrap state reset successfully"}


if __name__ == "__main__":
    # Demo usage
    bootstrap = SmartBootstrapSystem()

    # Test different project contexts
    test_contexts = [
        {
            'name': 'E-commerce Startup',
            'context': {
                'domain': 'ecommerce',
                'technologies': ['react', 'node.js', 'postgresql'],
                'complexity': 'medium',
                'team_size': 'small',
                'has_frontend': True,
                'has_backend': True
            }
        },
        {
            'name': 'Gaming Project',
            'context': {
                'domain': 'gaming',
                'technologies': ['c++', 'opengl', 'vulkan'],
                'complexity': 'high',
                'team_size': 'medium'
            }
        }
    ]

    print("🚀 Smart Bootstrap System Demo")
    print("=" * 45)

    for test in test_contexts:
        print(f"\n📋 Testing: {test['name']}")

        result = bootstrap.bootstrap_project(test['context'])

        print(f"   Status: {result.status}")
        print(f"   Mode: {result.mode}")
        print(f"   Recommendations: {len(result.recommendations)}")

        if result.template_info:
            print(f"   Template: {result.template_info['name']}")
            print(f"   Confidence: {result.template_info['confidence']:.2f}")

        print(f"   Next Steps: {len(result.next_steps)}")
        if result.next_steps:
            print(f"   • {result.next_steps[0]}")

    # Analytics
    analytics = bootstrap.get_bootstrap_analytics()
    print(f"\nBootstrap Analytics:")
    print(f"Available Modes: {', '.join(analytics['bootstrap_modes_available'])}")
    print(f"Total Bootstraps: {analytics['current_state'].get('bootstrap_count', 0)}")