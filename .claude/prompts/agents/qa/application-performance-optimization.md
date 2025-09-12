# Application Performance Optimization Prompt

**Agent Focus**: qa-engineer  
**Primary Specialization**: Performance testing, optimization strategies, monitoring implementation

## Context Analysis

The qa-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Technology stack for optimization approach
- **Project Scale**: Performance requirements (startup/basic, SME/moderate, enterprise/high-performance)
- **Business Domain**: Performance-critical areas (e-commerce checkout, fintech transactions, etc.)
- **Development Stage**: Current optimization needs (MVP/basic, production/advanced)

## Technology-Adaptive Performance Optimization

### Frontend Performance (React/Angular/Vue)

#### React Performance Optimization
```typescript
// Memoization and lazy loading
import React, { memo, useMemo, useCallback, lazy, Suspense } from 'react';

const ExpensiveComponent = lazy(() => import('./ExpensiveComponent'));

const OptimizedProductList = memo(({ products, onSelect }) => {
    const sortedProducts = useMemo(() => 
        products.sort((a, b) => a.price - b.price), [products]
    );
    
    const handleSelect = useCallback((product) => {
        onSelect(product);
    }, [onSelect]);
    
    return (
        <div>
            {sortedProducts.map(product => (
                <ProductCard 
                    key={product.id} 
                    product={product} 
                    onSelect={handleSelect}
                />
            ))}
        </div>
    );
});

// Virtual scrolling for large lists
import { FixedSizeList as List } from 'react-window';

const VirtualizedList = ({ items }) => (
    <List
        height={600}
        itemCount={items.length}
        itemSize={50}
        itemData={items}
    >
        {({ index, style }) => (
            <div style={style}>
                <ProductCard product={items[index]} />
            </div>
        )}
    </List>
);

// Performance monitoring
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
    console.log(metric.name, metric.value);
    // Send to your analytics service
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

#### Angular Performance Optimization
```typescript
// OnPush change detection strategy
import { Component, ChangeDetectionStrategy, TrackByFunction } from '@angular/core';

@Component({
    selector: 'app-product-list',
    changeDetection: ChangeDetectionStrategy.OnPush,
    template: `
        <div *ngFor="let product of products; trackBy: trackByFn">
            <app-product-card [product]="product"></app-product-card>
        </div>
    `
})
export class ProductListComponent {
    trackByFn: TrackByFunction<Product> = (index, item) => item.id;
    
    products$ = this.productService.getProducts().pipe(
        shareReplay(1) // Cache the result
    );
}

// Lazy loading modules
const routes: Routes = [
    {
        path: 'products',
        loadChildren: () => import('./products/products.module').then(m => m.ProductsModule)
    }
];

// Virtual scrolling with CDK
import { ScrollingModule } from '@angular/cdk/scrolling';

@Component({
    template: `
        <cdk-virtual-scroll-viewport itemSize="50" class="viewport">
            <div *cdkVirtualFor="let product of products">
                <app-product-card [product]="product"></app-product-card>
            </div>
        </cdk-virtual-scroll-viewport>
    `
})
export class VirtualizedProductListComponent {}
```

### Backend Performance Optimization

#### Java/Spring Boot Performance
```java
// Caching configuration
@Configuration
@EnableCaching
public class CacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        RedisCacheManager.Builder builder = RedisCacheManager
            .RedisCacheManagerBuilder
            .fromConnectionFactory(redisConnectionFactory())
            .cacheDefaults(cacheConfiguration(Duration.ofMinutes(10)));
        return builder.build();
    }
}

// Service with caching
@Service
public class ProductService {
    
    @Cacheable(value = "products", key = "#id")
    public Product findById(Long id) {
        return productRepository.findById(id).orElse(null);
    }
    
    @CacheEvict(value = "products", key = "#product.id")
    public Product save(Product product) {
        return productRepository.save(product);
    }
}

// Database query optimization
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    
    @Query("SELECT p FROM Product p LEFT JOIN FETCH p.category WHERE p.active = true")
    List<Product> findActiveProductsWithCategory();
    
    // Pagination for large datasets
    @Query(value = "SELECT * FROM products WHERE price BETWEEN :minPrice AND :maxPrice",
           countQuery = "SELECT count(*) FROM products WHERE price BETWEEN :minPrice AND :maxPrice",
           nativeQuery = true)
    Page<Product> findByPriceRange(@Param("minPrice") BigDecimal minPrice,
                                  @Param("maxPrice") BigDecimal maxPrice,
                                  Pageable pageable);
}

// Async processing
@Service
public class AsyncProductService {
    
    @Async
    @Retryable(value = {Exception.class}, maxAttempts = 3)
    public CompletableFuture<Void> processProductBatch(List<Product> products) {
        // Heavy processing logic
        return CompletableFuture.completedFuture(null);
    }
}
```

#### .NET Core Performance
```csharp
// Memory optimization with Span<T>
public class PerformantStringProcessor
{
    public string ProcessLargeString(string input)
    {
        ReadOnlySpan<char> span = input.AsSpan();
        Span<char> buffer = stackalloc char[256];
        
        // Process data without allocations
        for (int i = 0; i < span.Length; i++)
        {
            if (i < buffer.Length)
                buffer[i] = char.ToUpper(span[i]);
        }
        
        return new string(buffer);
    }
}

// Response caching
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet("{id}")]
    [ResponseCache(Duration = 300, VaryByHeader = "Accept")]
    public async Task<IActionResult> GetProduct(int id)
    {
        var product = await _productService.GetByIdAsync(id);
        return Ok(product);
    }
}

// Database optimization with compiled queries
public class ProductRepository
{
    private static readonly Func<AppDbContext, int, Task<Product>> GetProductById =
        EF.CompileAsyncQuery((AppDbContext context, int id) => 
            context.Products.FirstOrDefault(p => p.Id == id));
    
    public async Task<Product> FindByIdAsync(int id)
    {
        return await GetProductById(_context, id);
    }
}

// Background processing
public class ProductProcessingService : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            await ProcessPendingProducts();
            await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
        }
    }
}
```

#### Node.js Performance
```typescript
// Clustering for CPU-intensive tasks
import cluster from 'cluster';
import os from 'os';

if (cluster.isMaster) {
    const numCPUs = os.cpus().length;
    
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }
    
    cluster.on('exit', (worker) => {
        console.log(`Worker ${worker.process.pid} died`);
        cluster.fork();
    });
} else {
    // Start the application
    startServer();
}

// Efficient data streaming
import { Transform } from 'stream';
import { pipeline } from 'stream/promises';

class DataProcessor extends Transform {
    _transform(chunk: any, encoding: string, callback: Function) {
        // Process data in chunks to avoid memory issues
        const processed = this.processChunk(chunk);
        callback(null, processed);
    }
}

// Connection pooling and optimization
import { Pool } from 'pg';

const pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    max: 20, // Maximum connections
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
});

// Caching with Redis
import Redis from 'ioredis';

const redis = new Redis({
    retryDelayOnFailover: 100,
    enableOfflineQueue: false,
    maxRetriesPerRequest: 3,
});

export class CacheService {
    async get<T>(key: string): Promise<T | null> {
        const cached = await redis.get(key);
        return cached ? JSON.parse(cached) : null;
    }
    
    async set(key: string, value: any, ttl: number = 3600): Promise<void> {
        await redis.setex(key, ttl, JSON.stringify(value));
    }
}
```

#### Python Performance
```python
# Async processing with FastAPI
import asyncio
import asyncpg
from fastapi import FastAPI
from typing import List

app = FastAPI()

# Database connection pooling
async def create_db_pool():
    return await asyncpg.create_pool(
        "postgresql://user:pass@localhost/db",
        min_size=10,
        max_size=20
    )

# Efficient data processing with generators
def process_large_dataset(data_source):
    for batch in batch_iterator(data_source, batch_size=1000):
        yield process_batch(batch)

# Caching with Redis
import aioredis
from functools import wraps

async def cached(ttl: int = 3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            cached_result = await redis.get(cache_key)
            if cached_result:
                return json.loads(cached_result)
            
            result = await func(*args, **kwargs)
            await redis.setex(cache_key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator

# Profiling and monitoring
import cProfile
import time
from functools import wraps

def profile_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        pr.disable()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
```

## Performance Testing Implementation

### Load Testing with Artillery/K6
```javascript
// Artillery configuration
export default {
    target: 'http://localhost:3000',
    phases: [
        { duration: '30s', arrivalRate: 10 },
        { duration: '60s', arrivalRate: 50 },
        { duration: '30s', arrivalRate: 100 }
    ],
    scenarios: [
        {
            name: 'Product API Load Test',
            weight: 70,
            function: 'testProductAPI'
        },
        {
            name: 'User Authentication',
            weight: 30,
            function: 'testAuth'
        }
    ]
};

export function testProductAPI(userContext, events) {
    const productId = Math.floor(Math.random() * 1000) + 1;
    
    http.get(`/api/products/${productId}`, {
        headers: {
            'Authorization': `Bearer ${userContext.vars.token}`
        }
    }).then(response => {
        if (response.status !== 200) {
            events.emit('error', `Unexpected status: ${response.status}`);
        }
    });
}
```

### Database Performance Monitoring
```sql
-- PostgreSQL performance queries
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- Index usage analysis
SELECT 
    schemaname,
    tablename,
    attname,
    n_distinct,
    correlation
FROM pg_stats
WHERE schemaname = 'public'
ORDER BY n_distinct DESC;
```

### Application Performance Monitoring (APM)
```typescript
// Custom performance metrics
class PerformanceMonitor {
    private metrics: Map<string, number[]> = new Map();
    
    startTimer(operation: string): () => void {
        const start = performance.now();
        
        return () => {
            const duration = performance.now() - start;
            this.recordMetric(operation, duration);
        };
    }
    
    recordMetric(operation: string, value: number): void {
        if (!this.metrics.has(operation)) {
            this.metrics.set(operation, []);
        }
        this.metrics.get(operation)!.push(value);
    }
    
    getStats(operation: string) {
        const values = this.metrics.get(operation) || [];
        return {
            avg: values.reduce((a, b) => a + b, 0) / values.length,
            min: Math.min(...values),
            max: Math.max(...values),
            count: values.length
        };
    }
}

// Usage example
const monitor = new PerformanceMonitor();

async function processOrder(order: Order) {
    const endTimer = monitor.startTimer('process_order');
    
    try {
        // Process order logic
        await orderService.process(order);
    } finally {
        endTimer();
    }
}
```

## Implementation Strategy

### 1. Performance Baseline Establishment
- Set up monitoring for key metrics (response time, throughput, resource usage)
- Establish performance budgets and SLAs
- Create automated performance regression tests

### 2. Code-Level Optimizations
- Implement caching strategies at appropriate layers
- Optimize database queries and add proper indexing
- Use asynchronous processing for heavy operations
- Implement connection pooling and resource management

### 3. Infrastructure Optimizations
- Set up CDN for static assets
- Implement load balancing and horizontal scaling
- Optimize database configuration and query performance
- Configure proper caching layers (Redis, Memcached)

### 4. Monitoring and Alerting
- Set up APM tools (New Relic, Datadog, Application Insights)
- Create performance dashboards and alerts
- Implement error tracking and performance regression detection

## Success Criteria

1. **Response Time**: API responses under defined SLA (e.g., 95th percentile < 200ms)
2. **Throughput**: Handle target requests per second without degradation
3. **Resource Usage**: CPU and memory usage within acceptable limits
4. **Database Performance**: Query execution times optimized with proper indexing
5. **User Experience**: Frontend performance metrics (LCP, FID, CLS) within targets
6. **Scalability**: System handles expected load increases gracefully

## Performance Monitoring Checklist

- [ ] Application Performance Monitoring (APM) configured
- [ ] Database query performance monitoring
- [ ] Frontend Core Web Vitals tracking
- [ ] Error rate and availability monitoring
- [ ] Resource usage (CPU, memory, disk) tracking
- [ ] Performance regression testing in CI/CD
- [ ] Load testing scenarios for critical paths
- [ ] Performance budgets defined and enforced