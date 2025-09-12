# Microservices Architecture Patterns

**Agent: api-engineer**
**Purpose: Design and implement scalable microservices architecture with proven patterns and best practices**

---

## Context Analysis

The api-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Technology stack for microservices implementation (Java/Spring Cloud, .NET/Dapr, Node.js/Kubernetes, Python/FastAPI)
- **Business Domain**: Domain decomposition strategy and service boundary identification
- **Project Scale**: Microservices complexity based on team size and system requirements
- **Infrastructure Preferences**: Cloud platform, containerization, and orchestration choices
- **Communication Patterns**: Synchronous vs asynchronous communication requirements

Based on this analysis, the engineer will select technology-appropriate microservices patterns and implementation strategies.

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

## Technology-Adaptive Implementation

### Java + Spring Cloud Microservices

**Recommended Pattern:** Spring Cloud ecosystem with Eureka, Gateway, and Config Server

```java
// Service Discovery with Eureka
@SpringBootApplication
@EnableEurekaServer
public class DiscoveryServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(DiscoveryServerApplication.class, args);
    }
}

// API Gateway with Spring Cloud Gateway
@SpringBootApplication
@EnableEurekaClient
public class GatewayApplication {
    
    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("customer-service", r -> r.path("/api/customers/**")
                .filters(f -> f
                    .circuitBreaker(config -> config
                        .setName("customer-service-cb")
                        .setFallbackUri("/fallback/customers"))
                    .retry(retryConfig -> retryConfig.setRetries(3)))
                .uri("lb://customer-service"))
            .route("order-service", r -> r.path("/api/orders/**")
                .filters(f -> f
                    .circuitBreaker(config -> config
                        .setName("order-service-cb")
                        .setFallbackUri("/fallback/orders"))
                    .rateLimit(config -> config
                        .setRateLimiter(RedisRateLimiter.class)
                        .setKeyResolver(exchange -> Mono.just("global"))))
                .uri("lb://order-service"))
            .build();
    }
}

// Microservice Implementation
@RestController
@RequestMapping("/api/customers")
@Slf4j
public class CustomerController {
    
    private final CustomerService customerService;
    private final OrderServiceClient orderServiceClient;
    
    @GetMapping("/{id}")
    @CircuitBreaker(name = "customer-service", fallbackMethod = "getCustomerFallback")
    @TimeLimiter(name = "customer-service")
    @Retry(name = "customer-service")
    public CompletableFuture<ResponseEntity<CustomerDto>> getCustomer(@PathVariable String id) {
        return CompletableFuture.supplyAsync(() -> {
            CustomerDto customer = customerService.findById(id);
            List<OrderDto> orders = orderServiceClient.getOrdersByCustomerId(id);
            customer.setOrders(orders);
            return ResponseEntity.ok(customer);
        });
    }
    
    public CompletableFuture<ResponseEntity<CustomerDto>> getCustomerFallback(
            String id, Exception ex) {
        log.warn("Fallback triggered for customer {}: {}", id, ex.getMessage());
        CustomerDto fallbackCustomer = new CustomerDto();
        fallbackCustomer.setId(id);
        fallbackCustomer.setName("Service Unavailable");
        return CompletableFuture.completedFuture(ResponseEntity.ok(fallbackCustomer));
    }
}

// Feign Client for Inter-Service Communication
@FeignClient(name = "order-service", fallback = OrderServiceClientFallback.class)
public interface OrderServiceClient {
    
    @GetMapping("/api/orders/customer/{customerId}")
    List<OrderDto> getOrdersByCustomerId(@PathVariable("customerId") String customerId);
}

@Component
public class OrderServiceClientFallback implements OrderServiceClient {
    
    @Override
    public List<OrderDto> getOrdersByCustomerId(String customerId) {
        log.warn("Order service unavailable for customer: {}", customerId);
        return Collections.emptyList();
    }
}

// Configuration Properties
@ConfigurationProperties(prefix = "app.microservices")
@Data
public class MicroservicesConfig {
    private Resilience4j resilience4j;
    private ServiceDiscovery serviceDiscovery;
    
    @Data
    public static class Resilience4j {
        private CircuitBreaker circuitBreaker;
        private Retry retry;
        private RateLimiter rateLimiter;
        
        @Data
        public static class CircuitBreaker {
            private int failureRateThreshold = 50;
            private int waitDurationInOpenState = 30000;
            private int slidingWindowSize = 10;
        }
    }
}
```

### .NET Core + Dapr Microservices

**Recommended Pattern:** Dapr sidecar pattern with service mesh capabilities

```csharp
// Startup Configuration for Dapr
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers().AddDapr();
        services.AddDaprClient();
        
        // Service registration
        services.AddScoped<ICustomerService, CustomerService>();
        services.AddScoped<IOrderService, OrderService>();
        
        // Health checks
        services.AddHealthChecks()
            .AddCheck<DatabaseHealthCheck>("database")
            .AddDapr();
    }
    
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        app.UseRouting();
        app.UseCloudEvents();
        
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers();
            endpoints.MapSubscribeHandler();
            endpoints.MapHealthChecks("/health");
        });
    }
}

// Customer Service with Dapr State Management
[ApiController]
[Route("api/[controller]")]
public class CustomersController : ControllerBase
{
    private readonly DaprClient _daprClient;
    private readonly ILogger<CustomersController> _logger;
    
    public CustomersController(DaprClient daprClient, ILogger<CustomersController> logger)
    {
        _daprClient = daprClient;
        _logger = logger;
    }
    
    [HttpGet("{id}")]
    public async Task<ActionResult<CustomerDto>> GetCustomer(string id)
    {
        try
        {
            // Get customer from state store
            var customer = await _daprClient.GetStateAsync<CustomerDto>("statestore", id);
            
            if (customer == null)
            {
                return NotFound();
            }
            
            // Call order service via Dapr service invocation
            var orders = await _daprClient.InvokeMethodAsync<List<OrderDto>>(
                "order-service", 
                $"api/orders/customer/{id}", 
                HttpMethod.Get);
                
            customer.Orders = orders;
            return Ok(customer);
        }
        catch (DaprException ex)
        {
            _logger.LogError(ex, "Dapr error occurred while getting customer {CustomerId}", id);
            return StatusCode(500, "Service unavailable");
        }
    }
    
    [HttpPost]
    public async Task<ActionResult<CustomerDto>> CreateCustomer([FromBody] CreateCustomerRequest request)
    {
        var customer = new CustomerDto
        {
            Id = Guid.NewGuid().ToString(),
            Name = request.Name,
            Email = request.Email,
            CreatedAt = DateTime.UtcNow
        };
        
        // Save to state store
        await _daprClient.SaveStateAsync("statestore", customer.Id, customer);
        
        // Publish event
        await _daprClient.PublishEventAsync("pubsub", "customer.created", new CustomerCreatedEvent
        {
            CustomerId = customer.Id,
            Name = customer.Name,
            Email = customer.Email,
            Timestamp = DateTime.UtcNow
        });
        
        return CreatedAtAction(nameof(GetCustomer), new { id = customer.Id }, customer);
    }
    
    // Event handler for order events
    [HttpPost("events/order.completed")]
    [Topic("pubsub", "order.completed")]
    public async Task HandleOrderCompleted([FromBody] OrderCompletedEvent orderEvent)
    {
        _logger.LogInformation("Processing order completed event for customer {CustomerId}", 
            orderEvent.CustomerId);
        
        // Update customer statistics
        var customer = await _daprClient.GetStateAsync<CustomerDto>("statestore", orderEvent.CustomerId);
        if (customer != null)
        {
            customer.TotalOrders += 1;
            customer.TotalSpent += orderEvent.Amount;
            customer.LastOrderDate = orderEvent.CompletedAt;
            
            await _daprClient.SaveStateAsync("statestore", customer.Id, customer);
        }
    }
}

// Dapr Configuration (components/statestore.yaml)
/*
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: statestore
spec:
  type: state.redis
  version: v1
  metadata:
  - name: redisHost
    value: redis:6379
  - name: redisPassword
    value: ""
  - name: actorStateStore
    value: "true"
*/

// Dapr Pub/Sub Configuration (components/pubsub.yaml)
/*
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: pubsub
spec:
  type: pubsub.redis
  version: v1
  metadata:
  - name: redisHost
    value: redis:6379
  - name: redisPassword
    value: ""
*/
```

### Node.js + NestJS + Kubernetes

**Recommended Pattern:** NestJS microservices with Kubernetes native patterns

```typescript
// Main Application with Microservices
@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'ORDER_SERVICE',
        transport: Transport.REDIS,
        options: {
          host: 'redis',
          port: 6379,
        },
      },
      {
        name: 'NOTIFICATION_SERVICE',
        transport: Transport.KAFKA,
        options: {
          client: {
            clientId: 'customer-service',
            brokers: ['kafka:9092'],
          },
          consumer: {
            groupId: 'customer-service-group',
          },
        },
      },
    ]),
    ConfigModule.forRoot(),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: parseInt(process.env.DB_PORT),
      username: process.env.DB_USERNAME,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      entities: [Customer],
      synchronize: process.env.NODE_ENV !== 'production',
    }),
    TypeOrmModule.forFeature([Customer]),
  ],
  controllers: [CustomerController],
  providers: [CustomerService, HealthController],
})
export class AppModule {}

// Microservice Controller with Circuit Breaker
@Controller('customers')
@ApiTags('customers')
export class CustomerController {
  constructor(
    private readonly customerService: CustomerService,
    @Inject('ORDER_SERVICE') private orderClient: ClientProxy,
    @Inject('NOTIFICATION_SERVICE') private notificationClient: ClientProxy,
  ) {}

  @Get(':id')
  @UseInterceptors(CacheInterceptor)
  @CacheTTL(300) // 5 minutes
  @ApiOperation({ summary: 'Get customer by ID' })
  async getCustomer(@Param('id') id: string): Promise<CustomerDto> {
    const customer = await this.customerService.findById(id);
    
    if (!customer) {
      throw new NotFoundException('Customer not found');
    }

    // Use circuit breaker for external service calls
    try {
      const orders = await this.orderClient
        .send('get_customer_orders', { customerId: id })
        .pipe(
          timeout(5000),
          retry(3),
          catchError((error) => {
            console.warn('Order service unavailable:', error.message);
            return of([]);
          }),
        )
        .toPromise();

      return {
        ...customer,
        orders,
      };
    } catch (error) {
      // Return customer without orders if service is down
      return customer;
    }
  }

  @Post()
  @ApiOperation({ summary: 'Create new customer' })
  async createCustomer(@Body() createCustomerDto: CreateCustomerDto): Promise<CustomerDto> {
    const customer = await this.customerService.create(createCustomerDto);

    // Publish event asynchronously
    this.notificationClient.emit('customer.created', {
      customerId: customer.id,
      email: customer.email,
      name: customer.name,
      timestamp: new Date().toISOString(),
    });

    return customer;
  }

  @EventPattern('order.completed')
  async handleOrderCompleted(@Payload() data: OrderCompletedEvent) {
    try {
      await this.customerService.updateOrderStats(data.customerId, {
        totalOrders: 1,
        totalSpent: data.amount,
        lastOrderDate: data.completedAt,
      });

      console.log(`Updated customer ${data.customerId} order statistics`);
    } catch (error) {
      console.error('Failed to update customer order stats:', error);
      // Could republish to dead letter queue here
    }
  }

  @Get('health')
  @ApiExcludeEndpoint()
  getHealth() {
    return { status: 'ok', timestamp: new Date().toISOString() };
  }
}

// Kubernetes Deployment Configuration
const kubernetesConfig = `
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customer-service
  labels:
    app: customer-service
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: customer-service
      version: v1
  template:
    metadata:
      labels:
        app: customer-service
        version: v1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "3000"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: customer-service
        image: customer-service:latest
        ports:
        - containerPort: 3000
        env:
        - name: DB_HOST
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        - name: REDIS_URL
          value: "redis://redis:6379"
        - name: KAFKA_BROKERS
          value: "kafka:9092"
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: customer-service
  labels:
    app: customer-service
spec:
  selector:
    app: customer-service
  ports:
  - port: 80
    targetPort: 3000
    protocol: TCP
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: customer-service-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /api/customers
        pathType: Prefix
        backend:
          service:
            name: customer-service
            port:
              number: 80
`;

// Service Mesh with Istio Configuration
const istioConfig = `
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: customer-service
spec:
  hosts:
  - customer-service
  http:
  - fault:
      delay:
        percentage:
          value: 0.1
        fixedDelay: 5s
  - match:
    - headers:
        version:
          exact: v2
    route:
    - destination:
        host: customer-service
        subset: v2
      weight: 100
  - route:
    - destination:
        host: customer-service
        subset: v1
      weight: 90
    - destination:
        host: customer-service
        subset: v2
      weight: 10
  timeout: 30s
  retries:
    attempts: 3
    perTryTimeout: 10s
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: customer-service
spec:
  host: customer-service
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
  trafficPolicy:
    outlierDetection:
      consecutiveErrors: 3
      interval: 30s
      baseEjectionTime: 30s
    circuitBreaker:
      http:
        http1MaxPendingRequests: 10
        maxRequestsPerConnection: 2
      connectionPool:
        tcp:
          maxConnections: 10
`;
```

### Python + FastAPI + asyncio

**Recommended Pattern:** Async microservices with message queues and service discovery

```python
# FastAPI Microservice with Async Patterns
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import asyncio
import aioredis
from typing import List, Optional
import httpx
from contextlib import asynccontextmanager
import logging
from prometheus_fastapi_instrumentator import Instrumentator

# Application Lifespan Management
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.redis = await aioredis.from_url("redis://redis:6379")
    app.state.http_client = httpx.AsyncClient()
    app.state.service_registry = ServiceRegistry()
    
    # Register service
    await app.state.service_registry.register_service(
        service_name="customer-service",
        host="customer-service",
        port=8000,
        health_check="/health"
    )
    
    yield
    
    # Shutdown
    await app.state.redis.close()
    await app.state.http_client.aclose()
    await app.state.service_registry.deregister_service("customer-service")

# FastAPI Application
app = FastAPI(
    title="Customer Service",
    version="1.0.0",
    lifespan=lifespan
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["customer-service", "*.example.com"]
)

# Metrics
Instrumentator().instrument(app).expose(app)

# Service Discovery
class ServiceRegistry:
    def __init__(self):
        self.services = {}
        
    async def register_service(self, service_name: str, host: str, port: int, health_check: str):
        self.services[service_name] = {
            "host": host,
            "port": port,
            "health_check": health_check,
            "last_seen": asyncio.get_event_loop().time()
        }
        
    async def get_service(self, service_name: str) -> Optional[dict]:
        return self.services.get(service_name)
        
    async def deregister_service(self, service_name: str):
        self.services.pop(service_name, None)

# Circuit Breaker Implementation
class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        
    async def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if asyncio.get_event_loop().time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise HTTPException(status_code=503, detail="Circuit breaker is OPEN")
                
        try:
            result = await func(*args, **kwargs)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = asyncio.get_event_loop().time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                
            raise e

# Service Communication with Retry and Circuit Breaker
class ServiceCommunication:
    def __init__(self):
        self.circuit_breakers = {}
        
    def get_circuit_breaker(self, service_name: str) -> CircuitBreaker:
        if service_name not in self.circuit_breakers:
            self.circuit_breakers[service_name] = CircuitBreaker()
        return self.circuit_breakers[service_name]
    
    async def call_service(self, service_name: str, path: str, method: str = "GET", **kwargs):
        circuit_breaker = self.get_circuit_breaker(service_name)
        
        async def make_request():
            service_info = await app.state.service_registry.get_service(service_name)
            if not service_info:
                raise HTTPException(status_code=503, detail=f"Service {service_name} not found")
                
            url = f"http://{service_info['host']}:{service_info['port']}{path}"
            
            # Retry logic with exponential backoff
            max_retries = 3
            base_delay = 1
            
            for attempt in range(max_retries):
                try:
                    async with app.state.http_client as client:
                        response = await client.request(method, url, timeout=5.0, **kwargs)
                        response.raise_for_status()
                        return response.json()
                except httpx.TimeoutException:
                    if attempt == max_retries - 1:
                        raise HTTPException(status_code=504, detail="Service timeout")
                    await asyncio.sleep(base_delay * (2 ** attempt))
                except httpx.HTTPStatusError as e:
                    if e.response.status_code >= 500:
                        if attempt == max_retries - 1:
                            raise HTTPException(status_code=e.response.status_code, 
                                             detail="Service unavailable")
                        await asyncio.sleep(base_delay * (2 ** attempt))
                    else:
                        raise HTTPException(status_code=e.response.status_code, 
                                         detail="Service error")
        
        return await circuit_breaker.call(make_request)

# Dependencies
async def get_redis():
    return app.state.redis

async def get_service_communication():
    return ServiceCommunication()

# API Routes
@app.get("/api/customers/{customer_id}")
async def get_customer(
    customer_id: str, 
    redis: aioredis.Redis = Depends(get_redis),
    service_comm: ServiceCommunication = Depends(get_service_communication)
):
    # Try cache first
    cached_customer = await redis.get(f"customer:{customer_id}")
    if cached_customer:
        customer_data = json.loads(cached_customer)
    else:
        # Get from database (simplified)
        customer_data = await get_customer_from_db(customer_id)
        if not customer_data:
            raise HTTPException(status_code=404, detail="Customer not found")
            
        # Cache for 5 minutes
        await redis.setex(f"customer:{customer_id}", 300, json.dumps(customer_data))
    
    # Get orders from order service with circuit breaker
    try:
        orders = await service_comm.call_service(
            "order-service", 
            f"/api/orders/customer/{customer_id}"
        )
        customer_data["orders"] = orders
    except HTTPException as e:
        logging.warning(f"Failed to get orders for customer {customer_id}: {e.detail}")
        customer_data["orders"] = []
    
    return customer_data

@app.post("/api/customers")
async def create_customer(
    customer_data: CustomerCreateRequest,
    background_tasks: BackgroundTasks,
    redis: aioredis.Redis = Depends(get_redis)
):
    # Create customer (simplified)
    customer = await create_customer_in_db(customer_data)
    
    # Cache the new customer
    await redis.setex(f"customer:{customer['id']}", 300, json.dumps(customer))
    
    # Publish event asynchronously
    background_tasks.add_task(
        publish_customer_created_event, 
        customer['id'], 
        customer['email']
    )
    
    return customer

# Event Publishing
async def publish_customer_created_event(customer_id: str, email: str):
    try:
        # Publish to Redis Streams or message queue
        await app.state.redis.xadd(
            "customer.events",
            {
                "event_type": "customer.created",
                "customer_id": customer_id,
                "email": email,
                "timestamp": datetime.utcnow().isoformat()
            }
        )
        logging.info(f"Published customer.created event for {customer_id}")
    except Exception as e:
        logging.error(f"Failed to publish customer.created event: {e}")

# Health Check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

# Docker Compose Configuration for Development
docker_compose_config = """
version: '3.8'
services:
  customer-service:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379
      - DATABASE_URL=postgresql://user:pass@postgres:5432/customers
    depends_on:
      - redis
      - postgres
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
      
  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: customers
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic microservices patterns:

```yaml
# Generic Microservices Configuration
microservices:
  architecture_pattern: "service_per_domain"
  communication:
    sync: "HTTP/REST with API Gateway"
    async: "Message Queue (Redis/RabbitMQ/Kafka)"
  
  service_discovery: "DNS-based or Registry-based"
  load_balancing: "Round-robin or Weighted"
  
  resilience_patterns:
    - circuit_breaker
    - retry_with_exponential_backoff
    - timeout_handling
    - bulkhead_isolation
    
  data_management: "Database-per-service"
  
  observability:
    tracing: "Distributed tracing with correlation IDs"
    metrics: "Prometheus + Grafana"
    logging: "Centralized logging with ELK stack"
    
  deployment: "Containerized with Kubernetes or Docker Swarm"
  
  security:
    authentication: "JWT with shared secret or PKI"
    authorization: "Role-based or Attribute-based"
    communication: "mTLS for service-to-service"
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

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Microservices framework** from primary_language field (Java/Spring Cloud, .NET/Dapr, Node.js/NestJS, Python/FastAPI)
- **Communication requirements** for synchronous vs asynchronous patterns
- **Infrastructure preferences** for container orchestration and service mesh
- **Data consistency needs** for event sourcing vs traditional approaches

### 2. Architecture Pattern Selection

Select patterns based on detected technology and scale:
- **Java/Spring Cloud**: Eureka discovery, Config Server, Gateway, Circuit Breaker
- **.NET/Dapr**: Sidecar pattern with state management and pub/sub
- **Node.js/NestJS**: Kubernetes-native with message queues and caching
- **Python/FastAPI**: Async patterns with service discovery and circuit breakers
- **Generic**: Standard microservices patterns with resilience and observability

### 3. Implementation Approach

Apply technology-specific microservices patterns:
- **Service decomposition**: Domain-driven design with bounded contexts
- **Communication**: Framework-appropriate sync/async patterns
- **Data management**: Database-per-service with eventual consistency
- **Resilience**: Circuit breakers, retries, and timeout handling
- **Observability**: Distributed tracing, metrics, and structured logging

### 4. Success Criteria

Microservices architecture validation checklist:
- **Technology alignment**: Implementation follows framework best practices
- **Service boundaries**: Clear domain separation with minimal coupling
- **Scalability**: Independent service scaling and deployment
- **Resilience**: Fault tolerance with graceful degradation
- **Observability**: Comprehensive monitoring and debugging capabilities

---
*Well-designed microservices architecture enables scalable, maintainable systems through proper decomposition, communication patterns, and operational excellence.*