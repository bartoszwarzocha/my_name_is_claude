#!/usr/bin/env python3
"""
Output Styles Manager for Claude Code Multi-Agent Framework

Context-aware communication style selection and management.
Automatically adapts Claude's output style based on audience, agent, and task.

Part of Framework v3.7.0 - Output Styles Activation

Features:
- 4 output styles: technical, executive, educational, code_review
- Context-aware style selection
- Agent-based defaults
- Customizable templates
- Quality guidelines enforcement
- Multi-language support (English/Polish)
"""

import json
import logging
from typing import Dict, List, Optional
from pathlib import Path
from dataclasses import dataclass
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OutputStyle(Enum):
    """Available output styles"""
    TECHNICAL = "technical"
    EXECUTIVE = "executive"
    EDUCATIONAL = "educational"
    CODE_REVIEW = "code_review"


@dataclass
class StyleContext:
    """Context information for style selection"""
    agent_type: Optional[str] = None
    audience: Optional[str] = None
    role: Optional[str] = None
    task_type: Optional[str] = None
    experience_level: Optional[str] = None
    language: str = "en"


class OutputStylesManager:
    """
    Manages output styles and context-aware selection.

    Features:
    - Load style configurations
    - Select style based on context
    - Generate style prompts
    - Apply quality guidelines
    """

    def __init__(self, config_path: Optional[str] = None, framework_root: Optional[Path] = None):
        """
        Initialize Output Styles Manager.

        Args:
            config_path: Path to output-styles.json
            framework_root: Framework root directory
        """
        self.framework_root = framework_root or self._get_framework_root()
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()

        # Cache for selected styles
        self.style_cache: Dict[str, OutputStyle] = {}

        logger.info("Output Styles Manager initialized")

    def _get_framework_root(self) -> Path:
        """Get framework root directory"""
        return Path(__file__).parent.parent.parent

    def _get_default_config_path(self) -> str:
        """Get default configuration file path"""
        return str(self.framework_root / ".claude" / "config" / "output-styles.json")

    def _load_config(self) -> Dict:
        """Load output styles configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading output styles config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "styles": {
                "technical": {
                    "name": "Technical Style",
                    "description": "Detailed technical communication"
                }
            },
            "contextualSelection": {
                "enabled": True,
                "defaultStyle": "technical"
            }
        }

    def select_style(self, context: StyleContext) -> OutputStyle:
        """
        Select appropriate output style based on context.

        Args:
            context: Style selection context

        Returns:
            Selected OutputStyle
        """
        # Check cache first
        cache_key = self._get_cache_key(context)
        if cache_key in self.style_cache and self.config.get("customization", {}).get("cachePreferences", True):
            return self.style_cache[cache_key]

        # Check if contextual selection is enabled
        if not self.config.get("contextualSelection", {}).get("enabled", True):
            default_style = self.config.get("contextualSelection", {}).get("defaultStyle", "technical")
            return OutputStyle(default_style)

        selected_style = None

        # 1. Check agent defaults first
        if context.agent_type:
            agent_defaults = self.config.get("agentDefaults", {})
            if context.agent_type in agent_defaults:
                selected_style = OutputStyle(agent_defaults[context.agent_type])
                logger.debug(f"Selected style from agent defaults: {selected_style.value}")

        # 2. Apply contextual rules (override agent defaults if applicable)
        if not selected_style or self.config.get("customization", {}).get("allowContextSpecific", True):
            contextual_style = self._apply_contextual_rules(context)
            if contextual_style:
                selected_style = contextual_style
                logger.debug(f"Selected style from contextual rules: {selected_style.value}")

        # 3. Fall back to default
        if not selected_style:
            default_style = self.config.get("contextualSelection", {}).get("defaultStyle", "technical")
            selected_style = OutputStyle(default_style)
            logger.debug(f"Using default style: {selected_style.value}")

        # Cache the selection
        self.style_cache[cache_key] = selected_style

        logger.info(f"Selected output style: {selected_style.value} (context: {cache_key})")
        return selected_style

    def _apply_contextual_rules(self, context: StyleContext) -> Optional[OutputStyle]:
        """
        Apply contextual selection rules.

        Args:
            context: Style selection context

        Returns:
            Selected style or None
        """
        rules = self.config.get("contextualSelection", {}).get("rules", [])

        for rule in rules:
            condition = rule.get("condition", "")
            style_name = rule.get("style")

            # Evaluate condition (simplified evaluation)
            if self._evaluate_condition(condition, context):
                logger.debug(f"Matched rule: {rule.get('reason')}")
                return OutputStyle(style_name)

        return None

    def _evaluate_condition(self, condition: str, context: StyleContext) -> bool:
        """
        Evaluate a condition against context (simplified).

        Args:
            condition: Condition string
            context: Context to evaluate against

        Returns:
            True if condition matches
        """
        # Simple condition evaluation (can be extended)
        context_dict = {
            "audience": context.audience,
            "role": context.role or "",
            "task_type": context.task_type,
            "experience_level": context.experience_level
        }

        # Check for simple equality conditions
        if "===" in condition:
            parts = condition.split("===")
            if len(parts) == 2:
                var_name = parts[0].strip()
                expected_value = parts[1].strip().strip("'\"")

                actual_value = context_dict.get(var_name)
                return actual_value == expected_value

        # Check for includes() conditions
        if ".includes(" in condition:
            import re
            match = re.search(r'(\w+)\.includes\(["\'](\w+)["\']\)', condition)
            if match:
                var_name = match.group(1)
                search_value = match.group(2)

                actual_value = context_dict.get(var_name, "")
                return search_value in str(actual_value)

        return False

    def _get_cache_key(self, context: StyleContext) -> str:
        """Generate cache key from context"""
        return f"{context.agent_type}_{context.audience}_{context.task_type}_{context.experience_level}"

    def get_style_prompt(self, style: OutputStyle, context: Optional[StyleContext] = None) -> str:
        """
        Generate prompt instructions for a specific style.

        Args:
            style: Output style
            context: Optional context for customization

        Returns:
            Prompt instructions string
        """
        style_config = self.config.get("styles", {}).get(style.value, {})

        if not style_config:
            logger.warning(f"No configuration found for style: {style.value}")
            return ""

        # Build prompt from style configuration
        prompt_parts = []

        # Style description
        prompt_parts.append(f"**Communication Style:** {style_config.get('name')}")
        prompt_parts.append(f"{style_config.get('description')}")
        prompt_parts.append("")

        # Characteristics
        characteristics = style_config.get("characteristics", {})
        if characteristics:
            prompt_parts.append("**Characteristics:**")
            for key, value in characteristics.items():
                prompt_parts.append(f"- {key.replace('_', ' ').title()}: {value}")
            prompt_parts.append("")

        # Communication patterns
        patterns = style_config.get("communicationPatterns", {})
        if patterns:
            prompt_parts.append("**Communication Patterns:**")
            for key, value in patterns.items():
                prompt_parts.append(f"- {key.replace('_', ' ').title()}: {value}")
            prompt_parts.append("")

        # Content guidelines
        guidelines = style_config.get("contentGuidelines", {})
        if guidelines:
            prompt_parts.append("**Content Guidelines:**")
            include_items = [k.replace("include", "").replace("_", " ").strip() for k, v in guidelines.items() if v is True and k.startswith("include")]
            exclude_items = [k.replace("include", "").replace("_", " ").strip() for k, v in guidelines.items() if v is False and k.startswith("include")]

            if include_items:
                prompt_parts.append(f"- Include: {', '.join(include_items)}")
            if exclude_items:
                prompt_parts.append(f"- Exclude: {', '.join(exclude_items)}")
            prompt_parts.append("")

        # Quality guidelines
        quality = self.config.get("qualityGuidelines", {}).get(style.value, {})
        if quality:
            prompt_parts.append("**Quality Requirements:**")
            for key, value in quality.items():
                prompt_parts.append(f"- {key.replace('_', ' ').title()}: {value}")
            prompt_parts.append("")

        return "\n".join(prompt_parts)

    def get_style_template(self, style: OutputStyle, template_type: str = "header") -> str:
        """
        Get template for a specific style and type.

        Args:
            style: Output style
            template_type: Template type (header, footer, etc.)

        Returns:
            Template string
        """
        templates = self.config.get("templates", {}).get(style.value, {})
        return templates.get(template_type, "")

    def get_style_config(self, style: OutputStyle) -> Dict:
        """
        Get full configuration for a style.

        Args:
            style: Output style

        Returns:
            Style configuration dictionary
        """
        return self.config.get("styles", {}).get(style.value, {})

    def list_available_styles(self) -> List[str]:
        """Get list of available style names"""
        return list(self.config.get("styles", {}).keys())

    def validate_style_usage(self, style: OutputStyle, content: str) -> Dict:
        """
        Validate content against style quality guidelines.

        Args:
            style: Output style
            content: Content to validate

        Returns:
            Validation result with warnings/errors
        """
        quality_guidelines = self.config.get("qualityGuidelines", {}).get(style.value, {})
        warnings = []
        errors = []

        # Example validations (can be extended)
        if style == OutputStyle.TECHNICAL:
            # Check for minimum code examples
            min_code_examples = quality_guidelines.get("minCodeExamples", 0)
            code_block_count = content.count("```")
            if code_block_count < min_code_examples * 2:  # *2 because ``` appears at start and end
                warnings.append(f"Technical style should include at least {min_code_examples} code examples")

        elif style == OutputStyle.EXECUTIVE:
            # Check for maximum response length
            max_length = quality_guidelines.get("maxResponseLength", 1000)
            if len(content) > max_length:
                warnings.append(f"Executive style should be concise (max {max_length} chars)")

            # Check for required elements
            if quality_guidelines.get("requireExecutiveSummary") and "Executive Summary" not in content:
                errors.append("Executive style requires an Executive Summary section")

        elif style == OutputStyle.CODE_REVIEW:
            # Check for severity levels
            if quality_guidelines.get("requireSeverity"):
                has_severity = any(severity in content for severity in ["Critical:", "Major:", "Minor:", "Suggestion:"])
                if not has_severity:
                    warnings.append("Code review should include severity levels")

        return {
            "valid": len(errors) == 0,
            "warnings": warnings,
            "errors": errors
        }

    def generate_context_prompt(self, context: StyleContext) -> str:
        """
        Generate complete context-aware style prompt.

        Args:
            context: Style context

        Returns:
            Complete prompt for Claude
        """
        # Select style
        style = self.select_style(context)

        # Build prompt
        prompt_parts = []

        prompt_parts.append("# Output Style Configuration")
        prompt_parts.append("")
        prompt_parts.append(f"**Active Style:** {style.value.replace('_', ' ').title()}")
        prompt_parts.append("")

        # Add style-specific prompt
        style_prompt = self.get_style_prompt(style, context)
        prompt_parts.append(style_prompt)

        # Add language-specific note
        if context.language == "pl":
            prompt_parts.append("**Language:** Polish (style principles apply across languages)")
        else:
            prompt_parts.append("**Language:** English")

        prompt_parts.append("")
        prompt_parts.append("---")
        prompt_parts.append("")
        prompt_parts.append("Please apply the above style to all your responses in this context.")

        return "\n".join(prompt_parts)


# CLI Interface
if __name__ == "__main__":
    # Initialize
    manager = OutputStylesManager()

    print("\n=== Testing Output Styles Manager ===")

    # Test 1: Select style for technical audience
    print("\n1. Technical Audience Context")
    context = StyleContext(
        agent_type="backend-engineer",
        audience="developer",
        task_type="implementation"
    )
    style = manager.select_style(context)
    print(f"Selected style: {style.value}")

    # Test 2: Select style for executive audience
    print("\n2. Executive Audience Context")
    context = StyleContext(
        audience="executive",
        role="manager",
        task_type="status_report"
    )
    style = manager.select_style(context)
    print(f"Selected style: {style.value}")

    # Test 3: Generate style prompt
    print("\n3. Generate Style Prompt for Technical")
    prompt = manager.get_style_prompt(OutputStyle.TECHNICAL)
    print(prompt[:300] + "...")

    # Test 4: Generate context prompt
    print("\n4. Complete Context Prompt")
    context = StyleContext(
        agent_type="qa-engineer",
        task_type="code_review"
    )
    full_prompt = manager.generate_context_prompt(context)
    print(full_prompt[:400] + "...")

    # Test 5: List available styles
    print("\n5. Available Styles")
    styles = manager.list_available_styles()
    print(f"Available: {', '.join(styles)}")

    print("\n=== Output Styles Manager Test Complete ===")
