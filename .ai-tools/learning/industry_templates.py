#!/usr/bin/env python3
"""
Industry Template System
Phase 3: Smart Bootstrap System - Pre-configured scenarios for different industries
"""

import json
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ProjectTemplate:
    """Represents an industry-specific project template"""
    template_id: str
    name: str
    industry: str
    description: str

    # Core configuration
    required_agents: List[str]
    recommended_agents: List[str]
    optional_agents: List[str]

    # Technology stack
    primary_technologies: List[str]
    secondary_technologies: List[str]
    infrastructure_tech: List[str]

    # Project characteristics
    typical_complexity: str
    typical_team_size: str
    development_phases: List[str]
    critical_aspects: List[str]

    # Best practices and patterns
    recommended_patterns: List[str]
    security_requirements: List[str]
    compliance_requirements: List[str]
    performance_requirements: List[str]

    # Learning configuration
    learning_focus_areas: List[str]
    success_metrics: List[str]
    common_challenges: List[str]

    # Template metadata
    confidence: float
    usage_frequency: int = 0
    last_updated: Optional[str] = None


@dataclass
class TemplateRecommendation:
    """Represents a template recommendation with confidence and reasoning"""
    template: ProjectTemplate
    confidence: float
    match_score: float
    reasoning: List[str]
    customization_suggestions: List[str]


class IndustryTemplateSystem:
    """
    System providing pre-configured industry templates for instant project setup
    with embedded expertise and best practice patterns.
    """

    def __init__(self):
        """Initialize industry template system."""
        self.templates = self._load_industry_templates()
        self.template_index = self._build_template_index()

    def _load_industry_templates(self) -> List[ProjectTemplate]:
        """Load comprehensive industry templates."""
        templates = [
            # E-commerce Template
            ProjectTemplate(
                template_id="ecommerce_standard",
                name="E-commerce Platform",
                industry="ecommerce",
                description="Complete e-commerce platform with payment processing, inventory management, and customer experience focus",

                required_agents=["backend-engineer", "frontend-engineer", "security-engineer"],
                recommended_agents=["api-engineer", "ux-designer", "qa-engineer", "database-administrator"],
                optional_agents=["performance-engineer", "data-engineer", "mobile-developer", "automation-engineer"],

                primary_technologies=["react", "node.js", "postgresql", "redis"],
                secondary_technologies=["typescript", "express", "prisma", "stripe-api"],
                infrastructure_tech=["docker", "aws", "nginx", "elasticsearch"],

                typical_complexity="medium",
                typical_team_size="medium",
                development_phases=["planning", "mvp", "core_features", "advanced_features", "optimization"],
                critical_aspects=["security", "performance", "user_experience", "scalability"],

                recommended_patterns=["microservices", "api_gateway", "caching", "cdn"],
                security_requirements=["pci_compliance", "data_encryption", "secure_payments", "fraud_detection"],
                compliance_requirements=["gdpr", "ccpa", "pci_dss"],
                performance_requirements=["sub_3s_load_time", "99.9_uptime", "horizontal_scaling"],

                learning_focus_areas=["user_behavior", "conversion_optimization", "security_patterns", "performance_optimization"],
                success_metrics=["conversion_rate", "page_load_time", "uptime", "security_incidents"],
                common_challenges=["payment_integration", "inventory_sync", "peak_traffic", "fraud_prevention"],

                confidence=0.95
            ),

            # FinTech Template
            ProjectTemplate(
                template_id="fintech_standard",
                name="Financial Technology Platform",
                industry="fintech",
                description="Financial services platform with regulatory compliance, security-first architecture, and audit capabilities",

                required_agents=["security-engineer", "compliance-auditor", "backend-engineer"],
                recommended_agents=["api-engineer", "data-engineer", "qa-engineer", "database-administrator"],
                optional_agents=["blockchain-engineer", "risk-manager", "performance-engineer", "automation-engineer"],

                primary_technologies=["java", "spring", "postgresql", "kafka"],
                secondary_technologies=["hibernate", "jwt", "oauth2", "microservices"],
                infrastructure_tech=["kubernetes", "aws", "vault", "prometheus"],

                typical_complexity="high",
                typical_team_size="large",
                development_phases=["compliance_planning", "core_security", "financial_features", "integration", "audit_preparation"],
                critical_aspects=["security", "compliance", "audit_trail", "data_protection"],

                recommended_patterns=["event_sourcing", "cqrs", "circuit_breaker", "saga_pattern"],
                security_requirements=["encryption_at_rest", "encryption_in_transit", "multi_factor_auth", "fraud_detection"],
                compliance_requirements=["pci_dss", "sox", "gdpr", "kyc_aml"],
                performance_requirements=["real_time_processing", "high_availability", "disaster_recovery"],

                learning_focus_areas=["regulatory_changes", "security_threats", "audit_requirements", "fraud_patterns"],
                success_metrics=["compliance_score", "security_incidents", "audit_results", "transaction_success_rate"],
                common_challenges=["regulatory_compliance", "security_requirements", "audit_preparation", "integration_complexity"],

                confidence=0.98
            ),

            # Healthcare Template
            ProjectTemplate(
                template_id="healthcare_standard",
                name="Healthcare Management System",
                industry="healthcare",
                description="Healthcare platform with HIPAA compliance, patient data protection, and clinical workflow optimization",

                required_agents=["security-engineer", "compliance-auditor", "backend-engineer"],
                recommended_agents=["frontend-engineer", "data-engineer", "ux-designer", "qa-engineer"],
                optional_agents=["mobile-developer", "integration-architect", "performance-engineer"],

                primary_technologies=["python", "django", "postgresql", "redis"],
                secondary_technologies=["celery", "jwt", "fhir", "hl7"],
                infrastructure_tech=["docker", "aws", "encryption", "backup_systems"],

                typical_complexity="high",
                typical_team_size="medium",
                development_phases=["compliance_setup", "patient_data_model", "clinical_workflows", "integration", "certification"],
                critical_aspects=["privacy", "security", "compliance", "data_integrity"],

                recommended_patterns=["data_encryption", "access_control", "audit_logging", "backup_recovery"],
                security_requirements=["hipaa_compliance", "data_encryption", "access_logging", "secure_communication"],
                compliance_requirements=["hipaa", "hitech", "gdpr", "fda_validation"],
                performance_requirements=["data_integrity", "backup_recovery", "uptime_requirements"],

                learning_focus_areas=["patient_workflows", "clinical_requirements", "compliance_updates", "integration_patterns"],
                success_metrics=["compliance_audit", "data_security", "user_adoption", "clinical_efficiency"],
                common_challenges=["hipaa_compliance", "system_integration", "clinical_workflows", "data_migration"],

                confidence=0.96
            ),

            # Gaming Template
            ProjectTemplate(
                template_id="gaming_standard",
                name="Gaming Platform",
                industry="gaming",
                description="High-performance gaming platform with real-time graphics, multiplayer capabilities, and performance optimization",

                required_agents=["graphics-3d-engineer", "performance-engineer", "backend-engineer"],
                recommended_agents=["math-specialist", "desktop-specialist", "qa-engineer"],
                optional_agents=["network-architect", "audio-engineer", "ui-engineer", "automation-engineer"],

                primary_technologies=["c++", "opengl", "vulkan", "networking"],
                secondary_technologies=["unity", "unreal", "physics_engine", "audio_system"],
                infrastructure_tech=["dedicated_servers", "cdn", "matchmaking", "analytics"],

                typical_complexity="high",
                typical_team_size="large",
                development_phases=["prototype", "core_gameplay", "graphics_optimization", "multiplayer", "launch_preparation"],
                critical_aspects=["performance", "graphics_quality", "user_experience", "scalability"],

                recommended_patterns=["entity_component_system", "object_pooling", "level_of_detail", "culling"],
                security_requirements=["anti_cheat", "secure_communication", "user_data_protection"],
                compliance_requirements=["age_rating", "privacy_policy", "regional_compliance"],
                performance_requirements=["60_fps_minimum", "low_latency", "memory_optimization", "loading_times"],

                learning_focus_areas=["player_behavior", "performance_bottlenecks", "graphics_optimization", "gameplay_balance"],
                success_metrics=["frame_rate", "loading_times", "player_retention", "crash_reports"],
                common_challenges=["performance_optimization", "cross_platform", "multiplayer_sync", "graphics_quality"],

                confidence=0.92
            ),

            # Enterprise SaaS Template
            ProjectTemplate(
                template_id="enterprise_saas",
                name="Enterprise SaaS Platform",
                industry="enterprise",
                description="Enterprise-grade SaaS platform with multi-tenancy, enterprise security, and scalable architecture",

                required_agents=["software-architect", "security-engineer", "backend-engineer"],
                recommended_agents=["frontend-engineer", "api-engineer", "devops-architect", "qa-engineer"],
                optional_agents=["data-engineer", "performance-engineer", "compliance-auditor", "ux-designer"],

                primary_technologies=["java", "spring", "postgresql", "microservices"],
                secondary_technologies=["kafka", "redis", "elasticsearch", "oauth2"],
                infrastructure_tech=["kubernetes", "docker", "aws", "monitoring"],

                typical_complexity="enterprise",
                typical_team_size="large",
                development_phases=["architecture", "core_platform", "tenant_management", "enterprise_features", "scaling"],
                critical_aspects=["scalability", "security", "multi_tenancy", "integration"],

                recommended_patterns=["microservices", "event_driven", "cqrs", "multi_tenant"],
                security_requirements=["enterprise_sso", "rbac", "audit_logging", "data_isolation"],
                compliance_requirements=["soc2", "gdpr", "iso27001", "enterprise_compliance"],
                performance_requirements=["horizontal_scaling", "high_availability", "enterprise_sla"],

                learning_focus_areas=["enterprise_requirements", "scaling_patterns", "integration_challenges", "tenant_behavior"],
                success_metrics=["uptime", "tenant_satisfaction", "scalability_metrics", "security_compliance"],
                common_challenges=["multi_tenancy", "enterprise_integration", "scaling_challenges", "compliance_requirements"],

                confidence=0.94
            ),

            # Startup MVP Template
            ProjectTemplate(
                template_id="startup_mvp",
                name="Startup MVP Platform",
                industry="startup",
                description="Rapid MVP development platform optimized for speed, flexibility, and cost-efficiency",

                required_agents=["backend-engineer", "frontend-engineer"],
                recommended_agents=["ux-designer", "product-manager", "qa-engineer"],
                optional_agents=["deployment-engineer", "mobile-developer", "data-engineer"],

                primary_technologies=["react", "node.js", "mongodb", "express"],
                secondary_technologies=["typescript", "jwt", "stripe", "sendgrid"],
                infrastructure_tech=["vercel", "mongodb_atlas", "cdn", "basic_monitoring"],

                typical_complexity="low",
                typical_team_size="small",
                development_phases=["mvp_planning", "core_features", "user_testing", "iteration", "scaling_preparation"],
                critical_aspects=["speed_to_market", "user_feedback", "cost_efficiency", "iteration_speed"],

                recommended_patterns=["monolith_first", "rapid_prototyping", "user_feedback_loops"],
                security_requirements=["basic_auth", "https", "data_protection"],
                compliance_requirements=["privacy_policy", "terms_of_service"],
                performance_requirements=["fast_loading", "mobile_responsive", "basic_scalability"],

                learning_focus_areas=["user_behavior", "feature_usage", "performance_bottlenecks", "market_validation"],
                success_metrics=["user_acquisition", "feature_adoption", "user_retention", "conversion_rates"],
                common_challenges=["feature_prioritization", "user_acquisition", "technical_debt", "scaling_decisions"],

                confidence=0.89
            ),

            # IoT Platform Template
            ProjectTemplate(
                template_id="iot_platform",
                name="IoT Platform",
                industry="iot",
                description="Internet of Things platform with device management, data collection, and real-time analytics",

                required_agents=["embedded-engineer", "backend-engineer", "data-engineer"],
                recommended_agents=["network-architect", "security-engineer", "frontend-engineer"],
                optional_agents=["electronics-engineer", "mobile-developer", "performance-engineer"],

                primary_technologies=["c", "python", "mqtt", "influxdb"],
                secondary_technologies=["arduino", "esp32", "raspberry_pi", "kafka"],
                infrastructure_tech=["aws_iot", "docker", "grafana", "prometheus"],

                typical_complexity="high",
                typical_team_size="medium",
                development_phases=["device_prototype", "connectivity", "data_pipeline", "analytics", "scaling"],
                critical_aspects=["connectivity", "data_integrity", "real_time_processing", "device_management"],

                recommended_patterns=["edge_computing", "data_streaming", "device_twins", "telemetry"],
                security_requirements=["device_authentication", "encrypted_communication", "secure_updates"],
                compliance_requirements=["iot_security", "data_privacy", "device_certification"],
                performance_requirements=["real_time_data", "low_latency", "high_throughput", "edge_processing"],

                learning_focus_areas=["device_behavior", "connectivity_patterns", "data_analytics", "edge_optimization"],
                success_metrics=["device_uptime", "data_accuracy", "latency", "scalability"],
                common_challenges=["connectivity_issues", "data_volume", "device_diversity", "edge_computing"],

                confidence=0.91
            ),

            # AI/ML Platform Template
            ProjectTemplate(
                template_id="ai_ml_platform",
                name="AI/ML Platform",
                industry="ai_ml",
                description="Machine learning platform with model training, deployment, and MLOps capabilities",

                required_agents=["data-scientist", "data-engineer", "backend-engineer"],
                recommended_agents=["ml-engineer", "devops-architect", "performance-engineer"],
                optional_agents=["frontend-engineer", "security-engineer", "qa-engineer"],

                primary_technologies=["python", "tensorflow", "pytorch", "jupyter"],
                secondary_technologies=["pandas", "numpy", "scikit-learn", "mlflow"],
                infrastructure_tech=["kubernetes", "docker", "gpu_clusters", "model_registry"],

                typical_complexity="high",
                typical_team_size="medium",
                development_phases=["data_preparation", "model_development", "training_pipeline", "deployment", "monitoring"],
                critical_aspects=["data_quality", "model_accuracy", "scalability", "monitoring"],

                recommended_patterns=["mlops", "model_versioning", "continuous_training", "a_b_testing"],
                security_requirements=["data_protection", "model_security", "access_control"],
                compliance_requirements=["data_privacy", "model_governance", "ai_ethics"],
                performance_requirements=["training_speed", "inference_latency", "scalability", "resource_efficiency"],

                learning_focus_areas=["model_performance", "data_patterns", "deployment_optimization", "user_behavior"],
                success_metrics=["model_accuracy", "inference_time", "data_quality", "deployment_success"],
                common_challenges=["data_quality", "model_drift", "scaling_inference", "mlops_implementation"],

                confidence=0.93
            )
        ]

        return templates

    def _build_template_index(self) -> Dict[str, Any]:
        """Build search index for templates."""
        index = {
            "by_industry": {},
            "by_complexity": {},
            "by_technology": {},
            "by_team_size": {}
        }

        for template in self.templates:
            # Index by industry
            if template.industry not in index["by_industry"]:
                index["by_industry"][template.industry] = []
            index["by_industry"][template.industry].append(template)

            # Index by complexity
            if template.typical_complexity not in index["by_complexity"]:
                index["by_complexity"][template.typical_complexity] = []
            index["by_complexity"][template.typical_complexity].append(template)

            # Index by technologies
            all_tech = template.primary_technologies + template.secondary_technologies + template.infrastructure_tech
            for tech in all_tech:
                if tech not in index["by_technology"]:
                    index["by_technology"][tech] = []
                index["by_technology"][tech].append(template)

            # Index by team size
            if template.typical_team_size not in index["by_team_size"]:
                index["by_team_size"][template.typical_team_size] = []
            index["by_team_size"][template.typical_team_size].append(template)

        return index

    def recommend_templates(self, project_context: Dict[str, Any]) -> List[TemplateRecommendation]:
        """
        Recommend templates based on project context.

        Args:
            project_context: Project context including domain, technologies, complexity

        Returns:
            List of template recommendations with confidence scores
        """
        recommendations = []

        for template in self.templates:
            match_score, reasoning = self._calculate_template_match(template, project_context)

            if match_score >= 0.3:  # Minimum threshold for recommendation
                customization_suggestions = self._generate_customization_suggestions(template, project_context)

                recommendation = TemplateRecommendation(
                    template=template,
                    confidence=template.confidence * match_score,
                    match_score=match_score,
                    reasoning=reasoning,
                    customization_suggestions=customization_suggestions
                )

                recommendations.append(recommendation)

        # Sort by confidence score
        recommendations.sort(key=lambda x: x.confidence, reverse=True)

        return recommendations

    def _calculate_template_match(self, template: ProjectTemplate, context: Dict[str, Any]) -> Tuple[float, List[str]]:
        """Calculate how well a template matches the project context."""
        score = 0.0
        reasoning = []

        # Industry match (highest weight)
        if context.get('domain') == template.industry:
            score += 0.4
            reasoning.append(f"Perfect industry match: {template.industry}")
        elif context.get('domain') in ['general', 'unknown'] and template.industry == 'startup':
            score += 0.2
            reasoning.append("Generic project - startup template suitable")

        # Technology match
        context_technologies = context.get('technologies', [])
        if context_technologies:
            tech_matches = []
            all_template_tech = template.primary_technologies + template.secondary_technologies

            for tech in context_technologies:
                for template_tech in all_template_tech:
                    if tech.lower() in template_tech.lower() or template_tech.lower() in tech.lower():
                        tech_matches.append(tech)
                        break

            if tech_matches:
                tech_score = len(tech_matches) / len(context_technologies)
                score += 0.3 * tech_score
                reasoning.append(f"Technology match: {', '.join(tech_matches)}")

        # Complexity match
        context_complexity = context.get('complexity', 'medium')
        if context_complexity == template.typical_complexity:
            score += 0.2
            reasoning.append(f"Complexity match: {context_complexity}")
        elif abs(self._complexity_to_number(context_complexity) - self._complexity_to_number(template.typical_complexity)) <= 1:
            score += 0.1
            reasoning.append(f"Close complexity match: {context_complexity} ≈ {template.typical_complexity}")

        # Team size consideration
        context_team_size = context.get('team_size', 'medium')
        if context_team_size == template.typical_team_size:
            score += 0.1
            reasoning.append(f"Team size match: {context_team_size}")

        return min(score, 1.0), reasoning

    def _complexity_to_number(self, complexity: str) -> int:
        """Convert complexity string to number for comparison."""
        mapping = {'low': 1, 'medium': 2, 'high': 3, 'enterprise': 4}
        return mapping.get(complexity, 2)

    def _generate_customization_suggestions(self, template: ProjectTemplate, context: Dict[str, Any]) -> List[str]:
        """Generate customization suggestions for the template."""
        suggestions = []

        # Technology customizations
        context_tech = set(context.get('technologies', []))
        template_tech = set(template.primary_technologies + template.secondary_technologies)

        missing_tech = context_tech - template_tech
        if missing_tech:
            suggestions.append(f"Consider adding these technologies: {', '.join(missing_tech)}")

        extra_tech = template_tech - context_tech
        if extra_tech and len(extra_tech) > 3:
            suggestions.append(f"Template includes additional technologies you may not need: {', '.join(list(extra_tech)[:3])}")

        # Complexity adjustments
        context_complexity = context.get('complexity', 'medium')
        if context_complexity != template.typical_complexity:
            if self._complexity_to_number(context_complexity) < self._complexity_to_number(template.typical_complexity):
                suggestions.append("Consider simplifying the template by removing optional components")
            else:
                suggestions.append("Consider adding enterprise-grade components and patterns")

        # Team size adjustments
        context_team_size = context.get('team_size', 'medium')
        if context_team_size == 'small' and template.typical_team_size in ['medium', 'large']:
            suggestions.append("With a small team, focus on required agents and defer optional ones")
        elif context_team_size == 'large' and template.typical_team_size == 'small':
            suggestions.append("With a large team, consider adding specialized roles and parallel workstreams")

        # Domain-specific suggestions
        if context.get('has_mobile', False) and 'mobile-developer' not in template.recommended_agents:
            suggestions.append("Add mobile-developer for mobile application requirements")

        if context.get('has_ai', False) and 'data-scientist' not in template.recommended_agents:
            suggestions.append("Add data-scientist and AI/ML specialists for AI features")

        return suggestions

    def get_template_by_id(self, template_id: str) -> Optional[ProjectTemplate]:
        """Get template by ID."""
        for template in self.templates:
            if template.template_id == template_id:
                return template
        return None

    def get_templates_by_industry(self, industry: str) -> List[ProjectTemplate]:
        """Get all templates for specific industry."""
        return self.template_index["by_industry"].get(industry, [])

    def get_templates_by_technology(self, technology: str) -> List[ProjectTemplate]:
        """Get templates that use specific technology."""
        return self.template_index["by_technology"].get(technology, [])

    def customize_template(self, template: ProjectTemplate, customizations: Dict[str, Any]) -> ProjectTemplate:
        """Create customized version of template."""
        # Create a copy of the template
        customized = ProjectTemplate(**asdict(template))

        # Apply customizations
        if 'additional_agents' in customizations:
            customized.recommended_agents.extend(customizations['additional_agents'])

        if 'additional_technologies' in customizations:
            customized.secondary_technologies.extend(customizations['additional_technologies'])

        if 'complexity_adjustment' in customizations:
            customized.typical_complexity = customizations['complexity_adjustment']

        if 'custom_requirements' in customizations:
            if 'security' in customizations['custom_requirements']:
                customized.security_requirements.extend(customizations['custom_requirements']['security'])
            if 'compliance' in customizations['custom_requirements']:
                customized.compliance_requirements.extend(customizations['custom_requirements']['compliance'])

        # Update metadata
        customized.template_id = f"{template.template_id}_custom_{datetime.now().strftime('%Y%m%d')}"
        customized.name = f"{template.name} (Customized)"
        customized.last_updated = datetime.now().isoformat()

        return customized

    def export_template_knowledge(self) -> Dict[str, Any]:
        """Export template knowledge for analysis."""
        return {
            "total_templates": len(self.templates),
            "industries_covered": list(self.template_index["by_industry"].keys()),
            "complexity_levels": list(self.template_index["by_complexity"].keys()),
            "technologies_covered": len(self.template_index["by_technology"]),
            "team_sizes_supported": list(self.template_index["by_team_size"].keys()),
            "template_summary": [
                {
                    "id": t.template_id,
                    "name": t.name,
                    "industry": t.industry,
                    "confidence": t.confidence,
                    "agent_count": len(t.required_agents + t.recommended_agents)
                }
                for t in self.templates
            ],
            "export_timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Demo usage
    template_system = IndustryTemplateSystem()

    # Test template recommendations
    test_contexts = [
        {
            'name': 'E-commerce Startup',
            'context': {
                'domain': 'ecommerce',
                'technologies': ['react', 'node.js', 'postgresql'],
                'complexity': 'medium',
                'team_size': 'small'
            }
        },
        {
            'name': 'FinTech Enterprise',
            'context': {
                'domain': 'fintech',
                'technologies': ['java', 'spring', 'postgresql'],
                'complexity': 'high',
                'team_size': 'large'
            }
        },
        {
            'name': 'Gaming Project',
            'context': {
                'domain': 'gaming',
                'technologies': ['c++', 'opengl'],
                'complexity': 'high',
                'team_size': 'medium'
            }
        }
    ]

    print("🏭 Industry Template System Demo")
    print("=" * 40)

    for test in test_contexts:
        print(f"\n📋 Testing: {test['name']}")
        recommendations = template_system.recommend_templates(test['context'])

        print(f"   Recommendations:")
        for rec in recommendations[:2]:
            print(f"   • {rec.template.name}: {rec.confidence:.2f}")
            print(f"     Match: {rec.match_score:.2f}")
            print(f"     Reasoning: {'; '.join(rec.reasoning)}")
            if rec.customization_suggestions:
                print(f"     Suggestions: {rec.customization_suggestions[0]}")

    # Export knowledge
    print(f"\nTemplate Knowledge Export:")
    export = template_system.export_template_knowledge()
    print(f"Total Templates: {export['total_templates']}")
    print(f"Industries: {', '.join(export['industries_covered'])}")
    print(f"Technologies: {export['technologies_covered']}")