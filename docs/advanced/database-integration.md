# Database Integration Guide

*Integrating My Name Is Claude framework with databases and data persistence layers*

## 🎯 Overview

Complete guide for database connectivity, session persistence, and data management in Claude Code Multi-Agent Framework.

---

## 🗄️ Supported Databases

### **1. PostgreSQL**

```python
import psycopg2
from psycopg2.extras import RealDictCursor

class PostgreSQLConnection:
    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string, cursor_factory=RealDictCursor)

    def execute_query(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def save_session(self, session_data):
        query = """
            INSERT INTO sessions (id, data, created_at)
            VALUES (%(id)s, %(data)s, NOW())
            ON CONFLICT (id) DO UPDATE SET data = %(data)s
        """
        self.execute_query(query, session_data)
```

### **2. MongoDB**

```python
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, connection_string, database):
        self.client = MongoClient(connection_string)
        self.db = self.client[database]

    def save_checkpoint(self, checkpoint_data):
        collection = self.db.checkpoints
        return collection.insert_one(checkpoint_data)

    def load_latest_checkpoint(self, project_id):
        collection = self.db.checkpoints
        return collection.find_one(
            {"project_id": project_id},
            sort=[("created_at", -1)]
        )
```

### **3. Redis (Caching)**

```python
import redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def cache_agent_config(self, agent_name, config, ttl=3600):
        """Cache agent configuration for fast access"""
        key = f"agent:{agent_name}"
        self.client.setex(key, ttl, json.dumps(config))

    def get_agent_config(self, agent_name):
        key = f"agent:{agent_name}"
        data = self.client.get(key)
        return json.loads(data) if data else None
```

---

## 💾 Session Persistence

### **Database Schema**

```sql
-- PostgreSQL session storage
CREATE TABLE sessions (
    id VARCHAR(255) PRIMARY KEY,
    project_id VARCHAR(255) NOT NULL,
    data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_project_created (project_id, created_at DESC)
);

-- Checkpoints table
CREATE TABLE checkpoints (
    id VARCHAR(255) PRIMARY KEY,
    session_id VARCHAR(255) REFERENCES sessions(id),
    type VARCHAR(50) NOT NULL,
    data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_session_created (session_id, created_at DESC)
);
```

### **ORM Integration (SQLAlchemy)**

```python
from sqlalchemy import create_engine, Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(String(255), primary_key=True)
    project_id = Column(String(255), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Usage
engine = create_engine('postgresql://user:pass@localhost/framework_db')
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Save session
new_session = Session(id='abc123', project_id='project-1', data=session_data)
db.add(new_session)
db.commit()
```

---

## 📊 Query Optimization

```python
# Use connection pooling
from sqlalchemy.pool import QueuePool

engine = create_engine(
    'postgresql://user:pass@localhost/framework_db',
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40
)

# Batch operations
def save_checkpoints_batch(checkpoints):
    db.bulk_insert_mappings(Checkpoint, checkpoints)
    db.commit()

# Indexed queries
db.query(Session).filter(
    Session.project_id == 'project-1'
).order_by(Session.created_at.desc()).limit(10).all()
```

---

## 🔗 Related Documentation

- **[API Integration](api-integration.md)** - External API connectivity
- **[Enterprise Deployment](enterprise-deployment.md)** - Production database setup
- **[Performance Optimization](performance-optimization.md)** - Database performance tuning

---

**Last Updated:** 2025-10-05 | **Version:** 3.3.0
