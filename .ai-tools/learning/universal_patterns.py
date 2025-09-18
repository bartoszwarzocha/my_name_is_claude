#!/usr/bin/env python3
"""
Universal Patterns System
Base knowledge system with industry best practices and universal technology patterns
"""

import json
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime


@dataclass
class UniversalPattern:
    """Represents a universal pattern for agent-technology mapping"""
    pattern_id: str
    name: str
    technology_indicators: List[str]
    recommended_agents: List[str]
    confidence: float
    context_requirements: Dict[str, Any]
    industry_specific: Optional[str] = None


@dataclass
class BestPracticeRule:
    """Represents an industry best practice rule"""
    rule_id: str
    name: str
    condition: Dict[str, Any]
    recommended_agents: List[str]
    priority: int
    reasoning: str
    applicable_domains: List[str]


class UniversalPatternsSystem:
    """
    System that provides universal patterns and best practices
    for agent selection based on technology stacks and project contexts.
    """

    def __init__(self):
        """Initialize universal patterns system."""
        self.patterns = self._load_universal_patterns()
        self.best_practices = self._load_best_practices()
        self.domain_rules = self._load_domain_rules()
        self.complexity_indicators = self._load_complexity_indicators()

    def _load_universal_patterns(self) -> List[UniversalPattern]:
        """Load universal technology → agent patterns."""
        patterns = [
            # Frontend Development Patterns
            UniversalPattern(
                pattern_id="frontend_react",
                name="React Frontend Development",
                technology_indicators=["react", "jsx", "typescript", "javascript", "npm"],
                recommended_agents=["frontend-engineer", "ux-designer"],
                confidence=0.9,
                context_requirements={"has_frontend": True}
            ),
            UniversalPattern(
                pattern_id="frontend_angular",
                name="Angular Frontend Development",
                technology_indicators=["angular", "typescript", "@angular", "ng"],
                recommended_agents=["frontend-engineer", "ux-designer"],
                confidence=0.9,
                context_requirements={"has_frontend": True}
            ),
            UniversalPattern(
                pattern_id="frontend_vue",
                name="Vue.js Frontend Development",
                technology_indicators=["vue", "vue.js", "nuxt", "vuetify"],
                recommended_agents=["frontend-engineer", "ux-designer"],
                confidence=0.9,
                context_requirements={"has_frontend": True}
            ),

            # Backend Development Patterns
            UniversalPattern(
                pattern_id="backend_node",
                name="Node.js Backend Development",
                technology_indicators=["nodejs", "node.js", "express", "fastify", "npm"],
                recommended_agents=["backend-engineer", "api-engineer"],
                confidence=0.9,
                context_requirements={"has_backend": True}
            ),
            UniversalPattern(
                pattern_id="backend_python",
                name="Python Backend Development",
                technology_indicators=["python", "django", "flask", "fastapi", "pip"],
                recommended_agents=["backend-engineer", "api-engineer", "data-engineer"],
                confidence=0.9,
                context_requirements={"has_backend": True}
            ),
            UniversalPattern(
                pattern_id="backend_java",
                name="Java Backend Development",
                technology_indicators=["java", "spring", "maven", "gradle", "hibernate"],
                recommended_agents=["backend-engineer", "api-engineer"],
                confidence=0.9,
                context_requirements={"has_backend": True}
            ),

            # API Development Patterns
            UniversalPattern(
                pattern_id="api_rest",
                name="REST API Development",
                technology_indicators=["rest", "api", "endpoint", "swagger", "openapi"],
                recommended_agents=["api-engineer", "backend-engineer"],
                confidence=0.8,
                context_requirements={"has_api": True}
            ),
            UniversalPattern(
                pattern_id="api_graphql",
                name="GraphQL API Development",
                technology_indicators=["graphql", "apollo", "prisma", "hasura"],
                recommended_agents=["api-engineer", "backend-engineer"],
                confidence=0.8,
                context_requirements={"has_api": True}
            ),

            # Database Patterns
            UniversalPattern(
                pattern_id="database_sql",
                name="SQL Database Management",
                technology_indicators=["postgresql", "mysql", "sqlite", "sql"],
                recommended_agents=["database-administrator", "backend-engineer"],
                confidence=0.8,
                context_requirements={"has_database": True}
            ),
            UniversalPattern(
                pattern_id="database_nosql",
                name="NoSQL Database Management",
                technology_indicators=["mongodb", "redis", "cassandra", "dynamodb"],
                recommended_agents=["database-administrator", "data-engineer"],
                confidence=0.8,
                context_requirements={"has_database": True}
            ),

            # DevOps Patterns
            UniversalPattern(
                pattern_id="devops_containerization",
                name="Containerization & Orchestration",
                technology_indicators=["docker", "kubernetes", "k8s", "container"],
                recommended_agents=["deployment-engineer", "devops-architect"],
                confidence=0.9,
                context_requirements={"has_deployment": True}
            ),
            UniversalPattern(
                pattern_id="devops_cloud",
                name="Cloud Infrastructure",
                technology_indicators=["aws", "azure", "gcp", "cloud", "terraform"],
                recommended_agents=["cloud-engineer", "deployment-engineer"],
                confidence=0.9,
                context_requirements={"has_deployment": True}
            ),

            # Testing Patterns
            UniversalPattern(
                pattern_id="testing_unit",
                name="Unit Testing",
                technology_indicators=["jest", "pytest", "junit", "test", "spec"],
                recommended_agents=["qa-engineer", "backend-engineer", "frontend-engineer"],
                confidence=0.8,
                context_requirements={"has_tests": True}
            ),
            UniversalPattern(
                pattern_id="testing_e2e",
                name="End-to-End Testing",
                technology_indicators=["cypress", "playwright", "selenium", "e2e"],
                recommended_agents=["qa-engineer", "automation-engineer"],
                confidence=0.8,
                context_requirements={"has_tests": True}
            ),

            # Security Patterns
            UniversalPattern(
                pattern_id="security_auth",
                name="Authentication & Security",
                technology_indicators=["auth", "jwt", "oauth", "security", "encryption"],
                recommended_agents=["security-engineer", "backend-engineer"],
                confidence=0.8,
                context_requirements={"has_security": True}
            ),

            # Specialized Technology Patterns
            UniversalPattern(
                pattern_id="graphics_3d",
                name="3D Graphics Development",
                technology_indicators=["opengl", "vulkan", "3d", "shader", "graphics"],
                recommended_agents=["graphics-3d-engineer", "math-specialist"],
                confidence=0.9,
                context_requirements={"has_graphics": True}
            ),
            UniversalPattern(
                pattern_id="desktop_native",
                name="Native Desktop Development",
                technology_indicators=["wxwidgets", "qt", "desktop", "native", "gui"],
                recommended_agents=["desktop-specialist", "graphics-2d-engineer"],
                confidence=0.9,
                context_requirements={"has_desktop": True}
            ),
            UniversalPattern(
                pattern_id="embedded_systems",
                name="Embedded Systems Development",
                technology_indicators=["arduino", "esp32", "embedded", "microcontroller"],
                recommended_agents=["embedded-engineer", "electronics-engineer"],
                confidence=0.9,
                context_requirements={"has_embedded": True}
            )
        ]

        return patterns

    def _load_best_practices(self) -> List[BestPracticeRule]:
        """Load industry best practice rules."""
        rules = [
            # Architecture Best Practices
            BestPracticeRule(
                rule_id="architecture_microservices",
                name="Microservices Architecture",
                condition={"complexity": "high", "team_size": "large"},
                recommended_agents=["software-architect", "api-engineer", "deployment-engineer"],
                priority=1,
                reasoning="Large teams with high complexity benefit from microservices architecture",
                applicable_domains=["enterprise", "fintech", "ecommerce"]
            ),
            BestPracticeRule(
                rule_id="architecture_monolith",
                name="Monolithic Architecture",
                condition={"complexity": "low", "team_size": "small"},
                recommended_agents=["backend-engineer", "frontend-engineer"],
                priority=1,
                reasoning="Small teams with lower complexity should start with monolithic architecture",
                applicable_domains=["startup", "mvp", "prototype"]
            ),

            # Development Process Best Practices
            BestPracticeRule(
                rule_id="process_tdd",
                name="Test-Driven Development",
                condition={"quality_focus": "high", "has_tests": True},
                recommended_agents=["qa-engineer", "backend-engineer", "frontend-engineer"],
                priority=2,
                reasoning="High quality focus projects benefit from TDD approach",
                applicable_domains=["fintech", "healthcare", "enterprise"]
            ),
            BestPracticeRule(
                rule_id="process_ci_cd",
                name="Continuous Integration/Deployment",
                condition={"team_size": "medium", "has_deployment": True},
                recommended_agents=["devops-architect", "deployment-engineer"],
                priority=1,
                reasoning="Medium+ teams require automated CI/CD pipelines",
                applicable_domains=["enterprise", "saas", "platform"]
            ),

            # Security Best Practices
            BestPracticeRule(
                rule_id="security_first",
                name="Security-First Development",
                condition={"domain": ["fintech", "healthcare", "government"]},
                recommended_agents=["security-engineer", "compliance-auditor"],
                priority=1,
                reasoning="Regulated industries require security-first approach",
                applicable_domains=["fintech", "healthcare", "government"]
            ),

            # Performance Best Practices
            BestPracticeRule(
                rule_id="performance_optimization",
                name="Performance Optimization",
                condition={"expected_load": "high", "performance_critical": True},
                recommended_agents=["performance-engineer", "backend-engineer"],
                priority=2,
                reasoning="High-load applications require performance optimization from start",
                applicable_domains=["gaming", "streaming", "fintech"]
            ),

            # Data Management Best Practices
            BestPracticeRule(
                rule_id="data_governance",
                name="Data Governance & Privacy",
                condition={"handles_personal_data": True},
                recommended_agents=["data-engineer", "compliance-auditor", "security-engineer"],
                priority=1,
                reasoning="Projects handling personal data require proper governance",
                applicable_domains=["healthcare", "fintech", "ecommerce"]
            )
        ]

        return rules

    def _load_domain_rules(self) -> Dict[str, Dict[str, Any]]:
        """Load domain-specific rules and patterns."""
        return {
            "ecommerce": {
                "required_agents": ["backend-engineer", "frontend-engineer", "security-engineer"],
                "recommended_agents": ["api-engineer", "data-engineer", "qa-engineer"],
                "critical_aspects": ["security", "performance", "scalability"],
                "common_technologies": ["react", "node.js", "postgresql", "redis", "docker"],
                "best_practices": ["microservices", "caching", "payment_security"]
            },
            "fintech": {
                "required_agents": ["security-engineer", "compliance-auditor", "backend-engineer"],
                "recommended_agents": ["api-engineer", "data-engineer", "qa-engineer"],
                "critical_aspects": ["security", "compliance", "reliability"],
                "common_technologies": ["java", "spring", "postgresql", "kafka", "kubernetes"],
                "best_practices": ["security_first", "audit_logging", "data_encryption"]
            },
            "healthcare": {
                "required_agents": ["security-engineer", "compliance-auditor", "backend-engineer"],
                "recommended_agents": ["data-engineer", "qa-engineer", "frontend-engineer"],
                "critical_aspects": ["privacy", "compliance", "reliability"],
                "common_technologies": ["python", "django", "postgresql", "docker", "aws"],
                "best_practices": ["hipaa_compliance", "data_privacy", "secure_communication"]
            },
            "gaming": {
                "required_agents": ["graphics-3d-engineer", "performance-engineer", "backend-engineer"],
                "recommended_agents": ["math-specialist", "desktop-specialist", "qa-engineer"],
                "critical_aspects": ["performance", "graphics", "user_experience"],
                "common_technologies": ["unity", "unreal", "c++", "opengl", "vulkan"],
                "best_practices": ["performance_optimization", "graphics_pipeline", "real_time_systems"]
            },
            "enterprise": {
                "required_agents": ["software-architect", "security-engineer", "backend-engineer"],
                "recommended_agents": ["api-engineer", "deployment-engineer", "qa-engineer"],
                "critical_aspects": ["scalability", "security", "maintainability"],
                "common_technologies": ["java", "spring", "microservices", "kubernetes", "postgresql"],
                "best_practices": ["microservices", "ci_cd", "monitoring", "documentation"]
            },
            "startup": {
                "required_agents": ["backend-engineer", "frontend-engineer"],
                "recommended_agents": ["product-manager", "ux-designer", "deployment-engineer"],
                "critical_aspects": ["speed", "flexibility", "cost_efficiency"],
                "common_technologies": ["react", "node.js", "mongodb", "docker", "aws"],
                "best_practices": ["mvp_approach", "rapid_prototyping", "lean_development"]
            }
        }

    def _load_complexity_indicators(self) -> Dict[str, Dict[str, Any]]:
        """Load complexity indicators and their agent requirements."""
        return {
            "low": {
                "characteristics": ["<5 files", "single developer", "prototype", "mvp"],
                "recommended_agents": ["backend-engineer", "frontend-engineer"],
                "max_agents": 3,
                "focus": ["development", "basic_testing"]
            },
            "medium": {
                "characteristics": ["5-50 files", "2-5 developers", "production ready"],
                "recommended_agents": ["backend-engineer", "frontend-engineer", "qa-engineer"],
                "max_agents": 5,
                "focus": ["development", "testing", "basic_deployment"]
            },
            "high": {
                "characteristics": [">50 files", "5+ developers", "enterprise", "scaling"],
                "recommended_agents": ["software-architect", "backend-engineer", "frontend-engineer", "qa-engineer", "deployment-engineer"],
                "max_agents": 8,
                "focus": ["architecture", "development", "testing", "deployment", "monitoring"]
            },
            "enterprise": {
                "characteristics": [">200 files", "10+ developers", "multiple teams", "compliance"],
                "recommended_agents": ["software-architect", "security-engineer", "compliance-auditor", "backend-engineer", "frontend-engineer", "qa-engineer", "deployment-engineer"],
                "max_agents": 12,
                "focus": ["architecture", "security", "compliance", "development", "testing", "deployment", "monitoring"]
            }
        }

    def get_universal_recommendations(self, project_context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """
        Get universal agent recommendations based on project context.

        Args:
            project_context: Project context including technologies, domain, complexity

        Returns:
            List of tuples (agent_name, confidence, reasoning)
        """
        recommendations = []

        # Technology pattern matching
        tech_recommendations = self._match_technology_patterns(project_context)
        recommendations.extend(tech_recommendations)

        # Best practice rule matching
        best_practice_recommendations = self._apply_best_practice_rules(project_context)
        recommendations.extend(best_practice_recommendations)

        # Domain-specific recommendations
        domain_recommendations = self._apply_domain_rules(project_context)
        recommendations.extend(domain_recommendations)

        # Complexity-based recommendations
        complexity_recommendations = self._apply_complexity_rules(project_context)
        recommendations.extend(complexity_recommendations)

        # Consolidate and rank recommendations
        consolidated = self._consolidate_recommendations(recommendations)

        return consolidated

    def _match_technology_patterns(self, context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """Match technology indicators to universal patterns."""
        recommendations = []
        technologies = context.get('technologies', [])

        for pattern in self.patterns:
            # Check if pattern's technology indicators are present
            matches = [tech for tech in pattern.technology_indicators if tech.lower() in [t.lower() for t in technologies]]

            if matches:
                # Check context requirements
                context_match = all(
                    context.get(req_key) == req_value or (req_value is True and context.get(req_key, False))
                    for req_key, req_value in pattern.context_requirements.items()
                )

                if context_match or not pattern.context_requirements:
                    # Calculate confidence based on match ratio
                    match_ratio = len(matches) / len(pattern.technology_indicators)
                    confidence = pattern.confidence * match_ratio

                    for agent in pattern.recommended_agents:
                        reasoning = f"Universal pattern '{pattern.name}' (matched: {', '.join(matches)})"
                        recommendations.append((agent, confidence, reasoning))

        return recommendations

    def _apply_best_practice_rules(self, context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """Apply best practice rules based on project context."""
        recommendations = []

        for rule in self.best_practices:
            # Check if rule conditions are met
            conditions_met = all(
                context.get(condition_key) == condition_value or
                (isinstance(condition_value, list) and context.get(condition_key) in condition_value)
                for condition_key, condition_value in rule.condition.items()
            )

            if conditions_met:
                # Check if rule applies to current domain
                project_domain = context.get('domain', 'general')
                if not rule.applicable_domains or project_domain in rule.applicable_domains or 'general' in rule.applicable_domains:
                    confidence = 0.8 / rule.priority  # Higher priority = higher confidence

                    for agent in rule.recommended_agents:
                        reasoning = f"Best practice: {rule.reasoning}"
                        recommendations.append((agent, confidence, reasoning))

        return recommendations

    def _apply_domain_rules(self, context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """Apply domain-specific rules."""
        recommendations = []
        domain = context.get('domain')

        if domain and domain in self.domain_rules:
            domain_config = self.domain_rules[domain]

            # Required agents (high confidence)
            for agent in domain_config.get('required_agents', []):
                reasoning = f"Required for {domain} domain"
                recommendations.append((agent, 0.9, reasoning))

            # Recommended agents (medium confidence)
            for agent in domain_config.get('recommended_agents', []):
                reasoning = f"Recommended for {domain} domain"
                recommendations.append((agent, 0.7, reasoning))

        return recommendations

    def _apply_complexity_rules(self, context: Dict[str, Any]) -> List[Tuple[str, float, str]]:
        """Apply complexity-based rules."""
        recommendations = []
        complexity = context.get('complexity', 'medium')

        if complexity in self.complexity_indicators:
            complexity_config = self.complexity_indicators[complexity]

            for agent in complexity_config.get('recommended_agents', []):
                reasoning = f"Recommended for {complexity} complexity projects"
                recommendations.append((agent, 0.6, reasoning))

        return recommendations

    def _consolidate_recommendations(self, recommendations: List[Tuple[str, float, str]]) -> List[Tuple[str, float, str]]:
        """Consolidate and rank recommendations."""
        agent_scores = {}
        agent_reasons = {}

        # Aggregate scores for each agent
        for agent, confidence, reasoning in recommendations:
            if agent not in agent_scores:
                agent_scores[agent] = []
                agent_reasons[agent] = []

            agent_scores[agent].append(confidence)
            agent_reasons[agent].append(reasoning)

        # Calculate final scores and consolidate reasoning
        consolidated = []
        for agent, scores in agent_scores.items():
            # Use weighted average with boost for multiple matches
            final_score = sum(scores) / len(scores) * min(1.0, 0.5 + len(scores) * 0.1)
            combined_reasoning = "; ".join(set(agent_reasons[agent])[:3])  # Top 3 unique reasons

            consolidated.append((agent, final_score, combined_reasoning))

        # Sort by confidence score
        consolidated.sort(key=lambda x: x[1], reverse=True)

        return consolidated

    def get_domain_guidance(self, domain: str) -> Optional[Dict[str, Any]]:
        """Get specific guidance for a domain."""
        return self.domain_rules.get(domain)

    def get_complexity_guidance(self, complexity: str) -> Optional[Dict[str, Any]]:
        """Get specific guidance for a complexity level."""
        return self.complexity_indicators.get(complexity)

    def get_pattern_info(self, pattern_id: str) -> Optional[UniversalPattern]:
        """Get information about a specific pattern."""
        for pattern in self.patterns:
            if pattern.pattern_id == pattern_id:
                return pattern
        return None

    def export_universal_knowledge(self) -> Dict[str, Any]:
        """Export universal knowledge for analysis or transfer."""
        return {
            "patterns_count": len(self.patterns),
            "best_practices_count": len(self.best_practices),
            "supported_domains": list(self.domain_rules.keys()),
            "complexity_levels": list(self.complexity_indicators.keys()),
            "technology_coverage": sorted(list(set(
                tech for pattern in self.patterns
                for tech in pattern.technology_indicators
            ))),
            "export_timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Demo usage
    universal_system = UniversalPatternsSystem()

    # Test context
    test_context = {
        'technologies': ['react', 'node.js', 'postgresql', 'docker'],
        'domain': 'ecommerce',
        'complexity': 'medium',
        'has_frontend': True,
        'has_backend': True,
        'has_database': True
    }

    recommendations = universal_system.get_universal_recommendations(test_context)

    print("Universal Recommendations:")
    for agent, confidence, reasoning in recommendations[:5]:
        print(f"- {agent}: {confidence:.2f} ({reasoning})")

    print(f"\nUniversal Knowledge Export:")
    export = universal_system.export_universal_knowledge()
    print(json.dumps(export, indent=2))