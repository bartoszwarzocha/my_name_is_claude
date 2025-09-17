#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Feature Engineering Pipeline
Claude Code Multi-Agent Framework Enhancement

This module implements comprehensive feature engineering for converting
project context data into ML-ready feature vectors for agent recommendation models.

Components:
- Project Context Feature Encoder
- Agent Competency Feature Encoder
- Technology Similarity Calculator
- Business Domain Vectorizer
- Team Context Feature Extractor
- Success Pattern Feature Generator

Version: 1.0.0
Phase: 1 - Foundation Development
"""

import numpy as np
import pandas as pd
import json
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pickle
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class FeatureConfig:
    """Configuration for feature engineering pipeline"""
    technology_vector_size: int = 50
    domain_vector_size: int = 20
    complexity_features: int = 10
    team_features: int = 15
    mcp_features: int = 8
    total_features: int = 103  # Sum of above + additional derived features

@dataclass
class EncodedFeatures:
    """Container for encoded feature vectors"""
    project_features: np.ndarray
    agent_features: np.ndarray
    similarity_features: np.ndarray
    feature_names: List[str]
    metadata: Dict[str, Any]

class TechnologyStackEncoder:
    """Advanced technology stack encoding with semantic understanding"""

    def __init__(self):
        self.technology_categories = {
            'frontend': {
                'react': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7},
                'angular': {'complexity': 0.9, 'enterprise_readiness': 0.95, 'team_size_factor': 0.8},
                'vue': {'complexity': 0.6, 'enterprise_readiness': 0.7, 'team_size_factor': 0.6},
                'typescript': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7},
                'javascript': {'complexity': 0.5, 'enterprise_readiness': 0.6, 'team_size_factor': 0.5},
                'html5': {'complexity': 0.2, 'enterprise_readiness': 0.3, 'team_size_factor': 0.2},
                'css3': {'complexity': 0.3, 'enterprise_readiness': 0.4, 'team_size_factor': 0.3},
                'tailwind': {'complexity': 0.4, 'enterprise_readiness': 0.6, 'team_size_factor': 0.4},
                'bootstrap': {'complexity': 0.3, 'enterprise_readiness': 0.5, 'team_size_factor': 0.3}
            },
            'backend': {
                'python': {'complexity': 0.6, 'enterprise_readiness': 0.8, 'team_size_factor': 0.7},
                'fastapi': {'complexity': 0.7, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'django': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.8},
                'flask': {'complexity': 0.5, 'enterprise_readiness': 0.6, 'team_size_factor': 0.5},
                'nodejs': {'complexity': 0.6, 'enterprise_readiness': 0.7, 'team_size_factor': 0.6},
                'express': {'complexity': 0.5, 'enterprise_readiness': 0.6, 'team_size_factor': 0.5},
                'nestjs': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7},
                'java': {'complexity': 0.9, 'enterprise_readiness': 0.95, 'team_size_factor': 0.9},
                'spring': {'complexity': 0.9, 'enterprise_readiness': 0.95, 'team_size_factor': 0.9},
                'csharp': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.8},
                'go': {'complexity': 0.7, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'rust': {'complexity': 0.9, 'enterprise_readiness': 0.7, 'team_size_factor': 0.8}
            },
            'database': {
                'postgresql': {'complexity': 0.8, 'enterprise_readiness': 0.95, 'team_size_factor': 0.8},
                'mysql': {'complexity': 0.6, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'mongodb': {'complexity': 0.7, 'enterprise_readiness': 0.8, 'team_size_factor': 0.7},
                'redis': {'complexity': 0.6, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'sqlite': {'complexity': 0.3, 'enterprise_readiness': 0.4, 'team_size_factor': 0.3},
                'elasticsearch': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.8}
            },
            'infrastructure': {
                'docker': {'complexity': 0.7, 'enterprise_readiness': 0.9, 'team_size_factor': 0.6},
                'kubernetes': {'complexity': 0.9, 'enterprise_readiness': 0.95, 'team_size_factor': 0.8},
                'terraform': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7},
                'aws': {'complexity': 0.8, 'enterprise_readiness': 0.95, 'team_size_factor': 0.7},
                'azure': {'complexity': 0.8, 'enterprise_readiness': 0.95, 'team_size_factor': 0.7},
                'gcp': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7}
            },
            'testing': {
                'jest': {'complexity': 0.5, 'enterprise_readiness': 0.7, 'team_size_factor': 0.5},
                'pytest': {'complexity': 0.6, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'cypress': {'complexity': 0.7, 'enterprise_readiness': 0.8, 'team_size_factor': 0.6},
                'playwright': {'complexity': 0.8, 'enterprise_readiness': 0.9, 'team_size_factor': 0.7},
                'selenium': {'complexity': 0.6, 'enterprise_readiness': 0.7, 'team_size_factor': 0.6}
            }
        }

        # Technology compatibility matrix for semantic understanding
        self.compatibility_matrix = self._build_compatibility_matrix()

        # Initialize encoders
        self.label_encoders = {}
        self.one_hot_encoders = {}
        self.scaler = StandardScaler()

    def _build_compatibility_matrix(self) -> Dict[str, Dict[str, float]]:
        """Build technology compatibility matrix for semantic relationships"""
        compatibility = {}

        # Frontend-Backend compatibility
        frontend_backend = {
            'react': {'nodejs': 0.9, 'python': 0.7, 'java': 0.6, 'csharp': 0.6},
            'angular': {'nodejs': 0.9, 'java': 0.8, 'csharp': 0.8, 'python': 0.6},
            'vue': {'nodejs': 0.8, 'python': 0.7, 'php': 0.7},
            'typescript': {'nodejs': 0.95, 'python': 0.7, 'java': 0.7}
        }

        # Backend-Database compatibility
        backend_database = {
            'python': {'postgresql': 0.9, 'mysql': 0.8, 'mongodb': 0.8, 'redis': 0.9},
            'nodejs': {'mongodb': 0.9, 'postgresql': 0.8, 'mysql': 0.7, 'redis': 0.9},
            'java': {'postgresql': 0.9, 'mysql': 0.9, 'mongodb': 0.7, 'oracle': 0.9},
            'csharp': {'mssql': 0.95, 'postgresql': 0.8, 'mysql': 0.7}
        }

        compatibility.update({
            'frontend_backend': frontend_backend,
            'backend_database': backend_database
        })

        return compatibility

    def encode_technology_stack(self, tech_stack: Dict[str, List[str]]) -> np.ndarray:
        """
        Encode technology stack into comprehensive feature vector

        Args:
            tech_stack: Dictionary with technology categories and lists

        Returns:
            Feature vector representing technology stack characteristics
        """
        features = []

        # One-hot encoding for each technology category
        for category in ['frontend', 'backend', 'database', 'infrastructure', 'testing', 'mobile', 'desktop', 'graphics', 'ai_ml']:
            category_features = self._encode_category(tech_stack.get(category, []), category)
            features.extend(category_features)

        # Derived features
        complexity_score = self._calculate_stack_complexity(tech_stack)
        enterprise_readiness = self._calculate_enterprise_readiness(tech_stack)
        team_size_indicator = self._estimate_required_team_size(tech_stack)
        compatibility_score = self._calculate_stack_compatibility(tech_stack)

        features.extend([complexity_score, enterprise_readiness, team_size_indicator, compatibility_score])

        return np.array(features)

    def _encode_category(self, technologies: List[str], category: str) -> List[float]:
        """Encode a single technology category"""
        category_features = [0.0] * 5  # 5 features per category

        if not technologies:
            return category_features

        # Count technologies in category
        tech_count = len(technologies)
        category_features[0] = min(1.0, tech_count / 3.0)  # Normalized count

        # Average complexity
        complexities = []
        for tech in technologies:
            if category in self.technology_categories and tech in self.technology_categories[category]:
                complexities.append(self.technology_categories[category][tech]['complexity'])

        if complexities:
            category_features[1] = np.mean(complexities)

        # Average enterprise readiness
        enterprise_scores = []
        for tech in technologies:
            if category in self.technology_categories and tech in self.technology_categories[category]:
                enterprise_scores.append(self.technology_categories[category][tech]['enterprise_readiness'])

        if enterprise_scores:
            category_features[2] = np.mean(enterprise_scores)

        # Technology diversity in category
        category_features[3] = min(1.0, tech_count / 2.0)

        # Modern technology indicator (simplified heuristic)
        modern_techs = {'react', 'vue', 'typescript', 'fastapi', 'nestjs', 'kubernetes', 'docker', 'playwright'}
        modern_count = len([tech for tech in technologies if tech in modern_techs])
        category_features[4] = min(1.0, modern_count / max(1, tech_count))

        return category_features

    def _calculate_stack_complexity(self, tech_stack: Dict[str, List[str]]) -> float:
        """Calculate overall technology stack complexity"""
        total_complexity = 0.0
        tech_count = 0

        for category, technologies in tech_stack.items():
            if category in self.technology_categories:
                for tech in technologies:
                    if tech in self.technology_categories[category]:
                        total_complexity += self.technology_categories[category][tech]['complexity']
                        tech_count += 1

        return total_complexity / max(1, tech_count)

    def _calculate_enterprise_readiness(self, tech_stack: Dict[str, List[str]]) -> float:
        """Calculate enterprise readiness score"""
        total_readiness = 0.0
        tech_count = 0

        for category, technologies in tech_stack.items():
            if category in self.technology_categories:
                for tech in technologies:
                    if tech in self.technology_categories[category]:
                        total_readiness += self.technology_categories[category][tech]['enterprise_readiness']
                        tech_count += 1

        return total_readiness / max(1, tech_count)

    def _estimate_required_team_size(self, tech_stack: Dict[str, List[str]]) -> float:
        """Estimate required team size based on technology stack"""
        team_factors = []

        for category, technologies in tech_stack.items():
            if category in self.technology_categories:
                for tech in technologies:
                    if tech in self.technology_categories[category]:
                        team_factors.append(self.technology_categories[category][tech]['team_size_factor'])

        if not team_factors:
            return 0.5

        return np.mean(team_factors)

    def _calculate_stack_compatibility(self, tech_stack: Dict[str, List[str]]) -> float:
        """Calculate technology stack internal compatibility"""
        compatibility_scores = []

        # Check frontend-backend compatibility
        frontends = tech_stack.get('frontend', [])
        backends = tech_stack.get('backend', [])

        for frontend in frontends:
            for backend in backends:
                compatibility = self.compatibility_matrix.get('frontend_backend', {}).get(frontend, {}).get(backend, 0.5)
                compatibility_scores.append(compatibility)

        # Check backend-database compatibility
        databases = tech_stack.get('database', [])

        for backend in backends:
            for database in databases:
                compatibility = self.compatibility_matrix.get('backend_database', {}).get(backend, {}).get(database, 0.5)
                compatibility_scores.append(compatibility)

        return np.mean(compatibility_scores) if compatibility_scores else 0.5

class BusinessDomainVectorizer:
    """Advanced business domain encoding with industry context"""

    def __init__(self):
        self.domain_hierarchy = {
            'fintech': {
                'parent': 'financial_services',
                'complexity': 0.9,
                'compliance_weight': 0.95,
                'security_requirements': 0.95,
                'related_domains': ['ecommerce', 'enterprise']
            },
            'healthcare': {
                'parent': 'regulated_industry',
                'complexity': 0.85,
                'compliance_weight': 0.9,
                'security_requirements': 0.9,
                'related_domains': ['enterprise', 'api_integration']
            },
            'ecommerce': {
                'parent': 'retail',
                'complexity': 0.7,
                'compliance_weight': 0.8,
                'security_requirements': 0.8,
                'related_domains': ['fintech', 'api_integration']
            },
            'education': {
                'parent': 'public_sector',
                'complexity': 0.6,
                'compliance_weight': 0.7,
                'security_requirements': 0.7,
                'related_domains': ['enterprise', 'social']
            },
            'gaming': {
                'parent': 'entertainment',
                'complexity': 0.8,
                'compliance_weight': 0.5,
                'security_requirements': 0.6,
                'related_domains': ['social', 'mobile']
            },
            'enterprise': {
                'parent': 'business_software',
                'complexity': 0.85,
                'compliance_weight': 0.8,
                'security_requirements': 0.85,
                'related_domains': ['api_integration', 'data_analytics']
            },
            'data_analytics': {
                'parent': 'technology',
                'complexity': 0.8,
                'compliance_weight': 0.7,
                'security_requirements': 0.75,
                'related_domains': ['ai_ml', 'enterprise']
            },
            'ai_ml': {
                'parent': 'technology',
                'complexity': 0.9,
                'compliance_weight': 0.6,
                'security_requirements': 0.7,
                'related_domains': ['data_analytics', 'api_integration']
            },
            'iot': {
                'parent': 'technology',
                'complexity': 0.85,
                'compliance_weight': 0.7,
                'security_requirements': 0.8,
                'related_domains': ['embedded', 'api_integration']
            },
            'api_integration': {
                'parent': 'technology',
                'complexity': 0.7,
                'compliance_weight': 0.6,
                'security_requirements': 0.75,
                'related_domains': ['enterprise', 'microservices']
            }
        }

        self.compliance_frameworks = {
            'gdpr': {'complexity': 0.8, 'implementation_effort': 0.7},
            'hipaa': {'complexity': 0.9, 'implementation_effort': 0.8},
            'pci_dss': {'complexity': 0.85, 'implementation_effort': 0.75},
            'sox': {'complexity': 0.9, 'implementation_effort': 0.85},
            'iso27001': {'complexity': 0.8, 'implementation_effort': 0.7}
        }

    def encode_business_domain(self, domain_data: Dict[str, Any]) -> np.ndarray:
        """
        Encode business domain into comprehensive feature vector

        Args:
            domain_data: Business domain information from project analysis

        Returns:
            Feature vector representing business domain characteristics
        """
        features = []

        primary_domain = domain_data.get('primary', 'general')
        secondary_domains = domain_data.get('secondary', [])
        compliance_requirements = domain_data.get('compliance_requirements', [])
        industry_vertical = domain_data.get('industry_vertical', 'technology')

        # Primary domain encoding
        domain_features = self._encode_primary_domain(primary_domain)
        features.extend(domain_features)

        # Secondary domains encoding
        secondary_features = self._encode_secondary_domains(secondary_domains)
        features.extend(secondary_features)

        # Compliance requirements encoding
        compliance_features = self._encode_compliance_requirements(compliance_requirements)
        features.extend(compliance_features)

        # Industry vertical encoding
        industry_features = self._encode_industry_vertical(industry_vertical)
        features.extend(industry_features)

        return np.array(features)

    def _encode_primary_domain(self, primary_domain: str) -> List[float]:
        """Encode primary business domain"""
        features = [0.0] * 6

        if primary_domain in self.domain_hierarchy:
            domain_info = self.domain_hierarchy[primary_domain]

            features[0] = 1.0  # Has valid primary domain
            features[1] = domain_info['complexity']
            features[2] = domain_info['compliance_weight']
            features[3] = domain_info['security_requirements']
            features[4] = len(domain_info.get('related_domains', [])) / 5.0  # Normalized
            features[5] = 1.0 if domain_info.get('parent') in ['regulated_industry', 'financial_services'] else 0.0

        return features

    def _encode_secondary_domains(self, secondary_domains: List[str]) -> List[float]:
        """Encode secondary business domains"""
        features = [0.0] * 4

        if secondary_domains:
            features[0] = min(1.0, len(secondary_domains) / 3.0)  # Domain diversity

            # Average complexity of secondary domains
            complexities = []
            for domain in secondary_domains:
                if domain in self.domain_hierarchy:
                    complexities.append(self.domain_hierarchy[domain]['complexity'])

            if complexities:
                features[1] = np.mean(complexities)

            # Domain relationship strength
            relationship_scores = []
            for domain in secondary_domains:
                if domain in self.domain_hierarchy:
                    related = self.domain_hierarchy[domain].get('related_domains', [])
                    relationship_scores.append(len(related) / 5.0)

            if relationship_scores:
                features[2] = np.mean(relationship_scores)

            features[3] = 1.0 if len(secondary_domains) > 1 else 0.0  # Multi-domain indicator

        return features

    def _encode_compliance_requirements(self, compliance_requirements: List[str]) -> List[float]:
        """Encode compliance requirements"""
        features = [0.0] * 5

        if compliance_requirements:
            features[0] = min(1.0, len(compliance_requirements) / 3.0)  # Compliance burden

            # Average compliance complexity
            complexities = []
            implementation_efforts = []

            for requirement in compliance_requirements:
                if requirement in self.compliance_frameworks:
                    framework = self.compliance_frameworks[requirement]
                    complexities.append(framework['complexity'])
                    implementation_efforts.append(framework['implementation_effort'])

            if complexities:
                features[1] = np.mean(complexities)
                features[2] = np.mean(implementation_efforts)

            # Specific compliance indicators
            features[3] = 1.0 if 'gdpr' in compliance_requirements else 0.0
            features[4] = 1.0 if any(req in ['hipaa', 'sox', 'pci_dss'] for req in compliance_requirements) else 0.0

        return features

    def _encode_industry_vertical(self, industry_vertical: str) -> List[float]:
        """Encode industry vertical"""
        features = [0.0] * 5

        industry_mapping = {
            'financial_services': [1.0, 0.95, 0.9, 0.85, 1.0],
            'healthcare': [0.9, 0.9, 0.85, 0.8, 1.0],
            'retail': [0.7, 0.6, 0.7, 0.6, 0.0],
            'education': [0.6, 0.5, 0.6, 0.5, 0.0],
            'entertainment': [0.5, 0.4, 0.5, 0.4, 0.0],
            'technology': [0.8, 0.7, 0.7, 0.7, 0.0],
            'manufacturing': [0.7, 0.6, 0.7, 0.6, 0.0]
        }

        if industry_vertical in industry_mapping:
            features = industry_mapping[industry_vertical]

        return features

class ProjectComplexityEncoder:
    """Encode project complexity metrics"""

    def __init__(self):
        self.complexity_thresholds = {
            'file_count': {'startup': 100, 'sme': 500, 'enterprise': 1000},
            'code_lines': {'startup': 5000, 'sme': 25000, 'enterprise': 50000},
            'directory_depth': {'startup': 3, 'sme': 6, 'enterprise': 10},
            'dependency_count': {'startup': 20, 'sme': 50, 'enterprise': 100}
        }

    def encode_complexity(self, complexity_data: Dict[str, Any]) -> np.ndarray:
        """
        Encode project complexity metrics

        Args:
            complexity_data: Project complexity information

        Returns:
            Feature vector representing project complexity
        """
        features = []

        # Raw metrics (normalized)
        file_count = complexity_data.get('file_count', 0)
        code_lines = complexity_data.get('code_lines', 0)
        directory_depth = complexity_data.get('directory_depth', 0)
        dependency_count = complexity_data.get('dependency_count', 0)

        # Normalize metrics
        features.append(min(1.0, file_count / 1000.0))
        features.append(min(1.0, code_lines / 50000.0))
        features.append(min(1.0, directory_depth / 10.0))
        features.append(min(1.0, dependency_count / 100.0))

        # Complexity rating encoding
        complexity_rating = complexity_data.get('complexity_rating', 'startup')
        rating_encoding = {'startup': [1, 0, 0], 'sme': [0, 1, 0], 'enterprise': [0, 0, 1]}
        features.extend(rating_encoding.get(complexity_rating, [1, 0, 0]))

        # Derived complexity indicators
        overall_complexity = complexity_data.get('complexity_score', 0.0)
        features.append(overall_complexity)

        # Scale indicators
        features.append(1.0 if file_count > 500 else 0.0)  # Medium scale indicator
        features.append(1.0 if file_count > 1000 else 0.0)  # Large scale indicator

        # Code density
        code_density = code_lines / max(1, file_count)
        features.append(min(1.0, code_density / 100.0))

        return np.array(features)

class TeamContextEncoder:
    """Encode team context and development patterns"""

    def __init__(self):
        self.experience_indicators = {
            'test_driven_development': 0.8,
            'automated_deployment': 0.7,
            'architectural_discipline': 0.9,
            'code_quality_focus': 0.7,
            'type_safety_awareness': 0.6,
            'senior_level': 0.9,
            'intermediate_level': 0.6,
            'junior_level': 0.3
        }

        self.development_patterns = {
            'test_driven': 0.8,
            'containerized_development': 0.7,
            'api_first': 0.7,
            'microservices': 0.9
        }

    def encode_team_context(self, team_data: Dict[str, Any]) -> np.ndarray:
        """
        Encode team context and development patterns

        Args:
            team_data: Team context information

        Returns:
            Feature vector representing team characteristics
        """
        features = []

        # Team size encoding
        team_size = team_data.get('estimated_team_size', 'unknown')
        size_encoding = {'small': [1, 0, 0], 'medium': [0, 1, 0], 'large': [0, 0, 1], 'unknown': [0, 0, 0]}
        features.extend(size_encoding.get(team_size, [0, 0, 0]))

        # Experience indicators
        experience_indicators = team_data.get('experience_indicators', [])
        experience_score = 0.0
        for indicator in experience_indicators:
            if indicator in self.experience_indicators:
                experience_score += self.experience_indicators[indicator]

        features.append(min(1.0, experience_score / 3.0))  # Normalized experience score

        # Development patterns
        development_patterns = team_data.get('development_patterns', [])
        pattern_scores = []
        for pattern in development_patterns:
            if pattern in self.development_patterns:
                pattern_scores.append(self.development_patterns[pattern])

        if pattern_scores:
            features.append(np.mean(pattern_scores))
        else:
            features.append(0.0)

        # Git activity level
        git_activity = team_data.get('git_activity_level', 'unknown')
        activity_encoding = {'low': 0.2, 'medium': 0.6, 'high': 1.0, 'unknown': 0.0}
        features.append(activity_encoding.get(git_activity, 0.0))

        # Collaboration patterns
        collaboration_patterns = team_data.get('collaboration_patterns', [])
        features.append(1.0 if 'collaborative_development' in collaboration_patterns else 0.0)
        features.append(1.0 if 'feature_branch_workflow' in collaboration_patterns else 0.0)
        features.append(1.0 if 'code_review_process' in collaboration_patterns else 0.0)

        # Experience level indicators
        features.append(1.0 if 'senior_level' in experience_indicators else 0.0)
        features.append(1.0 if 'intermediate_level' in experience_indicators else 0.0)
        features.append(1.0 if 'junior_level' in experience_indicators else 0.0)

        # Quality focus indicators
        features.append(1.0 if 'test_driven_development' in experience_indicators else 0.0)
        features.append(1.0 if 'code_quality_focus' in experience_indicators else 0.0)
        features.append(1.0 if 'architectural_discipline' in experience_indicators else 0.0)

        return np.array(features)

class MCPToolsEncoder:
    """Encode MCP tools integration data"""

    def encode_mcp_insights(self, mcp_data: Dict[str, Any]) -> np.ndarray:
        """
        Encode MCP tools insights

        Args:
            mcp_data: MCP tools integration data

        Returns:
            Feature vector representing MCP tools capabilities
        """
        features = []

        # Tool availability
        features.append(1.0 if mcp_data.get('serena_available', False) else 0.0)
        features.append(1.0 if mcp_data.get('context7_available', False) else 0.0)
        features.append(1.0 if mcp_data.get('playwright_available', False) else 0.0)

        # Integration quality score
        integration_quality = mcp_data.get('integration_quality_score', 0.0)
        features.append(integration_quality)

        # Tool-specific insights (simplified encoding)
        serena_analysis = mcp_data.get('serena_analysis', '')
        features.append(1.0 if serena_analysis and 'complex' in serena_analysis.lower() else 0.0)

        context7_patterns = mcp_data.get('context7_patterns', '')
        features.append(1.0 if context7_patterns and 'async' in context7_patterns.lower() else 0.0)

        playwright_coverage = mcp_data.get('playwright_coverage', '')
        features.append(1.0 if playwright_coverage and 'comprehensive' in playwright_coverage.lower() else 0.0)

        # Overall MCP integration strength
        available_tools = sum([mcp_data.get('serena_available', False),
                              mcp_data.get('context7_available', False),
                              mcp_data.get('playwright_available', False)])
        features.append(available_tools / 3.0)

        return np.array(features)

class AgentCompetencyEncoder:
    """Encode agent competency and specialization data"""

    def __init__(self):
        # Agent competency matrix (simplified representation)
        self.agent_competencies = {
            'frontend-engineer': {
                'technologies': ['react', 'angular', 'vue', 'typescript', 'javascript'],
                'complexity_preference': 0.7,
                'team_size_preference': 0.6,
                'project_phase': 'development'
            },
            'backend-engineer': {
                'technologies': ['python', 'nodejs', 'java', 'csharp', 'go'],
                'complexity_preference': 0.8,
                'team_size_preference': 0.7,
                'project_phase': 'development'
            },
            'api-engineer': {
                'technologies': ['fastapi', 'express', 'spring', 'rest', 'graphql'],
                'complexity_preference': 0.8,
                'team_size_preference': 0.6,
                'project_phase': 'development'
            },
            'data-engineer': {
                'technologies': ['python', 'postgresql', 'mongodb', 'redis', 'spark'],
                'complexity_preference': 0.8,
                'team_size_preference': 0.7,
                'project_phase': 'architecture'
            },
            'deployment-engineer': {
                'technologies': ['docker', 'kubernetes', 'aws', 'terraform', 'jenkins'],
                'complexity_preference': 0.8,
                'team_size_preference': 0.6,
                'project_phase': 'deployment'
            },
            'security-engineer': {
                'technologies': ['security', 'compliance', 'authentication', 'encryption'],
                'complexity_preference': 0.9,
                'team_size_preference': 0.8,
                'project_phase': 'architecture'
            },
            'qa-engineer': {
                'technologies': ['jest', 'pytest', 'cypress', 'playwright', 'selenium'],
                'complexity_preference': 0.6,
                'team_size_preference': 0.5,
                'project_phase': 'quality_assurance'
            }
        }

    def encode_agent_compatibility(self, agent_name: str, project_context: Dict[str, Any]) -> float:
        """
        Calculate agent compatibility score with project context

        Args:
            agent_name: Name of the agent
            project_context: Project context data

        Returns:
            Compatibility score between 0 and 1
        """
        if agent_name not in self.agent_competencies:
            return 0.5  # Default compatibility for unknown agents

        agent_data = self.agent_competencies[agent_name]
        compatibility_scores = []

        # Technology compatibility
        project_technologies = []
        tech_stack = project_context.get('technology_stack', {})
        for category, techs in tech_stack.items():
            project_technologies.extend(techs)

        agent_technologies = agent_data['technologies']
        tech_overlap = len(set(project_technologies) & set(agent_technologies))
        tech_compatibility = tech_overlap / max(1, len(agent_technologies))
        compatibility_scores.append(tech_compatibility)

        # Complexity compatibility
        project_complexity = project_context.get('complexity', {}).get('complexity_score', 0.5)
        complexity_preference = agent_data['complexity_preference']
        complexity_compatibility = 1.0 - abs(project_complexity - complexity_preference)
        compatibility_scores.append(complexity_compatibility)

        # Team size compatibility
        team_context = project_context.get('team_context', {})
        team_size = team_context.get('estimated_team_size', 'medium')
        size_mapping = {'small': 0.3, 'medium': 0.6, 'large': 0.9}
        project_team_factor = size_mapping.get(team_size, 0.6)

        team_preference = agent_data['team_size_preference']
        team_compatibility = 1.0 - abs(project_team_factor - team_preference)
        compatibility_scores.append(team_compatibility)

        return np.mean(compatibility_scores)

class ProjectFeatureEncoder:
    """Main feature encoding coordinator"""

    def __init__(self, config: Optional[FeatureConfig] = None):
        self.config = config or FeatureConfig()

        # Initialize component encoders
        self.tech_encoder = TechnologyStackEncoder()
        self.domain_encoder = BusinessDomainVectorizer()
        self.complexity_encoder = ProjectComplexityEncoder()
        self.team_encoder = TeamContextEncoder()
        self.mcp_encoder = MCPToolsEncoder()
        self.agent_encoder = AgentCompetencyEncoder()

        # Initialize data transformers
        self.scaler = StandardScaler()
        self.feature_names = []

        # Fit status
        self.is_fitted = False

    def fit_transform(self, project_contexts: List[Dict[str, Any]]) -> np.ndarray:
        """
        Fit the encoder on training data and transform

        Args:
            project_contexts: List of project context dictionaries

        Returns:
            Transformed feature matrix
        """
        feature_matrix = self._encode_projects(project_contexts)
        self.scaler.fit(feature_matrix)
        self.is_fitted = True

        transformed_features = self.scaler.transform(feature_matrix)
        self._generate_feature_names()

        return transformed_features

    def transform(self, project_contexts: List[Dict[str, Any]]) -> np.ndarray:
        """
        Transform project contexts using fitted encoder

        Args:
            project_contexts: List of project context dictionaries

        Returns:
            Transformed feature matrix
        """
        if not self.is_fitted:
            raise ValueError("Encoder must be fitted before transform")

        feature_matrix = self._encode_projects(project_contexts)
        return self.scaler.transform(feature_matrix)

    def encode_single_project(self, project_context: Dict[str, Any]) -> np.ndarray:
        """
        Encode a single project context

        Args:
            project_context: Single project context dictionary

        Returns:
            Feature vector for the project
        """
        if not self.is_fitted:
            # For single project encoding without fitting, use default scaling
            feature_vector = self._encode_single_project(project_context)
            return feature_vector

        feature_vector = self._encode_single_project(project_context)
        return self.scaler.transform(feature_vector.reshape(1, -1))[0]

    def _encode_projects(self, project_contexts: List[Dict[str, Any]]) -> np.ndarray:
        """Encode list of project contexts"""
        feature_vectors = []

        for context in project_contexts:
            feature_vector = self._encode_single_project(context)
            feature_vectors.append(feature_vector)

        return np.array(feature_vectors)

    def _encode_single_project(self, project_context: Dict[str, Any]) -> np.ndarray:
        """Encode single project context into feature vector"""
        all_features = []

        # Technology stack features
        tech_features = self.tech_encoder.encode_technology_stack(
            project_context.get('technology_stack', {})
        )
        all_features.extend(tech_features)

        # Business domain features
        domain_features = self.domain_encoder.encode_business_domain(
            project_context.get('business_domain', {})
        )
        all_features.extend(domain_features)

        # Project complexity features
        complexity_features = self.complexity_encoder.encode_complexity(
            project_context.get('complexity', {})
        )
        all_features.extend(complexity_features)

        # Team context features
        team_features = self.team_encoder.encode_team_context(
            project_context.get('team_context', {})
        )
        all_features.extend(team_features)

        # MCP tools features
        mcp_features = self.mcp_encoder.encode_mcp_insights(
            project_context.get('mcp_insights', {})
        )
        all_features.extend(mcp_features)

        return np.array(all_features)

    def _generate_feature_names(self):
        """Generate descriptive feature names"""
        self.feature_names = []

        # Technology stack feature names (45 features: 9 categories * 5 features each)
        tech_categories = ['frontend', 'backend', 'database', 'infrastructure', 'testing', 'mobile', 'desktop', 'graphics', 'ai_ml']
        tech_features = ['count', 'complexity', 'enterprise_readiness', 'diversity', 'modernity']

        for category in tech_categories:
            for feature in tech_features:
                self.feature_names.append(f"tech_{category}_{feature}")

        # Technology stack derived features
        self.feature_names.extend(['tech_stack_complexity', 'tech_enterprise_readiness', 'tech_team_size_indicator', 'tech_compatibility_score'])

        # Business domain feature names (20 features)
        domain_features = ['primary_complexity', 'primary_compliance', 'primary_security', 'primary_relationships', 'primary_regulated']
        secondary_features = ['secondary_diversity', 'secondary_complexity', 'secondary_relationships', 'secondary_multi_domain']
        compliance_features = ['compliance_burden', 'compliance_complexity', 'compliance_effort', 'compliance_gdpr', 'compliance_regulated']
        industry_features = ['industry_complexity', 'industry_compliance', 'industry_security', 'industry_maturity', 'industry_regulated']

        self.feature_names.append('domain_has_primary')
        self.feature_names.extend([f"domain_{f}" for f in domain_features])
        self.feature_names.extend([f"domain_{f}" for f in secondary_features])
        self.feature_names.extend([f"domain_{f}" for f in compliance_features])
        self.feature_names.extend([f"domain_{f}" for f in industry_features])

        # Project complexity feature names (10 features)
        complexity_features = ['file_count_norm', 'code_lines_norm', 'directory_depth_norm', 'dependency_count_norm',
                             'rating_startup', 'rating_sme', 'rating_enterprise', 'overall_complexity',
                             'medium_scale', 'large_scale', 'code_density']
        self.feature_names.extend([f"complexity_{f}" for f in complexity_features])

        # Team context feature names (15 features)
        team_features = ['size_small', 'size_medium', 'size_large', 'experience_score', 'pattern_score',
                        'git_activity', 'collaborative', 'feature_branch', 'code_review',
                        'senior_level', 'intermediate_level', 'junior_level',
                        'test_driven', 'quality_focus', 'architectural_discipline']
        self.feature_names.extend([f"team_{f}" for f in team_features])

        # MCP tools feature names (8 features)
        mcp_features = ['serena_available', 'context7_available', 'playwright_available', 'integration_quality',
                       'serena_complex', 'context7_async', 'playwright_comprehensive', 'overall_strength']
        self.feature_names.extend([f"mcp_{f}" for f in mcp_features])

    def save_encoder(self, filepath: str):
        """Save fitted encoder to file"""
        if not self.is_fitted:
            raise ValueError("Cannot save unfitted encoder")

        encoder_data = {
            'config': self.config,
            'scaler': self.scaler,
            'feature_names': self.feature_names,
            'is_fitted': self.is_fitted
        }

        with open(filepath, 'wb') as f:
            pickle.dump(encoder_data, f)

        logger.info(f"Feature encoder saved to {filepath}")

    @classmethod
    def load_encoder(cls, filepath: str) -> 'ProjectFeatureEncoder':
        """Load fitted encoder from file"""
        with open(filepath, 'rb') as f:
            encoder_data = pickle.load(f)

        encoder = cls(encoder_data['config'])
        encoder.scaler = encoder_data['scaler']
        encoder.feature_names = encoder_data['feature_names']
        encoder.is_fitted = encoder_data['is_fitted']

        logger.info(f"Feature encoder loaded from {filepath}")
        return encoder

    def get_feature_importance_analysis(self, feature_importances: np.ndarray) -> Dict[str, float]:
        """
        Analyze feature importance scores

        Args:
            feature_importances: Feature importance array from trained model

        Returns:
            Dictionary with feature categories and their importance scores
        """
        if len(feature_importances) != len(self.feature_names):
            raise ValueError("Feature importance array length doesn't match feature names")

        # Group features by category
        feature_groups = {
            'technology_stack': [i for i, name in enumerate(self.feature_names) if name.startswith('tech_')],
            'business_domain': [i for i, name in enumerate(self.feature_names) if name.startswith('domain_')],
            'project_complexity': [i for i, name in enumerate(self.feature_names) if name.startswith('complexity_')],
            'team_context': [i for i, name in enumerate(self.feature_names) if name.startswith('team_')],
            'mcp_tools': [i for i, name in enumerate(self.feature_names) if name.startswith('mcp_')]
        }

        importance_analysis = {}
        for group_name, indices in feature_groups.items():
            group_importance = np.sum(feature_importances[indices])
            importance_analysis[group_name] = group_importance

        # Individual top features
        top_feature_indices = np.argsort(feature_importances)[-10:]
        importance_analysis['top_features'] = {
            self.feature_names[i]: feature_importances[i]
            for i in top_feature_indices
        }

        return importance_analysis

def main():
    """Demo feature engineering pipeline"""
    print("🔧 AI-POWERED AGENT SELECTION - FEATURE ENGINEERING DEMO")
    print("=" * 80)

    # Sample project contexts for demonstration
    sample_contexts = [
        {
            'technology_stack': {
                'frontend': ['react', 'typescript'],
                'backend': ['python', 'fastapi'],
                'database': ['postgresql'],
                'infrastructure': ['docker', 'aws'],
                'testing': ['jest', 'pytest']
            },
            'business_domain': {
                'primary': 'fintech',
                'secondary': ['api_integration'],
                'compliance_requirements': ['gdpr', 'pci_dss'],
                'industry_vertical': 'financial_services'
            },
            'complexity': {
                'file_count': 800,
                'code_lines': 35000,
                'directory_depth': 6,
                'dependency_count': 45,
                'complexity_rating': 'enterprise',
                'complexity_score': 0.75
            },
            'team_context': {
                'estimated_team_size': 'medium',
                'experience_indicators': ['senior_level', 'test_driven_development'],
                'development_patterns': ['api_first', 'containerized_development'],
                'git_activity_level': 'high',
                'collaboration_patterns': ['collaborative_development', 'code_review_process']
            },
            'mcp_insights': {
                'serena_available': True,
                'context7_available': True,
                'playwright_available': False,
                'integration_quality_score': 0.7,
                'serena_analysis': 'Complex multi-service architecture',
                'context7_patterns': 'Heavy use of async patterns'
            }
        }
    ]

    # Initialize and fit encoder
    encoder = ProjectFeatureEncoder()
    print("🔄 Fitting feature encoder on sample data...")

    # Fit and transform
    feature_matrix = encoder.fit_transform(sample_contexts)

    print(f"✅ Feature encoding complete!")
    print(f"📊 Feature matrix shape: {feature_matrix.shape}")
    print(f"📋 Number of features: {len(encoder.feature_names)}")

    # Display feature categories
    print(f"\n🏷️ FEATURE CATEGORIES:")
    print("-" * 40)

    feature_counts = {}
    for name in encoder.feature_names:
        category = name.split('_')[0]
        feature_counts[category] = feature_counts.get(category, 0) + 1

    for category, count in feature_counts.items():
        print(f"  {category.title()}: {count} features")

    # Show sample feature values
    print(f"\n📊 SAMPLE FEATURE VALUES (first 20 features):")
    print("-" * 40)
    for i in range(min(20, len(encoder.feature_names))):
        feature_name = encoder.feature_names[i]
        feature_value = feature_matrix[0][i]
        print(f"  {feature_name}: {feature_value:.3f}")

    # Demo agent compatibility calculation
    print(f"\n🤖 AGENT COMPATIBILITY DEMO:")
    print("-" * 40)

    agents_to_test = ['frontend-engineer', 'backend-engineer', 'api-engineer', 'security-engineer', 'qa-engineer']

    for agent in agents_to_test:
        compatibility = encoder.agent_encoder.encode_agent_compatibility(agent, sample_contexts[0])
        compatibility_level = "🟢 High" if compatibility > 0.7 else "🟡 Medium" if compatibility > 0.4 else "🔴 Low"
        print(f"  {agent}: {compatibility:.3f} {compatibility_level}")

    print(f"\n✅ Feature engineering pipeline demonstrated successfully!")
    print("🚀 Ready for ML model training phase!")

if __name__ == "__main__":
    main()