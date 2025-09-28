#!/bin/bash
# AI Tools Core Dependencies Installation Script
# Framework v3.2.0 - Optimized Architecture

echo "🤖 Installing AI Tools Core Dependencies"
echo "========================================"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install Python 3 and pip first."
    exit 1
fi

echo "📦 Installing essential dependencies..."

# Install from requirements.txt if available
if [ -f "$(dirname "$0")/requirements.txt" ]; then
    pip3 install -r "$(dirname "$0")/requirements.txt"
else
    # Fallback: install essential dependencies directly
    pip3 install PyYAML>=6.0.0
    pip3 install pytest>=6.0.0
    pip3 install pytest-cov>=3.0.0
fi

echo ""
echo "✅ Dependencies installation completed!"
echo ""
echo "🔍 Verifying installation..."

# Verify critical dependencies
python3 -c "import yaml; print('✅ PyYAML:', yaml.__version__)" 2>/dev/null || echo "❌ PyYAML installation failed"
python3 -c "import pytest; print('✅ pytest:', pytest.__version__)" 2>/dev/null || echo "❌ pytest installation failed"

echo ""
echo "🚀 AI Tools ready for technology detection and agent recommendations!"
echo "   Run: python3 .ai-tools/core/bin/project_analyzer.py"