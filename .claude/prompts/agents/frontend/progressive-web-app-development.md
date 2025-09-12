# Progressive Web App Development

**Agent Type: frontend-engineer**
**Complexity Level: Expert**
**Estimated Duration: 8-12 hours**

---

## 🎯 Mission

Design and implement comprehensive Progressive Web Applications (PWAs) with advanced features including offline functionality, background sync, push notifications, and native-like experiences across all devices and platforms.

## 📋 Process Framework

### Phase 1: PWA Architecture and Service Worker Implementation (3-4 hours)

**Step 1.1: Advanced Service Worker Architecture**

```typescript
// Advanced Service Worker Implementation
// File: public/sw.js (will be compiled from TypeScript)

declare const self: ServiceWorkerGlobalScope;

interface CacheStrategy {
  name: string;
  pattern: RegExp | string;
  strategy: 'cacheFirst' | 'networkFirst' | 'staleWhileRevalidate' | 'networkOnly' | 'cacheOnly';
  options?: {
    cacheName?: string;
    expiration?: {
      maxEntries?: number;
      maxAgeSeconds?: number;
    };
    backgroundSync?: string;
    broadcastUpdate?: boolean;
  };
}

interface SyncTask {
  tag: string;
  data: any;
  timestamp: number;
  retryCount: number;
  maxRetries: number;
}

class AdvancedServiceWorker {
  private static readonly CACHE_VERSION = 'v2.1.0';
  private static readonly CACHE_PREFIX = 'pwa-cache';
  private static readonly SYNC_STORE = 'sync-store';
  
  private cacheStrategies: CacheStrategy[] = [
    {
      name: 'static-assets',
      pattern: /\.(js|css|woff2?|png|jpg|jpeg|gif|svg|ico)$/,
      strategy: 'cacheFirst',
      options: {
        cacheName: `${AdvancedServiceWorker.CACHE_PREFIX}-static-${AdvancedServiceWorker.CACHE_VERSION}`,
        expiration: {
          maxEntries: 100,
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 days
        }
      }
    },
    {
      name: 'api-data',
      pattern: /^https:\/\/api\./,
      strategy: 'networkFirst',
      options: {
        cacheName: `${AdvancedServiceWorker.CACHE_PREFIX}-api-${AdvancedServiceWorker.CACHE_VERSION}`,
        expiration: {
          maxEntries: 50,
          maxAgeSeconds: 5 * 60 // 5 minutes
        },
        backgroundSync: 'api-sync'
      }
    },
    {
      name: 'images',
      pattern: /\.(png|jpg|jpeg|gif|webp|avif)$/,
      strategy: 'staleWhileRevalidate',
      options: {
        cacheName: `${AdvancedServiceWorker.CACHE_PREFIX}-images-${AdvancedServiceWorker.CACHE_VERSION}`,
        expiration: {
          maxEntries: 200,
          maxAgeSeconds: 7 * 24 * 60 * 60 // 7 days
        }
      }
    },
    {
      name: 'html-pages',
      pattern: /\.html$|\/$/,
      strategy: 'staleWhileRevalidate',
      options: {
        cacheName: `${AdvancedServiceWorker.CACHE_PREFIX}-pages-${AdvancedServiceWorker.CACHE_VERSION}`,
        broadcastUpdate: true
      }
    }
  ];

  private syncQueue: SyncTask[] = [];
  private isOnline = navigator.onLine;

  install(): void {
    self.addEventListener('install', (event: ExtendableEvent) => {
      event.waitUntil(this.handleInstall());
    });
  }

  activate(): void {
    self.addEventListener('activate', (event: ExtendableEvent) => {
      event.waitUntil(this.handleActivate());
    });
  }

  fetch(): void {
    self.addEventListener('fetch', (event: FetchEvent) => {
      event.respondWith(this.handleFetch(event));
    });
  }

  backgroundSync(): void {
    self.addEventListener('sync', (event: any) => {
      event.waitUntil(this.handleBackgroundSync(event));
    });
  }

  pushNotifications(): void {
    self.addEventListener('push', (event: PushEvent) => {
      event.waitUntil(this.handlePushNotification(event));
    });

    self.addEventListener('notificationclick', (event: NotificationEvent) => {
      event.waitUntil(this.handleNotificationClick(event));
    });
  }

  private async handleInstall(): Promise<void> {
    console.log('[SW] Installing...');
    
    // Pre-cache critical assets
    const criticalAssets = [
      '/',
      '/static/js/main.js',
      '/static/css/main.css',
      '/offline.html'
    ];

    const cache = await caches.open(
      `${AdvancedServiceWorker.CACHE_PREFIX}-critical-${AdvancedServiceWorker.CACHE_VERSION}`
    );
    
    await cache.addAll(criticalAssets);
    
    // Skip waiting to activate immediately
    self.skipWaiting();
  }

  private async handleActivate(): Promise<void> {
    console.log('[SW] Activating...');
    
    // Clean up old caches
    const cacheNames = await caches.keys();
    const oldCaches = cacheNames.filter(name => 
      name.startsWith(AdvancedServiceWorker.CACHE_PREFIX) && 
      !name.includes(AdvancedServiceWorker.CACHE_VERSION)
    );

    await Promise.all(
      oldCaches.map(cacheName => caches.delete(cacheName))
    );

    // Claim all clients
    self.clients.claim();
    
    // Initialize sync store
    await this.initializeSyncStore();
  }

  private async handleFetch(event: FetchEvent): Promise<Response> {
    const { request } = event;
    const url = new URL(request.url);

    // Skip non-GET requests for caching
    if (request.method !== 'GET') {
      return this.handleNonGetRequest(request);
    }

    // Find matching cache strategy
    const strategy = this.cacheStrategies.find(s => {
      if (typeof s.pattern === 'string') {
        return url.href.includes(s.pattern);
      }
      return s.pattern.test(url.href);
    });

    if (!strategy) {
      return fetch(request);
    }

    return this.executeStrategy(request, strategy);
  }

  private async executeStrategy(
    request: Request, 
    strategy: CacheStrategy
  ): Promise<Response> {
    const cacheName = strategy.options?.cacheName || 
      `${AdvancedServiceWorker.CACHE_PREFIX}-default-${AdvancedServiceWorker.CACHE_VERSION}`;
    const cache = await caches.open(cacheName);

    switch (strategy.strategy) {
      case 'cacheFirst':
        return this.cacheFirst(request, cache, strategy);
      case 'networkFirst':
        return this.networkFirst(request, cache, strategy);
      case 'staleWhileRevalidate':
        return this.staleWhileRevalidate(request, cache, strategy);
      case 'networkOnly':
        return fetch(request);
      case 'cacheOnly':
        return cache.match(request) || new Response('Not found', { status: 404 });
      default:
        return fetch(request);
    }
  }

  private async cacheFirst(
    request: Request, 
    cache: Cache, 
    strategy: CacheStrategy
  ): Promise<Response> {
    const cachedResponse = await cache.match(request);
    
    if (cachedResponse) {
      // Check expiration
      if (this.isResponseExpired(cachedResponse, strategy)) {
        this.updateCacheInBackground(request, cache);
      }
      return cachedResponse;
    }

    try {
      const networkResponse = await fetch(request);
      if (networkResponse.ok) {
        await cache.put(request, networkResponse.clone());
      }
      return networkResponse;
    } catch (error) {
      return this.getFallbackResponse(request);
    }
  }

  private async networkFirst(
    request: Request, 
    cache: Cache, 
    strategy: CacheStrategy
  ): Promise<Response> {
    try {
      const networkResponse = await fetch(request);
      
      if (networkResponse.ok) {
        await cache.put(request, networkResponse.clone());
        
        if (strategy.options?.broadcastUpdate) {
          this.broadcastUpdate(request.url);
        }
      }
      
      return networkResponse;
    } catch (error) {
      const cachedResponse = await cache.match(request);
      
      if (cachedResponse) {
        return cachedResponse;
      }

      // Queue for background sync if configured
      if (strategy.options?.backgroundSync) {
        await this.queueForSync(strategy.options.backgroundSync, {
          url: request.url,
          method: request.method,
          headers: Array.from(request.headers.entries()),
          body: await request.clone().text()
        });
      }

      return this.getFallbackResponse(request);
    }
  }

  private async staleWhileRevalidate(
    request: Request, 
    cache: Cache, 
    strategy: CacheStrategy
  ): Promise<Response> {
    const cachedResponse = await cache.match(request);
    
    const fetchPromise = fetch(request).then(networkResponse => {
      if (networkResponse.ok) {
        cache.put(request, networkResponse.clone());
        
        if (strategy.options?.broadcastUpdate) {
          this.broadcastUpdate(request.url);
        }
      }
      return networkResponse;
    }).catch(() => null);

    if (cachedResponse) {
      // Start fetch in background but return cached response immediately
      fetchPromise;
      return cachedResponse;
    }

    // No cached response, wait for network
    const networkResponse = await fetchPromise;
    return networkResponse || this.getFallbackResponse(request);
  }

  private async handleNonGetRequest(request: Request): Promise<Response> {
    try {
      return await fetch(request);
    } catch (error) {
      // Queue for background sync
      await this.queueForSync('api-sync', {
        url: request.url,
        method: request.method,
        headers: Array.from(request.headers.entries()),
        body: await request.clone().text()
      });

      return new Response(JSON.stringify({
        error: 'Network unavailable',
        queued: true
      }), {
        status: 202,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }

  private isResponseExpired(response: Response, strategy: CacheStrategy): boolean {
    if (!strategy.options?.expiration?.maxAgeSeconds) {
      return false;
    }

    const dateHeader = response.headers.get('date');
    if (!dateHeader) {
      return false;
    }

    const responseDate = new Date(dateHeader);
    const maxAge = strategy.options.expiration.maxAgeSeconds * 1000;
    
    return Date.now() - responseDate.getTime() > maxAge;
  }

  private async updateCacheInBackground(request: Request, cache: Cache): Promise<void> {
    try {
      const networkResponse = await fetch(request);
      if (networkResponse.ok) {
        await cache.put(request, networkResponse);
      }
    } catch (error) {
      console.log('[SW] Background update failed:', error);
    }
  }

  private getFallbackResponse(request: Request): Response {
    const url = new URL(request.url);
    
    if (url.pathname.includes('api/')) {
      return new Response(JSON.stringify({
        error: 'Network unavailable',
        offline: true
      }), {
        status: 503,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Return offline page for navigation requests
    if (request.mode === 'navigate') {
      return caches.match('/offline.html').then(response => 
        response || new Response('Offline', { status: 503 })
      );
    }

    return new Response('Network unavailable', { status: 503 });
  }

  private async queueForSync(tag: string, data: any): Promise<void> {
    const syncTask: SyncTask = {
      tag,
      data,
      timestamp: Date.now(),
      retryCount: 0,
      maxRetries: 3
    };

    this.syncQueue.push(syncTask);
    await this.persistSyncQueue();

    // Register for background sync
    if ('serviceWorker' in navigator && 'sync' in window.ServiceWorkerRegistration.prototype) {
      const registration = await navigator.serviceWorker.ready;
      await registration.sync.register(tag);
    }
  }

  private async handleBackgroundSync(event: any): Promise<void> {
    console.log('[SW] Background sync:', event.tag);
    
    const tasks = this.syncQueue.filter(task => task.tag === event.tag);
    const results = await Promise.allSettled(
      tasks.map(task => this.executeSyncTask(task))
    );

    // Remove successful tasks and increment retry count for failed ones
    this.syncQueue = this.syncQueue.filter((task, index) => {
      const result = results[index];
      
      if (result.status === 'fulfilled') {
        return false; // Remove successful task
      }
      
      task.retryCount++;
      return task.retryCount <= task.maxRetries;
    });

    await this.persistSyncQueue();
  }

  private async executeSyncTask(task: SyncTask): Promise<void> {
    const { url, method, headers, body } = task.data;
    
    const response = await fetch(url, {
      method,
      headers: new Headers(headers),
      body: method !== 'GET' ? body : undefined
    });

    if (!response.ok) {
      throw new Error(`Sync task failed: ${response.status}`);
    }
  }

  private async initializeSyncStore(): Promise<void> {
    try {
      const cache = await caches.open(AdvancedServiceWorker.SYNC_STORE);
      const response = await cache.match('/sync-queue');
      
      if (response) {
        this.syncQueue = await response.json();
      }
    } catch (error) {
      console.log('[SW] Failed to initialize sync store:', error);
    }
  }

  private async persistSyncQueue(): Promise<void> {
    try {
      const cache = await caches.open(AdvancedServiceWorker.SYNC_STORE);
      await cache.put('/sync-queue', new Response(JSON.stringify(this.syncQueue)));
    } catch (error) {
      console.log('[SW] Failed to persist sync queue:', error);
    }
  }

  private broadcastUpdate(url: string): void {
    self.clients.matchAll().then(clients => {
      clients.forEach(client => {
        client.postMessage({
          type: 'CACHE_UPDATED',
          url,
          timestamp: Date.now()
        });
      });
    });
  }

  private async handlePushNotification(event: PushEvent): Promise<void> {
    const options = {
      body: 'Default notification body',
      icon: '/icon-192x192.png',
      badge: '/badge-72x72.png',
      data: {},
      actions: [],
      requireInteraction: false,
      silent: false,
      ...event.data?.json()
    };

    await self.registration.showNotification(options.title || 'Notification', options);
  }

  private async handleNotificationClick(event: NotificationEvent): Promise<void> {
    event.notification.close();

    const action = event.action;
    const data = event.notification.data;

    if (action === 'open') {
      const url = data?.url || '/';
      const windowClients = await self.clients.matchAll({ type: 'window' });
      
      // Check if there's already a window open
      for (const client of windowClients) {
        if (client.url === url && 'focus' in client) {
          return client.focus();
        }
      }
      
      // Open new window
      if (self.clients.openWindow) {
        return self.clients.openWindow(url);
      }
    }
  }
}

// Initialize Service Worker
const serviceWorker = new AdvancedServiceWorker();
serviceWorker.install();
serviceWorker.activate();
serviceWorker.fetch();
serviceWorker.backgroundSync();
serviceWorker.pushNotifications();
```

**Step 1.2: PWA Manifest and Installation**

```typescript
// PWA Manifest Generator and Installation Handler
// File: src/utils/pwa-manager.ts

interface PWAManifest {
  name: string;
  short_name: string;
  description: string;
  start_url: string;
  display: 'standalone' | 'fullscreen' | 'minimal-ui' | 'browser';
  orientation: 'portrait' | 'landscape' | 'any';
  theme_color: string;
  background_color: string;
  icons: ManifestIcon[];
  categories: string[];
  shortcuts?: ManifestShortcut[];
  screenshots?: ManifestScreenshot[];
  share_target?: ShareTarget;
  protocol_handlers?: ProtocolHandler[];
}

interface ManifestIcon {
  src: string;
  sizes: string;
  type: string;
  purpose?: 'any' | 'maskable' | 'monochrome';
}

interface ManifestShortcut {
  name: string;
  short_name?: string;
  description: string;
  url: string;
  icons: ManifestIcon[];
}

interface ManifestScreenshot {
  src: string;
  sizes: string;
  type: string;
  platform?: 'wide' | 'narrow';
  label?: string;
}

interface ShareTarget {
  action: string;
  method: 'GET' | 'POST';
  params: {
    title?: string;
    text?: string;
    url?: string;
    files?: FileShareTargetParam[];
  };
}

interface FileShareTargetParam {
  name: string;
  accept: string[];
}

interface ProtocolHandler {
  protocol: string;
  url: string;
}

export class PWAManager {
  private deferredPrompt: BeforeInstallPromptEvent | null = null;
  private isInstalled = false;
  private installAnalytics: InstallAnalytics;

  constructor() {
    this.installAnalytics = new InstallAnalytics();
    this.setupInstallPrompt();
    this.detectInstallation();
    this.handleAppInstalled();
  }

  generateManifest(config: Partial<PWAManifest> = {}): PWAManifest {
    const defaultManifest: PWAManifest = {
      name: 'Progressive Web Application',
      short_name: 'PWA',
      description: 'A powerful Progressive Web Application',
      start_url: '/',
      display: 'standalone',
      orientation: 'portrait',
      theme_color: '#000000',
      background_color: '#ffffff',
      categories: ['productivity', 'utilities'],
      icons: [
        {
          src: '/icon-72x72.png',
          sizes: '72x72',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-96x96.png',
          sizes: '96x96',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-128x128.png',
          sizes: '128x128',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-144x144.png',
          sizes: '144x144',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-152x152.png',
          sizes: '152x152',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-192x192.png',
          sizes: '192x192',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-384x384.png',
          sizes: '384x384',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/icon-512x512.png',
          sizes: '512x512',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: '/maskable-icon-512x512.png',
          sizes: '512x512',
          type: 'image/png',
          purpose: 'maskable'
        }
      ],
      shortcuts: [
        {
          name: 'Dashboard',
          description: 'Open the main dashboard',
          url: '/dashboard',
          icons: [
            {
              src: '/shortcut-dashboard-96x96.png',
              sizes: '96x96',
              type: 'image/png'
            }
          ]
        },
        {
          name: 'Profile',
          description: 'View your profile',
          url: '/profile',
          icons: [
            {
              src: '/shortcut-profile-96x96.png',
              sizes: '96x96',
              type: 'image/png'
            }
          ]
        }
      ],
      screenshots: [
        {
          src: '/screenshot-desktop-1280x720.png',
          sizes: '1280x720',
          type: 'image/png',
          platform: 'wide',
          label: 'Desktop view of the application'
        },
        {
          src: '/screenshot-mobile-375x812.png',
          sizes: '375x812',
          type: 'image/png',
          platform: 'narrow',
          label: 'Mobile view of the application'
        }
      ],
      share_target: {
        action: '/share',
        method: 'POST',
        params: {
          title: 'title',
          text: 'text',
          url: 'url',
          files: [
            {
              name: 'files',
              accept: ['image/*', '.pdf', '.doc', '.docx']
            }
          ]
        }
      },
      protocol_handlers: [
        {
          protocol: 'web+pwa',
          url: '/handle-protocol?url=%s'
        }
      ]
    };

    return { ...defaultManifest, ...config };
  }

  private setupInstallPrompt(): void {
    window.addEventListener('beforeinstallprompt', (e) => {
      // Prevent Chrome 67 and earlier from automatically showing the prompt
      e.preventDefault();
      
      this.deferredPrompt = e as BeforeInstallPromptEvent;
      this.installAnalytics.trackInstallPromptShown();
      
      // Show custom install button/banner
      this.showInstallPromotion();
    });
  }

  private detectInstallation(): void {
    // Check if app is installed
    if (window.matchMedia('(display-mode: standalone)').matches) {
      this.isInstalled = true;
      this.installAnalytics.trackAppLaunched('standalone');
    } else if (window.navigator.standalone) {
      // iOS Safari standalone mode
      this.isInstalled = true;
      this.installAnalytics.trackAppLaunched('ios-standalone');
    }

    // Listen for app installation
    window.addEventListener('appinstalled', () => {
      this.handleAppInstalled();
    });
  }

  async promptInstall(): Promise<{ outcome: string; platform: string }> {
    if (!this.deferredPrompt) {
      throw new Error('Install prompt not available');
    }

    // Show the install prompt
    this.deferredPrompt.prompt();

    // Wait for the user to respond to the prompt
    const { outcome, platform } = await this.deferredPrompt.userChoice;
    
    this.installAnalytics.trackInstallPromptResult(outcome, platform);

    if (outcome === 'accepted') {
      this.deferredPrompt = null;
      this.hideInstallPromotion();
    }

    return { outcome, platform };
  }

  private handleAppInstalled(): void {
    this.isInstalled = true;
    this.deferredPrompt = null;
    this.hideInstallPromotion();
    this.installAnalytics.trackAppInstalled();
    
    // Show welcome message for first-time users
    this.showWelcomeMessage();
  }

  private showInstallPromotion(): void {
    // Create and show install promotion UI
    const installBanner = document.createElement('div');
    installBanner.id = 'install-banner';
    installBanner.className = 'install-banner';
    installBanner.innerHTML = `
      <div class="install-banner__content">
        <img src="/icon-48x48.png" alt="App icon" class="install-banner__icon">
        <div class="install-banner__text">
          <h3>Install App</h3>
          <p>Get quick access and a better experience</p>
        </div>
        <button id="install-button" class="install-banner__button">Install</button>
        <button id="dismiss-install" class="install-banner__dismiss">×</button>
      </div>
    `;

    document.body.appendChild(installBanner);

    // Add event listeners
    document.getElementById('install-button')?.addEventListener('click', () => {
      this.promptInstall();
    });

    document.getElementById('dismiss-install')?.addEventListener('click', () => {
      this.hideInstallPromotion();
      this.installAnalytics.trackInstallPromptDismissed();
    });

    // Auto-hide after 10 seconds
    setTimeout(() => {
      this.hideInstallPromotion();
    }, 10000);
  }

  private hideInstallPromotion(): void {
    const banner = document.getElementById('install-banner');
    if (banner) {
      banner.remove();
    }
  }

  private showWelcomeMessage(): void {
    // Show welcome message for newly installed app
    const welcome = document.createElement('div');
    welcome.className = 'welcome-message';
    welcome.innerHTML = `
      <div class="welcome-message__content">
        <h2>Welcome to the App!</h2>
        <p>Thanks for installing. Here are some tips to get started:</p>
        <ul>
          <li>Access offline features even without internet</li>
          <li>Receive important notifications</li>
          <li>Enjoy a fast, app-like experience</li>
        </ul>
        <button class="welcome-message__close">Get Started</button>
      </div>
    `;

    document.body.appendChild(welcome);

    welcome.querySelector('.welcome-message__close')?.addEventListener('click', () => {
      welcome.remove();
    });

    // Auto-remove after 15 seconds
    setTimeout(() => {
      if (welcome.parentNode) {
        welcome.remove();
      }
    }, 15000);
  }

  getInstallationStatus(): {
    isInstalled: boolean;
    canInstall: boolean;
    platform: string;
  } {
    return {
      isInstalled: this.isInstalled,
      canInstall: !!this.deferredPrompt,
      platform: this.getPlatform()
    };
  }

  private getPlatform(): string {
    const userAgent = navigator.userAgent.toLowerCase();
    
    if (/iphone|ipad|ipod/.test(userAgent)) return 'ios';
    if (/android/.test(userAgent)) return 'android';
    if (/windows/.test(userAgent)) return 'windows';
    if (/macintosh/.test(userAgent)) return 'macos';
    if (/linux/.test(userAgent)) return 'linux';
    
    return 'unknown';
  }
}

class InstallAnalytics {
  trackInstallPromptShown(): void {
    this.sendEvent('pwa_install_prompt_shown', {
      timestamp: Date.now(),
      userAgent: navigator.userAgent,
      viewport: `${window.innerWidth}x${window.innerHeight}`
    });
  }

  trackInstallPromptResult(outcome: string, platform: string): void {
    this.sendEvent('pwa_install_prompt_result', {
      outcome,
      platform,
      timestamp: Date.now()
    });
  }

  trackInstallPromptDismissed(): void {
    this.sendEvent('pwa_install_prompt_dismissed', {
      timestamp: Date.now()
    });
  }

  trackAppInstalled(): void {
    this.sendEvent('pwa_app_installed', {
      timestamp: Date.now(),
      installMethod: 'prompt'
    });
  }

  trackAppLaunched(displayMode: string): void {
    this.sendEvent('pwa_app_launched', {
      displayMode,
      timestamp: Date.now(),
      isReturnUser: localStorage.getItem('pwa_first_launch') !== null
    });

    if (!localStorage.getItem('pwa_first_launch')) {
      localStorage.setItem('pwa_first_launch', Date.now().toString());
    }
  }

  private sendEvent(eventName: string, data: Record<string, any>): void {
    // Send to analytics service
    if (window.gtag) {
      window.gtag('event', eventName, data);
    }

    // Log to console in development
    if (process.env.NODE_ENV === 'development') {
      console.log('[PWA Analytics]', eventName, data);
    }
  }
}

// Service Worker Registration with Update Handling
export class ServiceWorkerManager {
  private registration: ServiceWorkerRegistration | null = null;
  private updateAvailable = false;

  async register(): Promise<ServiceWorkerRegistration | null> {
    if (!('serviceWorker' in navigator)) {
      console.warn('Service Worker not supported');
      return null;
    }

    try {
      this.registration = await navigator.serviceWorker.register('/sw.js', {
        scope: '/'
      });

      console.log('Service Worker registered:', this.registration.scope);

      this.setupUpdateHandling();
      this.setupMessageHandling();

      return this.registration;
    } catch (error) {
      console.error('Service Worker registration failed:', error);
      return null;
    }
  }

  private setupUpdateHandling(): void {
    if (!this.registration) return;

    this.registration.addEventListener('updatefound', () => {
      const newWorker = this.registration!.installing;
      
      if (newWorker) {
        newWorker.addEventListener('statechange', () => {
          if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
            this.updateAvailable = true;
            this.showUpdateNotification();
          }
        });
      }
    });

    // Check for updates periodically
    setInterval(() => {
      this.registration?.update();
    }, 60000); // Check every minute
  }

  private setupMessageHandling(): void {
    navigator.serviceWorker.addEventListener('message', (event) => {
      const { type, url, timestamp } = event.data;

      switch (type) {
        case 'CACHE_UPDATED':
          console.log('[SW] Cache updated:', url);
          this.handleCacheUpdate(url);
          break;
        default:
          console.log('[SW] Message:', event.data);
      }
    });
  }

  private showUpdateNotification(): void {
    const notification = document.createElement('div');
    notification.className = 'update-notification';
    notification.innerHTML = `
      <div class="update-notification__content">
        <span>A new version is available!</span>
        <button id="update-app">Update</button>
        <button id="dismiss-update">Later</button>
      </div>
    `;

    document.body.appendChild(notification);

    document.getElementById('update-app')?.addEventListener('click', () => {
      this.applyUpdate();
      notification.remove();
    });

    document.getElementById('dismiss-update')?.addEventListener('click', () => {
      notification.remove();
    });
  }

  private applyUpdate(): void {
    if (this.registration?.waiting) {
      this.registration.waiting.postMessage({ type: 'SKIP_WAITING' });
      
      navigator.serviceWorker.addEventListener('controllerchange', () => {
        window.location.reload();
      });
    }
  }

  private handleCacheUpdate(url: string): void {
    // Notify user about content update
    if (window.location.pathname === new URL(url, window.location.origin).pathname) {
      console.log('Current page content updated');
      // Optionally show a subtle notification
    }
  }

  async unregister(): Promise<boolean> {
    if (this.registration) {
      return this.registration.unregister();
    }
    return false;
  }

  getUpdateStatus(): { updateAvailable: boolean; registration: ServiceWorkerRegistration | null } {
    return {
      updateAvailable: this.updateAvailable,
      registration: this.registration
    };
  }
}
```

### Phase 2: Offline Functionality and Data Synchronization (2-3 hours)

**Step 2.1: Advanced Offline Storage Management**

```typescript
// Advanced Offline Storage and Synchronization
// File: src/utils/offline-storage.ts

interface StorageItem<T = any> {
  data: T;
  timestamp: number;
  version: number;
  ttl?: number;
  syncStatus: 'synced' | 'pending' | 'conflict' | 'failed';
  lastSyncAttempt?: number;
  syncRetries: number;
}

interface SyncOperation {
  id: string;
  type: 'create' | 'update' | 'delete';
  collection: string;
  data: any;
  localTimestamp: number;
  priority: 'high' | 'medium' | 'low';
}

export class AdvancedOfflineStorage {
  private dbName: string;
  private dbVersion: number;
  private db: IDBDatabase | null = null;
  private syncQueue: SyncOperation[] = [];
  private isOnline = navigator.onLine;
  private syncInProgress = false;

  constructor(dbName = 'PWAOfflineDB', version = 1) {
    this.dbName = dbName;
    this.dbVersion = version;
    this.initializeDatabase();
    this.setupOnlineListener();
    this.startPeriodicSync();
  }

  private async initializeDatabase(): Promise<void> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.dbVersion);

      request.onerror = () => {
        console.error('IndexedDB open error:', request.error);
        reject(request.error);
      };

      request.onsuccess = () => {
        this.db = request.result;
        console.log('IndexedDB opened successfully');
        this.loadSyncQueue();
        resolve();
      };

      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;

        // Create object stores
        if (!db.objectStoreNames.contains('storage')) {
          const storageStore = db.createObjectStore('storage', { keyPath: 'id' });
          storageStore.createIndex('collection', 'collection', { unique: false });
          storageStore.createIndex('timestamp', 'timestamp', { unique: false });
          storageStore.createIndex('syncStatus', 'syncStatus', { unique: false });
        }

        if (!db.objectStoreNames.contains('syncQueue')) {
          const syncStore = db.createObjectStore('syncQueue', { keyPath: 'id' });
          syncStore.createIndex('priority', 'priority', { unique: false });
          syncStore.createIndex('timestamp', 'localTimestamp', { unique: false });
        }

        if (!db.objectStoreNames.contains('metadata')) {
          db.createObjectStore('metadata', { keyPath: 'key' });
        }
      };
    });
  }

  async store<T>(
    collection: string,
    id: string,
    data: T,
    options: {
      ttl?: number;
      syncImmediately?: boolean;
      optimisticUpdate?: boolean;
    } = {}
  ): Promise<void> {
    if (!this.db) {
      throw new Error('Database not initialized');
    }

    const timestamp = Date.now();
    const version = await this.getNextVersion(collection, id);

    const item: StorageItem<T> & { id: string; collection: string } = {
      id: `${collection}:${id}`,
      collection,
      data,
      timestamp,
      version,
      ttl: options.ttl,
      syncStatus: this.isOnline ? 'synced' : 'pending',
      syncRetries: 0
    };

    // Store locally
    await this.performTransaction('storage', 'readwrite', (store) => {
      store.put(item);
    });

    // Add to sync queue if needed
    if (!this.isOnline || options.optimisticUpdate) {
      const syncOperation: SyncOperation = {
        id: crypto.randomUUID(),
        type: await this.exists(collection, id) ? 'update' : 'create',
        collection,
        data: { id, ...data },
        localTimestamp: timestamp,
        priority: options.syncImmediately ? 'high' : 'medium'
      };

      await this.addToSyncQueue(syncOperation);
    }

    // Immediate sync if requested and online
    if (options.syncImmediately && this.isOnline) {
      this.performSync();
    }
  }

  async retrieve<T>(collection: string, id: string): Promise<T | null> {
    if (!this.db) {
      throw new Error('Database not initialized');
    }

    const item = await this.performTransaction('storage', 'readonly', (store) => {
      return store.get(`${collection}:${id}`);
    });

    if (!item) {
      return null;
    }

    // Check TTL
    if (item.ttl && Date.now() - item.timestamp > item.ttl) {
      await this.delete(collection, id);
      return null;
    }

    return item.data;
  }

  async query<T>(
    collection: string,
    filter?: {
      limit?: number;
      offset?: number;
      sortBy?: 'timestamp' | 'version';
      sortOrder?: 'asc' | 'desc';
      where?: (item: StorageItem<T>) => boolean;
    }
  ): Promise<T[]> {
    if (!this.db) {
      throw new Error('Database not initialized');
    }

    const items = await this.performTransaction('storage', 'readonly', (store) => {
      const index = store.index('collection');
      return this.getAllFromIndex(index, collection);
    });

    let results = items.filter(item => {
      // Check TTL
      if (item.ttl && Date.now() - item.timestamp > item.ttl) {
        this.delete(collection, item.id.split(':')[1]);
        return false;
      }
      return true;
    });

    // Apply custom filter
    if (filter?.where) {
      results = results.filter(filter.where);
    }

    // Sort
    if (filter?.sortBy) {
      results.sort((a, b) => {
        const aVal = a[filter.sortBy!];
        const bVal = b[filter.sortBy!];
        const order = filter.sortOrder === 'desc' ? -1 : 1;
        return (aVal > bVal ? 1 : -1) * order;
      });
    }

    // Pagination
    const start = filter?.offset || 0;
    const end = filter?.limit ? start + filter.limit : undefined;
    
    return results.slice(start, end).map(item => item.data);
  }

  async delete(collection: string, id: string): Promise<void> {
    if (!this.db) {
      throw new Error('Database not initialized');
    }

    const fullId = `${collection}:${id}`;

    // Remove from local storage
    await this.performTransaction('storage', 'readwrite', (store) => {
      store.delete(fullId);
    });

    // Add deletion to sync queue
    const syncOperation: SyncOperation = {
      id: crypto.randomUUID(),
      type: 'delete',
      collection,
      data: { id },
      localTimestamp: Date.now(),
      priority: 'medium'
    };

    await this.addToSyncQueue(syncOperation);

    if (this.isOnline) {
      this.performSync();
    }
  }

  private async addToSyncQueue(operation: SyncOperation): Promise<void> {
    if (!this.db) return;

    this.syncQueue.push(operation);

    await this.performTransaction('syncQueue', 'readwrite', (store) => {
      store.put(operation);
    });
  }

  private async loadSyncQueue(): Promise<void> {
    if (!this.db) return;

    this.syncQueue = await this.performTransaction('syncQueue', 'readonly', (store) => {
      return this.getAllFromStore(store);
    });
  }

  private setupOnlineListener(): void {
    window.addEventListener('online', () => {
      this.isOnline = true;
      console.log('App came online, starting sync...');
      this.performSync();
    });

    window.addEventListener('offline', () => {
      this.isOnline = false;
      console.log('App went offline');
    });
  }

  private startPeriodicSync(): void {
    setInterval(() => {
      if (this.isOnline && !this.syncInProgress && this.syncQueue.length > 0) {
        this.performSync();
      }
    }, 30000); // Sync every 30 seconds when online
  }

  private async performSync(): Promise<void> {
    if (this.syncInProgress || !this.isOnline || this.syncQueue.length === 0) {
      return;
    }

    this.syncInProgress = true;
    console.log(`Starting sync of ${this.syncQueue.length} operations...`);

    // Sort by priority and timestamp
    const sortedQueue = this.syncQueue.sort((a, b) => {
      const priorityOrder = { high: 0, medium: 1, low: 2 };
      const priorityDiff = priorityOrder[a.priority] - priorityOrder[b.priority];
      
      if (priorityDiff !== 0) return priorityDiff;
      return a.localTimestamp - b.localTimestamp;
    });

    const results = await Promise.allSettled(
      sortedQueue.map(operation => this.syncOperation(operation))
    );

    // Remove successful operations from queue
    const successfulIds = results
      .map((result, index) => ({ result, operation: sortedQueue[index] }))
      .filter(({ result }) => result.status === 'fulfilled')
      .map(({ operation }) => operation.id);

    this.syncQueue = this.syncQueue.filter(op => !successfulIds.includes(op.id));

    // Update IndexedDB sync queue
    await this.performTransaction('syncQueue', 'readwrite', (store) => {
      successfulIds.forEach(id => store.delete(id));
    });

    console.log(`Sync completed. ${successfulIds.length} operations synced successfully.`);
    this.syncInProgress = false;
  }

  private async syncOperation(operation: SyncOperation): Promise<void> {
    const { type, collection, data } = operation;
    
    try {
      let response: Response;
      
      switch (type) {
        case 'create':
          response = await fetch(`/api/${collection}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });
          break;
          
        case 'update':
          response = await fetch(`/api/${collection}/${data.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });
          break;
          
        case 'delete':
          response = await fetch(`/api/${collection}/${data.id}`, {
            method: 'DELETE'
          });
          break;
          
        default:
          throw new Error(`Unknown sync operation type: ${type}`);
      }

      if (!response.ok) {
        throw new Error(`Sync failed: ${response.status} ${response.statusText}`);
      }

      // Update local item sync status
      if (type !== 'delete') {
        await this.updateSyncStatus(collection, data.id, 'synced');
      }

    } catch (error) {
      console.error(`Sync operation failed:`, operation, error);
      
      // Mark as failed and increment retry count
      await this.updateSyncStatus(collection, data.id, 'failed');
      throw error;
    }
  }

  private async updateSyncStatus(
    collection: string, 
    id: string, 
    status: StorageItem['syncStatus']
  ): Promise<void> {
    if (!this.db) return;

    await this.performTransaction('storage', 'readwrite', (store) => {
      const request = store.get(`${collection}:${id}`);
      request.onsuccess = () => {
        const item = request.result;
        if (item) {
          item.syncStatus = status;
          item.lastSyncAttempt = Date.now();
          if (status === 'failed') {
            item.syncRetries++;
          }
          store.put(item);
        }
      };
    });
  }

  private async performTransaction<T>(
    storeName: string,
    mode: IDBTransactionMode,
    operation: (store: IDBObjectStore) => IDBRequest<T> | T | void
  ): Promise<T> {
    if (!this.db) {
      throw new Error('Database not initialized');
    }

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(storeName, mode);
      const store = transaction.objectStore(storeName);

      transaction.onerror = () => reject(transaction.error);
      transaction.oncomplete = () => resolve(result);

      let result: T;
      const request = operation(store);

      if (request && typeof request === 'object' && 'onsuccess' in request) {
        request.onsuccess = () => {
          result = request.result;
        };
        request.onerror = () => reject(request.error);
      } else {
        result = request as T;
      }
    });
  }

  private async getAllFromStore<T>(store: IDBObjectStore): Promise<T[]> {
    return new Promise((resolve, reject) => {
      const request = store.getAll();
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  private async getAllFromIndex<T>(index: IDBIndex, query: string): Promise<T[]> {
    return new Promise((resolve, reject) => {
      const request = index.getAll(query);
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  private async exists(collection: string, id: string): Promise<boolean> {
    const item = await this.retrieve(collection, id);
    return item !== null;
  }

  private async getNextVersion(collection: string, id: string): Promise<number> {
    const current = await this.retrieve(collection, id);
    return current ? (current as any).version + 1 : 1;
  }

  // Public methods for monitoring sync status
  getSyncStatus(): {
    isOnline: boolean;
    syncInProgress: boolean;
    queueLength: number;
    lastSyncAttempt?: number;
  } {
    return {
      isOnline: this.isOnline,
      syncInProgress: this.syncInProgress,
      queueLength: this.syncQueue.length,
      lastSyncAttempt: this.syncQueue.reduce(
        (latest, op) => Math.max(latest, op.localTimestamp),
        0
      )
    };
  }

  async clearExpiredData(): Promise<number> {
    if (!this.db) return 0;

    const now = Date.now();
    let deletedCount = 0;

    await this.performTransaction('storage', 'readwrite', (store) => {
      const request = store.openCursor();
      request.onsuccess = (event) => {
        const cursor = (event.target as IDBRequest).result;
        if (cursor) {
          const item = cursor.value;
          if (item.ttl && now - item.timestamp > item.ttl) {
            cursor.delete();
            deletedCount++;
          }
          cursor.continue();
        }
      };
    });

    console.log(`Cleared ${deletedCount} expired items`);
    return deletedCount;
  }

  async getStorageUsage(): Promise<{
    itemCount: number;
    estimatedSize: number;
    collections: Record<string, number>;
  }> {
    if (!this.db) {
      return { itemCount: 0, estimatedSize: 0, collections: {} };
    }

    const items = await this.performTransaction('storage', 'readonly', (store) => {
      return this.getAllFromStore(store);
    });

    const collections: Record<string, number> = {};
    let estimatedSize = 0;

    items.forEach(item => {
      collections[item.collection] = (collections[item.collection] || 0) + 1;
      estimatedSize += JSON.stringify(item).length;
    });

    return {
      itemCount: items.length,
      estimatedSize,
      collections
    };
  }
}
```

**Step 2.2: Push Notifications and Background Sync**

```typescript
// Advanced Push Notifications and Background Sync
// File: src/utils/push-notifications.ts

interface NotificationOptions {
  title: string;
  body: string;
  icon?: string;
  badge?: string;
  image?: string;
  data?: any;
  actions?: NotificationAction[];
  silent?: boolean;
  requireInteraction?: boolean;
  tag?: string;
  renotify?: boolean;
  vibrate?: number[];
  sound?: string;
  dir?: 'auto' | 'ltr' | 'rtl';
  lang?: string;
  timestamp?: number;
}

interface NotificationAction {
  action: string;
  title: string;
  icon?: string;
}

interface PushSubscriptionInfo {
  endpoint: string;
  keys: {
    p256dh: string;
    auth: string;
  };
  userId?: string;
  topics?: string[];
}

export class PushNotificationManager {
  private registration: ServiceWorkerRegistration | null = null;
  private subscription: PushSubscription | null = null;
  private vapidPublicKey: string;
  private serverEndpoint: string;

  constructor(
    vapidPublicKey: string,
    serverEndpoint = '/api/push/subscribe'
  ) {
    this.vapidPublicKey = vapidPublicKey;
    this.serverEndpoint = serverEndpoint;
    this.initializeManager();
  }

  private async initializeManager(): Promise<void> {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
      this.registration = await navigator.serviceWorker.ready;
      await this.checkExistingSubscription();
      this.setupNotificationClickHandler();
    }
  }

  private async checkExistingSubscription(): Promise<void> {
    if (!this.registration) return;

    this.subscription = await this.registration.pushManager.getSubscription();
    
    if (this.subscription) {
      console.log('Existing push subscription found');
      await this.updateSubscriptionOnServer();
    }
  }

  async requestPermission(): Promise<NotificationPermission> {
    if (!('Notification' in window)) {
      throw new Error('Notifications not supported');
    }

    const permission = await Notification.requestPermission();
    
    if (permission === 'granted') {
      console.log('Notification permission granted');
    } else if (permission === 'denied') {
      console.log('Notification permission denied');
    } else {
      console.log('Notification permission dismissed');
    }

    return permission;
  }

  async subscribe(options: {
    userId?: string;
    topics?: string[];
    userVisibleOnly?: boolean;
  } = {}): Promise<PushSubscription> {
    if (!this.registration) {
      throw new Error('Service Worker not ready');
    }

    // Request permission if not granted
    const permission = await this.requestPermission();
    if (permission !== 'granted') {
      throw new Error('Notification permission not granted');
    }

    try {
      this.subscription = await this.registration.pushManager.subscribe({
        userVisibleOnly: options.userVisibleOnly !== false,
        applicationServerKey: this.urlBase64ToUint8Array(this.vapidPublicKey)
      });

      console.log('Push subscription created:', this.subscription);

      // Send subscription to server
      await this.sendSubscriptionToServer({
        ...this.subscription.toJSON(),
        userId: options.userId,
        topics: options.topics
      } as PushSubscriptionInfo);

      // Store subscription locally
      localStorage.setItem('pushSubscription', JSON.stringify({
        subscription: this.subscription.toJSON(),
        timestamp: Date.now(),
        userId: options.userId,
        topics: options.topics
      }));

      return this.subscription;
    } catch (error) {
      console.error('Failed to subscribe to push notifications:', error);
      throw error;
    }
  }

  async unsubscribe(): Promise<boolean> {
    if (!this.subscription) {
      return true;
    }

    try {
      const result = await this.subscription.unsubscribe();
      
      if (result) {
        // Remove from server
        await this.removeSubscriptionFromServer();
        
        // Clear local storage
        localStorage.removeItem('pushSubscription');
        
        this.subscription = null;
        console.log('Push subscription removed');
      }

      return result;
    } catch (error) {
      console.error('Failed to unsubscribe from push notifications:', error);
      return false;
    }
  }

  async showLocalNotification(options: NotificationOptions): Promise<void> {
    if (!this.registration) {
      throw new Error('Service Worker not ready');
    }

    const permission = await this.requestPermission();
    if (permission !== 'granted') {
      throw new Error('Notification permission not granted');
    }

    const notificationOptions: NotificationOptions = {
      icon: '/icon-192x192.png',
      badge: '/badge-72x72.png',
      vibrate: [200, 100, 200],
      timestamp: Date.now(),
      ...options
    };

    await this.registration.showNotification(options.title, notificationOptions);
  }

  async scheduleNotification(
    options: NotificationOptions,
    scheduledTime: Date
  ): Promise<void> {
    const delay = scheduledTime.getTime() - Date.now();
    
    if (delay <= 0) {
      return this.showLocalNotification(options);
    }

    // Store scheduled notification
    const scheduledNotifications = this.getScheduledNotifications();
    const notification = {
      id: crypto.randomUUID(),
      options,
      scheduledTime: scheduledTime.getTime()
    };

    scheduledNotifications.push(notification);
    localStorage.setItem('scheduledNotifications', JSON.stringify(scheduledNotifications));

    // Set timeout for notification
    setTimeout(() => {
      this.showLocalNotification(options);
      this.removeScheduledNotification(notification.id);
    }, delay);
  }

  private getScheduledNotifications(): Array<{
    id: string;
    options: NotificationOptions;
    scheduledTime: number;
  }> {
    const stored = localStorage.getItem('scheduledNotifications');
    return stored ? JSON.parse(stored) : [];
  }

  private removeScheduledNotification(id: string): void {
    const scheduled = this.getScheduledNotifications();
    const filtered = scheduled.filter(n => n.id !== id);
    localStorage.setItem('scheduledNotifications', JSON.stringify(filtered));
  }

  private setupNotificationClickHandler(): void {
    navigator.serviceWorker.addEventListener('message', (event) => {
      if (event.data.type === 'NOTIFICATION_CLICK') {
        this.handleNotificationClick(event.data);
      }
    });
  }

  private handleNotificationClick(data: {
    action?: string;
    notification: any;
  }): void {
    const { action, notification } = data;
    
    if (action === 'reply' && notification.data?.conversationId) {
      // Handle reply action
      this.handleReplyAction(notification.data.conversationId);
    } else if (action === 'view' && notification.data?.url) {
      // Handle view action
      window.open(notification.data.url, '_blank');
    } else {
      // Default action - focus app
      window.focus();
    }
  }

  private async handleReplyAction(conversationId: string): Promise<void> {
    // Open reply interface or focus existing one
    console.log('Opening reply for conversation:', conversationId);
    // Implementation depends on your app structure
  }

  private async sendSubscriptionToServer(
    subscriptionInfo: PushSubscriptionInfo
  ): Promise<void> {
    try {
      const response = await fetch(this.serverEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(subscriptionInfo)
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      console.log('Subscription sent to server successfully');
    } catch (error) {
      console.error('Failed to send subscription to server:', error);
      throw error;
    }
  }

  private async updateSubscriptionOnServer(): Promise<void> {
    if (!this.subscription) return;

    const stored = localStorage.getItem('pushSubscription');
    const storedData = stored ? JSON.parse(stored) : {};

    const subscriptionInfo: PushSubscriptionInfo = {
      ...this.subscription.toJSON(),
      userId: storedData.userId,
      topics: storedData.topics
    } as PushSubscriptionInfo;

    await this.sendSubscriptionToServer(subscriptionInfo);
  }

  private async removeSubscriptionFromServer(): Promise<void> {
    if (!this.subscription) return;

    try {
      const response = await fetch(`${this.serverEndpoint}/unsubscribe`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          endpoint: this.subscription.endpoint
        })
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      console.log('Subscription removed from server');
    } catch (error) {
      console.error('Failed to remove subscription from server:', error);
    }
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

  getSubscriptionStatus(): {
    isSupported: boolean;
    permission: NotificationPermission;
    isSubscribed: boolean;
    subscription: PushSubscription | null;
  } {
    return {
      isSupported: 'PushManager' in window && 'serviceWorker' in navigator,
      permission: Notification.permission,
      isSubscribed: !!this.subscription,
      subscription: this.subscription
    };
  }

  async updateTopics(topics: string[]): Promise<void> {
    if (!this.subscription) {
      throw new Error('No active subscription');
    }

    const stored = localStorage.getItem('pushSubscription');
    const storedData = stored ? JSON.parse(stored) : {};

    const updatedData = {
      ...storedData,
      topics,
      timestamp: Date.now()
    };

    localStorage.setItem('pushSubscription', JSON.stringify(updatedData));

    // Update on server
    const subscriptionInfo: PushSubscriptionInfo = {
      ...this.subscription.toJSON(),
      userId: storedData.userId,
      topics
    } as PushSubscriptionInfo;

    await this.sendSubscriptionToServer(subscriptionInfo);
  }
}

// Background Sync Manager
export class BackgroundSyncManager {
  private registration: ServiceWorkerRegistration | null = null;
  private syncTags = new Set<string>();

  constructor() {
    this.initializeManager();
  }

  private async initializeManager(): Promise<void> {
    if ('serviceWorker' in navigator && 'sync' in window.ServiceWorkerRegistration.prototype) {
      this.registration = await navigator.serviceWorker.ready;
      console.log('Background Sync initialized');
    }
  }

  async registerSync(tag: string, data?: any): Promise<void> {
    if (!this.registration) {
      throw new Error('Background sync not supported or service worker not ready');
    }

    try {
      await this.registration.sync.register(tag);
      this.syncTags.add(tag);
      
      // Store sync data if provided
      if (data) {
        const syncData = this.getSyncData();
        syncData[tag] = data;
        localStorage.setItem('backgroundSyncData', JSON.stringify(syncData));
      }

      console.log(`Background sync registered for tag: ${tag}`);
    } catch (error) {
      console.error('Failed to register background sync:', error);
      throw error;
    }
  }

  async getSyncTags(): Promise<string[]> {
    if (!this.registration) {
      return [];
    }

    try {
      return Array.from(await this.registration.sync.getTags());
    } catch (error) {
      console.error('Failed to get sync tags:', error);
      return [];
    }
  }

  private getSyncData(): Record<string, any> {
    const stored = localStorage.getItem('backgroundSyncData');
    return stored ? JSON.parse(stored) : {};
  }

  isSupported(): boolean {
    return 'serviceWorker' in navigator && 'sync' in window.ServiceWorkerRegistration.prototype;
  }

  getSyncStatus(): {
    isSupported: boolean;
    isReady: boolean;
    registeredTags: string[];
  } {
    return {
      isSupported: this.isSupported(),
      isReady: !!this.registration,
      registeredTags: Array.from(this.syncTags)
    };
  }
}
```

### Phase 3: Native Features Integration and Performance Optimization (3-4 hours)

**Step 3.1: Advanced Native Features Integration**

```typescript
// Advanced Native Features Integration
// File: src/utils/native-features.ts

interface DeviceCapabilities {
  camera: boolean;
  microphone: boolean;
  geolocation: boolean;
  deviceMotion: boolean;
  deviceOrientation: boolean;
  ambientLight: boolean;
  proximity: boolean;
  battery: boolean;
  bluetooth: boolean;
  usb: boolean;
  nfc: boolean;
  wakeLock: boolean;
  clipboard: boolean;
  share: boolean;
  fileSystem: boolean;
  contacts: boolean;
  payment: boolean;
}

export class NativeFeaturesManager {
  private capabilities: Partial<DeviceCapabilities> = {};
  private wakeLock: WakeLockSentinel | null = null;
  private mediaStream: MediaStream | null = null;
  private geolocationWatcher: number | null = null;

  constructor() {
    this.detectCapabilities();
  }

  private async detectCapabilities(): Promise<void> {
    this.capabilities = {
      camera: 'mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices,
      microphone: 'mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices,
      geolocation: 'geolocation' in navigator,
      deviceMotion: 'DeviceMotionEvent' in window,
      deviceOrientation: 'DeviceOrientationEvent' in window,
      ambientLight: 'AmbientLightSensor' in window,
      proximity: 'ProximitySensor' in window,
      battery: 'getBattery' in navigator,
      bluetooth: 'bluetooth' in navigator,
      usb: 'usb' in navigator,
      nfc: 'nfc' in navigator,
      wakeLock: 'wakeLock' in navigator,
      clipboard: 'clipboard' in navigator,
      share: 'share' in navigator,
      fileSystem: 'showDirectoryPicker' in window,
      contacts: 'contacts' in navigator,
      payment: 'PaymentRequest' in window
    };
  }

  // Camera and Media Access
  async accessCamera(
    options: MediaStreamConstraints = { video: true, audio: false }
  ): Promise<MediaStream> {
    if (!this.capabilities.camera) {
      throw new Error('Camera not supported');
    }

    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia(options);
      return this.mediaStream;
    } catch (error) {
      console.error('Camera access denied:', error);
      throw new Error('Camera access denied');
    }
  }

  async takePicture(): Promise<Blob> {
    if (!this.mediaStream) {
      throw new Error('Camera not active');
    }

    const video = document.createElement('video');
    video.srcObject = this.mediaStream;
    video.play();

    await new Promise(resolve => {
      video.onloadedmetadata = resolve;
    });

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    const ctx = canvas.getContext('2d')!;
    ctx.drawImage(video, 0, 0);

    return new Promise(resolve => {
      canvas.toBlob(resolve!, 'image/jpeg', 0.9);
    });
  }

  stopCamera(): void {
    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach(track => track.stop());
      this.mediaStream = null;
    }
  }

  // Geolocation
  async getCurrentLocation(
    options: PositionOptions = {}
  ): Promise<GeolocationPosition> {
    if (!this.capabilities.geolocation) {
      throw new Error('Geolocation not supported');
    }

    return new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 300000, // 5 minutes
        ...options
      });
    });
  }

  watchLocation(
    callback: (position: GeolocationPosition) => void,
    errorCallback?: (error: GeolocationPositionError) => void,
    options: PositionOptions = {}
  ): number {
    if (!this.capabilities.geolocation) {
      throw new Error('Geolocation not supported');
    }

    this.geolocationWatcher = navigator.geolocation.watchPosition(
      callback,
      errorCallback,
      {
        enableHighAccuracy: true,
        timeout: 30000,
        maximumAge: 60000, // 1 minute
        ...options
      }
    );

    return this.geolocationWatcher;
  }

  stopWatchingLocation(): void {
    if (this.geolocationWatcher) {
      navigator.geolocation.clearWatch(this.geolocationWatcher);
      this.geolocationWatcher = null;
    }
  }

  // Device Orientation and Motion
  async requestMotionPermission(): Promise<boolean> {
    if ('DeviceMotionEvent' in window && 'requestPermission' in DeviceMotionEvent) {
      const permission = await (DeviceMotionEvent as any).requestPermission();
      return permission === 'granted';
    }
    return this.capabilities.deviceMotion || false;
  }

  startMotionTracking(
    callback: (event: DeviceMotionEvent) => void
  ): () => void {
    if (!this.capabilities.deviceMotion) {
      throw new Error('Device motion not supported');
    }

    window.addEventListener('devicemotion', callback);
    
    return () => {
      window.removeEventListener('devicemotion', callback);
    };
  }

  startOrientationTracking(
    callback: (event: DeviceOrientationEvent) => void
  ): () => void {
    if (!this.capabilities.deviceOrientation) {
      throw new Error('Device orientation not supported');
    }

    window.addEventListener('deviceorientation', callback);
    
    return () => {
      window.removeEventListener('deviceorientation', callback);
    };
  }

  // Wake Lock
  async requestWakeLock(): Promise<void> {
    if (!this.capabilities.wakeLock) {
      throw new Error('Wake lock not supported');
    }

    try {
      this.wakeLock = await (navigator as any).wakeLock.request('screen');
      
      this.wakeLock.addEventListener('release', () => {
        console.log('Wake lock released');
        this.wakeLock = null;
      });

      console.log('Wake lock acquired');
    } catch (error) {
      console.error('Wake lock failed:', error);
      throw error;
    }
  }

  async releaseWakeLock(): Promise<void> {
    if (this.wakeLock) {
      await this.wakeLock.release();
      this.wakeLock = null;
    }
  }

  // Clipboard
  async writeToClipboard(text: string): Promise<void> {
    if (!this.capabilities.clipboard) {
      // Fallback for older browsers
      const textArea = document.createElement('textarea');
      textArea.value = text;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
      return;
    }

    try {
      await navigator.clipboard.writeText(text);
    } catch (error) {
      console.error('Clipboard write failed:', error);
      throw error;
    }
  }

  async readFromClipboard(): Promise<string> {
    if (!this.capabilities.clipboard) {
      throw new Error('Clipboard read not supported');
    }

    try {
      return await navigator.clipboard.readText();
    } catch (error) {
      console.error('Clipboard read failed:', error);
      throw error;
    }
  }

  // Web Share API
  async shareContent(data: {
    title?: string;
    text?: string;
    url?: string;
    files?: File[];
  }): Promise<void> {
    if (!this.capabilities.share) {
      // Fallback to clipboard
      const shareText = `${data.title || ''}\n${data.text || ''}\n${data.url || ''}`.trim();
      await this.writeToClipboard(shareText);
      throw new Error('Share not supported, content copied to clipboard');
    }

    try {
      await navigator.share(data);
    } catch (error) {
      if ((error as Error).name === 'AbortError') {
        console.log('Share cancelled');
      } else {
        console.error('Share failed:', error);
        throw error;
      }
    }
  }

  // File System Access
  async openFileDialog(
    options: {
      types?: Array<{
        description: string;
        accept: Record<string, string[]>;
      }>;
      multiple?: boolean;
    } = {}
  ): Promise<FileSystemFileHandle[]> {
    if (!this.capabilities.fileSystem) {
      // Fallback to input element
      return new Promise((resolve, reject) => {
        const input = document.createElement('input');
        input.type = 'file';
        input.multiple = options.multiple || false;
        
        if (options.types) {
          const accept = options.types.flatMap(type => 
            Object.values(type.accept).flat()
          ).join(',');
          input.accept = accept;
        }
        
        input.onchange = () => {
          if (input.files) {
            // Convert File objects to mock FileSystemFileHandle
            const handles = Array.from(input.files).map(file => ({
              name: file.name,
              getFile: async () => file
            }));
            resolve(handles as any);
          } else {
            reject(new Error('No files selected'));
          }
        };
        
        input.click();
      });
    }

    try {
      return await (window as any).showOpenFilePicker(options);
    } catch (error) {
      if ((error as Error).name === 'AbortError') {
        console.log('File selection cancelled');
        return [];
      }
      throw error;
    }
  }

  async saveFile(
    content: string | Blob,
    filename: string,
    options: {
      types?: Array<{
        description: string;
        accept: Record<string, string[]>;
      }>;
    } = {}
  ): Promise<void> {
    if (!this.capabilities.fileSystem) {
      // Fallback to download
      const blob = typeof content === 'string' 
        ? new Blob([content], { type: 'text/plain' })
        : content;
      
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.click();
      URL.revokeObjectURL(url);
      return;
    }

    try {
      const handle = await (window as any).showSaveFilePicker({
        suggestedName: filename,
        ...options
      });
      
      const writable = await handle.createWritable();
      await writable.write(content);
      await writable.close();
    } catch (error) {
      if ((error as Error).name === 'AbortError') {
        console.log('Save cancelled');
      } else {
        throw error;
      }
    }
  }

  // Battery API
  async getBatteryInfo(): Promise<{
    level: number;
    charging: boolean;
    chargingTime: number;
    dischargingTime: number;
  } | null> {
    if (!this.capabilities.battery) {
      return null;
    }

    try {
      const battery = await (navigator as any).getBattery();
      return {
        level: battery.level,
        charging: battery.charging,
        chargingTime: battery.chargingTime,
        dischargingTime: battery.dischargingTime
      };
    } catch (error) {
      console.error('Battery API failed:', error);
      return null;
    }
  }

  // Payment Request API
  async requestPayment(
    methodData: PaymentMethodData[],
    details: PaymentDetailsInit,
    options?: PaymentOptions
  ): Promise<PaymentResponse> {
    if (!this.capabilities.payment) {
      throw new Error('Payment Request API not supported');
    }

    const request = new PaymentRequest(methodData, details, options);
    
    try {
      const response = await request.show();
      return response;
    } catch (error) {
      console.error('Payment request failed:', error);
      throw error;
    }
  }

  // Web Bluetooth (experimental)
  async connectBluetoothDevice(
    options: RequestDeviceOptions = {}
  ): Promise<BluetoothDevice> {
    if (!this.capabilities.bluetooth) {
      throw new Error('Web Bluetooth not supported');
    }

    try {
      const device = await (navigator as any).bluetooth.requestDevice(options);
      return device;
    } catch (error) {
      console.error('Bluetooth connection failed:', error);
      throw error;
    }
  }

  getCapabilities(): Partial<DeviceCapabilities> {
    return { ...this.capabilities };
  }

  cleanup(): void {
    this.stopCamera();
    this.stopWatchingLocation();
    this.releaseWakeLock();
  }
}

// PWA Installation and Update Manager
export class PWAUpdateManager {
  private registration: ServiceWorkerRegistration | null = null;
  private updateAvailable = false;
  private updateCheckInterval: number | null = null;

  constructor() {
    this.initialize();
  }

  private async initialize(): Promise<void> {
    if ('serviceWorker' in navigator) {
      this.registration = await navigator.serviceWorker.ready;
      this.setupUpdateDetection();
      this.startUpdateChecking();
    }
  }

  private setupUpdateDetection(): void {
    if (!this.registration) return;

    this.registration.addEventListener('updatefound', () => {
      const newWorker = this.registration!.installing;
      
      if (newWorker) {
        newWorker.addEventListener('statechange', () => {
          if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
            this.updateAvailable = true;
            this.notifyUpdateAvailable();
          }
        });
      }
    });

    // Listen for messages from service worker
    navigator.serviceWorker.addEventListener('message', (event) => {
      if (event.data && event.data.type === 'NEW_VERSION_AVAILABLE') {
        this.updateAvailable = true;
        this.notifyUpdateAvailable();
      }
    });
  }

  private startUpdateChecking(): void {
    // Check for updates every 30 minutes
    this.updateCheckInterval = window.setInterval(() => {
      this.checkForUpdates();
    }, 30 * 60 * 1000);

    // Check immediately
    this.checkForUpdates();
  }

  async checkForUpdates(): Promise<boolean> {
    if (!this.registration) {
      return false;
    }

    try {
      await this.registration.update();
      return this.updateAvailable;
    } catch (error) {
      console.error('Update check failed:', error);
      return false;
    }
  }

  async applyUpdate(): Promise<void> {
    if (!this.registration?.waiting) {
      throw new Error('No update available');
    }

    // Tell the waiting service worker to skip waiting
    this.registration.waiting.postMessage({ type: 'SKIP_WAITING' });

    // Reload the page when the new service worker takes control
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      window.location.reload();
    });
  }

  private notifyUpdateAvailable(): void {
    // Dispatch custom event for app to handle
    window.dispatchEvent(new CustomEvent('pwa-update-available', {
      detail: { updateAvailable: true }
    }));

    // Show notification
    this.showUpdateNotification();
  }

  private showUpdateNotification(): void {
    // Create update notification UI
    const notification = document.createElement('div');
    notification.className = 'pwa-update-notification';
    notification.innerHTML = `
      <div class="update-content">
        <span>🚀 New version available!</span>
        <div class="update-actions">
          <button id="update-now">Update Now</button>
          <button id="update-later">Later</button>
        </div>
      </div>
    `;

    document.body.appendChild(notification);

    // Handle user actions
    notification.querySelector('#update-now')?.addEventListener('click', () => {
      this.applyUpdate();
      notification.remove();
    });

    notification.querySelector('#update-later')?.addEventListener('click', () => {
      notification.remove();
    });

    // Auto-remove after 30 seconds
    setTimeout(() => {
      if (notification.parentNode) {
        notification.remove();
      }
    }, 30000);
  }

  getUpdateStatus(): {
    updateAvailable: boolean;
    registration: ServiceWorkerRegistration | null;
    isChecking: boolean;
  } {
    return {
      updateAvailable: this.updateAvailable,
      registration: this.registration,
      isChecking: !!this.updateCheckInterval
    };
  }

  stopUpdateChecking(): void {
    if (this.updateCheckInterval) {
      clearInterval(this.updateCheckInterval);
      this.updateCheckInterval = null;
    }
  }

  cleanup(): void {
    this.stopUpdateChecking();
  }
}
```

## 📊 Success Criteria

### PWA Performance Metrics
- **Lighthouse PWA Score**: >90/100 across all audits
- **First Load Performance**: <3s on 3G networks
- **Offline Functionality**: 100% critical features work offline
- **Installation Rate**: >25% of repeat visitors install the app

### Native Features Integration
- **Device API Coverage**: >80% of available APIs utilized appropriately
- **Permission Handling**: Graceful fallbacks for all permission scenarios
- **Cross-platform Compatibility**: Consistent experience across iOS, Android, and Desktop
- **Battery Impact**: <5% additional battery drain from PWA features

### User Experience Metrics
- **App-like Feel**: Native-like navigation and interactions
- **Engagement**: >40% increase in user engagement post-installation
- **Retention**: >60% 30-day retention for installed users
- **Push Notification Engagement**: >20% click-through rate

## 🎯 Deliverables

Upon completion of comprehensive Progressive Web App development:

- ✅ **Advanced Service Worker** with sophisticated caching strategies and background sync
- ✅ **PWA Manifest** with comprehensive app configuration and installation prompts
- ✅ **Offline Storage System** with IndexedDB integration and conflict resolution
- ✅ **Push Notifications** with advanced targeting and interactive actions
- ✅ **Native Features Integration** with device APIs and graceful fallbacks
- ✅ **Update Management** with automatic updates and user-controlled deployment
- ✅ **Performance Optimization** with resource preloading and critical path optimization
- ✅ **Cross-platform Compatibility** ensuring consistent experience across all devices
- ✅ **Analytics Integration** with installation and engagement tracking

---

*This comprehensive Progressive Web App development approach delivers native-like experiences with advanced offline capabilities, push notifications, and seamless integration with device features across all platforms.*