# Modern JavaScript and TypeScript Development

**Agent Type: frontend-engineer**
**Complexity Level: Expert**
**Estimated Duration: 6-12 hours**

---

## 🎯 Mission

Develop high-performance, type-safe frontend applications using modern JavaScript and TypeScript features, advanced language patterns, and cutting-edge development tools to create scalable, maintainable, and robust web applications.

## 📋 Process Framework

### Phase 1: Advanced TypeScript Implementation (2-4 hours)

**Step 1.1: Advanced Type System Design**

```typescript
// Advanced TypeScript Type System
// File: src/types/advanced-types.ts

// Utility Types for Complex Data Transformations
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type DeepRequired<T> = {
  [P in keyof T]-?: T[P] extends object ? DeepRequired<T[P]> : T[P];
};

type NonNullable<T> = T extends null | undefined ? never : T;

type Flatten<T> = T extends (infer U)[] ? U : T;

type UnionToIntersection<U> = (
  U extends any ? (k: U) => void : never
) extends (k: infer I) => void
  ? I
  : never;

// Advanced Conditional Types
type IsArray<T> = T extends any[] ? true : false;
type IsFunction<T> = T extends (...args: any[]) => any ? true : false;
type IsPromise<T> = T extends Promise<any> ? true : false;

// Template Literal Types for API Endpoints
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
type ApiVersion = 'v1' | 'v2' | 'v3';
type EntityType = 'users' | 'products' | 'orders' | 'categories';

type ApiEndpoint<
  Version extends ApiVersion = 'v1',
  Entity extends EntityType = EntityType,
  ID extends string | number = string | number
> = `/api/${Version}/${Entity}` | `/api/${Version}/${Entity}/${ID}`;

// Example usage: '/api/v1/users' | '/api/v1/users/123'
type UserEndpoints = ApiEndpoint<'v1', 'users'>;

// Advanced Mapped Types
type EventHandlers<T extends Record<string, any>> = {
  [K in keyof T as `on${Capitalize<string & K>}`]?: (value: T[K]) => void;
};

// Example: { onName?: (value: string) => void; onAge?: (value: number) => void; }
type PersonHandlers = EventHandlers<{ name: string; age: number }>;

// Recursive Type for Nested Objects
type NestedKeyOf<ObjectType extends object> = {
  [Key in keyof ObjectType & (string | number)]: ObjectType[Key] extends object
    ? `${Key}` | `${Key}.${NestedKeyOf<ObjectType[Key]>}`
    : `${Key}`;
}[keyof ObjectType & (string | number)];

interface UserProfile {
  user: {
    personal: {
      name: string;
      email: string;
    };
    preferences: {
      theme: 'light' | 'dark';
      notifications: boolean;
    };
  };
}

// Result: "user" | "user.personal" | "user.personal.name" | "user.personal.email" | ...
type UserProfileKeys = NestedKeyOf<UserProfile>;

// Advanced Generic Constraints
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

// Advanced Function Overloads with Generics
interface Repository<T> {
  find<K extends keyof T>(id: T[K]): Promise<T | null>;
  find<K extends keyof T>(query: Partial<Pick<T, K>>): Promise<T[]>;
  find<K extends keyof T>(
    idOrQuery: T[K] | Partial<Pick<T, K>>
  ): Promise<T | T[] | null>;
}

// Brand Types for Type Safety
type Brand<K, T> = K & { __brand: T };
type UserId = Brand<string, 'UserId'>;
type ProductId = Brand<string, 'ProductId'>;
type OrderId = Brand<string, 'OrderId'>;

function createUserId(id: string): UserId {
  // Validation logic here
  return id as UserId;
}

function getUserById(userId: UserId): Promise<User> {
  // This ensures we can't accidentally pass a ProductId
  return fetchUser(userId);
}

// Advanced Class Decorators and Metadata
function Serializable<T extends new (...args: any[]) => {}>(constructor: T) {
  return class extends constructor {
    serialize(): string {
      return JSON.stringify(this);
    }
    
    static deserialize<U>(this: new (...args: any[]) => U, data: string): U {
      const obj = JSON.parse(data);
      return Object.assign(new this(), obj);
    }
  };
}

function Validate(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  
  descriptor.value = function (...args: any[]) {
    // Validation logic
    const metadata = Reflect.getMetadata('validation', target, propertyKey);
    if (metadata) {
      // Perform validation based on metadata
    }
    return originalMethod.apply(this, args);
  };
  
  return descriptor;
}

@Serializable
class User {
  constructor(
    public id: UserId,
    public name: string,
    public email: string
  ) {}
  
  @Validate
  updateEmail(email: string) {
    this.email = email;
  }
}

// Advanced Type Guards
interface Dog {
  type: 'dog';
  breed: string;
  bark(): void;
}

interface Cat {
  type: 'cat';
  color: string;
  meow(): void;
}

type Animal = Dog | Cat;

// Type predicate functions
function isDog(animal: Animal): animal is Dog {
  return animal.type === 'dog';
}

function isCat(animal: Animal): animal is Cat {
  return animal.type === 'cat';
}

// Advanced type narrowing
function handleAnimal(animal: Animal) {
  if (isDog(animal)) {
    // TypeScript knows this is a Dog
    animal.bark();
    console.log(`This dog is a ${animal.breed}`);
  } else {
    // TypeScript knows this is a Cat
    animal.meow();
    console.log(`This cat is ${animal.color}`);
  }
}

// Assertion Functions
function assertIsNumber(value: unknown): asserts value is number {
  if (typeof value !== 'number') {
    throw new Error('Expected number');
  }
}

function processValue(value: unknown) {
  assertIsNumber(value);
  // TypeScript knows value is a number here
  return value * 2;
}

// Advanced Module Declaration
declare global {
  interface Window {
    gtag: (command: string, targetId: string, config?: any) => void;
  }
  
  namespace JSX {
    interface IntrinsicElements {
      'custom-element': {
        'data-value': string;
        onClick?: () => void;
      };
    }
  }
}

// Module Augmentation
declare module 'existing-library' {
  interface ExistingInterface {
    newMethod(): string;
  }
}
```

**Step 1.2: Advanced Language Features and Patterns**

```typescript
// Advanced JavaScript Patterns and Modern Features
// File: src/utils/advanced-patterns.ts

// Advanced Async Patterns
class AsyncQueue<T> {
  private queue: Array<() => Promise<T>> = [];
  private running = 0;
  
  constructor(private concurrency = 3) {}
  
  async add<R extends T>(task: () => Promise<R>): Promise<R> {
    return new Promise<R>((resolve, reject) => {
      this.queue.push(async () => {
        try {
          const result = await task();
          resolve(result);
          return result;
        } catch (error) {
          reject(error);
          throw error;
        }
      });
      
      this.process();
    });
  }
  
  private async process() {
    if (this.running >= this.concurrency || this.queue.length === 0) {
      return;
    }
    
    this.running++;
    const task = this.queue.shift()!;
    
    try {
      await task();
    } finally {
      this.running--;
      this.process();
    }
  }
}

// Advanced Promise Utilities
class PromiseUtils {
  static async timeout<T>(
    promise: Promise<T>,
    ms: number,
    timeoutMessage = 'Promise timed out'
  ): Promise<T> {
    const timeoutPromise = new Promise<never>((_, reject) => {
      setTimeout(() => reject(new Error(timeoutMessage)), ms);
    });
    
    return Promise.race([promise, timeoutPromise]);
  }
  
  static async retry<T>(
    fn: () => Promise<T>,
    attempts = 3,
    delay = 1000,
    backoff = 2
  ): Promise<T> {
    try {
      return await fn();
    } catch (error) {
      if (attempts <= 1) throw error;
      
      await new Promise(resolve => setTimeout(resolve, delay));
      return this.retry(fn, attempts - 1, delay * backoff, backoff);
    }
  }
  
  static async allSettledWithLimit<T>(
    promises: Promise<T>[],
    limit = 5
  ): Promise<PromiseSettledResult<T>[]> {
    const results: PromiseSettledResult<T>[] = [];
    const executing: Promise<any>[] = [];
    
    for (const promise of promises) {
      const p = promise.then(
        value => ({ status: 'fulfilled' as const, value }),
        reason => ({ status: 'rejected' as const, reason })
      ).then(result => {
        results.push(result);
        executing.splice(executing.indexOf(p), 1);
      });
      
      executing.push(p);
      
      if (executing.length >= limit) {
        await Promise.race(executing);
      }
    }
    
    await Promise.all(executing);
    return results;
  }
}

// Advanced Observable Pattern
class Observable<T> {
  private observers: Array<(value: T) => void> = [];
  
  subscribe(observer: (value: T) => void): () => void {
    this.observers.push(observer);
    
    return () => {
      const index = this.observers.indexOf(observer);
      if (index > -1) {
        this.observers.splice(index, 1);
      }
    };
  }
  
  notify(value: T): void {
    this.observers.forEach(observer => observer(value));
  }
  
  map<U>(transform: (value: T) => U): Observable<U> {
    const mapped = new Observable<U>();
    
    this.subscribe(value => {
      mapped.notify(transform(value));
    });
    
    return mapped;
  }
  
  filter(predicate: (value: T) => boolean): Observable<T> {
    const filtered = new Observable<T>();
    
    this.subscribe(value => {
      if (predicate(value)) {
        filtered.notify(value);
      }
    });
    
    return filtered;
  }
  
  static fromEvent<K extends keyof HTMLElementEventMap>(
    element: HTMLElement,
    eventType: K
  ): Observable<HTMLElementEventMap[K]> {
    const observable = new Observable<HTMLElementEventMap[K]>();
    
    element.addEventListener(eventType, (event) => {
      observable.notify(event);
    });
    
    return observable;
  }
}

// Advanced State Management Pattern
class StateManager<T extends Record<string, any>> {
  private state: T;
  private listeners: Set<(state: T, prevState: T) => void> = new Set();
  private middleware: Array<(action: any, state: T) => any> = [];
  
  constructor(initialState: T) {
    this.state = { ...initialState };
  }
  
  getState(): Readonly<T> {
    return { ...this.state };
  }
  
  setState(updater: Partial<T> | ((prevState: T) => Partial<T>)): void {
    const prevState = { ...this.state };
    const updates = typeof updater === 'function' ? updater(prevState) : updater;
    
    this.state = { ...this.state, ...updates };
    
    this.listeners.forEach(listener => {
      listener(this.state, prevState);
    });
  }
  
  subscribe(listener: (state: T, prevState: T) => void): () => void {
    this.listeners.add(listener);
    
    return () => {
      this.listeners.delete(listener);
    };
  }
  
  use(middleware: (action: any, state: T) => any): void {
    this.middleware.push(middleware);
  }
  
  dispatch(action: any): void {
    const processedAction = this.middleware.reduce(
      (acc, middleware) => middleware(acc, this.state),
      action
    );
    
    this.handleAction(processedAction);
  }
  
  private handleAction(action: any): void {
    // Custom action handling logic
    switch (action.type) {
      case 'UPDATE':
        this.setState(action.payload);
        break;
      case 'RESET':
        this.setState(action.initialState);
        break;
    }
  }
}

// Advanced Memoization with LRU Cache
class LRUCache<K, V> {
  private cache = new Map<K, V>();
  private maxSize: number;
  
  constructor(maxSize = 100) {
    this.maxSize = maxSize;
  }
  
  get(key: K): V | undefined {
    if (this.cache.has(key)) {
      // Move to end (most recently used)
      const value = this.cache.get(key)!;
      this.cache.delete(key);
      this.cache.set(key, value);
      return value;
    }
    
    return undefined;
  }
  
  set(key: K, value: V): void {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.maxSize) {
      // Remove least recently used (first item)
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    
    this.cache.set(key, value);
  }
  
  clear(): void {
    this.cache.clear();
  }
  
  size(): number {
    return this.cache.size;
  }
}

function memoizeWithLRU<Args extends any[], Return>(
  fn: (...args: Args) => Return,
  maxSize = 100,
  keySelector: (...args: Args) => string = (...args) => JSON.stringify(args)
): (...args: Args) => Return {
  const cache = new LRUCache<string, Return>(maxSize);
  
  return (...args: Args): Return => {
    const key = keySelector(...args);
    const cached = cache.get(key);
    
    if (cached !== undefined) {
      return cached;
    }
    
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

// Advanced Event System with Type Safety
interface EventMap {
  'user:login': { userId: string; timestamp: Date };
  'user:logout': { userId: string; reason: string };
  'data:update': { entity: string; data: any };
  'error': { message: string; stack?: string };
}

class TypedEventEmitter<T extends Record<string, any> = EventMap> {
  private events = new Map<keyof T, Set<(data: any) => void>>();
  
  on<K extends keyof T>(event: K, listener: (data: T[K]) => void): () => void {
    if (!this.events.has(event)) {
      this.events.set(event, new Set());
    }
    
    const listeners = this.events.get(event)!;
    listeners.add(listener);
    
    return () => {
      listeners.delete(listener);
      if (listeners.size === 0) {
        this.events.delete(event);
      }
    };
  }
  
  emit<K extends keyof T>(event: K, data: T[K]): void {
    const listeners = this.events.get(event);
    if (listeners) {
      listeners.forEach(listener => listener(data));
    }
  }
  
  once<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    const unsubscribe = this.on(event, (data) => {
      listener(data);
      unsubscribe();
    });
  }
  
  removeAllListeners<K extends keyof T>(event?: K): void {
    if (event) {
      this.events.delete(event);
    } else {
      this.events.clear();
    }
  }
}

// Advanced Decorator Patterns
function debounce(delay: number) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    let timeout: NodeJS.Timeout;
    const originalMethod = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        originalMethod.apply(this, args);
      }, delay);
    };
    
    return descriptor;
  };
}

function throttle(limit: number) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    let inThrottle: boolean;
    const originalMethod = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
      if (!inThrottle) {
        originalMethod.apply(this, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
    
    return descriptor;
  };
}

function measure(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  
  descriptor.value = function (...args: any[]) {
    const start = performance.now();
    const result = originalMethod.apply(this, args);
    const end = performance.now();
    
    console.log(`${target.constructor.name}.${propertyKey} took ${end - start}ms`);
    return result;
  };
  
  return descriptor;
}

// Usage examples
class SearchComponent {
  @debounce(300)
  handleSearch(query: string) {
    console.log('Searching for:', query);
  }
  
  @throttle(1000)
  handleScroll(event: Event) {
    console.log('Scroll event:', event);
  }
  
  @measure
  expensiveCalculation(data: number[]) {
    return data.reduce((sum, n) => sum + n * n, 0);
  }
}
```

### Phase 2: Modern JavaScript Features and APIs (2-3 hours)

**Step 2.1: Advanced Web APIs and Browser Features**

```typescript
// Modern Web APIs Implementation
// File: src/utils/web-apis.ts

// Intersection Observer API for Advanced Lazy Loading
class LazyLoader {
  private observer: IntersectionObserver;
  private elementsMap = new WeakMap<Element, () => void>();
  
  constructor(
    private options: IntersectionObserverInit = {
      root: null,
      rootMargin: '50px',
      threshold: 0.1
    }
  ) {
    this.observer = new IntersectionObserver(
      this.handleIntersection.bind(this),
      options
    );
  }
  
  observe(element: Element, callback: () => void): void {
    this.elementsMap.set(element, callback);
    this.observer.observe(element);
  }
  
  unobserve(element: Element): void {
    this.elementsMap.delete(element);
    this.observer.unobserve(element);
  }
  
  private handleIntersection(entries: IntersectionObserverEntry[]): void {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const callback = this.elementsMap.get(entry.target);
        if (callback) {
          callback();
          this.unobserve(entry.target);
        }
      }
    });
  }
  
  disconnect(): void {
    this.observer.disconnect();
  }
}

// Advanced Service Worker Management
class ServiceWorkerManager {
  private registration: ServiceWorkerRegistration | null = null;
  
  async register(
    scriptURL: string,
    options?: RegistrationOptions
  ): Promise<ServiceWorkerRegistration> {
    if (!('serviceWorker' in navigator)) {
      throw new Error('Service Workers not supported');
    }
    
    try {
      this.registration = await navigator.serviceWorker.register(scriptURL, options);
      
      this.registration.addEventListener('updatefound', () => {
        const newWorker = this.registration!.installing;
        if (newWorker) {
          newWorker.addEventListener('statechange', () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
              this.notifyUpdate();
            }
          });
        }
      });
      
      return this.registration;
    } catch (error) {
      console.error('Service Worker registration failed:', error);
      throw error;
    }
  }
  
  async update(): Promise<ServiceWorkerRegistration | undefined> {
    if (this.registration) {
      return this.registration.update();
    }
  }
  
  async unregister(): Promise<boolean> {
    if (this.registration) {
      return this.registration.unregister();
    }
    return false;
  }
  
  private notifyUpdate(): void {
    if (confirm('A new version is available. Reload to update?')) {
      window.location.reload();
    }
  }
  
  // Background Sync
  async requestBackgroundSync(tag: string): Promise<void> {
    if ('serviceWorker' in navigator && 'sync' in window.ServiceWorkerRegistration.prototype) {
      const registration = await navigator.serviceWorker.ready;
      await registration.sync.register(tag);
    }
  }
  
  // Push Notifications
  async subscribeToPushNotifications(): Promise<PushSubscription | null> {
    if (!this.registration) {
      throw new Error('Service Worker not registered');
    }
    
    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
      return null;
    }
    
    const vapidPublicKey = process.env.REACT_APP_VAPID_PUBLIC_KEY;
    if (!vapidPublicKey) {
      throw new Error('VAPID public key not configured');
    }
    
    return this.registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: this.urlBase64ToUint8Array(vapidPublicKey)
    });
  }
  
  private urlBase64ToUint8Array(base64String: string): Uint8Array {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    
    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    
    return outputArray;
  }
}

// Web Storage API with Type Safety and Encryption
class SecureStorage<T extends Record<string, any>> {
  private storage: Storage;
  private encryptionKey?: CryptoKey;
  
  constructor(
    type: 'localStorage' | 'sessionStorage' = 'localStorage',
    private namespace = 'app'
  ) {
    this.storage = type === 'localStorage' ? localStorage : sessionStorage;
  }
  
  async initializeEncryption(password: string): Promise<void> {
    const encoder = new TextEncoder();
    const keyMaterial = await crypto.subtle.importKey(
      'raw',
      encoder.encode(password),
      'PBKDF2',
      false,
      ['deriveBits', 'deriveKey']
    );
    
    this.encryptionKey = await crypto.subtle.deriveKey(
      {
        name: 'PBKDF2',
        salt: encoder.encode('salt'), // In production, use a random salt
        iterations: 100000,
        hash: 'SHA-256'
      },
      keyMaterial,
      { name: 'AES-GCM', length: 256 },
      true,
      ['encrypt', 'decrypt']
    );
  }
  
  async set<K extends keyof T>(key: K, value: T[K]): Promise<void> {
    const serialized = JSON.stringify(value);
    const storageKey = `${this.namespace}:${String(key)}`;
    
    if (this.encryptionKey) {
      const encrypted = await this.encrypt(serialized);
      this.storage.setItem(storageKey, encrypted);
    } else {
      this.storage.setItem(storageKey, serialized);
    }
  }
  
  async get<K extends keyof T>(key: K): Promise<T[K] | null> {
    const storageKey = `${this.namespace}:${String(key)}`;
    const stored = this.storage.getItem(storageKey);
    
    if (!stored) return null;
    
    try {
      let data = stored;
      
      if (this.encryptionKey) {
        data = await this.decrypt(stored);
      }
      
      return JSON.parse(data);
    } catch (error) {
      console.error('Failed to parse stored data:', error);
      return null;
    }
  }
  
  remove<K extends keyof T>(key: K): void {
    const storageKey = `${this.namespace}:${String(key)}`;
    this.storage.removeItem(storageKey);
  }
  
  clear(): void {
    const keys = Object.keys(this.storage);
    keys.forEach(key => {
      if (key.startsWith(`${this.namespace}:`)) {
        this.storage.removeItem(key);
      }
    });
  }
  
  private async encrypt(text: string): Promise<string> {
    if (!this.encryptionKey) throw new Error('Encryption key not initialized');
    
    const encoder = new TextEncoder();
    const data = encoder.encode(text);
    const iv = crypto.getRandomValues(new Uint8Array(12));
    
    const encrypted = await crypto.subtle.encrypt(
      { name: 'AES-GCM', iv },
      this.encryptionKey,
      data
    );
    
    const result = new Uint8Array(iv.length + encrypted.byteLength);
    result.set(iv);
    result.set(new Uint8Array(encrypted), iv.length);
    
    return btoa(String.fromCharCode.apply(null, Array.from(result)));
  }
  
  private async decrypt(encryptedData: string): Promise<string> {
    if (!this.encryptionKey) throw new Error('Encryption key not initialized');
    
    const data = new Uint8Array(
      atob(encryptedData).split('').map(char => char.charCodeAt(0))
    );
    
    const iv = data.slice(0, 12);
    const encrypted = data.slice(12);
    
    const decrypted = await crypto.subtle.decrypt(
      { name: 'AES-GCM', iv },
      this.encryptionKey,
      encrypted
    );
    
    return new TextDecoder().decode(decrypted);
  }
}

// Web Workers with TypeScript Support
interface WorkerMessage<T = any> {
  id: string;
  type: string;
  payload: T;
}

interface WorkerResponse<T = any> {
  id: string;
  success: boolean;
  data?: T;
  error?: string;
}

class TypedWorker {
  private worker: Worker;
  private pendingTasks = new Map<string, {
    resolve: (value: any) => void;
    reject: (reason: any) => void;
  }>();
  
  constructor(workerScript: string | URL) {
    this.worker = new Worker(workerScript);
    this.worker.addEventListener('message', this.handleMessage.bind(this));
    this.worker.addEventListener('error', this.handleError.bind(this));
  }
  
  async execute<T = any, R = any>(
    type: string,
    payload: T,
    transferables?: Transferable[]
  ): Promise<R> {
    const id = crypto.randomUUID();
    
    return new Promise<R>((resolve, reject) => {
      this.pendingTasks.set(id, { resolve, reject });
      
      const message: WorkerMessage<T> = { id, type, payload };
      this.worker.postMessage(message, transferables);
    });
  }
  
  private handleMessage(event: MessageEvent<WorkerResponse>) {
    const { id, success, data, error } = event.data;
    const task = this.pendingTasks.get(id);
    
    if (task) {
      this.pendingTasks.delete(id);
      
      if (success) {
        task.resolve(data);
      } else {
        task.reject(new Error(error));
      }
    }
  }
  
  private handleError(error: ErrorEvent) {
    console.error('Worker error:', error);
    // Reject all pending tasks
    this.pendingTasks.forEach(({ reject }) => {
      reject(new Error('Worker error'));
    });
    this.pendingTasks.clear();
  }
  
  terminate(): void {
    this.worker.terminate();
    this.pendingTasks.clear();
  }
}

// WebRTC Implementation for Real-time Communication
class WebRTCManager {
  private peerConnection: RTCPeerConnection;
  private localStream: MediaStream | null = null;
  private dataChannel: RTCDataChannel | null = null;
  
  constructor(
    private config: RTCConfiguration = {
      iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
    }
  ) {
    this.peerConnection = new RTCPeerConnection(config);
    this.setupEventHandlers();
  }
  
  private setupEventHandlers(): void {
    this.peerConnection.addEventListener('icecandidate', (event) => {
      if (event.candidate) {
        // Send ICE candidate to remote peer
        this.onIceCandidate?.(event.candidate);
      }
    });
    
    this.peerConnection.addEventListener('track', (event) => {
      this.onRemoteStream?.(event.streams[0]);
    });
    
    this.peerConnection.addEventListener('datachannel', (event) => {
      const channel = event.channel;
      channel.addEventListener('message', (event) => {
        this.onDataChannelMessage?.(event.data);
      });
    });
  }
  
  async getUserMedia(constraints: MediaStreamConstraints): Promise<MediaStream> {
    this.localStream = await navigator.mediaDevices.getUserMedia(constraints);
    
    this.localStream.getTracks().forEach(track => {
      this.peerConnection.addTrack(track, this.localStream!);
    });
    
    return this.localStream;
  }
  
  async createOffer(): Promise<RTCSessionDescriptionInit> {
    this.dataChannel = this.peerConnection.createDataChannel('data');
    
    const offer = await this.peerConnection.createOffer();
    await this.peerConnection.setLocalDescription(offer);
    
    return offer;
  }
  
  async createAnswer(offer: RTCSessionDescriptionInit): Promise<RTCSessionDescriptionInit> {
    await this.peerConnection.setRemoteDescription(offer);
    
    const answer = await this.peerConnection.createAnswer();
    await this.peerConnection.setLocalDescription(answer);
    
    return answer;
  }
  
  async setRemoteAnswer(answer: RTCSessionDescriptionInit): Promise<void> {
    await this.peerConnection.setRemoteDescription(answer);
  }
  
  async addIceCandidate(candidate: RTCIceCandidateInit): Promise<void> {
    await this.peerConnection.addIceCandidate(candidate);
  }
  
  sendData(data: string): void {
    if (this.dataChannel && this.dataChannel.readyState === 'open') {
      this.dataChannel.send(data);
    }
  }
  
  close(): void {
    if (this.localStream) {
      this.localStream.getTracks().forEach(track => track.stop());
    }
    
    this.peerConnection.close();
  }
  
  // Event handlers (to be set by consumer)
  onIceCandidate?: (candidate: RTCIceCandidate) => void;
  onRemoteStream?: (stream: MediaStream) => void;
  onDataChannelMessage?: (data: string) => void;
}
```

**Step 2.2: Performance Optimization and Bundle Management**

```typescript
// Advanced Performance Optimization Utilities
// File: src/utils/performance.ts

// Resource Loading Optimization
class ResourceLoader {
  private static instance: ResourceLoader;
  private loadedResources = new Set<string>();
  private pendingLoads = new Map<string, Promise<any>>();
  
  static getInstance(): ResourceLoader {
    if (!ResourceLoader.instance) {
      ResourceLoader.instance = new ResourceLoader();
    }
    return ResourceLoader.instance;
  }
  
  async loadScript(src: string, options: {
    async?: boolean;
    defer?: boolean;
    integrity?: string;
    crossOrigin?: string;
  } = {}): Promise<void> {
    if (this.loadedResources.has(src)) {
      return;
    }
    
    if (this.pendingLoads.has(src)) {
      return this.pendingLoads.get(src);
    }
    
    const promise = new Promise<void>((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      
      if (options.async !== undefined) script.async = options.async;
      if (options.defer !== undefined) script.defer = options.defer;
      if (options.integrity) script.integrity = options.integrity;
      if (options.crossOrigin) script.crossOrigin = options.crossOrigin;
      
      script.onload = () => {
        this.loadedResources.add(src);
        this.pendingLoads.delete(src);
        resolve();
      };
      
      script.onerror = () => {
        this.pendingLoads.delete(src);
        reject(new Error(`Failed to load script: ${src}`));
      };
      
      document.head.appendChild(script);
    });
    
    this.pendingLoads.set(src, promise);
    return promise;
  }
  
  async loadCSS(href: string, media = 'all'): Promise<void> {
    if (this.loadedResources.has(href)) {
      return;
    }
    
    if (this.pendingLoads.has(href)) {
      return this.pendingLoads.get(href);
    }
    
    const promise = new Promise<void>((resolve, reject) => {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      link.media = media;
      
      link.onload = () => {
        this.loadedResources.add(href);
        this.pendingLoads.delete(href);
        resolve();
      };
      
      link.onerror = () => {
        this.pendingLoads.delete(href);
        reject(new Error(`Failed to load CSS: ${href}`));
      };
      
      document.head.appendChild(link);
    });
    
    this.pendingLoads.set(href, promise);
    return promise;
  }
  
  preloadResource(href: string, as: string, crossOrigin?: string): void {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = href;
    link.as = as;
    if (crossOrigin) link.crossOrigin = crossOrigin;
    
    document.head.appendChild(link);
  }
  
  prefetchResource(href: string): void {
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = href;
    
    document.head.appendChild(link);
  }
}

// Advanced Performance Monitoring
class PerformanceMonitor {
  private observers: {
    intersectionObserver?: IntersectionObserver;
    performanceObserver?: PerformanceObserver;
    mutationObserver?: MutationObserver;
  } = {};
  
  private metrics = {
    lcp: 0,
    fid: 0,
    cls: 0,
    fcp: 0,
    ttfb: 0
  };
  
  start(): void {
    this.observeWebVitals();
    this.observeResourceTiming();
    this.observeLongTasks();
    this.observeLayoutShifts();
  }
  
  private observeWebVitals(): void {
    // Largest Contentful Paint
    if ('PerformanceObserver' in window) {
      try {
        const lcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1] as any;
          this.metrics.lcp = lastEntry.startTime;
          this.reportMetric('LCP', lastEntry.startTime);
        });
        
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
        
        // First Input Delay
        const fidObserver = new PerformanceObserver((list) => {
          const firstInput = list.getEntries()[0] as any;
          this.metrics.fid = firstInput.processingStart - firstInput.startTime;
          this.reportMetric('FID', this.metrics.fid);
        });
        
        fidObserver.observe({ entryTypes: ['first-input'] });
        
        // First Contentful Paint
        const fcpObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach((entry: any) => {
            if (entry.name === 'first-contentful-paint') {
              this.metrics.fcp = entry.startTime;
              this.reportMetric('FCP', entry.startTime);
            }
          });
        });
        
        fcpObserver.observe({ entryTypes: ['paint'] });
        
      } catch (error) {
        console.warn('Performance Observer not supported', error);
      }
    }
    
    // Navigation Timing
    window.addEventListener('load', () => {
      const navigation = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
      this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
      this.reportMetric('TTFB', this.metrics.ttfb);
    });
  }
  
  private observeResourceTiming(): void {
    if ('PerformanceObserver' in window) {
      const resourceObserver = new PerformanceObserver((list) => {
        list.getEntries().forEach((entry: PerformanceResourceTiming) => {
          this.analyzeResourceTiming(entry);
        });
      });
      
      resourceObserver.observe({ entryTypes: ['resource'] });
      this.observers.performanceObserver = resourceObserver;
    }
  }
  
  private observeLongTasks(): void {
    if ('PerformanceObserver' in window) {
      try {
        const longTaskObserver = new PerformanceObserver((list) => {
          list.getEntries().forEach((entry: any) => {
            console.warn('Long task detected:', {
              duration: entry.duration,
              startTime: entry.startTime
            });
          });
        });
        
        longTaskObserver.observe({ entryTypes: ['longtask'] });
      } catch (error) {
        // longtask might not be supported
      }
    }
  }
  
  private observeLayoutShifts(): void {
    if ('PerformanceObserver' in window) {
      try {
        let clsValue = 0;
        
        const clsObserver = new PerformanceObserver((list) => {
          list.getEntries().forEach((entry: any) => {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
            }
          });
          
          this.metrics.cls = clsValue;
          this.reportMetric('CLS', clsValue);
        });
        
        clsObserver.observe({ entryTypes: ['layout-shift'] });
      } catch (error) {
        // layout-shift might not be supported
      }
    }
  }
  
  private analyzeResourceTiming(entry: PerformanceResourceTiming): void {
    const analysis = {
      name: entry.name,
      duration: entry.duration,
      transferSize: entry.transferSize,
      encodedBodySize: entry.encodedBodySize,
      decodedBodySize: entry.decodedBodySize,
      compressionRatio: entry.encodedBodySize > 0 
        ? (entry.decodedBodySize / entry.encodedBodySize) 
        : 0
    };
    
    // Report slow resources
    if (entry.duration > 1000) {
      console.warn('Slow resource detected:', analysis);
    }
    
    // Report large resources
    if (entry.transferSize > 1024 * 1024) { // > 1MB
      console.warn('Large resource detected:', analysis);
    }
  }
  
  private reportMetric(name: string, value: number): void {
    // Send metrics to analytics service
    if (window.gtag) {
      window.gtag('event', 'web_vital', {
        name,
        value: Math.round(value),
        event_category: 'Performance'
      });
    }
    
    // Console log for debugging
    console.log(`${name}: ${Math.round(value)}ms`);
  }
  
  getMetrics(): typeof this.metrics {
    return { ...this.metrics };
  }
  
  stop(): void {
    Object.values(this.observers).forEach(observer => {
      observer?.disconnect();
    });
  }
}

// Bundle Splitting and Code Organization
export class ModuleLoader {
  private static cache = new Map<string, any>();
  
  static async loadModule<T = any>(
    moduleFactory: () => Promise<T>,
    key?: string
  ): Promise<T> {
    const cacheKey = key || moduleFactory.toString();
    
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }
    
    try {
      const module = await moduleFactory();
      this.cache.set(cacheKey, module);
      return module;
    } catch (error) {
      console.error('Failed to load module:', error);
      throw error;
    }
  }
  
  static async loadComponent(componentPath: string) {
    return this.loadModule(
      () => import(/* webpackChunkName: "[request]" */ componentPath),
      componentPath
    );
  }
  
  static preloadModule(moduleFactory: () => Promise<any>, key?: string): void {
    const cacheKey = key || moduleFactory.toString();
    
    if (!this.cache.has(cacheKey)) {
      moduleFactory().then(module => {
        this.cache.set(cacheKey, module);
      }).catch(error => {
        console.error('Failed to preload module:', error);
      });
    }
  }
  
  static clearCache(): void {
    this.cache.clear();
  }
}

// Usage examples for chunk splitting
export const ChunkExamples = {
  // Route-based splitting
  loadDashboard: () => ModuleLoader.loadComponent('./pages/Dashboard'),
  loadProfile: () => ModuleLoader.loadComponent('./pages/Profile'),
  
  // Feature-based splitting
  loadChartLibrary: () => ModuleLoader.loadModule(() => import('chart.js')),
  loadDateLibrary: () => ModuleLoader.loadModule(() => import('date-fns')),
  
  // Vendor splitting
  loadUtilities: () => ModuleLoader.loadModule(() => import('lodash')),
  
  // Preloading critical modules
  preloadCritical: () => {
    ModuleLoader.preloadModule(() => import('./components/Header'));
    ModuleLoader.preloadModule(() => import('./components/Navigation'));
  }
};
```

### Phase 3: Testing and Development Tools Integration (2-3 hours)

**Step 3.1: Comprehensive Testing Framework**

```typescript
// Advanced Testing Utilities and Patterns
// File: src/utils/testing.ts

import { vi, describe, it, expect, beforeEach, afterEach } from 'vitest';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import { renderHook, act } from '@testing-library/react-hooks';

// Advanced Mock Utilities
export class MockBuilder<T> {
  private mockObj: Partial<T> = {};
  private spies: Map<string, any> = new Map();
  
  with<K extends keyof T>(key: K, value: T[K] | ((original: T[K]) => T[K])): MockBuilder<T> {
    if (typeof value === 'function' && typeof this.mockObj[key] === 'function') {
      // If it's a function and we're mocking a function, create a spy
      const spy = vi.fn(value as any);
      this.spies.set(key as string, spy);
      this.mockObj[key] = spy;
    } else {
      this.mockObj[key] = typeof value === 'function' ? (value as any)(this.mockObj[key]) : value;
    }
    return this;
  }
  
  spy<K extends keyof T>(key: K): MockBuilder<T> {
    if (this.mockObj[key]) {
      const spy = vi.fn(this.mockObj[key] as any);
      this.spies.set(key as string, spy);
      this.mockObj[key] = spy;
    }
    return this;
  }
  
  build(): T & { [K in keyof T]: T[K] extends (...args: any[]) => any ? ReturnType<typeof vi.fn> : T[K] } {
    return this.mockObj as any;
  }
  
  getSpy<K extends keyof T>(key: K): ReturnType<typeof vi.fn> | undefined {
    return this.spies.get(key as string);
  }
  
  reset(): void {
    this.spies.forEach(spy => spy.mockReset());
  }
  
  restore(): void {
    this.spies.forEach(spy => spy.mockRestore());
  }
}

// API Testing Utilities
export class APITestHelper {
  private baseURL: string;
  private defaultHeaders: Record<string, string>;
  
  constructor(baseURL = '', headers: Record<string, string> = {}) {
    this.baseURL = baseURL;
    this.defaultHeaders = headers;
  }
  
  mockFetch(responses: Array<{
    url?: string | RegExp;
    method?: string;
    status?: number;
    data?: any;
    delay?: number;
  }>): void {
    global.fetch = vi.fn().mockImplementation(async (url: string, options = {}) => {
      const method = (options as RequestInit).method || 'GET';
      
      const matchingResponse = responses.find(response => {
        if (response.url) {
          if (response.url instanceof RegExp) {
            return response.url.test(url);
          }
          return url.includes(response.url);
        }
        if (response.method && response.method !== method) {
          return false;
        }
        return true;
      });
      
      if (matchingResponse?.delay) {
        await new Promise(resolve => setTimeout(resolve, matchingResponse.delay));
      }
      
      const response = matchingResponse || { status: 404, data: { error: 'Not found' } };
      
      return {
        ok: (response.status || 200) >= 200 && (response.status || 200) < 300,
        status: response.status || 200,
        json: async () => response.data,
        text: async () => JSON.stringify(response.data),
        headers: new Headers(),
        clone: () => ({
          json: async () => response.data,
        }),
      } as Response;
    });
  }
  
  expectAPICall(
    url: string | RegExp,
    method = 'GET',
    expectedBody?: any
  ): jest.SpyInstance {
    const fetchSpy = vi.mocked(global.fetch);
    
    if (expectedBody) {
      expect(fetchSpy).toHaveBeenCalledWith(
        expect.stringMatching(url instanceof RegExp ? url : new RegExp(url)),
        expect.objectContaining({
          method,
          body: JSON.stringify(expectedBody),
          headers: expect.objectContaining({
            'Content-Type': 'application/json',
          }),
        })
      );
    } else {
      expect(fetchSpy).toHaveBeenCalledWith(
        expect.stringMatching(url instanceof RegExp ? url : new RegExp(url)),
        expect.objectContaining({ method })
      );
    }
    
    return fetchSpy;
  }
  
  reset(): void {
    vi.clearAllMocks();
  }
}

// Component Testing Utilities
export class ComponentTestHelper {
  static async waitForLoadingToFinish(): Promise<void> {
    await waitFor(() => {
      expect(screen.queryByTestId('loading')).not.toBeInTheDocument();
    }, { timeout: 5000 });
  }
  
  static async waitForElementToAppear(
    testId: string,
    timeout = 5000
  ): Promise<HTMLElement> {
    return waitFor(
      () => {
        const element = screen.getByTestId(testId);
        expect(element).toBeInTheDocument();
        return element;
      },
      { timeout }
    );
  }
  
  static async waitForElementToDisappear(
    testId: string,
    timeout = 5000
  ): Promise<void> {
    await waitFor(
      () => {
        expect(screen.queryByTestId(testId)).not.toBeInTheDocument();
      },
      { timeout }
    );
  }
  
  static async fillForm(
    fields: Array<{ testId: string; value: string; type?: 'input' | 'select' | 'textarea' }>
  ): Promise<void> {
    for (const field of fields) {
      const element = screen.getByTestId(field.testId);
      
      switch (field.type) {
        case 'select':
          fireEvent.change(element, { target: { value: field.value } });
          break;
        case 'textarea':
        case 'input':
        default:
          fireEvent.change(element, { target: { value: field.value } });
          break;
      }
    }
  }
  
  static async submitForm(submitButtonTestId: string): Promise<void> {
    const submitButton = screen.getByTestId(submitButtonTestId);
    fireEvent.click(submitButton);
  }
  
  static getAccessibilityTree(): string {
    return screen.debug();
  }
}

// Performance Testing Utilities
export class PerformanceTestHelper {
  static measureRenderTime<T>(
    renderFunction: () => T,
    iterations = 100
  ): { averageTime: number; minTime: number; maxTime: number; results: T[] } {
    const times: number[] = [];
    const results: T[] = [];
    
    for (let i = 0; i < iterations; i++) {
      const startTime = performance.now();
      const result = renderFunction();
      const endTime = performance.now();
      
      times.push(endTime - startTime);
      results.push(result);
    }
    
    return {
      averageTime: times.reduce((sum, time) => sum + time, 0) / times.length,
      minTime: Math.min(...times),
      maxTime: Math.max(...times),
      results
    };
  }
  
  static async measureAsyncOperation<T>(
    operation: () => Promise<T>,
    iterations = 10
  ): Promise<{ averageTime: number; minTime: number; maxTime: number; results: T[] }> {
    const times: number[] = [];
    const results: T[] = [];
    
    for (let i = 0; i < iterations; i++) {
      const startTime = performance.now();
      const result = await operation();
      const endTime = performance.now();
      
      times.push(endTime - startTime);
      results.push(result);
    }
    
    return {
      averageTime: times.reduce((sum, time) => sum + time, 0) / times.length,
      minTime: Math.min(...times),
      maxTime: Math.max(...times),
      results
    };
  }
  
  static expectPerformance(
    actualTime: number,
    expectedMaxTime: number,
    operation = 'Operation'
  ): void {
    expect(actualTime).toBeLessThan(expectedMaxTime);
    
    if (actualTime > expectedMaxTime * 0.8) {
      console.warn(
        `${operation} took ${actualTime.toFixed(2)}ms, approaching limit of ${expectedMaxTime}ms`
      );
    }
  }
}

// Integration Testing Utilities
export class IntegrationTestHelper {
  private mockServices = new Map<string, any>();
  
  mockService<T>(name: string, implementation: Partial<T>): void {
    this.mockServices.set(name, implementation);
  }
  
  getService<T>(name: string): T {
    return this.mockServices.get(name);
  }
  
  setupTestEnvironment(): void {
    // Mock common browser APIs
    Object.defineProperty(window, 'matchMedia', {
      writable: true,
      value: vi.fn().mockImplementation(query => ({
        matches: false,
        media: query,
        onchange: null,
        addListener: vi.fn(),
        removeListener: vi.fn(),
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        dispatchEvent: vi.fn(),
      })),
    });
    
    Object.defineProperty(window, 'ResizeObserver', {
      writable: true,
      value: vi.fn().mockImplementation(() => ({
        observe: vi.fn(),
        unobserve: vi.fn(),
        disconnect: vi.fn(),
      })),
    });
    
    Object.defineProperty(window, 'IntersectionObserver', {
      writable: true,
      value: vi.fn().mockImplementation(() => ({
        observe: vi.fn(),
        unobserve: vi.fn(),
        disconnect: vi.fn(),
      })),
    });
  }
  
  teardownTestEnvironment(): void {
    vi.clearAllMocks();
    this.mockServices.clear();
  }
}

// Example Test Suite
describe('Advanced Testing Examples', () => {
  let apiHelper: APITestHelper;
  let integrationHelper: IntegrationTestHelper;
  
  beforeEach(() => {
    apiHelper = new APITestHelper('https://api.example.com');
    integrationHelper = new IntegrationTestHelper();
    integrationHelper.setupTestEnvironment();
  });
  
  afterEach(() => {
    apiHelper.reset();
    integrationHelper.teardownTestEnvironment();
  });
  
  describe('MockBuilder', () => {
    it('should create comprehensive mocks with spies', () => {
      interface UserService {
        getUser: (id: string) => Promise<User>;
        updateUser: (id: string, data: Partial<User>) => Promise<User>;
        deleteUser: (id: string) => Promise<void>;
      }
      
      const mockUserService = new MockBuilder<UserService>()
        .with('getUser', vi.fn().mockResolvedValue({ id: '1', name: 'Test User' }))
        .with('updateUser', vi.fn().mockResolvedValue({ id: '1', name: 'Updated User' }))
        .spy('deleteUser')
        .build();
      
      expect(mockUserService.getUser).toBeDefined();
      expect(mockUserService.updateUser).toBeDefined();
      expect(mockUserService.deleteUser).toBeDefined();
    });
  });
  
  describe('Performance Testing', () => {
    it('should measure component render performance', () => {
      const performanceResults = PerformanceTestHelper.measureRenderTime(
        () => render(<div>Test Component</div>),
        50
      );
      
      PerformanceTestHelper.expectPerformance(
        performanceResults.averageTime,
        10, // 10ms max
        'Component render'
      );
    });
  });
  
  describe('API Testing', () => {
    it('should mock and verify API calls', async () => {
      apiHelper.mockFetch([
        {
          url: '/users/1',
          method: 'GET',
          status: 200,
          data: { id: '1', name: 'Test User' },
          delay: 100
        }
      ]);
      
      const response = await fetch('/users/1');
      const data = await response.json();
      
      expect(data).toEqual({ id: '1', name: 'Test User' });
      apiHelper.expectAPICall('/users/1', 'GET');
    });
  });
});
```

## 📊 Success Criteria

### Code Quality Metrics
- **Type Safety**: 100% TypeScript strict mode compliance with zero `any` types
- **Test Coverage**: >95% line coverage for critical business logic
- **Performance**: <50ms for complex operations, <16ms for UI interactions
- **Bundle Size**: <100KB gzipped for main application bundle

### Modern JavaScript Standards
- **ES2022+ Features**: Full utilization of modern JavaScript features
- **Browser Compatibility**: Support for last 2 versions of major browsers
- **Tree Shaking**: >90% unused code elimination in production builds
- **Code Splitting**: Optimal chunk sizes <250KB for route-based splits

### Developer Experience Metrics
- **Build Speed**: <30s for development builds, <2min for production builds
- **Hot Reload**: <200ms for component updates
- **IDE Integration**: Full IntelliSense and error reporting
- **Debugging**: Complete source map coverage with meaningful stack traces

## 🎯 Deliverables

Upon completion of modern JavaScript and TypeScript development implementation:

- ✅ **Advanced TypeScript Configuration** with strict mode, custom types, and utility types
- ✅ **Modern JavaScript Features** utilizing ES2022+ syntax and browser APIs
- ✅ **Performance Optimization** with lazy loading, code splitting, and bundle optimization
- ✅ **Comprehensive Testing Suite** with unit, integration, and performance tests
- ✅ **Developer Tooling** with hot reloading, source maps, and debugging capabilities
- ✅ **Web APIs Integration** including Service Workers, WebRTC, and modern browser features
- ✅ **Type-Safe Architecture** with branded types, advanced generics, and runtime validation
- ✅ **Build Configuration** with Webpack/Vite optimization and development workflow

---

*This comprehensive modern JavaScript and TypeScript development approach provides cutting-edge language features, robust type safety, and optimized performance for scalable frontend applications.*