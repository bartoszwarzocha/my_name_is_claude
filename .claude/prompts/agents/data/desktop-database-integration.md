# Desktop Database Integration

## Mission
Implement comprehensive database integration for desktop applications, adapting to the database technology and programming language specified in CLAUDE.md. Create robust data access layers, handle migrations, and implement appropriate ORM patterns for desktop application requirements.

## Pre-Implementation Analysis

### Step 1: Project Technology Detection
**CRITICAL: Always analyze CLAUDE.md first to determine the database and application technology:**
```bash
# Read project configuration
cat CLAUDE.md | grep -A 5 "Database\|primary_language\|Desktop"
```

**Technology-specific database analysis:**
```bash
# For SQLite (most common for desktop)
find . -name "*.db" -o -name "*.sqlite*" | head -5
ls -la data/ db/ database/ 2>/dev/null

# For PostgreSQL/MySQL desktop connections
find . -name "*config*" -o -name "*connection*" | grep -i db | head -5
grep -r "postgresql\|mysql\|mariadb" . --include="*.py" --include="*.cpp" --include="*.cs" 2>/dev/null | head -5

# For embedded databases
find . -name "*.mdb" -o -name "*.accdb" -o -name "*.sdf" | head -5

# Check existing database scripts
find . -name "*.sql" -o -name "*migration*" -o -name "*schema*" | head -10
```

### Step 2: Application Technology Analysis
```bash
# Python applications
find . -name "requirements.txt" -o -name "*.py" | head -5
grep -r "sqlite3\|sqlalchemy\|peewee" . --include="*.py" 2>/dev/null | head -3

# C++ applications
find . -name "*.cpp" -o -name "*.h" -o -name "CMakeLists.txt" | head -5
grep -r "sqlite\|mysql\|postgresql" . --include="*.cpp" --include="*.h" 2>/dev/null | head -3

# .NET applications
find . -name "*.csproj" -o -name "*.cs" | head -5
grep -r "Entity.*Framework\|System.Data" . --include="*.cs" 2>/dev/null | head -3

# Java applications
find . -name "*.java" -o -name "pom.xml" | head -5
grep -r "hibernate\|jpa\|jdbc" . --include="*.java" 2>/dev/null | head -3
```

## Technology-Specific Database Integration

**⚠️ IMPORTANT: Select integration approach based on CLAUDE.md database and language specification**

### Python/SQLite Integration

**Use when CLAUDE.md specifies: Python, SQLite, desktop**

```python
# database/connection_manager.py - Database connection management
import sqlite3
import threading
import logging
from contextlib import contextmanager
from typing import Optional, Generator
import os

class DatabaseManager:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, db_path: str = "app_data.db"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.db_path = db_path
                    cls._instance.logger = logging.getLogger(__name__)
                    cls._instance._initialize_database()
        return cls._instance
    
    def _initialize_database(self):
        """Initialize database with schema"""
        try:
            # Ensure database directory exists
            os.makedirs(os.path.dirname(self.db_path) if os.path.dirname(self.db_path) else '.', exist_ok=True)
            
            with self.get_connection() as conn:
                self._create_schema(conn)
                self._apply_migrations(conn)
                
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
            raise
    
    @contextmanager
    def get_connection(self) -> Generator[sqlite3.Connection, None, None]:
        """Context manager for database connections"""
        conn = sqlite3.connect(
            self.db_path,
            timeout=30.0,
            check_same_thread=False
        )
        conn.row_factory = sqlite3.Row  # Enable dict-like access
        conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
        conn.execute("PRAGMA journal_mode = WAL")  # Better concurrency
        
        try:
            yield conn
        except Exception as e:
            conn.rollback()
            self.logger.error(f"Database operation failed: {e}")
            raise
        else:
            conn.commit()
        finally:
            conn.close()
    
    def _create_schema(self, conn: sqlite3.Connection):
        """Create initial database schema"""
        schema_sql = '''
        -- Main entities table
        CREATE TABLE IF NOT EXISTS entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'archived')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            version INTEGER DEFAULT 1
        );
        
        -- Categories table
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT DEFAULT '#FFFFFF',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Many-to-many relationship
        CREATE TABLE IF NOT EXISTS entity_categories (
            entity_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (entity_id, category_id),
            FOREIGN KEY (entity_id) REFERENCES entities(id) ON DELETE CASCADE,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
        
        -- Settings table for application configuration
        CREATE TABLE IF NOT EXISTS app_settings (
            key TEXT PRIMARY KEY,
            value TEXT,
            data_type TEXT DEFAULT 'string',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Audit log table
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_name TEXT NOT NULL,
            record_id INTEGER NOT NULL,
            operation TEXT NOT NULL CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE')),
            old_values TEXT,  -- JSON
            new_values TEXT,  -- JSON
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Indexes for performance
        CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(name);
        CREATE INDEX IF NOT EXISTS idx_entities_status ON entities(status);
        CREATE INDEX IF NOT EXISTS idx_entities_created_at ON entities(created_at);
        CREATE INDEX IF NOT EXISTS idx_categories_name ON categories(name);
        CREATE INDEX IF NOT EXISTS idx_audit_log_table_record ON audit_log(table_name, record_id);
        CREATE INDEX IF NOT EXISTS idx_audit_log_timestamp ON audit_log(timestamp);
        
        -- Triggers for updated_at
        CREATE TRIGGER IF NOT EXISTS tr_entities_updated_at 
        AFTER UPDATE ON entities 
        BEGIN
            UPDATE entities SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
        END;
        
        CREATE TRIGGER IF NOT EXISTS tr_app_settings_updated_at 
        AFTER UPDATE ON app_settings 
        BEGIN
            UPDATE app_settings SET updated_at = CURRENT_TIMESTAMP WHERE key = NEW.key;
        END;
        '''
        
        conn.executescript(schema_sql)
        self.logger.info("Database schema created successfully")
    
    def _apply_migrations(self, conn: sqlite3.Connection):
        """Apply database migrations"""
        # Get current schema version
        try:
            cursor = conn.execute("SELECT value FROM app_settings WHERE key = 'schema_version'")
            current_version = int(cursor.fetchone()[0] if cursor.fetchone() else 0)
        except:
            current_version = 0
        
        migrations = [
            # Migration 1: Add email field to entities
            (1, '''
                ALTER TABLE entities ADD COLUMN email TEXT;
                CREATE INDEX IF NOT EXISTS idx_entities_email ON entities(email);
            '''),
            # Migration 2: Add preferences table
            (2, '''
                CREATE TABLE IF NOT EXISTS user_preferences (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    preference_key TEXT NOT NULL UNIQUE,
                    preference_value TEXT,
                    data_type TEXT DEFAULT 'string',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            '''),
        ]
        
        for version, migration_sql in migrations:
            if current_version < version:
                try:
                    conn.executescript(migration_sql)
                    conn.execute(
                        "INSERT OR REPLACE INTO app_settings (key, value) VALUES (?, ?)",
                        ('schema_version', str(version))
                    )
                    self.logger.info(f"Applied migration version {version}")
                except Exception as e:
                    self.logger.error(f"Migration {version} failed: {e}")
                    raise
    
    def backup_database(self, backup_path: str) -> bool:
        """Create database backup"""
        try:
            with sqlite3.connect(self.db_path) as source:
                with sqlite3.connect(backup_path) as backup:
                    source.backup(backup)
            
            self.logger.info(f"Database backed up to {backup_path}")
            return True
        except Exception as e:
            self.logger.error(f"Backup failed: {e}")
            return False
    
    def vacuum_database(self) -> bool:
        """Optimize database by vacuuming"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("VACUUM")
            
            self.logger.info("Database vacuumed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Vacuum failed: {e}")
            return False
```

```python
# models/base_repository.py - Generic repository pattern
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic, Dict, Any
import json
from datetime import datetime
from database.connection_manager import DatabaseManager

T = TypeVar('T')

class BaseRepository(Generic[T], ABC):
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.table_name = self.get_table_name()
    
    @abstractmethod
    def get_table_name(self) -> str:
        pass
    
    @abstractmethod
    def from_row(self, row: dict) -> T:
        """Convert database row to entity"""
        pass
    
    @abstractmethod
    def to_dict(self, entity: T) -> Dict[str, Any]:
        """Convert entity to dictionary for database storage"""
        pass
    
    def get_by_id(self, entity_id: int) -> Optional[T]:
        """Get entity by ID"""
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute(
                f"SELECT * FROM {self.table_name} WHERE id = ?",
                (entity_id,)
            )
            row = cursor.fetchone()
            return self.from_row(dict(row)) if row else None
    
    def get_all(self, limit: Optional[int] = None, offset: int = 0) -> List[T]:
        """Get all entities with optional pagination"""
        with self.db_manager.get_connection() as conn:
            sql = f"SELECT * FROM {self.table_name} ORDER BY created_at DESC"
            if limit:
                sql += f" LIMIT {limit} OFFSET {offset}"
            
            cursor = conn.execute(sql)
            return [self.from_row(dict(row)) for row in cursor.fetchall()]
    
    def create(self, entity: T) -> Optional[T]:
        """Create new entity"""
        entity_dict = self.to_dict(entity)
        
        # Remove id and auto-generated fields
        entity_dict.pop('id', None)
        entity_dict.pop('created_at', None)
        entity_dict.pop('updated_at', None)
        
        columns = ', '.join(entity_dict.keys())
        placeholders = ', '.join(['?' for _ in entity_dict])
        values = list(entity_dict.values())
        
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute(
                f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})",
                values
            )
            
            # Log audit trail
            self._log_audit(conn, cursor.lastrowid, 'INSERT', None, entity_dict)
            
            return self.get_by_id(cursor.lastrowid)
    
    def update(self, entity_id: int, updates: Dict[str, Any]) -> Optional[T]:
        """Update existing entity"""
        # Get old values for audit
        old_entity = self.get_by_id(entity_id)
        if not old_entity:
            return None
        
        # Remove auto-generated fields
        updates.pop('id', None)
        updates.pop('created_at', None)
        updates.pop('updated_at', None)
        
        if not updates:
            return old_entity
        
        set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [entity_id]
        
        with self.db_manager.get_connection() as conn:
            conn.execute(
                f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?",
                values
            )
            
            # Log audit trail
            old_dict = self.to_dict(old_entity)
            self._log_audit(conn, entity_id, 'UPDATE', old_dict, updates)
            
            return self.get_by_id(entity_id)
    
    def delete(self, entity_id: int) -> bool:
        """Delete entity by ID"""
        old_entity = self.get_by_id(entity_id)
        if not old_entity:
            return False
        
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute(
                f"DELETE FROM {self.table_name} WHERE id = ?",
                (entity_id,)
            )
            
            if cursor.rowcount > 0:
                # Log audit trail
                old_dict = self.to_dict(old_entity)
                self._log_audit(conn, entity_id, 'DELETE', old_dict, None)
                return True
        
        return False
    
    def search(self, search_term: str, columns: List[str] = None) -> List[T]:
        """Search entities by term"""
        if not columns:
            columns = ['name']  # Default search column
        
        conditions = [f"{col} LIKE ?" for col in columns]
        where_clause = " OR ".join(conditions)
        search_values = [f"%{search_term}%" for _ in columns]
        
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute(
                f"SELECT * FROM {self.table_name} WHERE {where_clause} ORDER BY created_at DESC",
                search_values
            )
            return [self.from_row(dict(row)) for row in cursor.fetchall()]
    
    def count(self) -> int:
        """Get total count of entities"""
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute(f"SELECT COUNT(*) FROM {self.table_name}")
            return cursor.fetchone()[0]
    
    def _log_audit(self, conn, record_id: int, operation: str, 
                   old_values: Optional[Dict], new_values: Optional[Dict]):
        """Log audit trail"""
        try:
            conn.execute('''
                INSERT INTO audit_log (table_name, record_id, operation, old_values, new_values)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                self.table_name,
                record_id,
                operation,
                json.dumps(old_values) if old_values else None,
                json.dumps(new_values) if new_values else None
            ))
        except Exception as e:
            # Don't fail the main operation if audit logging fails
            print(f"Audit logging failed: {e}")
```

### C++/SQLite Integration

**Use when CLAUDE.md specifies: C++, SQLite, desktop**

```cpp
// include/database/DatabaseManager.h - C++ SQLite integration
#pragma once
#include <sqlite3.h>
#include <string>
#include <vector>
#include <memory>
#include <functional>
#include <mutex>

struct Entity {
    int id = 0;
    std::string name;
    std::string description;
    std::string status = "active";
    std::string created_at;
    std::string updated_at;
    int version = 1;
};

class DatabaseManager {
public:
    static DatabaseManager& getInstance(const std::string& db_path = "app_data.db");
    ~DatabaseManager();
    
    // Database operations
    bool initialize();
    bool backup(const std::string& backup_path);
    bool vacuum();
    
    // Entity operations
    std::vector<Entity> getAllEntities();
    std::unique_ptr<Entity> getEntityById(int id);
    std::unique_ptr<Entity> createEntity(const Entity& entity);
    bool updateEntity(int id, const Entity& entity);
    bool deleteEntity(int id);
    
    // Search operations
    std::vector<Entity> searchEntities(const std::string& search_term);
    int getEntityCount();
    
    // Transaction support
    class Transaction {
    public:
        Transaction(DatabaseManager& manager);
        ~Transaction();
        void commit();
        void rollback();
        
    private:
        DatabaseManager& manager_;
        bool committed_ = false;
        bool active_ = true;
    };
    
    std::unique_ptr<Transaction> beginTransaction();

private:
    DatabaseManager(const std::string& db_path);
    DatabaseManager(const DatabaseManager&) = delete;
    DatabaseManager& operator=(const DatabaseManager&) = delete;
    
    sqlite3* db_;
    std::string db_path_;
    mutable std::mutex db_mutex_;
    
    bool createSchema();
    bool applyMigrations();
    int getCurrentSchemaVersion();
    void logError(const std::string& message);
    void logAudit(const std::string& table_name, int record_id, 
                  const std::string& operation, const std::string& old_values = "",
                  const std::string& new_values = "");
    
    // Prepared statements for performance
    sqlite3_stmt* stmt_get_all_entities_ = nullptr;
    sqlite3_stmt* stmt_get_entity_by_id_ = nullptr;
    sqlite3_stmt* stmt_insert_entity_ = nullptr;
    sqlite3_stmt* stmt_update_entity_ = nullptr;
    sqlite3_stmt* stmt_delete_entity_ = nullptr;
    
    void prepareFequentStatements();
    void finalizeStatements();
};
```

```cpp
// src/database/DatabaseManager.cpp
#include "database/DatabaseManager.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <filesystem>

DatabaseManager& DatabaseManager::getInstance(const std::string& db_path) {
    static DatabaseManager instance(db_path);
    return instance;
}

DatabaseManager::DatabaseManager(const std::string& db_path) : db_path_(db_path), db_(nullptr) {
    // Constructor
}

DatabaseManager::~DatabaseManager() {
    finalizeStatements();
    if (db_) {
        sqlite3_close(db_);
    }
}

bool DatabaseManager::initialize() {
    std::lock_guard<std::mutex> lock(db_mutex_);
    
    // Create directory if it doesn't exist
    std::filesystem::path db_file(db_path_);
    std::filesystem::create_directories(db_file.parent_path());
    
    int rc = sqlite3_open(db_path_.c_str(), &db_);
    if (rc != SQLITE_OK) {
        logError("Cannot open database: " + std::string(sqlite3_errmsg(db_)));
        return false;
    }
    
    // Configure SQLite
    sqlite3_exec(db_, "PRAGMA foreign_keys = ON", nullptr, nullptr, nullptr);
    sqlite3_exec(db_, "PRAGMA journal_mode = WAL", nullptr, nullptr, nullptr);
    sqlite3_exec(db_, "PRAGMA synchronous = NORMAL", nullptr, nullptr, nullptr);
    sqlite3_exec(db_, "PRAGMA cache_size = 10000", nullptr, nullptr, nullptr);
    sqlite3_exec(db_, "PRAGMA temp_store = memory", nullptr, nullptr, nullptr);
    
    if (!createSchema()) {
        logError("Failed to create database schema");
        return false;
    }
    
    if (!applyMigrations()) {
        logError("Failed to apply database migrations");
        return false;
    }
    
    prepareFequentStatements();
    
    return true;
}

bool DatabaseManager::createSchema() {
    const char* schema_sql = R"(
        -- Main entities table
        CREATE TABLE IF NOT EXISTS entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'archived')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            version INTEGER DEFAULT 1
        );
        
        -- Categories table
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT DEFAULT '#FFFFFF',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Many-to-many relationship
        CREATE TABLE IF NOT EXISTS entity_categories (
            entity_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (entity_id, category_id),
            FOREIGN KEY (entity_id) REFERENCES entities(id) ON DELETE CASCADE,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
        
        -- Settings table
        CREATE TABLE IF NOT EXISTS app_settings (
            key TEXT PRIMARY KEY,
            value TEXT,
            data_type TEXT DEFAULT 'string',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Audit log table
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_name TEXT NOT NULL,
            record_id INTEGER NOT NULL,
            operation TEXT NOT NULL CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE')),
            old_values TEXT,
            new_values TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Indexes
        CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(name);
        CREATE INDEX IF NOT EXISTS idx_entities_status ON entities(status);
        CREATE INDEX IF NOT EXISTS idx_entities_created_at ON entities(created_at);
        
        -- Triggers
        CREATE TRIGGER IF NOT EXISTS tr_entities_updated_at 
        AFTER UPDATE ON entities 
        BEGIN
            UPDATE entities SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
        END;
    )";
    
    char* err_msg = nullptr;
    int rc = sqlite3_exec(db_, schema_sql, nullptr, nullptr, &err_msg);
    if (rc != SQLITE_OK) {
        logError("SQL error in schema creation: " + std::string(err_msg));
        sqlite3_free(err_msg);
        return false;
    }
    
    return true;
}

void DatabaseManager::prepareFequentStatements() {
    // Prepare frequently used statements for better performance
    sqlite3_prepare_v2(db_, 
        "SELECT id, name, description, status, created_at, updated_at, version FROM entities ORDER BY created_at DESC",
        -1, &stmt_get_all_entities_, nullptr);
    
    sqlite3_prepare_v2(db_,
        "SELECT id, name, description, status, created_at, updated_at, version FROM entities WHERE id = ?",
        -1, &stmt_get_entity_by_id_, nullptr);
    
    sqlite3_prepare_v2(db_,
        "INSERT INTO entities (name, description, status) VALUES (?, ?, ?)",
        -1, &stmt_insert_entity_, nullptr);
    
    sqlite3_prepare_v2(db_,
        "UPDATE entities SET name = ?, description = ?, status = ?, version = version + 1 WHERE id = ?",
        -1, &stmt_update_entity_, nullptr);
    
    sqlite3_prepare_v2(db_,
        "DELETE FROM entities WHERE id = ?",
        -1, &stmt_delete_entity_, nullptr);
}

std::vector<Entity> DatabaseManager::getAllEntities() {
    std::lock_guard<std::mutex> lock(db_mutex_);
    std::vector<Entity> entities;
    
    if (!stmt_get_all_entities_) return entities;
    
    sqlite3_reset(stmt_get_all_entities_);
    
    while (sqlite3_step(stmt_get_all_entities_) == SQLITE_ROW) {
        Entity entity;
        entity.id = sqlite3_column_int(stmt_get_all_entities_, 0);
        entity.name = reinterpret_cast<const char*>(sqlite3_column_text(stmt_get_all_entities_, 1));
        
        const char* desc = reinterpret_cast<const char*>(sqlite3_column_text(stmt_get_all_entities_, 2));
        entity.description = desc ? desc : "";
        
        const char* status = reinterpret_cast<const char*>(sqlite3_column_text(stmt_get_all_entities_, 3));
        entity.status = status ? status : "active";
        
        const char* created = reinterpret_cast<const char*>(sqlite3_column_text(stmt_get_all_entities_, 4));
        entity.created_at = created ? created : "";
        
        const char* updated = reinterpret_cast<const char*>(sqlite3_column_text(stmt_get_all_entities_, 5));
        entity.updated_at = updated ? updated : "";
        
        entity.version = sqlite3_column_int(stmt_get_all_entities_, 6);
        
        entities.push_back(entity);
    }
    
    return entities;
}

std::unique_ptr<Entity> DatabaseManager::createEntity(const Entity& entity) {
    std::lock_guard<std::mutex> lock(db_mutex_);
    
    if (!stmt_insert_entity_) return nullptr;
    
    sqlite3_reset(stmt_insert_entity_);
    sqlite3_bind_text(stmt_insert_entity_, 1, entity.name.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt_insert_entity_, 2, entity.description.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt_insert_entity_, 3, entity.status.c_str(), -1, SQLITE_STATIC);
    
    int rc = sqlite3_step(stmt_insert_entity_);
    if (rc == SQLITE_DONE) {
        int new_id = static_cast<int>(sqlite3_last_insert_rowid(db_));
        logAudit("entities", new_id, "INSERT", "", 
                 "name=" + entity.name + ",desc=" + entity.description);
        
        return getEntityById(new_id);
    }
    
    logError("Failed to insert entity: " + std::string(sqlite3_errmsg(db_)));
    return nullptr;
}

DatabaseManager::Transaction::Transaction(DatabaseManager& manager) : manager_(manager) {
    sqlite3_exec(manager_.db_, "BEGIN TRANSACTION", nullptr, nullptr, nullptr);
}

DatabaseManager::Transaction::~Transaction() {
    if (active_ && !committed_) {
        rollback();
    }
}

void DatabaseManager::Transaction::commit() {
    if (active_ && !committed_) {
        sqlite3_exec(manager_.db_, "COMMIT", nullptr, nullptr, nullptr);
        committed_ = true;
        active_ = false;
    }
}

void DatabaseManager::Transaction::rollback() {
    if (active_) {
        sqlite3_exec(manager_.db_, "ROLLBACK", nullptr, nullptr, nullptr);
        active_ = false;
    }
}

std::unique_ptr<DatabaseManager::Transaction> DatabaseManager::beginTransaction() {
    return std::make_unique<Transaction>(*this);
}

void DatabaseManager::logError(const std::string& message) {
    std::cerr << "DatabaseManager Error: " << message << std::endl;
}
```

### .NET Entity Framework Integration

**Use when CLAUDE.md specifies: C#, .NET, Entity Framework**

```csharp
// Data/ApplicationDbContext.cs - Entity Framework context
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using DesktopApp.Models;

namespace DesktopApp.Data
{
    public class ApplicationDbContext : DbContext
    {
        private readonly ILogger<ApplicationDbContext> _logger;

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options, 
                                   ILogger<ApplicationDbContext> logger) : base(options)
        {
            _logger = logger;
        }

        public DbSet<Entity> Entities { get; set; }
        public DbSet<Category> Categories { get; set; }
        public DbSet<AppSetting> AppSettings { get; set; }
        public DbSet<AuditLog> AuditLogs { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Entity configuration
            modelBuilder.Entity<Entity>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.Property(e => e.Name).IsRequired().HasMaxLength(200);
                entity.Property(e => e.Status).HasDefaultValue("active");
                entity.Property(e => e.Version).HasDefaultValue(1);
                entity.Property(e => e.CreatedAt).HasDefaultValueSql("datetime('now')");
                entity.Property(e => e.UpdatedAt).HasDefaultValueSql("datetime('now')");
                
                entity.HasIndex(e => e.Name).IsUnique();
                entity.HasIndex(e => e.Status);
                entity.HasIndex(e => e.CreatedAt);
            });

            // Category configuration
            modelBuilder.Entity<Category>(entity =>
            {
                entity.HasKey(c => c.Id);
                entity.Property(c => c.Name).IsRequired().HasMaxLength(100);
                entity.Property(c => c.Color).HasDefaultValue("#FFFFFF");
                entity.HasIndex(c => c.Name).IsUnique();
            });

            // Many-to-many relationship
            modelBuilder.Entity<Entity>()
                .HasMany(e => e.Categories)
                .WithMany(c => c.Entities)
                .UsingEntity<Dictionary<string, object>>(
                    "EntityCategories",
                    j => j.HasOne<Category>().WithMany().HasForeignKey("CategoryId"),
                    j => j.HasOne<Entity>().WithMany().HasForeignKey("EntityId"),
                    j =>
                    {
                        j.Property<DateTime>("AssignedAt").HasDefaultValueSql("datetime('now')");
                        j.HasKey("EntityId", "CategoryId");
                    });

            // App settings configuration
            modelBuilder.Entity<AppSetting>(entity =>
            {
                entity.HasKey(s => s.Key);
                entity.Property(s => s.DataType).HasDefaultValue("string");
                entity.Property(s => s.UpdatedAt).HasDefaultValueSql("datetime('now')");
            });

            // Audit log configuration
            modelBuilder.Entity<AuditLog>(entity =>
            {
                entity.HasKey(a => a.Id);
                entity.Property(a => a.TableName).IsRequired().HasMaxLength(50);
                entity.Property(a => a.Operation).IsRequired();
                entity.Property(a => a.Timestamp).HasDefaultValueSql("datetime('now')");
                
                entity.HasIndex(a => new { a.TableName, a.RecordId });
                entity.HasIndex(a => a.Timestamp);
            });

            // Seed default data
            SeedData(modelBuilder);
        }

        private static void SeedData(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<AppSetting>().HasData(
                new AppSetting { Key = "schema_version", Value = "1", DataType = "integer" },
                new AppSetting { Key = "app_initialized", Value = "true", DataType = "boolean" }
            );

            modelBuilder.Entity<Category>().HasData(
                new Category { Id = 1, Name = "General", Color = "#007ACC" },
                new Category { Id = 2, Name = "Important", Color = "#FF6B35" }
            );
        }

        public override int SaveChanges()
        {
            AddAuditLogs();
            return base.SaveChanges();
        }

        public override async Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
        {
            AddAuditLogs();
            return await base.SaveChangesAsync(cancellationToken);
        }

        private void AddAuditLogs()
        {
            var auditEntries = new List<AuditLog>();
            
            foreach (var entry in ChangeTracker.Entries())
            {
                if (entry.Entity is AuditLog || entry.State == EntityState.Unchanged)
                    continue;

                var auditLog = new AuditLog
                {
                    TableName = entry.Entity.GetType().Name,
                    RecordId = GetPrimaryKeyValue(entry),
                    Operation = entry.State.ToString().ToUpper(),
                    Timestamp = DateTime.UtcNow
                };

                if (entry.State == EntityState.Modified)
                {
                    auditLog.OldValues = GetOriginalValues(entry);
                    auditLog.NewValues = GetCurrentValues(entry);
                }
                else if (entry.State == EntityState.Added)
                {
                    auditLog.NewValues = GetCurrentValues(entry);
                }
                else if (entry.State == EntityState.Deleted)
                {
                    auditLog.OldValues = GetOriginalValues(entry);
                }

                auditEntries.Add(auditLog);
            }

            AuditLogs.AddRange(auditEntries);
        }

        private int GetPrimaryKeyValue(EntityEntry entry)
        {
            var keyProperty = entry.Properties.FirstOrDefault(p => p.Metadata.IsPrimaryKey());
            return keyProperty?.CurrentValue as int? ?? 0;
        }

        private string GetOriginalValues(EntityEntry entry)
        {
            var values = new Dictionary<string, object>();
            foreach (var property in entry.Properties)
            {
                values[property.Metadata.Name] = property.OriginalValue;
            }
            return System.Text.Json.JsonSerializer.Serialize(values);
        }

        private string GetCurrentValues(EntityEntry entry)
        {
            var values = new Dictionary<string, object>();
            foreach (var property in entry.Properties)
            {
                values[property.Metadata.Name] = property.CurrentValue;
            }
            return System.Text.Json.JsonSerializer.Serialize(values);
        }
    }
}
```

## Quality Gates

### ✅ Database Integration
- [ ] Database technology matches CLAUDE.md specification
- [ ] Connection management properly implemented
- [ ] Migration system in place
- [ ] Error handling and logging configured

### ✅ Data Access Layer
- [ ] Repository pattern implemented where appropriate
- [ ] ORM configuration correct for technology stack
- [ ] Audit logging implemented
- [ ] Transaction support available

### ✅ Performance & Reliability
- [ ] Database indexes created for performance
- [ ] Connection pooling configured appropriately
- [ ] Backup and maintenance procedures defined
- [ ] Concurrency handling implemented

**This prompt ensures database integration follows best practices for the specific technology stack defined in CLAUDE.md, providing robust data access for desktop applications.**