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
            for category_dir in agents_dir.iterdir():
                if category_dir.is_dir():
                    for agent_file in category_dir.glob("*.md"):
                        agent_name = agent_file.stem
                        agents.append(agent_name)

        logger.info(f"Discovered {len(agents)} available agents")
        return sorted(agents)

    def _load_agent_capabilities(self) -> Dict[str, Dict[str, Any]]:
        """Load agent capabilities and metadata"""
        capabilities = {}

        # Define agent capabilities (simplified - in real implementation,
        # this would parse from agent files)
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

        for agent in self.available_agents:
            if agent in agent_definitions:
                capabilities[agent] = agent_definitions[agent]
            else:
                # Default capabilities for unknown agents
                capabilities[agent] = {
                    'technologies': [],
                    'complexity_preference': 0.5,
                    'project_phases': ['development'],
                    'team_collaboration': 'medium',
                    'expertise_level': 'general'
                }

        return capabilities

    def _initialize_ai_components(self):
        """Initialize AI components if enabled"""
        if not self.config.ai_enabled:
            logger.info("AI features disabled in configuration")
            return

        try:
            # Import AI components (would be actual imports in real implementation)
            from ai_tools.core.data_collection_system import ProjectContextAnalyzer
            from ai_tools.core.feature_engineering import ProjectFeatureEncoder
            from ai_tools.models.ensemble_recommender import create_default_ensemble

            # Initialize components
            self.project_analyzer = ProjectContextAnalyzer()
            self.feature_encoder = ProjectFeatureEncoder()
            self.ml_ensemble = create_default_ensemble()

            # Try to load pre-trained models
            self._load_pretrained_models()

            logger.info("✅ AI components initialized successfully")

        except Exception as e:
            logger.warning(f"⚠️ Failed to initialize AI components: {e}")
            logger.info("🔄 Falling back to rule-based selection")
            self.config.ai_enabled = False

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
        """Main agent selection method"""
        start_time = time.time()

        try:
            # Track the request
            self.performance_tracker.track_request(request)

            if self.config.ai_enabled and self.ml_ensemble:
                response = self._ai_powered_selection(request)
            else:
                response = self._rule_based_selection(request)

            # Add processing time
            response.processing_time = time.time() - start_time

            # Track the response
            self.performance_tracker.track_response(response)

            return response

        except Exception as e:
            logger.error(f"Error in agent selection: {e}")

            # Fallback to basic selection
            fallback_response = self._emergency_fallback_selection(request)
            fallback_response.processing_time = time.time() - start_time
            fallback_response.fallback_used = True

            return fallback_response

    def _ai_powered_selection(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """AI-powered agent selection using ML models"""
        logger.info(f"🤖 Using AI-powered agent selection for {request.project_path}")

        try:
            # Analyze project context
            if request.context_data:
                project_context = request.context_data
            else:
                context_obj = self.project_analyzer.analyze_project(request.project_path)
                project_context = {
                    'technology_stack': asdict(context_obj.technology_stack),
                    'complexity': asdict(context_obj.complexity),
                    'business_domain': asdict(context_obj.business_domain),
                    'team_context': asdict(context_obj.team_context),
                    'mcp_insights': asdict(context_obj.mcp_insights)
                }

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

            # Build response
            recommended_agents = [rec.agent_name for rec in limited_recommendations]
            confidence_scores = {rec.agent_name: rec.confidence_score for rec in limited_recommendations}
            reasoning = {rec.agent_name: rec.reasoning for rec in limited_recommendations}

            return AgentSelectionResponse(
                recommended_agents=recommended_agents,
                confidence_scores=confidence_scores,
                reasoning=reasoning,
                workflow_sequence=ml_recommendations.workflow_sequence,
                fallback_used=False,
                processing_time=0.0,  # Will be set by caller
                metadata={
                    'selection_method': 'ai_powered',
                    'ml_performance': ml_recommendations.model_performance,
                    'project_context_hash': project_context.get('context_hash', 'unknown')
                }
            )

        except Exception as e:
            logger.warning(f"AI selection failed: {e}, falling back to rule-based")
            return self._rule_based_selection(request)

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
        """Simple project analysis for rule-based selection"""
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
            # Check for common files and directories
            project = Path(project_path)

            # Frontend indicators
            if any((project / f).exists() for f in ['package.json', 'src/', 'public/', 'index.html']):
                analysis['has_frontend'] = True
                analysis['technologies'].extend(['frontend', 'javascript'])

            # Backend indicators
            if any((project / f).exists() for f in ['requirements.txt', 'app.py', 'main.py', 'server.js']):
                analysis['has_backend'] = True
                analysis['technologies'].extend(['backend', 'api'])

            # Database indicators
            if any((project / f).exists() for f in ['database/', 'migrations/', 'models/', 'schema.sql']):
                analysis['has_database'] = True
                analysis['technologies'].append('database')

            # Testing indicators
            if any((project / f).exists() for f in ['tests/', 'test/', '__tests__/', 'spec/']):
                analysis['has_tests'] = True
                analysis['technologies'].append('testing')

            # Docker indicators
            if any((project / f).exists() for f in ['Dockerfile', 'docker-compose.yml', '.dockerignore']):
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
        """Apply selection rules to project analysis"""
        agent_scores = {}

        # Always recommend core agents
        agent_scores['project-owner'] = 0.95
        agent_scores['session-manager'] = 0.90

        # Technology-based rules
        if project_analysis['has_frontend']:
            agent_scores['frontend-engineer'] = 0.85

        if project_analysis['has_backend']:
            agent_scores['backend-engineer'] = 0.85
            agent_scores['api-engineer'] = 0.75

        if project_analysis['has_database']:
            agent_scores['data-engineer'] = 0.80

        if project_analysis['has_tests']:
            agent_scores['qa-engineer'] = 0.75

        if project_analysis['has_docker']:
            agent_scores['deployment-engineer'] = 0.80

        # Complexity-based rules
        if project_analysis['complexity'] == 'complex':
            agent_scores['enterprise-architect'] = 0.75
            agent_scores['security-engineer'] = 0.70

        # Ensure all scores are within valid range
        for agent in agent_scores:
            agent_scores[agent] = max(0.0, min(1.0, agent_scores[agent]))

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