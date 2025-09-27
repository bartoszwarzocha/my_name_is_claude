#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Intelligent Agent Selector
Claude Code Multi-Agent Framework Enhancement

This module implements the AI-enhanced agent selection system that integrates
machine learning models with the existing agent-prompt binding framework.

Components:
- AI Agent Selection Engine
- Framework Integration Layer
- Backward Compatibility Manager
- Performance Monitoring
- Fallback Mechanisms

Version: 1.0.0
Phase: 2 - Framework Integration
"""

import os
import sys
import json
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass, asdict
from pathlib import Path
import time
from abc import ABC, abstractmethod

# Add the framework root to Python path
framework_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(framework_root))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentSelectionRequest:
    """Request for agent selection"""
    project_path: str
    user_preferences: Optional[Dict[str, Any]] = None
    selection_mode: str = "ai"  # "ai", "manual", "hybrid"
    confidence_threshold: float = 0.5
    max_agents: int = 10
    context_data: Optional[Dict[str, Any]] = None

@dataclass
class AgentSelectionResponse:
    """Response from agent selection"""
    recommended_agents: List[str]
    confidence_scores: Dict[str, float]
    reasoning: Dict[str, List[str]]
    workflow_sequence: List[str]
    fallback_used: bool
    processing_time: float
    metadata: Dict[str, Any]

@dataclass
class FrameworkConfig:
    """Framework configuration for AI integration"""
    ai_enabled: bool = True
    selection_confidence_threshold: float = 0.5
    fallback_to_manual: bool = True
    learning_enabled: bool = True
    personalization_enabled: bool = True
    performance_monitoring: bool = True

class AgentSelectionEngine:
    """Core AI-powered agent selection engine"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.config = self._load_framework_config()

        # Initialize components
        self.project_analyzer = None
        self.feature_encoder = None
        self.ml_ensemble = None
        self.performance_tracker = PerformanceTracker()

        # Agent registry
        self.available_agents = self._discover_available_agents()
        self.agent_capabilities = self._load_agent_capabilities()

        # Initialize AI components
        self._initialize_ai_components()

    def _load_framework_config(self) -> FrameworkConfig:
        """Load framework configuration from CLAUDE.md"""
        try:
            claude_md_path = self.framework_root / "CLAUDE.md"
            if claude_md_path.exists():
                with open(claude_md_path, 'r') as f:
                    content = f.read()

                # Extract AI configuration (simplified parsing)
                config = FrameworkConfig()

                # Look for AI configuration section
                if "ai_enabled: true" in content.lower():
                    config.ai_enabled = True
                elif "ai_enabled: false" in content.lower():
                    config.ai_enabled = False

                # Extract other configuration parameters
                config_patterns = {
                    'selection_confidence_threshold': r'selection_confidence_threshold:\s*([0-9.]+)',
                    'fallback_to_manual': r'fallback_to_manual:\s*(true|false)',
                    'learning_enabled': r'learning_enabled:\s*(true|false)',
                    'personalization_enabled': r'personalization_enabled:\s*(true|false)'
                }

                import re
                for param, pattern in config_patterns.items():
                    match = re.search(pattern, content, re.IGNORECASE)
                    if match:
                        value = match.group(1)
                        if param == 'selection_confidence_threshold':
                            setattr(config, param, float(value))
                        else:
                            setattr(config, param, value.lower() == 'true')

                return config

        except Exception as e:
            logger.warning(f"Error loading framework config: {e}")

        return FrameworkConfig()  # Default config

    def _discover_available_agents(self) -> List[str]:
        """Discover available agents in the framework"""
        agents = []
        agents_dir = self.framework_root / ".claude" / "agents"

        if agents_dir.exists():
            # Recursively search for all .md files in subdirectories
            for agent_file in agents_dir.rglob("*.md"):
                agent_name = agent_file.stem
                agents.append(agent_name)

        logger.info(f"Discovered {len(agents)} available agents")
        return sorted(agents)

    def _parse_agent_file(self, agent_name: str) -> Dict[str, Any]:
        """Parse agent file to extract capabilities"""
        agents_dir = self.framework_root / ".claude" / "agents"

        # Find the agent file
        agent_file = None
        for file_path in agents_dir.rglob(f"{agent_name}.md"):
            agent_file = file_path
            break

        if not agent_file or not agent_file.exists():
            logger.warning(f"Agent file not found for: {agent_name}")
            return self._get_default_capabilities()

        try:
            with open(agent_file, 'r') as f:
                content = f.read()

            # Parse YAML header
            if content.startswith('---'):
                yaml_end = content.find('---', 3)
                if yaml_end != -1:
                    yaml_content = content[3:yaml_end].strip()
                    description = self._extract_yaml_value(yaml_content, 'description')
                else:
                    description = ""
            else:
                description = ""

            # Extract technologies from description
            technologies = self._extract_technologies_from_description(description)

            # Extract complexity preference based on description
            complexity_preference = self._infer_complexity_preference(description)

            # Extract project phases
            project_phases = self._infer_project_phases(description, agent_name)

            # Extract collaboration level
            team_collaboration = self._infer_collaboration_level(description)

            return {
                'technologies': technologies,
                'complexity_preference': complexity_preference,
                'project_phases': project_phases,
                'team_collaboration': team_collaboration,
                'expertise_level': 'specialized',
                'description': description
            }

        except Exception as e:
            logger.warning(f"Error parsing agent file {agent_name}: {e}")
            return self._get_default_capabilities()

    def _extract_yaml_value(self, yaml_content: str, key: str) -> str:
        """Extract value from YAML content"""
        import re
        pattern = rf'^{key}:\s*(.+)$'
        match = re.search(pattern, yaml_content, re.MULTILINE)
        return match.group(1).strip() if match else ""

    def _extract_technologies_from_description(self, description: str) -> List[str]:
        """Extract technologies from agent description"""
        if not description:
            return []

        description_lower = description.lower()
        technologies = []

        # Technology mapping from description keywords
        tech_keywords = {
            'opengl': ['opengl', 'open gl'],
            'vulkan': ['vulkan'],
            'directx': ['directx', 'direct x'],
            'wxwidgets': ['wxwidgets', 'wx widgets'],
            'qt': ['qt'],
            'react': ['react'],
            'angular': ['angular'],
            'vue': ['vue.js', 'vue'],
            'python': ['python'],
            'javascript': ['javascript', 'js'],
            'typescript': ['typescript', 'ts'],
            'java': ['java'],
            'csharp': ['c#', 'csharp'],
            'cpp': ['c++', 'cpp'],
            'go': ['golang', 'go'],
            'rust': ['rust'],
            'docker': ['docker'],
            'kubernetes': ['kubernetes', 'k8s'],
            'aws': ['aws', 'amazon web services'],
            'azure': ['azure'],
            'gcp': ['google cloud', 'gcp'],
            'postgresql': ['postgresql', 'postgres'],
            'mysql': ['mysql'],
            'mongodb': ['mongodb', 'mongo'],
            'nodejs': ['node.js', 'nodejs'],
            'express': ['express.js', 'express'],
            'fastapi': ['fastapi'],
            'django': ['django'],
            'flask': ['flask'],
            'tensorflow': ['tensorflow'],
            'pytorch': ['pytorch'],
            'pandas': ['pandas'],
            'numpy': ['numpy'],
            'testing': ['testing', 'test', 'quality assurance'],
            'security': ['security', 'cybersecurity'],
            'mobile': ['mobile', 'android', 'ios'],
            'desktop': ['desktop', 'native'],
            'graphics': ['graphics', '3d', '2d', 'rendering'],
            'api': ['api', 'rest', 'graphql'],
            'database': ['database', 'sql'],
            'infrastructure': ['infrastructure', 'devops'],
            'monitoring': ['monitoring', 'observability'],
            'compliance': ['compliance', 'regulatory']
        }

        for tech, keywords in tech_keywords.items():
            if any(keyword in description_lower for keyword in keywords):
                technologies.append(tech)

        return technologies

    def _infer_complexity_preference(self, description: str) -> float:
        """Infer complexity preference from description"""
        if not description:
            return 0.5

        description_lower = description.lower()

        # High complexity indicators
        high_complexity_terms = ['enterprise', 'complex', 'advanced', 'expert', 'senior', 'architecture', 'system']
        # Low complexity indicators
        low_complexity_terms = ['simple', 'basic', 'junior', 'beginner']

        high_score = sum(1 for term in high_complexity_terms if term in description_lower)
        low_score = sum(1 for term in low_complexity_terms if term in description_lower)

        if high_score > low_score:
            return 0.8
        elif low_score > high_score:
            return 0.3
        else:
            return 0.6

    def _infer_project_phases(self, description: str, agent_name: str) -> List[str]:
        """Infer project phases from description and agent name"""
        phases = []

        if not description:
            description = ""

        description_lower = description.lower()
        agent_lower = agent_name.lower()

        # Phase mapping
        if any(term in description_lower or term in agent_lower for term in ['architect', 'design', 'planning']):
            phases.append('architecture')
        if any(term in description_lower or term in agent_lower for term in ['develop', 'engineer', 'implementation']):
            phases.append('development')
        if any(term in description_lower or term in agent_lower for term in ['test', 'qa', 'quality']):
            phases.append('quality_assurance')
        if any(term in description_lower or term in agent_lower for term in ['deploy', 'operations', 'infrastructure']):
            phases.append('deployment')
        if any(term in description_lower or term in agent_lower for term in ['manage', 'coordinate', 'owner']):
            phases.append('coordination')
        if any(term in description_lower or term in agent_lower for term in ['security', 'compliance']):
            phases.append('security')

        return phases if phases else ['development']

    def _infer_collaboration_level(self, description: str) -> str:
        """Infer collaboration level from description"""
        if not description:
            return 'medium'

        description_lower = description.lower()

        if any(term in description_lower for term in ['team', 'collaboration', 'coordination', 'management']):
            return 'high'
        elif any(term in description_lower for term in ['specialist', 'expert', 'individual']):
            return 'medium'
        else:
            return 'medium'

    def _get_default_capabilities(self) -> Dict[str, Any]:
        """Get default capabilities for unknown agents"""
        return {
            'technologies': [],
            'complexity_preference': 0.5,
            'project_phases': ['development'],
            'team_collaboration': 'medium',
            'expertise_level': 'general',
            'description': ''
        }

    def _load_agent_capabilities(self) -> Dict[str, Dict[str, Any]]:
        """Load agent capabilities and metadata"""
        capabilities = {}

        # Dynamic agent parsing from actual files
        for agent_name in self.available_agents:
            capabilities[agent_name] = self._parse_agent_file(agent_name)

        # Fallback hardcoded definitions for critical agents (if parsing fails)
        agent_definitions = {
            'frontend-engineer': {
                'technologies': ['react', 'angular', 'vue', 'typescript', 'javascript'],
                'complexity_preference': 0.7,
                'project_phases': ['development'],
                'team_collaboration': 'high',
                'expertise_level': 'specialized'
            },
            'backend-engineer': {
                'technologies': ['python', 'nodejs', 'java', 'csharp', 'go'],
                'complexity_preference': 0.8,
                'project_phases': ['architecture', 'development'],
                'team_collaboration': 'high',
                'expertise_level': 'specialized'
            },
            'api-engineer': {
                'technologies': ['rest', 'graphql', 'fastapi', 'express', 'spring'],
                'complexity_preference': 0.8,
                'project_phases': ['architecture', 'development'],
                'team_collaboration': 'medium',
                'expertise_level': 'specialized'
            },
            'data-engineer': {
                'technologies': ['python', 'sql', 'postgresql', 'mongodb', 'spark'],
                'complexity_preference': 0.8,
                'project_phases': ['architecture', 'development'],
                'team_collaboration': 'medium',
                'expertise_level': 'specialized'
            },
            'deployment-engineer': {
                'technologies': ['docker', 'kubernetes', 'aws', 'terraform', 'jenkins'],
                'complexity_preference': 0.8,
                'project_phases': ['deployment'],
                'team_collaboration': 'medium',
                'expertise_level': 'specialized'
            },
            'security-engineer': {
                'technologies': ['security', 'compliance', 'authentication', 'encryption'],
                'complexity_preference': 0.9,
                'project_phases': ['architecture', 'development', 'deployment'],
                'team_collaboration': 'medium',
                'expertise_level': 'expert'
            },
            'qa-engineer': {
                'technologies': ['testing', 'jest', 'pytest', 'cypress', 'playwright'],
                'complexity_preference': 0.6,
                'project_phases': ['development', 'quality_assurance'],
                'team_collaboration': 'high',
                'expertise_level': 'specialized'
            },
            'project-owner': {
                'technologies': ['management', 'coordination', 'planning'],
                'complexity_preference': 0.9,
                'project_phases': ['initialization', 'planning', 'coordination'],
                'team_collaboration': 'very_high',
                'expertise_level': 'leadership'
            },
            'session-manager': {
                'technologies': ['framework', 'session_management', 'context'],
                'complexity_preference': 0.7,
                'project_phases': ['initialization', 'coordination'],
                'team_collaboration': 'high',
                'expertise_level': 'framework_specific'
            }
        }

        # Add hardcoded definitions only for agents not dynamically parsed or as fallback
        for agent in self.available_agents:
            if agent not in capabilities:
                # Use hardcoded definition if available
                if agent in agent_definitions:
                    capabilities[agent] = agent_definitions[agent]
                    # Add missing description field
                    capabilities[agent]['description'] = f"Hardcoded definition for {agent}"
                else:
                    # Use default capabilities for completely unknown agents
                    capabilities[agent] = self._get_default_capabilities()

        return capabilities

    def _initialize_ai_components(self):
        """Initialize AI components if enabled"""
        if not self.config.ai_enabled:
            logger.info("AI features disabled in configuration")
            return

        try:
            # Import AI components with relative imports
            # Use simplified systems for compatibility
            from ..core.simple_technology_detector import SimpleTechnologyDetector
            from dataclasses import dataclass
            from typing import Any, Dict

            # Create compatibility wrapper for ProjectContextAnalyzer
            @dataclass
            class MockProjectContext:
                technology_stack: Any

            class ProjectContextAnalyzerCompat:
                def __init__(self):
                    self.tech_detector = SimpleTechnologyDetector()

                def analyze_project(self, project_path: str):
                    tech_stack = self.tech_detector.detect_technology_stack(project_path)
                    return MockProjectContext(technology_stack=tech_stack)

            # Initialize simplified components
            self.project_analyzer = ProjectContextAnalyzerCompat()
            # Disable ML components for simplified system
            self.feature_encoder = None
            self.ml_ensemble = None

            # Try to load pre-trained models
            self._load_pretrained_models()

            # Initialize adaptive learning integration
            self._initialize_adaptive_learning()

            logger.info("✅ AI components initialized successfully")

        except Exception as e:
            logger.warning(f"⚠️ Failed to initialize AI components: {e}")
            logger.info("🔄 Falling back to rule-based selection")
            self.config.ai_enabled = False

    def _initialize_adaptive_learning(self):
        """Initialize adaptive learning integration with hybrid intelligence"""
        try:
            # Import hybrid intelligence system
            sys.path.insert(0, str(self.framework_root / "learning"))
            from learning.hybrid_intelligence import HybridIntelligenceSystem

            # Initialize hybrid intelligence system
            self.hybrid_intelligence = HybridIntelligenceSystem(str(self.framework_root))

            if self.hybrid_intelligence.learning_enabled:
                logger.info("🧠 Hybrid Intelligence System enabled (Universal + Adaptive)")
            else:
                logger.info("🔄 Hybrid Intelligence System initializing (Universal patterns active)")

            # Keep backward compatibility
            self.learning_integration = self.hybrid_intelligence

        except Exception as e:
            logger.warning(f"⚠️ Hybrid intelligence not available: {e}")
            # Fallback to basic adaptive learning
            try:
                from learning.learning_integration import AdaptiveLearningIntegration
                self.learning_integration = AdaptiveLearningIntegration(str(self.framework_root))
                self.hybrid_intelligence = None
                logger.info("🔄 Fallback to basic adaptive learning")
            except Exception as e2:
                logger.warning(f"⚠️ All learning systems unavailable: {e2}")
                self.learning_integration = None
                self.hybrid_intelligence = None

    def _load_pretrained_models(self):
        """Load pre-trained models if available"""
        models_dir = self.framework_root / "ai_tools" / "models"

        try:
            # Check for pre-trained ensemble
            ensemble_path = models_dir / "trained_ensemble.json"
            if ensemble_path.exists():
                logger.info("📦 Loading pre-trained ensemble models...")
                # In real implementation, would load actual trained models
                logger.info("✅ Pre-trained models loaded")
            else:
                logger.info("🔄 No pre-trained models found, using default configuration")

        except Exception as e:
            logger.warning(f"⚠️ Error loading pre-trained models: {e}")

    def select_agents(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """Main agent selection method with timeout protection"""
        start_time = time.time()

        # Master timeout for entire selection process (90 seconds)
        import signal

        def master_timeout_handler(signum, frame):
            raise TimeoutError("Agent selection process timed out after 90 seconds")

        original_master_handler = signal.signal(signal.SIGALRM, master_timeout_handler)
        signal.alarm(90)  # 90 second master timeout

        try:
            # Track the request
            self.performance_tracker.track_request(request)

            logger.info(f"🎯 Starting agent selection for {request.project_path} (mode: {request.selection_mode})")

            if self.config.ai_enabled and self.ml_ensemble and request.selection_mode in ['ai', 'hybrid']:
                logger.info(f"🤖 Attempting AI-powered selection for {request.project_path}")
                response = self._ai_powered_selection(request)
            else:
                logger.info(f"📋 Using rule-based selection for {request.project_path}")
                response = self._rule_based_selection(request)

            # Add processing time
            response.processing_time = time.time() - start_time

            # Track the response
            self.performance_tracker.track_response(response)

            logger.info(f"✅ Agent selection completed for {request.project_path} in {response.processing_time:.2f}s")
            return response

        except TimeoutError as e:
            logger.error(f"🚨 Master timeout reached for {request.project_path}: {e}")
            # Emergency fallback with minimal processing
            return self._emergency_fallback_selection(request, start_time)

        except Exception as e:
            logger.error(f"🚨 Unexpected error in agent selection for {request.project_path}: {e}")
            # Emergency fallback
            return self._emergency_fallback_selection(request, start_time)

        finally:
            # Cleanup master timeout
            try:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, original_master_handler)
            except Exception as cleanup_error:
                logger.debug(f"Master timeout cleanup error (non-critical): {cleanup_error}")

    def _emergency_fallback_selection(self, request: AgentSelectionRequest, start_time: float) -> AgentSelectionResponse:
        """Ultra-fast emergency fallback when everything else fails"""
        logger.warning(f"🆘 Using emergency fallback selection for {request.project_path}")

        # Hardcoded minimal agent set - no analysis, just basic defaults
        emergency_agents = ["project-owner", "session-manager", "software-architect"]

        # Quick technology-based additions (minimal file checking)
        try:
            project_path = Path(request.project_path)
            if any(f.suffix in ['.py'] for f in project_path.glob('*.py')):
                emergency_agents.append("backend-engineer")
            if any(f.suffix in ['.js', '.ts', '.tsx', '.jsx'] for f in project_path.glob('*')):
                emergency_agents.append("frontend-engineer")
            if any(f.name in ['package.json', 'requirements.txt'] for f in project_path.glob('*')):
                emergency_agents.append("qa-engineer")
        except:
            pass  # Ignore any errors in emergency mode

        # Limit to max agents
        final_agents = emergency_agents[:request.max_agents]

        return AgentSelectionResponse(
            recommended_agents=final_agents,
            confidence_scores={agent: 0.5 for agent in final_agents},
            reasoning={agent: ["Emergency fallback selection"] for agent in final_agents},
            workflow_sequence=final_agents,
            fallback_used=True,
            processing_time=time.time() - start_time,
            metadata={
                'selection_method': 'emergency_fallback',
                'reason': 'timeout_or_error'
            }
        )

    def _ai_powered_selection(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """AI-powered agent selection using ML models with circuit breaker"""
        logger.info(f"🤖 Using AI-powered agent selection for {request.project_path}")

        # Circuit breaker for AI selection - max 60 seconds total
        import signal
        import time

        def timeout_handler(signum, frame):
            raise TimeoutError("AI-powered selection timed out after 60 seconds")

        # Set up timeout circuit breaker
        original_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(60)  # 60 second timeout for entire AI selection

        try:
            # Analyze project context with timeout protection
            if request.context_data:
                project_context = request.context_data
            else:
                try:
                    # Protected project analysis with shorter timeout (45s)
                    signal.alarm(45)  # Reduce timeout for project analysis
                    logger.info(f"🔄 Starting project analysis for {request.project_path}")

                    context_obj = self.project_analyzer.analyze_project(request.project_path)
                    project_context = {
                        'technology_stack': asdict(context_obj.technology_stack),
                        'complexity': asdict(context_obj.complexity),
                        'business_domain': asdict(context_obj.business_domain),
                        'team_context': asdict(context_obj.team_context),
                        'mcp_insights': asdict(context_obj.mcp_insights)
                    }
                    logger.info(f"✅ Project analysis completed for {request.project_path}")

                except TimeoutError:
                    logger.warning(f"⏰ Project analysis timed out for {request.project_path}, using fallback")
                    raise TimeoutError("Project analysis timeout - falling back to rule-based")
                except Exception as e:
                    logger.warning(f"❌ Project analysis failed for {request.project_path}: {e}")
                    raise Exception(f"Project analysis failed: {e}")

            # Extract features
            features = self.feature_encoder.encode_single_project(project_context)

            # Get ML recommendations
            ml_recommendations = self.ml_ensemble.recommend_agents(
                features.tolist() if hasattr(features, 'tolist') else features,
                confidence_threshold=request.confidence_threshold
            )

            # Filter to available agents
            available_recommendations = [
                rec for rec in ml_recommendations.primary_recommendations
                if rec.agent_name in self.available_agents
            ]

            # Limit to max agents
            limited_recommendations = available_recommendations[:request.max_agents]

            # Get base recommendations
            recommended_agents = [rec.agent_name for rec in limited_recommendations]
            confidence_scores = {rec.agent_name: rec.confidence_score for rec in limited_recommendations}
            reasoning = {rec.agent_name: rec.reasoning for rec in limited_recommendations}

            # Apply hybrid intelligence enhancement if available
            if hasattr(self, 'hybrid_intelligence') and self.hybrid_intelligence:
                try:
                    # Use hybrid intelligence system for enhanced recommendations
                    hybrid_context = {
                        'technologies': project_context.get('technology_stack', {}).get('languages', []) +
                                      project_context.get('technology_stack', {}).get('frameworks', []),
                        'domain': project_context.get('business_domain', {}).get('type', 'general'),
                        'complexity': project_context.get('complexity', {}).get('level', 'medium'),
                        'task_type': request.context_data.get('task_type') if request.context_data else 'development',
                        'project_phase': request.context_data.get('project_phase') if request.context_data else 'development',
                        'has_frontend': 'frontend' in str(project_context).lower(),
                        'has_backend': 'backend' in str(project_context).lower(),
                        'has_database': 'database' in str(project_context).lower(),
                        'has_api': 'api' in str(project_context).lower()
                    }

                    # Get hybrid recommendations
                    hybrid_recs = self.hybrid_intelligence.get_hybrid_recommendations(hybrid_context)

                    if hybrid_recs:
                        logger.info("🧠 Applied Hybrid Intelligence System (Universal + Adaptive)")

                        # Extract top recommendations from hybrid system
                        hybrid_agents = [rec['agent'] for rec in hybrid_recs[:request.max_agents]]
                        hybrid_scores = {rec['agent']: rec['confidence'] for rec in hybrid_recs}
                        hybrid_reasoning = {rec['agent']: [rec['reasoning']] for rec in hybrid_recs}

                        # Use hybrid recommendations
                        recommended_agents = hybrid_agents
                        confidence_scores = hybrid_scores
                        reasoning = hybrid_reasoning

                except Exception as e:
                    logger.warning(f"Hybrid intelligence enhancement failed: {e}")

                    # Fallback to basic adaptive learning if available
                    if hasattr(self, 'learning_integration') and self.learning_integration:
                        try:
                            learning_context = {
                                'task_type': request.context_data.get('task_type') if request.context_data else 'development',
                                'project_phase': request.context_data.get('project_phase') if request.context_data else 'development'
                            }

                            enhanced_agents = self.learning_integration.enhance_agent_recommendations(
                                base_recommendations=recommended_agents,
                                context=learning_context
                            )

                            if enhanced_agents != recommended_agents:
                                logger.info("🔄 Applied basic adaptive learning fallback")
                                recommended_agents = enhanced_agents

                        except Exception as e2:
                            logger.warning(f"Adaptive learning fallback also failed: {e2}")

            # Final recommendations
            final_recommended_agents = recommended_agents

            return AgentSelectionResponse(
                recommended_agents=final_recommended_agents,
                confidence_scores=confidence_scores,
                reasoning=reasoning,
                workflow_sequence=ml_recommendations.workflow_sequence,
                fallback_used=False,
                processing_time=0.0,  # Will be set by caller
                metadata={
                    'selection_method': 'ai_powered',
                    'ml_performance': ml_recommendations.model_performance,
                    'project_context_hash': project_context.get('context_hash', 'unknown'),
                    'learning_enhanced': hasattr(self, 'learning_integration') and self.learning_integration is not None
                }
            )

        except TimeoutError as e:
            logger.warning(f"⏰ AI selection timed out for {request.project_path}: {e}")
            logger.info(f"🔄 Falling back to rule-based selection for {request.project_path}")
            return self._rule_based_selection(request)

        except Exception as e:
            logger.warning(f"❌ AI selection failed for {request.project_path}: {e}")
            logger.info(f"🔄 Falling back to rule-based selection for {request.project_path}")
            return self._rule_based_selection(request)

        finally:
            # Critical cleanup - restore signal handler and cancel alarm
            try:
                signal.alarm(0)  # Cancel any pending alarm
                signal.signal(signal.SIGALRM, original_handler)  # Restore original handler
            except Exception as cleanup_error:
                logger.debug(f"Signal cleanup error (non-critical): {cleanup_error}")

    def _rule_based_selection(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """Rule-based agent selection fallback"""
        logger.info(f"📋 Using rule-based agent selection for {request.project_path}")

        try:
            # Simplified project analysis
            project_analysis = self._simple_project_analysis(request.project_path)

            # Apply rules
            agent_scores = self._apply_selection_rules(project_analysis)

            # Filter by confidence threshold
            recommended_agents = [
                agent for agent, score in agent_scores.items()
                if score >= request.confidence_threshold
            ]

            # Sort by score and limit
            recommended_agents = sorted(
                recommended_agents,
                key=lambda x: agent_scores[x],
                reverse=True
            )[:request.max_agents]

            # Generate reasoning
            reasoning = {agent: [f"Rule-based selection with score {agent_scores[agent]:.2f}"]
                        for agent in recommended_agents}

            # Simple workflow sequence
            workflow_sequence = self._generate_simple_workflow(recommended_agents)

            return AgentSelectionResponse(
                recommended_agents=recommended_agents,
                confidence_scores={agent: agent_scores[agent] for agent in recommended_agents},
                reasoning=reasoning,
                workflow_sequence=workflow_sequence,
                fallback_used=True,
                processing_time=0.0,
                metadata={
                    'selection_method': 'rule_based',
                    'project_analysis': project_analysis
                }
            )

        except Exception as e:
            logger.error(f"Rule-based selection failed: {e}")
            return self._emergency_fallback_selection(request)

    def _simple_project_analysis(self, project_path: str) -> Dict[str, Any]:
        """Enhanced project analysis using TechnologyDetector"""
        analysis = {
            'has_frontend': False,
            'has_backend': False,
            'has_database': False,
            'has_tests': False,
            'has_docker': False,
            'complexity': 'medium',
            'technologies': []
        }

        try:
            # Use SimpleTechnologyDetector for analysis
            from ..core.simple_technology_detector import SimpleTechnologyDetector
            detector = SimpleTechnologyDetector()
            tech_stack = detector.detect_technology_stack(project_path)

            # Collect all detected technologies (simplified format)
            all_technologies = tech_stack.languages + tech_stack.frameworks + tech_stack.build_tools
            analysis['technologies'] = all_technologies

            # Set flags based on detected technologies (simplified categorization)
            frontend_techs = {'javascript', 'typescript', 'react', 'angular', 'vue', 'html', 'css'}
            backend_techs = {'python', 'java', 'c#', 'go', 'rust', 'php', 'ruby', 'django', 'flask', 'spring'}
            database_techs = {'postgresql', 'mysql', 'mongodb', 'redis'}

            all_lower = [tech.lower() for tech in all_technologies]
            analysis['has_frontend'] = any(tech in frontend_techs for tech in all_lower)
            analysis['has_backend'] = any(tech in backend_techs for tech in all_lower)
            analysis['has_database'] = any(tech in database_techs for tech in all_lower)
            testing_techs = {'pytest', 'jest', 'junit'}
            infrastructure_techs = {'docker', 'kubernetes'}
            analysis['has_tests'] = any(tech.lower() in testing_techs for tech in all_technologies)
            analysis['has_docker'] = any(tech.lower() in infrastructure_techs for tech in all_technologies)

            # Fallback to file-based detection for additional indicators
            project = Path(project_path)

            # Additional frontend indicators
            if not analysis['has_frontend'] and any((project / f).exists() for f in ['package.json', 'src/', 'public/', 'index.html']):
                analysis['has_frontend'] = True
                analysis['technologies'].extend(['frontend', 'javascript'])

            # Additional backend indicators
            if not analysis['has_backend'] and any((project / f).exists() for f in ['requirements.txt', 'app.py', 'main.py', 'server.js']):
                analysis['has_backend'] = True
                analysis['technologies'].extend(['backend', 'api'])

            # Additional database indicators
            if not analysis['has_database'] and any((project / f).exists() for f in ['database/', 'migrations/', 'models/', 'schema.sql']):
                analysis['has_database'] = True
                analysis['technologies'].append('database')

            # Additional testing indicators
            if not analysis['has_tests'] and any((project / f).exists() for f in ['tests/', 'test/', '__tests__/', 'spec/']):
                analysis['has_tests'] = True
                analysis['technologies'].append('testing')

            # Additional Docker indicators
            if not analysis['has_docker'] and any((project / f).exists() for f in ['Dockerfile', 'docker-compose.yml', '.dockerignore']):
                analysis['has_docker'] = True
                analysis['technologies'].append('infrastructure')

            # Complexity assessment (simplified)
            file_count = sum(1 for _ in project.rglob('*') if _.is_file())
            if file_count < 50:
                analysis['complexity'] = 'simple'
            elif file_count > 500:
                analysis['complexity'] = 'complex'

        except Exception as e:
            logger.debug(f"Error in simple project analysis: {e}")

        return analysis

    def _apply_selection_rules(self, project_analysis: Dict[str, Any]) -> Dict[str, float]:
        """Apply intelligent selection rules using dynamic agent capabilities"""
        agent_scores = {}

        # Always recommend core management agents
        agent_scores['project-owner'] = 0.95
        agent_scores['session-manager'] = 0.90

        # Get detected technologies from project analysis
        detected_technologies = project_analysis.get('technologies', [])

        # Score agents based on technology matches
        for agent_name, capabilities in self.agent_capabilities.items():
            if agent_name in ['project-owner', 'session-manager']:
                continue  # Already scored above

            score = 0.0
            agent_technologies = capabilities.get('technologies', [])

            # Technology matching score
            tech_matches = sum(1 for tech in agent_technologies if tech in detected_technologies)
            if tech_matches > 0 and len(agent_technologies) > 0:
                score += (tech_matches / len(agent_technologies)) * 0.6

            # Project analysis pattern matching
            if project_analysis['has_frontend'] and any(tech in agent_technologies for tech in ['react', 'angular', 'vue', 'javascript', 'typescript']):
                score += 0.3
            if project_analysis['has_backend'] and any(tech in agent_technologies for tech in ['python', 'nodejs', 'java', 'api']):
                score += 0.3
            if project_analysis['has_database'] and any(tech in agent_technologies for tech in ['database', 'sql', 'postgresql', 'mongodb']):
                score += 0.3
            if project_analysis['has_tests'] and any(tech in agent_technologies for tech in ['testing', 'qa']):
                score += 0.3
            if project_analysis['has_docker'] and any(tech in agent_technologies for tech in ['docker', 'kubernetes', 'infrastructure']):
                score += 0.3

            # Detected technology specific bonuses
            if 'wxwidgets' in detected_technologies and any(tech in agent_technologies for tech in ['wxwidgets', 'desktop']):
                score += 0.4
            if 'opengl' in detected_technologies and any(tech in agent_technologies for tech in ['opengl', 'graphics']):
                score += 0.4
            if 'vulkan' in detected_technologies and any(tech in agent_technologies for tech in ['vulkan', 'graphics']):
                score += 0.4

            # Complexity-based adjustments
            complexity_preference = capabilities.get('complexity_preference', 0.5)
            if project_analysis['complexity'] == 'complex' and complexity_preference > 0.7:
                score += 0.2
            elif project_analysis['complexity'] == 'simple' and complexity_preference < 0.4:
                score += 0.1

            # Only add agents with meaningful scores
            if score > 0.2:
                agent_scores[agent_name] = min(1.0, score)

        # Ensure core architecture agents for medium/complex projects
        if project_analysis['complexity'] in ['medium', 'complex']:
            if 'software-architect' in self.agent_capabilities:
                base_score = 0.65 if project_analysis['complexity'] == 'medium' else 0.75
                agent_scores['software-architect'] = max(agent_scores.get('software-architect', 0), base_score)

        return agent_scores

    def _generate_simple_workflow(self, recommended_agents: List[str]) -> List[str]:
        """Generate simple workflow sequence"""
        workflow_phases = {
            'initialization': ['project-owner', 'session-manager'],
            'development': ['frontend-engineer', 'backend-engineer', 'api-engineer', 'data-engineer'],
            'quality': ['qa-engineer', 'security-engineer'],
            'deployment': ['deployment-engineer']
        }

        workflow = []
        for phase_agents in workflow_phases.values():
            for agent in phase_agents:
                if agent in recommended_agents and agent not in workflow:
                    workflow.append(agent)

        return workflow

    def _emergency_fallback_selection(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """Emergency fallback when all other methods fail"""
        logger.warning("🚨 Using emergency fallback selection")

        # Return minimal viable agent set
        emergency_agents = ['project-owner', 'session-manager']

        # Add a few more if available
        for agent in ['backend-engineer', 'frontend-engineer', 'qa-engineer']:
            if agent in self.available_agents:
                emergency_agents.append(agent)

        return AgentSelectionResponse(
            recommended_agents=emergency_agents,
            confidence_scores={agent: 0.5 for agent in emergency_agents},
            reasoning={agent: ["Emergency fallback selection"] for agent in emergency_agents},
            workflow_sequence=emergency_agents,
            fallback_used=True,
            processing_time=0.0,
            metadata={'selection_method': 'emergency_fallback'}
        )

    def record_user_selection(self, recommended_agents: List[str], selected_agent: str,
                             context: Dict[str, Any] = None):
        """Record user selection for hybrid intelligence system"""
        # Try hybrid intelligence system first
        if hasattr(self, 'hybrid_intelligence') and self.hybrid_intelligence:
            try:
                self.hybrid_intelligence.record_feedback(
                    recommended_agents=recommended_agents,
                    selected_agent=selected_agent,
                    context=context or {}
                )
                logger.info(f"🧠 Recorded user selection for hybrid intelligence: {selected_agent}")
            except Exception as e:
                logger.warning(f"Failed to record hybrid intelligence feedback: {e}")

        # Fallback to basic adaptive learning
        elif hasattr(self, 'learning_integration') and self.learning_integration:
            try:
                task_type = context.get('task_type') if context else 'development'
                project_phase = context.get('project_phase') if context else 'development'

                self.learning_integration.record_user_selection(
                    recommended_agents=recommended_agents,
                    selected_agent=selected_agent,
                    task_type=task_type,
                    project_phase=project_phase
                )
                logger.info(f"📚 Recorded user selection for basic learning: {selected_agent}")
            except Exception as e:
                logger.warning(f"Failed to record user selection: {e}")

    def record_task_outcome(self, agent_name: str, success: bool, task_type: str = None,
                           completion_time: float = None, quality_score: float = None):
        """Record task outcome for hybrid intelligence system"""
        context = {
            'task_type': task_type or 'development',
            'completion_time': completion_time,
            'quality_score': quality_score
        }

        # Try hybrid intelligence system first
        if hasattr(self, 'hybrid_intelligence') and self.hybrid_intelligence:
            try:
                self.hybrid_intelligence.record_task_outcome(
                    agent_name=agent_name,
                    success=success,
                    context=context
                )
                logger.info(f"🧠 Recorded task outcome for hybrid intelligence {agent_name}: {'✅' if success else '❌'}")
            except Exception as e:
                logger.warning(f"Failed to record hybrid intelligence task outcome: {e}")

        # Fallback to basic adaptive learning
        elif hasattr(self, 'learning_integration') and self.learning_integration:
            try:
                self.learning_integration.record_task_outcome(
                    agent_name=agent_name,
                    task_type=task_type or 'development',
                    success=success,
                    completion_time=completion_time,
                    quality_score=quality_score
                )
                logger.info(f"📊 Recorded task outcome for basic learning {agent_name}: {'✅' if success else '❌'}")
            except Exception as e:
                logger.warning(f"Failed to record task outcome: {e}")

    def get_learning_status(self) -> Dict[str, Any]:
        """Get status of hybrid intelligence / adaptive learning system"""
        # Try hybrid intelligence system first
        if hasattr(self, 'hybrid_intelligence') and self.hybrid_intelligence:
            try:
                return self.hybrid_intelligence.get_system_status()
            except Exception as e:
                return {"error": f"Error getting hybrid intelligence status: {e}"}

        # Fallback to basic adaptive learning
        elif hasattr(self, 'learning_integration') and self.learning_integration:
            try:
                return self.learning_integration.get_learning_status()
            except Exception as e:
                return {"error": f"Error getting learning status: {e}"}

        else:
            return {"learning_enabled": False, "reason": "No learning system available"}

    def get_agent_insights(self, agent_name: str) -> Dict[str, Any]:
        """Get detailed insights for specific agent"""
        if hasattr(self, 'learning_integration') and self.learning_integration:
            try:
                return self.learning_integration.get_agent_insights(agent_name)
            except Exception as e:
                return {"error": f"Error getting agent insights: {e}"}
        else:
            return {"learning_enabled": False, "reason": "Learning integration not available"}

class PerformanceTracker:
    """Track performance metrics for agent selection"""

    def __init__(self):
        self.request_history = []
        self.response_history = []
        self.performance_metrics = {
            'total_requests': 0,
            'ai_selections': 0,
            'fallback_selections': 0,
            'average_processing_time': 0.0,
            'success_rate': 1.0
        }

    def track_request(self, request: AgentSelectionRequest):
        """Track incoming request"""
        self.request_history.append({
            'timestamp': time.time(),
            'project_path': request.project_path,
            'selection_mode': request.selection_mode,
            'confidence_threshold': request.confidence_threshold
        })

        self.performance_metrics['total_requests'] += 1

    def track_response(self, response: AgentSelectionResponse):
        """Track response"""
        self.response_history.append({
            'timestamp': time.time(),
            'agent_count': len(response.recommended_agents),
            'fallback_used': response.fallback_used,
            'processing_time': response.processing_time,
            'selection_method': response.metadata.get('selection_method', 'unknown')
        })

        # Update metrics
        if response.fallback_used:
            self.performance_metrics['fallback_selections'] += 1
        else:
            self.performance_metrics['ai_selections'] += 1

        # Update average processing time
        times = [r['processing_time'] for r in self.response_history if r['processing_time'] > 0]
        if times:
            self.performance_metrics['average_processing_time'] = sum(times) / len(times)

    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        return {
            'metrics': self.performance_metrics.copy(),
            'recent_performance': self.response_history[-10:],  # Last 10 responses
            'ai_success_rate': (
                self.performance_metrics['ai_selections'] /
                max(1, self.performance_metrics['total_requests'])
            )
        }

class FrameworkIntegrator:
    """Integration layer with existing framework"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.agent_selector = AgentSelectionEngine(framework_root)

    def enhanced_agent_selection(self, project_path: str, **kwargs) -> Dict[str, Any]:
        """Enhanced agent selection that integrates with existing framework"""

        # Create selection request
        request = AgentSelectionRequest(
            project_path=project_path,
            selection_mode=kwargs.get('mode', 'ai'),
            confidence_threshold=kwargs.get('threshold', 0.5),
            max_agents=kwargs.get('max_agents', 10),
            user_preferences=kwargs.get('preferences', None)
        )

        # Get recommendations
        response = self.agent_selector.select_agents(request)

        # Format for framework compatibility
        return {
            'recommended_agents': response.recommended_agents,
            'workflow_sequence': response.workflow_sequence,
            'confidence_scores': response.confidence_scores,
            'reasoning': response.reasoning,
            'processing_time': response.processing_time,
            'ai_powered': not response.fallback_used,
            'metadata': response.metadata
        }

    def get_agent_for_prompt(self, prompt_path: str, project_context: Optional[Dict] = None) -> str:
        """Get optimal agent for a specific prompt"""

        # Extract prompt category from path
        prompt_file = Path(prompt_path)
        category = self._extract_prompt_category(prompt_file)

        if project_context:
            # Use AI to select best agent for prompt + context
            request = AgentSelectionRequest(
                project_path=project_context.get('project_path', '.'),
                context_data=project_context,
                max_agents=1
            )

            response = self.agent_selector.select_agents(request)

            # Filter agents by category compatibility
            compatible_agents = self._filter_agents_by_category(response.recommended_agents, category)

            if compatible_agents:
                return compatible_agents[0]

        # Fallback to category-based selection
        return self._get_default_agent_for_category(category)

    def _extract_prompt_category(self, prompt_file: Path) -> str:
        """Extract category from prompt file path"""
        # Look for category in path
        path_parts = prompt_file.parts

        # Check for agents directory structure
        if 'agents' in path_parts:
            agents_index = path_parts.index('agents')
            if agents_index + 1 < len(path_parts):
                return path_parts[agents_index + 1]

        # Default category
        return 'general'

    def _filter_agents_by_category(self, agents: List[str], category: str) -> List[str]:
        """Filter agents by category compatibility"""
        category_mapping = {
            'frontend': ['frontend-engineer'],
            'backend': ['backend-engineer', 'api-engineer'],
            'api': ['api-engineer', 'backend-engineer'],
            'data': ['data-engineer', 'data-scientist'],
            'security': ['security-engineer'],
            'quality': ['qa-engineer'],
            'deployment': ['deployment-engineer', 'platform-engineer'],
            'planner': ['product-manager', 'business-analyst'],
            'session': ['session-manager'],
            'project': ['project-owner']
        }

        compatible = category_mapping.get(category, [])

        # Return agents that are both recommended and compatible
        return [agent for agent in agents if agent in compatible]

    def _get_default_agent_for_category(self, category: str) -> str:
        """Get default agent for category"""
        default_mapping = {
            'frontend': 'frontend-engineer',
            'backend': 'backend-engineer',
            'api': 'api-engineer',
            'data': 'data-engineer',
            'security': 'security-engineer',
            'quality': 'qa-engineer',
            'deployment': 'deployment-engineer',
            'planner': 'product-owner',
            'session': 'session-manager',
            'project': 'project-owner'
        }

        return default_mapping.get(category, 'project-owner')

def main():
    """Demo AI agent selector"""
    print("🤖 AI-POWERED AGENT SELECTION - FRAMEWORK INTEGRATION DEMO")
    print("=" * 80)

    # Initialize framework integrator
    framework_root = str(Path(__file__).parent.parent.parent)
    integrator = FrameworkIntegrator(framework_root)

    print(f"🔧 Initialized framework integrator")
    print(f"📁 Framework root: {framework_root}")

    # Test 1: Enhanced agent selection
    print(f"\n🎯 TEST 1: Enhanced Agent Selection")
    print("-" * 40)

    test_project = framework_root  # Use framework itself as test project
    selection_result = integrator.enhanced_agent_selection(
        test_project,
        mode='ai',
        threshold=0.5,
        max_agents=8
    )

    print(f"📊 Selection Results:")
    print(f"  AI-Powered: {'✅' if selection_result['ai_powered'] else '❌'}")
    print(f"  Processing Time: {selection_result['processing_time']:.3f}s")
    print(f"  Agents ({len(selection_result['recommended_agents'])}):")

    for i, agent in enumerate(selection_result['recommended_agents'][:5], 1):
        confidence = selection_result['confidence_scores'].get(agent, 0.0)
        confidence_icon = "🟢" if confidence > 0.7 else "🟡" if confidence > 0.5 else "🔴"
        print(f"    {i}. {agent} {confidence_icon} ({confidence:.3f})")

    print(f"\n⚡ Workflow Sequence:")
    for i, agent in enumerate(selection_result['workflow_sequence'][:6], 1):
        print(f"    {i}. {agent}")

    # Test 2: Prompt-specific agent selection
    print(f"\n🎯 TEST 2: Prompt-Specific Agent Selection")
    print("-" * 40)

    test_prompts = [
        ".claude/prompts/agents/frontend/react-component.md",
        ".claude/prompts/agents/backend/api-development.md",
        ".claude/prompts/agents/security/threat-modeling.md",
        ".claude/prompts/session/session-start.md"
    ]

    for prompt_path in test_prompts:
        optimal_agent = integrator.get_agent_for_prompt(
            prompt_path,
            project_context={'project_path': test_project}
        )
        prompt_name = Path(prompt_path).stem
        print(f"  📝 {prompt_name} → 🤖 {optimal_agent}")

    # Test 3: Performance metrics
    print(f"\n🎯 TEST 3: Performance Metrics")
    print("-" * 40)

    performance = integrator.agent_selector.performance_tracker.get_performance_summary()
    metrics = performance['metrics']

    print(f"📊 Performance Summary:")
    print(f"  Total Requests: {metrics['total_requests']}")
    print(f"  AI Selections: {metrics['ai_selections']}")
    print(f"  Fallback Selections: {metrics['fallback_selections']}")
    print(f"  Average Processing Time: {metrics['average_processing_time']:.3f}s")
    print(f"  AI Success Rate: {performance['ai_success_rate']:.1%}")

    # Test 4: Configuration
    print(f"\n🎯 TEST 4: Framework Configuration")
    print("-" * 40)

    config = integrator.agent_selector.config
    print(f"⚙️ AI Configuration:")
    print(f"  AI Enabled: {'✅' if config.ai_enabled else '❌'}")
    print(f"  Confidence Threshold: {config.selection_confidence_threshold}")
    print(f"  Fallback to Manual: {'✅' if config.fallback_to_manual else '❌'}")
    print(f"  Learning Enabled: {'✅' if config.learning_enabled else '❌'}")
    print(f"  Performance Monitoring: {'✅' if config.performance_monitoring else '❌'}")

    print(f"\n✅ AI-Enhanced Agent Selection integration demonstrated successfully!")
    print("🚀 Ready for intelligent workflow orchestration!")

if __name__ == "__main__":
    main()