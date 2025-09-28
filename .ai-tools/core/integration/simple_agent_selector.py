#!/usr/bin/env python3
"""
Simplified Agent Selection System
Claude Code Multi-Agent Framework

A fast, reliable agent recommendation system based on dynamic agent discovery
and Technical Proficiencies analysis. No hardcoded mappings.

Version: 3.0.0 - Dynamic Architecture
"""

import os
import sys
from pathlib import Path

# Add the discovery module to the path
current_dir = Path(__file__).parent
discovery_dir = current_dir.parent / "discovery"
sys.path.insert(0, str(discovery_dir))

from dynamic_agent_discovery import DynamicAgentDiscovery
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
    """Fast, reliable agent selection based on dynamic agent discovery"""

    def __init__(self, agents_root_path: str = ".claude/agents"):
        # Initialize dynamic agent discovery
        self.discovery = DynamicAgentDiscovery(agents_root_path)
        self.agents_scanned = False

        # Core agents that are useful for most projects
        self.core_agents = [
            'project-owner',      # Project management
            'session-manager',    # Session and workflow management
            'software-architect', # Overall architecture
            'qa-engineer'         # Quality assurance
        ]

    def _ensure_agents_scanned(self):
        """Ensure agents have been scanned and mappings built"""
        if not self.agents_scanned:
            print("🔍 Scanning agents...")
            self.discovery.scan_agents()
            self.discovery.build_technology_mapping()
            self.discovery.build_domain_mapping()
            self.agents_scanned = True
            print(f"✅ Loaded {len(self.discovery.discovered_agents)} agents with {len(self.discovery.technology_mapping)} technologies")

    def select_agents(self, request: AgentSelectionRequest) -> AgentSelectionResponse:
        """
        Select appropriate agents based on technology stack using dynamic discovery

        Args:
            request: Agent selection request

        Returns:
            AgentSelectionResponse with recommended agents
        """
        import time
        import sys
        from pathlib import Path

        # Add the core module to the path
        core_dir = Path(__file__).parent.parent / "core"
        sys.path.insert(0, str(core_dir))

        from simple_technology_detector import SimpleTechnologyDetector

        start_time = time.time()

        # Ensure agents are scanned
        self._ensure_agents_scanned()

        # Detect technology stack
        detector = SimpleTechnologyDetector()
        tech_stack = detector.detect_technology_stack(request.project_path)

        # Get all technologies (languages + frameworks + build tools + databases + frontend + backend + infrastructure)
        all_technologies = []

        # Add detected technologies
        all_technologies.extend(tech_stack.languages)
        all_technologies.extend(tech_stack.frameworks)
        all_technologies.extend(tech_stack.build_tools)

        # Add compatibility properties if they exist
        if hasattr(tech_stack, 'frontend') and tech_stack.frontend:
            all_technologies.extend(tech_stack.frontend)
        if hasattr(tech_stack, 'backend') and tech_stack.backend:
            all_technologies.extend(tech_stack.backend)
        if hasattr(tech_stack, 'database') and tech_stack.database:
            all_technologies.extend(tech_stack.database)
        if hasattr(tech_stack, 'infrastructure') and tech_stack.infrastructure:
            all_technologies.extend(tech_stack.infrastructure)

        # Normalize to lowercase
        all_technologies = [tech.lower() for tech in all_technologies if tech]

        # Use dynamic agent discovery to get agent recommendations
        agent_recommendations = self.discovery.get_agents_for_technologies(all_technologies)

        # Start with core agents that exist in our discovered agents
        recommended_agents = []
        agent_reasoning = {}

        # Add core agents if they exist
        for core_agent in self.core_agents:
            if core_agent in self.discovery.discovered_agents:
                recommended_agents.append(core_agent)
                agent_reasoning[core_agent] = ['core_framework_agent']

        # Add technology-specific agents
        for agent, matching_technologies in agent_recommendations:
            if agent not in recommended_agents and len(recommended_agents) < request.max_agents:
                recommended_agents.append(agent)
                agent_reasoning[agent] = matching_technologies

        # Calculate confidence based on technology detection confidence and agent matches
        technology_match_score = len(agent_recommendations) * 0.1
        confidence = min(1.0, tech_stack.confidence + technology_match_score)

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