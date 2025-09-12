# Security Architecture and Threat Modeling

**Agent: security-engineer**
**Purpose: Design comprehensive security architecture and conduct thorough threat modeling with technology-adaptive security patterns**

---

## Context Analysis

The security-engineer will analyze the CLAUDE.md file to determine:
- **Technology Stack**: Backend framework (Java/Spring, .NET Core, Node.js, Python/FastAPI) for appropriate security implementations and vulnerability patterns
- **Database Technology**: Database system (PostgreSQL, SQL Server, MongoDB) for data protection strategies and access controls
- **Business Domain**: Industry-specific security requirements (fintech, healthcare, ecommerce) for compliance frameworks and threat landscapes
- **Project Scale**: Application complexity and user base for appropriate security controls, monitoring solutions, and risk assessment levels
- **Development Stage**: Security maturity requirements from MVP to enterprise-grade security implementations

Based on this analysis, the security engineer will select appropriate security frameworks, implement technology-specific security controls, and ensure compliance with relevant industry standards.

## 🎯 Mission

Establish robust security controls and frameworks that protect applications, data, and infrastructure while enabling business operations and maintaining compliance requirements.

## 📋 Security Architecture Process

### Step 1: Security Requirements Analysis
**From business and architecture specifications:**
- **Regulatory compliance** requirements (GDPR, HIPAA, SOX, PCI-DSS)
- **Data classification** and sensitivity levels
- **Business risk tolerance** and security priorities
- **User access patterns** and authentication needs
- **Integration security** with external systems

### Step 2: Threat Modeling Framework

**STRIDE Threat Model:**
- **Spoofing** - Impersonating users or systems
- **Tampering** - Unauthorized modification of data
- **Repudiation** - Denying actions performed
- **Information Disclosure** - Unauthorized access to information
- **Denial of Service** - Preventing legitimate access
- **Elevation of Privilege** - Gaining unauthorized permissions

**Asset Identification:**
```
High-Value Assets:
├── User Authentication Data
│   ├── Passwords and credentials
│   ├── Session tokens and certificates
│   └── Multi-factor authentication secrets
├── Business Data
│   ├── Customer personal information
│   ├── Financial transaction data
│   └── Proprietary business logic
└── Infrastructure Components
    ├── Database servers and data
    ├── API endpoints and services
    └── Administrative access systems
```

### Step 3: Attack Surface Analysis

**External Attack Vectors:**
- **Web application** interfaces and APIs
- **Network services** and exposed ports
- **Third-party integrations** and dependencies
- **Social engineering** and phishing attacks
- **Supply chain** vulnerabilities

**Internal Attack Vectors:**
- **Privileged user** access and insider threats
- **Lateral movement** within network infrastructure
- **Data exfiltration** channels and methods
- **System vulnerabilities** and misconfigurations
- **Process weaknesses** and human error

## 🛡️ Security Controls Implementation

### Step 4: Authentication and Authorization

**Multi-Factor Authentication (MFA):**
```yaml
# Example MFA policy configuration
authentication_policy:
  mfa_required: true
  mfa_methods:
    - totp  # Time-based One-Time Password
    - sms   # SMS verification (backup only)
    - hardware_key  # FIDO2/WebAuthn
  
  session_management:
    timeout_idle: 30m
    timeout_absolute: 8h
    concurrent_sessions: 3
    
  password_policy:
    min_length: 12
    require_uppercase: true
    require_lowercase: true
    require_numbers: true
    require_special: true
    history_count: 12
    max_age_days: 90
```

**Role-Based Access Control (RBAC):**
```json
{
  "roles": {
    "admin": {
      "permissions": ["*"],
      "resources": ["*"]
    },
    "user_manager": {
      "permissions": ["read", "write"],
      "resources": ["users", "groups"]
    },
    "read_only": {
      "permissions": ["read"],
      "resources": ["users", "reports"]
    }
  },
  "policies": {
    "data_access": {
      "rules": [
        {
          "effect": "allow",
          "principal": "role:admin",
          "action": "*",
          "resource": "*"
        },
        {
          "effect": "allow", 
          "principal": "role:user_manager",
          "action": ["create", "read", "update"],
          "resource": "users/*"
        }
      ]
    }
  }
}
```

### Step 5: Data Protection and Encryption

**Encryption Strategy:**
- **Data at Rest** - Database encryption, file system encryption
- **Data in Transit** - TLS/SSL for all communications
- **Data in Processing** - Application-level encryption for sensitive fields
- **Key Management** - Hardware Security Modules (HSM) or cloud KMS
- **Certificate Management** - Automated certificate lifecycle management

**Implementation Example:**
```python
# Data encryption service
import cryptography
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self, key_service):
        self.key_service = key_service
        
    def encrypt_pii(self, data, user_context):
        """Encrypt personally identifiable information"""
        key = self.key_service.get_encryption_key('pii', user_context)
        fernet = Fernet(key)
        
        encrypted_data = {}
        for field, value in data.items():
            if field in ['ssn', 'credit_card', 'email']:
                encrypted_data[field] = fernet.encrypt(value.encode())
            else:
                encrypted_data[field] = value
                
        return encrypted_data
        
    def decrypt_pii(self, encrypted_data, user_context):
        """Decrypt PII with proper authorization"""
        if not self.authorize_decrypt(user_context):
            raise UnauthorizedError("Insufficient privileges for PII access")
            
        key = self.key_service.get_encryption_key('pii', user_context)
        fernet = Fernet(key)
        
        # Decrypt and audit access
        self.audit_log.record_pii_access(user_context, encrypted_data.keys())
        return self._decrypt_fields(encrypted_data, fernet)
```

## 🔍 Security Monitoring and Incident Response

### Step 6: Security Information and Event Management (SIEM)

**Log Collection Strategy:**
```yaml
# Security logging configuration
logging:
  security_events:
    - authentication_attempts
    - authorization_failures  
    - privilege_escalations
    - data_access_patterns
    - configuration_changes
    - network_anomalies
    
  log_sources:
    - application_logs
    - web_server_access_logs
    - database_audit_logs
    - system_security_logs
    - network_device_logs
    
  retention:
    security_logs: 7_years
    audit_logs: 10_years
    access_logs: 1_year
    debug_logs: 30_days
```

**Automated Threat Detection:**
```python
# Security monitoring rules
class SecurityMonitoring:
    def detect_brute_force(self, login_attempts):
        """Detect brute force login attempts"""
        failed_attempts = self.count_failed_logins(
            window_minutes=5,
            threshold=5
        )
        
        if failed_attempts > 5:
            return {
                'threat_type': 'brute_force',
                'severity': 'high',
                'recommended_action': 'block_ip_temporary',
                'duration_minutes': 30
            }
    
    def detect_privilege_escalation(self, user_actions):
        """Detect unusual privilege usage"""
        baseline = self.get_user_baseline(user_actions.user_id)
        
        if user_actions.permissions_used > baseline.max_permissions * 1.5:
            return {
                'threat_type': 'privilege_escalation',
                'severity': 'critical',
                'recommended_action': 'require_additional_auth'
            }
```

### Step 7: Vulnerability Management

**Security Testing Framework:**
- **Static Application Security Testing (SAST)** - Code analysis
- **Dynamic Application Security Testing (DAST)** - Runtime testing
- **Interactive Application Security Testing (IAST)** - Hybrid approach
- **Dependency Scanning** - Third-party vulnerability detection
- **Infrastructure Scanning** - System and network vulnerabilities

**Continuous Security Integration:**
```yaml
# Security testing in CI/CD pipeline
name: Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      
    - name: SAST Scan
      uses: securecodewarrior/github-action-add-sarif@v1
      with:
        sarif-file: 'sast-results.sarif'
        
    - name: Dependency Check
      run: |
        npm audit --audit-level high
        safety check -r requirements.txt
        
    - name: Container Security Scan
      run: |
        trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest
        
    - name: Infrastructure Security Scan
      run: |
        checkov -d ./terraform --framework terraform
```

## 🚨 Incident Response and Recovery

### Step 8: Security Incident Management

**Incident Response Plan:**
```yaml
incident_response:
  phases:
    preparation:
      - incident_response_team_defined
      - communication_plan_established
      - tools_and_resources_available
      - regular_training_conducted
      
    identification:
      - security_monitoring_active
      - alert_triage_procedures
      - incident_classification_criteria
      - escalation_triggers_defined
      
    containment:
      - isolation_procedures
      - evidence_preservation
      - damage_assessment
      - communication_protocols
      
    eradication:
      - root_cause_analysis
      - vulnerability_remediation
      - system_hardening
      - security_improvement
      
    recovery:
      - system_restoration
      - monitoring_enhancement
      - validation_testing
      - business_continuity
      
    lessons_learned:
      - post_incident_review
      - process_improvement
      - documentation_update
      - training_enhancement
```

**Incident Classification:**
- **P0 - Critical** - Data breach, system compromise affecting production
- **P1 - High** - Unauthorized access, significant security control failure
- **P2 - Medium** - Policy violation, minor security incident
- **P3 - Low** - Security awareness issue, procedural non-compliance

## Technology-Adaptive Implementation

### Java/Spring Boot + Spring Security

**Recommended Pattern:** Enterprise security with JWT, OAuth2, and comprehensive audit logging

```java
// Security Configuration
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfiguration {
    
    @Autowired
    private JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    
    @Autowired
    private JwtRequestFilter jwtRequestFilter;
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12);
    }
    
    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/auth/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers(HttpMethod.GET, "/api/public/**").permitAll()
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
            );
            
        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
        
        return http.build();
    }
}

// Threat Detection Service
@Service
@Transactional
public class ThreatDetectionService {
    
    private static final Logger logger = LoggerFactory.getLogger(ThreatDetectionService.class);
    
    @Autowired
    private SecurityEventRepository securityEventRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    @EventListener
    public void handleAuthenticationFailure(AuthenticationFailureBadCredentialsEvent event) {
        String username = event.getAuthentication().getName();
        String ipAddress = getClientIpAddress();
        
        SecurityEvent securityEvent = new SecurityEvent();
        securityEvent.setEventType(SecurityEventType.AUTHENTICATION_FAILURE);
        securityEvent.setUsername(username);
        securityEvent.setIpAddress(ipAddress);
        securityEvent.setTimestamp(Instant.now());
        securityEvent.setDetails("Failed login attempt");
        
        securityEventRepository.save(securityEvent);
        
        // Check for brute force attack
        if (isBruteForceAttack(username, ipAddress)) {
            handleBruteForceAttack(username, ipAddress);
        }
    }
    
    private boolean isBruteForceAttack(String username, String ipAddress) {
        Instant fiveMinutesAgo = Instant.now().minus(5, ChronoUnit.MINUTES);
        
        long failedAttempts = securityEventRepository
            .countByUsernameAndIpAddressAndEventTypeAndTimestampAfter(
                username, ipAddress, SecurityEventType.AUTHENTICATION_FAILURE, fiveMinutesAgo
            );
            
        return failedAttempts >= 5;
    }
    
    private void handleBruteForceAttack(String username, String ipAddress) {
        logger.warn("Brute force attack detected for user: {} from IP: {}", username, ipAddress);
        
        // Block IP address temporarily
        securityEventRepository.save(SecurityEvent.builder()
            .eventType(SecurityEventType.IP_BLOCKED)
            .username(username)
            .ipAddress(ipAddress)
            .timestamp(Instant.now())
            .details("IP blocked due to brute force attack")
            .build());
        
        // Send security alert
        sendSecurityAlert("Brute Force Attack", 
            String.format("Multiple failed login attempts detected for user %s from IP %s", 
                username, ipAddress));
    }
}

// Data Encryption Service
@Service
public class DataEncryptionService {
    
    private final AESUtil aesUtil;
    private final KeyManagementService keyManagementService;
    
    @Value("${app.security.encryption.algorithm:AES/GCM/NoPadding}")
    private String encryptionAlgorithm;
    
    public String encryptPII(String plaintext, String context) {
        try {
            SecretKey key = keyManagementService.getEncryptionKey(context);
            return aesUtil.encrypt(plaintext, key, encryptionAlgorithm);
        } catch (Exception e) {
            logger.error("Encryption failed for context: {}", context, e);
            throw new SecurityException("Data encryption failed", e);
        }
    }
    
    @PreAuthorize("hasPermission(#context, 'PII_ACCESS')")
    public String decryptPII(String ciphertext, String context) {
        try {
            SecretKey key = keyManagementService.getEncryptionKey(context);
            String decrypted = aesUtil.decrypt(ciphertext, key, encryptionAlgorithm);
            
            // Audit PII access
            auditService.logPIIAccess(SecurityContextHolder.getContext()
                .getAuthentication().getName(), context);
                
            return decrypted;
        } catch (Exception e) {
            logger.error("Decryption failed for context: {}", context, e);
            throw new SecurityException("Data decryption failed", e);
        }
    }
}
```

### .NET Core + IdentityServer4 + Entity Framework

**Recommended Pattern:** Enterprise identity management with comprehensive authorization and threat detection

```csharp
// Security Configuration
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        // Identity configuration
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
            
            options.Events = new JwtBearerEvents
            {
                OnAuthenticationFailed = context =>
                {
                    var logger = context.HttpContext.RequestServices
                        .GetRequiredService<ILogger<Startup>>();
                    logger.LogWarning("JWT authentication failed: {Exception}", 
                        context.Exception.Message);
                    return Task.CompletedTask;
                },
                OnTokenValidated = context =>
                {
                    var securityService = context.HttpContext.RequestServices
                        .GetRequiredService<ISecurityMonitoringService>();
                    return securityService.LogSuccessfulAuthenticationAsync(context);
                }
            };
        });
        
        // Authorization policies
        services.AddAuthorization(options =>
        {
            options.AddPolicy("AdminOnly", policy => 
                policy.RequireRole("Admin"));
            options.AddPolicy("PIIAccess", policy => 
                policy.RequireClaim("permission", "pii.read"));
            options.AddPolicy("FinancialData", policy =>
                policy.RequireAssertion(context =>
                    context.User.HasClaim("department", "Finance") &&
                    context.User.HasClaim("clearance", "High")));
        });
        
        // Security services
        services.AddScoped<IThreatDetectionService, ThreatDetectionService>();
        services.AddScoped<IDataProtectionService, DataProtectionService>();
        services.AddScoped<ISecurityAuditService, SecurityAuditService>();
    }
    
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        // Security headers
        app.UseSecurityHeaders(options =>
        {
            options.AddFrameOptionsDeny()
                   .AddContentTypeOptionsNoSniff()
                   .AddStrictTransportSecurityMaxAgeIncludeSubDomains(maxAgeInSeconds: 31536000)
                   .AddReferrerPolicyStrictOriginWhenCrossOrigin()
                   .AddContentSecurityPolicy(builder =>
                   {
                       builder.AddObjectSrc().None();
                       builder.AddFormAction().Self();
                       builder.AddFrameAncestors().None();
                   });
        });
        
        app.UseAuthentication();
        app.UseAuthorization();
        
        // Custom security middleware
        app.UseMiddleware<SecurityMonitoringMiddleware>();
        app.UseMiddleware<RateLimitingMiddleware>();
    }
}

// Threat Detection Service
public interface IThreatDetectionService
{
    Task<ThreatAssessment> AnalyzeLoginAttemptAsync(string username, string ipAddress);
    Task<bool> IsBruteForceAttackAsync(string username, string ipAddress);
    Task HandleSuspiciousActivityAsync(SecurityEvent securityEvent);
}

public class ThreatDetectionService : IThreatDetectionService
{
    private readonly ISecurityEventRepository _securityEventRepository;
    private readonly ILogger<ThreatDetectionService> _logger;
    private readonly INotificationService _notificationService;
    
    public async Task<ThreatAssessment> AnalyzeLoginAttemptAsync(string username, string ipAddress)
    {
        var assessment = new ThreatAssessment { Username = username, IpAddress = ipAddress };
        
        // Check for brute force patterns
        var recentFailures = await _securityEventRepository
            .GetRecentAuthenticationFailuresAsync(username, ipAddress, TimeSpan.FromMinutes(15));
            
        if (recentFailures.Count >= 5)
        {
            assessment.ThreatLevel = ThreatLevel.High;
            assessment.ThreatType = ThreatType.BruteForce;
            assessment.RecommendedAction = ThreatAction.BlockIP;
            
            await HandleSuspiciousActivityAsync(new SecurityEvent
            {
                EventType = SecurityEventType.BruteForceDetected,
                Username = username,
                IpAddress = ipAddress,
                Details = $"Multiple failed login attempts: {recentFailures.Count}",
                Timestamp = DateTime.UtcNow
            });
        }
        
        // Check for suspicious IP patterns
        var ipReputation = await CheckIpReputationAsync(ipAddress);
        if (ipReputation.IsMalicious)
        {
            assessment.ThreatLevel = ThreatLevel.Critical;
            assessment.ThreatType = ThreatType.MaliciousIP;
            assessment.RecommendedAction = ThreatAction.BlockIP;
        }
        
        // Check for unusual login patterns
        var userProfile = await GetUserLoginProfileAsync(username);
        if (IsUnusualLoginPattern(userProfile, ipAddress))
        {
            assessment.ThreatLevel = ThreatLevel.Medium;
            assessment.ThreatType = ThreatType.AnomalousAccess;
            assessment.RecommendedAction = ThreatAction.RequireAdditionalAuth;
        }
        
        return assessment;
    }
    
    public async Task HandleSuspiciousActivityAsync(SecurityEvent securityEvent)
    {
        await _securityEventRepository.AddAsync(securityEvent);
        
        _logger.LogWarning("Suspicious activity detected: {EventType} for user {Username} from IP {IpAddress}",
            securityEvent.EventType, securityEvent.Username, securityEvent.IpAddress);
            
        // Send security alert based on threat level
        if (securityEvent.ThreatLevel >= ThreatLevel.High)
        {
            await _notificationService.SendSecurityAlertAsync(new SecurityAlert
            {
                Title = $"Security Threat Detected: {securityEvent.ThreatType}",
                Description = securityEvent.Details,
                Severity = securityEvent.ThreatLevel,
                Timestamp = securityEvent.Timestamp,
                UserId = securityEvent.Username,
                IpAddress = securityEvent.IpAddress
            });
        }
    }
}
```

### Node.js + Passport.js + Express Security

**Recommended Pattern:** Middleware-based security with comprehensive logging and monitoring

```javascript
// Security Configuration
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const passport = require('passport');
const JwtStrategy = require('passport-jwt').Strategy;
const ExtractJwt = require('passport-jwt').ExtractJwt;
const bcrypt = require('bcryptjs');
const winston = require('winston');

class SecurityConfiguration {
  constructor(app) {
    this.app = app;
    this.logger = winston.createLogger({
      level: 'info',
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.errors({ stack: true }),
        winston.format.json()
      ),
      transports: [
        new winston.transports.File({ 
          filename: 'logs/security.log',
          level: 'warn'
        })
      ]
    });
    
    this.setupSecurityMiddleware();
    this.setupAuthentication();
    this.setupRateLimiting();
  }
  
  setupSecurityMiddleware() {
    // Security headers
    this.app.use(helmet({
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          scriptSrc: ["'self'", "'unsafe-inline'"],
          styleSrc: ["'self'", "'unsafe-inline'"],
          imgSrc: ["'self'", 'data:', 'https:'],
          connectSrc: ["'self'"],
          fontSrc: ["'self'"],
          objectSrc: ["'none'"],
          mediaSrc: ["'self'"],
          frameSrc: ["'none'"]
        }
      },
      hsts: {
        maxAge: 31536000,
        includeSubDomains: true,
        preload: true
      }
    }));
    
    // Custom security logging middleware
    this.app.use((req, res, next) => {
      const securityData = {
        ip: req.ip,
        userAgent: req.get('User-Agent'),
        method: req.method,
        url: req.url,
        timestamp: new Date().toISOString()
      };
      
      // Log suspicious patterns
      if (this.isSuspiciousRequest(req)) {
        this.logger.warn('Suspicious request detected', securityData);
      }
      
      next();
    });
  }
  
  setupAuthentication() {
    const jwtOptions = {
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: process.env.JWT_SECRET,
      algorithms: ['HS256']
    };
    
    passport.use(new JwtStrategy(jwtOptions, async (payload, done) => {
      try {
        const user = await User.findById(payload.sub);
        if (user) {
          // Log successful authentication
          this.logger.info('Successful JWT authentication', {
            userId: user.id,
            ip: payload.ip,
            timestamp: new Date().toISOString()
          });
          return done(null, user);
        }
        return done(null, false);
      } catch (error) {
        this.logger.error('JWT authentication error', {
          error: error.message,
          payload,
          timestamp: new Date().toISOString()
        });
        return done(error, false);
      }
    }));
    
    this.app.use(passport.initialize());
  }
  
  setupRateLimiting() {
    // General rate limiting
    const generalLimiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 1000, // limit each IP to 1000 requests per windowMs
      message: 'Too many requests from this IP, please try again later',
      standardHeaders: true,
      legacyHeaders: false,
      handler: (req, res) => {
        this.logger.warn('Rate limit exceeded', {
          ip: req.ip,
          userAgent: req.get('User-Agent'),
          url: req.url,
          timestamp: new Date().toISOString()
        });
        res.status(429).json({ error: 'Too many requests' });
      }
    });
    
    // Strict rate limiting for authentication endpoints
    const authLimiter = rateLimit({
      windowMs: 5 * 60 * 1000, // 5 minutes
      max: 5, // limit each IP to 5 requests per windowMs
      skipSuccessfulRequests: true,
      handler: (req, res) => {
        this.logger.error('Authentication rate limit exceeded', {
          ip: req.ip,
          userAgent: req.get('User-Agent'),
          timestamp: new Date().toISOString()
        });
        res.status(429).json({ error: 'Too many authentication attempts' });
      }
    });
    
    this.app.use('/api/', generalLimiter);
    this.app.use('/api/auth/', authLimiter);
  }
  
  isSuspiciousRequest(req) {
    const suspiciousPatterns = [
      /\.\.[\/\\]/,  // Directory traversal
      /<script/i,     // XSS attempts
      /union.*select/i, // SQL injection
      /eval\(/i,      // Code injection
      /\bor\s+1=1/i   // SQL injection
    ];
    
    const testString = `${req.url} ${JSON.stringify(req.query)} ${JSON.stringify(req.body)}`;
    return suspiciousPatterns.some(pattern => pattern.test(testString));
  }
}

// Threat Detection Service
class ThreatDetectionService {
  constructor() {
    this.logger = winston.createLogger({
      level: 'info',
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
      ),
      transports: [
        new winston.transports.File({ filename: 'logs/threats.log' })
      ]
    });
    
    this.bruteForceAttempts = new Map();
    this.suspiciousIPs = new Set();
  }
  
  async detectBruteForce(username, ip) {
    const key = `${username}:${ip}`;
    const now = Date.now();
    const attempts = this.bruteForceAttempts.get(key) || [];
    
    // Remove attempts older than 5 minutes
    const recentAttempts = attempts.filter(time => now - time < 5 * 60 * 1000);
    
    if (recentAttempts.length >= 5) {
      this.suspiciousIPs.add(ip);
      
      const threat = {
        type: 'BRUTE_FORCE_ATTACK',
        severity: 'HIGH',
        username,
        ip,
        attemptCount: recentAttempts.length,
        timestamp: new Date().toISOString()
      };
      
      this.logger.error('Brute force attack detected', threat);
      
      // Send alert to security team
      await this.sendSecurityAlert(threat);
      
      return true;
    }
    
    recentAttempts.push(now);
    this.bruteForceAttempts.set(key, recentAttempts);
    return false;
  }
  
  async sendSecurityAlert(threat) {
    // Implementation would send alerts via email, Slack, etc.
    console.log(`🚨 SECURITY ALERT: ${threat.type}`, threat);
    
    // Log to external SIEM system
    if (process.env.SIEM_ENDPOINT) {
      try {
        await fetch(process.env.SIEM_ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(threat)
        });
      } catch (error) {
        this.logger.error('Failed to send threat data to SIEM', { error: error.message });
      }
    }
  }
  
  isIPSuspicious(ip) {
    return this.suspiciousIPs.has(ip);
  }
}

module.exports = { SecurityConfiguration, ThreatDetectionService };
```

## 📊 Compliance and Governance

### Step 9: Compliance Framework

**GDPR Compliance Controls:**
```json
{
  "gdpr_controls": {
    "data_protection_by_design": {
      "privacy_impact_assessments": "required",
      "data_minimization": "enforced",
      "purpose_limitation": "implemented"
    },
    "individual_rights": {
      "right_to_access": "automated_portal",
      "right_to_rectification": "self_service",
      "right_to_erasure": "workflow_based",
      "right_to_portability": "data_export_api"
    },
    "breach_notification": {
      "detection_time": "72_hours",
      "authority_notification": "automated",
      "individual_notification": "risk_based"
    }
  }
}
```

**Security Governance:**
- **Security policies** and procedures documentation
- **Risk assessment** and management procedures
- **Security awareness** training and certification
- **Vendor security** assessment and management
- **Regular security** audits and compliance reviews

## 📤 Deliverables

- **Security Architecture Document** with controls and frameworks
- **Threat Model Report** with risk assessment and mitigation strategies
- **Security Policies** and procedures documentation
- **Incident Response Plan** with roles, responsibilities, and procedures
- **Compliance Framework** with controls and audit procedures
- **Security Monitoring Setup** with SIEM configuration and alerting
- **Vulnerability Management** program and remediation procedures

## 🤝 Collaboration Points

**With software-architect:** Security architecture integration and technical controls
**With deployment-engineer:** Infrastructure security and deployment pipeline security
**With data-engineer:** Data protection, encryption, and access controls
**With api-engineer:** API security, authentication, and authorization
**With qa-engineer:** Security testing integration and vulnerability validation

### Python + FastAPI + OAuth2

**Recommended Pattern:** Async security with dependency injection and comprehensive monitoring

```python
# Security Configuration
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import asyncio
import logging
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, List

# Security logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/security.log'),
        logging.StreamHandler()
    ]
)
security_logger = logging.getLogger('security')

class SecurityConfiguration:
    def __init__(self, app: FastAPI):
        self.app = app
        self.limiter = Limiter(key_func=get_remote_address)
        self.app.state.limiter = self.limiter
        self.app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
        
        self.setup_middleware()
        self.setup_security_headers()
        
    def setup_middleware(self):
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
        
        # Custom security middleware
        @self.app.middleware("http")
        async def security_middleware(request: Request, call_next):
            # Log all requests
            start_time = datetime.utcnow()
            client_ip = get_remote_address(request)
            user_agent = request.headers.get("user-agent", "")
            
            security_logger.info(
                f"Request: {request.method} {request.url} from {client_ip}"
            )
            
            # Check for suspicious patterns
            if self.is_suspicious_request(request):
                security_logger.warning(
                    f"Suspicious request detected: {request.method} {request.url} "
                    f"from {client_ip} with User-Agent: {user_agent}"
                )
            
            response = await call_next(request)
            
            # Log response time and status
            process_time = (datetime.utcnow() - start_time).total_seconds()
            security_logger.info(
                f"Response: {response.status_code} in {process_time:.4f}s"
            )
            
            return response
    
    def setup_security_headers(self):
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
                "style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; "
                "connect-src 'self'; font-src 'self'; object-src 'none'; "
                "media-src 'self'; frame-src 'none';"
            )
            response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
            response.headers["Permissions-Policy"] = (
                "geolocation=(), microphone=(), camera=()"
            )
            
            return response
    
    def is_suspicious_request(self, request: Request) -> bool:
        suspicious_patterns = [
            r'\.\.[/\\]',     # Directory traversal
            r'<script',       # XSS attempts
            r'union.*select', # SQL injection
            r'eval\(',        # Code injection
            r'\bor\s+1=1'     # SQL injection
        ]
        
        import re
        test_string = f"{request.url} {request.query_params}"
        return any(re.search(pattern, test_string, re.IGNORECASE) 
                  for pattern in suspicious_patterns)

class ThreatDetectionService:
    def __init__(self):
        self.brute_force_attempts: Dict[str, List[datetime]] = {}
        self.suspicious_ips: set = set()
        self.logger = logging.getLogger('threat_detection')
    
    async def detect_brute_force(self, username: str, ip_address: str) -> bool:
        """Detect brute force authentication attempts"""
        key = f"{username}:{ip_address}"
        now = datetime.utcnow()
        
        # Initialize if not exists
        if key not in self.brute_force_attempts:
            self.brute_force_attempts[key] = []
        
        # Remove attempts older than 5 minutes
        cutoff_time = now - timedelta(minutes=5)
        self.brute_force_attempts[key] = [
            attempt for attempt in self.brute_force_attempts[key]
            if attempt > cutoff_time
        ]
        
        # Check if threshold exceeded
        if len(self.brute_force_attempts[key]) >= 5:
            self.suspicious_ips.add(ip_address)
            
            threat_data = {
                'type': 'BRUTE_FORCE_ATTACK',
                'severity': 'HIGH',
                'username': username,
                'ip_address': ip_address,
                'attempt_count': len(self.brute_force_attempts[key]),
                'timestamp': now.isoformat()
            }
            
            self.logger.error(f"Brute force attack detected: {threat_data}")
            await self.send_security_alert(threat_data)
            
            return True
        
        # Record this attempt
        self.brute_force_attempts[key].append(now)
        return False
    
    async def analyze_user_behavior(self, user_id: str, request: Request) -> Dict:
        """Analyze user behavior for anomalies"""
        analysis = {
            'user_id': user_id,
            'ip_address': get_remote_address(request),
            'user_agent': request.headers.get('user-agent', ''),
            'timestamp': datetime.utcnow().isoformat(),
            'risk_score': 0,
            'anomalies': []
        }
        
        # Check for IP reputation
        if await self.is_malicious_ip(analysis['ip_address']):
            analysis['risk_score'] += 50
            analysis['anomalies'].append('MALICIOUS_IP')
        
        # Check for unusual access patterns
        if await self.is_unusual_access_pattern(user_id, analysis['ip_address']):
            analysis['risk_score'] += 30
            analysis['anomalies'].append('UNUSUAL_ACCESS_PATTERN')
        
        # Check for suspicious user agent
        if self.is_suspicious_user_agent(analysis['user_agent']):
            analysis['risk_score'] += 20
            analysis['anomalies'].append('SUSPICIOUS_USER_AGENT')
        
        if analysis['risk_score'] >= 50:
            self.logger.warning(f"High-risk user behavior detected: {analysis}")
            await self.send_security_alert({
                'type': 'ANOMALOUS_USER_BEHAVIOR',
                'severity': 'MEDIUM' if analysis['risk_score'] < 80 else 'HIGH',
                'details': analysis
            })
        
        return analysis
    
    async def is_malicious_ip(self, ip_address: str) -> bool:
        """Check IP against threat intelligence feeds"""
        # Implementation would check against threat intelligence APIs
        return ip_address in self.suspicious_ips
    
    async def is_unusual_access_pattern(self, user_id: str, ip_address: str) -> bool:
        """Check if access pattern is unusual for this user"""
        # Implementation would analyze historical access patterns
        return False  # Placeholder
    
    def is_suspicious_user_agent(self, user_agent: str) -> bool:
        """Check for suspicious user agent patterns"""
        suspicious_patterns = [
            'bot', 'crawler', 'spider', 'scraper',
            'curl', 'wget', 'python-requests'
        ]
        return any(pattern in user_agent.lower() for pattern in suspicious_patterns)
    
    async def send_security_alert(self, threat_data: Dict):
        """Send security alert to monitoring systems"""
        self.logger.critical(f"🚨 SECURITY ALERT: {threat_data}")
        
        # Implementation would send to SIEM, email, Slack, etc.
        # Example: await send_to_siem(threat_data)
        # Example: await send_email_alert(threat_data)
        # Example: await send_slack_alert(threat_data)

# Data Protection Service
class DataProtectionService:
    def __init__(self, encryption_key: str):
        self.encryption_key = encryption_key.encode()
        self.logger = logging.getLogger('data_protection')
    
    async def encrypt_pii(self, data: str, context: str) -> str:
        """Encrypt personally identifiable information"""
        try:
            from cryptography.fernet import Fernet
            
            # Generate context-specific key
            context_key = self.derive_context_key(context)
            f = Fernet(context_key)
            
            encrypted = f.encrypt(data.encode())
            
            self.logger.info(f"PII encrypted for context: {context}")
            return encrypted.decode()
            
        except Exception as e:
            self.logger.error(f"PII encryption failed for context {context}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Data protection failure"
            )
    
    async def decrypt_pii(self, encrypted_data: str, context: str, user_id: str) -> str:
        """Decrypt PII with proper authorization and auditing"""
        try:
            from cryptography.fernet import Fernet
            
            # Audit PII access
            self.logger.info(
                f"PII access attempt by user {user_id} for context {context}"
            )
            
            context_key = self.derive_context_key(context)
            f = Fernet(context_key)
            
            decrypted = f.decrypt(encrypted_data.encode())
            
            self.logger.info(
                f"PII successfully decrypted for user {user_id}, context {context}"
            )
            
            return decrypted.decode()
            
        except Exception as e:
            self.logger.error(
                f"PII decryption failed for user {user_id}, context {context}: {e}"
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Data decryption failure"
            )
    
    def derive_context_key(self, context: str) -> bytes:
        """Derive context-specific encryption key"""
        import base64
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        
        salt = context.encode()[:16].ljust(16, b'0')  # Ensure 16 bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.encryption_key))
        return key

# Usage in FastAPI app
app = FastAPI(title="Secure API", version="1.0.0")
security_config = SecurityConfiguration(app)
threat_detection = ThreatDetectionService()
data_protection = DataProtectionService("your-encryption-key-here")

@app.post("/api/auth/login")
@security_config.limiter.limit("5 per minute")
async def login(request: Request, credentials: LoginCredentials):
    client_ip = get_remote_address(request)
    
    # Check for brute force before processing
    if await threat_detection.detect_brute_force(credentials.username, client_ip):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many failed attempts. Account temporarily locked."
        )
    
    # Analyze user behavior
    behavior_analysis = await threat_detection.analyze_user_behavior(
        credentials.username, request
    )
    
    # Process authentication...
    return {"message": "Login successful", "risk_score": behavior_analysis['risk_score']}
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic security patterns:

```yaml
# Generic Security Implementation Configuration
security_architecture:
  approach: "defense_in_depth"  # or "zero_trust", "risk_based"
  
  authentication_principles:
    - "multi_factor_authentication_required"
    - "strong_password_policies_enforced"
    - "session_management_secure"
    - "account_lockout_protection"
    - "secure_password_recovery"
    
  authorization_patterns:
    - "role_based_access_control"
    - "principle_of_least_privilege"
    - "attribute_based_access_control"
    - "regular_access_reviews"
    - "segregation_of_duties"
    
  data_protection:
    - "encryption_at_rest_and_transit"
    - "data_classification_implemented"
    - "pii_protection_controls"
    - "data_loss_prevention"
    - "secure_key_management"
    
  threat_detection:
    - "security_monitoring_continuous"
    - "anomaly_detection_behavioral"
    - "threat_intelligence_integration"
    - "incident_response_automated"
    - "forensic_logging_comprehensive"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Backend Framework** from primary_language for appropriate security libraries and patterns
- **Database Technology** to select proper encryption, access controls, and audit logging
- **Business Domain** for compliance requirements (GDPR, HIPAA, PCI-DSS) and threat models
- **Project Scale** for appropriate security controls complexity and monitoring solutions

### 2. Security Architecture Approach

Select security patterns based on detected requirements:
- **Enterprise Applications**: Comprehensive RBAC, SIEM integration, and compliance frameworks
- **Web Applications**: OWASP security controls, API security, and frontend protection
- **Mobile Applications**: Device security, API protection, and data encryption
- **Desktop Applications**: Local data protection, secure communication, and privilege management

### 3. Threat Modeling Strategy

Apply technology-specific threat analysis:
- **STRIDE Analysis**: Technology-appropriate threat vectors and attack surfaces
- **Risk Assessment**: Business impact analysis based on domain and scale
- **Security Controls**: Framework-specific implementations and monitoring
- **Compliance Mapping**: Regulatory requirements to technical controls

### 4. Success Criteria

Security implementation validation checklist:
- **Technology Alignment**: Security controls match framework capabilities and best practices
- **Threat Coverage**: All identified threats have appropriate mitigation controls
- **Compliance**: Regulatory requirements are addressed with technical implementations
- **Monitoring**: Comprehensive logging and alerting for security events
- **Incident Response**: Automated detection and response capabilities implemented

---
*Comprehensive security architecture protects business assets while enabling secure, compliant operations and building stakeholder trust.*