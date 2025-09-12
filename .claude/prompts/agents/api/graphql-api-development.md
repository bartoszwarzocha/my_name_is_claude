# GraphQL API Development

**Agent: api-engineer**
**Purpose: Design and implement efficient GraphQL APIs with advanced features like subscriptions, caching, and federation**

---

## 🎯 Mission

Build scalable GraphQL APIs that provide flexible data fetching capabilities while maintaining performance, security, and maintainability through modern GraphQL practices and tooling.

## 📋 GraphQL Development Process

### Step 1: Schema Design and Architecture

**Schema-First Design Approach:**
```graphql
# schema/user.graphql
"""
User entity representing application users
"""
type User {
  id: ID!
  email: String!
  firstName: String!
  lastName: String!
  fullName: String!  # Computed field
  avatar: String
  role: UserRole!
  isActive: Boolean!
  createdAt: DateTime!
  updatedAt: DateTime!
  
  # Relationships
  orders(
    first: Int = 10
    after: String
    status: OrderStatus
  ): OrderConnection!
  
  preferences: UserPreferences!
  posts(first: Int = 10): PostConnection!
}

"""
User role enumeration
"""
enum UserRole {
  USER
  ADMIN
  MODERATOR
}

"""
User preferences configuration
"""
type UserPreferences {
  theme: Theme!
  notifications: NotificationSettings!
  privacy: PrivacySettings!
}

"""
Connection pattern for pagination
"""
type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  node: User!
  cursor: String!
}

"""
Standard pagination info
"""
type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# schema/mutations.graphql
"""
Root mutation type
"""
type Mutation {
  # User mutations
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
  
  # Authentication mutations
  login(input: LoginInput!): AuthPayload!
  logout: LogoutPayload!
  refreshToken(refreshToken: String!): AuthPayload!
}

"""
Create user input with validation
"""
input CreateUserInput {
  email: String! @validate(format: EMAIL)
  password: String! @validate(minLength: 8, pattern: "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]")
  firstName: String! @validate(minLength: 1, maxLength: 50)
  lastName: String! @validate(minLength: 1, maxLength: 50)
  role: UserRole = USER
}

"""
Standardized mutation payload
"""
type CreateUserPayload {
  user: User
  errors: [UserError!]!
  success: Boolean!
}

type UserError {
  field: String
  message: String!
  code: String!
}

# schema/subscriptions.graphql
"""
Real-time subscriptions
"""
type Subscription {
  # User-related subscriptions
  userUpdated(userId: ID!): User!
  userOnlineStatus(userIds: [ID!]!): UserOnlineStatus!
  
  # Order tracking
  orderStatusChanged(orderId: ID!): Order!
  
  # Notifications
  notificationReceived(userId: ID!): Notification!
}

type UserOnlineStatus {
  userId: ID!
  isOnline: Boolean!
  lastSeen: DateTime
}
```

**Advanced Schema Features:**
```graphql
# schema/directives.graphql
"""
Authentication directive
"""
directive @auth(
  requires: UserRole = USER
) on FIELD_DEFINITION | OBJECT

"""
Rate limiting directive
"""
directive @rateLimit(
  max: Int!
  window: String!
) on FIELD_DEFINITION

"""
Input validation directive
"""
directive @validate(
  format: ValidateFormat
  minLength: Int
  maxLength: Int
  pattern: String
  min: Float
  max: Float
) on INPUT_FIELD_DEFINITION | ARGUMENT_DEFINITION

enum ValidateFormat {
  EMAIL
  URL
  UUID
  PHONE
}

"""
Caching directive for Apollo Federation
"""
directive @cacheControl(
  maxAge: Int
  scope: CacheControlScope
  inheritMaxAge: Boolean
) on FIELD_DEFINITION | OBJECT | INTERFACE | UNION

enum CacheControlScope {
  PUBLIC
  PRIVATE
}

# Usage in schema
type User @cacheControl(maxAge: 300) {
  id: ID!
  email: String! @auth(requires: USER)
  
  # Admin-only field
  internalNotes: String @auth(requires: ADMIN)
  
  # Rate-limited expensive operation
  recommendations: [Product!]! @rateLimit(max: 10, window: "1h")
}

type Query {
  # Public data with caching
  publicPosts: [Post!]! @cacheControl(maxAge: 3600, scope: PUBLIC)
  
  # Private user data
  me: User @auth(requires: USER) @cacheControl(maxAge: 300, scope: PRIVATE)
  
  # Search with rate limiting
  searchUsers(query: String!): [User!]! @rateLimit(max: 100, window: "15m")
}
```

### Step 2: Resolver Implementation

**TypeScript Resolver Architecture:**
```typescript
// resolvers/userResolvers.ts
import { Resolvers, User, CreateUserInput } from '../generated/graphql';
import { Context } from '../context';
import { UserService } from '../services/UserService';
import { AuthenticationError, ValidationError } from '../errors';

export const userResolvers: Resolvers<Context> = {
  Query: {
    me: async (parent, args, context) => {
      if (!context.user) {
        throw new AuthenticationError('Authentication required');
      }
      return context.dataSources.userService.findById(context.user.id);
    },
    
    user: async (parent, { id }, context) => {
      return context.dataSources.userService.findById(id);
    },
    
    users: async (parent, { first, after, filter }, context) => {
      return context.dataSources.userService.findMany({
        first,
        after,
        filter
      });
    }
  },
  
  Mutation: {
    createUser: async (parent, { input }, context) => {
      try {
        // Input validation
        await validateCreateUserInput(input);
        
        // Business logic
        const user = await context.dataSources.userService.create(input);
        
        // Clear relevant caches
        await context.cache.invalidatePattern('users:*');
        
        return {
          user,
          errors: [],
          success: true
        };
      } catch (error) {
        if (error instanceof ValidationError) {
          return {
            user: null,
            errors: error.errors,
            success: false
          };
        }
        throw error;
      }
    },
    
    updateUser: async (parent, { input }, context) => {
      const user = await context.dataSources.userService.update(input);
      
      // Publish subscription update
      context.pubsub.publish('USER_UPDATED', { userUpdated: user });
      
      return {
        user,
        errors: [],
        success: true
      };
    }
  },
  
  Subscription: {
    userUpdated: {
      subscribe: (parent, { userId }, context) => {
        if (!context.user) {
          throw new AuthenticationError('Authentication required for subscriptions');
        }
        
        return context.pubsub.asyncIterator(`USER_UPDATED_${userId}`);
      }
    },
    
    notificationReceived: {
      subscribe: withFilter(
        (parent, args, context) => context.pubsub.asyncIterator('NOTIFICATION_RECEIVED'),
        (payload, variables, context) => {
          // Only send notifications to the intended recipient
          return payload.notificationReceived.userId === context.user?.id;
        }
      )
    }
  },
  
  // Field resolvers
  User: {
    fullName: (parent) => `${parent.firstName} ${parent.lastName}`,
    
    orders: async (parent, args, context) => {
      return context.dataSources.orderService.findByUserId(parent.id, args);
    },
    
    recommendations: async (parent, args, context, info) => {
      // Check cache first
      const cacheKey = `recommendations:${parent.id}`;
      const cached = await context.cache.get(cacheKey);
      
      if (cached) {
        return cached;
      }
      
      // Expensive recommendation calculation
      const recommendations = await context.dataSources.recommendationService
        .generateForUser(parent.id);
      
      // Cache for 1 hour
      await context.cache.set(cacheKey, recommendations, 3600);
      
      return recommendations;
    }
  }
};

// Input validation
const validateCreateUserInput = async (input: CreateUserInput) => {
  const errors: UserError[] = [];
  
  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(input.email)) {
    errors.push({
      field: 'email',
      message: 'Invalid email format',
      code: 'INVALID_EMAIL'
    });
  }
  
  // Password strength validation
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/;
  if (input.password.length < 8 || !passwordRegex.test(input.password)) {
    errors.push({
      field: 'password',
      message: 'Password must be at least 8 characters with uppercase, lowercase, number and special character',
      code: 'WEAK_PASSWORD'
    });
  }
  
  if (errors.length > 0) {
    throw new ValidationError(errors);
  }
};
```

**DataLoader for N+1 Query Prevention:**
```typescript
// dataloaders/userDataLoaders.ts
import DataLoader from 'dataloader';
import { User, Order, Post } from '../types';
import { UserService, OrderService, PostService } from '../services';

export interface DataLoaders {
  userById: DataLoader<string, User>;
  ordersByUserId: DataLoader<string, Order[]>;
  postsByUserId: DataLoader<string, Post[]>;
  usersByIds: DataLoader<string[], User[]>;
}

export const createDataLoaders = (services: {
  userService: UserService;
  orderService: OrderService; 
  postService: PostService;
}): DataLoaders => ({
  // Single user by ID
  userById: new DataLoader(
    async (userIds: readonly string[]) => {
      const users = await services.userService.findByIds(userIds as string[]);
      return userIds.map(id => users.find(user => user.id === id) || null);
    },
    {
      maxBatchSize: 100,
      cacheKeyFn: (key) => key,
      cacheMap: new Map() // Custom cache implementation
    }
  ),
  
  // Orders for multiple users
  ordersByUserId: new DataLoader(
    async (userIds: readonly string[]) => {
      const allOrders = await services.orderService.findByUserIds(userIds as string[]);
      
      // Group orders by user ID
      const ordersByUser = userIds.map(userId => 
        allOrders.filter(order => order.userId === userId)
      );
      
      return ordersByUser;
    },
    {
      maxBatchSize: 50
    }
  ),
  
  // Posts for multiple users  
  postsByUserId: new DataLoader(
    async (userIds: readonly string[]) => {
      const allPosts = await services.postService.findByUserIds(userIds as string[]);
      
      const postsByUser = userIds.map(userId =>
        allPosts.filter(post => post.authorId === userId)
      );
      
      return postsByUser;
    }
  ),
  
  // Batch multiple users at once
  usersByIds: new DataLoader(
    async (userIdArrays: readonly string[][]) => {
      const allUserIds = [...new Set(userIdArrays.flat())];
      const users = await services.userService.findByIds(allUserIds);
      
      return userIdArrays.map(userIds => 
        userIds.map(id => users.find(user => user.id === id)).filter(Boolean)
      );
    }
  )
});
```

### Step 3: Advanced GraphQL Features

**GraphQL Subscriptions with Redis:**
```typescript
// subscriptions/setup.ts
import { RedisPubSub } from 'graphql-redis-subscriptions';
import { withFilter } from 'graphql-subscriptions';
import Redis from 'ioredis';

const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: parseInt(process.env.REDIS_PORT || '6379'),
  retryDelayOnFailover: 100,
  enableReadyCheck: false,
  maxRetriesPerRequest: null,
});

export const pubsub = new RedisPubSub({
  publisher: redis,
  subscriber: redis,
});

// Real-time notifications
export const notificationSubscription = {
  subscribe: withFilter(
    () => pubsub.asyncIterator('NOTIFICATION'),
    (payload, variables, context) => {
      // User-specific filtering
      return payload.notification.recipientId === context.user?.id;
    }
  )
};

// Live order tracking
export const orderTrackingSubscription = {
  subscribe: withFilter(
    () => pubsub.asyncIterator('ORDER_STATUS_CHANGED'),
    async (payload, variables, context) => {
      // Check if user has permission to track this order
      const order = await context.dataSources.orderService.findById(payload.order.id);
      return order && (
        order.customerId === context.user?.id || 
        context.user?.role === 'ADMIN'
      );
    }
  )
};

// Connection state management
export const connectionManager = {
  connections: new Map<string, Set<string>>(),
  
  addConnection(userId: string, connectionId: string) {
    if (!this.connections.has(userId)) {
      this.connections.set(userId, new Set());
    }
    this.connections.get(userId)!.add(connectionId);
    
    // Publish online status
    pubsub.publish('USER_ONLINE_STATUS', {
      userOnlineStatus: {
        userId,
        isOnline: true,
        lastSeen: new Date()
      }
    });
  },
  
  removeConnection(userId: string, connectionId: string) {
    const userConnections = this.connections.get(userId);
    if (userConnections) {
      userConnections.delete(connectionId);
      
      if (userConnections.size === 0) {
        this.connections.delete(userId);
        
        // Publish offline status
        pubsub.publish('USER_ONLINE_STATUS', {
          userOnlineStatus: {
            userId,
            isOnline: false,
            lastSeen: new Date()
          }
        });
      }
    }
  }
};
```

**Query Complexity Analysis:**
```typescript
// middleware/queryComplexity.ts
import { createComplexityLimitRule } from 'graphql-query-complexity';
import { separateOperations } from 'graphql';

const complexityAnalysis = createComplexityLimitRule(1000, {
  // Field complexity calculation
  fieldConfigMap: {
    User: {
      orders: { complexity: 10 }, // Expensive relationship
      posts: { complexity: 5 },
      recommendations: { complexity: 20 } // Very expensive computation
    },
    Query: {
      searchUsers: { 
        complexity: ({ args }) => args.first * 2 // Based on result size
      },
      analytics: { complexity: 50 } // Complex aggregation
    }
  },
  
  // Dynamic complexity calculation
  estimators: [
    simpleEstimator({ 
      defaultComplexity: 1,
      scalarCost: 1,
      objectCost: 2,
      listFactor: 10,
      introspectionCost: 1000
    }),
    
    // Custom estimator for pagination
    (args, childComplexity) => {
      const { first = 10 } = args;
      return childComplexity * Math.min(first, 100);
    }
  ],
  
  // Complexity reporting
  onComplete: (complexity, context) => {
    console.log(`Query complexity: ${complexity}`);
    
    // Log expensive queries
    if (complexity > 500) {
      logger.warn('High complexity query', {
        complexity,
        userId: context.user?.id,
        query: context.request.query
      });
    }
  }
});
```

### Step 4: GraphQL Federation

**Apollo Federation Setup:**
```typescript
// federation/userService.ts
import { buildFederatedSchema } from '@apollo/federation';
import { gql } from 'apollo-server-express';

const typeDefs = gql`
  extend type Query {
    me: User
    user(id: ID!): User
  }
  
  type User @key(fields: "id") {
    id: ID!
    email: String!
    firstName: String!
    lastName: String!
    fullName: String!
    
    # Extended by other services
    orders: [Order!]! @external
    reviews: [Review!]! @external
  }
  
  # Reference types from other services
  extend type Order @key(fields: "id") {
    id: ID! @external
    customer: User! @provides(fields: "id email firstName lastName")
  }
`;

const resolvers = {
  Query: {
    me: (parent, args, context) => context.user,
    user: (parent, { id }, context) => context.dataSources.userService.findById(id)
  },
  
  User: {
    // Federation resolver for external references
    __resolveReference: (reference, context) => {
      return context.dataSources.userService.findById(reference.id);
    },
    
    fullName: (user) => `${user.firstName} ${user.lastName}`
  }
};

export const federatedSchema = buildFederatedSchema([{ typeDefs, resolvers }]);
```

**Gateway Configuration:**
```typescript
// gateway/apollo-gateway.ts
import { ApolloGateway } from '@apollo/gateway';
import { ApolloServer } from 'apollo-server-express';

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'users', url: 'http://user-service:4001/graphql' },
    { name: 'products', url: 'http://product-service:4002/graphql' },
    { name: 'orders', url: 'http://order-service:4003/graphql' },
    { name: 'reviews', url: 'http://review-service:4004/graphql' }
  ],
  
  // Service health checking
  serviceHealthCheck: true,
  
  // Schema composition debugging  
  debug: process.env.NODE_ENV === 'development',
  
  // Custom directive handling
  buildService: ({ url }) => new RemoteGraphQLDataSource({
    url,
    willSendRequest({ request, context }) {
      // Forward authentication
      if (context.auth) {
        request.http?.headers.set('authorization', context.auth);
      }
      
      // Add correlation ID
      request.http?.headers.set('x-correlation-id', context.correlationId);
    }
  })
});

const server = new ApolloServer({
  gateway,
  subscriptions: false, // Handled by individual services
  context: ({ req }) => ({
    auth: req.headers.authorization,
    correlationId: req.headers['x-correlation-id'] || generateId(),
    user: req.user
  }),
  
  // Gateway-level plugins
  plugins: [
    {
      requestDidStart() {
        return {
          willSendSubgraphRequest(requestContext) {
            console.log(`Sending request to ${requestContext.subgraphName}`);
          }
        };
      }
    }
  ]
});
```

## 📊 Performance and Monitoring

### Step 5: Caching and Performance

**Multi-Level Caching Strategy:**
```typescript
// caching/graphqlCache.ts
import { KeyvAdapter } from '@apollo/utils.keyvadapter';
import Keyv from 'keyv';
import KeyvRedis from '@keyv/redis';

// Response cache setup
const responseCache = new Keyv({
  store: new KeyvRedis(process.env.REDIS_URL),
  namespace: 'graphql-response',
  ttl: 1000 * 60 * 15 // 15 minutes default
});

// Field-level caching
export const createFieldCache = () => new Map();

// Cache configuration per field
export const cacheConfig = {
  'Query.me': { ttl: 300, scope: 'PRIVATE' },
  'Query.publicPosts': { ttl: 3600, scope: 'PUBLIC' },
  'User.recommendations': { ttl: 1800, scope: 'PRIVATE' },
  'Product.reviews': { ttl: 600, scope: 'PUBLIC' }
};

// Automatic persisted queries
export const apolloServerConfig = {
  cache: new KeyvAdapter(responseCache),
  
  // Enable APQ
  persistedQueries: {
    cache: new KeyvAdapter(new Keyv({
      store: new KeyvRedis(process.env.REDIS_URL),
      namespace: 'graphql-apq'
    }))
  },
  
  // Response caching plugin
  plugins: [
    require('apollo-server-plugin-response-cache')({
      sessionId: (requestContext) => {
        return requestContext.context.user?.id || null;
      },
      
      // Cache hints from directives
      shouldReadFromCache: (requestContext) => {
        const { operation } = requestContext.request;
        return operation?.operation === 'query';
      },
      
      // Dynamic TTL calculation
      cacheKeyFrom: (requestContext) => {
        const { query, variables, operationName } = requestContext.request;
        return `${operationName}:${hash({ query, variables })}`;
      }
    })
  ]
};
```

**Query Analysis and Monitoring:**
```typescript
// monitoring/graphqlMetrics.ts
import { plugin } from 'apollo-server-core';
import { promisify } from 'util';

export const metricsPlugin = plugin({
  requestDidStart() {
    return {
      didResolveOperation(requestContext) {
        const { operationName, operation } = requestContext.request;
        
        // Track operation metrics
        graphqlOperations.inc({
          operation_name: operationName || 'anonymous',
          operation_type: operation?.operation || 'unknown'
        });
      },
      
      willSendResponse(requestContext) {
        const { response } = requestContext;
        const duration = Date.now() - requestContext.request.startTime;
        
        // Response time histogram
        graphqlDuration.observe(
          {
            operation_name: requestContext.operationName || 'anonymous',
            has_errors: response.errors ? 'true' : 'false'
          },
          duration / 1000
        );
        
        // Error tracking
        if (response.errors) {
          response.errors.forEach(error => {
            graphqlErrors.inc({
              error_type: error.constructor.name,
              error_code: error.extensions?.code || 'UNKNOWN'
            });
          });
        }
        
        // Complexity tracking
        const complexity = requestContext.context.complexity;
        if (complexity) {
          queryComplexity.observe(
            { operation_name: requestContext.operationName },
            complexity
          );
        }
      }
    };
  }
});

// Prometheus metrics
const graphqlOperations = new Counter({
  name: 'graphql_operations_total',
  help: 'Total number of GraphQL operations',
  labelNames: ['operation_name', 'operation_type']
});

const graphqlDuration = new Histogram({
  name: 'graphql_operation_duration_seconds',
  help: 'Duration of GraphQL operations',
  labelNames: ['operation_name', 'has_errors'],
  buckets: [0.01, 0.1, 0.3, 0.5, 1, 3, 5, 10]
});

const queryComplexity = new Histogram({
  name: 'graphql_query_complexity',
  help: 'Complexity score of GraphQL queries', 
  labelNames: ['operation_name'],
  buckets: [1, 5, 10, 25, 50, 100, 250, 500, 1000]
});
```

## 📤 Deliverables

- **GraphQL Schema** with comprehensive type definitions and advanced features
- **Resolver Implementation** with efficient data fetching and N+1 query prevention
- **Subscription System** with real-time capabilities and Redis pub/sub
- **Federation Architecture** with service composition and gateway configuration
- **Caching Strategy** with multi-level caching and automatic persisted queries
- **Performance Monitoring** with metrics collection and query analysis
- **Security Implementation** with authentication, authorization, and query complexity limits

## 🤝 Collaboration Points

**With frontend-engineer:** GraphQL client integration, query optimization, and real-time features
**With data-engineer:** Efficient data fetching patterns, caching strategies, and analytics integration
**With security-engineer:** Authentication middleware, authorization rules, and input validation
**With deployment-engineer:** Federation deployment, monitoring setup, and performance optimization
**With qa-engineer:** GraphQL testing strategies, schema validation, and performance testing

---
*Well-architected GraphQL APIs provide flexible, efficient data access while maintaining performance and security through modern GraphQL practices and tooling.*