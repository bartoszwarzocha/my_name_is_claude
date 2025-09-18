#!/usr/bin/env python3
"""
Hybrid Intelligence System Demo
Demonstrates Phase 2: Universal Patterns + Adaptive Learning
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
    from hybrid_intelligence import HybridIntelligenceSystem
    from universal_patterns import UniversalPatternsSystem
    from ai_agent_selector import AgentSelectionEngine, AgentSelectionRequest
except ImportError as e:
    print(f"Note: Import error - {e}")
    print("Running in limited demo mode")


def demo_hybrid_intelligence_system():
    """Demonstrate the hybrid intelligence system capabilities."""
    print("🧠 AI Tools Hybrid Intelligence System Demo")
    print("Phase 2: Universal Patterns + Adaptive Learning")
    print("=" * 60)

    # Initialize the hybrid intelligence system
    print("\n1. Initializing Hybrid Intelligence System...")
    try:
        hybrid_system = HybridIntelligenceSystem()
        print(f"✅ Hybrid intelligence system initialized")

        status = hybrid_system.get_system_status()
        print(f"   Learning Enabled: {status['learning_enabled']}")
        print(f"   Universal Patterns: {status['universal_patterns']['patterns_count']} patterns")
        print(f"   Supported Domains: {len(status['universal_patterns']['supported_domains'])} domains")
        print(f"   Best Practices: {status['universal_patterns']['best_practices_count']} rules")

    except Exception as e:
        print(f"❌ Failed to initialize hybrid system: {e}")
        return

    # Demo universal patterns alone
    print("\n2. Universal Patterns System Demo...")
    try:
        universal_system = UniversalPatternsSystem()

        # Test different project contexts
        test_contexts = [
            {
                'name': 'E-commerce React App',
                'context': {
                    'technologies': ['react', 'node.js', 'postgresql', 'docker'],
                    'domain': 'ecommerce',
                    'complexity': 'medium',
                    'has_frontend': True,
                    'has_backend': True,
                    'has_database': True
                }
            },
            {
                'name': 'FinTech Java Backend',
                'context': {
                    'technologies': ['java', 'spring', 'postgresql', 'kubernetes'],
                    'domain': 'fintech',
                    'complexity': 'high',
                    'has_backend': True,
                    'has_database': True,
                    'has_security': True
                }
            },
            {
                'name': '3D Gaming Engine',
                'context': {
                    'technologies': ['c++', 'opengl', 'vulkan', '3d'],
                    'domain': 'gaming',
                    'complexity': 'enterprise',
                    'has_graphics': True,
                    'performance_critical': True
                }
            }
        ]

        for test in test_contexts:
            print(f"\n   📋 Testing: {test['name']}")
            universal_recs = universal_system.get_universal_recommendations(test['context'])

            print(f"      Universal Recommendations:")
            for agent, confidence, reasoning in universal_recs[:3]:
                print(f"      • {agent}: {confidence:.2f} - {reasoning[:80]}...")

    except Exception as e:
        print(f"❌ Universal patterns demo failed: {e}")

    # Demo hybrid intelligence with different scenarios
    print("\n3. Hybrid Intelligence System Demo...")

    test_scenarios = [
        {
            'name': 'Startup MVP (React + Node.js)',
            'context': {
                'technologies': ['react', 'node.js', 'mongodb', 'docker'],
                'domain': 'startup',
                'complexity': 'low',
                'project_phase': 'initialization',
                'task_type': 'development',
                'has_frontend': True,
                'has_backend': True,
                'has_database': True,
                'urgency': 'high'
            }
        },
        {
            'name': 'Enterprise Healthcare Platform',
            'context': {
                'technologies': ['python', 'django', 'postgresql', 'kubernetes', 'aws'],
                'domain': 'healthcare',
                'complexity': 'enterprise',
                'project_phase': 'development',
                'task_type': 'development',
                'has_frontend': True,
                'has_backend': True,
                'has_database': True,
                'handles_personal_data': True,
                'quality_focus': 'high'
            }
        },
        {
            'name': 'Real-time Gaming Backend',
            'context': {
                'technologies': ['c++', 'redis', 'websockets', 'docker'],
                'domain': 'gaming',
                'complexity': 'high',
                'project_phase': 'development',
                'task_type': 'performance',
                'has_backend': True,
                'performance_critical': True,
                'expected_load': 'high'
            }
        }
    ]

    for scenario in test_scenarios:
        print(f"\n   🎯 Scenario: {scenario['name']}")

        try:
            # Get hybrid recommendations
            hybrid_recs = hybrid_system.get_hybrid_recommendations(scenario['context'])

            print(f"      Hybrid Intelligence Recommendations:")
            for i, rec in enumerate(hybrid_recs[:5], 1):
                sources = ', '.join(rec['sources'])
                print(f"      {i}. {rec['agent']}: {rec['confidence']:.2f}")
                print(f"         Sources: {sources}")
                print(f"         Universal: {rec['universal_score']:.2f}, Adaptive: {rec['adaptive_score']:.2f}")
                print(f"         Reasoning: {rec['reasoning'][:100]}...")

        except Exception as e:
            print(f"      ❌ Scenario failed: {e}")

    # Demo learning feedback simulation
    print("\n4. Simulating User Feedback for Learning...")

    learning_simulations = [
        {
            'recommended': ['frontend-engineer', 'ux-designer', 'backend-engineer'],
            'selected': 'frontend-engineer',
            'context': {'task_type': 'development', 'project_phase': 'implementation'}
        },
        {
            'recommended': ['security-engineer', 'backend-engineer', 'compliance-auditor'],
            'selected': 'security-engineer',
            'context': {'task_type': 'security', 'project_phase': 'development'}
        },
        {
            'recommended': ['qa-engineer', 'automation-engineer', 'performance-engineer'],
            'selected': 'qa-engineer',
            'context': {'task_type': 'testing', 'project_phase': 'quality_assurance'}
        }
    ]

    for sim in learning_simulations:
        try:
            hybrid_system.record_feedback(
                recommended_agents=sim['recommended'],
                selected_agent=sim['selected'],
                context=sim['context']
            )
            print(f"   ✅ Recorded feedback: {sim['selected']}")
        except Exception as e:
            print(f"   ❌ Failed to record feedback: {e}")

    # Demo task outcome tracking
    print("\n5. Simulating Task Outcomes...")

    outcome_simulations = [
        {
            'agent': 'frontend-engineer',
            'success': True,
            'context': {
                'task_type': 'development',
                'completion_time': 45.0,
                'quality_score': 0.9
            }
        },
        {
            'agent': 'security-engineer',
            'success': True,
            'context': {
                'task_type': 'security',
                'completion_time': 90.0,
                'quality_score': 0.95
            }
        },
        {
            'agent': 'qa-engineer',
            'success': True,
            'context': {
                'task_type': 'testing',
                'completion_time': 60.0,
                'quality_score': 0.85
            }
        }
    ]

    for outcome in outcome_simulations:
        try:
            hybrid_system.record_task_outcome(
                agent_name=outcome['agent'],
                success=outcome['success'],
                context=outcome['context']
            )
            print(f"   ✅ Recorded outcome for {outcome['agent']}: {'✅' if outcome['success'] else '❌'}")
        except Exception as e:
            print(f"   ❌ Failed to record outcome: {e}")

    # Demo system insights after learning
    print("\n6. System Insights After Learning...")
    try:
        insights = hybrid_system.get_insights_and_suggestions()

        print(f"   System Performance:")
        print(f"   • Learning Quality: {insights['system_performance']['learning_quality']}")
        print(f"   • Recommendation Mode: {insights['system_performance']['recommendation_mode']}")
        print(f"   • Data Sufficiency: {insights['system_performance']['data_sufficiency']}")

        if 'learning_insights' in insights:
            learning = insights['learning_insights']
            print(f"\n   Learning Insights:")
            print(f"   • Alignment Trend: {learning.get('alignment_trend', 'N/A')}")
            print(f"   • Personalization Strength: {learning.get('personalization_strength', 0):.2%}")
            print(f"   • Learning Acceleration: {learning.get('learning_acceleration', 'N/A')}")

        print(f"\n   Universal Coverage:")
        coverage = insights['universal_coverage']
        print(f"   • Technology Coverage: {coverage['technology_coverage']} technologies")
        print(f"   • Domain Coverage: {coverage['domain_coverage']} domains")
        print(f"   • Patterns Available: {coverage['patterns_available']} patterns")

        print(f"\n   Suggestions:")
        for suggestion in insights.get('suggestions', []):
            priority_emoji = {"high": "🔥", "medium": "⭐", "low": "💡", "info": "ℹ️"}.get(suggestion['priority'], "📝")
            print(f"   {priority_emoji} {suggestion['type']}: {suggestion['message']}")

    except Exception as e:
        print(f"   ❌ Failed to get insights: {e}")

    # Demo with integrated AI Agent Selector
    print("\n7. Integration with AI Agent Selector...")
    try:
        framework_root = str(parent_dir)
        agent_selector = AgentSelectionEngine(framework_root)

        print(f"   Agent Selector Status:")
        print(f"   • AI Enabled: {agent_selector.config.ai_enabled}")
        print(f"   • Hybrid Intelligence: {hasattr(agent_selector, 'hybrid_intelligence')}")

        if hasattr(agent_selector, 'hybrid_intelligence'):
            learning_status = agent_selector.get_learning_status()
            print(f"   • Learning Status: {learning_status.get('learning_enabled', False)}")
            print(f"   • Universal Patterns: {learning_status.get('universal_patterns', {}).get('patterns_count', 0)}")

    except Exception as e:
        print(f"   ❌ AI Agent Selector integration failed: {e}")

    # Performance comparison
    print("\n8. Performance Comparison...")
    try:
        test_context = {
            'technologies': ['react', 'node.js', 'postgresql', 'docker'],
            'domain': 'ecommerce',
            'complexity': 'medium',
            'project_phase': 'development',
            'has_frontend': True,
            'has_backend': True,
            'has_database': True
        }

        # Universal only
        universal_recs = hybrid_system.universal_system.get_universal_recommendations(test_context)
        print(f"   Universal Only: {len(universal_recs)} recommendations")

        # Hybrid intelligence
        hybrid_recs = hybrid_system.get_hybrid_recommendations(test_context)
        print(f"   Hybrid Intelligence: {len(hybrid_recs)} recommendations")

        print(f"   Improvement: Enhanced contextualization and personalization")

    except Exception as e:
        print(f"   ❌ Performance comparison failed: {e}")

    print("\n" + "=" * 60)
    print("✅ Hybrid Intelligence System Demo Complete!")
    print("\nPhase 2 Features Demonstrated:")
    print("  🔵 Universal Patterns: Industry best practices and technology mappings")
    print("  🟢 Adaptive Learning: Project-specific preference learning")
    print("  🟣 Hybrid Intelligence: Optimal combination of both systems")
    print("  ⚙️  Context Awareness: Domain, complexity, and phase considerations")
    print("  📊 Performance Tracking: Real-time effectiveness monitoring")
    print("  🎯 Smart Recommendations: Contextual and personalized agent selection")


if __name__ == "__main__":
    demo_hybrid_intelligence_system()