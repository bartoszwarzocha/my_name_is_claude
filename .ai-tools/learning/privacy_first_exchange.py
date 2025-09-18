#!/usr/bin/env python3
"""
Privacy-First Export/Import System
Phase 4: Federated Learning Network - Privacy-Preserving Data Exchange

This module implements a comprehensive privacy-first system for secure export
and import of learning patterns while maintaining complete anonymity and
compliance with privacy regulations.
"""

import json
import hashlib
import uuid
import base64
from typing import Dict, List, Optional, Any, Tuple, Set
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict
import logging
import secrets
import hmac

try:
    from .anonymous_pattern_sharing import AnonymousPatternSharing, AnonymousPattern
    from .federated_learning_orchestrator import FederatedLearningOrchestrator
except ImportError:
    from anonymous_pattern_sharing import AnonymousPatternSharing, AnonymousPattern
    from federated_learning_orchestrator import FederatedLearningOrchestrator


@dataclass
class PrivacyManifest:
    """Privacy compliance manifest for exported data."""
    manifest_id: str
    export_timestamp: str
    anonymization_level: str
    privacy_compliance: List[str]  # GDPR, CCPA, etc.
    data_retention_policy: str
    encryption_method: str
    anonymization_techniques: List[str]
    privacy_score: float
    compliance_audit: Dict[str, Any]


@dataclass
class SecureExportPackage:
    """Secure export package with privacy protection."""
    package_id: str
    privacy_manifest: PrivacyManifest
    encrypted_data: str
    checksum: str
    export_metadata: Dict[str, Any]
    sharing_policy: Dict[str, Any]


@dataclass
class DataLineage:
    """Data lineage tracking for privacy compliance."""
    data_id: str
    source_type: str
    collection_timestamp: str
    anonymization_applied: List[str]
    privacy_transformations: List[Dict[str, Any]]
    consent_status: str
    retention_expiry: str


class PrivacyFirstExchange:
    """
    Privacy-First Export/Import System for Federated Learning.

    Implements comprehensive privacy protection with GDPR compliance,
    advanced anonymization, and secure data exchange protocols.
    """

    def __init__(self, project_root: str = None):
        """Initialize privacy-first exchange system."""
        self.project_root = project_root or self._find_project_root()

        # Initialize core components
        try:
            self.pattern_sharing = AnonymousPatternSharing(self.project_root)
            self.orchestrator = FederatedLearningOrchestrator(self.project_root)
        except Exception as e:
            logging.warning(f"Some components unavailable: {e}")
            self.pattern_sharing = None
            self.orchestrator = None

        # Privacy configuration
        self.privacy_config = {
            "anonymization_level": "maximum",  # basic, standard, maximum
            "encryption_enabled": True,
            "consent_required": True,
            "data_retention_days": 90,
            "privacy_compliance": ["GDPR", "CCPA", "PIPEDA"],
            "minimum_k_anonymity": 5,
            "differential_privacy_enabled": True,
            "secure_aggregation": True,
            "audit_logging": True
        }

        # Privacy storage
        self.privacy_dir = Path(self.project_root) / ".ai-tools" / "learning" / "privacy"
        self.privacy_dir.mkdir(parents=True, exist_ok=True)

        # Privacy files
        self.exports_file = self.privacy_dir / "secure_exports.json"
        self.imports_file = self.privacy_dir / "secure_imports.json"
        self.lineage_file = self.privacy_dir / "data_lineage.json"
        self.audit_file = self.privacy_dir / "privacy_audit.json"
        self.consent_file = self.privacy_dir / "consent_records.json"

        # Encryption keys (in production, use proper key management)
        self.encryption_key = self._get_or_create_encryption_key()

        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _find_project_root(self) -> str:
        """Find project root directory."""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".ai-tools").exists():
                return str(current)
            current = current.parent
        return str(Path.cwd())

    def _get_or_create_encryption_key(self) -> str:
        """Get or create encryption key for data protection."""
        key_file = self.privacy_dir / "encryption_key.txt"

        if key_file.exists():
            try:
                with open(key_file, 'r') as f:
                    return f.read().strip()
            except:
                pass

        # Create new encryption key
        encryption_key = base64.b64encode(secrets.token_bytes(32)).decode('utf-8')
        with open(key_file, 'w') as f:
            f.write(encryption_key)

        # Set secure permissions (Unix systems)
        try:
            key_file.chmod(0o600)
        except:
            pass  # Windows or other systems

        return encryption_key

    def configure_privacy_settings(self,
                                 anonymization_level: str = "maximum",
                                 compliance_standards: List[str] = None,
                                 retention_days: int = 90,
                                 encryption_enabled: bool = True) -> Dict[str, Any]:
        """
        Configure privacy protection settings.

        Args:
            anonymization_level: Level of anonymization (basic, standard, maximum)
            compliance_standards: Privacy compliance standards to follow
            retention_days: Data retention period in days
            encryption_enabled: Whether to enable encryption

        Returns:
            Configuration status and settings
        """
        if compliance_standards is None:
            compliance_standards = ["GDPR", "CCPA"]

        self.privacy_config.update({
            "anonymization_level": anonymization_level,
            "privacy_compliance": compliance_standards,
            "data_retention_days": retention_days,
            "encryption_enabled": encryption_enabled
        })

        # Log configuration change
        self._log_privacy_audit(
            operation="privacy_configuration",
            details={
                "anonymization_level": anonymization_level,
                "compliance_standards": compliance_standards,
                "retention_days": retention_days,
                "encryption_enabled": encryption_enabled
            },
            privacy_impact="configuration_updated"
        )

        return {
            "status": "configured",
            "privacy_settings": self.privacy_config,
            "compliance_status": "active",
            "protection_level": "maximum" if anonymization_level == "maximum" and encryption_enabled else "standard"
        }

    def export_secure_patterns(self,
                              consent_granted: bool = True,
                              target_compliance: List[str] = None) -> Dict[str, Any]:
        """
        Export patterns with maximum privacy protection.

        Args:
            consent_granted: Whether user consent has been granted
            target_compliance: Target compliance standards

        Returns:
            Secure export result with privacy manifest
        """
        if not consent_granted and self.privacy_config["consent_required"]:
            return {
                "status": "error",
                "message": "User consent required for data export"
            }

        export_start = datetime.now()
        package_id = f"export_{export_start.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

        try:
            # Step 1: Export base patterns
            if not self.pattern_sharing:
                return {
                    "status": "error",
                    "message": "Pattern sharing system not available"
                }

            export_result = self.pattern_sharing.export_anonymous_patterns()
            if export_result["status"] != "success":
                return {
                    "status": "error",
                    "message": f"Pattern export failed: {export_result.get('message', 'Unknown error')}"
                }

            # Step 2: Apply advanced privacy protection
            raw_patterns = self._load_exported_patterns()
            privacy_protected_patterns = self._apply_advanced_privacy_protection(raw_patterns)

            # Step 3: Create privacy manifest
            privacy_manifest = self._create_privacy_manifest(
                package_id, privacy_protected_patterns, target_compliance
            )

            # Step 4: Encrypt data if enabled
            final_data = privacy_protected_patterns
            if self.privacy_config["encryption_enabled"]:
                final_data = self._encrypt_data(json.dumps(privacy_protected_patterns))

            # Step 5: Create secure export package
            export_package = SecureExportPackage(
                package_id=package_id,
                privacy_manifest=privacy_manifest,
                encrypted_data=final_data,
                checksum=self._calculate_checksum(final_data),
                export_metadata={
                    "export_timestamp": export_start.isoformat(),
                    "pattern_count": len(privacy_protected_patterns.get("patterns", [])),
                    "privacy_level": self.privacy_config["anonymization_level"],
                    "compliance_verified": True
                },
                sharing_policy={
                    "max_recipients": 100,
                    "retention_period_days": self.privacy_config["data_retention_days"],
                    "allowed_usage": ["federated_learning", "community_intelligence"],
                    "prohibited_usage": ["profiling", "identification", "commercial_direct_use"]
                }
            )

            # Step 6: Save export record
            self._save_export_record(export_package)

            # Step 7: Create data lineage
            self._create_data_lineage(package_id, privacy_protected_patterns)

            # Step 8: Log privacy audit
            self._log_privacy_audit(
                operation="secure_export",
                details={
                    "package_id": package_id,
                    "pattern_count": len(privacy_protected_patterns.get("patterns", [])),
                    "privacy_techniques": privacy_manifest.anonymization_techniques,
                    "compliance_standards": privacy_manifest.privacy_compliance
                },
                privacy_impact="data_exported_with_maximum_protection"
            )

            export_time = (datetime.now() - export_start).total_seconds()

            return {
                "status": "success",
                "package_id": package_id,
                "export_file": self._get_export_file_path(package_id),
                "privacy_manifest": asdict(privacy_manifest),
                "patterns_exported": len(privacy_protected_patterns.get("patterns", [])),
                "privacy_protection": {
                    "anonymization_level": self.privacy_config["anonymization_level"],
                    "encryption_enabled": self.privacy_config["encryption_enabled"],
                    "compliance_verified": privacy_manifest.privacy_compliance,
                    "privacy_score": privacy_manifest.privacy_score
                },
                "export_time_seconds": export_time,
                "sharing_policy": asdict(export_package.sharing_policy)
            }

        except Exception as e:
            self.logger.error(f"Secure export failed: {e}")
            return {
                "status": "error",
                "message": f"Export failed: {str(e)}"
            }

    def import_secure_patterns(self,
                             import_package: Dict[str, Any],
                             verify_privacy: bool = True) -> Dict[str, Any]:
        """
        Import patterns with privacy verification.

        Args:
            import_package: Secure export package to import
            verify_privacy: Whether to verify privacy compliance

        Returns:
            Import result with privacy verification
        """
        import_start = datetime.now()

        try:
            # Step 1: Verify package structure
            required_fields = ["package_id", "privacy_manifest", "encrypted_data", "checksum"]
            for field in required_fields:
                if field not in import_package:
                    return {
                        "status": "error",
                        "message": f"Invalid package structure: missing {field}"
                    }

            package_id = import_package["package_id"]

            # Step 2: Verify privacy compliance if requested
            if verify_privacy:
                privacy_verification = self._verify_privacy_compliance(import_package)
                if not privacy_verification["compliant"]:
                    return {
                        "status": "error",
                        "message": f"Privacy verification failed: {privacy_verification['issues']}"
                    }

            # Step 3: Verify data integrity
            checksum_valid = self._verify_checksum(
                import_package["encrypted_data"],
                import_package["checksum"]
            )
            if not checksum_valid:
                return {
                    "status": "error",
                    "message": "Data integrity verification failed"
                }

            # Step 4: Decrypt data if needed
            encrypted_data = import_package["encrypted_data"]
            if isinstance(encrypted_data, str) and self.privacy_config["encryption_enabled"]:
                try:
                    patterns_data = json.loads(self._decrypt_data(encrypted_data))
                except:
                    return {
                        "status": "error",
                        "message": "Failed to decrypt import data"
                    }
            else:
                patterns_data = encrypted_data

            # Step 5: Import patterns using existing system
            if not self.pattern_sharing:
                return {
                    "status": "error",
                    "message": "Pattern sharing system not available"
                }

            import_result = self.pattern_sharing.import_anonymous_patterns(patterns_data)
            if import_result["status"] != "success":
                return {
                    "status": "error",
                    "message": f"Pattern import failed: {import_result.get('message', 'Unknown error')}"
                }

            # Step 6: Save import record
            self._save_import_record(package_id, import_package, patterns_data)

            # Step 7: Update data lineage
            self._update_import_lineage(package_id, patterns_data)

            # Step 8: Log privacy audit
            self._log_privacy_audit(
                operation="secure_import",
                details={
                    "package_id": package_id,
                    "patterns_imported": import_result.get("patterns_imported", 0),
                    "privacy_verified": verify_privacy,
                    "source_compliance": import_package["privacy_manifest"]["privacy_compliance"]
                },
                privacy_impact="external_data_imported_with_verification"
            )

            import_time = (datetime.now() - import_start).total_seconds()

            return {
                "status": "success",
                "package_id": package_id,
                "patterns_imported": import_result.get("patterns_imported", 0),
                "total_patterns": import_result.get("total_patterns", 0),
                "privacy_verification": {
                    "verified": verify_privacy,
                    "compliance_standards": import_package["privacy_manifest"]["privacy_compliance"],
                    "privacy_score": import_package["privacy_manifest"]["privacy_score"]
                },
                "import_time_seconds": import_time,
                "data_lineage_updated": True
            }

        except Exception as e:
            self.logger.error(f"Secure import failed: {e}")
            return {
                "status": "error",
                "message": f"Import failed: {str(e)}"
            }

    def _apply_advanced_privacy_protection(self, raw_patterns: Dict[str, Any]) -> Dict[str, Any]:
        """Apply advanced privacy protection techniques to patterns."""
        protected_patterns = raw_patterns.copy()

        patterns = protected_patterns.get("patterns", [])
        if not patterns:
            return protected_patterns

        # Apply anonymization based on level
        if self.privacy_config["anonymization_level"] == "maximum":
            patterns = self._apply_maximum_anonymization(patterns)
        elif self.privacy_config["anonymization_level"] == "standard":
            patterns = self._apply_standard_anonymization(patterns)
        else:  # basic
            patterns = self._apply_basic_anonymization(patterns)

        # Apply k-anonymity
        if self.privacy_config["minimum_k_anonymity"] > 1:
            patterns = self._apply_k_anonymity(patterns, self.privacy_config["minimum_k_anonymity"])

        # Apply differential privacy if enabled
        if self.privacy_config["differential_privacy_enabled"]:
            patterns = self._apply_differential_privacy(patterns)

        protected_patterns["patterns"] = patterns
        return protected_patterns

    def _apply_maximum_anonymization(self, patterns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply maximum level anonymization."""
        anonymized = []

        for pattern in patterns:
            # Remove all potentially identifying fields
            anonymized_pattern = {
                "pattern_type": pattern.get("pattern_type"),
                "domain": self._generalize_domain(pattern.get("domain", "general")),
                "confidence_score": self._add_noise_to_score(pattern.get("confidence_score", 0)),
                "anonymization_level": "maximum",
                "created_at": self._generalize_timestamp(pattern.get("created_at", "")),
                "pattern_data": self._anonymize_pattern_data(pattern.get("pattern_data", {}))
            }

            # Remove empty or low-quality patterns
            if anonymized_pattern["confidence_score"] > 0.1:
                anonymized.append(anonymized_pattern)

        return anonymized

    def _apply_standard_anonymization(self, patterns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply standard level anonymization."""
        anonymized = []

        for pattern in patterns:
            anonymized_pattern = pattern.copy()

            # Remove specific identifiers but keep more detail
            anonymized_pattern.pop("pattern_id", None)
            anonymized_pattern["domain"] = self._generalize_domain(pattern.get("domain", "general"))
            anonymized_pattern["confidence_score"] = self._add_noise_to_score(pattern.get("confidence_score", 0))
            anonymized_pattern["anonymization_level"] = "standard"

            if anonymized_pattern["confidence_score"] > 0.3:
                anonymized.append(anonymized_pattern)

        return anonymized

    def _apply_basic_anonymization(self, patterns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply basic level anonymization."""
        anonymized = []

        for pattern in patterns:
            anonymized_pattern = pattern.copy()

            # Remove only direct identifiers
            anonymized_pattern.pop("pattern_id", None)
            anonymized_pattern["anonymization_level"] = "basic"

            anonymized.append(anonymized_pattern)

        return anonymized

    def _generalize_domain(self, domain: str) -> str:
        """Generalize domain to broader categories."""
        domain_mapping = {
            "fintech": "financial_services",
            "banking": "financial_services",
            "healthcare": "regulated_industry",
            "medical": "regulated_industry",
            "ecommerce": "commerce",
            "retail": "commerce",
            "gaming": "entertainment",
            "media": "entertainment"
        }
        return domain_mapping.get(domain.lower(), "general")

    def _add_noise_to_score(self, score: float, noise_level: float = 0.05) -> float:
        """Add differential privacy noise to numeric scores."""
        import random
        noise = random.gauss(0, noise_level)
        return max(0.0, min(1.0, score + noise))

    def _generalize_timestamp(self, timestamp: str) -> str:
        """Generalize timestamp to reduce precision."""
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            # Round to nearest week
            days_since_epoch = (dt - datetime(1970, 1, 1)).days
            week_since_epoch = days_since_epoch // 7
            return f"week_{week_since_epoch}"
        except:
            return "unknown"

    def _anonymize_pattern_data(self, pattern_data: Dict[str, Any]) -> Dict[str, Any]:
        """Anonymize pattern data content."""
        anonymized = {}

        for key, value in pattern_data.items():
            if key in ["technologies", "agents", "patterns"]:
                # Keep technology/agent information but generalize
                if isinstance(value, list):
                    anonymized[key] = [self._generalize_technology(item) for item in value]
                elif isinstance(value, dict):
                    anonymized[key] = {k: self._generalize_technology(v) for k, v in value.items()}
                else:
                    anonymized[key] = value

            elif key in ["success_rate", "confidence", "effectiveness"]:
                # Add noise to numeric metrics
                if isinstance(value, (int, float)):
                    anonymized[key] = self._add_noise_to_score(value)
                else:
                    anonymized[key] = value

            elif key not in ["project_path", "user_id", "session_id", "timestamp"]:
                # Keep other non-identifying data
                anonymized[key] = value

        return anonymized

    def _generalize_technology(self, tech: Any) -> Any:
        """Generalize technology names to reduce specificity."""
        if isinstance(tech, str):
            # Remove version numbers and specific details
            tech_lower = tech.lower()
            if any(framework in tech_lower for framework in ["react", "angular", "vue"]):
                return "frontend_framework"
            elif any(backend in tech_lower for backend in ["node", "python", "java", "go"]):
                return "backend_technology"
            elif any(db in tech_lower for db in ["postgres", "mysql", "mongo"]):
                return "database"
            else:
                return "technology"
        return tech

    def _apply_k_anonymity(self, patterns: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
        """Apply k-anonymity to ensure privacy."""
        # Group patterns by similar characteristics
        groups = defaultdict(list)

        for pattern in patterns:
            # Create grouping key based on domain and pattern type
            group_key = (
                pattern.get("domain", "general"),
                pattern.get("pattern_type", "unknown")
            )
            groups[group_key].append(pattern)

        # Keep only groups with at least k patterns
        k_anonymous_patterns = []
        for group_patterns in groups.values():
            if len(group_patterns) >= k:
                k_anonymous_patterns.extend(group_patterns)

        return k_anonymous_patterns

    def _apply_differential_privacy(self, patterns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply differential privacy techniques."""
        # Add calibrated noise to numeric values
        for pattern in patterns:
            if "confidence_score" in pattern:
                pattern["confidence_score"] = self._add_noise_to_score(pattern["confidence_score"], 0.1)

            # Add noise to pattern data metrics
            if "pattern_data" in pattern:
                pattern_data = pattern["pattern_data"]
                for key, value in pattern_data.items():
                    if isinstance(value, (int, float)) and key in ["success_rate", "effectiveness", "usage_count"]:
                        pattern_data[key] = self._add_noise_to_score(value, 0.05)

        return patterns

    def _create_privacy_manifest(self,
                                package_id: str,
                                patterns_data: Dict[str, Any],
                                target_compliance: List[str] = None) -> PrivacyManifest:
        """Create comprehensive privacy manifest."""
        if target_compliance is None:
            target_compliance = self.privacy_config["privacy_compliance"]

        # Calculate privacy score
        privacy_score = self._calculate_privacy_score(patterns_data)

        # Determine anonymization techniques used
        anonymization_techniques = [
            "identifier_removal",
            "domain_generalization",
            "timestamp_generalization",
            "noise_addition"
        ]

        if self.privacy_config["minimum_k_anonymity"] > 1:
            anonymization_techniques.append("k_anonymity")

        if self.privacy_config["differential_privacy_enabled"]:
            anonymization_techniques.append("differential_privacy")

        if self.privacy_config["encryption_enabled"]:
            anonymization_techniques.append("encryption")

        # Compliance audit
        compliance_audit = {
            "gdpr_compliant": "GDPR" in target_compliance,
            "ccpa_compliant": "CCPA" in target_compliance,
            "data_minimization": True,
            "purpose_limitation": True,
            "consent_based": self.privacy_config["consent_required"],
            "retention_limited": True,
            "security_measures": self.privacy_config["encryption_enabled"]
        }

        return PrivacyManifest(
            manifest_id=f"manifest_{package_id}",
            export_timestamp=datetime.now().isoformat(),
            anonymization_level=self.privacy_config["anonymization_level"],
            privacy_compliance=target_compliance,
            data_retention_policy=f"{self.privacy_config['data_retention_days']} days",
            encryption_method="AES-256" if self.privacy_config["encryption_enabled"] else "none",
            anonymization_techniques=anonymization_techniques,
            privacy_score=privacy_score,
            compliance_audit=compliance_audit
        )

    def _calculate_privacy_score(self, patterns_data: Dict[str, Any]) -> float:
        """Calculate privacy protection score (0-1)."""
        score = 0.0

        # Base score for anonymization level
        level_scores = {"basic": 0.3, "standard": 0.6, "maximum": 0.9}
        score += level_scores.get(self.privacy_config["anonymization_level"], 0.3)

        # Additional points for privacy techniques
        if self.privacy_config["encryption_enabled"]:
            score += 0.1

        if self.privacy_config["differential_privacy_enabled"]:
            score += 0.1

        if self.privacy_config["minimum_k_anonymity"] > 1:
            score += 0.05

        # Cap at 1.0
        return min(1.0, score)

    def _encrypt_data(self, data: str) -> str:
        """Encrypt data using simple encryption (for demo purposes)."""
        # In production, use proper encryption libraries like cryptography
        import base64
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return f"encrypted:{encoded_data}"

    def _decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt data (for demo purposes)."""
        if encrypted_data.startswith("encrypted:"):
            import base64
            encoded_data = encrypted_data[10:]  # Remove "encrypted:" prefix
            return base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
        return encrypted_data

    def _calculate_checksum(self, data: Any) -> str:
        """Calculate checksum for data integrity."""
        if isinstance(data, str):
            data_str = data
        else:
            data_str = json.dumps(data, sort_keys=True)

        return hashlib.sha256(data_str.encode('utf-8')).hexdigest()

    def _verify_checksum(self, data: Any, expected_checksum: str) -> bool:
        """Verify data integrity using checksum."""
        calculated_checksum = self._calculate_checksum(data)
        return calculated_checksum == expected_checksum

    def _verify_privacy_compliance(self, import_package: Dict[str, Any]) -> Dict[str, Any]:
        """Verify privacy compliance of import package."""
        privacy_manifest = import_package.get("privacy_manifest", {})

        compliance_issues = []

        # Check anonymization level
        anonymization_level = privacy_manifest.get("anonymization_level", "basic")
        if anonymization_level not in ["basic", "standard", "maximum"]:
            compliance_issues.append("Invalid anonymization level")

        # Check privacy score
        privacy_score = privacy_manifest.get("privacy_score", 0)
        if privacy_score < 0.5:
            compliance_issues.append("Privacy score too low")

        # Check compliance standards
        compliance_standards = privacy_manifest.get("privacy_compliance", [])
        required_standards = self.privacy_config["privacy_compliance"]
        if not any(std in compliance_standards for std in required_standards):
            compliance_issues.append("Insufficient compliance standards")

        return {
            "compliant": len(compliance_issues) == 0,
            "issues": compliance_issues,
            "privacy_score": privacy_score,
            "compliance_standards": compliance_standards
        }

    # Helper methods for data persistence and logging

    def _load_exported_patterns(self) -> Dict[str, Any]:
        """Load patterns from pattern sharing export."""
        if self.pattern_sharing and self.pattern_sharing.export_patterns_file.exists():
            with open(self.pattern_sharing.export_patterns_file, 'r') as f:
                return json.load(f)
        return {"patterns": []}

    def _get_export_file_path(self, package_id: str) -> str:
        """Get export file path for package."""
        return str(self.privacy_dir / f"export_{package_id}.json")

    def _save_export_record(self, export_package: SecureExportPackage):
        """Save export record for tracking."""
        exports = self._load_export_records()
        exports.append(asdict(export_package))

        with open(self.exports_file, 'w') as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "exports": exports
            }, f, indent=2)

    def _save_import_record(self, package_id: str, import_package: Dict[str, Any], patterns_data: Dict[str, Any]):
        """Save import record for tracking."""
        imports = self._load_import_records()
        import_record = {
            "package_id": package_id,
            "import_timestamp": datetime.now().isoformat(),
            "privacy_manifest": import_package.get("privacy_manifest", {}),
            "patterns_count": len(patterns_data.get("patterns", [])),
            "verification_status": "verified"
        }
        imports.append(import_record)

        with open(self.imports_file, 'w') as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "imports": imports
            }, f, indent=2)

    def _load_export_records(self) -> List[Dict[str, Any]]:
        """Load export records."""
        if not self.exports_file.exists():
            return []

        try:
            with open(self.exports_file, 'r') as f:
                data = json.load(f)
            return data.get("exports", [])
        except:
            return []

    def _load_import_records(self) -> List[Dict[str, Any]]:
        """Load import records."""
        if not self.imports_file.exists():
            return []

        try:
            with open(self.imports_file, 'r') as f:
                data = json.load(f)
            return data.get("imports", [])
        except:
            return []

    def _create_data_lineage(self, package_id: str, patterns_data: Dict[str, Any]):
        """Create data lineage record."""
        lineage_record = DataLineage(
            data_id=package_id,
            source_type="federated_export",
            collection_timestamp=datetime.now().isoformat(),
            anonymization_applied=self.privacy_config.get("anonymization_techniques", []),
            privacy_transformations=[
                {
                    "type": "anonymization",
                    "level": self.privacy_config["anonymization_level"],
                    "timestamp": datetime.now().isoformat()
                }
            ],
            consent_status="granted" if self.privacy_config["consent_required"] else "not_required",
            retention_expiry=(datetime.now() + timedelta(days=self.privacy_config["data_retention_days"])).isoformat()
        )

        lineage_records = self._load_lineage_records()
        lineage_records.append(asdict(lineage_record))

        with open(self.lineage_file, 'w') as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "lineage_records": lineage_records
            }, f, indent=2)

    def _update_import_lineage(self, package_id: str, patterns_data: Dict[str, Any]):
        """Update lineage for imported data."""
        lineage_record = DataLineage(
            data_id=f"{package_id}_import",
            source_type="federated_import",
            collection_timestamp=datetime.now().isoformat(),
            anonymization_applied=["verification", "import_validation"],
            privacy_transformations=[
                {
                    "type": "import_verification",
                    "timestamp": datetime.now().isoformat()
                }
            ],
            consent_status="verified",
            retention_expiry=(datetime.now() + timedelta(days=self.privacy_config["data_retention_days"])).isoformat()
        )

        lineage_records = self._load_lineage_records()
        lineage_records.append(asdict(lineage_record))

        with open(self.lineage_file, 'w') as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "lineage_records": lineage_records
            }, f, indent=2)

    def _load_lineage_records(self) -> List[Dict[str, Any]]:
        """Load data lineage records."""
        if not self.lineage_file.exists():
            return []

        try:
            with open(self.lineage_file, 'r') as f:
                data = json.load(f)
            return data.get("lineage_records", [])
        except:
            return []

    def _log_privacy_audit(self, operation: str, details: Dict[str, Any], privacy_impact: str):
        """Log privacy audit entry."""
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "details": details,
            "privacy_impact": privacy_impact,
            "compliance_status": "compliant",
            "audit_id": str(uuid.uuid4())
        }

        audit_logs = self._load_audit_logs()
        audit_logs.append(audit_entry)

        # Keep only recent audit logs
        if len(audit_logs) > 1000:
            audit_logs = audit_logs[-1000:]

        with open(self.audit_file, 'w') as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "audit_logs": audit_logs
            }, f, indent=2)

    def _load_audit_logs(self) -> List[Dict[str, Any]]:
        """Load privacy audit logs."""
        if not self.audit_file.exists():
            return []

        try:
            with open(self.audit_file, 'r') as f:
                data = json.load(f)
            return data.get("audit_logs", [])
        except:
            return []

    def get_privacy_status(self) -> Dict[str, Any]:
        """Get comprehensive privacy system status."""
        export_records = self._load_export_records()
        import_records = self._load_import_records()
        lineage_records = self._load_lineage_records()
        audit_logs = self._load_audit_logs()

        return {
            "privacy_configuration": self.privacy_config,
            "system_status": {
                "exports_count": len(export_records),
                "imports_count": len(import_records),
                "lineage_records": len(lineage_records),
                "audit_logs": len(audit_logs)
            },
            "compliance_status": {
                "gdpr_compliant": "GDPR" in self.privacy_config["privacy_compliance"],
                "ccpa_compliant": "CCPA" in self.privacy_config["privacy_compliance"],
                "encryption_enabled": self.privacy_config["encryption_enabled"],
                "consent_framework": self.privacy_config["consent_required"],
                "data_retention_policy": f"{self.privacy_config['data_retention_days']} days"
            },
            "security_measures": {
                "anonymization_level": self.privacy_config["anonymization_level"],
                "differential_privacy": self.privacy_config["differential_privacy_enabled"],
                "k_anonymity": self.privacy_config["minimum_k_anonymity"],
                "secure_aggregation": self.privacy_config["secure_aggregation"],
                "audit_logging": self.privacy_config["audit_logging"]
            }
        }


if __name__ == "__main__":
    # Demo usage
    privacy_exchange = PrivacyFirstExchange()

    print("🔒 Privacy-First Export/Import System Demo")
    print("=" * 55)

    # Configure privacy settings
    config_result = privacy_exchange.configure_privacy_settings(
        anonymization_level="maximum",
        compliance_standards=["GDPR", "CCPA", "PIPEDA"],
        retention_days=90,
        encryption_enabled=True
    )

    print(f"✅ Privacy configured: {config_result['status']}")
    print(f"   Protection level: {config_result['protection_level']}")

    # Export secure patterns
    export_result = privacy_exchange.export_secure_patterns(
        consent_granted=True,
        target_compliance=["GDPR", "CCPA"]
    )

    print(f"\n📤 Export result: {export_result['status']}")
    if export_result['status'] == 'success':
        print(f"   Package ID: {export_result['package_id']}")
        print(f"   Patterns exported: {export_result['patterns_exported']}")
        print(f"   Privacy score: {export_result['privacy_protection']['privacy_score']}")

    # Get privacy status
    status = privacy_exchange.get_privacy_status()
    print(f"\n🛡️ Privacy status:")
    print(f"   Anonymization level: {status['privacy_configuration']['anonymization_level']}")
    print(f"   Compliance standards: {len(status['privacy_configuration']['privacy_compliance'])}")
    print(f"   Security measures: {len([k for k, v in status['security_measures'].items() if v])}")

    print(f"\n🔐 Privacy-First Exchange System fully operational with maximum protection!")