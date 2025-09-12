# Database Design and ETL Implementation

**Agent: data-engineer**
**Purpose: Design efficient database schemas and implement robust ETL pipelines for data processing**

---

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

---
*Effective data engineering provides the foundation for reliable business operations and data-driven decision making.*