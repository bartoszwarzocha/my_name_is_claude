#!/usr/bin/env python3
"""
Simplified Agent Selection System
Claude Code Multi-Agent Framework

A fast, reliable agent recommendation system based on technology stack analysis.
Replaces the over-engineered 1,323-line ai_agent_selector.py with ~100 lines.

Version: 2.0.0 - Simplified Architecture
"""

from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class AgentSelectionRequest:
    """Simplified agent selection request"""
    project_path: str
    max_agents: int = 8
    selection_mode: str = "auto"

@dataclass
class AgentSelectionResponse:
    """Simplified agent selection response"""
    recommended_agents: List[str]
    confidence: float
    processing_time: float
    agent_reasoning: Dict[str, List[str]] = None  # Agent -> reasons (technologies that triggered it)

class SimpleAgentSelector:
    """Fast, reliable agent selection based on technology patterns"""

    def __init__(self):
        # Technology to agent mappings
        self.technology_agent_map = {
            # Programming Languages
            'python': ['backend-engineer', 'data-engineer', 'api-engineer'],
            'javascript': ['frontend-engineer', 'api-engineer'],
            'typescript': ['frontend-engineer', 'api-engineer'],
            'java': ['backend-engineer', 'enterprise-architect'],
            'c++': ['performance-engineer', 'software-architect', 'desktop-developer'],
            'c#': ['backend-engineer', 'enterprise-architect'],
            'go': ['backend-engineer', 'api-engineer'],
            'rust': ['performance-engineer', 'backend-engineer'],
            'php': ['backend-engineer', 'api-engineer'],
            'ruby': ['backend-engineer', 'api-engineer'],

            # Frontend Frameworks
            'react': ['frontend-engineer', 'ux-designer'],
            'angular': ['frontend-engineer', 'enterprise-architect'],
            'vue': ['frontend-engineer', 'ux-designer'],
            'svelte': ['frontend-engineer'],

            # Backend Frameworks
            'django': ['backend-engineer', 'api-engineer'],
            'flask': ['backend-engineer', 'api-engineer'],
            'fastapi': ['api-engineer', 'backend-engineer'],
            'express': ['api-engineer', 'backend-engineer'],
            'spring': ['enterprise-architect', 'backend-engineer'],

            # Build Systems and Tools
            'cmake': ['performance-engineer', 'software-architect'],
            'make': ['performance-engineer', 'software-architect'],
            'docker': ['deployment-engineer', 'platform-engineer'],
            'kubernetes': ['deployment-engineer', 'platform-engineer'],

            # Databases
            'postgresql': ['data-engineer', 'backend-engineer'],
            'mysql': ['data-engineer', 'backend-engineer'],
            'mongodb': ['data-engineer', 'backend-engineer'],
            'redis': ['performance-engineer', 'backend-engineer'],

            # AI/ML
            'tensorflow': ['ai-engineer', 'data-engineer'],
            'pytorch': ['ai-engineer', 'data-engineer'],
            'scikit-learn': ['data-engineer', 'ai-engineer'],

            # Desktop Development
            'wxpython': ['desktop-developer', 'python-specialist'],
            'qt': ['desktop-developer', 'performance-engineer'],
            'electron': ['frontend-engineer', 'desktop-developer'],

            # Graphics and Game Development
            'opengl': ['graphics-engineer', 'performance-engineer', 'desktop-developer'],
            'vulkan': ['graphics-engineer', 'performance-engineer'],
            'directx': ['graphics-engineer', 'performance-engineer'],
            'opencv': ['graphics-engineer', 'ai-engineer', 'computer-vision-engineer'],
            'assimp': ['graphics-engineer', '3d-engineer', 'game-developer'],
            'glfw': ['graphics-engineer', 'desktop-developer'],
            'sdl': ['graphics-engineer', 'desktop-developer', 'game-developer'],
            'wxwidgets': ['desktop-developer', 'gui-engineer', 'cpp-specialist'],

            # Testing
            'pytest': ['qa-engineer', 'backend-engineer'],
            'jest': ['qa-engineer', 'frontend-engineer'],
            'junit': ['qa-engineer', 'backend-engineer'],
        }

        # Core agents that are useful for most projects
        self.core_agents = [
            'project-owner',      # Project management
            'session-manager',    # Session and workflow management
            'software-architect', # Overall architecture
            'qa-engineer'         # Quality assurance
        ]

    def select_agents(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """
        Select appropriate agents based on technology stack

        Args:
            request: Agent selection request

        Returns:
            AgentSelectionResponse with recommended agents
        """
        import time
        from core.core.simple_technology_detector import SimpleTechnologyDetector

        start_time = time.time()

        # Detect technology stack
        detector = SimpleTechnologyDetector()
        tech_stack = detector.detect_technology_stack(request.project_path)

        # Get all technologies (languages + frameworks + build tools)
        all_technologies = [
            tech.lower() for tech in
            tech_stack.languages + tech_stack.frameworks + tech_stack.build_tools
        ]

        # Start with core agents
        recommended_agents = list(self.core_agents)

        # Add technology-specific agents with reasoning
        agent_scores = {}
        agent_reasoning = {}
        for tech in all_technologies:
            if tech in self.technology_agent_map:
                for agent in self.technology_agent_map[tech]:
                    agent_scores[agent] = agent_scores.get(agent, 0) + 1
                    if agent not in agent_reasoning:
                        agent_reasoning[agent] = []
                    agent_reasoning[agent].append(tech)

        # Sort agents by relevance score and add top ones
        sorted_agents = sorted(agent_scores.items(), key=lambda x: x[1], reverse=True)

        for agent, score in sorted_agents:
            if agent not in recommended_agents and len(recommended_agents) < request.max_agents:
                recommended_agents.append(agent)

        # Calculate confidence based on technology detection confidence and agent matches
        confidence = min(1.0, tech_stack.confidence + (len(agent_scores) * 0.1))

        processing_time = time.time() - start_time

        return AgentSelectionResponse(
            recommended_agents=recommended_agents[:request.max_agents],
            confidence=confidence,
            processing_time=processing_time,
            agent_reasoning=agent_reasoning
        )


# Compatibility layer for existing framework wizard
class AgentSelectionEngine(SimpleAgentSelector):
    """Compatibility wrapper for existing code"""

    def __init__(self, project_path: str = None):
        super().__init__()
        self.project_path = project_path