#!/usr/bin/env python3
"""
AI Tools Basic Tutorial
Claude Code Multi-Agent Framework

Interactive tutorial demonstrating AI tools capabilities
Version: 1.0.0
"""

import os
import sys
import time
from pathlib import Path

# Colors for output
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_colored(text, color=Colors.CYAN):
    """Print colored text"""
    print(f"{color}{text}{Colors.END}")

def print_header(title):
    """Print section header"""
    print("\n" + "="*60)
    print_colored(f"🎯 {title}", Colors.BOLD + Colors.BLUE)
    print("="*60)

def wait_for_user():
    """Wait for user to continue"""
    import sys
    if sys.stdin.isatty():
        try:
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        except (EOFError, KeyboardInterrupt):
            pass
    else:
        # Non-interactive mode - just add a pause
        print(f"\n{Colors.YELLOW}(Auto-continuing in non-interactive mode...){Colors.END}")
        time.sleep(1)

def demo_technology_detection():
    """Demonstrate technology detection"""
    print_header("Technology Detection Demo")

    print_colored("🔍 AI Tools can automatically detect technology stacks in projects:", Colors.GREEN)
    print("   • Languages: Python, JavaScript, C++, Java, etc.")
    print("   • Frameworks: React, Django, Spring, OpenGL, etc.")
    print("   • Build Tools: CMake, Maven, npm, etc.")
    print("   • Graphics: OpenGL, Vulkan, wxWidgets, etc.")

    print_colored("\n📊 Example Detection Results:", Colors.BLUE)
    print("   Frontend: React, TypeScript, CSS")
    print("   Backend: Python, Django, PostgreSQL")
    print("   Infrastructure: Docker, CMake")
    print("   Confidence: 0.85")

    wait_for_user()

def demo_agent_recommendations():
    """Demonstrate agent recommendation system"""
    print_header("Agent Recommendation System")

    print_colored("🤖 Based on technology detection, AI Tools recommends optimal agents:", Colors.GREEN)
    print("   • Core Management: project-owner, session-manager")
    print("   • Development: frontend-engineer, backend-engineer")
    print("   • Quality: qa-engineer, security-engineer")
    print("   • Specialized: graphics-engineer, data-engineer")

    print_colored("\n🎯 Smart Matching Examples:", Colors.BLUE)
    print("   C++ + OpenGL → graphics-engineer, performance-engineer")
    print("   React + Node.js → frontend-engineer, api-engineer")
    print("   Python + Django → backend-engineer, api-engineer")
    print("   CMake + vcpkg → software-architect, desktop-developer")

    wait_for_user()

def demo_project_analysis():
    """Demonstrate project analysis capabilities"""
    print_header("Project Analysis Features")

    print_colored("📈 AI Tools provides comprehensive project insights:", Colors.GREEN)
    print("   • Technology Stack Detection (90+ technologies)")
    print("   • Project Complexity Assessment")
    print("   • Business Domain Classification")
    print("   • Agent Workflow Recommendations")

    print_colored("\n🏢 Business Domain Examples:", Colors.BLUE)
    print("   • Software Development Tools")
    print("   • Graphics & Visualization")
    print("   • Scientific Computing")
    print("   • Enterprise Applications")

    wait_for_user()

def demo_framework_integration():
    """Demonstrate framework integration"""
    print_header("Framework Integration")

    print_colored("🔗 AI Tools seamlessly integrates with Claude Code Framework:", Colors.GREEN)
    print("   • Automatic agent selection")
    print("   • CLAUDE.md generation from templates")
    print("   • Session management integration")
    print("   • Quality validation automation")

    print_colored("\n⚡ Efficiency Benefits:", Colors.BLUE)
    print("   • 50% reduction in project setup time")
    print("   • Intelligent agent matching")
    print("   • Automated quality checks")
    print("   • Seamless workflow orchestration")

    wait_for_user()

def show_tutorial_menu():
    """Show tutorial options"""
    print_colored("\n🎓 AI Tools Tutorial Menu:", Colors.BOLD + Colors.CYAN)
    print("   [1] Technology Detection Demo")
    print("   [2] Agent Recommendation System")
    print("   [3] Project Analysis Features")
    print("   [4] Framework Integration")
    print("   [5] Complete Tutorial")
    print("   [q] Quit Tutorial")

def main():
    """Main tutorial function"""
    os.system('clear' if os.name == 'posix' else 'cls')

    print_colored("🚀 Welcome to AI Tools Tutorial!", Colors.BOLD + Colors.GREEN)
    print_colored("Claude Code Multi-Agent Framework", Colors.CYAN)
    print("\nThis tutorial will demonstrate the key features of AI Tools:")
    print("• Intelligent technology detection")
    print("• Smart agent recommendations")
    print("• Comprehensive project analysis")
    print("• Seamless framework integration")

    # Check if running in non-interactive mode (from script)
    import sys
    if not sys.stdin.isatty():
        # Non-interactive mode - run complete tutorial
        print_colored("\n🎯 Running complete tutorial in non-interactive mode...", Colors.CYAN)
        demo_technology_detection()
        demo_agent_recommendations()
        demo_project_analysis()
        demo_framework_integration()
    else:
        # Interactive mode
        while True:
            show_tutorial_menu()
            try:
                choice = input(f"\n{Colors.YELLOW}Select option (1-5, q): {Colors.END}").strip().lower()
            except (EOFError, KeyboardInterrupt):
                break

            if choice == '1':
                demo_technology_detection()
            elif choice == '2':
                demo_agent_recommendations()
            elif choice == '3':
                demo_project_analysis()
            elif choice == '4':
                demo_framework_integration()
            elif choice == '5':
                # Complete tutorial
                demo_technology_detection()
                demo_agent_recommendations()
                demo_project_analysis()
                demo_framework_integration()
                break
            elif choice in ['q', 'quit', 'exit']:
                break
            else:
                print_colored("❌ Invalid option. Please select 1-5 or q.", Colors.RED)
                continue

    print_header("Tutorial Complete")
    print_colored("🎉 Thank you for completing the AI Tools tutorial!", Colors.GREEN)
    print_colored("💡 You're now ready to use AI Tools effectively!", Colors.BLUE)
    print("\nNext steps:")
    print("• Run './ai-tools.sh' to access the full system")
    print("• Try project analysis on your current directory")
    print("• Explore agent recommendations for your tech stack")
    print("• Use the framework setup wizard for new projects")

if __name__ == "__main__":
    main()