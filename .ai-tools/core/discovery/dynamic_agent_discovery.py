#!/usr/bin/env python3
"""
Dynamic Agent Discovery System
Claude Code Multi-Agent Framework

Professional dynamic agent discovery system that automatically scans for all agents
(including custom ones) and builds technology mappings from agent metadata.

Version: 3.0.0 - Dynamic Architecture
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass

@dataclass
class AgentMetadata:
    """Comprehensive agent metadata structure"""
    name: str
    description: str
    category: str
    subcategory: str
    agent_type: str
    file_path: str

    # Technology metadata
    technologies: List[str] = None
    domains: List[str] = None
    languages: List[str] = None
    frameworks: List[str] = None
    project_types: List[str] = None
    platforms: List[str] = None
    tools: List[str] = None
    project_scales: List[str] = None
    keywords: List[str] = None

    def __post_init__(self):
        """Initialize empty lists for None values"""
        for field in ['technologies', 'domains', 'languages', 'frameworks',
                      'project_types', 'platforms', 'tools', 'project_scales', 'keywords']:
            if getattr(self, field) is None:
                setattr(self, field, [])

class DynamicAgentDiscovery:
    """Professional dynamic agent discovery system"""

    def __init__(self, agents_root_path: str = ".claude/agents"):
        self.agents_root_path = Path(agents_root_path)
        self.discovered_agents: Dict[str, AgentMetadata] = {}
        self.technology_mapping: Dict[str, List[str]] = {}
        self.domain_mapping: Dict[str, List[str]] = {}

    def scan_agents(self) -> Dict[str, AgentMetadata]:
        """
        Scan agents directory recursively and discover all agent files

        Returns:
            Dictionary of agent_name -> AgentMetadata
        """
        discovered = {}

        if not self.agents_root_path.exists():
            print(f"Warning: Agents directory not found: {self.agents_root_path}")
            return discovered

        # Recursively find all .md files in agents directory
        for agent_file in self.agents_root_path.rglob("*.md"):
            try:
                metadata = self._parse_agent_file(agent_file)
                if metadata:
                    agent_key = self._get_agent_key(agent_file)
                    discovered[agent_key] = metadata

            except Exception as e:
                print(f"Warning: Failed to parse agent file {agent_file}: {e}")
                continue

        self.discovered_agents = discovered
        print(f"✅ Discovered {len(discovered)} agents")
        return discovered

    def _parse_agent_file(self, file_path: Path) -> Optional[AgentMetadata]:
        """
        Parse individual agent file and extract metadata

        Args:
            file_path: Path to agent .md file

        Returns:
            AgentMetadata object or None if parsing fails
        """
        try:
            content = file_path.read_text(encoding='utf-8')

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not yaml_match:
                print(f"Warning: No YAML frontmatter found in {file_path}")
                return None

            yaml_content = yaml_match.group(1)
            metadata_dict = yaml.safe_load(yaml_content)

            if not metadata_dict:
                print(f"Warning: Empty YAML frontmatter in {file_path}")
                return None

            # Extract basic metadata from YAML
            name = metadata_dict.get('name', '')
            description = metadata_dict.get('description', '')
            category = metadata_dict.get('category', '')
            subcategory = metadata_dict.get('subcategory', '')
            agent_type = metadata_dict.get('agent_type', '')

            # Extract Technical Proficiencies from markdown content
            tech_proficiencies = self._extract_technical_proficiencies(content)

            # Create AgentMetadata object
            metadata = AgentMetadata(
                name=name,
                description=description,
                category=category,
                subcategory=subcategory,
                agent_type=agent_type,
                file_path=str(file_path),
                technologies=tech_proficiencies.get('technologies', []),
                domains=tech_proficiencies.get('domains', []),
                languages=tech_proficiencies.get('languages', []),
                frameworks=tech_proficiencies.get('frameworks', []),
                project_types=tech_proficiencies.get('project_types', []),
                platforms=tech_proficiencies.get('platforms', []),
                tools=tech_proficiencies.get('tools', []),
                project_scales=tech_proficiencies.get('project_scales', []),
                keywords=tech_proficiencies.get('keywords', [])
            )

            # If no technology metadata extracted, try to infer from filename and category
            if not any([metadata.technologies, metadata.languages, metadata.frameworks]):
                metadata = self._infer_metadata_from_context(metadata, file_path)

            return metadata

        except Exception as e:
            print(f"Error parsing agent file {file_path}: {e}")
            return None

    def _extract_technical_proficiencies(self, content: str) -> Dict[str, List[str]]:
        """
        Extract Technical Proficiencies from agent markdown content

        Args:
            content: Full markdown content of agent file

        Returns:
            Dictionary with categorized technologies
        """
        # Find Technical Proficiencies section
        tech_prof_pattern = r'\*\*Technical Proficiencies:\*\*(.*?)(?=\n\*\*|\n##|\Z)'
        match = re.search(tech_prof_pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return {'technologies': [], 'languages': [], 'frameworks': [], 'tools': [], 'domains': [], 'project_types': [], 'platforms': [], 'project_scales': [], 'keywords': []}

        tech_section = match.group(1)

        # Extract bullet points
        bullet_pattern = r'^\s*-\s+(.+)$'
        bullets = re.findall(bullet_pattern, tech_section, re.MULTILINE)

        # Parse all technologies from bullet points
        all_technologies = []
        for bullet in bullets:
            # Split by commas and clean up
            techs = [tech.strip() for tech in bullet.split(',')]
            all_technologies.extend(techs)

        # Remove empty strings
        all_technologies = [tech for tech in all_technologies if tech]

        # Categorize technologies
        languages = []
        frameworks = []
        tools = []
        technologies = []

        # Known categorization patterns
        language_patterns = {
            'python', 'javascript', 'typescript', 'java', 'c++', 'c#', 'go', 'rust',
            'c', 'kotlin', 'swift', 'dart', 'scala', 'julia', 'r', 'sql', 'bash',
            'powershell', 'php', 'ruby', 'perl', 'lua', 'haskell', 'ocaml', 'matlab',
            'fortran', 'assembly', 'vhdl', 'verilog', 'glsl', 'hlsl', 'autolisp', 'vba'
        }

        framework_patterns = {
            'react', 'angular', 'vue', 'django', 'flask', 'fastapi', 'express',
            'spring', 'hibernate', 'laravel', 'rails', 'gin', 'echo', 'actix',
            'tokio', 'tensorflow', 'pytorch', 'scikit-learn', 'keras', 'pandas',
            'numpy', 'opencv', 'opengl', 'vulkan', 'directx', 'wxwidgets', 'qt',
            'electron', 'xamarin', 'flutter', 'react native', 'bootstrap', 'tailwind'
        }

        tool_patterns = {
            'docker', 'kubernetes', 'jenkins', 'gitlab ci', 'github actions', 'terraform',
            'ansible', 'puppet', 'chef', 'prometheus', 'grafana', 'elasticsearch', 'kibana',
            'mongodb', 'postgresql', 'mysql', 'redis', 'nginx', 'apache', 'aws', 'azure',
            'gcp', 'heroku', 'vercel', 'netlify', 'jira', 'confluence', 'sonarqube',
            'eslint', 'prettier', 'webpack', 'vite', 'babel', 'jest', 'cypress', 'pytest',
            'maven', 'gradle', 'npm', 'yarn', 'pip', 'cmake', 'visual studio', 'vscode',
            'intellij', 'xcode', 'unity', 'unreal', 'blender', 'photoshop', 'figma',
            'sketch', 'git', 'github', 'gitlab', 'bitbucket', 'svn'
        }

        for tech in all_technologies:
            tech_lower = tech.lower()

            # Check if it's a programming language
            if tech_lower in language_patterns:
                languages.append(tech)
            # Check if it's a framework/library
            elif tech_lower in framework_patterns or any(pattern in tech_lower for pattern in ['framework', 'library', 'api', 'sdk']):
                frameworks.append(tech)
            # Check if it's a tool
            elif tech_lower in tool_patterns or any(pattern in tech_lower for pattern in ['tool', 'ide', 'editor', 'server', 'database', 'cloud']):
                tools.append(tech)
            # Everything else goes to technologies
            else:
                technologies.append(tech)

        # Infer domains from agent specialization
        domains = []
        category_to_domain = {
            'graphics': ['graphics_3d', 'visualization', 'game_development'],
            'desktop': ['desktop_application', 'cross_platform'],
            'web': ['web_development', 'frontend', 'backend'],
            'mobile': ['mobile_development', 'cross_platform'],
            'data': ['data_science', 'analytics', 'machine_learning'],
            'cloud': ['cloud_computing', 'infrastructure'],
            'security': ['security_tools', 'cybersecurity'],
            'enterprise': ['enterprise_software', 'business_applications']
        }

        # Simple domain inference based on technologies found
        for tech in all_technologies:
            tech_lower = tech.lower()
            if 'opengl' in tech_lower or 'vulkan' in tech_lower or '3d' in tech_lower:
                domains.extend(['graphics_3d', 'visualization'])
            elif 'react' in tech_lower or 'angular' in tech_lower or 'vue' in tech_lower:
                domains.extend(['web_development', 'frontend'])
            elif 'docker' in tech_lower or 'kubernetes' in tech_lower or 'aws' in tech_lower:
                domains.extend(['cloud_computing', 'infrastructure'])
            elif 'tensorflow' in tech_lower or 'pytorch' in tech_lower or 'pandas' in tech_lower:
                domains.extend(['data_science', 'machine_learning'])

        # Remove duplicates
        domains = list(set(domains))

        return {
            'technologies': technologies,
            'languages': languages,
            'frameworks': frameworks,
            'tools': tools,
            'domains': domains,
            'project_types': [],  # Could be inferred later if needed
            'platforms': [],      # Could be inferred later if needed
            'project_scales': [], # Could be inferred later if needed
            'keywords': all_technologies  # All technologies as keywords for search
        }

    def _get_agent_key(self, file_path: Path) -> str:
        """Get agent key from file path (filename without extension)"""
        return file_path.stem

    def _infer_metadata_from_context(self, metadata: AgentMetadata, file_path: Path) -> AgentMetadata:
        """
        Infer technology metadata from filename, directory, and description for agents without metadata
        This provides fallback support for agents that haven't been updated yet.
        """
        agent_name = file_path.stem.lower()
        directory_path = str(file_path.parent).lower()
        description = metadata.description.lower()

        # Inference patterns based on agent names and contexts
        inference_patterns = {
            # Programming languages
            'python': (['Python'], ['python'], ['django', 'flask', 'fastapi']),
            'javascript': (['JavaScript', 'Node.js'], ['javascript'], ['express', 'react', 'angular']),
            'java': (['Java'], ['java'], ['spring', 'hibernate']),
            'cpp': (['C++'], ['cpp', 'c'], ['cmake', 'vcpkg']),
            'c#': (['C#'], ['csharp'], ['dotnet', 'asp.net']),
            'go': (['Go'], ['go'], ['gin', 'echo']),
            'rust': (['Rust'], ['rust'], ['actix', 'tokio']),

            # Frontend technologies
            'frontend': (['React', 'Angular', 'Vue.js'], ['javascript', 'typescript'], ['react', 'angular', 'vue']),
            'react': (['React', 'JavaScript'], ['javascript', 'typescript'], ['react', 'next.js']),
            'angular': (['Angular', 'TypeScript'], ['typescript', 'javascript'], ['angular']),
            'vue': (['Vue.js', 'JavaScript'], ['javascript', 'typescript'], ['vue', 'nuxt.js']),

            # Backend technologies
            'backend': (['Python', 'Node.js', 'Java'], ['python', 'javascript', 'java'], ['django', 'express', 'spring']),
            'api': (['REST', 'GraphQL'], ['javascript', 'python'], ['express', 'fastapi']),

            # Graphics and 3D
            'graphics': (['OpenGL', 'Vulkan'], ['cpp', 'c'], ['opengl', 'vulkan']),
            '3d': (['OpenGL', 'Vulkan', 'DirectX'], ['cpp', 'c'], ['opengl', 'vulkan', 'directx']),
            'opengl': (['OpenGL', 'C++'], ['cpp', 'c'], ['opengl', 'glfw']),

            # Desktop applications
            'desktop': (['wxWidgets', 'Qt'], ['cpp', 'c'], ['wxwidgets', 'qt']),
            'qt': (['Qt', 'C++'], ['cpp'], ['qt']),
            'wxwidgets': (['wxWidgets', 'C++'], ['cpp'], ['wxwidgets']),

            # Data and ML
            'data': (['Python', 'SQL'], ['python', 'sql'], ['pandas', 'spark']),
            'ml': (['Python', 'TensorFlow'], ['python'], ['tensorflow', 'pytorch']),
            'ai': (['Python', 'TensorFlow'], ['python'], ['tensorflow', 'pytorch']),

            # Mobile
            'mobile': (['React Native', 'Flutter'], ['javascript', 'dart'], ['react_native', 'flutter']),

            # DevOps and Cloud
            'cloud': (['Docker', 'Kubernetes'], ['yaml'], ['docker', 'kubernetes']),
            'devops': (['Docker', 'Kubernetes'], ['bash', 'yaml'], ['docker', 'kubernetes']),
            'deployment': (['Docker', 'Kubernetes'], ['bash'], ['docker', 'kubernetes']),

            # Security
            'security': (['OAuth', 'JWT'], ['python', 'javascript'], ['oauth', 'jwt']),

            # Performance
            'performance': (['C++', 'Rust'], ['cpp', 'rust'], ['profiling', 'optimization']),
        }

        # Check agent name and description for patterns
        all_text = f"{agent_name} {directory_path} {description}"

        inferred_technologies = []
        inferred_languages = []
        inferred_frameworks = []

        for pattern, (technologies, languages, frameworks) in inference_patterns.items():
            if pattern in all_text:
                inferred_technologies.extend(technologies)
                inferred_languages.extend(languages)
                inferred_frameworks.extend(frameworks)

        # Remove duplicates and update metadata
        if inferred_technologies:
            metadata.technologies = list(set(inferred_technologies))
        if inferred_languages:
            metadata.languages = list(set(inferred_languages))
        if inferred_frameworks:
            metadata.frameworks = list(set(inferred_frameworks))

        # Infer domains based on category and subcategory
        domain_mapping = {
            'graphics': ['graphics_3d', 'visualization'],
            'desktop': ['desktop_application'],
            'development': ['web_development', 'software_development'],
            'data': ['data_science', 'analytics'],
            'enterprise': ['enterprise_software'],
            'mobile': ['mobile_development'],
            'security': ['security_tools'],
            'performance': ['performance_optimization'],
        }

        category_lower = metadata.category.lower()
        for domain_key, domains in domain_mapping.items():
            if domain_key in category_lower or domain_key in all_text:
                metadata.domains.extend(domains)

        metadata.domains = list(set(metadata.domains))

        return metadata

    def build_technology_mapping(self, agents: Optional[Dict[str, AgentMetadata]] = None) -> Dict[str, List[str]]:
        """
        Build technology -> agents mapping from discovered agents

        Args:
            agents: Optional agents dict, uses self.discovered_agents if None

        Returns:
            Dictionary mapping technology -> list of agent names
        """
        if agents is None:
            agents = self.discovered_agents

        mapping = {}

        for agent_key, metadata in agents.items():
            # All technology-related fields to include in mapping
            all_technologies = (
                metadata.technologies +
                metadata.languages +
                metadata.frameworks +
                metadata.tools
            )

            # Add each technology to mapping
            for tech in all_technologies:
                tech_lower = tech.lower()
                if tech_lower not in mapping:
                    mapping[tech_lower] = []
                if agent_key not in mapping[tech_lower]:
                    mapping[tech_lower].append(agent_key)

        self.technology_mapping = mapping
        print(f"✅ Built technology mapping for {len(mapping)} technologies")
        return mapping

    def build_domain_mapping(self, agents: Optional[Dict[str, AgentMetadata]] = None) -> Dict[str, List[str]]:
        """
        Build domain -> agents mapping from discovered agents

        Args:
            agents: Optional agents dict, uses self.discovered_agents if None

        Returns:
            Dictionary mapping domain -> list of agent names
        """
        if agents is None:
            agents = self.discovered_agents

        mapping = {}

        for agent_key, metadata in agents.items():
            for domain in metadata.domains:
                domain_lower = domain.lower()
                if domain_lower not in mapping:
                    mapping[domain_lower] = []
                if agent_key not in mapping[domain_lower]:
                    mapping[domain_lower].append(agent_key)

        self.domain_mapping = mapping
        return mapping

    def get_agents_for_technologies(self, technologies: List[str]) -> List[Tuple[str, List[str]]]:
        """
        Get recommended agents for given technologies with reasoning

        Args:
            technologies: List of technology names

        Returns:
            List of (agent_name, matching_technologies) tuples
        """
        if not self.technology_mapping:
            self.build_technology_mapping()

        agent_scores = {}
        agent_reasoning = {}

        for tech in technologies:
            tech_lower = tech.lower()
            if tech_lower in self.technology_mapping:
                for agent in self.technology_mapping[tech_lower]:
                    agent_scores[agent] = agent_scores.get(agent, 0) + 1
                    if agent not in agent_reasoning:
                        agent_reasoning[agent] = []
                    agent_reasoning[agent].append(tech)

        # Sort agents by relevance score
        sorted_agents = sorted(agent_scores.items(), key=lambda x: x[1], reverse=True)

        # Return with reasoning
        return [(agent, agent_reasoning[agent]) for agent, score in sorted_agents]

    def validate_agents(self) -> Dict[str, List[str]]:
        """
        Validate discovered agents and return validation report

        Returns:
            Dictionary with validation results
        """
        validation_report = {
            'total_agents': len(self.discovered_agents),
            'agents_with_metadata': 0,
            'agents_without_metadata': [],
            'missing_files': [],
            'parsing_errors': []
        }

        for agent_key, metadata in self.discovered_agents.items():
            # Check if agent file exists
            if not Path(metadata.file_path).exists():
                validation_report['missing_files'].append(agent_key)
                continue

            # Check if has technology metadata
            has_metadata = any([
                metadata.technologies,
                metadata.languages,
                metadata.frameworks,
                metadata.domains
            ])

            if has_metadata:
                validation_report['agents_with_metadata'] += 1
            else:
                validation_report['agents_without_metadata'].append(agent_key)

        return validation_report

    def get_discovery_summary(self) -> str:
        """Get formatted summary of discovery results"""
        if not self.discovered_agents:
            return "❌ No agents discovered"

        total = len(self.discovered_agents)
        with_metadata = len([a for a in self.discovered_agents.values()
                           if any([a.technologies, a.languages, a.frameworks])])

        summary = f"""
🤖 Dynamic Agent Discovery Summary:
  Total Agents: {total}
  With Metadata: {with_metadata}
  Without Metadata: {total - with_metadata}
  Technology Mappings: {len(self.technology_mapping)}
  Domain Mappings: {len(self.domain_mapping)}
"""
        return summary


def main():
    """Test the dynamic agent discovery system"""
    print("🚀 Testing Dynamic Agent Discovery System")
    print("=" * 50)

    # Initialize discovery system
    discovery = DynamicAgentDiscovery()

    # Scan for agents
    agents = discovery.scan_agents()

    # Build mappings
    tech_mapping = discovery.build_technology_mapping()
    domain_mapping = discovery.build_domain_mapping()

    # Print summary
    print(discovery.get_discovery_summary())

    # Test technology matching
    print("\n🧪 Testing Technology Matching:")
    test_technologies = ["opengl", "c++", "react", "python"]

    for tech in test_technologies:
        recommendations = discovery.get_agents_for_technologies([tech])
        print(f"\n{tech.upper()}:")
        for agent, reasoning in recommendations[:3]:  # Top 3
            print(f"  → {agent} (because of: {', '.join(reasoning)})")

    # Validation report
    validation = discovery.validate_agents()
    print(f"\n📊 Validation Report:")
    print(f"  Agents with metadata: {validation['agents_with_metadata']}/{validation['total_agents']}")
    if validation['agents_without_metadata']:
        print(f"  Agents needing metadata: {len(validation['agents_without_metadata'])}")


if __name__ == "__main__":
    main()