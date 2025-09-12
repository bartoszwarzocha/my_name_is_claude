# Test Automation and Quality Assurance

**Agent: qa-engineer**
**Purpose: Design comprehensive testing strategies and implement automated quality assurance processes**

---

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

---
*Comprehensive quality assurance ensures software reliability, user satisfaction, and business success through systematic testing and continuous improvement.*