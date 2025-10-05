#!/usr/bin/env python3
"""
Dependency Manager for Parallel Agent Execution System

Manages dependencies between agents with automatic resolution and cycle detection.

Part of Framework v3.8.0 - Parallel Agent Execution System
"""

import logging
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AgentDependency:
    """Agent dependency information"""
    agent_type: str
    depends_on: List[str]
    provides: List[str]


class DependencyManager:
    """
    Manages agent dependencies and provides resolution algorithms.

    Features:
    - Dependency graph management
    - Topological sorting
    - Circular dependency detection
    - Automatic dependency resolution
    """

    def __init__(self, dependency_graph: Optional[Dict] = None):
        """
        Initialize dependency manager.

        Args:
            dependency_graph: Dictionary of agent dependencies
        """
        self.dependency_graph: Dict[str, AgentDependency] = {}

        if dependency_graph:
            self._load_dependency_graph(dependency_graph)

        logger.info(f"Dependency Manager initialized with {len(self.dependency_graph)} agents")

    def _load_dependency_graph(self, graph: Dict):
        """Load dependency graph from configuration"""
        for agent_type, config in graph.items():
            depends_on = config.get("dependsOn", [])
            provides = config.get("provides", [])

            self.dependency_graph[agent_type] = AgentDependency(
                agent_type=agent_type,
                depends_on=depends_on,
                provides=provides
            )

    def add_dependency(self, agent_type: str, depends_on: List[str], provides: Optional[List[str]] = None):
        """
        Add agent dependency.

        Args:
            agent_type: Agent type
            depends_on: List of agent types this agent depends on
            provides: List of artifacts this agent provides
        """
        self.dependency_graph[agent_type] = AgentDependency(
            agent_type=agent_type,
            depends_on=depends_on,
            provides=provides or []
        )

        logger.info(f"Added dependency for {agent_type}: depends on {depends_on}")

    def get_dependencies(self, agent_type: str) -> List[str]:
        """
        Get list of dependencies for an agent.

        Args:
            agent_type: Agent type

        Returns:
            List of agent types this agent depends on
        """
        if agent_type in self.dependency_graph:
            return self.dependency_graph[agent_type].depends_on
        return []

    def resolve_execution_order(self, agent_types: List[str]) -> Tuple[List[str], List[str]]:
        """
        Resolve execution order using topological sort.

        Args:
            agent_types: List of agent types to order

        Returns:
            Tuple of (ordered_agents, errors)
        """
        # Build in-degree map
        in_degree = {}
        graph = {}

        for agent_type in agent_types:
            dependencies = self.get_dependencies(agent_type)
            in_degree[agent_type] = len(dependencies)
            graph[agent_type] = dependencies

        # Kahn's algorithm for topological sort
        queue = [agent for agent in agent_types if in_degree[agent] == 0]
        ordered = []

        while queue:
            agent = queue.pop(0)
            ordered.append(agent)

            # Update in-degrees for dependent agents
            for other_agent in agent_types:
                if agent in graph.get(other_agent, []):
                    in_degree[other_agent] -= 1
                    if in_degree[other_agent] == 0:
                        queue.append(other_agent)

        # Check for cycles
        errors = []
        if len(ordered) != len(agent_types):
            missing = set(agent_types) - set(ordered)
            errors.append(f"Circular dependency detected for agents: {missing}")
            logger.warning(f"Circular dependency: {missing}")

        return ordered, errors

    def detect_circular_dependencies(self, agent_types: List[str]) -> Optional[List[str]]:
        """
        Detect circular dependencies.

        Args:
            agent_types: List of agent types to check

        Returns:
            List of agents involved in cycle, or None if no cycle
        """
        visited = set()
        rec_stack = set()

        def has_cycle(agent: str, path: List[str]) -> Optional[List[str]]:
            visited.add(agent)
            rec_stack.add(agent)
            path.append(agent)

            dependencies = self.get_dependencies(agent)
            for dep in dependencies:
                if dep not in agent_types:
                    continue

                if dep not in visited:
                    cycle = has_cycle(dep, path)
                    if cycle:
                        return cycle
                elif dep in rec_stack:
                    # Found cycle
                    cycle_start = path.index(dep)
                    return path[cycle_start:]

            rec_stack.remove(agent)
            path.pop()
            return None

        for agent in agent_types:
            if agent not in visited:
                cycle = has_cycle(agent, [])
                if cycle:
                    return cycle

        return None

    def get_dependency_tree(self, agent_type: str, max_depth: int = 10) -> Dict:
        """
        Get full dependency tree for an agent.

        Args:
            agent_type: Agent type
            max_depth: Maximum recursion depth

        Returns:
            Dependency tree dictionary
        """
        def build_tree(agent: str, depth: int = 0) -> Dict:
            if depth > max_depth:
                return {"agent": agent, "error": "Max depth reached"}

            dependencies = self.get_dependencies(agent)
            return {
                "agent": agent,
                "dependencies": [build_tree(dep, depth + 1) for dep in dependencies]
            }

        return build_tree(agent_type)

    def can_run_parallel(self, agent_types: List[str]) -> bool:
        """
        Check if agents can run in parallel (no dependencies between them).

        Args:
            agent_types: List of agent types

        Returns:
            True if agents can run in parallel
        """
        for agent in agent_types:
            dependencies = self.get_dependencies(agent)
            if any(dep in agent_types for dep in dependencies):
                return False
        return True

    def get_parallel_groups(self, agent_types: List[str]) -> List[List[str]]:
        """
        Group agents into parallel execution groups.

        Args:
            agent_types: List of agent types

        Returns:
            List of agent groups that can run in parallel
        """
        ordered, errors = self.resolve_execution_order(agent_types)

        if errors:
            logger.warning(f"Cannot create parallel groups: {errors}")
            return [[agent] for agent in agent_types]

        # Group agents by level (agents at same level can run in parallel)
        levels: Dict[int, List[str]] = {}
        agent_level = {}

        # Calculate level for each agent
        for agent in ordered:
            dependencies = self.get_dependencies(agent)
            if not dependencies:
                agent_level[agent] = 0
            else:
                max_dep_level = max(agent_level.get(dep, 0) for dep in dependencies if dep in agent_level)
                agent_level[agent] = max_dep_level + 1

        # Group by level
        for agent, level in agent_level.items():
            if level not in levels:
                levels[level] = []
            levels[level].append(agent)

        # Return groups in order
        return [levels[level] for level in sorted(levels.keys())]


# CLI Interface
if __name__ == "__main__":
    print("\n=== Testing Dependency Manager ===")

    # Create dependency graph
    dependency_graph = {
        "backend-engineer": {
            "dependsOn": ["software-architect"],
            "provides": ["api", "database"]
        },
        "frontend-engineer": {
            "dependsOn": ["ux-designer", "backend-engineer"],
            "provides": ["ui"]
        },
        "ux-designer": {
            "dependsOn": ["software-architect"],
            "provides": ["design"]
        },
        "qa-engineer": {
            "dependsOn": ["backend-engineer", "frontend-engineer"],
            "provides": ["test_results"]
        }
    }

    manager = DependencyManager(dependency_graph)

    # Test 1: Resolve execution order
    print("\n1. Resolving execution order")
    agents = ["backend-engineer", "frontend-engineer", "ux-designer", "qa-engineer", "software-architect"]
    ordered, errors = manager.resolve_execution_order(agents)
    print(f"Execution order: {ordered}")
    if errors:
        print(f"Errors: {errors}")

    # Test 2: Get parallel groups
    print("\n2. Getting parallel execution groups")
    groups = manager.get_parallel_groups(agents)
    for i, group in enumerate(groups):
        print(f"  Group {i + 1}: {group}")

    # Test 3: Check if agents can run in parallel
    print("\n3. Checking if agents can run in parallel")
    can_parallel = manager.can_run_parallel(["backend-engineer", "frontend-engineer"])
    print(f"  backend-engineer + frontend-engineer: {can_parallel}")

    can_parallel = manager.can_run_parallel(["software-architect", "ux-designer"])
    print(f"  software-architect + ux-designer: {can_parallel}")

    # Test 4: Dependency tree
    print("\n4. Getting dependency tree for frontend-engineer")
    tree = manager.get_dependency_tree("frontend-engineer")
    print(f"  {tree}")

    print("\n=== Dependency Manager Test Complete ===")
