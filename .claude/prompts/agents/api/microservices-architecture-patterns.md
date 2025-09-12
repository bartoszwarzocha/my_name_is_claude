# Microservices Architecture Patterns

**Agent: api-engineer**
**Purpose: Design and implement scalable microservices architecture with proven patterns and best practices**

---

## 🎯 Mission

Architect robust microservices systems that provide scalability, maintainability, and resilience while managing complexity through well-established patterns and practices.

## 📋 Microservices Design Process

### Step 1: Service Decomposition Strategy

**Domain-Driven Design (DDD) Approach:**
```typescript
// Service boundary identification
interface ServiceBoundary {
  domain: string;
  subdomain: string;
  bounded_context: string;
  business_capabilities: string[];
  data_ownership: string[];
  team_ownership: string;
}

// Example: E-commerce domain decomposition
const ecommerceServices: ServiceBoundary[] = [
  {
    domain: "E-commerce",
    subdomain: "Customer Management",
    bounded_context: "Customer",
    business_capabilities: [
      "customer_registration",
      "customer_authentication", 
      "profile_management",
      "customer_preferences"
    ],
    data_ownership: ["customers", "customer_preferences"],
    team_ownership: "customer_team"
  },
  {
    domain: "E-commerce",
    subdomain: "Product Catalog",
    bounded_context: "Catalog",
    business_capabilities: [
      "product_management",
      "inventory_tracking",
      "pricing_management",
      "search_and_discovery"
    ],
    data_ownership: ["products", "inventory", "categories"],
    team_ownership: "catalog_team"
  },
  {
    domain: "E-commerce", 
    subdomain: "Order Management",
    bounded_context: "Orders",
    business_capabilities: [
      "order_creation",
      "payment_processing",
      "order_fulfillment",
      "order_tracking"
    ],
    data_ownership: ["orders", "payments", "shipments"],
    team_ownership: "order_team"
  }
];
```

**Service Size Guidelines:**
```yaml
service_sizing_principles:
  team_size_rule: "Two pizza team rule (6-10 people max)"
  
  database_rule: "One database per service maximum"
  
  deployment_independence: "Service can be deployed independently"
  
  business_capability: "Single well-defined business capability"
  
  code_size: 
    small: "< 10,000 lines of code"
    medium: "10,000 - 50,000 lines of code"
    large: "> 50,000 lines (consider splitting)"
    
  api_surface:
    endpoints: "< 20 public endpoints per service"
    complexity: "Single responsibility principle"
```

### Step 2: Inter-Service Communication Patterns

**Synchronous Communication (API Gateway Pattern):**
```typescript
// API Gateway configuration
interface ApiGatewayConfig {
  routes: ServiceRoute[];
  middleware: MiddlewareConfig[];
  authentication: AuthConfig;
  rateLimit: RateLimitConfig;
  monitoring: MonitoringConfig;
}

interface ServiceRoute {
  path: string;
  method: HttpMethod;
  service: string;
  endpoint: string;
  timeout: number;
  retries: number;
  circuit_breaker: CircuitBreakerConfig;
}

// Example API Gateway setup
const apiGateway: ApiGatewayConfig = {
  routes: [
    {
      path: "/api/customers/*",
      method: "ALL",
      service: "customer-service",
      endpoint: "http://customer-service:3001",
      timeout: 5000,
      retries: 3,
      circuit_breaker: {
        failure_threshold: 5,
        recovery_timeout: 30000,
        monitor_window: 60000
      }
    },
    {
      path: "/api/products/*", 
      method: "ALL",
      service: "catalog-service",
      endpoint: "http://catalog-service:3002",
      timeout: 5000,
      retries: 3,
      circuit_breaker: {
        failure_threshold: 5,
        recovery_timeout: 30000,
        monitor_window: 60000
      }
    }
  ],
  middleware: [
    { type: "authentication", order: 1 },
    { type: "rate_limiting", order: 2 },
    { type: "logging", order: 3 },
    { type: "metrics", order: 4 }
  ],
  authentication: {
    type: "JWT",
    secret: "${JWT_SECRET}",
    algorithms: ["HS256"]
  },
  rateLimit: {
    window: "15m",
    max_requests: 1000,
    strategy: "sliding_window"
  }
};
```

**Asynchronous Communication (Event-Driven Architecture):**
```typescript
// Event-driven communication patterns
interface EventDrivenArchitecture {
  event_store: EventStoreConfig;
  message_broker: MessageBrokerConfig;
  event_schemas: EventSchema[];
  saga_patterns: SagaPattern[];
}

// Event schema definition
interface EventSchema {
  event_name: string;
  version: string;
  schema: object;
  producers: string[];
  consumers: string[];
}

// Example: Order processing events
const orderEvents: EventSchema[] = [
  {
    event_name: "OrderCreated",
    version: "v1",
    schema: {
      orderId: "string",
      customerId: "string", 
      items: "ProductItem[]",
      totalAmount: "number",
      timestamp: "ISO8601"
    },
    producers: ["order-service"],
    consumers: ["inventory-service", "payment-service", "notification-service"]
  },
  {
    event_name: "PaymentProcessed",
    version: "v1", 
    schema: {
      orderId: "string",
      paymentId: "string",
      amount: "number",
      status: "success | failed",
      timestamp: "ISO8601"
    },
    producers: ["payment-service"],
    consumers: ["order-service", "fulfillment-service"]
  }
];

// Saga pattern for distributed transactions
interface SagaPattern {
  name: string;
  steps: SagaStep[];
  compensation: CompensationStep[];
}

const orderProcessingSaga: SagaPattern = {
  name: "OrderProcessingSaga",
  steps: [
    {
      service: "inventory-service",
      action: "reserve_items",
      input: "order_items",
      output: "reservation_id"
    },
    {
      service: "payment-service", 
      action: "process_payment",
      input: "payment_details",
      output: "payment_result"
    },
    {
      service: "fulfillment-service",
      action: "create_shipment",
      input: "order_details",
      output: "tracking_number"
    }
  ],
  compensation: [
    {
      step: "create_shipment",
      compensation: "cancel_shipment",
      service: "fulfillment-service"
    },
    {
      step: "process_payment",
      compensation: "refund_payment", 
      service: "payment-service"
    },
    {
      step: "reserve_items",
      compensation: "release_reservation",
      service: "inventory-service"
    }
  ]
};
```

### Step 3: Data Management Patterns

**Database Per Service Pattern:**
```yaml
# Data management strategy
data_management:
  customer_service:
    database_type: "PostgreSQL"
    schema: "customer_management"
    tables:
      - customers
      - customer_preferences
      - authentication_tokens
    access_pattern: "CRUD + Search"
    
  catalog_service:
    database_type: "MongoDB" 
    collections:
      - products
      - categories
      - product_reviews
    access_pattern: "Read-heavy + Search"
    search_engine: "Elasticsearch"
    
  order_service:
    database_type: "PostgreSQL"
    schema: "order_management" 
    tables:
      - orders
      - order_items
      - payments
      - shipments
    access_pattern: "Transactional"
    
  analytics_service:
    database_type: "ClickHouse"
    tables:
      - user_events
      - order_analytics
      - product_metrics
    access_pattern: "Write-heavy + Analytics"
```

**Event Sourcing Pattern:**
```typescript
// Event sourcing implementation
interface EventStore {
  append_event(stream_id: string, event: DomainEvent): Promise<void>;
  read_events(stream_id: string, from_version?: number): Promise<DomainEvent[]>;
  read_all_events(from_position?: number): Promise<DomainEvent[]>;
}

interface DomainEvent {
  id: string;
  stream_id: string;
  event_type: string;
  event_data: object;
  metadata: object;
  version: number;
  timestamp: Date;
}

// Example: Order aggregate with event sourcing
class OrderAggregate {
  private id: string;
  private version: number = 0;
  private events: DomainEvent[] = [];
  
  // State
  private customerId: string;
  private items: OrderItem[] = [];
  private status: OrderStatus = OrderStatus.Created;
  private totalAmount: number = 0;
  
  static async loadFromEvents(id: string, eventStore: EventStore): Promise<OrderAggregate> {
    const events = await eventStore.read_events(id);
    const aggregate = new OrderAggregate(id);
    
    events.forEach(event => aggregate.apply_event(event));
    aggregate.version = events.length;
    aggregate.events = [];  // Clear uncommitted events
    
    return aggregate;
  }
  
  create_order(customerId: string, items: OrderItem[]): void {
    const event: DomainEvent = {
      id: generateId(),
      stream_id: this.id,
      event_type: "OrderCreated",
      event_data: { customerId, items },
      metadata: { timestamp: new Date() },
      version: this.version + 1,
      timestamp: new Date()
    };
    
    this.apply_event(event);
    this.events.push(event);
  }
  
  private apply_event(event: DomainEvent): void {
    switch(event.event_type) {
      case "OrderCreated":
        this.customerId = event.event_data.customerId;
        this.items = event.event_data.items;
        this.status = OrderStatus.Created;
        this.totalAmount = this.calculate_total();
        break;
      case "OrderPaid":
        this.status = OrderStatus.Paid;
        break;
      case "OrderShipped":
        this.status = OrderStatus.Shipped;
        break;
    }
  }
  
  async save(eventStore: EventStore): Promise<void> {
    for (const event of this.events) {
      await eventStore.append_event(this.id, event);
    }
    this.version += this.events.length;
    this.events = [];
  }
}
```

## 🔧 Implementation Patterns

### Step 4: Service Mesh Architecture

**Istio Service Mesh Configuration:**
```yaml
# service-mesh.yml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: control-plane
spec:
  components:
    pilot:
      k8s:
        resources:
          requests:
            cpu: 500m
            memory: 2048Mi
    ingressGateways:
    - name: istio-ingressgateway
      enabled: true
      k8s:
        service:
          type: LoadBalancer
  values:
    global:
      meshID: mesh1
      network: network1
      
---
# Virtual Service for routing
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: customer-service
spec:
  http:
  - match:
    - uri:
        prefix: "/api/customers"
  - route:
    - destination:
        host: customer-service
        port:
          number: 3001
      weight: 90
    - destination:
        host: customer-service-v2
        port:
          number: 3001
      weight: 10  # Canary deployment
  - timeout: 30s
  - retries:
      attempts: 3
      per_try_timeout: 10s
      
---
# Circuit breaker configuration
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: customer-service
spec:
  host: customer-service
  trafficPolicy:
    outlierDetection:
      consecutiveErrors: 5
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
    connectionPool:
      tcp:
        maxConnections: 10
      http:
        http1MaxPendingRequests: 10
        maxRequestsPerConnection: 2
```

### Step 5: Observability and Monitoring

**Distributed Tracing Setup:**
```typescript
// OpenTelemetry tracing configuration
import { NodeSDK } from '@opentelemetry/auto-instrumentations-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

const jaegerExporter = new JaegerExporter({
  endpoint: 'http://jaeger:14268/api/traces',
});

const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'customer-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: '1.0.0',
  }),
  traceExporter: jaegerExporter,
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

// Custom tracing for business logic
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('customer-service', '1.0.0');

class CustomerService {
  async getCustomer(customerId: string): Promise<Customer> {
    const span = tracer.startSpan('get_customer', {
      attributes: {
        'customer.id': customerId,
        'operation.type': 'read'
      }
    });
    
    try {
      // Add custom events
      span.addEvent('validating_customer_id');
      
      if (!customerId) {
        throw new Error('Customer ID is required');
      }
      
      span.addEvent('fetching_from_database');
      const customer = await this.repository.findById(customerId);
      
      span.setAttributes({
        'customer.found': !!customer,
        'customer.status': customer?.status || 'not_found'
      });
      
      return customer;
    } catch (error) {
      span.recordException(error);
      span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
      throw error;
    } finally {
      span.end();
    }
  }
}
```

**Metrics and Logging:**
```typescript
// Prometheus metrics setup
import promClient from 'prom-client';

const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code', 'service'],
  buckets: [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10]
});

const httpRequestsTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code', 'service']
});

const databaseConnectionsActive = new promClient.Gauge({
  name: 'database_connections_active',
  help: 'Number of active database connections',
  labelNames: ['database', 'service']
});

// Custom business metrics
const customersCreated = new promClient.Counter({
  name: 'customers_created_total',
  help: 'Total number of customers created',
  labelNames: ['source', 'tier']
});

const orderValue = new promClient.Histogram({
  name: 'order_value_dollars',
  help: 'Distribution of order values in dollars',
  labelNames: ['customer_tier', 'product_category'],
  buckets: [10, 25, 50, 100, 250, 500, 1000, 2500, 5000]
});

// Structured logging with correlation IDs
import winston from 'winston';

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'customer-service',
    version: '1.0.0'
  },
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'app.log' })
  ]
});

// Correlation ID middleware
app.use((req, res, next) => {
  req.correlationId = req.headers['x-correlation-id'] || generateId();
  res.setHeader('x-correlation-id', req.correlationId);
  
  logger.child({ 
    correlationId: req.correlationId,
    traceId: req.headers['x-trace-id']
  });
  
  next();
});
```

## 🛡️ Resilience Patterns

### Step 6: Circuit Breaker Implementation

**Circuit Breaker Pattern:**
```typescript
// Circuit breaker implementation
enum CircuitBreakerState {
  CLOSED = 'CLOSED',
  OPEN = 'OPEN', 
  HALF_OPEN = 'HALF_OPEN'
}

interface CircuitBreakerOptions {
  failure_threshold: number;
  recovery_timeout: number;
  monitor_window: number;
  success_threshold: number;
}

class CircuitBreaker {
  private state: CircuitBreakerState = CircuitBreakerState.CLOSED;
  private failure_count: number = 0;
  private success_count: number = 0;
  private last_failure_time?: Date;
  private monitor_window_start: Date = new Date();
  
  constructor(private options: CircuitBreakerOptions) {}
  
  async execute<T>(operation: () => Promise<T>): Promise<T> {
    if (this.state === CircuitBreakerState.OPEN) {
      if (this.should_attempt_reset()) {
        this.state = CircuitBreakerState.HALF_OPEN;
        this.success_count = 0;
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
    }
    
    try {
      const result = await operation();
      this.record_success();
      return result;
    } catch (error) {
      this.record_failure();
      throw error;
    }
  }
  
  private record_success(): void {
    if (this.state === CircuitBreakerState.HALF_OPEN) {
      this.success_count++;
      if (this.success_count >= this.options.success_threshold) {
        this.state = CircuitBreakerState.CLOSED;
        this.reset_counts();
      }
    } else {
      this.reset_counts();
    }
  }
  
  private record_failure(): void {
    this.failure_count++;
    this.last_failure_time = new Date();
    
    if (this.failure_count >= this.options.failure_threshold) {
      this.state = CircuitBreakerState.OPEN;
    }
  }
  
  private should_attempt_reset(): boolean {
    if (!this.last_failure_time) return false;
    
    const time_since_failure = Date.now() - this.last_failure_time.getTime();
    return time_since_failure >= this.options.recovery_timeout;
  }
  
  private reset_counts(): void {
    this.failure_count = 0;
    this.success_count = 0;
    this.monitor_window_start = new Date();
  }
}

// Usage in service
class ExternalApiClient {
  private circuit_breaker: CircuitBreaker;
  
  constructor() {
    this.circuit_breaker = new CircuitBreaker({
      failure_threshold: 5,
      recovery_timeout: 30000,
      monitor_window: 60000,
      success_threshold: 3
    });
  }
  
  async fetchUserData(userId: string): Promise<UserData> {
    return this.circuit_breaker.execute(async () => {
      const response = await fetch(`/api/users/${userId}`, {
        timeout: 5000
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return response.json();
    });
  }
}
```

### Step 7: Retry and Timeout Patterns

**Exponential Backoff Retry:**
```typescript
// Retry mechanism with exponential backoff
interface RetryOptions {
  max_attempts: number;
  base_delay: number;
  max_delay: number;
  jitter: boolean;
  backoff_factor: number;
}

class RetryExecutor {
  constructor(private options: RetryOptions) {}
  
  async execute<T>(operation: () => Promise<T>): Promise<T> {
    let last_error: Error;
    
    for (let attempt = 1; attempt <= this.options.max_attempts; attempt++) {
      try {
        return await operation();
      } catch (error) {
        last_error = error;
        
        if (attempt === this.options.max_attempts) {
          throw error;
        }
        
        if (!this.is_retryable_error(error)) {
          throw error;
        }
        
        const delay = this.calculate_delay(attempt);
        await this.sleep(delay);
        
        logger.warn('Retry attempt', {
          attempt,
          max_attempts: this.options.max_attempts,
          delay,
          error: error.message
        });
      }
    }
    
    throw last_error;
  }
  
  private calculate_delay(attempt: number): number {
    let delay = this.options.base_delay * 
      Math.pow(this.options.backoff_factor, attempt - 1);
    
    delay = Math.min(delay, this.options.max_delay);
    
    if (this.options.jitter) {
      delay = delay * (0.5 + Math.random() * 0.5);
    }
    
    return Math.floor(delay);
  }
  
  private is_retryable_error(error: any): boolean {
    // Retry on network errors, timeouts, 5xx errors
    if (error.code === 'ECONNRESET' || 
        error.code === 'ETIMEDOUT' ||
        error.code === 'ENOTFOUND') {
      return true;
    }
    
    if (error.response?.status >= 500) {
      return true;
    }
    
    return false;
  }
  
  private sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

## 📊 Performance and Scaling Patterns

### Step 8: Caching Strategies

**Multi-Level Caching:**
```typescript
// Cache hierarchy implementation
interface CacheConfig {
  l1_cache: MemoryCacheConfig;
  l2_cache: RedisCacheConfig;
  l3_cache: CdnCacheConfig;
}

class MultilevelCache {
  private memory_cache: MemoryCache;
  private redis_cache: RedisCache;
  private cdn_cache: CdnCache;
  
  constructor(config: CacheConfig) {
    this.memory_cache = new MemoryCache(config.l1_cache);
    this.redis_cache = new RedisCache(config.l2_cache);
    this.cdn_cache = new CdnCache(config.l3_cache);
  }
  
  async get<T>(key: string): Promise<T | null> {
    // L1: In-memory cache
    let value = await this.memory_cache.get<T>(key);
    if (value) {
      return value;
    }
    
    // L2: Redis cache
    value = await this.redis_cache.get<T>(key);
    if (value) {
      // Populate L1 cache
      await this.memory_cache.set(key, value, 300); // 5 min TTL
      return value;
    }
    
    // L3: CDN/Distributed cache
    value = await this.cdn_cache.get<T>(key);
    if (value) {
      // Populate L2 and L1 caches
      await this.redis_cache.set(key, value, 3600); // 1 hour TTL
      await this.memory_cache.set(key, value, 300);  // 5 min TTL
      return value;
    }
    
    return null;
  }
  
  async set(key: string, value: any, ttl?: number): Promise<void> {
    // Set in all cache levels
    await Promise.all([
      this.memory_cache.set(key, value, Math.min(ttl || 300, 300)),
      this.redis_cache.set(key, value, ttl || 3600),
      this.cdn_cache.set(key, value, ttl || 86400)
    ]);
  }
  
  async invalidate(key: string): Promise<void> {
    await Promise.all([
      this.memory_cache.delete(key),
      this.redis_cache.delete(key),
      this.cdn_cache.delete(key)
    ]);
  }
}
```

## 📤 Deliverables

- **Microservices Architecture Design** with service boundaries and communication patterns
- **Service Implementation** with API specifications and inter-service contracts
- **Event-Driven Architecture** with event schemas and saga implementations
- **Service Mesh Configuration** with traffic management and security policies
- **Observability Stack** with tracing, metrics, and logging infrastructure
- **Resilience Patterns** with circuit breakers, retries, and failover mechanisms
- **Documentation** with architecture diagrams, API docs, and operational runbooks

## 🤝 Collaboration Points

**With software-architect:** Overall system architecture alignment and technology stack decisions
**With data-engineer:** Data consistency patterns, event sourcing, and cross-service queries
**With security-engineer:** Service-to-service authentication, network security, and data protection
**With deployment-engineer:** Container orchestration, service mesh deployment, and infrastructure scaling
**With qa-engineer:** Contract testing, integration testing, and chaos engineering practices

---
*Well-designed microservices architecture enables scalable, maintainable systems through proper decomposition, communication patterns, and operational excellence.*