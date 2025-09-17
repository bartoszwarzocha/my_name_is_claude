#!/bin/bash
# AI-Powered Agent Selection - Dependency Installation Script
# Framework v3.0.0 Compatibility

echo "🤖 Installing AI-Powered Agent Selection Dependencies"
echo "=================================================="

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install Python 3 and pip first."
    exit 1
fi

echo "📦 Installing core ML dependencies..."

# Install core dependencies
pip3 install numpy>=1.21.0
pip3 install pandas>=1.3.0
pip3 install scikit-learn>=1.0.0
pip3 install scipy>=1.7.0
pip3 install joblib>=1.0.0

echo "📊 Installing visualization libraries..."
pip3 install matplotlib>=3.5.0
pip3 install seaborn>=0.11.0

echo "📝 Installing text processing libraries..."
pip3 install nltk>=3.6.0

echo "🧪 Installing development dependencies..."
pip3 install pytest>=6.0.0
pip3 install pytest-cov>=3.0.0

echo "⚡ Installing performance optimization..."
pip3 install numba>=0.55.0

echo ""
echo "✅ Dependencies installation completed!"
echo ""
echo "🔍 Verifying installation..."

# Verify critical dependencies
python3 -c "import numpy; print('✅ numpy:', numpy.__version__)" 2>/dev/null || echo "❌ numpy installation failed"
python3 -c "import pandas; print('✅ pandas:', pandas.__version__)" 2>/dev/null || echo "❌ pandas installation failed"
python3 -c "import sklearn; print('✅ scikit-learn:', sklearn.__version__)" 2>/dev/null || echo "❌ scikit-learn installation failed"
python3 -c "import matplotlib; print('✅ matplotlib:', matplotlib.__version__)" 2>/dev/null || echo "❌ matplotlib installation failed"

echo ""
echo "🚀 Ready to test AI-Powered Agent Selection!"
echo "   Run: python3 .ai-tools/core/integration/ai_agent_selector.py"