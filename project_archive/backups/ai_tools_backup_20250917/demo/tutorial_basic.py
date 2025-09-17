#!/usr/bin/env python3
"""
AI-Powered Agent Selection - Basic Tutorial
Claude Code Multi-Agent Framework

Interactive tutorial demonstrating basic usage of the AI-powered agent selection system.
Learn how to analyze projects and get intelligent agent recommendations.

Usage:
    python .ai-tools/core/demo/tutorial_basic.py
"""

import sys
from pathlib import Path

# Add the framework root to Python path
framework_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(framework_root))

def main():
    print("🎓 AI-POWERED AGENT SELECTION - BASIC TUTORIAL")
    print("=" * 60)
    print()

    print("This tutorial will guide you through:")
    print("1. Basic project analysis")
    print("2. Understanding agent recommendations")
    print("3. Interpreting confidence scores")
    print("4. Using workflow suggestions")
    print()

    print("📋 TUTORIAL STEPS:")
    print()

    print("Step 1: Run the main project analyzer")
    print("  Command: python .ai-tools/core/bin/project_analyzer.py .")
    print("  This analyzes the current framework project")
    print()

    print("Step 2: Analyze a custom project")
    print("  Command: python .ai-tools/core/bin/project_analyzer.py /path/to/your/project")
    print("  Replace /path/to/your/project with your actual project path")
    print()

    print("Step 3: Understanding the output")
    print("  • Technology Stack: Detected technologies and confidence")
    print("  • Project Complexity: Startup/SME/Enterprise classification")
    print("  • Business Domain: Detected business focus area")
    print("  • Agent Recommendations: Suggested agents with confidence scores")
    print("  • Workflow Sequence: Recommended execution order")
    print()

    print("Step 4: Using the recommendations")
    print("  • High confidence (>0.85): Strongly recommended agents")
    print("  • Medium confidence (0.7-0.85): Good fit agents")
    print("  • Lower confidence (<0.7): Consider based on specific needs")
    print()

    print("🚀 Ready to start? Run the commands above!")
    print("📚 For more advanced features, see tutorial_advanced.py")

if __name__ == "__main__":
    main()