#!/usr/bin/env python3
"""
AI-Powered Agent Selection - React Project Example
Claude Code Multi-Agent Framework

Example demonstrating how the AI system analyzes a typical React e-commerce project
and provides intelligent agent recommendations.

Usage:
    python .ai-tools/core/demo/example_react_project.py
"""

import sys
from pathlib import Path

# Add the framework root to Python path
framework_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(framework_root))

def main():
    print("⚛️ REACT E-COMMERCE PROJECT ANALYSIS EXAMPLE")
    print("=" * 60)
    print()

    print("This example shows how the AI system would analyze a typical React e-commerce project:")
    print()

    print("📁 EXAMPLE PROJECT STRUCTURE:")
    print("""
    react-ecommerce/
    ├── package.json          # React, TypeScript, Tailwind
    ├── src/
    │   ├── components/       # React components
    │   ├── pages/           # Application pages
    │   ├── services/        # API services
    │   └── utils/           # Utility functions
    ├── backend/
    │   ├── package.json     # Node.js, Express
    │   └── src/             # Backend API
    ├── docker-compose.yml   # Docker setup
    └── README.md
    """)

    print("🔍 AI ANALYSIS RESULTS:")
    print()

    print("Technology Stack Detection:")
    print("  ✅ Frontend: React, TypeScript, Tailwind CSS")
    print("  ✅ Backend: Node.js, Express")
    print("  ✅ Database: PostgreSQL (detected from docker-compose)")
    print("  ✅ Infrastructure: Docker")
    print("  ✅ Testing: Jest (detected from package.json)")
    print("  Confidence: 0.92")
    print()

    print("Project Complexity Assessment:")
    print("  📊 Classification: SME (Small-Medium Enterprise)")
    print("  📁 Files: ~450 files")
    print("  📝 Lines of Code: ~15,000 LOC")
    print("  🏗️ Complexity Score: 0.58")
    print()

    print("Business Domain Classification:")
    print("  🛒 Primary Domain: E-commerce")
    print("  🏢 Industry: Retail/Technology")
    print("  📋 Compliance: GDPR, PCI-DSS (payment processing)")
    print("  Confidence: 0.89")
    print()

    print("🤖 AI AGENT RECOMMENDATIONS:")
    print()

    print("Core Project Management:")
    print("  🟢 project-owner (confidence: 0.95)")
    print("  🟢 session-manager (confidence: 0.90)")
    print()

    print("Development Team:")
    print("  🟢 frontend-engineer (confidence: 0.92) - React expertise")
    print("  🟢 api-engineer (confidence: 0.90) - E-commerce APIs")
    print("  🟡 backend-engineer (confidence: 0.88) - Node.js services")
    print()

    print("Quality & Security:")
    print("  🟡 qa-engineer (confidence: 0.83) - Testing automation")
    print("  🟡 security-engineer (confidence: 0.84) - PCI-DSS compliance")
    print()

    print("Operations:")
    print("  🟡 deployment-engineer (confidence: 0.88) - Docker deployment")
    print()

    print("⚡ RECOMMENDED WORKFLOW:")
    print()
    print("Phase 1: Initialization (4h)")
    print("  → project-owner: Project setup and configuration")
    print("  → business-analyst: Requirements gathering")
    print()

    print("Phase 2: Architecture (8h)")
    print("  → software-architect: System design")
    print("  → ux-designer: User experience design")
    print()

    print("Phase 3: Development (20h)")
    print("  → frontend-engineer: React components and pages")
    print("  → api-engineer: E-commerce API development")
    print("  → backend-engineer: Business logic implementation")
    print()

    print("Phase 4: Quality Assurance (6h)")
    print("  → qa-engineer: Testing and validation")
    print("  → security-engineer: Security review and PCI compliance")
    print()

    print("Phase 5: Deployment (4h)")
    print("  → deployment-engineer: Production deployment")
    print()

    print("📊 EFFICIENCY PREDICTION:")
    print("  Manual Setup Time: ~20 minutes")
    print("  AI-Assisted Setup: ~10 minutes")
    print("  Time Saved: 50% reduction")
    print()

    print("🎯 KEY INSIGHTS:")
    print("  • High confidence in React/TypeScript stack detection")
    print("  • E-commerce domain properly identified from project context")
    print("  • Compliance requirements (PCI-DSS) automatically flagged")
    print("  • Appropriate agent mix for SME-scale e-commerce project")
    print("  • Realistic workflow with proper phase sequencing")

if __name__ == "__main__":
    main()