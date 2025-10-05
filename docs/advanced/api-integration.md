# API Integration Guide

*Integrating My Name Is Claude framework with external APIs and services*

## 🎯 Overview

Comprehensive guide for integrating Claude Code Multi-Agent Framework with external APIs, microservices, and third-party platforms.

---

## 🔌 Common API Integrations

### **1. REST APIs**

```python
import requests
from typing import Dict, Any

class APIIntegration:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def call_endpoint(self, endpoint: str, method: str = "GET", data: Dict = None) -> Any:
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
```

### **2. GraphQL APIs**

```python
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

class GraphQLIntegration:
    def __init__(self, endpoint: str, api_key: str):
        transport = RequestsHTTPTransport(
            url=endpoint,
            headers={"Authorization": f"Bearer {api_key}"}
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def query(self, query_string: str, variables: Dict = None):
        query = gql(query_string)
        return self.client.execute(query, variable_values=variables)
```

### **3. Webhook Receivers**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    """Receive GitHub webhooks"""
    event = request.headers.get('X-GitHub-Event')
    payload = request.json

    # Trigger agent based on event
    if event == 'push':
        trigger_agent('qa-engineer', payload)

    return jsonify({"status": "received"}), 200
```

---

## 🔐 Authentication Patterns

### **API Key Authentication**
```python
headers = {"X-API-Key": os.getenv("API_KEY")}
```

### **OAuth 2.0**
```python
from requests_oauthlib import OAuth2Session

oauth = OAuth2Session(client_id, redirect_uri=callback_url)
authorization_url, state = oauth.authorization_url(authorize_url)
token = oauth.fetch_token(token_url, authorization_response=callback_url)
```

### **JWT Token**
```python
import jwt

token = jwt.encode({"user_id": user_id}, secret_key, algorithm="HS256")
headers = {"Authorization": f"Bearer {token}"}
```

---

## 📊 Rate Limiting & Retry Logic

```python
from ratelimit import limits, sleep_and_retry
from tenacity import retry, stop_after_attempt, wait_exponential

@sleep_and_retry
@limits(calls=100, period=60)  # 100 calls per minute
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def api_call_with_retry(endpoint):
    """API call with rate limiting and retry logic"""
    return requests.get(endpoint)
```

---

## 🔗 Related Documentation

- **[Database Integration](database-integration.md)** - Database connectivity
- **[Enterprise Deployment](enterprise-deployment.md)** - Production API integrations
- **[Performance Optimization](performance-optimization.md)** - API performance tuning

---

**Last Updated:** 2025-10-05 | **Version:** 3.3.0
