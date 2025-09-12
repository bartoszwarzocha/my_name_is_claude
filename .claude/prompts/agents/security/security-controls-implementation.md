# Security Controls Implementation

**Agent: security-engineer**
**Purpose: Design, implement, and operationalize comprehensive security controls with technology-adaptive protection strategies**

---

## Context Analysis

The security-engineer will analyze the CLAUDE.md file to determine:
- **Technology Infrastructure**: Application architecture and deployment model (cloud, on-premise, hybrid) for appropriate security control selection and implementation
- **Application Stack**: Programming languages and frameworks for technology-specific security controls and integration patterns
- **Business Domain**: Industry-specific security requirements and compliance obligations for control framework selection
- **Project Scale**: Infrastructure complexity and user base for appropriate control granularity and automation levels
- **Security Maturity**: Existing security tools and processes for integration planning and control layering strategies

Based on this analysis, the security engineer will select appropriate security control frameworks, implement technology-specific protections, and ensure comprehensive defense-in-depth coverage across the entire technology stack.

## 🎯 Mission

Design, implement, and operationalize comprehensive security controls across the entire technology stack, ensuring defense-in-depth protection while maintaining usability and business functionality through systematic security engineering practices.

## 📋 Process Framework

### Phase 1: Security Control Architecture Design (2-3 hours)

**Step 1.1: Comprehensive Security Control Framework**

```python
# Defense-in-Depth Security Control Framework
SECURITY_CONTROL_LAYERS = {
    'physical_security': {
        'facility_controls': [
            'access_card_systems', 'biometric_controls', 'surveillance_systems',
            'environmental_monitoring', 'secure_destruction_facilities'
        ],
        'hardware_controls': [
            'secure_boot_processes', 'hardware_security_modules',
            'tamper_evident_seals', 'asset_tracking_systems'
        ]
    },
    'network_security': {
        'perimeter_controls': [
            'next_gen_firewalls', 'intrusion_prevention_systems',
            'ddos_protection', 'secure_remote_access_gateways'
        ],
        'internal_controls': [
            'network_segmentation', 'micro_segmentation', 'network_access_control',
            'network_monitoring', 'east_west_traffic_inspection'
        ]
    },
    'endpoint_security': {
        'device_controls': [
            'endpoint_detection_response', 'mobile_device_management',
            'disk_encryption', 'application_whitelisting', 'patch_management'
        ],
        'user_controls': [
            'privileged_access_management', 'multi_factor_authentication',
            'identity_governance', 'behavioral_analytics'
        ]
    },
    'application_security': {
        'development_controls': [
            'secure_coding_standards', 'static_analysis', 'dynamic_analysis',
            'dependency_scanning', 'secure_development_lifecycle'
        ],
        'runtime_controls': [
            'web_application_firewalls', 'runtime_application_protection',
            'api_security_gateways', 'container_security'
        ]
    },
    'data_security': {
        'data_protection_controls': [
            'data_classification', 'encryption_at_rest', 'encryption_in_transit',
            'data_loss_prevention', 'rights_management'
        ],
        'data_governance_controls': [
            'data_discovery', 'privacy_controls', 'retention_management',
            'audit_logging', 'data_masking'
        ]
    }
}

class SecurityControlArchitect:
    def __init__(self, business_requirements, threat_model):
        self.requirements = business_requirements
        self.threats = threat_model
        self.control_framework = {}
        
    def design_layered_security_architecture(self):
        """Design comprehensive defense-in-depth security architecture"""
        architecture_design = {
            'threat_aligned_controls': self._map_controls_to_threats(),
            'risk_based_prioritization': self._prioritize_controls_by_risk(),
            'integration_architecture': self._design_integration_patterns(),
            'monitoring_architecture': self._design_monitoring_framework(),
            'automation_framework': self._design_automation_capabilities()
        }
        
        return architecture_design
    
    def _map_controls_to_threats(self):
        """Map security controls to specific threat scenarios"""
        threat_control_mapping = {
            'advanced_persistent_threats': {
                'detection_controls': [
                    'behavioral_analytics_ueba', 'threat_hunting_platform',
                    'deception_technology', 'extended_detection_response_xdr'
                ],
                'prevention_controls': [
                    'zero_trust_architecture', 'privileged_access_management',
                    'application_control', 'network_segmentation'
                ],
                'response_controls': [
                    'security_orchestration_automation', 'incident_response_platform',
                    'forensic_tools', 'containment_automation'
                ]
            },
            'insider_threats': {
                'detection_controls': [
                    'user_behavior_analytics', 'data_access_monitoring',
                    'privileged_session_recording', 'anomaly_detection'
                ],
                'prevention_controls': [
                    'data_classification_labeling', 'rights_management',
                    'segregation_of_duties', 'approval_workflows'
                ],
                'deterrent_controls': [
                    'audit_logging', 'screen_recording', 'legal_agreements',
                    'security_awareness_training'
                ]
            },
            'external_attacks': {
                'perimeter_controls': [
                    'web_application_firewall', 'ddos_protection',
                    'threat_intelligence_feeds', 'email_security_gateway'
                ],
                'endpoint_controls': [
                    'endpoint_protection_platform', 'vulnerability_management',
                    'patch_management', 'configuration_management'
                ],
                'identity_controls': [
                    'identity_provider_integration', 'risk_based_authentication',
                    'session_management', 'account_lockout_policies'
                ]
            }
        }
        
        return threat_control_mapping
```

**Step 1.2: Technology Integration and Orchestration**

```python
class SecurityControlIntegrationFramework:
    def __init__(self, existing_infrastructure, security_tools):
        self.infrastructure = existing_infrastructure
        self.tools = security_tools
        
    def design_siem_integration_architecture(self):
        """Design comprehensive SIEM integration with all security tools"""
        siem_integration = {
            'data_ingestion_architecture': {
                'log_sources': {
                    'network_devices': {
                        'firewalls': 'syslog_cef_format_real_time',
                        'switches_routers': 'snmp_netflow_sflow_real_time',
                        'wireless_controllers': 'syslog_radius_accounting',
                        'load_balancers': 'syslog_http_access_logs'
                    },
                    'security_tools': {
                        'endpoint_protection': 'api_json_real_time_alerts',
                        'vulnerability_scanners': 'api_xml_scheduled_pulls',
                        'identity_providers': 'api_oauth_real_time_events',
                        'cloud_platforms': 'api_cloudtrail_continuous_streaming'
                    },
                    'business_applications': {
                        'web_applications': 'syslog_application_logs',
                        'databases': 'database_audit_logs_real_time',
                        'erp_systems': 'api_business_transaction_logs',
                        'collaboration_tools': 'api_user_activity_logs'
                    }
                },
                'data_normalization': {
                    'common_event_format': 'cef_standardized_field_mapping',
                    'taxonomy_mapping': 'mitre_att_ck_technique_mapping',
                    'threat_intelligence_enrichment': 'ioc_reputation_context_addition',
                    'asset_context_enrichment': 'cmdb_user_directory_integration'
                }
            },
            'correlation_and_analytics': {
                'real_time_correlation_rules': {
                    'authentication_anomalies': 'impossible_travel_brute_force_detection',
                    'lateral_movement_detection': 'kerberos_smb_rdp_anomaly_correlation',
                    'data_exfiltration_patterns': 'large_file_transfers_unusual_destinations',
                    'privilege_escalation': 'account_modification_privilege_changes'
                },
                'machine_learning_analytics': {
                    'user_behavior_baselines': 'unsupervised_clustering_normal_patterns',
                    'anomaly_detection': 'supervised_learning_known_attack_patterns',
                    'threat_hunting': 'graph_analytics_relationship_discovery',
                    'predictive_analytics': 'risk_scoring_attack_probability'
                }
            }
        }
        
        return siem_integration
    
    def implement_security_orchestration(self):
        """Implement comprehensive security orchestration and automation"""
        orchestration_framework = {
            'playbook_automation': {
                'incident_response_playbooks': {
                    'malware_detection': {
                        'trigger': 'edr_malware_alert_confidence_high',
                        'automated_actions': [
                            'isolate_endpoint_network_quarantine',
                            'collect_forensic_triage_package',
                            'notify_security_team_escalation',
                            'create_incident_ticket_documentation',
                            'initiate_threat_hunting_related_systems'
                        ],
                        'approval_gates': 'manager_approval_before_system_wipe',
                        'rollback_procedures': 'restore_endpoint_if_false_positive'
                    },
                    'credential_compromise': {
                        'trigger': 'multiple_failed_logins_password_spray',
                        'automated_actions': [
                            'lock_user_account_temporary_disable',
                            'invalidate_existing_sessions_tokens',
                            'require_password_reset_mfa_setup',
                            'notify_user_manager_security_team',
                            'initiate_account_activity_review'
                        ],
                        'approval_gates': 'security_analyst_validation_required',
                        'rollback_procedures': 'unlock_account_if_legitimate_activity'
                    }
                },
                'threat_intelligence_automation': {
                    'ioc_processing': {
                        'feed_ingestion': 'automated_threat_feed_consumption',
                        'ioc_validation': 'reputation_scoring_false_positive_filtering',
                        'distribution': 'automatic_firewall_dns_sinkhole_updates',
                        'hunting': 'retroactive_search_historical_data',
                        'reporting': 'automated_threat_landscape_reports'
                    }
                }
            }
        }
        
        return orchestration_framework
```

### Phase 2: Identity and Access Control Implementation (3-4 hours)

**Step 2.1: Zero Trust Identity Architecture**

```python
class ZeroTrustIdentityFramework:
    def __init__(self, user_directory, application_inventory):
        self.users = user_directory
        self.applications = application_inventory
        
    def implement_identity_governance(self):
        """Implement comprehensive identity governance and administration"""
        identity_governance = {
            'identity_lifecycle_management': {
                'user_provisioning': {
                    'automated_onboarding': {
                        'trigger': 'hr_system_new_employee_webhook',
                        'process': [
                            'create_active_directory_account',
                            'assign_role_based_group_memberships',
                            'provision_email_collaboration_accounts',
                            'generate_temporary_credentials',
                            'send_welcome_package_training_links'
                        ],
                        'approval_workflow': 'manager_hr_security_three_way_approval',
                        'audit_trail': 'complete_provisioning_activity_logging'
                    },
                    'role_changes': {
                        'trigger': 'hr_system_role_change_promotion_transfer',
                        'process': [
                            'analyze_current_access_rights',
                            'determine_new_access_requirements',
                            'implement_least_privilege_principle',
                            'remove_obsolete_access_rights',
                            'notify_stakeholders_of_changes'
                        ],
                        'approval_workflow': 'new_manager_security_approval_required',
                        'validation': 'access_recertification_within_30_days'
                    },
                    'user_deprovisioning': {
                        'trigger': 'hr_system_termination_resignation_webhook',
                        'immediate_actions': [
                            'disable_all_user_accounts',
                            'revoke_all_access_tokens_sessions',
                            'disable_vpn_remote_access',
                            'flag_user_data_for_backup_retention',
                            'notify_it_security_managers'
                        ],
                        'delayed_actions': [
                            'transfer_data_ownership_new_assignee',
                            'delete_personal_user_data_gdpr_compliance',
                            'return_company_assets_device_wipe',
                            'complete_exit_interview_security_briefing'
                        ]
                    }
                },
                'access_certification': {
                    'periodic_reviews': {
                        'frequency': 'quarterly_role_based_semi_annual_privileged',
                        'scope': 'all_application_access_data_access_admin_rights',
                        'reviewers': 'data_owners_managers_security_team',
                        'automation': 'ai_assisted_anomaly_flagging',
                        'enforcement': 'auto_revoke_uncertified_access_30_days'
                    },
                    'event_driven_reviews': {
                        'triggers': [
                            'role_change_promotion_transfer',
                            'security_incident_account_compromise',
                            'compliance_audit_external_review',
                            'data_breach_privileged_account_exposure'
                        ],
                        'scope': 'risk_based_expanded_review_related_accounts',
                        'urgency': 'complete_within_48_hours_critical_systems'
                    }
                }
            },
            'privileged_access_management': {
                'privileged_account_discovery': {
                    'scanning_scope': 'all_systems_applications_databases_network_devices',
                    'identification_methods': [
                        'active_directory_privileged_group_enumeration',
                        'database_sysadmin_role_identification',
                        'application_admin_account_discovery',
                        'service_account_privileged_access_mapping'
                    ],
                    'risk_assessment': 'criticality_exposure_usage_frequency_scoring'
                },
                'password_vaulting': {
                    'vault_architecture': 'high_availability_encrypted_vault_cluster',
                    'access_controls': 'dual_person_integrity_manager_approval',
                    'session_recording': 'full_session_video_keystroke_recording',
                    'password_rotation': 'automated_30_day_rotation_policy',
                    'emergency_access': 'break_glass_procedures_full_audit_trail'
                },
                'just_in_time_access': {
                    'implementation': 'temporary_group_membership_elevation',
                    'approval_workflow': 'business_justification_manager_security_approval',
                    'time_limits': 'maximum_8_hours_automatic_revocation',
                    'monitoring': 'continuous_activity_monitoring_privileged_sessions',
                    'attestation': 'post_access_activity_justification_required'
                }
            }
        }
        
        return identity_governance
    
    def implement_advanced_authentication(self):
        """Implement risk-based adaptive authentication"""
        authentication_framework = {
            'multi_factor_authentication': {
                'factor_types': {
                    'knowledge_factors': 'passwords_passphrases_security_questions',
                    'possession_factors': 'hardware_tokens_mobile_apps_smart_cards',
                    'inherence_factors': 'biometrics_fingerprint_face_voice_recognition',
                    'location_factors': 'gps_network_location_device_registration',
                    'behavioral_factors': 'keystroke_dynamics_mouse_movement_patterns'
                },
                'adaptive_policies': {
                    'low_risk_scenarios': {
                        'conditions': 'known_device_trusted_network_normal_hours',
                        'requirements': 'single_factor_password_only',
                        'monitoring': 'passive_behavioral_analytics'
                    },
                    'medium_risk_scenarios': {
                        'conditions': 'new_device_vpn_access_after_hours',
                        'requirements': 'two_factor_password_plus_mobile_app',
                        'monitoring': 'enhanced_session_monitoring'
                    },
                    'high_risk_scenarios': {
                        'conditions': 'foreign_country_tor_exit_node_privileged_access',
                        'requirements': 'three_factor_password_token_biometric',
                        'monitoring': 'real_time_security_analyst_review'
                    }
                }
            },
            'single_sign_on_architecture': {
                'identity_provider': 'saml_oauth_openid_connect_federation',
                'application_integration': 'pre_built_connectors_custom_integration',
                'session_management': 'centralized_session_timeout_policies',
                'federation_trusts': 'b2b_partner_customer_identity_federation',
                'security_controls': 'token_encryption_signature_validation_replay_protection'
            }
        }
        
        return authentication_framework
```

**Step 2.2: Application Security Controls**

```python
class ApplicationSecurityControlFramework:
    def __init__(self, application_portfolio, development_practices):
        self.applications = application_portfolio
        self.dev_practices = development_practices
        
    def implement_application_protection(self):
        """Implement comprehensive application security controls"""
        app_security_controls = {
            'web_application_firewall': {
                'deployment_architecture': {
                    'cloud_native_waf': 'aws_cloudflare_azure_front_door',
                    'on_premise_waf': 'f5_asm_imperva_securesphere',
                    'hybrid_deployment': 'consistent_policy_management_across_environments'
                },
                'protection_capabilities': {
                    'owasp_top_10_protection': 'injection_xss_csrf_security_misconfiguration',
                    'api_protection': 'rest_graphql_soap_api_specific_rules',
                    'bot_protection': 'malicious_bot_detection_captcha_challenge',
                    'ddos_protection': 'application_layer_ddos_mitigation',
                    'threat_intelligence': 'real_time_reputation_feeds_integration'
                },
                'advanced_features': {
                    'behavioral_analysis': 'anomaly_detection_user_behavior_profiling',
                    'machine_learning': 'adaptive_rules_false_positive_reduction',
                    'custom_rules': 'application_specific_business_logic_protection',
                    'virtual_patching': 'immediate_protection_before_code_fixes'
                }
            },
            'runtime_application_protection': {
                'rasp_deployment': {
                    'agent_based': 'application_server_embedded_protection',
                    'agentless': 'network_based_traffic_inspection',
                    'container_integration': 'kubernetes_sidecar_istio_service_mesh'
                },
                'protection_mechanisms': {
                    'code_injection_prevention': 'sql_injection_command_injection_detection',
                    'deserialization_protection': 'unsafe_deserialization_attack_prevention',
                    'file_upload_security': 'malware_scanning_file_type_validation',
                    'session_protection': 'session_hijacking_fixation_prevention'
                }
            },
            'api_security_gateway': {
                'api_discovery': 'automatic_api_endpoint_documentation_discovery',
                'authentication_authorization': 'oauth_jwt_api_key_management',
                'rate_limiting': 'per_user_per_api_adaptive_rate_limiting',
                'monitoring_analytics': 'api_usage_patterns_anomaly_detection',
                'data_protection': 'sensitive_data_masking_tokenization'
            }
        }
        
        return app_security_controls
    
    def implement_secure_development_controls(self):
        """Implement security controls in development pipeline"""
        dev_security_controls = {
            'secure_code_analysis': {
                'static_analysis': {
                    'tools': 'checkmarx_veracode_sonarqube_semgrep',
                    'integration': 'ide_plugins_git_hooks_ci_cd_pipeline',
                    'coverage': 'all_languages_frameworks_custom_rules',
                    'remediation': 'developer_guidance_fix_recommendations'
                },
                'dynamic_analysis': {
                    'tools': 'owasp_zap_burp_suite_rapid7_appspider',
                    'automation': 'automated_scanning_ci_cd_integration',
                    'coverage': 'authenticated_scanning_complete_application_flow',
                    'reporting': 'vulnerability_prioritization_false_positive_filtering'
                },
                'interactive_analysis': {
                    'tools': 'contrast_security_hdiv_protection_prevoty',
                    'runtime_feedback': 'real_time_vulnerability_detection',
                    'accuracy': 'reduced_false_positives_context_awareness',
                    'integration': 'development_testing_production_environments'
                }
            },
            'dependency_security_management': {
                'vulnerability_scanning': {
                    'tools': 'snyk_blackduck_whitesource_dependabot',
                    'coverage': 'direct_transitive_dependencies_container_images',
                    'automation': 'continuous_monitoring_pull_request_checking',
                    'remediation': 'automated_dependency_updates_security_patches'
                },
                'license_compliance': {
                    'scanning': 'open_source_license_identification',
                    'policy_enforcement': 'approved_restricted_prohibited_licenses',
                    'reporting': 'compliance_dashboards_legal_review_workflows',
                    'alternatives': 'alternative_component_recommendations'
                }
            }
        }
        
        return dev_security_controls
```

### Phase 3: Data Protection and Monitoring Implementation (2-3 hours)

**Step 3.1: Comprehensive Data Protection Framework**

```python
class DataProtectionFramework:
    def __init__(self, data_inventory, regulatory_requirements):
        self.data_catalog = data_inventory
        self.regulations = regulatory_requirements
        
    def implement_data_classification_protection(self):
        """Implement automated data classification and protection"""
        data_protection_controls = {
            'data_discovery_classification': {
                'automated_discovery': {
                    'structured_data': 'database_table_column_scanning_regex_patterns',
                    'unstructured_data': 'file_shares_email_document_content_analysis',
                    'cloud_storage': 'aws_s3_azure_blob_gcp_storage_scanning',
                    'application_data': 'api_endpoint_data_flow_analysis'
                },
                'classification_engine': {
                    'pattern_matching': 'regex_patterns_ssn_credit_card_patterns',
                    'machine_learning': 'nlp_content_classification_context_analysis',
                    'metadata_analysis': 'file_names_directory_structure_patterns',
                    'user_input': 'manual_classification_validation_feedback'
                },
                'classification_labels': {
                    'public': 'marketing_materials_public_website_content',
                    'internal': 'policies_procedures_internal_communications',
                    'confidential': 'financial_data_hr_records_customer_data',
                    'restricted': 'trade_secrets_legal_privileged_regulated_data'
                }
            },
            'encryption_implementation': {
                'encryption_at_rest': {
                    'database_encryption': 'tde_column_level_field_level_encryption',
                    'file_system_encryption': 'full_disk_encryption_file_level_encryption',
                    'backup_encryption': 'encrypted_backup_secure_key_management',
                    'key_management': 'hardware_security_modules_key_rotation'
                },
                'encryption_in_transit': {
                    'network_encryption': 'tls_1_3_ipsec_vpn_secure_protocols',
                    'application_encryption': 'end_to_end_message_encryption',
                    'api_encryption': 'https_certificate_pinning_mutual_tls',
                    'database_connections': 'encrypted_database_connections_ssl'
                },
                'key_management_service': {
                    'centralized_kms': 'aws_kms_azure_key_vault_hashicorp_vault',
                    'key_lifecycle': 'generation_rotation_revocation_destruction',
                    'access_controls': 'role_based_key_access_dual_control',
                    'audit_logging': 'complete_key_usage_access_audit_trail'
                }
            },
            'data_loss_prevention': {
                'network_dlp': {
                    'email_protection': 'outbound_email_scanning_attachment_analysis',
                    'web_protection': 'http_https_upload_monitoring_blocking',
                    'cloud_protection': 'saas_application_data_upload_monitoring',
                    'removable_media': 'usb_device_control_data_transfer_blocking'
                },
                'endpoint_dlp': {
                    'agent_deployment': 'windows_mac_linux_endpoint_agents',
                    'content_inspection': 'file_content_clipboard_screen_capture_monitoring',
                    'policy_enforcement': 'block_warn_allow_custom_actions',
                    'offline_protection': 'cached_policies_disconnected_enforcement'
                }
            }
        }
        
        return data_protection_controls
    
    def implement_privacy_controls(self):
        """Implement privacy by design controls"""
        privacy_controls = {
            'consent_management': {
                'consent_capture': 'granular_purpose_specific_consent_collection',
                'consent_storage': 'immutable_audit_trail_consent_decisions',
                'consent_withdrawal': 'easy_withdrawal_mechanisms_honor_requests',
                'consent_analytics': 'consent_rates_withdrawal_trends_analysis'
            },
            'data_subject_rights': {
                'right_of_access': 'automated_data_subject_access_request_fulfillment',
                'right_to_rectification': 'data_correction_workflows_verification',
                'right_to_erasure': 'automated_data_deletion_right_to_be_forgotten',
                'data_portability': 'structured_data_export_standard_formats'
            },
            'privacy_impact_assessments': {
                'automated_screening': 'high_risk_processing_activity_identification',
                'impact_analysis': 'privacy_risk_assessment_mitigation_planning',
                'stakeholder_consultation': 'dpo_legal_business_stakeholder_review',
                'monitoring': 'ongoing_privacy_impact_monitoring_updates'
            }
        }
        
        return privacy_controls
```

**Step 3.2: Security Monitoring and Analytics**

```python
class SecurityMonitoringFramework:
    def __init__(self, infrastructure_scale, security_requirements):
        self.scale = infrastructure_scale
        self.requirements = security_requirements
        
    def implement_comprehensive_monitoring(self):
        """Implement comprehensive security monitoring and analytics"""
        monitoring_architecture = {
            'extended_detection_response': {
                'data_collection': {
                    'endpoint_telemetry': 'process_network_file_registry_activity',
                    'network_telemetry': 'flow_records_packet_inspection_dns_logs',
                    'cloud_telemetry': 'api_calls_resource_changes_access_patterns',
                    'identity_telemetry': 'authentication_authorization_privilege_usage'
                },
                'advanced_analytics': {
                    'behavioral_analysis': 'ml_models_baseline_deviation_detection',
                    'threat_hunting': 'hypothesis_driven_proactive_threat_search',
                    'attack_path_analysis': 'graph_analytics_lateral_movement_detection',
                    'attribution_analysis': 'ttp_mapping_threat_actor_identification'
                },
                'automated_response': {
                    'containment_actions': 'automatic_isolation_quarantine_blocking',
                    'investigation_automation': 'evidence_collection_timeline_reconstruction',
                    'notification_escalation': 'stakeholder_notification_escalation_workflows',
                    'remediation_orchestration': 'automated_remediation_action_execution'
                }
            },
            'threat_intelligence_platform': {
                'intelligence_feeds': {
                    'commercial_feeds': 'crowdstrike_recorded_future_anomali',
                    'open_source_feeds': 'misp_otx_virustotal_abuse_ch',
                    'government_feeds': 'us_cert_ncsc_sector_specific_intel',
                    'internal_intelligence': 'incident_artifacts_ioc_generation'
                },
                'intelligence_processing': {
                    'normalization': 'stix_taxii_standard_format_conversion',
                    'enrichment': 'context_addition_confidence_scoring',
                    'validation': 'false_positive_filtering_source_reputation',
                    'distribution': 'automated_security_tool_integration'
                }
            },
            'security_metrics_kpis': {
                'operational_metrics': {
                    'mean_time_to_detection': 'average_time_incident_first_indicator',
                    'mean_time_to_response': 'average_time_response_action_initiated',
                    'mean_time_to_containment': 'average_time_threat_contained',
                    'false_positive_rate': 'percentage_false_alerts_total_alerts'
                },
                'effectiveness_metrics': {
                    'coverage_assessment': 'mitre_att_ck_technique_coverage_percentage',
                    'detection_accuracy': 'true_positive_rate_precision_recall',
                    'threat_hunting_success': 'proactive_threats_discovered_percentage',
                    'incident_prevention': 'attacks_blocked_before_impact'
                }
            }
        }
        
        return monitoring_architecture
```

## Technology-Adaptive Implementation

### Java/Spring Boot Security Controls

**Recommended Pattern:** Enterprise security with Spring Security, JWT, and comprehensive audit logging

```java
// SecurityConfiguration.java - Comprehensive Spring Security setup
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class EnterpriseSecurityConfiguration {
    
    @Autowired
    private JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    
    @Autowired
    private UserDetailsService jwtUserDetailsService;
    
    @Autowired
    private JwtRequestFilter jwtRequestFilter;
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12);
    }
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/auth/**").permitAll()
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers(HttpMethod.GET, "/api/health").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/user/**").hasAnyRole("USER", "ADMIN")
                .anyRequest().authenticated()
            )
            .exceptionHandling(ex -> ex
                .authenticationEntryPoint(jwtAuthenticationEntryPoint)
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .headers(headers -> headers
                .frameOptions().deny()
                .contentTypeOptions().and()
                .httpStrictTransportSecurity(hstsConfig -> hstsConfig
                    .maxAgeInSeconds(31536000)
                    .includeSubdomains(true)
                )
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt
                    .decoder(jwtDecoder())
                    .jwtAuthenticationConverter(jwtAuthenticationConverter())
                )
            );
            
        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
        
        return http.build();
    }
}

// SecurityAuditService.java - Comprehensive security event logging
@Service
@Transactional
public class SecurityAuditService {
    
    @Autowired
    private SecurityEventRepository securityEventRepository;
    
    @EventListener
    public void handleAuthenticationSuccess(AuthenticationSuccessEvent event) {
        SecurityEvent securityEvent = SecurityEvent.builder()
            .eventType(SecurityEventType.AUTHENTICATION_SUCCESS)
            .username(event.getAuthentication().getName())
            .timestamp(Instant.now())
            .ipAddress(getClientIpAddress())
            .userAgent(getCurrentUserAgent())
            .details("User successfully authenticated")
            .build();
            
        securityEventRepository.save(securityEvent);
    }
    
    @EventListener
    public void handleAuthenticationFailure(AbstractAuthenticationFailureEvent event) {
        String username = event.getAuthentication().getName();
        String reason = event.getException().getMessage();
        
        SecurityEvent securityEvent = SecurityEvent.builder()
            .eventType(SecurityEventType.AUTHENTICATION_FAILURE)
            .username(username)
            .timestamp(Instant.now())
            .ipAddress(getClientIpAddress())
            .reason(reason)
            .build();
            
        securityEventRepository.save(securityEvent);
        
        // Check for brute force attempts
        checkBruteForceAttempts(username);
    }
    
    private void checkBruteForceAttempts(String username) {
        Instant fiveMinutesAgo = Instant.now().minus(5, ChronoUnit.MINUTES);
        
        long failedAttempts = securityEventRepository
            .countByUsernameAndEventTypeAndTimestampAfter(
                username, SecurityEventType.AUTHENTICATION_FAILURE, fiveMinutesAgo
            );
            
        if (failedAttempts >= 5) {
            // Lock account and send alert
            lockUserAccount(username);
            sendSecurityAlert("Brute force attack detected", username);
        }
    }
}
```

### .NET Core Security Implementation

**Recommended Pattern:** ASP.NET Core Identity with comprehensive authorization and security headers

```csharp
// SecurityConfiguration.cs
public class SecurityStartup
{
    public void ConfigureServices(IServiceCollection services)
    {
        // Identity configuration with enhanced security
        services.AddIdentity<ApplicationUser, IdentityRole>(options =>
        {
            // Password policy
            options.Password.RequiredLength = 12;
            options.Password.RequireDigit = true;
            options.Password.RequireUppercase = true;
            options.Password.RequireLowercase = true;
            options.Password.RequireNonAlphanumeric = true;
            options.Password.RequiredUniqueChars = 4;
            
            // Lockout policy
            options.Lockout.MaxFailedAccessAttempts = 5;
            options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(30);
            options.Lockout.AllowedForNewUsers = true;
            
            // User policy
            options.User.RequireUniqueEmail = true;
            options.SignIn.RequireConfirmedEmail = true;
        })
        .AddEntityFrameworkStores<ApplicationDbContext>()
        .AddDefaultTokenProviders();
        
        // JWT Configuration
        services.AddAuthentication(options =>
        {
            options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
            options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
        })
        .AddJwtBearer(options =>
        {
            options.TokenValidationParameters = new TokenValidationParameters
            {
                ValidateIssuer = true,
                ValidateAudience = true,
                ValidateLifetime = true,
                ValidateIssuerSigningKey = true,
                ValidIssuer = Configuration["Jwt:Issuer"],
                ValidAudience = Configuration["Jwt:Audience"],
                IssuerSigningKey = new SymmetricSecurityKey(
                    Encoding.UTF8.GetBytes(Configuration["Jwt:Key"])),
                ClockSkew = TimeSpan.Zero
            };
        });
        
        // Authorization policies
        services.AddAuthorization(options =>
        {
            options.AddPolicy("AdminOnly", policy => 
                policy.RequireRole("Admin"));
            options.AddPolicy("RequireMFA", policy => 
                policy.RequireClaim("mfa", "true"));
        });
        
        // Security services
        services.AddScoped<ISecurityAuditService, SecurityAuditService>();
        services.AddScoped<IThreatDetectionService, ThreatDetectionService>();
    }
    
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        // Security headers middleware
        app.Use(async (context, next) =>
        {
            context.Response.Headers.Add("X-Content-Type-Options", "nosniff");
            context.Response.Headers.Add("X-Frame-Options", "DENY");
            context.Response.Headers.Add("X-XSS-Protection", "1; mode=block");
            context.Response.Headers.Add("Strict-Transport-Security", 
                "max-age=31536000; includeSubDomains; preload");
            context.Response.Headers.Add("Content-Security-Policy", 
                "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'");
                
            await next();
        });
        
        app.UseAuthentication();
        app.UseAuthorization();
        
        // Custom security middleware
        app.UseMiddleware<SecurityAuditMiddleware>();
        app.UseMiddleware<ThreatDetectionMiddleware>();
    }
}

// SecurityAuditService.cs
public class SecurityAuditService : ISecurityAuditService
{
    private readonly ApplicationDbContext _context;
    private readonly ILogger<SecurityAuditService> _logger;
    
    public async Task LogSecurityEventAsync(SecurityEvent securityEvent)
    {
        _context.SecurityEvents.Add(securityEvent);
        await _context.SaveChangesAsync();
        
        // Real-time threat analysis
        await AnalyzeThreatPatternsAsync(securityEvent);
    }
    
    private async Task AnalyzeThreatPatternsAsync(SecurityEvent securityEvent)
    {
        // Implement threat detection logic
        if (securityEvent.EventType == SecurityEventType.LoginFailure)
        {
            var recentFailures = await _context.SecurityEvents
                .Where(e => e.UserId == securityEvent.UserId 
                           && e.EventType == SecurityEventType.LoginFailure
                           && e.Timestamp > DateTime.UtcNow.AddMinutes(-15))
                .CountAsync();
                
            if (recentFailures >= 5)
            {
                await TriggerAccountLockdownAsync(securityEvent.UserId);
            }
        }
    }
}
```

### Python/FastAPI Security Controls

**Recommended Pattern:** FastAPI with OAuth2, comprehensive middleware, and async security monitoring

```python
# security_middleware.py
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
import asyncio
import logging
from datetime import datetime, timedelta

class SecurityMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app
        self.security_logger = logging.getLogger('security')
        self.setup_security_middleware()
    
    def setup_security_middleware(self):
        # CORS configuration
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["https://yourdomain.com"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Authorization", "Content-Type"]
        )
        
        # Trusted host middleware
        self.app.add_middleware(
            TrustedHostMiddleware, 
            allowed_hosts=["yourdomain.com", "*.yourdomain.com"]
        )
        
        # Rate limiting
        limiter = Limiter(key_func=get_remote_address)
        self.app.state.limiter = limiter
        self.app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
        
        # Security headers middleware
        @self.app.middleware("http")
        async def add_security_headers(request: Request, call_next):
            response = await call_next(request)
            
            # Security headers
            response.headers["X-Content-Type-Options"] = "nosniff"
            response.headers["X-Frame-Options"] = "DENY"
            response.headers["X-XSS-Protection"] = "1; mode=block"
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains; preload"
            )
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; script-src 'self' 'unsafe-inline'; "
                "style-src 'self' 'unsafe-inline'; img-src 'self' data: https:;"
            )
            
            return response
        
        # Security audit middleware
        @self.app.middleware("http")
        async def security_audit_middleware(request: Request, call_next):
            start_time = datetime.utcnow()
            client_ip = get_remote_address(request)
            user_agent = request.headers.get("user-agent", "")
            
            # Log request
            self.security_logger.info(
                f"Request: {request.method} {request.url} from {client_ip}"
            )
            
            # Check for suspicious patterns
            if self.is_suspicious_request(request):
                self.security_logger.warning(
                    f"Suspicious request: {request.method} {request.url} from {client_ip}"
                )
                await self.handle_suspicious_activity(request, client_ip)
            
            response = await call_next(request)
            
            # Log response
            process_time = (datetime.utcnow() - start_time).total_seconds()
            self.security_logger.info(
                f"Response: {response.status_code} in {process_time:.4f}s"
            )
            
            return response
    
    def is_suspicious_request(self, request: Request) -> bool:
        suspicious_patterns = [
            r'\.\.[/\\]',     # Directory traversal
            r'<script',       # XSS attempts
            r'union.*select', # SQL injection
            r'eval\(',        # Code injection
        ]
        
        import re
        test_string = f"{request.url} {request.query_params}"
        return any(re.search(pattern, test_string, re.IGNORECASE) 
                  for pattern in suspicious_patterns)
    
    async def handle_suspicious_activity(self, request: Request, client_ip: str):
        # Implement threat response logic
        await self.log_security_event({
            'event_type': 'suspicious_request',
            'ip_address': client_ip,
            'request_url': str(request.url),
            'user_agent': request.headers.get('user-agent'),
            'timestamp': datetime.utcnow()
        })

# Authentication and authorization
class SecurityManager:
    def __init__(self):
        self.oauth2_scheme = HTTPBearer()
        
    async def get_current_user(self, credentials: HTTPAuthorizationCredentials):
        token = credentials.credentials
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials"
                )
                
            # Additional token validation
            await self.validate_token_integrity(token, payload)
            
            return await self.get_user_by_username(username)
            
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    
    async def validate_token_integrity(self, token: str, payload: dict):
        # Check token blacklist
        if await self.is_token_blacklisted(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been revoked"
            )
        
        # Check token expiration with grace period
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
```

## 📊 Success Criteria

### Control Implementation Effectiveness
- **Coverage Completeness**: >95% of identified threats have corresponding controls
- **Control Operational Status**: >99% uptime for critical security controls
- **Integration Success**: 100% of security tools integrated with SIEM platform
- **Automation Level**: >80% of routine security tasks automated

### Security Posture Improvement
- **Vulnerability Reduction**: >90% reduction in critical vulnerabilities within 30 days
- **Incident Detection Speed**: Mean time to detection <5 minutes
- **Response Automation**: >70% of security incidents handled with minimal human intervention
- **Compliance Achievement**: 100% compliance with applicable regulatory frameworks

## 🎯 Deliverables

Upon completion of comprehensive security controls implementation:

- ✅ **Layered Security Architecture** with defense-in-depth controls across all technology layers
- ✅ **Identity and Access Management System** with zero trust principles and automated governance
- ✅ **Application Security Controls** integrated into development pipeline and runtime protection
- ✅ **Data Protection Framework** with classification, encryption, and privacy controls
- ✅ **Security Monitoring Platform** with advanced analytics and automated response capabilities
- ✅ **Threat Intelligence Integration** with automated IOC processing and distribution
- ✅ **Security Orchestration Playbooks** for common incident response scenarios
- ✅ **Compliance Documentation** demonstrating control implementation and effectiveness
- ✅ **Operational Procedures** for ongoing security control maintenance and optimization

### Generic/Fallback Implementation

For unsupported technologies, provide generic security control patterns:

```yaml
# Generic Security Controls Configuration
security_controls:
  approach: "defense_in_depth"  # or "zero_trust", "risk_based"
  
  control_categories:
    - "identity_and_access_management"
    - "network_security_controls"
    - "endpoint_protection_controls"
    - "application_security_controls"
    - "data_protection_controls"
    - "monitoring_and_detection_controls"
    
  implementation_principles:
    - "least_privilege_access_enforcement"
    - "defense_in_depth_layered_security"
    - "continuous_monitoring_and_assessment"
    - "automated_threat_detection_and_response"
    - "comprehensive_audit_logging_and_analysis"
    
  technology_integration:
    - "siem_centralized_log_management"
    - "security_orchestration_automation_response"
    - "threat_intelligence_integration"
    - "vulnerability_management_automation"
    - "compliance_monitoring_and_reporting"
    
  operational_procedures:
    - "incident_response_and_forensics"
    - "change_management_security_reviews"
    - "access_review_and_certification"
    - "security_awareness_training_programs"
    - "continuous_improvement_and_optimization"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Application Framework** from primary_language for appropriate security control integration patterns
- **Infrastructure Model** from deployment approach for suitable security architecture and control placement
- **Business Domain** for industry-specific security requirements and compliance control frameworks
- **Scale Requirements** for appropriate control granularity, automation levels, and monitoring capabilities

### 2. Security Control Strategy Selection

Select security implementation approaches based on detected requirements:
- **Enterprise Applications**: Comprehensive controls with SIEM integration, automated response, and compliance reporting
- **Cloud-Native Applications**: Container security, API gateways, and cloud-specific control implementations
- **Legacy Systems**: Compensating controls, network segmentation, and enhanced monitoring for older technologies
- **Hybrid Environments**: Unified control frameworks spanning cloud and on-premise infrastructure

### 3. Control Implementation Strategy

Apply technology-specific security patterns:
- **Authentication Controls**: Framework-appropriate identity integration and multi-factor authentication
- **Authorization Controls**: Technology-specific RBAC implementation and fine-grained access controls
- **Data Protection**: Encryption implementation suitable for application architecture and data flow patterns
- **Monitoring Integration**: Technology-aware log collection and security event correlation

### 4. Success Criteria

Security controls implementation validation checklist:
- **Control Coverage**: Comprehensive protection across all identified threat vectors and attack surfaces
- **Technology Integration**: Seamless integration with existing technology stack and development workflows
- **Operational Effectiveness**: Automated threat detection and response with minimal false positive rates
- **Compliance Alignment**: Controls mapped to applicable regulatory frameworks and audit requirements
- **Business Enablement**: Security controls that enhance rather than impede business functionality

---

*This comprehensive security controls implementation provides enterprise-grade protection while maintaining usability and enabling business functionality through systematic security engineering and automation.*