# Database Design and ETL Implementation

**Agent: data-engineer**
**Purpose: Design efficient database schemas and implement robust ETL pipelines for data processing**

---

## Context Analysis

The data-engineer will analyze the CLAUDE.md file to determine:
- **Database Technology**: Primary database system selection (PostgreSQL, MySQL, SQL Server, MongoDB) based on data patterns and requirements
- **Backend Framework**: ORM and data access pattern selection (Hibernate for Java, Entity Framework for .NET, TypeORM for Node.js, SQLAlchemy for Python)
- **Business Domain**: Industry-specific data modeling requirements, compliance needs (GDPR, HIPAA), and audit requirements
- **Project Scale**: Data volume expectations, performance requirements, and analytics complexity
- **Integration Requirements**: ETL complexity, real-time vs batch processing needs, and external system integrations

Based on this analysis, the engineer will select appropriate database technologies, data modeling approaches, and ETL implementation strategies.

## 🎯 Mission

Create scalable data architecture that efficiently stores, processes, and transforms data to support business operations and analytics requirements.

## 📋 Database Design Process

### Step 1: Data Requirements Analysis
**From business and architecture specifications:**
- **Business entities** and their relationships
- **Data volume estimates** and growth projections
- **Query patterns** and access requirements
- **Performance requirements** (read/write ratios, latency)
- **Compliance requirements** (GDPR, data retention, audit trails)

### Step 2: Data Modeling

**Conceptual Data Model:**
- **Business entities** identification (Customer, Order, Product)
- **Relationships** between entities (one-to-one, one-to-many, many-to-many)
- **Business rules** and constraints
- **Data lifecycle** and retention policies

**Logical Data Model:**
- **Normalized schema** design (3NF or higher)
- **Primary keys** and foreign key relationships
- **Data types** and constraints specification
- **Index strategy** for query optimization
- **Denormalization decisions** for performance

**Physical Data Model:**
- **Table structures** with columns and data types
- **Partitioning strategy** for large tables
- **Storage optimization** (compression, clustering)
- **Backup and recovery** design
- **Security controls** (encryption, access controls)

### Step 3: Database Schema Implementation

**Table Creation Scripts:**
```sql
-- Users table with audit fields
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id),
    updated_by UUID REFERENCES users(id)
);

-- Indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_users_created_at ON users(created_at);
```

**Migration Strategy:**
- **Version-controlled** schema changes
- **Backward compatibility** considerations
- **Data migration** scripts for existing data
- **Rollback procedures** for failed deployments
- **Testing strategy** for schema changes

## 🔄 ETL Pipeline Design

### Step 4: Data Integration Architecture

**Extract Phase:**
- **Source system** identification and connection
- **Data extraction** methods (full, incremental, CDC)
- **Data quality** validation at source
- **Error handling** and retry mechanisms
- **Scheduling** and orchestration

**Transform Phase:**
- **Data cleansing** and standardization rules
- **Business rule** application and validation
- **Data enrichment** from reference sources
- **Aggregation** and summarization logic
- **Data type** conversions and formatting

**Load Phase:**
- **Target schema** mapping and validation
- **Loading strategy** (batch, streaming, micro-batch)
- **Conflict resolution** for data updates
- **Performance optimization** (bulk loading, parallel processing)
- **Data validation** post-load verification

### Step 5: ETL Implementation

**Pipeline Architecture:**
```python
# Example ETL pipeline structure
class ETLPipeline:
    def __init__(self, source_config, target_config):
        self.source = DataSource(source_config)
        self.target = DataTarget(target_config)
        self.transformer = DataTransformer()
        
    def extract(self, query_config):
        """Extract data from source systems"""
        return self.source.fetch_data(query_config)
    
    def transform(self, raw_data):
        """Apply business rules and transformations"""
        cleaned_data = self.transformer.clean(raw_data)
        validated_data = self.transformer.validate(cleaned_data)
        return self.transformer.enrich(validated_data)
    
    def load(self, transformed_data):
        """Load data into target system"""
        return self.target.bulk_insert(transformed_data)
    
    def run(self, config):
        """Execute complete ETL process"""
        raw_data = self.extract(config.extract)
        transformed_data = self.transform(raw_data)
        result = self.load(transformed_data)
        self.log_metrics(result)
        return result
```

## Technology-Adaptive Implementation

### PostgreSQL + Java/Spring Boot + Hibernate

**Recommended Pattern:** JPA entities with Flyway migrations and Spring Data repositories

```java
// Maven Dependencies
/*
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
</dependency>
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
*/

// Database Migration Script (V001__Create_users_table.sql)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'INACTIVE', 'SUSPENDED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    version INTEGER DEFAULT 1
);

-- Performance indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status) WHERE status != 'INACTIVE';
CREATE INDEX idx_users_created_at ON users(created_at);

-- Audit trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    NEW.version = OLD.version + 1;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

// JPA Entity with comprehensive annotations
@Entity
@Table(name = "users", indexes = {
    @Index(name = "idx_users_email", columnList = "email"),
    @Index(name = "idx_users_status", columnList = "status"),
    @Index(name = "idx_users_created_at", columnList = "createdAt")
})
@EntityListeners(AuditingEntityListener.class)
@Audited
public class User {
    
    @Id
    @GeneratedValue(generator = "uuid2")
    @GenericGenerator(name = "uuid2", strategy = "uuid2")
    @Column(columnDefinition = "UUID")
    private UUID id;
    
    @Column(nullable = false, unique = true, length = 255)
    @Email(message = "Email should be valid")
    private String email;
    
    @Column(name = "password_hash", nullable = false)
    @JsonIgnore
    private String passwordHash;
    
    @Column(name = "first_name", nullable = false, length = 100)
    @Size(min = 2, max = 100, message = "First name must be between 2 and 100 characters")
    private String firstName;
    
    @Column(name = "last_name", nullable = false, length = 100)
    @Size(min = 2, max = 100, message = "Last name must be between 2 and 100 characters")
    private String lastName;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private UserStatus status = UserStatus.ACTIVE;
    
    @CreatedDate
    @Column(name = "created_at", nullable = false, updatable = false)
    private Instant createdAt;
    
    @LastModifiedDate
    @Column(name = "updated_at", nullable = false)
    private Instant updatedAt;
    
    @Version
    private Integer version;
    
    // Constructors, getters, setters, equals, hashCode
    
    public User() {}
    
    public User(String email, String firstName, String lastName) {
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.status = UserStatus.ACTIVE;
    }
    
    // Business methods
    public String getFullName() {
        return firstName + " " + lastName;
    }
    
    public void activate() {
        this.status = UserStatus.ACTIVE;
    }
    
    public void deactivate() {
        this.status = UserStatus.INACTIVE;
    }
    
    public boolean isActive() {
        return this.status == UserStatus.ACTIVE;
    }
}

// Repository with custom queries
@Repository
public interface UserRepository extends JpaRepository<User, UUID>, JpaSpecificationExecutor<User> {
    
    Optional<User> findByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.status = :status ORDER BY u.createdAt DESC")
    Page<User> findByStatus(@Param("status") UserStatus status, Pageable pageable);
    
    @Query("SELECT u FROM User u WHERE " +
           "LOWER(u.firstName) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(u.lastName) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(u.email) LIKE LOWER(CONCAT('%', :searchTerm, '%'))")
    Page<User> searchUsers(@Param("searchTerm") String searchTerm, Pageable pageable);
    
    @Modifying
    @Query("UPDATE User u SET u.status = :newStatus WHERE u.status = :currentStatus AND u.updatedAt < :cutoffDate")
    int bulkUpdateInactiveUsers(@Param("currentStatus") UserStatus currentStatus, 
                                @Param("newStatus") UserStatus newStatus, 
                                @Param("cutoffDate") Instant cutoffDate);
    
    // Analytics queries
    @Query("SELECT u.status, COUNT(u) FROM User u GROUP BY u.status")
    List<Object[]> getUserStatusCounts();
    
    @Query("SELECT DATE_TRUNC('day', u.createdAt) as date, COUNT(u) FROM User u " +
           "WHERE u.createdAt >= :startDate GROUP BY DATE_TRUNC('day', u.createdAt) ORDER BY date")
    List<Object[]> getUserRegistrationStats(@Param("startDate") Instant startDate);
}

// ETL Pipeline Implementation with Spring Batch
@Component
public class UserDataETLPipeline {
    
    private final UserRepository userRepository;
    private final ExternalUserApiClient externalApiClient;
    private final DataQualityValidator dataQualityValidator;
    
    @Autowired
    public UserDataETLPipeline(UserRepository userRepository, 
                              ExternalUserApiClient externalApiClient,
                              DataQualityValidator dataQualityValidator) {
        this.userRepository = userRepository;
        this.externalApiClient = externalApiClient;
        this.dataQualityValidator = dataQualityValidator;
    }
    
    @Scheduled(fixedRate = 3600000) // Run every hour
    @Transactional
    public void processUserDataETL() {
        log.info("Starting User Data ETL process");
        
        try {
            // Extract
            List<ExternalUserData> externalUsers = extractExternalUserData();
            log.info("Extracted {} users from external system", externalUsers.size());
            
            // Transform
            List<User> transformedUsers = transformUserData(externalUsers);
            log.info("Transformed {} users for loading", transformedUsers.size());
            
            // Load
            List<User> savedUsers = loadUserData(transformedUsers);
            log.info("Successfully loaded {} users to database", savedUsers.size());
            
            // Data Quality Check
            DataQualityReport report = dataQualityValidator.validateUserData();
            if (report.hasIssues()) {
                log.warn("Data quality issues detected: {}", report.getIssues());
                // Send alert to data team
            }
            
        } catch (Exception e) {
            log.error("ETL process failed", e);
            // Send failure alert
            throw new ETLProcessException("User Data ETL process failed", e);
        }
    }
    
    private List<ExternalUserData> extractExternalUserData() {
        // Implement incremental data extraction
        Instant lastProcessed = getLastProcessedTimestamp();
        return externalApiClient.getUsersModifiedSince(lastProcessed);
    }
    
    private List<User> transformUserData(List<ExternalUserData> externalUsers) {
        return externalUsers.stream()
            .filter(this::isValidUser)
            .map(this::mapToUser)
            .collect(Collectors.toList());
    }
    
    private boolean isValidUser(ExternalUserData userData) {
        return userData.getEmail() != null && 
               userData.getEmail().contains("@") &&
               userData.getFirstName() != null &&
               userData.getLastName() != null;
    }
    
    private User mapToUser(ExternalUserData userData) {
        User user = new User();
        user.setEmail(userData.getEmail().toLowerCase().trim());
        user.setFirstName(cleanName(userData.getFirstName()));
        user.setLastName(cleanName(userData.getLastName()));
        user.setStatus(mapStatus(userData.getStatus()));
        return user;
    }
    
    private List<User> loadUserData(List<User> users) {
        List<User> savedUsers = new ArrayList<>();
        
        for (User user : users) {
            try {
                Optional<User> existing = userRepository.findByEmail(user.getEmail());
                if (existing.isPresent()) {
                    // Update existing user
                    User existingUser = existing.get();
                    existingUser.setFirstName(user.getFirstName());
                    existingUser.setLastName(user.getLastName());
                    existingUser.setStatus(user.getStatus());
                    savedUsers.add(userRepository.save(existingUser));
                } else {
                    // Create new user
                    savedUsers.add(userRepository.save(user));
                }
            } catch (DataIntegrityViolationException e) {
                log.warn("Failed to save user with email {}: {}", user.getEmail(), e.getMessage());
            }
        }
        
        return savedUsers;
    }
}

// Application Properties
# application.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/myapp
    username: ${DB_USERNAME:myapp}
    password: ${DB_PASSWORD:password}
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
      
  jpa:
    hibernate:
      ddl-auto: validate
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        show_sql: false
        format_sql: true
        jdbc:
          batch_size: 50
        order_inserts: true
        order_updates: true
        batch_versioned_data: true
        
  flyway:
    enabled: true
    locations: classpath:db/migration
    baseline-on-migrate: true
    validate-on-migrate: true
    
logging:
  level:
    org.hibernate.SQL: DEBUG
    org.hibernate.type.descriptor.sql.BasicBinder: TRACE
    org.springframework.jdbc.core: DEBUG
```

### SQL Server + .NET Core + Entity Framework

**Recommended Pattern:** Code-First approach with EF Core migrations and comprehensive data annotations

```csharp
// NuGet Packages
/*
<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="7.0.0" />
<PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="7.0.0" />
<PackageReference Include="Microsoft.Extensions.Logging" Version="7.0.0" />
*/

// Entity with comprehensive annotations
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;

[Table("Users")]
[Index(nameof(Email), IsUnique = true, Name = "IX_Users_Email")]
[Index(nameof(Status), Name = "IX_Users_Status")]
[Index(nameof(CreatedAt), Name = "IX_Users_CreatedAt")]
public class User
{
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public Guid Id { get; set; }
    
    [Required]
    [MaxLength(255)]
    [EmailAddress]
    public string Email { get; set; }
    
    [Required]
    [Column("password_hash")]
    [MaxLength(255)]
    public string PasswordHash { get; set; }
    
    [Required]
    [Column("first_name")]
    [MaxLength(100)]
    public string FirstName { get; set; }
    
    [Required]
    [Column("last_name")]
    [MaxLength(100)]
    public string LastName { get; set; }
    
    [Required]
    [MaxLength(20)]
    public UserStatus Status { get; set; } = UserStatus.Active;
    
    [Column("created_at")]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public DateTime CreatedAt { get; set; }
    
    [Column("updated_at")]
    [DatabaseGenerated(DatabaseGeneratedOption.Computed)]
    public DateTime UpdatedAt { get; set; }
    
    [Timestamp]
    public byte[] RowVersion { get; set; }
    
    // Navigation properties
    public virtual ICollection<UserRole> UserRoles { get; set; } = new List<UserRole>();
    public virtual ICollection<UserAudit> AuditTrail { get; set; } = new List<UserAudit>();
    
    // Business methods
    [NotMapped]
    public string FullName => $"{FirstName} {LastName}";
    
    public void Activate()
    {
        Status = UserStatus.Active;
    }
    
    public void Deactivate()
    {
        Status = UserStatus.Inactive;
    }
    
    public bool IsActive => Status == UserStatus.Active;
}

// DbContext with comprehensive configuration
public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }
    
    public DbSet<User> Users { get; set; }
    public DbSet<UserRole> UserRoles { get; set; }
    public DbSet<UserAudit> UserAudits { get; set; }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        
        // User configuration
        modelBuilder.Entity<User>(entity =>
        {
            entity.HasKey(e => e.Id);
            
            entity.Property(e => e.Id)
                .HasDefaultValueSql("NEWID()")
                .ValueGeneratedOnAdd();
            
            entity.Property(e => e.Email)
                .IsRequired()
                .HasMaxLength(255)
                .IsUnicode(false);
                
            entity.Property(e => e.Status)
                .HasConversion<string>()
                .HasMaxLength(20);
            
            entity.Property(e => e.CreatedAt)
                .HasDefaultValueSql("GETUTCDATE()")
                .ValueGeneratedOnAdd();
                
            entity.Property(e => e.UpdatedAt)
                .HasDefaultValueSql("GETUTCDATE()")
                .ValueGeneratedOnAddOrUpdate();
            
            // Indexes
            entity.HasIndex(e => e.Email)
                .IsUnique()
                .HasDatabaseName("IX_Users_Email");
                
            entity.HasIndex(e => e.Status)
                .HasDatabaseName("IX_Users_Status")
                .HasFilter("[Status] <> 'Inactive'");
                
            entity.HasIndex(e => e.CreatedAt)
                .HasDatabaseName("IX_Users_CreatedAt");
            
            // Relationships
            entity.HasMany(e => e.UserRoles)
                .WithOne(ur => ur.User)
                .HasForeignKey(ur => ur.UserId)
                .OnDelete(DeleteBehavior.Cascade);
                
            entity.HasMany(e => e.AuditTrail)
                .WithOne(ua => ua.User)
                .HasForeignKey(ua => ua.UserId)
                .OnDelete(DeleteBehavior.Restrict);
        });
        
        // Global query filters
        modelBuilder.Entity<User>().HasQueryFilter(u => u.Status != UserStatus.Deleted);
        
        // Seed data
        modelBuilder.Entity<User>().HasData(
            new User
            {
                Id = Guid.Parse("550e8400-e29b-41d4-a716-446655440000"),
                Email = "admin@company.com",
                FirstName = "System",
                LastName = "Administrator",
                Status = UserStatus.Active,
                PasswordHash = "$2a$10$...", // Hashed password
                CreatedAt = new DateTime(2024, 1, 1, 0, 0, 0, DateTimeKind.Utc)
            }
        );
    }
    
    public override async Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        // Update audit fields
        var entries = ChangeTracker.Entries<User>()
            .Where(e => e.State == EntityState.Added || e.State == EntityState.Modified);
            
        foreach (var entry in entries)
        {
            if (entry.State == EntityState.Added)
            {
                entry.Entity.CreatedAt = DateTime.UtcNow;
            }
            
            if (entry.State == EntityState.Modified)
            {
                entry.Entity.UpdatedAt = DateTime.UtcNow;
            }
        }
        
        return await base.SaveChangesAsync(cancellationToken);
    }
}

// Repository with LINQ-based queries
public interface IUserRepository : IRepository<User>
{
    Task<User?> GetByEmailAsync(string email);
    Task<PagedResult<User>> SearchUsersAsync(string searchTerm, int page, int pageSize);
    Task<Dictionary<UserStatus, int>> GetUserStatusCountsAsync();
    Task<int> BulkUpdateStatusAsync(UserStatus currentStatus, UserStatus newStatus, DateTime cutoffDate);
}

public class UserRepository : Repository<User>, IUserRepository
{
    public UserRepository(ApplicationDbContext context) : base(context) { }
    
    public async Task<User?> GetByEmailAsync(string email)
    {
        return await _context.Users
            .AsNoTracking()
            .FirstOrDefaultAsync(u => u.Email == email);
    }
    
    public async Task<PagedResult<User>> SearchUsersAsync(string searchTerm, int page, int pageSize)
    {
        var query = _context.Users.AsQueryable();
        
        if (!string.IsNullOrWhiteSpace(searchTerm))
        {
            var lowerSearchTerm = searchTerm.ToLower();
            query = query.Where(u => 
                u.FirstName.ToLower().Contains(lowerSearchTerm) ||
                u.LastName.ToLower().Contains(lowerSearchTerm) ||
                u.Email.ToLower().Contains(lowerSearchTerm)
            );
        }
        
        var totalCount = await query.CountAsync();
        
        var items = await query
            .OrderBy(u => u.FirstName)
            .ThenBy(u => u.LastName)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .AsNoTracking()
            .ToListAsync();
            
        return new PagedResult<User>
        {
            Items = items,
            TotalCount = totalCount,
            PageNumber = page,
            PageSize = pageSize,
            TotalPages = (int)Math.Ceiling((double)totalCount / pageSize)
        };
    }
    
    public async Task<Dictionary<UserStatus, int>> GetUserStatusCountsAsync()
    {
        return await _context.Users
            .GroupBy(u => u.Status)
            .Select(g => new { Status = g.Key, Count = g.Count() })
            .ToDictionaryAsync(x => x.Status, x => x.Count);
    }
    
    public async Task<int> BulkUpdateStatusAsync(UserStatus currentStatus, UserStatus newStatus, DateTime cutoffDate)
    {
        return await _context.Users
            .Where(u => u.Status == currentStatus && u.UpdatedAt < cutoffDate)
            .ExecuteUpdateAsync(u => u
                .SetProperty(p => p.Status, newStatus)
                .SetProperty(p => p.UpdatedAt, DateTime.UtcNow));
    }
}

// ETL Service with background processing
[Service]
public class UserDataETLService : BackgroundService
{
    private readonly IServiceProvider _serviceProvider;
    private readonly ILogger<UserDataETLService> _logger;
    private readonly Timer _timer;
    
    public UserDataETLService(IServiceProvider serviceProvider, ILogger<UserDataETLService> logger)
    {
        _serviceProvider = serviceProvider;
        _logger = logger;
        
        // Schedule ETL to run every hour
        _timer = new Timer(ProcessETL, null, TimeSpan.Zero, TimeSpan.FromHours(1));
    }
    
    private async void ProcessETL(object state)
    {
        using var scope = _serviceProvider.CreateScope();
        var userRepository = scope.ServiceProvider.GetRequiredService<IUserRepository>();
        var externalApiClient = scope.ServiceProvider.GetRequiredService<IExternalUserApiClient>();
        var dataQualityService = scope.ServiceProvider.GetRequiredService<IDataQualityService>();
        
        try
        {
            _logger.LogInformation("Starting User Data ETL process at {Time}", DateTime.UtcNow);
            
            // Extract
            var lastProcessed = await GetLastProcessedTimestampAsync();
            var externalUsers = await externalApiClient.GetUsersModifiedSinceAsync(lastProcessed);
            _logger.LogInformation("Extracted {Count} users from external system", externalUsers.Count);
            
            // Transform and Load
            var processedCount = 0;
            var errorCount = 0;
            
            await foreach (var batch in externalUsers.Batch(100))
            {
                using var transaction = await _context.Database.BeginTransactionAsync();
                
                try
                {
                    foreach (var externalUser in batch)
                    {
                        var transformedUser = await TransformUserDataAsync(externalUser);
                        
                        if (transformedUser != null)
                        {
                            await LoadUserDataAsync(userRepository, transformedUser);
                            processedCount++;
                        }
                        else
                        {
                            errorCount++;
                        }
                    }
                    
                    await transaction.CommitAsync();
                    _logger.LogDebug("Processed batch of {Count} users", batch.Count());
                }
                catch (Exception ex)
                {
                    await transaction.RollbackAsync();
                    _logger.LogError(ex, "Failed to process batch of users");
                    errorCount += batch.Count();
                }
            }
            
            // Data Quality Validation
            var qualityReport = await dataQualityService.ValidateUserDataAsync();
            if (qualityReport.HasIssues)
            {
                _logger.LogWarning("Data quality issues detected: {Issues}", 
                    string.Join(", ", qualityReport.Issues));
            }
            
            _logger.LogInformation(
                "ETL process completed. Processed: {Processed}, Errors: {Errors}, Quality Issues: {QualityIssues}",
                processedCount, errorCount, qualityReport.Issues.Count);
                
            await UpdateLastProcessedTimestampAsync(DateTime.UtcNow);
            
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "ETL process failed with exception");
            // Send alert to operations team
        }
    }
    
    private async Task<User> TransformUserDataAsync(ExternalUserData externalUser)
    {
        // Data validation
        if (string.IsNullOrWhiteSpace(externalUser.Email) ||
            string.IsNullOrWhiteSpace(externalUser.FirstName) ||
            string.IsNullOrWhiteSpace(externalUser.LastName))
        {
            _logger.LogWarning("Invalid user data for external ID {ExternalId}", externalUser.ExternalId);
            return null;
        }
        
        // Data transformation
        return new User
        {
            Email = externalUser.Email.ToLowerInvariant().Trim(),
            FirstName = CleanName(externalUser.FirstName),
            LastName = CleanName(externalUser.LastName),
            Status = MapStatus(externalUser.Status)
        };
    }
    
    private string CleanName(string name)
    {
        return name?.Trim()
            .Replace("  ", " ")
            .ToTitleCase() ?? string.Empty;
    }
    
    private UserStatus MapStatus(string externalStatus)
    {
        return externalStatus?.ToLowerInvariant() switch
        {
            "active" => UserStatus.Active,
            "inactive" => UserStatus.Inactive,
            "suspended" => UserStatus.Suspended,
            _ => UserStatus.Active
        };
    }
}

// Startup Configuration
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddDbContext<ApplicationDbContext>(options =>
            options.UseSqlServer(connectionString, sqlOptions =>
            {
                sqlOptions.EnableRetryOnFailure(
                    maxRetryCount: 3,
                    maxRetryDelay: TimeSpan.FromSeconds(5),
                    errorNumbersToAdd: null);
                sqlOptions.CommandTimeout(30);
            })
            .EnableSensitiveDataLogging(isDevelopment)
            .EnableDetailedErrors(isDevelopment));
            
        services.AddScoped<IUserRepository, UserRepository>();
        services.AddHostedService<UserDataETLService>();
        services.AddTransient<IDataQualityService, DataQualityService>();
    }
}
```

## 📊 Data Quality and Monitoring

### Data Quality Framework
- **Completeness** - No missing required values
- **Accuracy** - Data correctly represents reality
- **Consistency** - Data is uniform across systems
- **Validity** - Data conforms to defined formats
- **Timeliness** - Data is current and available when needed

**Quality Checks Implementation:**
```sql
-- Data quality validation queries
-- Completeness check
SELECT COUNT(*) as missing_emails 
FROM users 
WHERE email IS NULL OR email = '';

-- Accuracy check
SELECT COUNT(*) as invalid_emails
FROM users 
WHERE email !~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';

-- Consistency check
SELECT status, COUNT(*) 
FROM users 
GROUP BY status 
HAVING status NOT IN ('active', 'inactive', 'suspended');
```

### Performance Optimization
- **Query optimization** with execution plan analysis
- **Index tuning** for common query patterns
- **Partitioning** for large tables
- **Materialized views** for complex aggregations
- **Connection pooling** and resource management

## 🔧 Analytics and Reporting

### Data Warehouse Design
- **Star schema** or snowflake schema for analytics
- **Dimension tables** for business entities
- **Fact tables** for business events and metrics
- **Slowly changing dimensions** handling
- **Data marts** for specific business domains

**Example Analytics Schema:**
```sql
-- Fact table for sales analytics
CREATE TABLE fact_sales (
    sale_id UUID PRIMARY KEY,
    customer_id UUID REFERENCES dim_customers(id),
    product_id UUID REFERENCES dim_products(id),
    date_id INTEGER REFERENCES dim_date(date_id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dimension table for customer analytics
CREATE TABLE dim_customers (
    id UUID PRIMARY KEY,
    customer_code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    segment VARCHAR(50),
    region VARCHAR(100),
    registration_date DATE,
    is_active BOOLEAN DEFAULT true
);
```

### Reporting and Dashboards
- **Business intelligence** tool integration
- **Real-time dashboards** for operational metrics
- **Scheduled reports** for business stakeholders
- **Self-service analytics** capabilities
- **Data export** and API access for external tools

## 🚀 Deployment and Operations

### Database Operations
- **Backup strategy** with point-in-time recovery
- **High availability** setup with replication
- **Disaster recovery** procedures and testing
- **Performance monitoring** and alerting
- **Capacity planning** and resource scaling

### ETL Operations
- **Job scheduling** and dependency management
- **Error handling** and retry mechanisms
- **Data lineage** tracking and documentation
- **Performance monitoring** and optimization
- **Alerting** for failed or delayed jobs

**Monitoring Dashboards:**
- **ETL job status** and execution times
- **Data quality metrics** and trend analysis
- **Database performance** (query time, connections, locks)
- **Storage utilization** and growth trends
- **Business metrics** derived from data processing

## 📤 Deliverables

- **Database Schema** with tables, indexes, and constraints
- **Migration Scripts** for schema deployment and updates
- **ETL Pipeline Code** with comprehensive error handling
- **Data Quality Rules** and validation procedures
- **Performance Tuning** recommendations and implementation
- **Monitoring Setup** with alerts and dashboards
- **Documentation** for data models, processes, and operations

## 🤝 Collaboration Points

**With api-engineer:** Database access patterns and query optimization
**With software-architect:** Data architecture alignment and integration patterns
**With security-engineer:** Data encryption, access controls, and compliance
**With qa-engineer:** Data testing strategies and quality validation
**With business-analyst:** Business rule validation and reporting requirements

### MongoDB + Node.js + TypeORM

**Recommended Pattern:** Document-based modeling with aggregation pipelines and change streams

```typescript
// MongoDB Entity with TypeORM
import { Entity, ObjectIdColumn, ObjectId, Column, CreateDateColumn, UpdateDateColumn, Index } from 'typeorm';

@Entity('users')
@Index(['email'], { unique: true })
@Index(['status'])
@Index(['createdAt'])
export class User {
  @ObjectIdColumn()
  _id: ObjectId;
  
  @Column({ unique: true, lowercase: true })
  email: string;
  
  @Column({ select: false }) // Exclude from default queries
  passwordHash: string;
  
  @Column()
  firstName: string;
  
  @Column()
  lastName: string;
  
  @Column({ default: 'active', enum: ['active', 'inactive', 'suspended'] })
  status: 'active' | 'inactive' | 'suspended';
  
  @Column({ type: 'object' })
  profile: {
    avatar?: string;
    bio?: string;
    location?: string;
    preferences: {
      notifications: boolean;
      theme: 'light' | 'dark';
      language: string;
    };
  };
  
  @Column({ type: 'array' })
  roles: string[];
  
  @Column({ type: 'array' })
  tags: string[];
  
  @CreateDateColumn()
  createdAt: Date;
  
  @UpdateDateColumn()
  updatedAt: Date;
  
  @Column({ default: 1 })
  version: number;
  
  // Virtual properties
  get id(): string {
    return this._id.toHexString();
  }
  
  get fullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
  
  // Business methods
  activate(): void {
    this.status = 'active';
  }
  
  deactivate(): void {
    this.status = 'inactive';
  }
  
  isActive(): boolean {
    return this.status === 'active';
  }
  
  addRole(role: string): void {
    if (!this.roles.includes(role)) {
      this.roles.push(role);
    }
  }
  
  removeRole(role: string): void {
    this.roles = this.roles.filter(r => r !== role);
  }
}

// Repository with MongoDB-specific operations
import { MongoRepository, getMongoRepository } from 'typeorm';
import { ObjectId } from 'mongodb';

export class UserRepository {
  private repository: MongoRepository<User>;
  
  constructor() {
    this.repository = getMongoRepository(User);
  }
  
  async findById(id: string): Promise<User | undefined> {
    return this.repository.findOne(new ObjectId(id));
  }
  
  async findByEmail(email: string): Promise<User | undefined> {
    return this.repository.findOne({ email: email.toLowerCase() });
  }
  
  async searchUsers(searchTerm: string, page: number = 1, limit: number = 20): Promise<{
    users: User[];
    total: number;
    page: number;
    totalPages: number;
  }> {
    const skip = (page - 1) * limit;
    
    const searchRegex = new RegExp(searchTerm, 'i');
    const query = {
      $or: [
        { firstName: searchRegex },
        { lastName: searchRegex },
        { email: searchRegex }
      ]
    };
    
    const [users, total] = await Promise.all([
      this.repository.find({
        where: query,
        skip,
        take: limit,
        order: { createdAt: 'DESC' }
      }),
      this.repository.count(query)
    ]);
    
    return {
      users,
      total,
      page,
      totalPages: Math.ceil(total / limit)
    };
  }
  
  async getUsersByStatus(status: string): Promise<User[]> {
    return this.repository.find({ where: { status } });
  }
  
  async getUserAnalytics(): Promise<any[]> {
    return this.repository.aggregate([
      {
        $group: {
          _id: '$status',
          count: { $sum: 1 },
          averageAge: {
            $avg: {
              $divide: [
                { $subtract: [new Date(), '$createdAt'] },
                1000 * 60 * 60 * 24 * 365.25 // Convert to years
              ]
            }
          }
        }
      },
      {
        $sort: { count: -1 }
      }
    ]).toArray();
  }
  
  async getRegistrationTrends(days: number = 30): Promise<any[]> {
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days);
    
    return this.repository.aggregate([
      {
        $match: {
          createdAt: { $gte: startDate }
        }
      },
      {
        $group: {
          _id: {
            year: { $year: '$createdAt' },
            month: { $month: '$createdAt' },
            day: { $dayOfMonth: '$createdAt' }
          },
          count: { $sum: 1 }
        }
      },
      {
        $sort: { '_id.year': 1, '_id.month': 1, '_id.day': 1 }
      }
    ]).toArray();
  }
  
  async bulkUpdateUsers(filter: any, update: any): Promise<number> {
    const result = await this.repository.updateMany(filter, { $set: update });
    return result.modifiedCount;
  }
  
  async createIndexes(): Promise<void> {
    const collection = this.repository.manager.connection.db.collection('users');
    
    await Promise.all([
      collection.createIndex({ email: 1 }, { unique: true, background: true }),
      collection.createIndex({ status: 1 }, { background: true }),
      collection.createIndex({ createdAt: 1 }, { background: true }),
      collection.createIndex({ firstName: 'text', lastName: 'text', email: 'text' }, {
        name: 'text_search_index',
        background: true
      }),
      collection.createIndex({ 'profile.location': 1 }, { background: true, sparse: true })
    ]);
  }
}

// ETL Pipeline with MongoDB Change Streams
import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';
import { ChangeStream, ChangeStreamDocument } from 'mongodb';

@Injectable()
export class UserDataETLService {
  private readonly logger = new Logger(UserDataETLService.name);
  private changeStream: ChangeStream;
  
  constructor(
    private readonly userRepository: UserRepository,
    private readonly externalApiService: ExternalApiService,
    private readonly dataQualityService: DataQualityService
  ) {}
  
  async onModuleInit() {
    await this.setupChangeStreamListeners();
  }
  
  async setupChangeStreamListeners() {
    const collection = this.userRepository.repository.manager.connection.db.collection('users');
    
    this.changeStream = collection.watch([
      {
        $match: {
          operationType: { $in: ['insert', 'update', 'delete'] }
        }
      }
    ]);
    
    this.changeStream.on('change', (change: ChangeStreamDocument) => {
      this.logger.log(`User collection change detected: ${change.operationType}`);
      this.handleUserChange(change);
    });
    
    this.logger.log('Change stream listeners configured');
  }
  
  private async handleUserChange(change: ChangeStreamDocument) {
    try {
      switch (change.operationType) {
        case 'insert':
          await this.handleUserCreated(change.fullDocument);
          break;
        case 'update':
          await this.handleUserUpdated(change.documentKey, change.updateDescription);
          break;
        case 'delete':
          await this.handleUserDeleted(change.documentKey);
          break;
      }
    } catch (error) {
      this.logger.error('Error handling user change', error);
    }
  }
  
  @Cron(CronExpression.EVERY_HOUR)
  async processHourlyETL() {
    this.logger.log('Starting hourly User Data ETL process');
    
    try {
      // Extract
      const lastProcessed = await this.getLastProcessedTimestamp();
      const externalUsers = await this.externalApiService.getUsersModifiedSince(lastProcessed);
      this.logger.log(`Extracted ${externalUsers.length} users from external system`);
      
      // Transform and Load
      const results = {
        created: 0,
        updated: 0,
        errors: 0
      };
      
      for (const externalUser of externalUsers) {
        try {
          const transformedUser = await this.transformUserData(externalUser);
          const result = await this.loadUserData(transformedUser);
          
          if (result.upsertedId) {
            results.created++;
          } else {
            results.updated++;
          }
        } catch (error) {
          this.logger.warn(`Failed to process user ${externalUser.id}: ${error.message}`);
          results.errors++;
        }
      }
      
      // Data Quality Validation
      const qualityReport = await this.dataQualityService.validateUserData();
      if (qualityReport.hasIssues) {
        this.logger.warn('Data quality issues detected', qualityReport.issues);
      }
      
      this.logger.log(`ETL completed. Created: ${results.created}, Updated: ${results.updated}, Errors: ${results.errors}`);
      
      await this.updateLastProcessedTimestamp();
      
    } catch (error) {
      this.logger.error('ETL process failed', error);
      throw error;
    }
  }
  
  private async transformUserData(externalUser: any): Promise<Partial<User>> {
    // Data validation and transformation
    if (!this.isValidExternalUser(externalUser)) {
      throw new Error('Invalid external user data');
    }
    
    return {
      email: externalUser.email.toLowerCase().trim(),
      firstName: this.cleanString(externalUser.firstName),
      lastName: this.cleanString(externalUser.lastName),
      status: this.mapStatus(externalUser.status),
      profile: {
        avatar: externalUser.profile?.avatar,
        bio: this.cleanString(externalUser.profile?.bio),
        location: this.cleanString(externalUser.profile?.location),
        preferences: {
          notifications: externalUser.profile?.preferences?.notifications ?? true,
          theme: externalUser.profile?.preferences?.theme ?? 'light',
          language: externalUser.profile?.preferences?.language ?? 'en'
        }
      },
      roles: externalUser.roles || ['user'],
      tags: externalUser.tags || []
    };
  }
  
  private async loadUserData(userData: Partial<User>): Promise<any> {
    const collection = this.userRepository.repository.manager.connection.db.collection('users');
    
    return collection.replaceOne(
      { email: userData.email },
      { ...userData, updatedAt: new Date() },
      { upsert: true }
    );
  }
  
  private isValidExternalUser(user: any): boolean {
    return user &&
           user.email &&
           user.email.includes('@') &&
           user.firstName &&
           user.lastName;
  }
  
  private cleanString(str: string | undefined): string {
    return str?.trim().replace(/\s+/g, ' ') || '';
  }
  
  private mapStatus(externalStatus: string): 'active' | 'inactive' | 'suspended' {
    switch (externalStatus?.toLowerCase()) {
      case 'active':
      case 'enabled':
        return 'active';
      case 'inactive':
      case 'disabled':
        return 'inactive';
      case 'suspended':
      case 'blocked':
        return 'suspended';
      default:
        return 'active';
    }
  }
  
  async onModuleDestroy() {
    if (this.changeStream) {
      await this.changeStream.close();
      this.logger.log('Change stream closed');
    }
  }
}

// Data Quality Service
@Injectable()
export class DataQualityService {
  private readonly logger = new Logger(DataQualityService.name);
  
  constructor(private readonly userRepository: UserRepository) {}
  
  async validateUserData(): Promise<{
    hasIssues: boolean;
    issues: string[];
    metrics: any;
  }> {
    const issues: string[] = [];
    const collection = this.userRepository.repository.manager.connection.db.collection('users');
    
    // Completeness checks
    const missingEmails = await collection.countDocuments({
      $or: [{ email: null }, { email: '' }]
    });
    if (missingEmails > 0) {
      issues.push(`${missingEmails} users with missing email addresses`);
    }
    
    // Validity checks
    const invalidEmails = await collection.countDocuments({
      email: { $not: /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/ }
    });
    if (invalidEmails > 0) {
      issues.push(`${invalidEmails} users with invalid email formats`);
    }
    
    // Consistency checks
    const invalidStatuses = await collection.countDocuments({
      status: { $nin: ['active', 'inactive', 'suspended'] }
    });
    if (invalidStatuses > 0) {
      issues.push(`${invalidStatuses} users with invalid status values`);
    }
    
    // Duplicate checks
    const duplicateEmails = await collection.aggregate([
      {
        $group: {
          _id: '$email',
          count: { $sum: 1 }
        }
      },
      {
        $match: { count: { $gt: 1 } }
      },
      {
        $count: 'duplicates'
      }
    ]).toArray();
    
    const duplicateCount = duplicateEmails[0]?.duplicates || 0;
    if (duplicateCount > 0) {
      issues.push(`${duplicateCount} duplicate email addresses found`);
    }
    
    // Performance metrics
    const metrics = await collection.aggregate([
      {
        $group: {
          _id: null,
          totalUsers: { $sum: 1 },
          activeUsers: {
            $sum: { $cond: [{ $eq: ['$status', 'active'] }, 1, 0] }
          },
          averageRoles: { $avg: { $size: '$roles' } },
          usersWithProfiles: {
            $sum: { $cond: [{ $ne: ['$profile', null] }, 1, 0] }
          }
        }
      }
    ]).toArray();
    
    return {
      hasIssues: issues.length > 0,
      issues,
      metrics: metrics[0] || {}
    };
  }
}
```

### Python + SQLAlchemy + PostgreSQL

**Recommended Pattern:** SQLAlchemy ORM with Alembic migrations and async support

```python
# Database Models with SQLAlchemy
from sqlalchemy import Column, String, DateTime, Boolean, Integer, Text, Enum, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from datetime import datetime
from typing import Optional, List, Dict, Any

Base = declarative_base()

class UserStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('ix_users_email', 'email', unique=True),
        Index('ix_users_status', 'status'),
        Index('ix_users_created_at', 'created_at'),
        Index('ix_users_full_text', 'first_name', 'last_name', 'email', postgresql_using='gin'),
    )
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.ACTIVE, index=True)
    
    # JSON fields for flexible data
    profile = Column(JSONB, nullable=True)
    preferences = Column(JSONB, nullable=True)
    metadata = Column(JSONB, nullable=True)
    
    # Audit fields
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    version = Column(Integer, default=1, nullable=False)
    
    # Relationships
    # user_roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")
    # audit_logs = relationship("UserAudit", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, status={self.status.value})>"
    
    @property
    def full_name(self) -> str:
        """Return the user's full name"""
        return f"{self.first_name} {self.last_name}"
    
    def activate(self) -> None:
        """Activate the user account"""
        self.status = UserStatus.ACTIVE
        self.updated_at = datetime.utcnow()
    
    def deactivate(self) -> None:
        """Deactivate the user account"""
        self.status = UserStatus.INACTIVE
        self.updated_at = datetime.utcnow()
    
    def is_active(self) -> bool:
        """Check if the user is active"""
        return self.status == UserStatus.ACTIVE
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary representation"""
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'status': self.status.value,
            'profile': self.profile,
            'preferences': self.preferences,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'version': self.version
        }

# Repository Pattern with async support
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func, update, delete, and_, or_
from typing import Optional, List, Dict, Any
import asyncio
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, user: User) -> User:
        """Create a new user"""
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        """Get user by ID"""
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        result = await self.session.execute(
            select(User).where(User.email == email.lower())
        )
        return result.scalar_one_or_none()
    
    async def search_users(
        self, 
        search_term: Optional[str] = None,
        status: Optional[UserStatus] = None,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Search users with pagination"""
        query = select(User)
        count_query = select(func.count(User.id))
        
        # Apply filters
        filters = []
        if search_term:
            search_filter = or_(
                User.first_name.ilike(f"%{search_term}%"),
                User.last_name.ilike(f"%{search_term}%"),
                User.email.ilike(f"%{search_term}%")
            )
            filters.append(search_filter)
        
        if status:
            filters.append(User.status == status)
        
        if filters:
            query = query.where(and_(*filters))
            count_query = count_query.where(and_(*filters))
        
        # Get total count
        total_result = await self.session.execute(count_query)
        total = total_result.scalar()
        
        # Get paginated results
        query = query.order_by(User.created_at.desc()).offset(offset).limit(limit)
        result = await self.session.execute(query)
        users = result.scalars().all()
        
        return {
            'users': [user.to_dict() for user in users],
            'total': total,
            'limit': limit,
            'offset': offset,
            'pages': (total + limit - 1) // limit if total > 0 else 0
        }
    
    async def update(self, user: User) -> User:
        """Update existing user"""
        user.updated_at = datetime.utcnow()
        user.version += 1
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def bulk_update_status(
        self, 
        current_status: UserStatus, 
        new_status: UserStatus, 
        cutoff_date: datetime
    ) -> int:
        """Bulk update user status"""
        result = await self.session.execute(
            update(User)
            .where(
                and_(
                    User.status == current_status,
                    User.updated_at < cutoff_date
                )
            )
            .values(
                status=new_status,
                updated_at=datetime.utcnow(),
                version=User.version + 1
            )
        )
        await self.session.commit()
        return result.rowcount
    
    async def get_analytics(self) -> Dict[str, Any]:
        """Get user analytics"""
        # Status distribution
        status_result = await self.session.execute(
            select(User.status, func.count(User.id))
            .group_by(User.status)
        )
        status_counts = {status.value: count for status, count in status_result.all()}
        
        # Registration trends (last 30 days)
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        trend_result = await self.session.execute(
            select(
                func.date_trunc('day', User.created_at).label('date'),
                func.count(User.id).label('count')
            )
            .where(User.created_at >= thirty_days_ago)
            .group_by(func.date_trunc('day', User.created_at))
            .order_by('date')
        )
        registration_trends = [
            {'date': date.isoformat(), 'count': count}
            for date, count in trend_result.all()
        ]
        
        return {
            'status_distribution': status_counts,
            'registration_trends': registration_trends,
            'total_users': sum(status_counts.values())
        }

# ETL Service with async processing
import asyncio
import aiohttp
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from contextlib import asynccontextmanager

@dataclass
class ExternalUserData:
    external_id: str
    email: str
    first_name: str
    last_name: str
    status: str
    profile: Optional[Dict[str, Any]] = None
    modified_at: Optional[datetime] = None

class UserDataETLService:
    def __init__(
        self, 
        user_repository: UserRepository,
        external_api_client: 'ExternalUserApiClient',
        data_quality_service: 'DataQualityService'
    ):
        self.user_repository = user_repository
        self.external_api_client = external_api_client
        self.data_quality_service = data_quality_service
        self.logger = logging.getLogger(__name__)
    
    async def process_etl_pipeline(self) -> Dict[str, Any]:
        """Execute the complete ETL pipeline"""
        start_time = datetime.utcnow()
        self.logger.info(f"Starting User Data ETL process at {start_time}")
        
        try:
            # Extract
            external_users = await self.extract_external_data()
            self.logger.info(f"Extracted {len(external_users)} users from external system")
            
            # Transform and Load
            results = await self.transform_and_load(external_users)
            
            # Data Quality Validation
            quality_report = await self.data_quality_service.validate_user_data()
            
            end_time = datetime.utcnow()
            duration = (end_time - start_time).total_seconds()
            
            summary = {
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration_seconds': duration,
                'processed': results['processed'],
                'created': results['created'],
                'updated': results['updated'],
                'errors': results['errors'],
                'quality_issues': len(quality_report.get('issues', []))
            }
            
            self.logger.info(f"ETL completed successfully: {summary}")
            return summary
            
        except Exception as e:
            self.logger.error(f"ETL process failed: {e}", exc_info=True)
            raise
    
    async def extract_external_data(self) -> List[ExternalUserData]:
        """Extract data from external systems"""
        last_processed = await self.get_last_processed_timestamp()
        
        # Fetch data from external API
        external_users = await self.external_api_client.get_users_modified_since(
            last_processed
        )
        
        return external_users
    
    async def transform_and_load(self, external_users: List[ExternalUserData]) -> Dict[str, int]:
        """Transform and load user data"""
        results = {
            'processed': 0,
            'created': 0,
            'updated': 0,
            'errors': 0
        }
        
        # Process in batches for better performance
        batch_size = 100
        for i in range(0, len(external_users), batch_size):
            batch = external_users[i:i + batch_size]
            batch_results = await self.process_batch(batch)
            
            for key in results:
                results[key] += batch_results[key]
            
            self.logger.debug(f"Processed batch {i//batch_size + 1}, results: {batch_results}")
        
        return results
    
    async def process_batch(self, batch: List[ExternalUserData]) -> Dict[str, int]:
        """Process a batch of external user data"""
        results = {'processed': 0, 'created': 0, 'updated': 0, 'errors': 0}
        
        async with self.user_repository.session.begin():
            for external_user in batch:
                try:
                    # Transform data
                    user_data = await self.transform_user_data(external_user)
                    
                    if user_data:
                        # Load data
                        is_new = await self.load_user_data(user_data)
                        results['processed'] += 1
                        
                        if is_new:
                            results['created'] += 1
                        else:
                            results['updated'] += 1
                    else:
                        results['errors'] += 1
                        
                except Exception as e:
                    self.logger.warning(
                        f"Failed to process external user {external_user.external_id}: {e}"
                    )
                    results['errors'] += 1
        
        return results
    
    async def transform_user_data(self, external_user: ExternalUserData) -> Optional[Dict[str, Any]]:
        """Transform external user data to internal format"""
        # Data validation
        if not self.is_valid_external_user(external_user):
            self.logger.warning(f"Invalid external user data: {external_user.external_id}")
            return None
        
        # Data transformation
        return {
            'email': external_user.email.lower().strip(),
            'first_name': self.clean_string(external_user.first_name),
            'last_name': self.clean_string(external_user.last_name),
            'status': self.map_status(external_user.status),
            'profile': self.transform_profile(external_user.profile),
            'metadata': {
                'external_id': external_user.external_id,
                'last_sync': datetime.utcnow().isoformat()
            }
        }
    
    async def load_user_data(self, user_data: Dict[str, Any]) -> bool:
        """Load user data into database"""
        existing_user = await self.user_repository.get_by_email(user_data['email'])
        
        if existing_user:
            # Update existing user
            for key, value in user_data.items():
                if key != 'email':  # Don't update email
                    setattr(existing_user, key, value)
            
            await self.user_repository.update(existing_user)
            return False
        else:
            # Create new user
            new_user = User(**user_data)
            await self.user_repository.create(new_user)
            return True
    
    def is_valid_external_user(self, user: ExternalUserData) -> bool:
        """Validate external user data"""
        return (
            user.email and '@' in user.email and
            user.first_name and len(user.first_name.strip()) > 0 and
            user.last_name and len(user.last_name.strip()) > 0
        )
    
    def clean_string(self, text: str) -> str:
        """Clean and normalize string data"""
        if not text:
            return ''
        return ' '.join(text.strip().split())
    
    def map_status(self, external_status: str) -> UserStatus:
        """Map external status to internal status"""
        status_mapping = {
            'active': UserStatus.ACTIVE,
            'enabled': UserStatus.ACTIVE,
            'inactive': UserStatus.INACTIVE,
            'disabled': UserStatus.INACTIVE,
            'suspended': UserStatus.SUSPENDED,
            'blocked': UserStatus.SUSPENDED
        }
        
        return status_mapping.get(external_status.lower(), UserStatus.ACTIVE)
    
    def transform_profile(self, external_profile: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Transform external profile data"""
        if not external_profile:
            return {}
        
        return {
            'avatar': external_profile.get('avatar_url'),
            'bio': self.clean_string(external_profile.get('bio', '')),
            'location': self.clean_string(external_profile.get('location', '')),
            'preferences': {
                'notifications': external_profile.get('notifications', True),
                'theme': external_profile.get('theme', 'light'),
                'language': external_profile.get('language', 'en')
            }
        }
    
    async def get_last_processed_timestamp(self) -> datetime:
        """Get the last processed timestamp"""
        # Implementation would retrieve from a configuration table or file
        return datetime.utcnow() - timedelta(hours=1)

# Scheduled ETL execution
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

class ETLScheduler:
    def __init__(self, etl_service: UserDataETLService):
        self.etl_service = etl_service
        self.scheduler = AsyncIOScheduler()
        self.logger = logging.getLogger(__name__)
    
    def start(self):
        """Start the ETL scheduler"""
        # Schedule ETL to run every hour
        self.scheduler.add_job(
            self.run_etl,
            CronTrigger(minute=0),  # Run at the top of every hour
            id='user_data_etl',
            name='User Data ETL Pipeline',
            replace_existing=True
        )
        
        self.scheduler.start()
        self.logger.info("ETL scheduler started")
    
    async def run_etl(self):
        """Execute ETL pipeline"""
        try:
            results = await self.etl_service.process_etl_pipeline()
            self.logger.info(f"Scheduled ETL completed: {results}")
        except Exception as e:
            self.logger.error(f"Scheduled ETL failed: {e}", exc_info=True)
    
    def stop(self):
        """Stop the ETL scheduler"""
        if self.scheduler.running:
            self.scheduler.shutdown()
            self.logger.info("ETL scheduler stopped")

# Data Quality Service
class DataQualityService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.logger = logging.getLogger(__name__)
    
    async def validate_user_data(self) -> Dict[str, Any]:
        """Comprehensive data quality validation"""
        issues = []
        metrics = {}
        
        # Completeness checks
        missing_emails = await self.user_repository.session.execute(
            select(func.count(User.id))
            .where(or_(User.email.is_(None), User.email == ''))
        )
        missing_count = missing_emails.scalar()
        if missing_count > 0:
            issues.append(f"{missing_count} users with missing email addresses")
        
        # Validity checks
        invalid_emails = await self.user_repository.session.execute(
            select(func.count(User.id))
            .where(~User.email.op('~')(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'))
        )
        invalid_count = invalid_emails.scalar()
        if invalid_count > 0:
            issues.append(f"{invalid_count} users with invalid email formats")
        
        # Duplicate checks
        duplicate_emails = await self.user_repository.session.execute(
            select(func.count(User.email))
            .group_by(User.email)
            .having(func.count(User.email) > 1)
        )
        duplicate_count = len(duplicate_emails.all())
        if duplicate_count > 0:
            issues.append(f"{duplicate_count} duplicate email addresses found")
        
        # Performance metrics
        total_users = await self.user_repository.session.execute(
            select(func.count(User.id))
        )
        metrics['total_users'] = total_users.scalar()
        
        status_distribution = await self.user_repository.session.execute(
            select(User.status, func.count(User.id))
            .group_by(User.status)
        )
        metrics['status_distribution'] = {
            status.value: count for status, count in status_distribution.all()
        }
        
        return {
            'has_issues': len(issues) > 0,
            'issues': issues,
            'metrics': metrics
        }

# Configuration and Database Setup
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql+asyncpg://user:password@localhost:5432/myapp'
)

# Engine configuration with optimizations
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL debugging
    pool_size=20,
    max_overflow=30,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)

# Session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency injection
async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Alembic Migration Script Example
# migrations/versions/001_create_users_table.py
"""
Create users table

Revision ID: 001
Revises: 
Create Date: 2024-01-01 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', 'SUSPENDED', name='user_status'), nullable=False, server_default='ACTIVE'),
        sa.Column('profile', JSONB, nullable=True),
        sa.Column('preferences', JSONB, nullable=True),
        sa.Column('metadata', JSONB, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('version', sa.Integer, nullable=False, server_default='1')
    )
    
    # Create indexes
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_status', 'users', ['status'])
    op.create_index('ix_users_created_at', 'users', ['created_at'])
    op.create_index('ix_users_full_text', 'users', ['first_name', 'last_name', 'email'], postgresql_using='gin')
    
    # Create trigger for updated_at
    op.execute("""
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            NEW.version = OLD.version + 1;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        
        CREATE TRIGGER update_users_updated_at
            BEFORE UPDATE ON users
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
    """)

def downgrade() -> None:
    op.drop_table('users')
    op.execute('DROP FUNCTION IF EXISTS update_updated_at_column() CASCADE;')

# FastAPI Application Integration
from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI(title="User Management API")

# Pydantic models
class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    profile: Optional[Dict[str, Any]] = None

class UserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    status: str
    profile: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime

class UserSearchResponse(BaseModel):
    users: List[UserResponse]
    total: int
    limit: int
    offset: int
    pages: int

@app.get("/users/search", response_model=UserSearchResponse)
async def search_users(
    q: Optional[str] = Query(None, description="Search term"),
    status: Optional[str] = Query(None, description="User status filter"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    session: AsyncSession = Depends(get_async_session)
):
    """Search users with filters and pagination"""
    user_repository = UserRepository(session)
    
    status_enum = None
    if status:
        try:
            status_enum = UserStatus(status.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid status value")
    
    result = await user_repository.search_users(
        search_term=q,
        status=status_enum,
        limit=limit,
        offset=offset
    )
    
    return UserSearchResponse(**result)

@app.get("/users/analytics")
async def get_user_analytics(
    session: AsyncSession = Depends(get_async_session)
):
    """Get user analytics and metrics"""
    user_repository = UserRepository(session)
    analytics = await user_repository.get_analytics()
    return analytics

@app.post("/etl/trigger")
async def trigger_etl(
    session: AsyncSession = Depends(get_async_session)
):
    """Manually trigger ETL process"""
    user_repository = UserRepository(session)
    # Initialize required services
    etl_service = UserDataETLService(
        user_repository,
        external_api_client,  # Would be injected
        data_quality_service   # Would be injected
    )
    
    results = await etl_service.process_etl_pipeline()
    return {"message": "ETL process completed", "results": results}
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic database patterns:

```yaml
# Generic Database Design Configuration
database:
  modeling_approach: "relational"  # or "document", "key-value", "graph"
  
  design_principles:
    - "normalized_schema_3nf_or_higher"
    - "primary_keys_and_foreign_keys"
    - "appropriate_indexes_for_queries"
    - "audit_fields_created_updated"
    - "version_control_for_schema_changes"
    
  performance_optimization:
    - "query_optimization_with_execution_plans"
    - "index_strategy_for_common_queries"
    - "partitioning_for_large_tables"
    - "connection_pooling"
    - "read_replicas_for_scaling"
    
  data_quality:
    - "completeness_validation"
    - "accuracy_verification"
    - "consistency_checks"
    - "uniqueness_constraints"
    - "referential_integrity"

etl_pipeline:
  architecture: "extract_transform_load"
  
  extract_patterns:
    - "full_extraction_for_initial_load"
    - "incremental_extraction_for_updates"
    - "change_data_capture_for_real_time"
    
  transform_patterns:
    - "data_cleansing_and_standardization"
    - "business_rule_application"
    - "data_enrichment_from_references"
    - "aggregation_and_summarization"
    
  load_patterns:
    - "batch_loading_for_large_volumes"
    - "upsert_operations_for_updates"
    - "bulk_insert_for_performance"
    - "error_handling_and_recovery"
    
  scheduling:
    - "cron_based_scheduling"
    - "dependency_management"
    - "error_alerting"
    - "performance_monitoring"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Database system** from primary_language and infrastructure preferences (PostgreSQL for Java/Python, SQL Server for .NET, MongoDB for document-based needs)
- **ORM framework** based on backend technology (Hibernate, Entity Framework, TypeORM, SQLAlchemy)
- **Data volume and complexity** to select appropriate modeling approaches and performance optimizations
- **Business domain** for compliance requirements, audit needs, and data retention policies

### 2. Database Design Approach

Select modeling patterns based on detected requirements:
- **Relational databases**: Normalized schemas with appropriate indexes and constraints
- **Document databases**: Flexible schemas with embedded documents and aggregation pipelines
- **Hybrid approaches**: JSON fields in relational databases for flexible data requirements
- **Performance optimization**: Partitioning, indexing, and caching strategies based on access patterns

### 3. ETL Implementation Strategy

Apply technology-specific ETL patterns:
- **Batch processing**: Scheduled ETL jobs for regular data synchronization
- **Real-time processing**: Change streams and event-driven architectures for immediate updates
- **Data quality**: Validation rules and monitoring for data integrity and consistency
- **Error handling**: Comprehensive error handling, retry mechanisms, and alerting

### 4. Success Criteria

Database and ETL validation checklist:
- **Technology alignment**: Database and ORM choices match backend framework and requirements
- **Performance**: Query response times meet SLA requirements with appropriate indexing
- **Data quality**: High data quality scores with minimal validation errors
- **Scalability**: Architecture supports expected data volume growth and concurrent access
- **Maintainability**: Schema changes and ETL processes are version-controlled and automated

---
*Effective data engineering provides the foundation for reliable business operations and data-driven decision making.*