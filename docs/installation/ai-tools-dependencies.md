# AI Tools Dependencies Installation Guide

## Overview

AI Tools require specific Python packages for full functionality. Without these dependencies, the system runs in **fallback mode** (rule-based) instead of full AI capabilities.

## Dependencies Status Detection

The framework automatically checks dependencies when running:
```bash
./ai-tools.sh
```

## Required Dependencies

### System Dependencies
- `python3` (3.8+)
- `python3-pip`
- `python3-venv` (for isolated installation)

### Python ML Dependencies
- `numpy>=1.21.0`
- `pandas>=1.3.0`
- `scikit-learn>=1.0.0`
- `scipy>=1.7.0`
- `joblib>=1.0.0`

## Installation Methods

### Method 1: Virtual Environment (RECOMMENDED)

**Ubuntu/Debian Issue:** Modern Ubuntu/Debian systems use "externally-managed-environment" which prevents direct pip installation.

**Solution:**

1. **Install venv support:**
   ```bash
   sudo apt update
   sudo apt install python3.12-venv
   ```

2. **Create and activate virtual environment:**
   ```bash
   cd /mnt/e/AI/my_name_is_claude/.ai-tools/
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install ML dependencies:**
   ```bash
   pip install numpy pandas scikit-learn scipy joblib
   ```

### Method 2: System Packages (Alternative)

```bash
sudo apt update
sudo apt install python3-numpy python3-pandas python3-sklearn python3-scipy python3-joblib
```

### Method 3: Framework Script (After venv setup)

```bash
bash /mnt/e/AI/my_name_is_claude/.ai-tools/core/install_dependencies.sh
```

## Common Issues

### Issue 1: "externally-managed-environment" Error

**Error:**
```
error: externally-managed-environment
× This environment is externally managed
```

**Solution:** Use virtual environment (Method 1 above)

### Issue 2: "ensurepip is not available"

**Error:**
```
The virtual environment was not created successfully because ensurepip is not available.
On Debian/Ubuntu systems, you need to install the python3-venv package
```

**Solution:**
```bash
sudo apt install python3.12-venv
# or for other Python versions:
sudo apt install python3-venv
```

### Issue 3: Missing pip in venv

**Symptoms:** `venv/bin/activate` doesn't exist or pip not available

**Solution:**
1. Remove corrupted venv: `rm -rf venv`
2. Install python3-venv: `sudo apt install python3.12-venv`
3. Recreate venv: `python3 -m venv venv`

## Verification

After installation, verify dependencies:

```bash
# Activate venv if using
source .ai-tools/venv/bin/activate

# Check each dependency
python3 -c "import numpy; print('✅ numpy:', numpy.__version__)"
python3 -c "import pandas; print('✅ pandas:', pandas.__version__)"
python3 -c "import sklearn; print('✅ scikit-learn:', sklearn.__version__)"
python3 -c "import scipy; print('✅ scipy:', scipy.__version__)"
python3 -c "import joblib; print('✅ joblib:', joblib.__version__)"
```

## Framework Integration

The framework will automatically:
- Detect missing dependencies
- Suggest appropriate installation commands
- Fall back to rule-based mode if ML packages unavailable
- Display clear status messages

## Performance Impact

- **With ML Dependencies:** Full AI-powered agent selection
- **Without ML Dependencies:** Rule-based selection (fallback mode)
- **Performance:** Both modes provide high-quality results

## Platform-Specific Notes

### Ubuntu 22.04+ / Debian 12+
- Requires `python3-venv` package
- Uses "externally-managed-environment" protection
- Virtual environment is mandatory for pip installs

### WSL (Windows Subsystem for Linux)
- Same requirements as Ubuntu/Debian
- May have timeout issues with long installations
- Virtual environment highly recommended

### macOS
- Use `brew install python3` if needed
- Virtual environment recommended but not mandatory

### Other Linux Distributions
- Adapt package manager commands (yum, dnf, pacman, etc.)
- Virtual environment universally recommended

## Troubleshooting

If AI Tools continues showing fallback mode after installation:

1. **Check activation:** Ensure venv is activated when running ai-tools
2. **Check paths:** Verify Python can import all packages
3. **Restart shell:** Source fresh environment
4. **Check permissions:** Ensure proper file permissions in venv

## Integration with AI Tools

The `ai-tools.sh` script will:
- Automatically detect available dependencies
- Suggest installation commands based on detected system
- Show clear status of AI vs fallback mode
- Provide specific instructions for your platform

---

*This documentation covers common installation scenarios. For specific issues, check system logs and Python error messages.*