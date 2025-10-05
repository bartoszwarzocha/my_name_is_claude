"""
Output Styles System

Part of Claude Code Multi-Agent Framework v3.7.0

Context-aware communication style selection for different audiences and tasks.
"""

from .output_styles_manager import (
    OutputStylesManager,
    OutputStyle,
    StyleContext
)

__all__ = [
    "OutputStylesManager",
    "OutputStyle",
    "StyleContext",
]

__version__ = "3.7.0"
