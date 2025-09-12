# DATABASE_CONNECTIONS.md

## Usage Instructions

This file contains standardized database connection configurations for Claude Code sessions. 

### Setup:
1. **Copy this file** to your project's root directory as `DATABASE_CONNECTIONS.md`
2. **Alternative**: Copy to `~/.claude/DATABASE_CONNECTIONS.md` for global access across projects
3. **Reference in CLAUDE.md**: Add link to this file in your project's CLAUDE.md for automatic discovery

### Purpose:
- Provides Claude Code with ready-to-use database connection parameters
- Eliminates need to discover connection details during sessions
- Standardizes connection approaches across different projects
- Supports multiple database types and environments

---

## Connection Configurations

### WSL to Windows Host Databases

#### MySQL Connection (XAMPP)
```bash
# Environment Variables
MYSQL_HOST=172.22.176.1    # Windows host IP (auto-detected via: ip route | awk '/default/ {print $3}')
MYSQL_PORT=3307            # XAMPP MySQL port (change port if necessary, here is for host and WSL servers working parallely)
MYSQL_USER=username        # Username
MYSQL_PASSWORD=password    # Password

# Direct Connection Command
mysql -h 172.22.176.1 -P 3307 -u username -ppassword

# Python Connection (pymysql)
import pymysql
connection = pymysql.connect(
    host='172.22.176.1',
    port=3307,
    user='username',
    password='password',
    database='database_name',
    autocommit=True
)

```

#### PostgreSQL Connection (Windows Host)
```bash
# Environment Variables
PGHOST=172.22.176.1        # Windows host IP (check host)
PGPORT=5432                # PostgreSQL standard port
PGUSER=username            # Username
PGPASSWORD=password        # Password

# Direct Connection Commands
PGPASSWORD=password psql -h 172.22.176.1 -U username -d postgres
PGPASSWORD=password psql -h 172.22.176.1 -U username -d cyklop_config

# Using pgw.sh wrapper (recommended)
PGPASSWORD=password ./utils/pgw.sh -U username -d postgres -c "\l"

# Python Connection (psycopg)
import psycopg
connection = psycopg.connect(
    host='172.22.176.1',
    port=5432,
    user='username',
    password='password',
    dbname='database_name',
    autocommit=True
)

```

### Docker Container Connections

#### PostgreSQL Test Container
```bash
# Container Connection
docker run -d --name postgres-test \
  -e POSTGRES_PASSWORD=testpass \
  -p 5433:5432 \
  postgres:17

# Connection Parameters
HOST=localhost
PORT=5433
USER=postgres  
PASSWORD=testpass

# Direct Connection
PGPASSWORD=testpass psql -h localhost -p 5433 -U postgres -d postgres

# Python Connection
connection = psycopg.connect(
    host='localhost',
    port=5433,
    user='postgres',
    password='testpass',
    dbname='database_name',
    autocommit=True
)
```

### Connection Utilities

#### PostgreSQL Wrapper Script (pgw.sh)
```bash
#!/bin/bash
# Auto-detect Windows host IP and connect to PostgreSQL
WINHOST=$(ip route | awk '/default/ {print $3}')
psql -h $WINHOST "$@"

# Usage examples:
# ./pgw.sh -U username -d postgres -c "\l"
# PGPASSWORD=password ./pgw.sh -U username -d database_name -c "SELECT COUNT(*) FROM users"
```

---

## Connection Templates for New Projects

### Template: Local Development
```yaml
database_connections:
  mysql_local:
    host: "localhost"
    port: 3306
    user: "root"
    password: "password"
    databases: ["app_db"]
    
  postgres_local:
    host: "localhost" 
    port: 5432
    user: "postgres"
    password: "password"
    databases: ["app_db"]
```

### Template: WSL to Windows
```yaml
database_connections:
  mysql_windows:
    host: "172.22.176.1"  # Auto-detect: ip route | awk '/default/ {print $3}'
    port: 3307
    user: "wsl"
    password: "Wsl!2345"
    databases: ["database1", "database2"]
    
  postgres_windows:
    host: "172.22.176.1"
    port: 5432  
    user: "taurus"
    password: "taurus"
    databases: ["database1", "database2"]
```

### Template: Docker Environment
```yaml
database_connections:
  postgres_docker:
    host: "localhost"
    port: 5433
    user: "postgres"
    password: "testpass"
    databases: ["test_db"]
    container: "postgres-test"
    image: "postgres:17"
```

---

## Troubleshooting

### Common Issues:

#### WSL IP Detection
```bash
# Get Windows host IP
WINHOST=$(ip route | awk '/default/ {print $3}')
echo $WINHOST  # Should show 172.22.176.1 or similar
```

#### PostgreSQL Permissions
```sql
-- Grant permissions if access denied
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO username;
ALTER TABLE table_name OWNER TO username;
```

#### Connection Testing
```bash
# Test MySQL connection
mysql -h $HOST -P $PORT -u $USER -p$PASSWORD -e "SHOW DATABASES;"

# Test PostgreSQL connection  
PGPASSWORD=$PASSWORD psql -h $HOST -p $PORT -U $USER -d postgres -c "\l"
```

---

## Integration with Claude Code

### In CLAUDE.md, add:
```markdown
## Database Connections
See `DATABASE_CONNECTIONS.md` for complete connection configurations.

Quick access:
- MySQL (XAMPP): `mysql -h 172.22.176.1 -P 3307 -u wsl -pWsl!2345`
- PostgreSQL: `PGPASSWORD=taurus ./utils/pgw.sh -U taurus -d postgres`
- Docker PostgreSQL: `PGPASSWORD=testpass psql -h localhost -p 5433 -U postgres`
```

### For Migration Projects:
```markdown
## Migration Environment
```bash
export MYSQL_HOST=172.22.176.1 MYSQL_PORT=3307 MYSQL_USER=mysql_username MYSQL_PASSWORD=mysql_password
export PGHOST=172.22.176.1 PGPORT=5432 PGUSER=pg_username PGPASSWORD=pg_password
```

This file ensures Claude Code can immediately access database connections without discovery phase.