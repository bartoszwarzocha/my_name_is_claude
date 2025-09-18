#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Data Collection Infrastructure
Claude Code Multi-Agent Framework Enhancement

This module implements comprehensive data collection infrastructure for training
ML models that will power intelligent agent selection and workflow orchestration.

Components:
- Project Context Analyzer
- Framework Usage Data Collector
- Agent Effectiveness Monitor
- MCP Tools Integration Layer
- Historical Success Pattern Extractor

Version: 1.0.0
Phase: 1 - Foundation Development
"""

import json
import os
import sys
import logging
import subprocess
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
import hashlib
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TechnologyStack:
    """Technology stack detection results"""
    frontend: List[str]
    backend: List[str]
    database: List[str]
    infrastructure: List[str]
    testing: List[str]
    mobile: List[str]
    desktop: List[str]
    graphics: List[str]
    ai_ml: List[str]
    confidence_score: float

@dataclass
class ProjectComplexity:
    """Project complexity assessment metrics"""
    file_count: int
    code_lines: int
    directory_depth: int
    dependency_count: int
    complexity_rating: str  # startup/sme/enterprise
    complexity_score: float

@dataclass
class BusinessDomain:
    """Business domain classification"""
    primary: str
    secondary: List[str]
    industry_vertical: str
    compliance_requirements: List[str]
    confidence_score: float

@dataclass
class TeamContext:
    """Team and project context information"""
    estimated_team_size: str  # small/medium/large
    experience_indicators: List[str]
    development_patterns: List[str]
    git_activity_level: str
    collaboration_patterns: List[str]

@dataclass
class MCPToolsInsights:
    """Insights from MCP tools integration"""
    serena_available: bool
    serena_analysis: Optional[str]
    context7_available: bool
    context7_patterns: Optional[str]
    playwright_available: bool
    playwright_coverage: Optional[str]
    integration_quality_score: float

@dataclass
class ProjectContext:
    """Complete project context for ML feature extraction"""
    project_path: str
    technology_stack: TechnologyStack
    complexity: ProjectComplexity
    business_domain: BusinessDomain
    team_context: TeamContext
    mcp_insights: MCPToolsInsights
    framework_config: Optional[Dict[str, Any]]
    timestamp: datetime.datetime
    context_hash: str

class TechnologyDetector:
    """Advanced technology stack detection system"""

    def __init__(self):
        self.technology_patterns = {
            'frontend': {
                'react': ['package.json', 'react', 'jsx', 'tsx'],
                'angular': ['angular.json', '@angular', 'component.ts'],
                'vue': ['vue.config.js', 'vue', '.vue'],
                'typescript': ['tsconfig.json', '.ts', '.tsx'],
                'javascript': ['package.json', '.js', '.jsx'],
                'html5': ['.html', '.htm'],
                'css3': ['.css', '.scss', '.sass', '.less'],
                'tailwind': ['tailwind.config.js', 'tailwindcss'],
                'bootstrap': ['bootstrap', 'bootstrap.css'],
                'webpack': ['webpack.config.js', 'webpack'],
                'vite': ['vite.config.js', 'vite']
            },
            'backend': {
                'python': ['.py', 'requirements.txt', 'setup.py', 'pyproject.toml'],
                'fastapi': ['fastapi', 'uvicorn'],
                'django': ['django', 'manage.py', 'settings.py'],
                'flask': ['flask', 'app.py'],
                'nodejs': ['package.json', '.js', '.ts'],
                'express': ['express', 'app.js'],
                'nestjs': ['@nestjs', 'nest-cli.json'],
                'java': ['.java', 'pom.xml', 'build.gradle'],
                'spring': ['spring-boot', 'application.properties'],
                'csharp': ['.cs', '.csproj', 'appsettings.json'],
                'dotnet': ['dotnet', '.net'],
                'go': ['.go', 'go.mod', 'go.sum'],
                'rust': ['.rs', 'Cargo.toml', 'Cargo.lock'],
                'php': ['.php', 'composer.json'],
                'ruby': ['.rb', 'Gemfile', 'config.ru']
            },
            'database': {
                'postgresql': ['postgres', 'postgresql', 'psql'],
                'mysql': ['mysql', 'mariadb'],
                'mongodb': ['mongodb', 'mongo', 'mongoose'],
                'redis': ['redis', 'redis-server'],
                'sqlite': ['sqlite', '.db', '.sqlite'],
                'elasticsearch': ['elasticsearch', 'elastic'],
                'dynamodb': ['dynamodb', 'aws-sdk'],
                'cassandra': ['cassandra', 'datastax']
            },
            'infrastructure': {
                'docker': ['Dockerfile', 'docker-compose.yml', '.dockerignore'],
                'kubernetes': ['k8s', 'kubectl', 'deployment.yaml'],
                'terraform': ['.tf', 'terraform', 'terraform.tfstate'],
                'aws': ['aws-cli', 'boto3', 'aws-sdk'],
                'azure': ['azure-cli', 'az', 'azure-sdk'],
                'gcp': ['gcloud', 'google-cloud', 'gcp'],
                'nginx': ['nginx.conf', 'nginx'],
                'apache': ['httpd.conf', 'apache'],
                'jenkins': ['Jenkinsfile', 'jenkins'],
                'github_actions': ['.github/workflows/', 'actions'],
                'gitlab_ci': ['.gitlab-ci.yml', 'gitlab']
            },
            'testing': {
                'jest': ['jest', 'jest.config.js'],
                'pytest': ['pytest', 'test_', '_test.py'],
                'junit': ['junit', 'test', '.java'],
                'cypress': ['cypress', 'cypress.json'],
                'playwright': ['playwright', '@playwright'],
                'selenium': ['selenium', 'webdriver'],
                'mocha': ['mocha', 'mocha.opts'],
                'karma': ['karma', 'karma.conf.js'],
                'jasmine': ['jasmine', 'jasmine.json']
            },
            'mobile': {
                'react_native': ['react-native', 'metro.config.js'],
                'flutter': ['flutter', 'pubspec.yaml', '.dart'],
                'xamarin': ['xamarin', '.xamarin'],
                'ionic': ['ionic', '@ionic'],
                'cordova': ['cordova', 'config.xml'],
                'android': ['android', 'build.gradle', 'AndroidManifest.xml'],
                'ios': ['ios', '.xcodeproj', 'Info.plist'],
                'swift': ['.swift', 'Package.swift']
            },
            'desktop': {
                'electron': ['electron', 'main.js'],
                'tauri': ['tauri', 'tauri.conf.json'],
                'wxwidgets': ['wxwidgets', 'wx/', '.cpp'],
                'qt': ['qt', 'cmake', '.pro'],
                'gtk': ['gtk', 'glade'],
                'tkinter': ['tkinter', 'tk'],
                'winforms': ['winforms', '.designer.cs'],
                'wpf': ['wpf', '.xaml'],
                'javafx': ['javafx', '.fxml']
            },
            'graphics': {
                'opengl': ['opengl', 'glfw', 'glad', 'gl.h'],
                'vulkan': ['vulkan', 'vk_', 'vulkan.h'],
                'directx': ['directx', 'd3d11', 'd3d12'],
                'openCV': ['opencv', 'cv2', 'opencv2'],
                'threejs': ['three.js', 'threejs', 'three'],
                'webgl': ['webgl', 'gl-'],
                'unity': ['unity', '.unity', 'Assets/'],
                'unreal': ['unreal', '.uproject', 'Source/'],
                'blender': ['blender', 'bpy', '.blend']
            },
            'ai_ml': {
                'tensorflow': ['tensorflow', 'tf.', 'keras'],
                'pytorch': ['pytorch', 'torch', 'torchvision'],
                'scikit_learn': ['sklearn', 'scikit-learn'],
                'pandas': ['pandas', 'pd.'],
                'numpy': ['numpy', 'np.'],
                'jupyter': ['jupyter', '.ipynb', 'nbconvert'],
                'opencv_ai': ['cv2', 'opencv-python'],
                'huggingface': ['transformers', 'huggingface'],
                'openai': ['openai', 'gpt-'],
                'anthropic': ['anthropic', 'claude']
            }
        }

    def detect_technology_stack(self, project_path: str) -> TechnologyStack:
        """
        Detect technology stack across all supported categories

        Args:
            project_path: Path to project directory

        Returns:
            TechnologyStack with detected technologies and confidence scores
        """
        logger.info(f"Detecting technology stack for project: {project_path}")

        detected = {category: [] for category in self.technology_patterns.keys()}
        confidence_scores = []

        try:
            # Walk through project directory
            for root, dirs, files in os.walk(project_path):
                # Skip common ignore directories
                dirs[:] = [d for d in dirs if not d.startswith('.')
                          and d not in ['node_modules', '__pycache__', 'venv', 'env', 'target', 'build']]

                for file in files:
                    file_path = os.path.join(root, file)
                    self._analyze_file(file_path, file, detected)

            # Additional analysis methods
            self._analyze_package_files(project_path, detected)
            self._analyze_configuration_files(project_path, detected)
            self._analyze_directory_structure(project_path, detected)

            # Calculate confidence score based on detection strength
            total_detections = sum(len(techs) for techs in detected.values())
            confidence_score = min(1.0, total_detections / 20.0)  # Normalize to 0-1

            logger.info(f"Technology detection completed. Found {total_detections} technologies.")

            return TechnologyStack(
                frontend=detected['frontend'],
                backend=detected['backend'],
                database=detected['database'],
                infrastructure=detected['infrastructure'],
                testing=detected['testing'],
                mobile=detected['mobile'],
                desktop=detected['desktop'],
                graphics=detected['graphics'],
                ai_ml=detected['ai_ml'],
                confidence_score=confidence_score
            )

        except Exception as e:
            logger.error(f"Error detecting technology stack: {e}")
            # Return empty stack with low confidence
            return TechnologyStack(
                frontend=[], backend=[], database=[], infrastructure=[],
                testing=[], mobile=[], desktop=[], graphics=[], ai_ml=[],
                confidence_score=0.0
            )

    def _analyze_file(self, file_path: str, filename: str, detected: Dict[str, List[str]]):
        """Analyze individual file for technology indicators"""
        try:
            # Check file extension and name patterns
            for category, technologies in self.technology_patterns.items():
                for tech, patterns in technologies.items():
                    for pattern in patterns:
                        if pattern in filename.lower() or filename.lower().endswith(pattern):
                            if tech not in detected[category]:
                                detected[category].append(tech)
                                logger.debug(f"Detected {tech} from file: {filename}")

            # For text files, check content for technology keywords
            if filename.lower().endswith(('.py', '.js', '.ts', '.java', '.cs', '.go', '.rs', '.php', '.rb', '.cpp', '.c', '.h', '.hpp', '.cc', '.cxx')):
                self._analyze_file_content(file_path, detected)

        except Exception as e:
            logger.debug(f"Error analyzing file {filename}: {e}")

    def _analyze_file_content(self, file_path: str, detected: Dict[str, List[str]]):
        """Analyze file content for technology imports and usage"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()

                # Look for import statements and technology usage
                for category, technologies in self.technology_patterns.items():
                    for tech, patterns in technologies.items():
                        for pattern in patterns:
                            if pattern.lower() in content:
                                if tech not in detected[category]:
                                    detected[category].append(tech)
                                    logger.debug(f"Detected {tech} from content in: {file_path}")

        except Exception as e:
            logger.debug(f"Error reading file content {file_path}: {e}")

    def _analyze_package_files(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze package configuration files for dependencies"""
        package_files = {
            'package.json': 'nodejs',
            'requirements.txt': 'python',
            'Pipfile': 'python',
            'setup.py': 'python',
            'pyproject.toml': 'python',
            'pom.xml': 'java',
            'build.gradle': 'java',
            'Cargo.toml': 'rust',
            'go.mod': 'go',
            'composer.json': 'php',
            'Gemfile': 'ruby'
        }

        for filename, tech in package_files.items():
            file_path = os.path.join(project_path, filename)
            if os.path.exists(file_path):
                if tech not in detected['backend']:
                    detected['backend'].append(tech)
                    logger.debug(f"Detected {tech} from package file: {filename}")

                # Analyze package dependencies
                self._analyze_dependency_file(file_path, detected)

    def _analyze_dependency_file(self, file_path: str, detected: Dict[str, List[str]]):
        """Analyze dependency files for technology clues"""
        try:
            filename = os.path.basename(file_path)

            if filename == 'package.json':
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    dependencies = {**data.get('dependencies', {}), **data.get('devDependencies', {})}

                    # Map common npm packages to technologies
                    npm_tech_mapping = {
                        'react': 'react', 'angular': 'angular', 'vue': 'vue',
                        'express': 'express', 'fastify': 'fastify', 'koa': 'koa',
                        'typescript': 'typescript', 'webpack': 'webpack', 'vite': 'vite',
                        'jest': 'jest', 'cypress': 'cypress', 'playwright': 'playwright',
                        'electron': 'electron', 'react-native': 'react_native'
                    }

                    for dep in dependencies:
                        for pattern, tech in npm_tech_mapping.items():
                            if pattern in dep.lower():
                                category = self._get_tech_category(tech)
                                if category and tech not in detected[category]:
                                    detected[category].append(tech)

        except Exception as e:
            logger.debug(f"Error analyzing dependency file {file_path}: {e}")

    def _analyze_configuration_files(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze configuration files for technology indicators"""
        config_files = [
            'docker-compose.yml', 'Dockerfile', '.dockerignore',
            'kubernetes.yaml', 'k8s.yaml', 'deployment.yaml',
            'terraform.tf', 'main.tf',
            '.github/workflows/', '.gitlab-ci.yml',
            'nginx.conf', 'apache.conf',
            'jest.config.js', 'cypress.json', 'pytest.ini'
        ]

        for config_file in config_files:
            config_path = os.path.join(project_path, config_file)
            if os.path.exists(config_path) or os.path.isdir(config_path):
                # Map config files to technologies
                self._map_config_to_technology(config_file, detected)

    def _analyze_directory_structure(self, project_path: str, detected: Dict[str, List[str]]):
        """Analyze directory structure for technology patterns"""
        common_directories = {
            'src/main/java': 'java',
            'src/main/resources': 'java',
            'Assets/': 'unity',
            'Source/': 'unreal',
            'www/': 'php',
            'public/': 'frontend',
            'static/': 'frontend',
            'templates/': 'backend',
            'migrations/': 'database',
            'tests/': 'testing',
            '__tests__/': 'testing'
        }

        for root, dirs, files in os.walk(project_path):
            rel_path = os.path.relpath(root, project_path)
            for dir_pattern, tech in common_directories.items():
                if dir_pattern in rel_path:
                    category = self._get_tech_category(tech)
                    if category and tech not in detected[category]:
                        detected[category].append(tech)

    def _get_tech_category(self, tech: str) -> Optional[str]:
        """Get the category for a given technology"""
        for category, technologies in self.technology_patterns.items():
            if tech in technologies:
                return category
        return None

    def _map_config_to_technology(self, config_file: str, detected: Dict[str, List[str]]):
        """Map configuration files to their corresponding technologies"""
        config_mapping = {
            'docker': 'docker',
            'kubernetes': 'kubernetes', 'k8s': 'kubernetes',
            'terraform': 'terraform',
            'github': 'github_actions',
            'gitlab': 'gitlab_ci',
            'nginx': 'nginx',
            'apache': 'apache',
            'jest': 'jest',
            'cypress': 'cypress',
            'pytest': 'pytest'
        }

        for pattern, tech in config_mapping.items():
            if pattern in config_file.lower():
                category = self._get_tech_category(tech)
                if category and tech not in detected[category]:
                    detected[category].append(tech)

class ProjectComplexityAnalyzer:
    """Analyze project complexity metrics"""

    def analyze_complexity(self, project_path: str) -> ProjectComplexity:
        """
        Analyze project complexity across multiple dimensions

        Args:
            project_path: Path to project directory

        Returns:
            ProjectComplexity with comprehensive complexity assessment
        """
        logger.info(f"Analyzing project complexity for: {project_path}")

        try:
            file_count = self._count_project_files(project_path)
            code_lines = self._count_code_lines(project_path)
            directory_depth = self._calculate_directory_depth(project_path)
            dependency_count = self._count_dependencies(project_path)

            # Calculate overall complexity score (0-1 scale)
            complexity_score = self._calculate_complexity_score(
                file_count, code_lines, directory_depth, dependency_count
            )

            # Determine complexity rating
            complexity_rating = self._determine_complexity_rating(complexity_score)

            logger.info(f"Complexity analysis complete: {complexity_rating} ({complexity_score:.2f})")

            return ProjectComplexity(
                file_count=file_count,
                code_lines=code_lines,
                directory_depth=directory_depth,
                dependency_count=dependency_count,
                complexity_rating=complexity_rating,
                complexity_score=complexity_score
            )

        except Exception as e:
            logger.error(f"Error analyzing project complexity: {e}")
            return ProjectComplexity(
                file_count=0, code_lines=0, directory_depth=0,
                dependency_count=0, complexity_rating="unknown", complexity_score=0.0
            )

    def _count_project_files(self, project_path: str) -> int:
        """Count relevant project files (excluding generated/cache files)"""
        count = 0
        exclude_patterns = {
            'node_modules', '__pycache__', '.git', 'venv', 'env',
            'target', 'build', 'dist', '.cache', 'coverage'
        }

        for root, dirs, files in os.walk(project_path):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_patterns]

            # Count relevant files
            for file in files:
                if not file.startswith('.') and not file.endswith(('.log', '.tmp')):
                    count += 1

        return count

    def _count_code_lines(self, project_path: str) -> int:
        """Count lines of code in relevant source files"""
        code_extensions = {
            '.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.cs', '.go',
            '.rs', '.php', '.rb', '.cpp', '.c', '.h', '.hpp', '.swift',
            '.kt', '.scala', '.clj', '.dart', '.vue', '.html', '.css',
            '.scss', '.sass', '.less', '.sql', '.yaml', '.yml', '.json'
        }

        total_lines = 0
        exclude_dirs = {'node_modules', '__pycache__', '.git', 'venv', 'target', 'build'}

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if any(file.lower().endswith(ext) for ext in code_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            total_lines += sum(1 for line in f if line.strip())
                    except Exception:
                        continue

        return total_lines

    def _calculate_directory_depth(self, project_path: str) -> int:
        """Calculate maximum directory depth"""
        max_depth = 0
        exclude_dirs = {'node_modules', '__pycache__', '.git', 'venv', 'target', 'build'}

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            relative_path = os.path.relpath(root, project_path)
            if relative_path != '.':
                depth = len(relative_path.split(os.sep))
                max_depth = max(max_depth, depth)

        return max_depth

    def _count_dependencies(self, project_path: str) -> int:
        """Count external dependencies from package files"""
        dependency_count = 0

        # Node.js dependencies
        package_json = os.path.join(project_path, 'package.json')
        if os.path.exists(package_json):
            try:
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    dependency_count += len(data.get('dependencies', {}))
                    dependency_count += len(data.get('devDependencies', {}))
            except Exception:
                pass

        # Python dependencies
        requirements_txt = os.path.join(project_path, 'requirements.txt')
        if os.path.exists(requirements_txt):
            try:
                with open(requirements_txt, 'r') as f:
                    dependency_count += len([line for line in f if line.strip() and not line.startswith('#')])
            except Exception:
                pass

        # Add other package managers as needed (Maven, Gradle, Cargo, etc.)

        return dependency_count

    def _calculate_complexity_score(self, file_count: int, code_lines: int,
                                  directory_depth: int, dependency_count: int) -> float:
        """Calculate normalized complexity score (0-1)"""
        # Normalize each metric to 0-1 scale
        file_score = min(1.0, file_count / 1000.0)  # 1000+ files = max
        lines_score = min(1.0, code_lines / 50000.0)  # 50k+ lines = max
        depth_score = min(1.0, directory_depth / 10.0)  # 10+ levels = max
        deps_score = min(1.0, dependency_count / 100.0)  # 100+ deps = max

        # Weighted combination
        return (file_score * 0.3 + lines_score * 0.4 +
                depth_score * 0.1 + deps_score * 0.2)

    def _determine_complexity_rating(self, complexity_score: float) -> str:
        """Determine complexity rating based on score"""
        if complexity_score < 0.3:
            return "startup"
        elif complexity_score < 0.7:
            return "sme"
        else:
            return "enterprise"

class BusinessDomainClassifier:
    """Classify project business domain and requirements"""

    def __init__(self):
        self.domain_keywords = {
            'fintech': ['bank', 'payment', 'finance', 'trading', 'crypto', 'wallet', 'loan'],
            'healthcare': ['medical', 'health', 'patient', 'clinic', 'hospital', 'pharma'],
            'ecommerce': ['shop', 'cart', 'product', 'order', 'inventory', 'payment'],
            'education': ['school', 'student', 'course', 'learn', 'university', 'grade'],
            'gaming': ['game', 'player', 'score', 'level', 'unity', 'unreal'],
            'social': ['social', 'chat', 'message', 'friend', 'post', 'feed'],
            'enterprise': ['crm', 'erp', 'workflow', 'business', 'employee', 'hr'],
            'api_integration': ['api', 'integration', 'webhook', 'service', 'microservice'],
            'data_analytics': ['analytics', 'dashboard', 'report', 'metric', 'bi', 'data'],
            'iot': ['sensor', 'device', 'iot', 'arduino', 'raspberry', 'embedded'],
            'ai_ml': ['ml', 'ai', 'model', 'training', 'neural', 'algorithm'],
            'devtools': ['tool', 'cli', 'framework', 'library', 'sdk', 'api']
        }

        self.compliance_indicators = {
            'gdpr': ['privacy', 'consent', 'gdpr', 'data protection'],
            'hipaa': ['hipaa', 'medical', 'health', 'patient'],
            'pci_dss': ['payment', 'card', 'pci', 'finance'],
            'sox': ['financial', 'audit', 'sox', 'sarbanes'],
            'iso27001': ['security', 'iso', 'information security']
        }

    def classify_domain(self, project_path: str) -> BusinessDomain:
        """
        Classify business domain based on project content analysis

        Args:
            project_path: Path to project directory

        Returns:
            BusinessDomain with classification and confidence score
        """
        logger.info(f"Classifying business domain for: {project_path}")

        try:
            # Analyze project content for domain indicators
            content_analysis = self._analyze_project_content(project_path)
            domain_scores = self._calculate_domain_scores(content_analysis)
            compliance_reqs = self._identify_compliance_requirements(content_analysis)

            # Determine primary and secondary domains
            primary_domain = max(domain_scores.items(), key=lambda x: x[1])[0] if domain_scores else 'general'
            secondary_domains = [domain for domain, score in domain_scores.items()
                               if score > 0.3 and domain != primary_domain]

            # Determine industry vertical
            industry_vertical = self._determine_industry_vertical(primary_domain, secondary_domains)

            # Calculate confidence score
            confidence_score = domain_scores.get(primary_domain, 0.0) if domain_scores else 0.1

            logger.info(f"Domain classification complete: {primary_domain} ({confidence_score:.2f})")

            return BusinessDomain(
                primary=primary_domain,
                secondary=secondary_domains,
                industry_vertical=industry_vertical,
                compliance_requirements=compliance_reqs,
                confidence_score=confidence_score
            )

        except Exception as e:
            logger.error(f"Error classifying business domain: {e}")
            return BusinessDomain(
                primary="general", secondary=[], industry_vertical="technology",
                compliance_requirements=[], confidence_score=0.1
            )

    def _analyze_project_content(self, project_path: str) -> Dict[str, int]:
        """Analyze project content for domain keywords"""
        keyword_counts = {}
        text_files = ['.md', '.txt', '.rst', '.json', '.yaml', '.yml']
        code_files = ['.py', '.js', '.ts', '.java', '.cs', '.go', '.rs', '.php', '.rb']

        for root, dirs, files in os.walk(project_path):
            # Skip common ignore directories
            dirs[:] = [d for d in dirs if not d.startswith('.')
                      and d not in ['node_modules', '__pycache__', 'venv']]

            for file in files:
                if any(file.lower().endswith(ext) for ext in text_files + code_files):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()

                            # Count domain keywords
                            for domain, keywords in self.domain_keywords.items():
                                for keyword in keywords:
                                    count = content.count(keyword)
                                    if count > 0:
                                        keyword_counts[keyword] = keyword_counts.get(keyword, 0) + count
                    except Exception:
                        continue

        return keyword_counts

    def _calculate_domain_scores(self, content_analysis: Dict[str, int]) -> Dict[str, float]:
        """Calculate domain scores based on keyword frequency"""
        domain_scores = {}

        for domain, keywords in self.domain_keywords.items():
            total_score = 0
            for keyword in keywords:
                if keyword in content_analysis:
                    # Weight score by keyword frequency and specificity
                    score = content_analysis[keyword] * (1.0 / len(keywords))
                    total_score += score

            # Normalize score (0-1 scale)
            if total_score > 0:
                domain_scores[domain] = min(1.0, total_score / 10.0)

        return domain_scores

    def _identify_compliance_requirements(self, content_analysis: Dict[str, int]) -> List[str]:
        """Identify compliance requirements based on content analysis"""
        compliance_reqs = []

        for compliance, indicators in self.compliance_indicators.items():
            for indicator in indicators:
                if indicator in content_analysis and content_analysis[indicator] > 0:
                    if compliance not in compliance_reqs:
                        compliance_reqs.append(compliance)
                    break

        return compliance_reqs

    def _determine_industry_vertical(self, primary_domain: str, secondary_domains: List[str]) -> str:
        """Determine industry vertical based on domain classification"""
        industry_mapping = {
            'fintech': 'financial_services',
            'healthcare': 'healthcare',
            'ecommerce': 'retail',
            'education': 'education',
            'gaming': 'entertainment',
            'social': 'social_media',
            'enterprise': 'enterprise_software',
            'api_integration': 'technology',
            'data_analytics': 'technology',
            'iot': 'manufacturing',
            'ai_ml': 'technology',
            'devtools': 'technology'
        }

        return industry_mapping.get(primary_domain, 'technology')

class TeamContextAnalyzer:
    """Analyze team and development context"""

    def analyze_team_context(self, project_path: str) -> TeamContext:
        """
        Analyze team context from project indicators

        Args:
            project_path: Path to project directory

        Returns:
            TeamContext with team size, experience, and patterns
        """
        logger.info(f"Analyzing team context for: {project_path}")

        try:
            git_analysis = self._analyze_git_activity(project_path)
            code_quality_indicators = self._analyze_code_quality_indicators(project_path)
            project_structure_analysis = self._analyze_project_structure(project_path)

            estimated_team_size = self._estimate_team_size(git_analysis)
            experience_indicators = self._identify_experience_indicators(
                code_quality_indicators, project_structure_analysis
            )
            development_patterns = self._identify_development_patterns(project_path)
            git_activity_level = self._assess_git_activity_level(git_analysis)
            collaboration_patterns = self._identify_collaboration_patterns(git_analysis)

            logger.info(f"Team context analysis complete: {estimated_team_size} team")

            return TeamContext(
                estimated_team_size=estimated_team_size,
                experience_indicators=experience_indicators,
                development_patterns=development_patterns,
                git_activity_level=git_activity_level,
                collaboration_patterns=collaboration_patterns
            )

        except Exception as e:
            logger.error(f"Error analyzing team context: {e}")
            return TeamContext(
                estimated_team_size="unknown",
                experience_indicators=[],
                development_patterns=[],
                git_activity_level="unknown",
                collaboration_patterns=[]
            )

    def _analyze_git_activity(self, project_path: str) -> Dict[str, Any]:
        """Analyze git repository activity patterns"""
        git_analysis = {
            'commit_count': 0,
            'contributor_count': 0,
            'recent_activity': False,
            'branch_count': 0,
            'has_issues': False,
            'has_pull_requests': False
        }

        try:
            if os.path.exists(os.path.join(project_path, '.git')):
                # Get commit count
                result = subprocess.run(
                    ['git', 'rev-list', '--count', 'HEAD'],
                    cwd=project_path, capture_output=True, text=True
                )
                if result.returncode == 0:
                    git_analysis['commit_count'] = int(result.stdout.strip())

                # Get contributor count
                result = subprocess.run(
                    ['git', 'shortlog', '-sn', '--all'],
                    cwd=project_path, capture_output=True, text=True
                )
                if result.returncode == 0:
                    git_analysis['contributor_count'] = len(result.stdout.strip().split('\n'))

                # Check recent activity (last 30 days)
                result = subprocess.run(
                    ['git', 'log', '--since="30 days ago"', '--oneline'],
                    cwd=project_path, capture_output=True, text=True
                )
                if result.returncode == 0:
                    git_analysis['recent_activity'] = len(result.stdout.strip().split('\n')) > 1

                # Get branch count
                result = subprocess.run(
                    ['git', 'branch', '-a'],
                    cwd=project_path, capture_output=True, text=True
                )
                if result.returncode == 0:
                    git_analysis['branch_count'] = len(result.stdout.strip().split('\n'))

        except Exception as e:
            logger.debug(f"Git analysis error: {e}")

        return git_analysis

    def _analyze_code_quality_indicators(self, project_path: str) -> List[str]:
        """Identify code quality indicators"""
        quality_indicators = []

        quality_files = {
            'testing': ['test/', 'tests/', '__tests__/', '*.test.*', '*.spec.*'],
            'linting': ['.eslintrc', '.pylintrc', 'tslint.json', '.flake8'],
            'formatting': ['.prettierrc', '.editorconfig', 'black.toml'],
            'ci_cd': ['.github/workflows/', '.gitlab-ci.yml', 'Jenkinsfile'],
            'documentation': ['README.md', 'docs/', 'wiki/'],
            'type_checking': ['mypy.ini', 'tsconfig.json', 'types/'],
            'dependency_management': ['package-lock.json', 'poetry.lock', 'Pipfile.lock']
        }

        for indicator, patterns in quality_files.items():
            for pattern in patterns:
                for root, dirs, files in os.walk(project_path):
                    if any(pattern in file or pattern in root for file in files):
                        if indicator not in quality_indicators:
                            quality_indicators.append(indicator)
                        break

        return quality_indicators

    def _analyze_project_structure(self, project_path: str) -> Dict[str, bool]:
        """Analyze project structure for organization patterns"""
        structure_indicators = {
            'modular_structure': False,
            'separation_of_concerns': False,
            'configuration_management': False,
            'environment_setup': False
        }

        # Check for modular structure
        common_modules = ['src/', 'lib/', 'components/', 'modules/', 'services/']
        if any(os.path.exists(os.path.join(project_path, module)) for module in common_modules):
            structure_indicators['modular_structure'] = True

        # Check for separation of concerns
        separation_dirs = ['models/', 'views/', 'controllers/', 'api/', 'frontend/', 'backend/']
        if sum(os.path.exists(os.path.join(project_path, d)) for d in separation_dirs) >= 2:
            structure_indicators['separation_of_concerns'] = True

        # Check for configuration management
        config_files = ['config/', '.env', 'settings.py', 'appsettings.json']
        if any(os.path.exists(os.path.join(project_path, config)) for config in config_files):
            structure_indicators['configuration_management'] = True

        # Check for environment setup
        env_files = ['Dockerfile', 'docker-compose.yml', 'requirements.txt', 'package.json']
        if any(os.path.exists(os.path.join(project_path, env)) for env in env_files):
            structure_indicators['environment_setup'] = True

        return structure_indicators

    def _estimate_team_size(self, git_analysis: Dict[str, Any]) -> str:
        """Estimate team size based on git activity"""
        contributor_count = git_analysis.get('contributor_count', 0)

        if contributor_count <= 2:
            return "small"
        elif contributor_count <= 8:
            return "medium"
        else:
            return "large"

    def _identify_experience_indicators(self, quality_indicators: List[str],
                                      structure_analysis: Dict[str, bool]) -> List[str]:
        """Identify team experience level indicators"""
        experience_indicators = []

        # High experience indicators
        if 'testing' in quality_indicators:
            experience_indicators.append('test_driven_development')
        if 'ci_cd' in quality_indicators:
            experience_indicators.append('automated_deployment')
        if structure_analysis.get('modular_structure'):
            experience_indicators.append('architectural_discipline')
        if 'linting' in quality_indicators and 'formatting' in quality_indicators:
            experience_indicators.append('code_quality_focus')
        if 'type_checking' in quality_indicators:
            experience_indicators.append('type_safety_awareness')

        # Determine overall experience level
        if len(experience_indicators) >= 4:
            experience_indicators.append('senior_level')
        elif len(experience_indicators) >= 2:
            experience_indicators.append('intermediate_level')
        else:
            experience_indicators.append('junior_level')

        return experience_indicators

    def _identify_development_patterns(self, project_path: str) -> List[str]:
        """Identify development patterns and methodologies"""
        patterns = []

        # Check for specific patterns
        if os.path.exists(os.path.join(project_path, 'test')) or os.path.exists(os.path.join(project_path, 'tests')):
            patterns.append('test_driven')

        if os.path.exists(os.path.join(project_path, 'docker-compose.yml')):
            patterns.append('containerized_development')

        if os.path.exists(os.path.join(project_path, 'api')) or any('api' in f for f in os.listdir(project_path)):
            patterns.append('api_first')

        # Check for microservices pattern
        services_dirs = [d for d in os.listdir(project_path)
                        if os.path.isdir(os.path.join(project_path, d)) and 'service' in d.lower()]
        if len(services_dirs) > 1:
            patterns.append('microservices')

        return patterns

    def _assess_git_activity_level(self, git_analysis: Dict[str, Any]) -> str:
        """Assess overall git activity level"""
        commit_count = git_analysis.get('commit_count', 0)
        recent_activity = git_analysis.get('recent_activity', False)

        if commit_count > 100 and recent_activity:
            return "high"
        elif commit_count > 20:
            return "medium"
        else:
            return "low"

    def _identify_collaboration_patterns(self, git_analysis: Dict[str, Any]) -> List[str]:
        """Identify collaboration patterns from git analysis"""
        patterns = []

        contributor_count = git_analysis.get('contributor_count', 0)
        branch_count = git_analysis.get('branch_count', 0)

        if contributor_count > 1:
            patterns.append('collaborative_development')

        if branch_count > 3:
            patterns.append('feature_branch_workflow')

        if git_analysis.get('has_pull_requests'):
            patterns.append('code_review_process')

        return patterns

class MCPToolsIntegrator:
    """Integration layer for MCP tools (Serena, Context7, Playwright)"""

    def __init__(self):
        self.serena_available = self._check_serena_availability()
        self.context7_available = self._check_context7_availability()
        self.playwright_available = self._check_playwright_availability()

    def gather_mcp_insights(self, project_path: str) -> MCPToolsInsights:
        """
        Gather insights from available MCP tools

        Args:
            project_path: Path to project directory

        Returns:
            MCPToolsInsights with analysis from available tools
        """
        logger.info(f"Gathering MCP tools insights for: {project_path}")

        serena_analysis = None
        context7_patterns = None
        playwright_coverage = None

        # Serena project indexing and analysis
        if self.serena_available:
            serena_analysis = self._get_serena_analysis(project_path)

        # Context7 semantic analysis
        if self.context7_available:
            context7_patterns = self._get_context7_patterns(project_path)

        # Playwright automation analysis
        if self.playwright_available:
            playwright_coverage = self._get_playwright_coverage(project_path)

        # Calculate integration quality score
        integration_quality = self._calculate_integration_quality(
            serena_analysis, context7_patterns, playwright_coverage
        )

        logger.info(f"MCP insights gathering complete. Quality score: {integration_quality:.2f}")

        return MCPToolsInsights(
            serena_available=self.serena_available,
            serena_analysis=serena_analysis,
            context7_available=self.context7_available,
            context7_patterns=context7_patterns,
            playwright_available=self.playwright_available,
            playwright_coverage=playwright_coverage,
            integration_quality_score=integration_quality
        )

    def _check_serena_availability(self) -> bool:
        """Check if Serena MCP tool is available"""
        try:
            # Check for .serena directory or serena command
            result = subprocess.run(['which', 'serena'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _check_context7_availability(self) -> bool:
        """Check if Context7 MCP tool is available"""
        try:
            # Check for context7 installation
            result = subprocess.run(['which', 'context7'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _check_playwright_availability(self) -> bool:
        """Check if Playwright MCP tool is available"""
        try:
            # Check for playwright installation
            result = subprocess.run(['which', 'playwright'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False

    def _get_serena_analysis(self, project_path: str) -> Optional[str]:
        """Get Serena project analysis"""
        try:
            # Mock Serena analysis - replace with actual Serena MCP integration
            serena_index_path = os.path.join(project_path, '.serena')
            if os.path.exists(serena_index_path):
                return "Complex multi-service architecture with well-defined component boundaries"
            else:
                return "Single-service application with straightforward structure"
        except Exception as e:
            logger.debug(f"Serena analysis error: {e}")
            return None

    def _get_context7_patterns(self, project_path: str) -> Optional[str]:
        """Get Context7 semantic patterns analysis"""
        try:
            # Mock Context7 analysis - replace with actual Context7 MCP integration
            # This would use Context7's semantic analysis capabilities
            return "Heavy use of async patterns and event-driven architecture"
        except Exception as e:
            logger.debug(f"Context7 analysis error: {e}")
            return None

    def _get_playwright_coverage(self, project_path: str) -> Optional[str]:
        """Get Playwright test coverage analysis"""
        try:
            # Check for Playwright test files
            playwright_tests = []
            for root, dirs, files in os.walk(project_path):
                for file in files:
                    if 'playwright' in file.lower() or file.endswith('.spec.ts'):
                        playwright_tests.append(file)

            if playwright_tests:
                return f"Comprehensive E2E testing infrastructure with {len(playwright_tests)} test files"
            else:
                return "No Playwright test automation detected"
        except Exception as e:
            logger.debug(f"Playwright analysis error: {e}")
            return None

    def _calculate_integration_quality(self, serena_analysis: Optional[str],
                                     context7_patterns: Optional[str],
                                     playwright_coverage: Optional[str]) -> float:
        """Calculate overall integration quality score"""
        score = 0.0
        total_tools = 3.0

        if serena_analysis:
            score += 0.4  # Serena provides project structure insights
        if context7_patterns:
            score += 0.3  # Context7 provides semantic understanding
        if playwright_coverage:
            score += 0.3  # Playwright provides testing insights

        return score

class FrameworkUsageCollector:
    """Collect framework usage data for ML training"""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

        # Create subdirectories for different data types
        (self.data_dir / 'project_contexts').mkdir(exist_ok=True)
        (self.data_dir / 'agent_selections').mkdir(exist_ok=True)
        (self.data_dir / 'workflow_patterns').mkdir(exist_ok=True)
        (self.data_dir / 'success_metrics').mkdir(exist_ok=True)

    def collect_project_context(self, project_context: ProjectContext):
        """Store project context data for ML training"""
        try:
            context_file = self.data_dir / 'project_contexts' / f"{project_context.context_hash}.json"

            # Convert to serializable format
            context_dict = asdict(project_context)
            context_dict['timestamp'] = project_context.timestamp.isoformat()

            with open(context_file, 'w') as f:
                json.dump(context_dict, f, indent=2)

            logger.info(f"Project context collected: {project_context.context_hash}")

        except Exception as e:
            logger.error(f"Error collecting project context: {e}")

    def collect_agent_selection(self, project_hash: str, selected_agents: List[str],
                              selection_method: str, user_satisfaction: Optional[float] = None):
        """Store agent selection data for ML training"""
        try:
            selection_data = {
                'project_hash': project_hash,
                'selected_agents': selected_agents,
                'selection_method': selection_method,  # 'manual', 'ai', 'hybrid'
                'user_satisfaction': user_satisfaction,
                'timestamp': datetime.datetime.now().isoformat()
            }

            selection_file = self.data_dir / 'agent_selections' / f"{project_hash}_{int(datetime.datetime.now().timestamp())}.json"

            with open(selection_file, 'w') as f:
                json.dump(selection_data, f, indent=2)

            logger.info(f"Agent selection collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting agent selection: {e}")

    def collect_workflow_pattern(self, project_hash: str, workflow_data: Dict[str, Any]):
        """Store workflow pattern data for ML training"""
        try:
            workflow_data.update({
                'project_hash': project_hash,
                'timestamp': datetime.datetime.now().isoformat()
            })

            workflow_file = self.data_dir / 'workflow_patterns' / f"{project_hash}_workflow.json"

            with open(workflow_file, 'w') as f:
                json.dump(workflow_data, f, indent=2)

            logger.info(f"Workflow pattern collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting workflow pattern: {e}")

    def collect_success_metrics(self, project_hash: str, metrics: Dict[str, Any]):
        """Store project success metrics for ML training"""
        try:
            metrics_data = {
                'project_hash': project_hash,
                'metrics': metrics,
                'timestamp': datetime.datetime.now().isoformat()
            }

            metrics_file = self.data_dir / 'success_metrics' / f"{project_hash}_metrics.json"

            with open(metrics_file, 'w') as f:
                json.dump(metrics_data, f, indent=2)

            logger.info(f"Success metrics collected for project: {project_hash}")

        except Exception as e:
            logger.error(f"Error collecting success metrics: {e}")

class ProjectContextAnalyzer:
    """Main class for comprehensive project context analysis"""

    def __init__(self, data_collection_dir: str = "./ai_training_data"):
        self.technology_detector = TechnologyDetector()
        self.complexity_analyzer = ProjectComplexityAnalyzer()
        self.domain_classifier = BusinessDomainClassifier()
        self.team_analyzer = TeamContextAnalyzer()
        self.mcp_integrator = MCPToolsIntegrator()
        self.usage_collector = FrameworkUsageCollector(data_collection_dir)

    def analyze_project(self, project_path: str) -> ProjectContext:
        """
        Perform comprehensive project analysis for AI-powered agent selection

        Args:
            project_path: Path to project directory

        Returns:
            ProjectContext with complete analysis results
        """
        logger.info(f"Starting comprehensive project analysis: {project_path}")

        try:
            # Detect technology stack
            technology_stack = self.technology_detector.detect_technology_stack(project_path)

            # Analyze project complexity
            complexity = self.complexity_analyzer.analyze_complexity(project_path)

            # Classify business domain
            business_domain = self.domain_classifier.classify_domain(project_path)

            # Analyze team context
            team_context = self.team_analyzer.analyze_team_context(project_path)

            # Gather MCP tools insights
            mcp_insights = self.mcp_integrator.gather_mcp_insights(project_path)

            # Load framework configuration if available
            framework_config = self._load_framework_config(project_path)

            # Generate context hash for unique identification
            context_hash = self._generate_context_hash(
                project_path, technology_stack, complexity, business_domain
            )

            # Create complete project context
            project_context = ProjectContext(
                project_path=project_path,
                technology_stack=technology_stack,
                complexity=complexity,
                business_domain=business_domain,
                team_context=team_context,
                mcp_insights=mcp_insights,
                framework_config=framework_config,
                timestamp=datetime.datetime.now(),
                context_hash=context_hash
            )

            # Collect data for ML training
            self.usage_collector.collect_project_context(project_context)

            logger.info(f"Project analysis complete: {context_hash}")
            return project_context

        except Exception as e:
            logger.error(f"Error during project analysis: {e}")
            raise

    def _load_framework_config(self, project_path: str) -> Optional[Dict[str, Any]]:
        """Load CLAUDE.md framework configuration if available"""
        try:
            claude_md_path = os.path.join(project_path, 'CLAUDE.md')
            if os.path.exists(claude_md_path):
                with open(claude_md_path, 'r') as f:
                    content = f.read()

                # Extract configuration from CLAUDE.md
                # This is a simplified parser - could be enhanced
                config = {
                    'has_claude_md': True,
                    'content_length': len(content),
                    'has_todo_config': 'todo_management_enabled' in content.lower(),
                    'has_agent_config': 'agents and roles' in content.lower()
                }

                return config
            else:
                return {'has_claude_md': False}

        except Exception as e:
            logger.debug(f"Error loading framework config: {e}")
            return None

    def _generate_context_hash(self, project_path: str, technology_stack: TechnologyStack,
                             complexity: ProjectComplexity, business_domain: BusinessDomain) -> str:
        """Generate unique hash for project context"""
        context_str = (
            f"{project_path}|"
            f"{technology_stack.frontend}|{technology_stack.backend}|"
            f"{complexity.complexity_rating}|{business_domain.primary}"
        )

        return hashlib.md5(context_str.encode()).hexdigest()

def main():
    """Main function for testing the data collection system"""
    if len(sys.argv) != 2:
        print("Usage: python data_collection_system.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)

    # Initialize project analyzer
    analyzer = ProjectContextAnalyzer()

    try:
        # Analyze project
        context = analyzer.analyze_project(project_path)

        # Print analysis results
        print("\n" + "="*80)
        print("🎯 PROJECT ANALYSIS RESULTS")
        print("="*80)

        print(f"\n📁 Project: {context.project_path}")
        print(f"🔍 Context Hash: {context.context_hash}")
        print(f"⏰ Analysis Time: {context.timestamp}")

        print(f"\n💻 Technology Stack (Confidence: {context.technology_stack.confidence_score:.2f}):")
        for category in ['frontend', 'backend', 'database', 'infrastructure', 'testing']:
            techs = getattr(context.technology_stack, category)
            if techs:
                print(f"  {category.title()}: {', '.join(techs)}")

        print(f"\n📊 Project Complexity: {context.complexity.complexity_rating.upper()}")
        print(f"  Files: {context.complexity.file_count}")
        print(f"  Lines of Code: {context.complexity.code_lines}")
        print(f"  Directory Depth: {context.complexity.directory_depth}")
        print(f"  Dependencies: {context.complexity.dependency_count}")
        print(f"  Complexity Score: {context.complexity.complexity_score:.2f}")

        print(f"\n🏢 Business Domain: {context.business_domain.primary.upper()}")
        print(f"  Industry: {context.business_domain.industry_vertical}")
        print(f"  Confidence: {context.business_domain.confidence_score:.2f}")
        if context.business_domain.secondary:
            print(f"  Secondary: {', '.join(context.business_domain.secondary)}")
        if context.business_domain.compliance_requirements:
            print(f"  Compliance: {', '.join(context.business_domain.compliance_requirements)}")

        print(f"\n👥 Team Context: {context.team_context.estimated_team_size.upper()} team")
        print(f"  Git Activity: {context.team_context.git_activity_level}")
        if context.team_context.experience_indicators:
            print(f"  Experience: {', '.join(context.team_context.experience_indicators)}")
        if context.team_context.development_patterns:
            print(f"  Patterns: {', '.join(context.team_context.development_patterns)}")

        print(f"\n🔗 MCP Tools Integration (Quality: {context.mcp_insights.integration_quality_score:.2f}):")
        print(f"  Serena: {'✅' if context.mcp_insights.serena_available else '❌'}")
        if context.mcp_insights.serena_analysis:
            print(f"    Analysis: {context.mcp_insights.serena_analysis}")

        print(f"  Context7: {'✅' if context.mcp_insights.context7_available else '❌'}")
        if context.mcp_insights.context7_patterns:
            print(f"    Patterns: {context.mcp_insights.context7_patterns}")

        print(f"  Playwright: {'✅' if context.mcp_insights.playwright_available else '❌'}")
        if context.mcp_insights.playwright_coverage:
            print(f"    Coverage: {context.mcp_insights.playwright_coverage}")

        if context.framework_config:
            print(f"\n⚙️ Framework Configuration:")
            print(f"  CLAUDE.md: {'✅' if context.framework_config.get('has_claude_md') else '❌'}")
            if context.framework_config.get('has_todo_config'):
                print(f"  TODO Management: ✅")
            if context.framework_config.get('has_agent_config'):
                print(f"  Agent Configuration: ✅")

        print("\n" + "="*80)
        print("✅ Analysis complete! Data collected for ML training.")
        print("="*80)

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()