#!/usr/bin/env python3
"""
Test script for the updated Simple Agent Selector
"""

import sys
from pathlib import Path

# Add the integration module to the path
current_dir = Path(__file__).parent
integration_dir = current_dir / ".ai-tools/core/integration"
sys.path.insert(0, str(integration_dir))

from simple_agent_selector import SimpleAgentSelector, AgentSelectionRequest

def test_agent_selector():
    """Test the updated agent selector"""
    print("🧪 Testing Updated Simple Agent Selector with Dynamic Discovery")
    print("=" * 70)

    # Initialize selector
    selector = SimpleAgentSelector()

    # Test with current project
    request = AgentSelectionRequest(project_path='.', max_agents=8)
    response = selector.select_agents(request)

    print("\n📊 Agent Selection Results:")
    print(f"  Recommended Agents: {len(response.recommended_agents)}")
    print(f"  Confidence: {response.confidence:.2f}")
    print(f"  Processing Time: {response.processing_time:.3f}s")

    print("\n🤖 Recommended Agents:")
    for i, agent in enumerate(response.recommended_agents, 1):
        reasons = response.agent_reasoning.get(agent, ['unknown'])
        print(f"  {i}. {agent}")
        print(f"     → Reason: {', '.join(reasons)}")

    print("\n✅ Test completed successfully!")

    # Validate that all recommended agents actually exist
    print("\n🔍 Validating agent existence:")
    for agent in response.recommended_agents:
        if agent in selector.discovery.discovered_agents:
            print(f"  ✅ {agent} - EXISTS")
        else:
            print(f"  ❌ {agent} - MISSING")

if __name__ == "__main__":
    test_agent_selector()