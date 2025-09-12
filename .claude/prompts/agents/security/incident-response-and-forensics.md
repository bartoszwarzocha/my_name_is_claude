# Incident Response and Digital Forensics

**Agent: security-engineer**
**Purpose: Lead comprehensive incident response operations and conduct digital forensics investigations with technology-adaptive response strategies**

---

## Context Analysis

The security-engineer will analyze the CLAUDE.md file to determine:
- **Technology Infrastructure**: System architecture (cloud, on-premise, hybrid) and technology stack for appropriate forensic tools and investigation techniques
- **Business Domain**: Industry-specific incident types, regulatory requirements, and compliance obligations for response procedures
- **Project Scale**: Infrastructure complexity and user base size for incident classification and resource allocation
- **Security Maturity**: Existing security tools and monitoring capabilities for evidence collection and analysis
- **Regulatory Environment**: Compliance requirements (GDPR, HIPAA, PCI-DSS) for breach notification timelines and forensic standards

Based on this analysis, the security engineer will customize incident response procedures, select appropriate forensic tools, and ensure compliance with regulatory requirements throughout the investigation process.

## 🎯 Mission

Lead comprehensive incident response operations and conduct digital forensics investigations to contain security incidents, preserve evidence, determine root causes, and implement preventive measures while maintaining business continuity.

## 📋 Process Framework

### Phase 1: Incident Detection and Initial Response (0-1 hour)

**Step 1.1: Incident Classification and Triage**

```python
# Incident Classification System
INCIDENT_SEVERITY_MATRIX = {
    'P0_CRITICAL': {
        'description': 'Active attack, data breach, or system compromise in progress',
        'response_time': '15_minutes',
        'escalation': 'immediate_ciso_ceo',
        'team_activation': 'full_incident_response_team',
        'external_notification': 'legal_regulatory_customers'
    },
    'P1_HIGH': {
        'description': 'Security control failure, unauthorized access attempt',
        'response_time': '1_hour',
        'escalation': 'security_manager_within_30min',
        'team_activation': 'core_security_team',
        'external_notification': 'legal_if_data_involved'
    },
    'P2_MEDIUM': {
        'description': 'Policy violation, suspicious activity, or minor vulnerability',
        'response_time': '4_hours',
        'escalation': 'team_lead_within_2hours',
        'team_activation': 'assigned_security_engineer',
        'external_notification': 'none_unless_escalated'
    },
    'P3_LOW': {
        'description': 'Security awareness issue or non-critical finding',
        'response_time': '24_hours',
        'escalation': 'daily_security_standup',
        'team_activation': 'individual_assignment',
        'external_notification': 'none'
    }
}

class IncidentResponseCoordinator:
    def __init__(self, incident_data):
        self.incident = incident_data
        self.timeline = []
        self.evidence_chain = []
        
    def classify_incident(self):
        """Rapidly classify incident severity and determine response level"""
        classification_criteria = {
            'data_exposure_confirmed': self._assess_data_exposure(),
            'system_compromise_indicators': self._assess_system_compromise(),
            'business_impact_level': self._assess_business_impact(),
            'attack_sophistication': self._assess_attack_sophistication(),
            'affected_systems_criticality': self._assess_system_criticality()
        }
        
        severity_score = self._calculate_severity_score(classification_criteria)
        incident_type = self._determine_incident_type()
        
        return {
            'severity': self._map_score_to_severity(severity_score),
            'type': incident_type,
            'response_level': self._determine_response_level(severity_score),
            'notification_requirements': self._determine_notifications(incident_type),
            'estimated_investigation_complexity': self._estimate_complexity()
        }
    
    def _assess_data_exposure(self):
        """Assess potential or confirmed data exposure"""
        indicators = {
            'database_access_anomalies': self._check_database_logs(),
            'file_system_modifications': self._check_file_integrity(),
            'network_data_exfiltration': self._check_network_flows(),
            'user_data_access_patterns': self._check_access_patterns(),
            'backup_integrity_status': self._check_backup_systems()
        }
        
        exposure_score = sum([
            indicators['database_access_anomalies'] * 3,
            indicators['file_system_modifications'] * 2,
            indicators['network_data_exfiltration'] * 4,
            indicators['user_data_access_patterns'] * 2,
            indicators['backup_integrity_status'] * 1
        ])
        
        return min(exposure_score, 10)  # Cap at 10
    
    def initiate_emergency_response(self):
        """Execute immediate containment and preservation actions"""
        response_actions = {
            'immediate_containment': [
                'Isolate affected systems from network',
                'Preserve system state for forensics',
                'Block suspicious network traffic',
                'Disable compromised user accounts',
                'Activate incident command center'
            ],
            'evidence_preservation': [
                'Create forensic images of affected systems',
                'Preserve network logs and traffic captures',
                'Document all observations and actions',
                'Secure physical access to systems',
                'Implement legal hold on relevant data'
            ],
            'stakeholder_notification': [
                'Notify incident response team',
                'Alert executive management',
                'Prepare customer communications',
                'Contact legal counsel',
                'Coordinate with external forensics firm'
            ]
        }
        
        return response_actions
```

**Step 1.2: Evidence Preservation and Chain of Custody**

```python
class ForensicsEvidenceManager:
    def __init__(self, incident_id):
        self.incident_id = incident_id
        self.evidence_catalog = {}
        self.chain_of_custody = []
        
    def create_forensic_images(self):
        """Create bit-for-bit forensic images of affected systems"""
        imaging_procedures = {
            'live_system_imaging': {
                'tools': ['FTK_Imager', 'dd', 'LinEn'],
                'priority_order': ['memory_dump', 'running_processes', 'network_connections'],
                'preservation_method': 'write_blocked_acquisition',
                'verification': 'cryptographic_hash_validation'
            },
            'storage_device_imaging': {
                'tools': ['Cellebrite', 'X1_Social_Discovery', 'EnCase'],
                'imaging_method': 'physical_bit_stream_copy',
                'verification': 'md5_sha1_sha256_hashes',
                'storage': 'encrypted_evidence_storage_system'
            },
            'cloud_evidence_collection': {
                'tools': ['Cloud_Trail_logs', 'Azure_Activity_logs', 'GCP_Audit_logs'],
                'collection_method': 'api_based_automated_collection',
                'preservation': 'immutable_evidence_vault',
                'legal_hold': 'litigation_hold_implementation'
            }
        }
        
        return imaging_procedures
    
    def establish_chain_of_custody(self):
        """Establish and maintain legal chain of custody for all evidence"""
        custody_procedures = {
            'evidence_handling_protocol': {
                'acquisition': {
                    'timestamp': 'ntp_synchronized_utc',
                    'acquiring_examiner': 'certified_forensics_professional',
                    'witness': 'secondary_team_member',
                    'documentation': 'detailed_acquisition_log',
                    'integrity_verification': 'cryptographic_hash_calculation'
                },
                'transfer': {
                    'authorization': 'incident_commander_approval',
                    'receiving_party': 'authorized_personnel_only',
                    'transfer_log': 'detailed_custody_transfer_form',
                    'integrity_check': 'hash_verification_pre_post_transfer',
                    'secure_transport': 'encrypted_tamper_evident_containers'
                },
                'storage': {
                    'facility': 'certified_evidence_storage_facility',
                    'access_control': 'dual_person_integrity_required',
                    'environmental_control': 'temperature_humidity_monitored',
                    'backup': 'geographically_distributed_copies',
                    'retention': 'legal_hold_plus_7_years'
                }
            }
        }
        
        return custody_procedures
        
    def create_evidence_timeline(self):
        """Create comprehensive timeline of events and evidence"""
        timeline_construction = {
            'data_sources': [
                'system_event_logs',
                'application_logs', 
                'network_flow_records',
                'database_transaction_logs',
                'security_tool_alerts',
                'user_authentication_logs',
                'file_system_metadata',
                'registry_modifications',
                'memory_artifacts',
                'network_packet_captures'
            ],
            'timeline_analysis_tools': [
                'Plaso/log2timeline',
                'Volatility_Framework',
                'Autopsy',
                'SIFT_Workstation',
                'TimeSketch'
            ],
            'correlation_techniques': [
                'timestamp_normalization_to_utc',
                'cross_reference_user_activities',
                'map_network_communications',
                'correlate_with_threat_intelligence',
                'identify_persistence_mechanisms'
            ]
        }
        
        return timeline_construction
```

### Phase 2: Deep Forensic Investigation (4-12 hours)

**Step 2.1: System and Network Forensics**

```python
class DeepForensicAnalysis:
    def __init__(self, evidence_collection, incident_context):
        self.evidence = evidence_collection
        self.context = incident_context
        
    def conduct_memory_forensics(self):
        """Perform comprehensive memory analysis for volatile artifacts"""
        memory_analysis = {
            'process_analysis': {
                'running_processes': 'volatility_pslist_psscan',
                'hidden_processes': 'volatility_psxview_detect_evasion',
                'process_relationships': 'volatility_pstree_parent_child',
                'malicious_processes': 'volatility_malfind_injected_code',
                'network_connections': 'volatility_netscan_active_connections'
            },
            'malware_detection': {
                'code_injection': 'volatility_malfind_hollowing_detection',
                'rootkit_detection': 'volatility_modscan_hidden_modules',
                'persistence_mechanisms': 'volatility_registry_services_analysis',
                'command_history': 'volatility_cmdline_console_history',
                'api_hooks': 'volatility_apihooks_inline_hooks'
            },
            'credential_extraction': {
                'cached_passwords': 'volatility_hashdump_lsa_secrets',
                'kerberos_tickets': 'volatility_kdbgscan_ticket_extraction',
                'browser_credentials': 'volatility_iehistory_chrome_analysis',
                'private_keys': 'volatility_filescan_key_material',
                'recent_documents': 'volatility_mftparser_file_access'
            }
        }
        
        return memory_analysis
    
    def analyze_file_system_artifacts(self):
        """Comprehensive file system and registry analysis"""
        file_system_analysis = {
            'master_file_table_analysis': {
                'deleted_files': 'mft_parser_unallocated_entries',
                'timestamp_analysis': 'mft_timeline_reconstruction',
                'file_relationships': 'mft_parent_directory_mapping',
                'alternate_data_streams': 'mft_ads_hidden_content',
                'volume_shadow_copies': 'vss_historical_file_versions'
            },
            'registry_forensics': {
                'user_activity': 'ntuser_dat_recent_documents_programs',
                'system_configuration': 'system_hive_services_drivers',
                'installed_software': 'software_hive_applications_versions',
                'network_settings': 'system_hive_network_configuration',
                'autostart_locations': 'all_hives_persistence_mechanisms'
            },
            'browser_forensics': {
                'browsing_history': 'sqlite_history_databases',
                'download_history': 'browser_download_records',
                'cookies_sessions': 'browser_authentication_tokens',
                'cached_files': 'browser_cache_directory_analysis',
                'bookmarks_searches': 'browser_user_interest_profiling'
            }
        }
        
        return file_system_analysis
    
    def perform_network_forensics(self):
        """Deep network traffic and communication analysis"""
        network_analysis = {
            'packet_analysis': {
                'protocol_analysis': 'wireshark_protocol_hierarchy_statistics',
                'conversation_analysis': 'wireshark_endpoints_communications',
                'suspicious_traffic': 'wireshark_expert_info_anomalies',
                'file_transfers': 'wireshark_http_ftp_smb_extractions',
                'encrypted_traffic': 'wireshark_tls_ssl_certificate_analysis'
            },
            'flow_analysis': {
                'netflow_analysis': 'nfcapd_long_duration_connections',
                'bandwidth_analysis': 'nfcapd_unusual_volume_patterns',
                'geographic_analysis': 'geoip_foreign_country_communications',
                'temporal_analysis': 'nfcapd_off_hours_activity_patterns',
                'protocol_anomalies': 'nfcapd_unusual_port_protocol_usage'
            },
            'dns_analysis': {
                'dns_queries': 'dns_logs_domain_name_requests',
                'malicious_domains': 'threat_intelligence_ioc_correlation',
                'dns_tunneling': 'dns_query_size_frequency_analysis',
                'fast_flux_detection': 'dns_rapid_ip_address_changes',
                'dga_detection': 'dns_algorithmic_domain_patterns'
            }
        }
        
        return network_analysis
```

**Step 2.2: Malware Analysis and Attribution**

```python
class MalwareAnalysisFramework:
    def __init__(self, sample_collection):
        self.samples = sample_collection
        self.analysis_environment = self._setup_sandbox()
        
    def static_malware_analysis(self):
        """Comprehensive static analysis without execution"""
        static_analysis = {
            'file_characteristics': {
                'file_type_identification': 'file_utility_magic_numbers',
                'hash_calculations': 'md5_sha1_sha256_ssdeep_fuzzy',
                'digital_signatures': 'signtool_certificate_validation',
                'packer_detection': 'peid_detect_it_easy_upx_detection',
                'entropy_analysis': 'binwalk_entropy_visualization'
            },
            'portable_executable_analysis': {
                'pe_header_analysis': 'pefile_import_export_tables',
                'section_analysis': 'pefile_suspicious_section_characteristics',
                'import_analysis': 'pefile_api_usage_patterns',
                'resource_analysis': 'pefile_embedded_resources_strings',
                'overlay_analysis': 'pefile_data_appended_to_executable'
            },
            'string_analysis': {
                'ascii_unicode_strings': 'strings_utility_readable_text',
                'url_ip_extraction': 'regex_network_indicators',
                'cryptographic_constants': 'yara_crypto_signature_detection',
                'api_function_names': 'pefile_import_table_analysis',
                'debug_information': 'pefile_pdb_paths_compilation_info'
            }
        }
        
        return static_analysis
    
    def dynamic_malware_analysis(self):
        """Controlled dynamic analysis in isolated environment"""
        dynamic_analysis = {
            'sandbox_execution': {
                'virtual_environment': 'vmware_virtualbox_isolated_network',
                'monitoring_tools': 'procmon_wireshark_regshot',
                'execution_timeout': '15_minutes_maximum_runtime',
                'snapshot_restoration': 'clean_state_between_executions',
                'network_simulation': 'inetsim_fakenet_dns_http_servers'
            },
            'behavioral_analysis': {
                'file_system_changes': 'procmon_file_creation_modification_deletion',
                'registry_modifications': 'procmon_registry_key_value_changes',
                'network_communications': 'wireshark_tcp_udp_icmp_traffic',
                'process_creation': 'procmon_child_process_spawning',
                'service_installation': 'sc_query_new_services_creation'
            },
            'evasion_detection': {
                'anti_vm_techniques': 'pafish_vm_detection_evasion_checks',
                'anti_debug_techniques': 'ollydbg_ida_debugger_detection',
                'sandbox_evasion': 'sleep_delays_user_interaction_checks',
                'packing_obfuscation': 'upx_themida_vmprotect_unpacking',
                'encryption_decryption': 'string_decryption_runtime_analysis'
            }
        }
        
        return dynamic_analysis
    
    def threat_attribution_analysis(self):
        """Link attack to known threat groups and campaigns"""
        attribution_analysis = {
            'ttps_mapping': {
                'mitre_att_ck_mapping': 'map_observed_techniques_to_framework',
                'tool_usage_patterns': 'correlate_tools_with_apt_groups',
                'infrastructure_overlap': 'compare_c2_domains_ips_with_intel',
                'timing_patterns': 'analyze_campaign_timing_working_hours',
                'target_selection': 'correlate_victim_profile_with_groups'
            },
            'malware_family_identification': {
                'yara_rule_matching': 'custom_commercial_yara_rule_sets',
                'similarity_analysis': 'ssdeep_imphash_similarity_scoring',
                'behavior_clustering': 'machine_learning_behavior_classification',
                'code_reuse_analysis': 'bindiff_ida_code_comparison',
                'evolution_tracking': 'malware_family_version_progression'
            },
            'threat_intelligence_correlation': {
                'ioc_matching': 'correlate_with_commercial_threat_feeds',
                'campaign_tracking': 'link_to_known_threat_campaigns',
                'geopolitical_context': 'correlate_with_current_events_tensions',
                'victim_analysis': 'analyze_other_victims_same_campaign',
                'motivation_assessment': 'determine_financial_espionage_sabotage'
            }
        }
        
        return attribution_analysis
```

### Phase 3: Impact Assessment and Containment (2-4 hours)

**Step 3.1: Comprehensive Impact Analysis**

```python
class IncidentImpactAssessment:
    def __init__(self, forensic_findings, business_context):
        self.findings = forensic_findings
        self.business_context = business_context
        
    def assess_data_compromise(self):
        """Determine extent and nature of data compromise"""
        data_assessment = {
            'compromised_data_inventory': {
                'personal_data': {
                    'types': ['pii', 'phi', 'financial_data', 'biometric_data'],
                    'volume': 'record_count_affected_individuals',
                    'sensitivity': 'gdpr_ccpa_hipaa_classification',
                    'geographic_scope': 'data_subject_jurisdictions',
                    'retention_period': 'how_long_data_retained'
                },
                'business_data': {
                    'types': ['intellectual_property', 'trade_secrets', 'financial_records'],
                    'competitive_value': 'business_impact_if_disclosed',
                    'legal_obligations': 'contractual_regulatory_requirements',
                    'recovery_complexity': 'effort_required_to_recreate',
                    'business_continuity_impact': 'operational_disruption_level'
                },
                'system_data': {
                    'types': ['credentials', 'certificates', 'configuration_data'],
                    'security_impact': 'compromise_propagation_potential',
                    'remediation_scope': 'systems_requiring_reconfiguration',
                    'downtime_requirements': 'maintenance_windows_needed',
                    'trust_relationship_impact': 'partners_customers_affected'
                }
            },
            'compromise_timeline_analysis': {
                'initial_compromise_date': 'earliest_evidence_of_intrusion',
                'data_access_timeline': 'when_sensitive_data_first_accessed',
                'exfiltration_timeline': 'evidence_of_data_leaving_network',
                'discovery_date': 'when_organization_became_aware',
                'notification_requirements': 'regulatory_deadline_calculations'
            }
        }
        
        return data_assessment
    
    def calculate_business_impact(self):
        """Quantify financial and operational business impact"""
        business_impact = {
            'direct_financial_costs': {
                'incident_response_costs': {
                    'internal_team_time': 'hours_x_hourly_rates',
                    'external_consultants': 'forensics_legal_pr_firm_costs',
                    'technology_costs': 'tools_infrastructure_replacement',
                    'regulatory_fines': 'estimated_potential_penalties',
                    'legal_settlements': 'estimated_litigation_costs'
                },
                'business_disruption_costs': {
                    'system_downtime': 'revenue_per_hour_x_downtime_hours',
                    'productivity_loss': 'affected_employees_x_hours_x_rates',
                    'customer_impact': 'lost_revenue_customer_churn',
                    'partner_impact': 'supply_chain_disruption_costs',
                    'recovery_costs': 'system_rebuild_data_recovery_costs'
                }
            },
            'indirect_business_impact': {
                'reputation_damage': {
                    'customer_confidence_loss': 'survey_data_customer_retention_metrics',
                    'brand_value_impact': 'marketing_required_to_restore_trust',
                    'competitive_disadvantage': 'market_share_loss_projections',
                    'employee_morale': 'hr_impact_retention_recruitment',
                    'investor_confidence': 'stock_price_impact_if_public'
                },
                'long_term_consequences': {
                    'regulatory_scrutiny': 'increased_audit_compliance_costs',
                    'insurance_implications': 'premium_increases_coverage_changes',
                    'contract_implications': 'customer_contract_renegotiations',
                    'market_position': 'competitive_positioning_changes',
                    'strategic_initiatives': 'delayed_projects_opportunity_costs'
                }
            }
        }
        
        return business_impact
```

**Step 3.2: Advanced Containment and Eradication**

```python
class AdvancedContainmentStrategy:
    def __init__(self, threat_profile, network_topology):
        self.threat = threat_profile
        self.network = network_topology
        
    def implement_surgical_containment(self):
        """Implement precise containment minimizing business disruption"""
        containment_strategy = {
            'network_segmentation': {
                'micro_segmentation': {
                    'implementation': 'zero_trust_network_access_ztna',
                    'granularity': 'application_level_access_control',
                    'monitoring': 'east_west_traffic_inspection',
                    'enforcement': 'software_defined_perimeter_sdp'
                },
                'lateral_movement_prevention': {
                    'privileged_access': 'pam_solution_jump_box_isolation',
                    'service_accounts': 'managed_service_identity_rotation',
                    'network_traffic': 'firewall_rules_traffic_blocking',
                    'authentication': 'mfa_enforcement_conditional_access'
                }
            },
            'endpoint_isolation': {
                'selective_isolation': {
                    'criteria': 'ioc_behavioral_analysis_risk_scoring',
                    'methods': 'network_acl_host_firewall_vpn_revocation',
                    'communication': 'out_of_band_management_interface',
                    'monitoring': 'continuous_endpoint_telemetry'
                },
                'forensic_preservation': {
                    'live_response': 'remote_forensic_toolkit_deployment',
                    'data_collection': 'memory_dump_triage_package_creation',
                    'state_preservation': 'vm_snapshot_disk_image_creation',
                    'chain_of_custody': 'automated_evidence_documentation'
                }
            },
            'threat_neutralization': {
                'malware_removal': {
                    'detection_engines': 'multiple_av_edr_yara_rule_scanning',
                    'removal_techniques': 'safe_mode_boot_offline_scanning',
                    'persistence_elimination': 'registry_file_system_cleanup',
                    'verification': 'multiple_scan_engine_confirmation'
                },
                'account_security': {
                    'password_resets': 'forced_password_change_all_users',
                    'credential_rotation': 'service_account_api_key_rotation',
                    'privilege_review': 'emergency_privilege_audit_reduction',
                    'session_invalidation': 'global_session_token_revocation'
                }
            }
        }
        
        return containment_strategy
    
    def coordinate_recovery_operations(self):
        """Coordinate comprehensive system recovery and validation"""
        recovery_operations = {
            'system_restoration': {
                'clean_build_deployment': {
                    'infrastructure': 'immutable_infrastructure_deployment',
                    'applications': 'container_based_clean_application_deployment',
                    'data_restoration': 'verified_clean_backup_restoration',
                    'configuration': 'infrastructure_as_code_secure_baseline',
                    'validation': 'automated_security_configuration_testing'
                },
                'data_integrity_verification': {
                    'backup_validation': 'pre_incident_backup_integrity_testing',
                    'data_consistency': 'database_transaction_log_validation',
                    'file_integrity': 'cryptographic_hash_verification',
                    'application_data': 'business_logic_data_validation',
                    'audit_trail': 'complete_restore_process_documentation'
                }
            },
            'security_enhancement': {
                'immediate_improvements': {
                    'patch_management': 'emergency_security_patch_deployment',
                    'configuration_hardening': 'cis_benchmark_security_baseline',
                    'monitoring_enhancement': 'additional_detection_rule_deployment',
                    'access_control': 'principle_of_least_privilege_enforcement'
                },
                'long_term_improvements': {
                    'architecture_changes': 'zero_trust_architecture_implementation',
                    'process_improvements': 'incident_response_plan_updates',
                    'training_programs': 'security_awareness_training_enhancement',
                    'technology_investments': 'advanced_threat_detection_capabilities'
                }
            }
        }
        
        return recovery_operations
```

## Technology-Adaptive Implementation

### Cloud-Native Incident Response (AWS/Azure/GCP)

**Recommended Pattern:** Cloud-native forensics with automated evidence collection and scalable response

```python
# cloud_incident_response.py
import boto3
import asyncio
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from google.cloud import compute_v1
from datetime import datetime
import logging

class CloudIncidentResponseService:
    def __init__(self, cloud_provider: str, region: str):
        self.provider = cloud_provider
        self.region = region
        self.logger = logging.getLogger(__name__)
        
        if cloud_provider == "aws":
            self.ec2 = boto3.client('ec2', region_name=region)
            self.cloudtrail = boto3.client('cloudtrail', region_name=region)
            self.guardduty = boto3.client('guardduty', region_name=region)
        elif cloud_provider == "azure":
            credential = DefaultAzureCredential()
            self.compute_client = ComputeManagementClient(credential, subscription_id)
        elif cloud_provider == "gcp":
            self.compute_client = compute_v1.InstancesClient()
    
    async def initiate_cloud_incident_response(self, incident_id: str, affected_resources: list):
        """Initiate cloud-specific incident response procedures"""
        
        response_actions = {
            'evidence_preservation': await self._preserve_cloud_evidence(affected_resources),
            'resource_isolation': await self._isolate_affected_resources(affected_resources),
            'log_collection': await self._collect_cloud_logs(incident_id),
            'forensic_imaging': await self._create_forensic_snapshots(affected_resources),
            'threat_analysis': await self._analyze_cloud_threats(incident_id)
        }
        
        return response_actions
    
    async def _preserve_cloud_evidence(self, resources: list) -> dict:
        """Preserve cloud infrastructure evidence"""
        evidence_collection = {}
        
        for resource in resources:
            if self.provider == "aws":
                # AWS-specific evidence preservation
                if resource['type'] == 'ec2_instance':
                    # Create EBS snapshots
                    snapshots = await self._create_ebs_snapshots(resource['id'])
                    evidence_collection[resource['id']] = {
                        'snapshots': snapshots,
                        'metadata': await self._collect_ec2_metadata(resource['id']),
                        'security_groups': await self._collect_security_groups(resource['id']),
                        'vpc_flow_logs': await self._collect_vpc_flow_logs(resource['id'])
                    }
                    
            elif self.provider == "azure":
                # Azure-specific evidence preservation
                if resource['type'] == 'virtual_machine':
                    vm_snapshots = await self._create_azure_snapshots(resource['id'])
                    evidence_collection[resource['id']] = {
                        'disk_snapshots': vm_snapshots,
                        'activity_logs': await self._collect_azure_activity_logs(resource['id']),
                        'nsg_logs': await self._collect_nsg_flow_logs(resource['id'])
                    }
                    
        return evidence_collection
    
    async def _create_ebs_snapshots(self, instance_id: str) -> list:
        """Create forensic EBS snapshots for AWS EC2 instances"""
        
        # Get instance details
        response = self.ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        
        snapshots = []
        for block_device in instance.get('BlockDeviceMappings', []):
            volume_id = block_device['Ebs']['VolumeId']
            
            # Create snapshot with forensic metadata
            snapshot_response = self.ec2.create_snapshot(
                VolumeId=volume_id,
                Description=f"Forensic snapshot - Incident Response - {datetime.utcnow().isoformat()}",
                TagSpecifications=[
                    {
                        'ResourceType': 'snapshot',
                        'Tags': [
                            {'Key': 'Purpose', 'Value': 'Forensic Analysis'},
                            {'Key': 'IncidentId', 'Value': f'INC-{datetime.utcnow().strftime("%Y%m%d-%H%M%S")}'},
                            {'Key': 'SourceInstance', 'Value': instance_id},
                            {'Key': 'CreatedBy', 'Value': 'IncidentResponse'},
                            {'Key': 'RetentionPeriod', 'Value': '7Years'}
                        ]
                    }
                ]
            )
            
            snapshots.append({
                'snapshot_id': snapshot_response['SnapshotId'],
                'volume_id': volume_id,
                'creation_time': datetime.utcnow().isoformat(),
                'hash_verification': await self._calculate_snapshot_hash(snapshot_response['SnapshotId'])
            })
            
        return snapshots
    
    async def _collect_cloud_logs(self, incident_id: str) -> dict:
        """Collect comprehensive cloud audit and security logs"""
        
        log_collection = {}
        
        if self.provider == "aws":
            # AWS CloudTrail logs
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=30)  # Look back 30 days
            
            cloudtrail_events = self.cloudtrail.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'EventName',
                        'AttributeValue': 'RunInstances'
                    },
                ],
                StartTime=start_time,
                EndTime=end_time
            )
            
            # AWS GuardDuty findings
            detector_ids = self.guardduty.list_detectors()['DetectorIds']
            if detector_ids:
                findings = self.guardduty.list_findings(
                    DetectorId=detector_ids[0],
                    FindingCriteria={
                        'Criterion': {
                            'updatedAt': {
                                'Gte': int(start_time.timestamp() * 1000)
                            }
                        }
                    }
                )
                
                log_collection['guardduty_findings'] = findings['FindingIds']
            
            log_collection['cloudtrail_events'] = cloudtrail_events['Events']
            
            # AWS Config compliance data
            config_client = boto3.client('config', region_name=self.region)
            compliance_summary = config_client.get_compliance_summary_by_resource_type()
            log_collection['config_compliance'] = compliance_summary
            
        return log_collection
    
    async def _analyze_cloud_threats(self, incident_id: str) -> dict:
        """Analyze cloud-specific threat indicators and attack patterns"""
        
        threat_analysis = {
            'cloud_specific_attacks': {
                'credential_harvesting': await self._detect_credential_harvesting(),
                'privilege_escalation': await self._detect_privilege_escalation(),
                'lateral_movement': await self._detect_lateral_movement(),
                'data_exfiltration': await self._detect_data_exfiltration(),
                'resource_abuse': await self._detect_resource_abuse()
            },
            'attack_timeline': await self._construct_cloud_attack_timeline(),
            'impact_assessment': await self._assess_cloud_impact(),
            'attribution_indicators': await self._collect_attribution_indicators()
        }
        
        return threat_analysis

class ContainerizedIncidentResponse:
    def __init__(self, orchestrator: str = "kubernetes"):
        self.orchestrator = orchestrator
        if orchestrator == "kubernetes":
            from kubernetes import client, config
            config.load_incluster_config()
            self.k8s_client = client.CoreV1Api()
            self.apps_client = client.AppsV1Api()
    
    async def respond_to_container_incident(self, namespace: str, pod_name: str):
        """Handle incidents in containerized environments"""
        
        # Container forensic evidence collection
        evidence = {
            'container_logs': await self._collect_container_logs(namespace, pod_name),
            'pod_manifest': await self._collect_pod_manifest(namespace, pod_name),
            'container_filesystem': await self._create_container_snapshot(namespace, pod_name),
            'network_policies': await self._collect_network_policies(namespace),
            'service_mesh_logs': await self._collect_service_mesh_logs(namespace)
        }
        
        # Container isolation
        isolation_actions = {
            'network_isolation': await self._isolate_pod_network(namespace, pod_name),
            'resource_limits': await self._apply_resource_constraints(namespace, pod_name),
            'security_context': await self._apply_security_constraints(namespace, pod_name)
        }
        
        return {
            'evidence_collection': evidence,
            'containment_actions': isolation_actions,
            'recovery_plan': await self._plan_container_recovery(namespace, pod_name)
        }
```

### On-Premise Infrastructure Response

**Recommended Pattern:** Traditional forensics with comprehensive evidence preservation

```bash
#!/bin/bash
# on_premise_incident_response.sh

INCIDENT_ID="INC-$(date +%Y%m%d-%H%M%S)"
EVIDENCE_DIR="/forensics/evidence/${INCIDENT_ID}"
LOG_FILE="/forensics/logs/incident_${INCIDENT_ID}.log"

# Create evidence directory structure
mkdir -p "${EVIDENCE_DIR}/{memory,disk,network,logs,malware}"

log_action() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Memory forensics acquisition
acquire_memory_dump() {
    local target_host=$1
    log_action "Starting memory acquisition for $target_host"
    
    # Use multiple tools for redundancy
    if command -v linpmem &> /dev/null; then
        linpmem -o "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw"
        sha256sum "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw" > "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw.sha256"
    fi
    
    if command -v avml &> /dev/null; then
        avml "${EVIDENCE_DIR}/memory/${target_host}_avml.raw"
        sha256sum "${EVIDENCE_DIR}/memory/${target_host}_avml.raw" > "${EVIDENCE_DIR}/memory/${target_host}_avml.raw.sha256"
    fi
    
    # Volatility analysis
    if command -v vol.py &> /dev/null; then
        vol.py -f "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw" imageinfo > "${EVIDENCE_DIR}/memory/${target_host}_imageinfo.txt"
        vol.py -f "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw" --profile=Win7SP1x64 pslist > "${EVIDENCE_DIR}/memory/${target_host}_pslist.txt"
        vol.py -f "${EVIDENCE_DIR}/memory/${target_host}_linpmem.raw" --profile=Win7SP1x64 netscan > "${EVIDENCE_DIR}/memory/${target_host}_netscan.txt"
    fi
    
    log_action "Memory acquisition completed for $target_host"
}

# Disk forensics imaging
acquire_disk_image() {
    local target_device=$1
    local output_name=$2
    
    log_action "Starting disk imaging for $target_device"
    
    # Create forensic image with verification
    dc3dd if="$target_device" of="${EVIDENCE_DIR}/disk/${output_name}.dd" hash=sha256 log="${EVIDENCE_DIR}/disk/${output_name}.log"
    
    # Create E01 format for compatibility
    if command -v ewfacquire &> /dev/null; then
        ewfacquire -t "${EVIDENCE_DIR}/disk/${output_name}" "$target_device"
    fi
    
    log_action "Disk imaging completed for $target_device"
}

# Network traffic capture
start_network_capture() {
    local interface=$1
    local duration=${2:-3600}  # Default 1 hour
    
    log_action "Starting network capture on $interface for ${duration}s"
    
    # Full packet capture
    tcpdump -i "$interface" -w "${EVIDENCE_DIR}/network/capture_$(date +%Y%m%d_%H%M%S).pcap" &
    TCPDUMP_PID=$!
    
    # Wait for specified duration then stop
    sleep "$duration"
    kill $TCPDUMP_PID
    
    # Generate traffic analysis
    if command -v tshark &> /dev/null; then
        tshark -r "${EVIDENCE_DIR}/network/capture_*.pcap" -q -z conv,ip > "${EVIDENCE_DIR}/network/conversations.txt"
        tshark -r "${EVIDENCE_DIR}/network/capture_*.pcap" -q -z http,tree > "${EVIDENCE_DIR}/network/http_analysis.txt"
    fi
    
    log_action "Network capture completed"
}

# System information collection
collect_system_info() {
    local target_host=$1
    
    log_action "Collecting system information for $target_host"
    
    # Basic system info
    uname -a > "${EVIDENCE_DIR}/logs/${target_host}_uname.txt"
    cat /etc/os-release > "${EVIDENCE_DIR}/logs/${target_host}_os_release.txt"
    
    # Running processes
    ps auxwww > "${EVIDENCE_DIR}/logs/${target_host}_processes.txt"
    
    # Network connections
    netstat -antlp > "${EVIDENCE_DIR}/logs/${target_host}_netstat.txt"
    ss -antlp > "${EVIDENCE_DIR}/logs/${target_host}_ss.txt"
    
    # Logged in users
    who > "${EVIDENCE_DIR}/logs/${target_host}_who.txt"
    last > "${EVIDENCE_DIR}/logs/${target_host}_last.txt"
    
    # File system information
    mount > "${EVIDENCE_DIR}/logs/${target_host}_mount.txt"
    df -h > "${EVIDENCE_DIR}/logs/${target_host}_df.txt"
    
    # Recently modified files
    find / -type f -mtime -7 -ls 2>/dev/null > "${EVIDENCE_DIR}/logs/${target_host}_recent_files.txt"
    
    log_action "System information collection completed for $target_host"
}

# Log collection
collect_system_logs() {
    local target_host=$1
    
    log_action "Collecting system logs for $target_host"
    
    # System logs
    cp -r /var/log/* "${EVIDENCE_DIR}/logs/${target_host}_var_log/" 2>/dev/null
    
    # Journal logs
    if command -v journalctl &> /dev/null; then
        journalctl --all --no-pager > "${EVIDENCE_DIR}/logs/${target_host}_journalctl.txt"
    fi
    
    # Authentication logs
    if [ -f /var/log/auth.log ]; then
        cp /var/log/auth.log "${EVIDENCE_DIR}/logs/${target_host}_auth.log"
    fi
    
    if [ -f /var/log/secure ]; then
        cp /var/log/secure "${EVIDENCE_DIR}/logs/${target_host}_secure.log"
    fi
    
    # Web server logs if present
    if [ -d /var/log/apache2 ]; then
        cp -r /var/log/apache2 "${EVIDENCE_DIR}/logs/${target_host}_apache2/"
    fi
    
    if [ -d /var/log/nginx ]; then
        cp -r /var/log/nginx "${EVIDENCE_DIR}/logs/${target_host}_nginx/"
    fi
    
    log_action "System log collection completed for $target_host"
}

# Main incident response workflow
main() {
    local target_host=${1:-localhost}
    local target_device=${2:-/dev/sda}
    local network_interface=${3:-eth0}
    
    log_action "Starting incident response for incident $INCIDENT_ID"
    log_action "Target host: $target_host, Device: $target_device, Interface: $network_interface"
    
    # Parallel evidence collection
    acquire_memory_dump "$target_host" &
    collect_system_info "$target_host" &
    collect_system_logs "$target_host" &
    start_network_capture "$network_interface" 3600 &
    
    # Wait for background jobs to complete
    wait
    
    # Disk imaging (do this last to avoid interference)
    acquire_disk_image "$target_device" "${target_host}_disk"
    
    # Generate evidence summary
    find "$EVIDENCE_DIR" -type f -exec ls -la {} \; > "${EVIDENCE_DIR}/evidence_inventory.txt"
    find "$EVIDENCE_DIR" -type f -exec sha256sum {} \; > "${EVIDENCE_DIR}/evidence_hashes.txt"
    
    log_action "Incident response evidence collection completed"
    log_action "Evidence stored in: $EVIDENCE_DIR"
}

# Execute main function with provided arguments
main "$@"
```

## 📊 Success Criteria

### Incident Response Effectiveness
- **Response Time**: Initial response <15 minutes for P0 incidents
- **Containment Speed**: Primary containment <1 hour for critical incidents  
- **Evidence Quality**: 100% forensically sound evidence collection
- **Business Continuity**: <5% service disruption during containment

### Investigation Quality Metrics
- **Root Cause Identification**: 100% definitive attribution for P0/P1 incidents
- **Timeline Accuracy**: <30 minute variance in event reconstruction
- **Evidence Completeness**: All relevant digital artifacts preserved and analyzed
- **Legal Admissibility**: 100% of evidence meets legal standards

## 🎯 Deliverables

Upon completion of incident response and forensic investigation:

- ✅ **Comprehensive Incident Report** with timeline, root cause analysis, and impact assessment
- ✅ **Forensic Analysis Report** with technical findings, malware analysis, and attribution assessment  
- ✅ **Evidence Package** with complete chain of custody documentation and digital evidence
- ✅ **Containment Documentation** with actions taken, systems affected, and recovery procedures
- ✅ **Lessons Learned Report** with process improvements and preventive recommendations
- ✅ **Legal and Regulatory Package** with breach notifications and compliance documentation
- ✅ **Business Impact Analysis** with financial quantification and risk assessment
- ✅ **Recovery Validation Report** confirming system integrity and security posture restoration

### Generic/Fallback Implementation

For unsupported technologies, provide generic incident response patterns:

```yaml
# Generic Incident Response Configuration
incident_response:
  approach: "nist_framework"  # or "sans_methodology", "iso_27035"
  
  response_phases:
    - "preparation_and_planning"
    - "detection_and_analysis"
    - "containment_eradication_recovery"
    - "post_incident_activity"
    
  evidence_collection:
    - "volatile_data_acquisition"
    - "non_volatile_data_imaging"
    - "network_traffic_capture"
    - "log_file_preservation"
    - "chain_of_custody_documentation"
    
  forensic_analysis:
    - "timeline_reconstruction"
    - "malware_analysis_and_attribution"
    - "network_forensics_and_traffic_analysis"
    - "file_system_and_registry_analysis"
    - "memory_forensics_and_process_analysis"
    
  reporting_deliverables:
    - "executive_summary_with_business_impact"
    - "technical_findings_and_evidence_analysis"
    - "forensic_timeline_and_attack_reconstruction"
    - "recommendations_and_lessons_learned"
    - "legal_and_regulatory_compliance_documentation"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Infrastructure Type** from deployment model for appropriate forensic tools and evidence collection methods
- **Technology Stack** for system-specific forensic techniques and log analysis procedures
- **Business Domain** for industry-specific incident types and regulatory compliance requirements
- **Scale and Complexity** for resource allocation and specialized forensic capabilities

### 2. Response Strategy Selection

Select incident response approaches based on detected requirements:
- **Cloud Environments**: Cloud-native forensics with API-based evidence collection and automated response
- **On-Premise Infrastructure**: Traditional forensics with comprehensive imaging and manual evidence preservation
- **Hybrid Environments**: Combined approach with both cloud and traditional forensic techniques
- **Containerized Applications**: Container-specific forensics with orchestration-aware response procedures

### 3. Forensic Implementation Strategy

Apply technology-specific forensic techniques:
- **Evidence Preservation**: Technology-appropriate imaging and data collection methods
- **Analysis Techniques**: Framework-specific forensic tools and investigation procedures
- **Timeline Reconstruction**: Technology-aware log correlation and event timeline construction
- **Attribution Analysis**: Threat intelligence correlation and attack pattern recognition

### 4. Success Criteria

Incident response implementation validation checklist:
- **Response Timeliness**: Incident classification and initial response within established timeframes
- **Evidence Integrity**: Forensically sound evidence collection with proper chain of custody
- **Investigation Completeness**: Thorough analysis with definitive root cause identification
- **Business Continuity**: Minimal service disruption during containment and recovery operations
- **Regulatory Compliance**: Adherence to industry-specific breach notification and documentation requirements

---

*This comprehensive incident response and forensics approach ensures rapid containment, thorough investigation, and complete recovery while maintaining evidence integrity and legal compliance throughout the entire process.*