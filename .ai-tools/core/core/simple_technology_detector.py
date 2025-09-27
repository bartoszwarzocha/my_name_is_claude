#!/usr/bin/env python3
"""
Simplified Technology Detection System
Claude Code Multi-Agent Framework

A lean, reliable technology detection system focused on accuracy over complexity.
Replaces the over-engineered 2,606-line data_collection_system.py with 150 lines.

Version: 2.0.0 - Simplified Architecture
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Set
from dataclasses import dataclass

@dataclass
class TechnologyStack:
    """Simplified technology stack results"""
    languages: List[str]
    frameworks: List[str]
    build_tools: List[str]
    confidence: float

class SimpleTechnologyDetector:
    """Simplified technology detector - accurate and fast"""

    def __init__(self):
        # Core language detection by file extensions
        self.language_extensions = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.tsx': 'TypeScript',
            '.jsx': 'JavaScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.cxx': 'C++',
            '.cc': 'C++',
            '.c': 'C',
            '.h': 'C/C++',
            '.hpp': 'C++',
            '.cs': 'C#',
            '.go': 'Go',
            '.rs': 'Rust',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sass': 'SASS',
            '.vue': 'Vue'
        }

        # Framework detection by configuration files and imports
        self.framework_indicators = {
            'package.json': self._detect_js_frameworks,
            'requirements.txt': self._detect_python_frameworks,
            'Pipfile': self._detect_python_frameworks,
            'pyproject.toml': self._detect_python_frameworks,
            'pom.xml': self._detect_java_frameworks,
            'build.gradle': self._detect_java_frameworks,
            'Cargo.toml': self._detect_rust_frameworks,
            'go.mod': self._detect_go_frameworks,
            'composer.json': self._detect_php_frameworks,
            'Gemfile': self._detect_ruby_frameworks,
            'CMakeLists.txt': self._detect_cmake_frameworks,
            'Makefile': lambda content: ['Make'],
            'vcpkg.json': self._detect_vcpkg_frameworks,
            'conanfile.txt': lambda content: ['Conan']
        }

        # Graphics and OpenGL patterns for content analysis
        self.graphics_patterns = {
            'opengl': ['#include <gl/', '#include <opengl/', 'opengl', 'gl.h', 'glew.h', 'glad.h'],
            'vulkan': ['#include <vulkan/', 'vulkan.h', 'vk_', 'VkDevice', 'VkInstance'],
            'directx': ['#include <d3d', 'd3d11.h', 'd3d12.h', 'directx', 'dxgi.h'],
            'assimp': ['#include <assimp/', 'assimp.h', 'aiScene', 'aiMesh'],
            'glfw': ['#include <glfw/', 'glfw.h', 'glfwInit', 'GLFWwindow'],
            'sdl': ['#include <sdl', 'sdl.h', 'SDL_', 'SDL_Init'],
            'opencv': ['#include <opencv', 'cv::', 'Mat ', 'imread', 'imshow'],
            'wxwidgets': ['#include <wx/', 'wxWidgets', 'wxApp', 'wxFrame', 'wxWindow']
        }

        # Skip these directories to avoid false positives and performance issues
        self.skip_dirs = {
            'node_modules', '__pycache__', 'venv', 'env', '.git',
            'build', 'dist', 'out', 'target', '.next', '.nuxt',
            'docs', 'documentation', 'html', 'vendor', 'third_party',
            # Framework directories (avoid analyzing framework when copied to projects)
            '.ai-tools', '.claude', '.mcp-tools', 'init_concept'
        }

    def detect_technology_stack(self, project_path: str) -> TechnologyStack:
        """
        Detect technology stack with focus on accuracy

        Args:
            project_path: Path to project directory

        Returns:
            TechnologyStack with detected technologies
        """
        languages = set()
        frameworks = set()
        build_tools = set()

        project_path = Path(project_path)

        # 1. Detect languages by file extensions
        for file_path in self._walk_project(project_path):
            ext = file_path.suffix.lower()
            if ext in self.language_extensions:
                languages.add(self.language_extensions[ext])

        # 2. Detect frameworks and build tools by configuration files
        for config_file, detector in self.framework_indicators.items():
            config_path = project_path / config_file
            if config_path.exists():
                try:
                    content = config_path.read_text(encoding='utf-8', errors='ignore')
                    detected = detector(content)
                    frameworks.update(detected)
                    build_tools.add(config_file.split('.')[0].capitalize())
                except Exception:
                    pass  # Skip files we can't read

        # 3. Analyze C++ files for graphics/OpenGL content
        for file_path in self._walk_project(project_path):
            if file_path.suffix.lower() in ['.cpp', '.cxx', '.cc', '.h', '.hpp', '.hxx']:
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore').lower()
                    for graphics_lib, patterns in self.graphics_patterns.items():
                        for pattern in patterns:
                            if pattern.lower() in content:
                                # Use proper capitalization for known graphics libraries
                                proper_name = {
                                    'opengl': 'OpenGL',
                                    'vulkan': 'Vulkan',
                                    'directx': 'DirectX',
                                    'assimp': 'Assimp',
                                    'glfw': 'GLFW',
                                    'sdl': 'SDL',
                                    'opencv': 'OpenCV',
                                    'wxwidgets': 'wxWidgets'
                                }.get(graphics_lib.lower(), graphics_lib.title())
                                frameworks.add(proper_name)
                                break  # Found one pattern, move to next library
                except Exception:
                    pass  # Skip files we can't read

        # 4. Calculate confidence based on detection consistency
        total_files = sum(1 for _ in self._walk_project(project_path))
        confidence = min(1.0, (len(languages) + len(frameworks)) / max(5, total_files * 0.1))

        return TechnologyStack(
            languages=sorted(list(languages)),
            frameworks=sorted(list(frameworks)),
            build_tools=sorted(list(build_tools)),
            confidence=confidence
        )

    def _walk_project(self, project_path: Path):
        """Walk project directory, skipping common ignore directories"""
        import os
        for root, dirs, files in os.walk(project_path):
            # Remove skip directories from dirs list to prevent walking into them
            dirs[:] = [d for d in dirs if d not in self.skip_dirs]

            for file in files:
                yield Path(root) / file

    def _detect_js_frameworks(self, content: str) -> List[str]:
        """Detect JavaScript frameworks from package.json"""
        frameworks = []
        try:
            package = json.loads(content)
            deps = {**package.get('dependencies', {}), **package.get('devDependencies', {})}

            framework_map = {
                'react': 'React', 'next': 'Next.js', 'gatsby': 'Gatsby',
                'vue': 'Vue.js', 'nuxt': 'Nuxt.js', '@angular/core': 'Angular',
                'svelte': 'Svelte', 'sveltekit': 'SvelteKit',
                'express': 'Express.js', 'fastify': 'Fastify', 'koa': 'Koa',
                'nestjs': 'NestJS', 'electron': 'Electron'
            }

            for dep, framework in framework_map.items():
                if any(dep in d for d in deps.keys()):
                    frameworks.append(framework)

        except json.JSONDecodeError:
            pass
        return frameworks

    def _detect_python_frameworks(self, content: str) -> List[str]:
        """Detect Python frameworks from requirements files"""
        frameworks = []

        framework_map = {
            'django': 'Django', 'flask': 'Flask', 'fastapi': 'FastAPI',
            'tornado': 'Tornado', 'pyramid': 'Pyramid', 'bottle': 'Bottle',
            'streamlit': 'Streamlit', 'dash': 'Dash', 'gradio': 'Gradio',
            'tensorflow': 'TensorFlow', 'pytorch': 'PyTorch', 'scikit-learn': 'Scikit-learn',
            'numpy': 'NumPy', 'pandas': 'Pandas', 'matplotlib': 'Matplotlib',
            'opencv': 'OpenCV', 'pillow': 'PIL', 'wxpython': 'wxPython',
            'tkinter': 'Tkinter', 'kivy': 'Kivy', 'pyside': 'PySide'
        }

        content_lower = content.lower()
        for lib, framework in framework_map.items():
            if lib in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_java_frameworks(self, content: str) -> List[str]:
        """Detect Java frameworks from build files"""
        frameworks = []

        framework_indicators = {
            'spring': 'Spring', 'springframework': 'Spring',
            'hibernate': 'Hibernate', 'junit': 'JUnit',
            'maven': 'Maven', 'gradle': 'Gradle'
        }

        content_lower = content.lower()
        for indicator, framework in framework_indicators.items():
            if indicator in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_rust_frameworks(self, content: str) -> List[str]:
        """Detect Rust frameworks from Cargo.toml"""
        frameworks = []

        framework_indicators = {
            'tokio': 'Tokio', 'actix': 'Actix', 'warp': 'Warp',
            'rocket': 'Rocket', 'axum': 'Axum', 'tauri': 'Tauri'
        }

        content_lower = content.lower()
        for indicator, framework in framework_indicators.items():
            if indicator in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_go_frameworks(self, content: str) -> List[str]:
        """Detect Go frameworks from go.mod"""
        frameworks = []

        framework_indicators = {
            'gin': 'Gin', 'echo': 'Echo', 'fiber': 'Fiber',
            'gorilla': 'Gorilla', 'buffalo': 'Buffalo'
        }

        content_lower = content.lower()
        for indicator, framework in framework_indicators.items():
            if indicator in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_php_frameworks(self, content: str) -> List[str]:
        """Detect PHP frameworks from composer.json"""
        frameworks = []
        try:
            composer = json.loads(content)
            deps = {**composer.get('require', {}), **composer.get('require-dev', {})}

            framework_map = {
                'laravel': 'Laravel', 'symfony': 'Symfony', 'codeigniter': 'CodeIgniter',
                'zend': 'Zend', 'cakephp': 'CakePHP', 'yii': 'Yii'
            }

            for dep, framework in framework_map.items():
                if any(dep in d for d in deps.keys()):
                    frameworks.append(framework)

        except json.JSONDecodeError:
            pass
        return frameworks

    def _detect_ruby_frameworks(self, content: str) -> List[str]:
        """Detect Ruby frameworks from Gemfile"""
        frameworks = []

        framework_indicators = {
            'rails': 'Ruby on Rails', 'sinatra': 'Sinatra',
            'hanami': 'Hanami', 'roda': 'Roda'
        }

        content_lower = content.lower()
        for indicator, framework in framework_indicators.items():
            if indicator in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_cmake_frameworks(self, content: str) -> List[str]:
        """Detect graphics and other frameworks from CMakeLists.txt"""
        frameworks = ['CMake']

        framework_indicators = {
            'opengl': 'OpenGL', 'glfw': 'GLFW', 'glew': 'GLEW', 'glad': 'GLAD',
            'vulkan': 'Vulkan', 'assimp': 'Assimp', 'opencv': 'OpenCV',
            'boost': 'Boost', 'eigen': 'Eigen', 'wxwidgets': 'wxWidgets',
            'qt': 'Qt', 'sdl': 'SDL', 'sfml': 'SFML'
        }

        content_lower = content.lower()
        for indicator, framework in framework_indicators.items():
            if indicator in content_lower:
                frameworks.append(framework)

        return frameworks

    def _detect_vcpkg_frameworks(self, content: str) -> List[str]:
        """Detect graphics and other frameworks from vcpkg.json"""
        frameworks = ['vcpkg']
        try:
            import json
            vcpkg_data = json.loads(content)
            dependencies = vcpkg_data.get('dependencies', [])

            framework_map = {
                'opengl': 'OpenGL', 'glfw3': 'GLFW', 'glew': 'GLEW',
                'vulkan': 'Vulkan', 'assimp': 'Assimp', 'opencv': 'OpenCV',
                'boost': 'Boost', 'eigen3': 'Eigen', 'wxwidgets': 'wxWidgets',
                'qt': 'Qt', 'sdl2': 'SDL', 'sfml': 'SFML'
            }

            if isinstance(dependencies, list):
                for dep in dependencies:
                    dep_name = dep if isinstance(dep, str) else dep.get('name', '') if isinstance(dep, dict) else ''
                    for pattern, framework in framework_map.items():
                        if pattern in dep_name.lower():
                            frameworks.append(framework)

        except (json.JSONDecodeError, AttributeError):
            pass
        return frameworks


# Compatibility layer for existing framework wizard
class TechnologyDetector(SimpleTechnologyDetector):
    """Compatibility wrapper for existing code"""

    def detect_technology_stack(self, project_path: str):
        """Return results in format expected by framework wizard"""
        result = super().detect_technology_stack(project_path)

        # Convert to simple string format for framework wizard
        all_technologies = result.languages + result.frameworks + result.build_tools
        return ' '.join(all_technologies).lower().replace(' ', '_').replace('.', '').replace('#', 'sharp')