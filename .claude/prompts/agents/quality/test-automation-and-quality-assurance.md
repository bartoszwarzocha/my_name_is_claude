# Test Automation and Quality Assurance

**Agent: qa-engineer**
**Purpose: Design comprehensive testing strategies and implement automated quality assurance processes**

---

## Context Analysis

The qa-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Testing framework selection (JUnit/TestNG for Java, NUnit/xUnit for .NET, Jest/Mocha for Node.js, pytest for Python)
- **Application Type**: Testing strategy based on web, mobile, desktop, or API-focused applications
- **Business Domain**: Domain-specific testing requirements, compliance needs, and quality standards
- **Project Scale**: Testing complexity and automation maturity based on team size and requirements
- **Technology Stack**: Integration testing patterns for databases, message queues, and external services

Based on this analysis, the engineer will select appropriate testing tools and implement technology-specific quality assurance processes.

## 🎯 Mission

Establish robust quality assurance processes that ensure software reliability, performance, and user satisfaction through comprehensive testing strategies and automated validation.

## 📋 Testing Strategy Framework

### Step 1: Quality Requirements Analysis
**From business and technical specifications:**
- **Functional requirements** and acceptance criteria
- **Non-functional requirements** (performance, security, usability)
- **User experience** expectations and quality standards
- **Compliance requirements** and regulatory standards
- **Risk assessment** and quality priorities

### Step 2: Test Pyramid Strategy

**Unit Testing (Foundation):**
- **Coverage target:** 80-90% code coverage
- **Scope:** Individual functions, methods, and components
- **Speed:** Fast execution (< 1 second per test)
- **Ownership:** Developers write and maintain
- **Tools:** Jest, pytest, JUnit, NUnit

**Integration Testing (Middle):**
- **Coverage target:** Critical integration points and data flows
- **Scope:** Component interactions and API contracts
- **Speed:** Moderate execution (< 30 seconds per test suite)
- **Ownership:** Shared between developers and QA
- **Tools:** Testcontainers, Postman, REST Assured

**End-to-End Testing (Top):**
- **Coverage target:** Critical user journeys and business workflows
- **Scope:** Complete application functionality from user perspective
- **Speed:** Slower execution (minutes per test)
- **Ownership:** QA engineers design and maintain
- **Tools:** Cypress, Selenium, Playwright, Puppeteer

### Step 3: Test Types and Coverage

**Functional Testing:**
```javascript
// Example user registration test
describe('User Registration Flow', () => {
  it('should successfully register a new user with valid data', async () => {
    // Arrange
    const userData = {
      email: 'test@example.com',
      password: 'SecurePassword123!',
      firstName: 'John',
      lastName: 'Doe'
    };
    
    // Act
    await registerPage.fillUserData(userData);
    await registerPage.submitForm();
    
    // Assert
    expect(await successPage.getWelcomeMessage()).toContain('Welcome, John!');
    expect(await apiClient.getUserByEmail(userData.email)).toBeTruthy();
  });
  
  it('should display validation errors for invalid email format', async () => {
    // Arrange
    const invalidData = { email: 'invalid-email', password: 'password123' };
    
    // Act
    await registerPage.fillUserData(invalidData);
    await registerPage.submitForm();
    
    // Assert
    expect(await registerPage.getEmailError()).toBe('Please enter a valid email address');
    expect(await registerPage.isSubmitButtonDisabled()).toBe(true);
  });
});
```

**Performance Testing:**
```javascript
// Load testing scenario
import { check, sleep } from 'k6';
import http from 'k6/http';

export let options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp up to 100 users
    { duration: '5m', target: 100 }, // Stay at 100 users
    { duration: '2m', target: 200 }, // Ramp up to 200 users
    { duration: '5m', target: 200 }, // Stay at 200 users
    { duration: '2m', target: 0 },   // Ramp down to 0 users
  ],
  thresholds: {
    http_req_duration: ['p(99)<1500'], // 99% of requests must complete below 1.5s
    http_req_failed: ['rate<0.1'],     // Error rate must be below 10%
  },
};

export default function () {
  // Test user login endpoint
  let response = http.post('https://api.example.com/auth/login', {
    email: 'testuser@example.com',
    password: 'password123',
  });
  
  check(response, {
    'login successful': (r) => r.status === 200,
    'response time OK': (r) => r.timings.duration < 1000,
    'auth token present': (r) => r.json('token') !== undefined,
  });
  
  sleep(1);
}
```

## 🔧 Test Automation Implementation

### Step 4: Automated Testing Framework

**Test Framework Architecture:**
```python
# pytest-based testing framework
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFramework:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.config = self.load_config()
    
    def setup_method(self):
        """Setup before each test method"""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def teardown_method(self):
        """Cleanup after each test method"""
        if self.driver:
            self.driver.quit()
    
    def login_user(self, email, password):
        """Reusable login helper method"""
        self.driver.get(f"{self.config.base_url}/login")
        
        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        
        email_field.send_keys(email)
        password_field.send_keys(password)
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("/dashboard"))
```

**Page Object Model:**
```python
# page_objects/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password") 
    LOGIN_BUTTON = (By.ID, "login-submit")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def enter_email(self, email):
        element = self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))
        element.clear()
        element.send_keys(email)
        
    def enter_password(self, password):
        element = self.driver.find_element(*self.PASSWORD_FIELD)
        element.clear()
        element.send_keys(password)
        
    def click_login(self):
        element = self.driver.find_element(*self.LOGIN_BUTTON)
        element.click()
        
    def get_error_message(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            return element.text
        except TimeoutException:
            return None
```

### Step 5: API Testing Framework

**REST API Testing:**
```python
import requests
import pytest

class APITestFramework:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_token = None
    
    def authenticate(self, email, password):
        """Authenticate and store token for subsequent requests"""
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json={"email": email, "password": password}
        )
        assert response.status_code == 200
        self.auth_token = response.json()["token"]
        self.session.headers.update({"Authorization": f"Bearer {self.auth_token}"})
        
    def create_user(self, user_data):
        """Create a new user and return response"""
        response = self.session.post(
            f"{self.base_url}/users",
            json=user_data
        )
        return response
    
    def get_user(self, user_id):
        """Retrieve user by ID"""
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        return response
    
    def validate_user_schema(self, user_data):
        """Validate user data against expected schema"""
        required_fields = ["id", "email", "firstName", "lastName", "createdAt"]
        
        for field in required_fields:
            assert field in user_data, f"Missing required field: {field}"
        
        assert isinstance(user_data["id"], (int, str))
        assert "@" in user_data["email"]
        assert len(user_data["firstName"]) > 0
        assert len(user_data["lastName"]) > 0

# Test implementation
class TestUserAPI:
    def test_create_user_success(self, api_client):
        # Arrange
        user_data = {
            "email": "newuser@example.com",
            "password": "SecurePassword123!",
            "firstName": "Jane",
            "lastName": "Smith"
        }
        
        # Act
        response = api_client.create_user(user_data)
        
        # Assert
        assert response.status_code == 201
        response_data = response.json()
        api_client.validate_user_schema(response_data)
        assert response_data["email"] == user_data["email"]
```

## 📊 Quality Metrics and Monitoring

### Step 6: Test Metrics and Reporting

**Test Coverage Metrics:**
```yaml
# Coverage reporting configuration
coverage:
  targets:
    unit_tests: 85%
    integration_tests: 70%
    e2e_tests: "critical_paths"
    
  exclusions:
    - "*/tests/*"
    - "*/mocks/*" 
    - "*/vendor/*"
    
  reports:
    - format: "html"
      output: "coverage/html"
    - format: "cobertura"
      output: "coverage/cobertura.xml"
    - format: "lcov"
      output: "coverage/lcov.info"
```

**Quality Dashboards:**
```python
# Test metrics collection
class TestMetrics:
    def collect_execution_metrics(self, test_results):
        return {
            'total_tests': len(test_results),
            'passed_tests': len([t for t in test_results if t.status == 'passed']),
            'failed_tests': len([t for t in test_results if t.status == 'failed']),
            'skipped_tests': len([t for t in test_results if t.status == 'skipped']),
            'execution_time': sum(t.duration for t in test_results),
            'pass_rate': self.calculate_pass_rate(test_results),
            'flaky_tests': self.identify_flaky_tests(test_results)
        }
    
    def generate_trend_analysis(self, historical_data):
        """Analyze test metrics trends over time"""
        return {
            'pass_rate_trend': self.calculate_trend(historical_data, 'pass_rate'),
            'execution_time_trend': self.calculate_trend(historical_data, 'execution_time'),
            'coverage_trend': self.calculate_trend(historical_data, 'coverage'),
            'defect_density_trend': self.calculate_trend(historical_data, 'defect_density')
        }
```

### Step 7: Continuous Quality Integration

**CI/CD Integration:**
```yaml
# GitHub Actions workflow for quality gates
name: Quality Gate

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Test Environment
      run: |
        npm ci
        docker-compose up -d
        
    - name: Run Unit Tests
      run: |
        npm run test:unit -- --coverage
        
    - name: Run Integration Tests  
      run: |
        npm run test:integration
        
    - name: Run E2E Tests
      run: |
        npm run test:e2e -- --headless
        
    - name: Run Security Tests
      run: |
        npm run test:security
        
    - name: Run Performance Tests
      run: |
        npm run test:performance
        
    - name: Generate Quality Report
      run: |
        npm run quality:report
        
    - name: Quality Gate Check
      run: |
        if [ "${{ steps.coverage.outputs.percentage }}" -lt "85" ]; then
          echo "Coverage below threshold: ${{ steps.coverage.outputs.percentage }}%"
          exit 1
        fi
```

**Quality Gates:**
- **Code Coverage** must be ≥ 85% for unit tests
- **Performance Tests** must pass with response time < 2s
- **Security Tests** must pass with no high/critical vulnerabilities
- **E2E Tests** must pass with 100% success rate on critical paths
- **Static Analysis** must pass with no blocker/critical issues

## 🚀 Test Environment Management

### Step 8: Test Data and Environment Setup

**Test Data Management:**
```python
# Test data factory
class TestDataFactory:
    @staticmethod
    def create_user(overrides=None):
        """Create test user with default or override values"""
        default_user = {
            "email": f"testuser_{uuid.uuid4()}@example.com",
            "password": "TestPassword123!",
            "firstName": "Test",
            "lastName": "User",
            "role": "user",
            "isActive": True
        }
        
        if overrides:
            default_user.update(overrides)
            
        return default_user
    
    @staticmethod
    def create_admin_user():
        """Create admin user for privileged operations"""
        return TestDataFactory.create_user({
            "email": "admin@example.com",
            "role": "admin",
            "permissions": ["read", "write", "delete", "admin"]
        })
    
    def cleanup_test_data(self, test_context):
        """Clean up test data after test execution"""
        for resource in test_context.created_resources:
            self.delete_resource(resource)
```

**Environment Configuration:**
```yaml
# test-environments.yml
environments:
  unit:
    database: "sqlite:///:memory:"
    cache: "memory"
    external_services: "mocked"
    
  integration:
    database: "postgresql://testdb:5432/integration_tests"
    cache: "redis://redis:6379/1"
    external_services: "stubbed"
    
  e2e:
    database: "postgresql://testdb:5432/e2e_tests"
    cache: "redis://redis:6379/2"
    external_services: "sandbox"
    
  performance:
    database: "postgresql://testdb:5432/perf_tests"
    cache: "redis://redis:6379/3"
    external_services: "production_like"
    load_balancer: "enabled"
    monitoring: "enabled"
```

## Technology-Adaptive Implementation

### Java + JUnit/TestNG + Maven/Gradle

**Recommended Pattern:** JUnit 5 with Testcontainers and AssertJ

```java
// Unit Testing with JUnit 5 and AssertJ
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private EmailService emailService;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    @DisplayName("Should create user successfully with valid data")
    void shouldCreateUserSuccessfully() {
        // Given
        CreateUserRequest request = CreateUserRequest.builder()
            .email("test@example.com")
            .firstName("John")
            .lastName("Doe")
            .build();
            
        User expectedUser = User.builder()
            .id(1L)
            .email(request.getEmail())
            .firstName(request.getFirstName())
            .lastName(request.getLastName())
            .status(UserStatus.ACTIVE)
            .build();
            
        when(userRepository.findByEmail(request.getEmail()))
            .thenReturn(Optional.empty());
        when(userRepository.save(any(User.class)))
            .thenReturn(expectedUser);
            
        // When
        UserDto result = userService.createUser(request);
        
        // Then
        assertThat(result)
            .isNotNull()
            .satisfies(user -> {
                assertThat(user.getId()).isEqualTo(1L);
                assertThat(user.getEmail()).isEqualTo("test@example.com");
                assertThat(user.getFullName()).isEqualTo("John Doe");
                assertThat(user.getStatus()).isEqualTo(UserStatus.ACTIVE);
            });
            
        verify(userRepository).findByEmail(request.getEmail());
        verify(userRepository).save(any(User.class));
        verify(emailService).sendWelcomeEmail(expectedUser);
    }
    
    @Test
    @DisplayName("Should throw exception when user already exists")
    void shouldThrowExceptionWhenUserExists() {
        // Given
        CreateUserRequest request = CreateUserRequest.builder()
            .email("existing@example.com")
            .firstName("Jane")
            .lastName("Smith")
            .build();
            
        when(userRepository.findByEmail(request.getEmail()))
            .thenReturn(Optional.of(User.builder().build()));
            
        // When & Then
        assertThatThrownBy(() -> userService.createUser(request))
            .isInstanceOf(UserAlreadyExistsException.class)
            .hasMessage("User with email existing@example.com already exists");
            
        verify(userRepository).findByEmail(request.getEmail());
        verifyNoMoreInteractions(userRepository, emailService);
    }
}

// Integration Testing with Testcontainers
@SpringBootTest
@Testcontainers
class UserIntegrationTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
        .withDatabaseName("testdb")
        .withUsername("test")
        .withPassword("test");
    
    @Container
    static GenericContainer<?> redis = new GenericContainer<>("redis:alpine")
        .withExposedPorts(6379);
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Autowired
    private UserRepository userRepository;
    
    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
        registry.add("spring.redis.host", redis::getHost);
        registry.add("spring.redis.port", redis::getFirstMappedPort);
    }
    
    @Test
    @Sql("/test-data/users.sql")
    void shouldCreateUserAndReturnCreatedResponse() {
        // Given
        CreateUserRequest request = CreateUserRequest.builder()
            .email("newuser@example.com")
            .firstName("Integration")
            .lastName("Test")
            .build();
            
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<CreateUserRequest> entity = new HttpEntity<>(request, headers);
        
        // When
        ResponseEntity<UserDto> response = restTemplate.postForEntity(
            "/api/users", 
            entity, 
            UserDto.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody())
            .isNotNull()
            .satisfies(user -> {
                assertThat(user.getEmail()).isEqualTo(request.getEmail());
                assertThat(user.getFirstName()).isEqualTo(request.getFirstName());
                assertThat(user.getLastName()).isEqualTo(request.getLastName());
            });
            
        // Verify database persistence
        Optional<User> savedUser = userRepository.findByEmail(request.getEmail());
        assertThat(savedUser).isPresent();
    }
}

// Performance Testing with JMH
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
public class UserServicePerformanceTest {
    
    private UserService userService;
    private CreateUserRequest testRequest;
    
    @Setup
    public void setup() {
        // Initialize service with mocked dependencies
        userService = new UserService(
            mock(UserRepository.class),
            mock(EmailService.class)
        );
        
        testRequest = CreateUserRequest.builder()
            .email("perf@example.com")
            .firstName("Performance")
            .lastName("Test")
            .build();
    }
    
    @Benchmark
    @Warmup(iterations = 5)
    @Measurement(iterations = 10)
    public UserDto benchmarkUserCreation() {
        return userService.createUser(testRequest);
    }
}

// pom.xml configuration for testing
/*
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.assertj</groupId>
        <artifactId>assertj-core</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>junit-jupiter</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>postgresql</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-core</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
*/
```

### .NET Core + xUnit/NUnit + Entity Framework

**Recommended Pattern:** xUnit with FluentAssertions and TestContainers

```csharp
// Unit Testing with xUnit and FluentAssertions
public class UserServiceTests
{
    private readonly Mock<IUserRepository> _userRepositoryMock;
    private readonly Mock<IEmailService> _emailServiceMock;
    private readonly UserService _userService;
    
    public UserServiceTests()
    {
        _userRepositoryMock = new Mock<IUserRepository>();
        _emailServiceMock = new Mock<IEmailService>();
        _userService = new UserService(_userRepositoryMock.Object, _emailServiceMock.Object);
    }
    
    [Fact]
    [Trait("Category", "Unit")]
    public async Task CreateUserAsync_WithValidData_ShouldReturnUserDto()
    {
        // Arrange
        var request = new CreateUserRequest
        {
            Email = "test@example.com",
            FirstName = "John",
            LastName = "Doe"
        };
        
        var user = new User
        {
            Id = 1,
            Email = request.Email,
            FirstName = request.FirstName,
            LastName = request.LastName,
            Status = UserStatus.Active,
            CreatedAt = DateTime.UtcNow
        };
        
        _userRepositoryMock
            .Setup(x => x.GetByEmailAsync(request.Email))
            .ReturnsAsync((User)null);
            
        _userRepositoryMock
            .Setup(x => x.AddAsync(It.IsAny<User>()))
            .ReturnsAsync(user);
        
        // Act
        var result = await _userService.CreateUserAsync(request);
        
        // Assert
        result.Should().NotBeNull();
        result.Id.Should().Be(1);
        result.Email.Should().Be(request.Email);
        result.FullName.Should().Be("John Doe");
        result.Status.Should().Be(UserStatus.Active);
        
        _userRepositoryMock.Verify(x => x.GetByEmailAsync(request.Email), Times.Once);
        _userRepositoryMock.Verify(x => x.AddAsync(It.IsAny<User>()), Times.Once);
        _emailServiceMock.Verify(x => x.SendWelcomeEmailAsync(user), Times.Once);
    }
    
    [Theory]
    [InlineData("")]
    [InlineData("invalid-email")]
    [InlineData("@example.com")]
    [Trait("Category", "Unit")]
    public async Task CreateUserAsync_WithInvalidEmail_ShouldThrowValidationException(string email)
    {
        // Arrange
        var request = new CreateUserRequest
        {
            Email = email,
            FirstName = "John",
            LastName = "Doe"
        };
        
        // Act & Assert
        await _userService
            .Invoking(service => service.CreateUserAsync(request))
            .Should()
            .ThrowAsync<ValidationException>()
            .WithMessage("*email*");
    }
}

// Integration Testing with WebApplicationFactory
public class UserControllerIntegrationTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly WebApplicationFactory<Program> _factory;
    private readonly HttpClient _client;
    
    public UserControllerIntegrationTests(WebApplicationFactory<Program> factory)
    {
        _factory = factory;
        _client = factory.WithWebHostBuilder(builder =>
        {
            builder.ConfigureTestServices(services =>
            {
                // Replace with in-memory database
                services.RemoveAll<DbContextOptions<ApplicationDbContext>>();
                services.AddDbContext<ApplicationDbContext>(options =>
                {
                    options.UseInMemoryDatabase("TestDb");
                });
            });
        }).CreateClient();
    }
    
    [Fact]
    [Trait("Category", "Integration")]
    public async Task POST_Users_WithValidData_ShouldReturnCreated()
    {
        // Arrange
        var request = new CreateUserRequest
        {
            Email = "integration@example.com",
            FirstName = "Integration",
            LastName = "Test"
        };
        
        var json = JsonSerializer.Serialize(request);
        var content = new StringContent(json, Encoding.UTF8, "application/json");
        
        // Act
        var response = await _client.PostAsync("/api/users", content);
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.Created);
        
        var responseContent = await response.Content.ReadAsStringAsync();
        var user = JsonSerializer.Deserialize<UserDto>(responseContent, new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase
        });
        
        user.Should().NotBeNull();
        user.Email.Should().Be(request.Email);
        user.FirstName.Should().Be(request.FirstName);
        user.LastName.Should().Be(request.LastName);
    }
}

// Load Testing with NBomber
public class UserApiLoadTest
{
    [Fact]
    public void LoadTest_CreateUser_ShouldHandleConcurrentRequests()
    {
        var scenario = Scenario.Create("create_user", async context =>
        {
            var request = new CreateUserRequest
            {
                Email = $"loadtest{context.ScenarioInfo.ThreadId}@example.com",
                FirstName = "Load",
                LastName = "Test"
            };
            
            using var httpClient = new HttpClient();
            var json = JsonSerializer.Serialize(request);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            
            var response = await httpClient.PostAsync("https://localhost:5001/api/users", content);
            
            return response.IsSuccessStatusCode ? Response.Ok() : Response.Fail();
        })
        .WithLoadSimulations(
            Simulation.InjectPerSec(rate: 10, during: TimeSpan.FromMinutes(2))
        );
        
        var stats = NBomberRunner
            .RegisterScenarios(scenario)
            .Run();
            
        // Assert performance requirements
        var sceneStats = stats.AllScenarioStats.First();
        sceneStats.Ok.Request.Mean.Should().BeLessOrEqualTo(TimeSpan.FromSeconds(2));
        sceneStats.Fail.Request.Count.Should().BeLessOrEqualTo(sceneStats.AllRequestCount * 0.01); // < 1% error rate
    }
}
```

### Node.js + Jest/Mocha + Supertest

**Recommended Pattern:** Jest with Supertest and Testing Library

```javascript
// Unit Testing with Jest
const UserService = require('../src/services/UserService');
const UserRepository = require('../src/repositories/UserRepository');
const EmailService = require('../src/services/EmailService');

// Mock dependencies
jest.mock('../src/repositories/UserRepository');
jest.mock('../src/services/EmailService');

describe('UserService', () => {
  let userService;
  let mockUserRepository;
  let mockEmailService;
  
  beforeEach(() => {
    jest.clearAllMocks();
    mockUserRepository = new UserRepository();
    mockEmailService = new EmailService();
    userService = new UserService(mockUserRepository, mockEmailService);
  });
  
  describe('createUser', () => {
    it('should create user successfully with valid data', async () => {
      // Arrange
      const userData = {
        email: 'test@example.com',
        firstName: 'John',
        lastName: 'Doe'
      };
      
      const expectedUser = {
        id: 1,
        email: userData.email,
        firstName: userData.firstName,
        lastName: userData.lastName,
        status: 'active',
        createdAt: new Date().toISOString()
      };
      
      mockUserRepository.findByEmail.mockResolvedValue(null);
      mockUserRepository.create.mockResolvedValue(expectedUser);
      mockEmailService.sendWelcomeEmail.mockResolvedValue(true);
      
      // Act
      const result = await userService.createUser(userData);
      
      // Assert
      expect(result).toEqual({
        id: 1,
        email: userData.email,
        fullName: 'John Doe',
        status: 'active'
      });
      
      expect(mockUserRepository.findByEmail).toHaveBeenCalledWith(userData.email);
      expect(mockUserRepository.create).toHaveBeenCalledWith(expect.objectContaining(userData));
      expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(expectedUser);
    });
    
    it('should throw error when user already exists', async () => {
      // Arrange
      const userData = {
        email: 'existing@example.com',
        firstName: 'Jane',
        lastName: 'Smith'
      };
      
      mockUserRepository.findByEmail.mockResolvedValue({ id: 1 });
      
      // Act & Assert
      await expect(userService.createUser(userData))
        .rejects
        .toThrow('User with email existing@example.com already exists');
        
      expect(mockUserRepository.findByEmail).toHaveBeenCalledWith(userData.email);
      expect(mockUserRepository.create).not.toHaveBeenCalled();
      expect(mockEmailService.sendWelcomeEmail).not.toHaveBeenCalled();
    });
  });
});

// Integration Testing with Supertest
const request = require('supertest');
const app = require('../src/app');
const { setupTestDb, cleanupTestDb } = require('./helpers/database');

describe('Users API Integration', () => {
  beforeAll(async () => {
    await setupTestDb();
  });
  
  afterAll(async () => {
    await cleanupTestDb();
  });
  
  beforeEach(async () => {
    // Clear test data before each test
    await request(app).delete('/api/test/cleanup');
  });
  
  describe('POST /api/users', () => {
    it('should create user and return 201', async () => {
      // Arrange
      const userData = {
        email: 'integration@example.com',
        firstName: 'Integration',
        lastName: 'Test'
      };
      
      // Act & Assert
      const response = await request(app)
        .post('/api/users')
        .send(userData)
        .expect(201)
        .expect('Content-Type', /json/);
        
      expect(response.body).toMatchObject({
        email: userData.email,
        firstName: userData.firstName,
        lastName: userData.lastName,
        status: 'active'
      });
      expect(response.body.id).toBeDefined();
      expect(response.body.createdAt).toBeDefined();
    });
    
    it('should return 400 for invalid email format', async () => {
      // Arrange
      const invalidData = {
        email: 'invalid-email',
        firstName: 'Test',
        lastName: 'User'
      };
      
      // Act & Assert
      const response = await request(app)
        .post('/api/users')
        .send(invalidData)
        .expect(400);
        
      expect(response.body).toMatchObject({
        error: 'Validation Error',
        details: expect.arrayContaining([
          expect.objectContaining({
            field: 'email',
            message: expect.stringContaining('valid email')
          })
        ])
      });
    });
  });
});

// E2E Testing with Playwright
const { test, expect } = require('@playwright/test');

test.describe('User Registration Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });
  
  test('should register new user successfully', async ({ page }) => {
    // Navigate to registration page
    await page.click('[data-testid="register-link"]');
    
    // Fill registration form
    await page.fill('[data-testid="email-input"]', 'e2e@example.com');
    await page.fill('[data-testid="firstname-input"]', 'E2E');
    await page.fill('[data-testid="lastname-input"]', 'Test');
    await page.fill('[data-testid="password-input"]', 'SecurePassword123!');
    await page.fill('[data-testid="confirm-password-input"]', 'SecurePassword123!');
    
    // Submit form
    await page.click('[data-testid="register-button"]');
    
    // Verify success
    await expect(page.locator('[data-testid="success-message"]'))
      .toContainText('Welcome, E2E!');
      
    await expect(page).toHaveURL(/.*\/dashboard/);
  });
  
  test('should show validation errors for invalid data', async ({ page }) => {
    await page.click('[data-testid="register-link"]');
    
    // Fill with invalid email
    await page.fill('[data-testid="email-input"]', 'invalid-email');
    await page.fill('[data-testid="firstname-input"]', '');
    
    // Try to submit
    await page.click('[data-testid="register-button"]');
    
    // Verify validation errors
    await expect(page.locator('[data-testid="email-error"]'))
      .toContainText('Please enter a valid email address');
      
    await expect(page.locator('[data-testid="firstname-error"]'))
      .toContainText('First name is required');
  });
});

// Performance Testing with Artillery
// artillery-config.yml
/*
config:
  target: 'http://localhost:3000'
  phases:
    - duration: 60
      arrivalRate: 10
    - duration: 120
      arrivalRate: 50
  processor: "./test-functions.js"
  
scenarios:
  - name: "Create User Load Test"
    weight: 100
    flow:
      - post:
          url: "/api/users"
          beforeRequest: "setUniqueUserData"
          json:
            email: "{{ email }}"
            firstName: "Load"
            lastName: "Test"
          expect:
            - statusCode: 201
            - hasHeader: "content-type"
*/
```

### Python + pytest + FastAPI

**Recommended Pattern:** pytest with pytest-asyncio and httpx

```python
# Unit Testing with pytest and pytest-mock
import pytest
from unittest.mock import AsyncMock, Mock
from src.services.user_service import UserService
from src.models.user import User, UserStatus
from src.schemas.user import CreateUserRequest, UserDto
from src.exceptions import UserAlreadyExistsException

@pytest.fixture
def mock_user_repository():
    return AsyncMock()

@pytest.fixture
def mock_email_service():
    return AsyncMock()

@pytest.fixture
def user_service(mock_user_repository, mock_email_service):
    return UserService(
        repository=mock_user_repository,
        email_service=mock_email_service
    )

class TestUserService:
    @pytest.mark.asyncio
    async def test_create_user_success(self, user_service, mock_user_repository, mock_email_service):
        # Arrange
        request = CreateUserRequest(
            email="test@example.com",
            first_name="John",
            last_name="Doe"
        )
        
        expected_user = User(
            id=1,
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            status=UserStatus.ACTIVE
        )
        
        mock_user_repository.get_by_email.return_value = None
        mock_user_repository.create.return_value = expected_user
        mock_email_service.send_welcome_email.return_value = True
        
        # Act
        result = await user_service.create_user(request)
        
        # Assert
        assert isinstance(result, UserDto)
        assert result.email == request.email
        assert result.first_name == request.first_name
        assert result.last_name == request.last_name
        assert result.full_name == "John Doe"
        assert result.status == UserStatus.ACTIVE
        
        mock_user_repository.get_by_email.assert_called_once_with(request.email)
        mock_user_repository.create.assert_called_once()
        mock_email_service.send_welcome_email.assert_called_once_with(expected_user)
    
    @pytest.mark.asyncio
    async def test_create_user_already_exists(self, user_service, mock_user_repository, mock_email_service):
        # Arrange
        request = CreateUserRequest(
            email="existing@example.com",
            first_name="Jane",
            last_name="Smith"
        )
        
        existing_user = User(id=1, email=request.email)
        mock_user_repository.get_by_email.return_value = existing_user
        
        # Act & Assert
        with pytest.raises(UserAlreadyExistsException) as exc_info:
            await user_service.create_user(request)
            
        assert "existing@example.com" in str(exc_info.value)
        mock_user_repository.get_by_email.assert_called_once_with(request.email)
        mock_user_repository.create.assert_not_called()
        mock_email_service.send_welcome_email.assert_not_called()
    
    @pytest.mark.parametrize("email,expected_error", [
        ("", "Email cannot be empty"),
        ("invalid-email", "Invalid email format"),
        ("@example.com", "Invalid email format"),
    ])
    @pytest.mark.asyncio
    async def test_create_user_invalid_email(self, user_service, email, expected_error):
        # Arrange
        request = CreateUserRequest(
            email=email,
            first_name="Test",
            last_name="User"
        )
        
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            await user_service.create_user(request)
            
        assert expected_error in str(exc_info.value)

# Integration Testing with FastAPI TestClient
import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import redis.asyncio as redis

from src.main import app
from src.database import get_db
from src.config import settings

# Test database setup
test_engine = create_async_engine(
    "postgresql+asyncpg://test:test@localhost:5432/testdb",
    echo=True
)
TestAsyncSession = sessionmaker(
    test_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

@pytest.fixture
async def db_session():
    async with TestAsyncSession() as session:
        yield session
        await session.rollback()

@pytest.fixture
async def client(db_session):
    def override_get_db():
        return db_session
        
    app.dependency_overrides[get_db] = override_get_db
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
        
    app.dependency_overrides.clear()

class TestUserAPI:
    @pytest.mark.asyncio
    async def test_create_user_success(self, client: AsyncClient):
        # Arrange
        user_data = {
            "email": "integration@example.com",
            "first_name": "Integration",
            "last_name": "Test"
        }
        
        # Act
        response = await client.post("/api/users", json=user_data)
        
        # Assert
        assert response.status_code == 201
        
        response_data = response.json()
        assert response_data["email"] == user_data["email"]
        assert response_data["first_name"] == user_data["first_name"]
        assert response_data["last_name"] == user_data["last_name"]
        assert response_data["status"] == "active"
        assert "id" in response_data
        assert "created_at" in response_data
    
    @pytest.mark.asyncio
    async def test_create_user_invalid_email(self, client: AsyncClient):
        # Arrange
        user_data = {
            "email": "invalid-email",
            "first_name": "Test",
            "last_name": "User"
        }
        
        # Act
        response = await client.post("/api/users", json=user_data)
        
        # Assert
        assert response.status_code == 422
        
        error_detail = response.json()["detail"]
        assert any(error["field"] == "email" for error in error_detail)

# Load Testing with Locust
from locust import HttpUser, task, between
import random
import string

class UserAPILoadTest(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Called when a user starts"""
        self.user_counter = 0
    
    @task(3)
    def create_user(self):
        """Create user - most common operation"""
        user_data = {
            "email": f"loadtest{self.user_counter}@example.com",
            "first_name": "Load",
            "last_name": "Test"
        }
        
        with self.client.post(
            "/api/users", 
            json=user_data, 
            catch_response=True
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f"Status code: {response.status_code}")
        
        self.user_counter += 1
    
    @task(1)
    def get_user(self):
        """Get user by ID - less frequent operation"""
        user_id = random.randint(1, 1000)
        
        with self.client.get(
            f"/api/users/{user_id}", 
            catch_response=True
        ) as response:
            if response.status_code in [200, 404]:
                response.success()
            else:
                response.failure(f"Status code: {response.status_code}")

# Performance Testing with pytest-benchmark
@pytest.mark.benchmark
class TestUserServicePerformance:
    def test_create_user_performance(self, benchmark, user_service, mock_user_repository, mock_email_service):
        # Arrange
        request = CreateUserRequest(
            email="perf@example.com",
            first_name="Performance",
            last_name="Test"
        )
        
        mock_user_repository.get_by_email.return_value = None
        mock_user_repository.create.return_value = User(id=1, email=request.email)
        mock_email_service.send_welcome_email.return_value = True
        
        # Act & Assert
        result = benchmark(asyncio.run, user_service.create_user(request))
        assert result.email == request.email
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic testing patterns:

```yaml
# Generic Testing Configuration
testing_strategy:
  test_pyramid:
    unit_tests:
      coverage_target: "85%"
      tools: "Language-specific unit testing framework"
      scope: "Individual functions and methods"
      
    integration_tests:
      coverage_target: "Critical integration points"
      tools: "API testing tools and database integration"
      scope: "Component interactions and data flow"
      
    e2e_tests:
      coverage_target: "Critical user journeys"
      tools: "Browser automation or API testing tools"
      scope: "Complete workflows from user perspective"
  
  quality_gates:
    - "unit_test_coverage >= 85%"
    - "integration_tests_pass"
    - "e2e_critical_paths_pass"
    - "performance_requirements_met"
    - "security_tests_pass"
    
  test_environments:
    - "unit: Mocked dependencies and in-memory resources"
    - "integration: Real database and external service stubs"
    - "e2e: Production-like environment with test data"
    - "performance: Scaled environment for load testing"
    
  automation:
    - "CI/CD integration with quality gates"
    - "Automated test execution on code changes"
    - "Test result reporting and trend analysis"
    - "Failed test alerting and notification"
```

## 📤 Deliverables

- **Test Strategy Document** with comprehensive testing approach
- **Automated Test Suites** (unit, integration, E2E, performance)
- **Test Framework** with reusable components and utilities
- **Quality Dashboards** with metrics and trend analysis
- **CI/CD Integration** with quality gates and automated reporting
- **Test Environment Setup** with data management and cleanup
- **Documentation** (test procedures, framework guides, troubleshooting)

## 🤝 Collaboration Points

**With frontend-engineer:** UI/UX testing strategies and component testing
**With api-engineer:** API contract testing and integration validation
**With security-engineer:** Security testing integration and vulnerability assessment
**With deployment-engineer:** Test environment automation and CI/CD integration
**With business-analyst:** Acceptance criteria validation and user story testing

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Testing framework** from primary_language field (JUnit/TestNG for Java, xUnit/NUnit for .NET, Jest/Mocha for Node.js, pytest for Python)
- **Application architecture** for testing strategy selection (monolithic vs microservices, web vs desktop)
- **Business domain** for compliance testing requirements and quality standards
- **Project scale** to determine testing automation maturity and coverage requirements

### 2. Test Framework Selection

Select testing tools based on detected technology:
- **Java**: JUnit 5, Testcontainers, AssertJ, Mockito for comprehensive testing
- **.NET**: xUnit, FluentAssertions, Moq, WebApplicationFactory for integration testing
- **Node.js**: Jest, Supertest, Playwright for full-stack testing coverage
- **Python**: pytest, pytest-asyncio, httpx for async testing and FastAPI integration
- **Generic**: Language-appropriate unit testing with API and E2E testing tools

### 3. Testing Implementation Approach

Apply technology-specific testing patterns:
- **Test pyramid**: Unit tests (85% coverage), integration tests (critical paths), E2E tests (user journeys)
- **Quality gates**: Coverage thresholds, performance requirements, security validation
- **Test environments**: Isolated test data, containerized dependencies, production-like staging
- **CI/CD integration**: Automated test execution, quality reporting, deployment gates

### 4. Success Criteria

Quality assurance validation checklist:
- **Technology alignment**: Testing frameworks match technology stack and best practices
- **Coverage targets**: Unit test coverage ≥85%, critical path integration testing
- **Performance validation**: Load testing meets SLA requirements with <1% error rate
- **Quality gates**: All automated tests pass before deployment to production
- **Maintainability**: Test code is maintainable, reliable, and provides fast feedback

---
*Comprehensive quality assurance ensures software reliability, user satisfaction, and business success through systematic testing and continuous improvement.*