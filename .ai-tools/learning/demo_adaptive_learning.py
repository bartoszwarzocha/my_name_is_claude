#!/usr/bin/env python3
"""
Adaptive Learning System Demo
Demonstrates the project-adaptive learning capabilities
"""

import sys
import json
from pathlib import Path

# Add necessary paths
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))
sys.path.insert(0, str(parent_dir / "core" / "integration"))

try:
    # Try direct import first
    from learning_integration import AdaptiveLearningIntegration
except ImportError:
    # If that fails, try importing the module directly
    import learning_integration
    AdaptiveLearningIntegration = learning_integration.AdaptiveLearningIntegration

try:
    from ai_agent_selector import AgentSelectionEngine, AgentSelectionRequest
except ImportError:
    # Simplified demo without full AI agent selector
    print("Note: Running in learning-only demo mode")


def demo_adaptive_learning_system():
    """Demonstrate the adaptive learning system capabilities."""
    print("🧠 AI Tools Adaptive Learning System Demo")
    print("=" * 50)

    # Initialize the adaptive learning integration
    print("\n1. Initializing Adaptive Learning System...")
    try:
        learning_integration = AdaptiveLearningIntegration()
        print(f"✅ Learning system initialized")
        print(f"   Project ID: {learning_integration.learning_system.project_id}")
        print(f"   Learning Enabled: {learning_integration.learning_enabled}")
    except Exception as e:
        print(f"❌ Failed to initialize learning system: {e}")
        return

    # Initialize AI Agent Selector with learning integration
    print("\n2. Initializing AI Agent Selector...")
    try:
        framework_root = str(parent_dir)
        agent_selector = AgentSelectionEngine(framework_root)
        print(f"✅ Agent selector initialized")
        print(f"   AI Enabled: {agent_selector.config.ai_enabled}")
        print(f"   Learning Integration: {hasattr(agent_selector, 'learning_integration')}")
    except Exception as e:
        print(f"❌ Failed to initialize agent selector: {e}")
        return

    # Demo 1: Basic learning system status
    print("\n3. Learning System Status:")
    try:
        status = learning_integration.get_learning_status()
        print(f"   Learning Enabled: {status.get('learning_enabled')}")
        print(f"   Project ID: {status.get('project_id')}")

        choice_stats = status.get('choice_statistics', {})
        if choice_stats.get('total_choices', 0) > 0:
            print(f"   Total User Choices: {choice_stats['total_choices']}")
            alignment_stats = choice_stats.get('alignment_statistics', {})
            alignment_rate = alignment_stats.get('overall_alignment_rate', 0)
            print(f"   Alignment Rate: {alignment_rate:.2%}")
        else:
            print("   No user choice data yet")

    except Exception as e:
        print(f"❌ Error getting learning status: {e}")

    # Demo 2: Simulate user interactions for learning
    print("\n4. Simulating User Interactions for Learning...")

    # Simulate some user choices
    demo_interactions = [
        {
            'recommended': ['frontend-engineer', 'ux-designer', 'backend-engineer'],
            'selected': 'frontend-engineer',
            'task_type': 'development',
            'project_phase': 'implementation'
        },
        {
            'recommended': ['qa-engineer', 'security-engineer', 'deployment-engineer'],
            'selected': 'qa-engineer',
            'task_type': 'testing',
            'project_phase': 'quality_assurance'
        },
        {
            'recommended': ['backend-engineer', 'api-engineer', 'database-administrator'],
            'selected': 'api-engineer',
            'task_type': 'development',
            'project_phase': 'implementation'
        }
    ]

    for i, interaction in enumerate(demo_interactions, 1):
        try:
            learning_integration.record_user_selection(
                recommended_agents=interaction['recommended'],
                selected_agent=interaction['selected'],
                task_type=interaction['task_type'],
                project_phase=interaction['project_phase']
            )
            print(f"   ✅ Recorded interaction {i}: {interaction['selected']}")
        except Exception as e:
            print(f"   ❌ Failed to record interaction {i}: {e}")

    # Demo 3: Simulate task outcomes
    print("\n5. Simulating Task Outcomes...")

    task_outcomes = [
        {'agent': 'frontend-engineer', 'success': True, 'completion_time': 45.0, 'quality_score': 0.85},
        {'agent': 'qa-engineer', 'success': True, 'completion_time': 30.0, 'quality_score': 0.90},
        {'agent': 'api-engineer', 'success': True, 'completion_time': 60.0, 'quality_score': 0.80}
    ]

    for outcome in task_outcomes:
        try:
            learning_integration.record_task_outcome(
                agent_name=outcome['agent'],
                task_type='development',
                success=outcome['success'],
                completion_time=outcome['completion_time'],
                quality_score=outcome['quality_score']
            )
            print(f"   ✅ Recorded outcome for {outcome['agent']}: {'✅' if outcome['success'] else '❌'}")
        except Exception as e:
            print(f"   ❌ Failed to record outcome for {outcome['agent']}: {e}")

    # Demo 4: Get personalized recommendations
    print("\n6. Testing Personalized Recommendations...")
    try:
        base_agents = ['frontend-engineer', 'backend-engineer', 'ux-designer', 'qa-engineer', 'api-engineer']
        context = {'task_type': 'development', 'project_phase': 'implementation'}

        enhanced_recommendations = learning_integration.enhance_agent_recommendations(
            base_recommendations=base_agents,
            context=context
        )

        print(f"   Base recommendations: {base_agents[:3]}")
        print(f"   Enhanced recommendations: {enhanced_recommendations[:3]}")

        if enhanced_recommendations != base_agents:
            print("   🧠 Learning system successfully personalized recommendations!")
        else:
            print("   📊 Learning system maintaining base recommendations")

    except Exception as e:
        print(f"   ❌ Error getting personalized recommendations: {e}")

    # Demo 5: Agent insights
    print("\n7. Agent Performance Insights...")
    test_agents = ['frontend-engineer', 'qa-engineer', 'api-engineer']

    for agent in test_agents:
        try:
            insights = learning_integration.get_agent_insights(agent)
            performance = insights.get('performance', {})
            overall_metrics = performance.get('overall_metrics', {})

            if overall_metrics.get('total_uses', 0) > 0:
                success_rate = overall_metrics.get('success_rate', 0)
                total_uses = overall_metrics.get('total_uses', 0)
                print(f"   {agent}: {total_uses} uses, {success_rate:.1%} success rate")
            else:
                print(f"   {agent}: No usage data")

        except Exception as e:
            print(f"   ❌ Error getting insights for {agent}: {e}")

    # Demo 6: Learning system suggestions
    print("\n8. Learning System Suggestions...")
    try:
        suggestions = learning_integration.suggest_improvements()
        if suggestions:
            for suggestion in suggestions:
                priority_emoji = {"high": "🔥", "medium": "⭐", "low": "💡", "info": "ℹ️"}.get(suggestion['priority'], "📝")
                print(f"   {priority_emoji} {suggestion['type']}: {suggestion['message']}")
        else:
            print("   ✅ No suggestions - system is performing well")
    except Exception as e:
        print(f"   ❌ Error getting suggestions: {e}")

    # Demo 7: Export learning data (anonymized)
    print("\n9. Learning Data Export (Anonymized)...")
    try:
        export_data = learning_integration.export_learning_data()

        # Show anonymized insights
        metadata = export_data.get('project_metadata', {})
        patterns = export_data.get('anonymized_patterns', {})
        insights = export_data.get('model_insights', {})

        print(f"   Project Learning: {metadata.get('learning_enabled', False)}")
        print(f"   Choice Patterns: {patterns.get('user_choice_patterns', {}).get('total_choices', 0)} total")
        print(f"   Effectiveness Data: {patterns.get('agent_effectiveness_patterns', {}).get('total_agents_tracked', 0)} agents")
        print(f"   Learning Accuracy: {insights.get('learning_accuracy', 0):.1%}")

    except Exception as e:
        print(f"   ❌ Error exporting learning data: {e}")

    print("\n" + "=" * 50)
    print("✅ Adaptive Learning System Demo Complete!")
    print("\nThe system is now ready to learn from your project-specific usage patterns.")
    print("It will continuously improve agent recommendations based on:")
    print("  • Your agent selection preferences")
    print("  • Task success rates and completion times")
    print("  • Project context and development phases")
    print("  • Quality feedback and effectiveness metrics")


if __name__ == "__main__":
    demo_adaptive_learning_system()