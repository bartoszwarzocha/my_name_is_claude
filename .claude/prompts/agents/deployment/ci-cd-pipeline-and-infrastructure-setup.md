# CI/CD Pipeline and Infrastructure Setup

**Agent: deployment-engineer**
**Purpose: Design and implement automated deployment pipelines and scalable infrastructure**

---

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

---
*Robust deployment infrastructure enables teams to deliver software quickly, safely, and reliably while maintaining high availability and security standards.*