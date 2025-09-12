# CI/CD Pipeline and Infrastructure Setup

**Agent: deployment-engineer**
**Purpose: Design and implement automated deployment pipelines and scalable infrastructure**

---

## Context Analysis

The deployment-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Build and deployment pipeline selection (Maven/Gradle for Java, npm/yarn for Node.js, dotnet for .NET, pip/poetry for Python)
- **Infrastructure Preferences**: Cloud platform, containerization strategy, and orchestration platform
- **Project Scale**: Infrastructure complexity based on startup/SME/enterprise requirements
- **Business Domain**: Compliance requirements, availability needs, and security standards
- **Development Stage**: CI/CD maturity level from basic automation to advanced deployment patterns

Based on this analysis, the engineer will select appropriate deployment tools and infrastructure patterns.

## 🎯 Mission

Create robust, automated deployment infrastructure that enables safe, fast, and reliable software delivery from development to production.

## 📋 Infrastructure Design Process

### Step 1: Requirements Analysis
**From architecture and business specifications:**
- **Application architecture** and deployment patterns
- **Scalability requirements** and expected load
- **Availability requirements** (uptime SLA, disaster recovery)
- **Security requirements** and compliance needs
- **Budget constraints** and cost optimization goals

### Step 2: Infrastructure Architecture Design

**Environment Strategy:**
- **Development** - Individual developer environments
- **Testing** - Automated testing and QA validation
- **Staging** - Production-like environment for final validation
- **Production** - Live environment serving real users
- **Disaster Recovery** - Backup environment for business continuity

**Cloud Architecture Patterns:**
```yaml
# Example Kubernetes deployment architecture
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
    spec:
      containers:
      - name: api
        image: myapp/api:latest
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: database-credentials
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

## 🔧 CI/CD Pipeline Implementation

### Step 3: Continuous Integration Setup

**Source Code Management:**
- **Git workflow** with feature branches and pull requests
- **Code quality gates** (linting, static analysis, security scanning)
- **Automated testing** (unit, integration, end-to-end)
- **Build automation** with consistent, reproducible builds
- **Artifact management** and version control

**CI Pipeline Example (GitHub Actions):**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '18'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run linting
      run: npm run lint
      
    - name: Run unit tests
      run: npm test -- --coverage
      
    - name: Run integration tests
      run: npm run test:integration
      
    - name: Security audit
      run: npm audit --audit-level high
      
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Build Docker image
      run: docker build -t myapp/api:${{ github.sha }} .
      
    - name: Push to registry
      run: |
        docker tag myapp/api:${{ github.sha }} myapp/api:latest
        docker push myapp/api:${{ github.sha }}
        docker push myapp/api:latest
```

### Step 4: Continuous Deployment Strategy

**Deployment Patterns:**
- **Blue-Green Deployment** - Zero downtime with environment switching
- **Rolling Deployment** - Gradual instance replacement
- **Canary Deployment** - Gradual traffic shifting to new version
- **Feature Flags** - Runtime feature toggling and gradual rollouts

**Deployment Pipeline:**
```yaml
  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to staging
      run: |
        kubectl set image deployment/api-service \
          api=myapp/api:${{ github.sha }} \
          --namespace=staging
        kubectl rollout status deployment/api-service --namespace=staging
        
    - name: Run smoke tests
      run: npm run test:smoke -- --env=staging
      
    - name: Deploy to production
      run: |
        kubectl set image deployment/api-service \
          api=myapp/api:${{ github.sha }} \
          --namespace=production
        kubectl rollout status deployment/api-service --namespace=production
        
    - name: Verify deployment
      run: npm run test:health -- --env=production
```

## 🏗️ Infrastructure as Code

### Step 5: Infrastructure Automation

**Terraform Configuration Example:**
```hcl
# main.tf - Infrastructure definition
provider "aws" {
  region = var.aws_region
}

# EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = "${var.project_name}-cluster"
  role_arn = aws_iam_role.cluster.arn
  version  = "1.27"

  vpc_config {
    subnet_ids = aws_subnet.private[*].id
    endpoint_config {
      private_access = true
      public_access  = true
    }
  }

  depends_on = [
    aws_iam_role_policy_attachment.cluster_AmazonEKSClusterPolicy,
  ]
}

# RDS Database
resource "aws_rds_instance" "main" {
  identifier = "${var.project_name}-db"
  
  engine         = "postgres"
  engine_version = "15.4"
  instance_class = "db.t3.micro"
  
  allocated_storage     = 20
  max_allocated_storage = 100
  storage_encrypted     = true
  
  db_name  = var.database_name
  username = var.database_username
  password = random_password.db_password.result
  
  vpc_security_group_ids = [aws_security_group.database.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  skip_final_snapshot = false
  final_snapshot_identifier = "${var.project_name}-final-snapshot"
}
```

**Environment Management:**
```bash
# Environment-specific configurations
# environments/production/terraform.tfvars
aws_region = "us-west-2"
project_name = "myapp-prod"
instance_type = "t3.medium"
min_size = 2
max_size = 10
desired_capacity = 3

# environments/staging/terraform.tfvars  
aws_region = "us-west-2"
project_name = "myapp-staging"
instance_type = "t3.small"
min_size = 1
max_size = 3
desired_capacity = 1
```

## 📊 Monitoring and Observability

### Step 6: Monitoring Stack Setup

**Application Monitoring:**
- **Metrics collection** (Prometheus, CloudWatch, DataDog)
- **Log aggregation** (ELK Stack, Fluentd, CloudWatch Logs)
- **Distributed tracing** (Jaeger, Zipkin, AWS X-Ray)
- **Alerting** (PagerDuty, Slack, email notifications)
- **Dashboards** (Grafana, CloudWatch, DataDog)

**Infrastructure Monitoring:**
```yaml
# prometheus-config.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert-rules.yml"

scrape_configs:
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
    - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token

alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - alertmanager:9093
```

**Alert Rules:**
```yaml
# alert-rules.yml
groups:
- name: application-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: High error rate detected
      description: "Error rate is {{ $value }} errors per second"

  - alert: HighResponseTime
    expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: High response time detected
      description: "95th percentile response time is {{ $value }}s"
```

## 🔒 Security and Compliance

### Step 7: Security Implementation

**Infrastructure Security:**
- **Network security** (VPC, security groups, NACLs)
- **Identity and Access Management** (IAM roles, service accounts)
- **Encryption** (at rest and in transit)
- **Secret management** (AWS Secrets Manager, Kubernetes Secrets)
- **Vulnerability scanning** (container and infrastructure)

**Deployment Security:**
```yaml
# security-policies.yml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-network-policy
spec:
  podSelector:
    matchLabels:
      app: api-service
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

## 🚀 Scaling and Performance

### Step 8: Auto-scaling Configuration

**Horizontal Pod Autoscaler:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-service-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-service
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

**Cluster Autoscaling:**
```yaml
# cluster-autoscaler deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  template:
    spec:
      containers:
      - image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.27.0
        name: cluster-autoscaler
        command:
        - ./cluster-autoscaler
        - --v=4
        - --stderrthreshold=info
        - --cloud-provider=aws
        - --skip-nodes-with-local-storage=false
        - --expander=least-waste
        - --node-group-auto-discovery=asg:tag=k8s.io/cluster-autoscaler/enabled,k8s.io/cluster-autoscaler/myapp-cluster
```

## Technology-Adaptive Implementation

### Java + Maven/Gradle + Docker

**Recommended Pattern:** Jenkins or GitHub Actions with Docker Registry and Kubernetes

```yaml
# GitHub Actions for Java Spring Boot
name: Java CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  JAVA_VERSION: 17
  MAVEN_OPTS: -Dmaven.repo.local=.m2/repository
  DOCKER_REGISTRY: ghcr.io

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up JDK ${{ env.JAVA_VERSION }}
      uses: actions/setup-java@v4
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'
        cache: maven
    
    - name: Cache Maven dependencies
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        restore-keys: ${{ runner.os }}-m2
    
    - name: Run tests
      run: |
        mvn clean compile
        mvn test -Dspring.profiles.active=test
        mvn jacoco:report
    
    - name: Run integration tests
      run: mvn verify -Dspring.profiles.active=integration
    
    - name: SonarQube analysis
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      run: |
        mvn sonar:sonar \
          -Dsonar.projectKey=myapp \
          -Dsonar.host.url=${{ secrets.SONAR_HOST_URL }} \
          -Dsonar.login=${{ secrets.SONAR_TOKEN }}
    
    - name: Security scan with OWASP Dependency Check
      run: mvn org.owasp:dependency-check-maven:check

  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up JDK ${{ env.JAVA_VERSION }}
      uses: actions/setup-java@v4
      with:
        java-version: ${{ env.JAVA_VERSION }}
        distribution: 'temurin'
        cache: maven
    
    - name: Build application
      run: |
        mvn clean package -DskipTests -Dspring.profiles.active=production
        ls -la target/
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.DOCKER_REGISTRY }}/${{ github.repository }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Log in to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.DOCKER_REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        file: ./Dockerfile
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
        platforms: linux/amd64,linux/arm64

# Dockerfile for Java Spring Boot
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /workspace/app
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
RUN ./mvnw dependency:go-offline -B
COPY src src
RUN ./mvnw clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine
VOLUME /tmp
EXPOSE 8080
ARG JAR_FILE=/workspace/app/target/*.jar
COPY --from=build ${JAR_FILE} app.jar

# Add non-root user for security
RUN addgroup -g 1001 -S appuser && \
    adduser -S -u 1001 -G appuser appuser
USER appuser

ENTRYPOINT ["java","-jar","/app.jar"]

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to Kubernetes
      run: |
        echo "${{ secrets.KUBECONFIG }}" | base64 --decode > kubeconfig
        export KUBECONFIG=kubeconfig
        
        # Update deployment with new image
        kubectl set image deployment/myapp-deployment \
          myapp=${{ needs.build.outputs.image-tag }} \
          --namespace=production
        
        # Wait for rollout to complete
        kubectl rollout status deployment/myapp-deployment \
          --namespace=production --timeout=600s
        
        # Verify deployment
        kubectl get pods -l app=myapp --namespace=production
```

### .NET Core + NuGet + Docker

**Recommended Pattern:** Azure DevOps or GitHub Actions with Azure Container Registry

```yaml
# GitHub Actions for .NET Core
name: .NET CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  DOTNET_VERSION: '8.0.x'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: ${{ env.DOTNET_VERSION }}
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore --configuration Release
    
    - name: Run unit tests
      run: |
        dotnet test --no-build --configuration Release \
          --collect:"XPlat Code Coverage" \
          --results-directory ./coverage
    
    - name: Run integration tests
      run: |
        dotnet test tests/IntegrationTests \
          --configuration Release \
          --logger trx --results-directory ./test-results
    
    - name: Security scan
      run: |
        dotnet list package --vulnerable --include-transitive
        dotnet audit
    
    - name: SonarCloud analysis
      uses: SonarSource/sonarcloud-github-action@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: ${{ env.DOTNET_VERSION }}
    
    - name: Publish application
      run: |
        dotnet publish src/MyApp.API \
          --configuration Release \
          --output ./publish \
          --no-restore
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}

# Dockerfile for .NET Core
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS base
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
WORKDIR /src
COPY ["src/MyApp.API/MyApp.API.csproj", "src/MyApp.API/"]
COPY ["src/MyApp.Core/MyApp.Core.csproj", "src/MyApp.Core/"]
RUN dotnet restore "src/MyApp.API/MyApp.API.csproj"
COPY . .
WORKDIR "/src/src/MyApp.API"
RUN dotnet build "MyApp.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MyApp.API.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

# Add non-root user
RUN adduser --disabled-password --home /app --gecos '' appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["dotnet", "MyApp.API.dll"]

# Azure DevOps Pipeline Alternative
# azure-pipelines.yml
trigger:
- main
- develop

variables:
  buildConfiguration: 'Release'
  vmImageName: 'ubuntu-latest'
  containerRegistry: 'myacr.azurecr.io'
  imageRepository: 'myapp'
  dockerfilePath: '$(Build.SourcesDirectory)/Dockerfile'

stages:
- stage: Test
  displayName: Test stage
  jobs:
  - job: Test
    displayName: Test
    pool:
      vmImage: $(vmImageName)
    steps:
    - task: DotNetCoreCLI@2
      displayName: 'Restore packages'
      inputs:
        command: 'restore'
        projects: '**/*.csproj'
        
    - task: DotNetCoreCLI@2
      displayName: 'Build project'
      inputs:
        command: 'build'
        projects: '**/*.csproj'
        arguments: '--configuration $(buildConfiguration)'
        
    - task: DotNetCoreCLI@2
      displayName: 'Run tests'
      inputs:
        command: 'test'
        projects: '**/*Tests/*.csproj'
        arguments: '--configuration $(buildConfiguration) --collect "Code coverage"'

- stage: Build
  displayName: Build and push stage
  dependsOn: Test
  condition: succeeded()
  jobs:
  - job: Build
    displayName: Build
    pool:
      vmImage: $(vmImageName)
    steps:
    - task: Docker@2
      displayName: Build and push image
      inputs:
        containerRegistry: 'Azure Container Registry'
        repository: $(imageRepository)
        command: 'buildAndPush'
        Dockerfile: $(dockerfilePath)
        tags: |
          $(Build.BuildId)
          latest
```

### Node.js + npm/yarn + Docker

**Recommended Pattern:** GitHub Actions or GitLab CI with container orchestration

```yaml
# GitHub Actions for Node.js
name: Node.js CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:alpine
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js ${{ env.NODE_VERSION }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run linting
      run: |
        npm run lint
        npm run lint:types
    
    - name: Run unit tests
      run: npm run test:unit -- --coverage --watchAll=false
      env:
        NODE_ENV: test
    
    - name: Run integration tests
      run: npm run test:integration
      env:
        NODE_ENV: test
        DATABASE_URL: postgres://postgres:postgres@localhost:5432/testdb
        REDIS_URL: redis://localhost:6379
    
    - name: Run E2E tests
      run: |
        npm run build
        npm run test:e2e
      env:
        NODE_ENV: test
    
    - name: Security audit
      run: |
        npm audit --audit-level high
        npx better-npm-audit audit
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage/lcov.info

  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js ${{ env.NODE_VERSION }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci --production=false
    
    - name: Build application
      run: |
        npm run build
        npm prune --production
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ github.repository }}
        tags: |
          type=ref,event=branch
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

# Multi-stage Dockerfile for Node.js
FROM node:20-alpine AS base
WORKDIR /app
RUN apk add --no-cache dumb-init

# Dependencies stage
FROM base AS deps
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Build stage
FROM base AS build
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM base AS production
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package*.json ./

# Add non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001
USER nodejs

EXPOSE 3000
CMD ["dumb-init", "node", "dist/index.js"]

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
    - name: Deploy to staging
      run: |
        # Deploy to staging environment first
        kubectl set image deployment/myapp-deployment \
          myapp=${{ needs.build.outputs.image-tag }} \
          --namespace=staging
        kubectl rollout status deployment/myapp-deployment --namespace=staging
    
    - name: Run smoke tests
      run: |
        # Wait for deployment to be ready
        sleep 30
        npm run test:smoke -- --env=staging
    
    - name: Deploy to production
      run: |
        kubectl set image deployment/myapp-deployment \
          myapp=${{ needs.build.outputs.image-tag }} \
          --namespace=production
        kubectl rollout status deployment/myapp-deployment --namespace=production
    
    - name: Verify deployment
      run: npm run test:health -- --env=production
```

### Python + pip/poetry + Docker

**Recommended Pattern:** GitHub Actions with Poetry and pytest

```yaml
# GitHub Actions for Python
name: Python CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  PYTHON_VERSION: '3.11'
  POETRY_VERSION: '1.7.1'
  REGISTRY: ghcr.io

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:alpine
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ env.PYTHON_VERSION }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Install Poetry
      uses: snok/install-poetry@v1
      with:
        version: ${{ env.POETRY_VERSION }}
        virtualenvs-create: true
        virtualenvs-in-project: true
        installer-parallel: true
    
    - name: Load cached venv
      id: cached-poetry-dependencies
      uses: actions/cache@v3
      with:
        path: .venv
        key: venv-${{ runner.os }}-${{ env.PYTHON_VERSION }}-${{ hashFiles('**/poetry.lock') }}
    
    - name: Install dependencies
      if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
      run: poetry install --no-interaction --no-root
    
    - name: Install project
      run: poetry install --no-interaction
    
    - name: Run linting and formatting
      run: |
        poetry run black --check .
        poetry run isort --check-only .
        poetry run flake8 .
        poetry run mypy .
    
    - name: Run unit tests
      run: |
        poetry run pytest tests/unit \
          --cov=src \
          --cov-report=xml \
          --cov-report=html \
          --junitxml=junit.xml
      env:
        ENVIRONMENT: test
    
    - name: Run integration tests
      run: |
        poetry run pytest tests/integration \
          --cov=src --cov-append \
          --cov-report=xml
      env:
        ENVIRONMENT: test
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/testdb
        REDIS_URL: redis://localhost:6379/0
    
    - name: Security scan with bandit
      run: poetry run bandit -r src/
    
    - name: Dependency vulnerability check
      run: poetry run safety check
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
    - uses: actions/checkout@v4
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ github.repository }}
        tags: |
          type=ref,event=branch
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

# Multi-stage Dockerfile for Python
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.7.1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==$POETRY_VERSION

# Configure Poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Dependencies stage
FROM base AS deps
COPY pyproject.toml poetry.lock ./
RUN poetry install --only=main --no-interaction --no-ansi

# Build stage
FROM base AS build
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi
COPY . .
RUN poetry build

# Production stage
FROM python:3.11-slim AS production

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

# Install runtime dependencies only
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependencies and application
COPY --from=deps /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin
COPY --from=build /app/dist/*.whl /tmp/
RUN pip install /tmp/*.whl && rm -rf /tmp/*.whl

COPY src/ ./src/
COPY alembic.ini ./
COPY alembic/ ./alembic/

# Add non-root user
RUN adduser --system --group --no-create-home appuser
USER appuser

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic CI/CD patterns:

```yaml
# Generic CI/CD Configuration
ci_cd:
  stages:
    - "lint"        # Code quality checks
    - "test"        # Unit and integration tests
    - "security"    # Security scanning and vulnerability assessment
    - "build"       # Application compilation and packaging
    - "deploy"      # Deployment to environments
  
  quality_gates:
    - "code_coverage >= 80%"
    - "security_scan_passed"
    - "all_tests_passed"
    - "linting_passed"
  
  deployment_strategy:
    - "staging_first"     # Deploy to staging environment first
    - "smoke_tests"       # Run basic functionality tests
    - "production_deploy" # Deploy to production after validation
    - "health_check"      # Verify deployment health
  
  infrastructure:
    containerization: "Docker"
    orchestration: "Kubernetes or Docker Swarm"
    monitoring: "Prometheus + Grafana"
    logging: "ELK Stack or equivalent"
    
  security:
    - "HTTPS/TLS encryption"
    - "Secret management"
    - "Network policies"
    - "Regular security updates"
```

## 📤 Deliverables

- **Infrastructure Code** (Terraform, CloudFormation, or Kubernetes manifests)
- **CI/CD Pipeline Configuration** (GitHub Actions, GitLab CI, Jenkins)
- **Deployment Scripts** and automation tools
- **Monitoring Configuration** (Prometheus, Grafana, alerting rules)
- **Security Policies** and compliance configurations
- **Documentation** (runbooks, disaster recovery procedures, troubleshooting guides)
- **Cost Optimization** recommendations and resource right-sizing

## 🤝 Collaboration Points

**With software-architect:** Infrastructure requirements and architecture alignment
**With security-engineer:** Security controls and compliance implementation
**With api-engineer:** Application deployment requirements and health checks
**With data-engineer:** Database deployment and backup strategies
**With qa-engineer:** Testing environment setup and automation integration

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Build system** from primary_language field (Maven/Gradle for Java, npm/yarn for Node.js, dotnet for .NET, pip/poetry for Python)
- **Infrastructure preferences** for cloud platform and containerization strategy
- **Project scale** to select appropriate CI/CD complexity and infrastructure requirements
- **Business domain** for compliance, security, and availability requirements

### 2. Pipeline Configuration Selection

Select CI/CD tools based on detected technology and preferences:
- **Java**: Jenkins, GitHub Actions, or GitLab CI with Maven/Gradle
- **.NET**: Azure DevOps, GitHub Actions with dotnet CLI
- **Node.js**: GitHub Actions, GitLab CI with npm/yarn workflows
- **Python**: GitHub Actions, Jenkins with pip/poetry dependency management
- **Generic**: Standard pipeline with build, test, security, and deploy stages

### 3. Infrastructure Implementation

Apply technology-specific deployment patterns:
- **Containerization**: Docker images with multi-stage builds for optimization
- **Orchestration**: Kubernetes, Docker Swarm, or cloud-managed services
- **Security**: Secret management, network policies, and vulnerability scanning
- **Monitoring**: Health checks, metrics collection, and alerting
- **Scaling**: Auto-scaling based on load and resource utilization

### 4. Success Criteria

Deployment infrastructure validation checklist:
- **Technology alignment**: Build tools and deployment patterns match tech stack
- **Automation**: End-to-end automation from code commit to production
- **Security**: Comprehensive security scanning and policy enforcement
- **Observability**: Complete monitoring, logging, and alerting coverage
- **Reliability**: Zero-downtime deployments with quick rollback capabilities

---
*Robust deployment infrastructure enables teams to deliver software quickly, safely, and reliably while maintaining high availability and security standards.*