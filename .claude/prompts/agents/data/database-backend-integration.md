# Database-Backend Integration Prompt

**Agent Collaboration**: data-engineer + api-engineer  
**Primary Focus**: Database schema design, ORM configuration, API data layer architecture

## Context Analysis

The data-engineer and api-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Backend technology stack (Java/Spring, .NET Core, Node.js, Python, etc.)
- **Database Technology**: Primary database system (PostgreSQL, MySQL, SQLite, MongoDB)
- **Project Scale**: Architecture complexity (startup/simple, SME/moderate, enterprise/complex)
- **Business Domain**: Data modeling requirements (e-commerce, fintech, healthcare, etc.)

## Technology-Adaptive Implementation

### Java/Spring Boot + Database
```java
// Entity with validation and audit
@Entity
@Table(name = "products")
@EntityListeners(AuditingEntityListener.class)
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    @NotBlank
    private String name;
    
    @Column(precision = 10, scale = 2)
    @DecimalMin("0.0")
    private BigDecimal price;
    
    @CreatedDate
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
}

// Repository with custom queries
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    @Query("SELECT p FROM Product p WHERE p.price BETWEEN :minPrice AND :maxPrice")
    List<Product> findByPriceRange(@Param("minPrice") BigDecimal minPrice, 
                                  @Param("maxPrice") BigDecimal maxPrice);
    
    @Query(value = "SELECT * FROM products WHERE created_at >= ?1", nativeQuery = true)
    List<Product> findRecentProducts(LocalDateTime since);
}

// Service with transaction management
@Service
@Transactional
public class ProductService {
    @Autowired
    private ProductRepository productRepository;
    
    public Product createProduct(ProductDto productDto) {
        Product product = new Product();
        BeanUtils.copyProperties(productDto, product);
        return productRepository.save(product);
    }
    
    @Transactional(readOnly = true)
    public Page<Product> findProducts(Pageable pageable) {
        return productRepository.findAll(pageable);
    }
}
```

### .NET Core + Entity Framework
```csharp
// Entity with annotations
public class Product
{
    public int Id { get; set; }
    
    [Required]
    [StringLength(200)]
    public string Name { get; set; }
    
    [Column(TypeName = "decimal(10,2)")]
    [Range(0, double.MaxValue)]
    public decimal Price { get; set; }
    
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }
}

// DbContext with configuration
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {}
    
    public DbSet<Product> Products { get; set; }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Product>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Name).IsRequired().HasMaxLength(200);
            entity.Property(e => e.Price).HasColumnType("decimal(10,2)");
            entity.Property(e => e.CreatedAt).HasDefaultValueSql("GETDATE()");
        });
    }
    
    public override int SaveChanges()
    {
        var entries = ChangeTracker.Entries()
            .Where(e => e.State == EntityState.Added || e.State == EntityState.Modified);
            
        foreach (var entry in entries)
        {
            if (entry.State == EntityState.Added)
                entry.Property("CreatedAt").CurrentValue = DateTime.UtcNow;
            entry.Property("UpdatedAt").CurrentValue = DateTime.UtcNow;
        }
        
        return base.SaveChanges();
    }
}

// Repository pattern with async operations
public interface IProductRepository
{
    Task<Product> GetByIdAsync(int id);
    Task<IEnumerable<Product>> GetAllAsync();
    Task<Product> CreateAsync(Product product);
    Task UpdateAsync(Product product);
    Task DeleteAsync(int id);
}

public class ProductRepository : IProductRepository
{
    private readonly AppDbContext _context;
    
    public ProductRepository(AppDbContext context)
    {
        _context = context;
    }
    
    public async Task<Product> GetByIdAsync(int id)
    {
        return await _context.Products.FindAsync(id);
    }
    
    public async Task<IEnumerable<Product>> GetAllAsync()
    {
        return await _context.Products.ToListAsync();
    }
    
    public async Task<Product> CreateAsync(Product product)
    {
        _context.Products.Add(product);
        await _context.SaveChangesAsync();
        return product;
    }
}
```

### Node.js + TypeORM/Prisma
```typescript
// TypeORM Entity
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

@Entity('products')
export class Product {
    @PrimaryGeneratedColumn()
    id: number;
    
    @Column({ length: 200 })
    name: string;
    
    @Column('decimal', { precision: 10, scale: 2 })
    price: number;
    
    @CreateDateColumn()
    createdAt: Date;
    
    @UpdateDateColumn()
    updatedAt: Date;
}

// Repository service
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

@Injectable()
export class ProductService {
    constructor(
        @InjectRepository(Product)
        private productRepository: Repository<Product>,
    ) {}
    
    async findAll(): Promise<Product[]> {
        return this.productRepository.find();
    }
    
    async findOne(id: number): Promise<Product> {
        return this.productRepository.findOne({ where: { id } });
    }
    
    async create(productData: Partial<Product>): Promise<Product> {
        const product = this.productRepository.create(productData);
        return this.productRepository.save(product);
    }
    
    async update(id: number, productData: Partial<Product>): Promise<Product> {
        await this.productRepository.update(id, productData);
        return this.findOne(id);
    }
}
```

### Python + SQLAlchemy
```python
# Models with SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': float(self.price),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Repository pattern
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self) -> List[Product]:
        return self.session.query(Product).all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.session.query(Product).filter(Product.id == product_id).first()
    
    def create(self, product_data: dict) -> Product:
        product = Product(**product_data)
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product
    
    def update(self, product_id: int, product_data: dict) -> Optional[Product]:
        product = self.get_by_id(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.session.commit()
            self.session.refresh(product)
        return product

# FastAPI service integration
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    created_at: str
    updated_at: str

@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    created_product = repository.create(product.dict())
    return ProductResponse(**created_product.to_dict())
```

## Implementation Strategy

### 1. Database Schema Analysis
- Analyze existing database structure or design new schema
- Implement proper indexing strategy for query performance
- Define relationships and foreign key constraints
- Set up audit trails and soft deletes if required

### 2. ORM Configuration
- Configure connection pooling and transaction management
- Set up migrations and versioning system
- Implement proper error handling and logging
- Configure caching strategy (Redis, in-memory cache)

### 3. Data Access Layer
- Implement repository pattern for clean separation
- Create service layer for business logic
- Set up proper validation and sanitization
- Implement pagination and filtering capabilities

### 4. API Integration Points
- Design RESTful endpoints with proper HTTP methods
- Implement proper status codes and error responses
- Set up request/response DTOs with validation
- Configure CORS and security policies

## Database-Specific Optimizations

### PostgreSQL Integration
```sql
-- Performance indexes
CREATE INDEX CONCURRENTLY idx_products_price ON products(price);
CREATE INDEX CONCURRENTLY idx_products_created_at ON products(created_at);

-- Full-text search
CREATE INDEX CONCURRENTLY idx_products_name_fts ON products USING gin(to_tsvector('english', name));
```

### MySQL Integration
```sql
-- Optimized table structure
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_price (price),
    INDEX idx_created (created_at)
) ENGINE=InnoDB;
```

### SQLite Integration (Desktop Apps)
```sql
-- Lightweight structure with proper constraints
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK(length(name) > 0),
    price REAL NOT NULL CHECK(price >= 0),
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TRIGGER update_products_timestamp 
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = datetime('now') WHERE id = NEW.id;
END;
```

## Success Criteria

1. **Database Integration**: Proper ORM configuration with connection management
2. **Data Validation**: Input validation and business rule enforcement
3. **Performance**: Optimized queries with appropriate indexing
4. **Error Handling**: Comprehensive error handling and logging
5. **API Consistency**: Standardized request/response formats
6. **Transaction Management**: Proper ACID compliance and rollback handling

## Common Pitfalls to Avoid

- N+1 query problems with lazy loading
- Missing database indexes on frequently queried fields
- Inadequate connection pool configuration
- Lack of proper error handling for constraint violations
- Missing transaction boundaries for multi-step operations
- Exposing internal database structure through API responses