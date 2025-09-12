# Web Accessibility and Inclusive Design

**Agent Type: frontend-engineer**
**Complexity Level: Expert**
**Estimated Duration: 6-10 hours**

---

## 🎯 Mission

Design and implement comprehensive web accessibility solutions following WCAG 2.1 guidelines, creating inclusive user experiences that work for all users regardless of their abilities, technologies, or circumstances, while ensuring legal compliance and exceptional usability.

## 📋 Process Framework

### Phase 1: Accessibility Foundation and WCAG Implementation (2-3 hours)

**Step 1.1: Comprehensive Accessibility Architecture**

```typescript
// Advanced Accessibility Architecture Framework
// File: src/utils/accessibility.ts

interface AccessibilityConfig {
  wcagLevel: 'A' | 'AA' | 'AAA';
  colorContrastRatio: 4.5 | 7.1;
  fontSize: {
    minimum: number;
    scalable: boolean;
    maxScale: number;
  };
  reducedMotion: boolean;
  highContrast: boolean;
  screenReader: boolean;
  keyboard: boolean;
  touch: boolean;
}

interface ContrastRatio {
  ratio: number;
  passes: {
    aa: boolean;
    aaa: boolean;
    aaLarge: boolean;
    aaaLarge: boolean;
  };
}

interface AccessibilityAudit {
  violations: AccessibilityViolation[];
  warnings: AccessibilityWarning[];
  passes: AccessibilityPass[];
  score: number;
  wcagLevel: string;
}

interface AccessibilityViolation {
  id: string;
  impact: 'minor' | 'moderate' | 'serious' | 'critical';
  description: string;
  help: string;
  helpUrl: string;
  nodes: Array<{
    html: string;
    target: string;
    failureSummary: string;
  }>;
}

export class AccessibilityManager {
  private config: AccessibilityConfig;
  private ariaAnnouncer: AriaLiveAnnouncer;
  private focusManager: FocusManager;
  private colorAnalyzer: ColorContrastAnalyzer;
  private keyboardNavigation: KeyboardNavigationManager;

  constructor(config: Partial<AccessibilityConfig> = {}) {
    this.config = {
      wcagLevel: 'AA',
      colorContrastRatio: 4.5,
      fontSize: {
        minimum: 16,
        scalable: true,
        maxScale: 200
      },
      reducedMotion: true,
      highContrast: true,
      screenReader: true,
      keyboard: true,
      touch: true,
      ...config
    };

    this.ariaAnnouncer = new AriaLiveAnnouncer();
    this.focusManager = new FocusManager();
    this.colorAnalyzer = new ColorContrastAnalyzer();
    this.keyboardNavigation = new KeyboardNavigationManager();

    this.initialize();
  }

  private initialize(): void {
    this.setupAccessibilityPreferences();
    this.injectAccessibilityStyles();
    this.setupKeyboardNavigation();
    this.setupFocusManagement();
    this.setupScreenReaderSupport();
    this.monitorAccessibilityViolations();
  }

  private setupAccessibilityPreferences(): void {
    // Detect user preferences from system settings
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const prefersHighContrast = window.matchMedia('(prefers-contrast: high)');
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)');

    this.handleReducedMotion(prefersReducedMotion.matches);
    this.handleHighContrast(prefersHighContrast.matches);
    this.handleColorScheme(prefersDarkMode.matches);

    // Listen for changes
    prefersReducedMotion.addEventListener('change', (e) => {
      this.handleReducedMotion(e.matches);
    });

    prefersHighContrast.addEventListener('change', (e) => {
      this.handleHighContrast(e.matches);
    });

    prefersDarkMode.addEventListener('change', (e) => {
      this.handleColorScheme(e.matches);
    });
  }

  private injectAccessibilityStyles(): void {
    const style = document.createElement('style');
    style.textContent = `
      /* Focus management */
      .a11y-focus-visible:focus-visible {
        outline: 2px solid #0066cc;
        outline-offset: 2px;
        border-radius: 2px;
      }

      /* Skip links */
      .a11y-skip-link {
        position: absolute;
        top: -40px;
        left: 6px;
        background: #000;
        color: #fff;
        padding: 8px;
        text-decoration: none;
        border-radius: 0 0 4px 4px;
        z-index: 10000;
        transition: top 0.2s;
      }

      .a11y-skip-link:focus {
        top: 0;
      }

      /* Screen reader only content */
      .a11y-sr-only {
        position: absolute !important;
        width: 1px !important;
        height: 1px !important;
        padding: 0 !important;
        margin: -1px !important;
        overflow: hidden !important;
        clip: rect(0, 0, 0, 0) !important;
        white-space: nowrap !important;
        border: 0 !important;
        clip-path: inset(50%) !important;
      }

      /* High contrast mode */
      @media (prefers-contrast: high) {
        * {
          border-color: CanvasText !important;
        }
        
        button, input, select, textarea {
          background: Canvas !important;
          color: CanvasText !important;
          border: 2px solid CanvasText !important;
        }
        
        a {
          color: LinkText !important;
        }
      }

      /* Reduced motion */
      @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
          animation-duration: 0.01ms !important;
          animation-iteration-count: 1 !important;
          transition-duration: 0.01ms !important;
          scroll-behavior: auto !important;
        }
      }

      /* Large text support */
      @media (min-resolution: 192dpi) {
        .a11y-large-text {
          font-size: 1.125em;
          line-height: 1.6;
        }
      }

      /* Touch target minimum size */
      .a11y-touch-target {
        min-width: 44px;
        min-height: 44px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }

      /* Color blind friendly patterns */
      .a11y-pattern-stripes {
        background-image: repeating-linear-gradient(
          45deg,
          transparent,
          transparent 2px,
          currentColor 2px,
          currentColor 4px
        );
      }

      .a11y-pattern-dots {
        background-image: radial-gradient(circle, currentColor 1px, transparent 1px);
        background-size: 8px 8px;
      }
    `;

    document.head.appendChild(style);
  }

  private setupKeyboardNavigation(): void {
    this.keyboardNavigation.initialize();
    
    // Add skip links
    this.addSkipLinks();
    
    // Enhance form navigation
    this.enhanceFormNavigation();
    
    // Setup roving tabindex for complex widgets
    this.setupRovingTabindex();
  }

  private addSkipLinks(): void {
    const skipLinks = [
      { href: '#main', text: 'Skip to main content' },
      { href: '#navigation', text: 'Skip to navigation' },
      { href: '#footer', text: 'Skip to footer' }
    ];

    const skipContainer = document.createElement('div');
    skipContainer.setAttribute('aria-label', 'Skip links');
    
    skipLinks.forEach(link => {
      const skipLink = document.createElement('a');
      skipLink.href = link.href;
      skipLink.textContent = link.text;
      skipLink.className = 'a11y-skip-link';
      skipContainer.appendChild(skipLink);
    });

    document.body.insertBefore(skipContainer, document.body.firstChild);
  }

  private enhanceFormNavigation(): void {
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' && event.target instanceof HTMLInputElement) {
        const form = event.target.closest('form');
        if (form) {
          const inputs = Array.from(form.querySelectorAll('input, select, textarea'));
          const currentIndex = inputs.indexOf(event.target);
          const nextInput = inputs[currentIndex + 1] as HTMLElement;
          
          if (nextInput && nextInput !== event.target) {
            event.preventDefault();
            nextInput.focus();
          }
        }
      }
    });
  }

  private setupRovingTabindex(): void {
    // Setup for toolbar patterns, menus, etc.
    const toolbars = document.querySelectorAll('[role="toolbar"]');
    
    toolbars.forEach(toolbar => {
      const items = toolbar.querySelectorAll('[role="button"], button');
      
      if (items.length === 0) return;
      
      // Set initial tabindex
      items.forEach((item, index) => {
        item.setAttribute('tabindex', index === 0 ? '0' : '-1');
      });
      
      // Handle arrow key navigation
      toolbar.addEventListener('keydown', (event) => {
        if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
        
        event.preventDefault();
        const currentIndex = Array.from(items).indexOf(event.target as Element);
        let newIndex = currentIndex;
        
        switch (event.key) {
          case 'ArrowLeft':
            newIndex = currentIndex > 0 ? currentIndex - 1 : items.length - 1;
            break;
          case 'ArrowRight':
            newIndex = currentIndex < items.length - 1 ? currentIndex + 1 : 0;
            break;
          case 'Home':
            newIndex = 0;
            break;
          case 'End':
            newIndex = items.length - 1;
            break;
        }
        
        // Update tabindex and focus
        items.forEach((item, index) => {
          item.setAttribute('tabindex', index === newIndex ? '0' : '-1');
        });
        
        (items[newIndex] as HTMLElement).focus();
      });
    });
  }

  private setupFocusManagement(): void {
    this.focusManager.initialize();
    
    // Handle modal focus trapping
    this.setupModalFocusTrap();
    
    // Manage focus on route changes
    this.setupRouteFocusManagement();
  }

  private setupModalFocusTrap(): void {
    document.addEventListener('keydown', (event) => {
      if (event.key !== 'Tab') return;
      
      const activeModal = document.querySelector('[role="dialog"][aria-hidden="false"]');
      if (!activeModal) return;
      
      const focusableElements = activeModal.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      
      if (focusableElements.length === 0) return;
      
      const firstFocusable = focusableElements[0] as HTMLElement;
      const lastFocusable = focusableElements[focusableElements.length - 1] as HTMLElement;
      
      if (event.shiftKey) {
        if (document.activeElement === firstFocusable) {
          event.preventDefault();
          lastFocusable.focus();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          event.preventDefault();
          firstFocusable.focus();
        }
      }
    });
  }

  private setupRouteFocusManagement(): void {
    // Listen for route changes (adjust based on your router)
    window.addEventListener('popstate', () => {
      this.manageFocusOnRouteChange();
    });
    
    // For single-page applications, you might need to hook into your router
    this.observeRouteChanges();
  }

  private observeRouteChanges(): void {
    let currentPath = window.location.pathname;
    
    const observer = new MutationObserver(() => {
      if (window.location.pathname !== currentPath) {
        currentPath = window.location.pathname;
        this.manageFocusOnRouteChange();
      }
    });
    
    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  private manageFocusOnRouteChange(): void {
    // Focus the main heading or main content area
    const mainHeading = document.querySelector('h1');
    const mainContent = document.querySelector('main, [role="main"]');
    
    const targetElement = mainHeading || mainContent;
    
    if (targetElement) {
      // Make sure it's focusable
      if (!targetElement.getAttribute('tabindex')) {
        targetElement.setAttribute('tabindex', '-1');
      }
      
      (targetElement as HTMLElement).focus();
      
      // Announce the page change to screen readers
      this.ariaAnnouncer.announce(
        `Page changed to ${document.title}`,
        'polite'
      );
    }
  }

  private setupScreenReaderSupport(): void {
    // Dynamic content announcements
    this.setupLiveRegions();
    
    // Form validation announcements
    this.setupFormValidationAnnouncements();
    
    // Progress and status updates
    this.setupProgressAnnouncements();
  }

  private setupLiveRegions(): void {
    // Create live regions if they don't exist
    if (!document.getElementById('aria-live-polite')) {
      const politeRegion = document.createElement('div');
      politeRegion.id = 'aria-live-polite';
      politeRegion.setAttribute('aria-live', 'polite');
      politeRegion.className = 'a11y-sr-only';
      document.body.appendChild(politeRegion);
    }
    
    if (!document.getElementById('aria-live-assertive')) {
      const assertiveRegion = document.createElement('div');
      assertiveRegion.id = 'aria-live-assertive';
      assertiveRegion.setAttribute('aria-live', 'assertive');
      assertiveRegion.className = 'a11y-sr-only';
      document.body.appendChild(assertiveRegion);
    }
  }

  private setupFormValidationAnnouncements(): void {
    document.addEventListener('invalid', (event) => {
      const input = event.target as HTMLInputElement;
      const errorMessage = this.getValidationMessage(input);
      
      this.ariaAnnouncer.announce(
        `Error in ${this.getFieldLabel(input)}: ${errorMessage}`,
        'assertive'
      );
    }, true);
  }

  private setupProgressAnnouncements(): void {
    // Monitor progress elements and announce updates
    const progressElements = document.querySelectorAll('progress, [role="progressbar"]');
    
    progressElements.forEach(progress => {
      const observer = new MutationObserver(() => {
        const value = progress.getAttribute('aria-valuenow') || progress.getAttribute('value');
        const max = progress.getAttribute('aria-valuemax') || progress.getAttribute('max') || '100';
        
        if (value) {
          const percentage = Math.round((parseFloat(value) / parseFloat(max)) * 100);
          this.ariaAnnouncer.announce(`Progress: ${percentage}%`, 'polite');
        }
      });
      
      observer.observe(progress, {
        attributes: true,
        attributeFilter: ['value', 'aria-valuenow']
      });
    });
  }

  private handleReducedMotion(prefersReduced: boolean): void {
    document.body.setAttribute('data-reduced-motion', prefersReduced.toString());
    
    if (prefersReduced) {
      // Disable or reduce animations
      const style = document.getElementById('reduced-motion-style') || document.createElement('style');
      style.id = 'reduced-motion-style';
      style.textContent = `
        *, *::before, *::after {
          animation-duration: 0.01ms !important;
          animation-iteration-count: 1 !important;
          transition-duration: 0.01ms !important;
          scroll-behavior: auto !important;
        }
      `;
      
      if (!style.parentNode) {
        document.head.appendChild(style);
      }
    } else {
      const style = document.getElementById('reduced-motion-style');
      if (style) {
        style.remove();
      }
    }
  }

  private handleHighContrast(prefersHigh: boolean): void {
    document.body.setAttribute('data-high-contrast', prefersHigh.toString());
    
    if (prefersHigh) {
      // Enhance contrast
      document.body.classList.add('high-contrast-mode');
    } else {
      document.body.classList.remove('high-contrast-mode');
    }
  }

  private handleColorScheme(prefersDark: boolean): void {
    document.body.setAttribute('data-color-scheme', prefersDark ? 'dark' : 'light');
  }

  private monitorAccessibilityViolations(): void {
    // Only in development mode
    if (process.env.NODE_ENV === 'development') {
      this.runAccessibilityAudit();
      
      // Monitor DOM changes and re-audit
      const observer = new MutationObserver((mutations) => {
        const hasSignificantChanges = mutations.some(mutation => 
          mutation.type === 'childList' && mutation.addedNodes.length > 0
        );
        
        if (hasSignificantChanges) {
          setTimeout(() => this.runAccessibilityAudit(), 1000);
        }
      });
      
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    }
  }

  private async runAccessibilityAudit(): Promise<AccessibilityAudit> {
    // This would integrate with axe-core or similar tool
    console.log('Running accessibility audit...');
    
    // Mock audit result for example
    return {
      violations: [],
      warnings: [],
      passes: [],
      score: 100,
      wcagLevel: this.config.wcagLevel
    };
  }

  private getValidationMessage(input: HTMLInputElement): string {
    if (input.validity.valueMissing) {
      return 'This field is required';
    }
    if (input.validity.typeMismatch) {
      return 'Please enter a valid value';
    }
    if (input.validity.tooShort) {
      return `Please enter at least ${input.minLength} characters`;
    }
    if (input.validity.tooLong) {
      return `Please enter no more than ${input.maxLength} characters`;
    }
    if (input.validity.patternMismatch) {
      return 'Please match the requested format';
    }
    
    return input.validationMessage || 'Invalid input';
  }

  private getFieldLabel(input: HTMLInputElement): string {
    const label = document.querySelector(`label[for="${input.id}"]`);
    if (label) {
      return label.textContent || 'Unknown field';
    }
    
    const ariaLabel = input.getAttribute('aria-label');
    if (ariaLabel) {
      return ariaLabel;
    }
    
    const placeholder = input.getAttribute('placeholder');
    if (placeholder) {
      return placeholder;
    }
    
    return input.name || 'Unknown field';
  }

  // Public API methods
  announceToScreenReader(message: string, priority: 'polite' | 'assertive' = 'polite'): void {
    this.ariaAnnouncer.announce(message, priority);
  }

  trapFocusIn(container: HTMLElement): () => void {
    return this.focusManager.trapFocus(container);
  }

  checkColorContrast(foreground: string, background: string): ContrastRatio {
    return this.colorAnalyzer.calculateContrast(foreground, background);
  }

  validateAccessibility(element?: HTMLElement): Promise<AccessibilityAudit> {
    return this.runAccessibilityAudit();
  }

  getConfig(): AccessibilityConfig {
    return { ...this.config };
  }

  updateConfig(newConfig: Partial<AccessibilityConfig>): void {
    this.config = { ...this.config, ...newConfig };
    this.initialize(); // Re-initialize with new config
  }
}
```

**Step 1.2: Advanced ARIA and Semantic HTML Implementation**

```typescript
// Advanced ARIA and Semantic HTML Utilities
// File: src/utils/aria-utilities.ts

interface AriaAttributeMap {
  'aria-label': string;
  'aria-labelledby': string;
  'aria-describedby': string;
  'aria-expanded': boolean;
  'aria-selected': boolean;
  'aria-checked': boolean | 'mixed';
  'aria-disabled': boolean;
  'aria-hidden': boolean;
  'aria-live': 'off' | 'polite' | 'assertive';
  'aria-atomic': boolean;
  'aria-relevant': 'additions' | 'removals' | 'text' | 'all';
  'aria-busy': boolean;
  'aria-current': 'page' | 'step' | 'location' | 'date' | 'time' | boolean;
  'aria-owns': string;
  'aria-controls': string;
  'aria-activedescendant': string;
  'aria-level': number;
  'aria-setsize': number;
  'aria-posinset': number;
  'aria-valuemin': number;
  'aria-valuemax': number;
  'aria-valuenow': number;
  'aria-valuetext': string;
}

interface SemanticElement {
  tag: string;
  role?: string;
  ariaAttributes: Partial<AriaAttributeMap>;
  children?: SemanticElement[];
  content?: string;
  className?: string;
  id?: string;
}

export class AriaLiveAnnouncer {
  private politeRegion: HTMLElement | null = null;
  private assertiveRegion: HTMLElement | null = null;
  private announcementQueue: Array<{
    message: string;
    priority: 'polite' | 'assertive';
    timestamp: number;
  }> = [];

  constructor() {
    this.initialize();
  }

  private initialize(): void {
    this.createLiveRegions();
    this.setupAnnouncementQueue();
  }

  private createLiveRegions(): void {
    // Polite live region
    this.politeRegion = document.createElement('div');
    this.politeRegion.id = 'aria-live-polite';
    this.politeRegion.setAttribute('aria-live', 'polite');
    this.politeRegion.setAttribute('aria-atomic', 'true');
    this.politeRegion.className = 'a11y-sr-only';
    document.body.appendChild(this.politeRegion);

    // Assertive live region
    this.assertiveRegion = document.createElement('div');
    this.assertiveRegion.id = 'aria-live-assertive';
    this.assertiveRegion.setAttribute('aria-live', 'assertive');
    this.assertiveRegion.setAttribute('aria-atomic', 'true');
    this.assertiveRegion.className = 'a11y-sr-only';
    document.body.appendChild(this.assertiveRegion);
  }

  private setupAnnouncementQueue(): void {
    // Process announcements to avoid overwhelming screen readers
    setInterval(() => {
      if (this.announcementQueue.length > 0) {
        const announcement = this.announcementQueue.shift()!;
        this.makeAnnouncement(announcement.message, announcement.priority);
      }
    }, 1000); // Process one announcement per second
  }

  announce(message: string, priority: 'polite' | 'assertive' = 'polite'): void {
    // Add to queue to prevent overwhelming screen readers
    this.announcementQueue.push({
      message,
      priority,
      timestamp: Date.now()
    });

    // If it's urgent, process immediately
    if (priority === 'assertive' && this.announcementQueue.length === 1) {
      const announcement = this.announcementQueue.shift()!;
      this.makeAnnouncement(announcement.message, announcement.priority);
    }
  }

  private makeAnnouncement(message: string, priority: 'polite' | 'assertive'): void {
    const region = priority === 'assertive' ? this.assertiveRegion : this.politeRegion;
    
    if (region) {
      // Clear previous announcement
      region.textContent = '';
      
      // Use setTimeout to ensure screen readers catch the change
      setTimeout(() => {
        region.textContent = message;
        
        // Clear after a delay to avoid conflicts
        setTimeout(() => {
          region.textContent = '';
        }, 5000);
      }, 100);
    }
  }

  announceWithDelay(message: string, delay: number, priority: 'polite' | 'assertive' = 'polite'): void {
    setTimeout(() => {
      this.announce(message, priority);
    }, delay);
  }

  announceFormValidation(fieldName: string, error: string): void {
    this.announce(`Error in ${fieldName}: ${error}`, 'assertive');
  }

  announceProgress(current: number, total: number, label?: string): void {
    const percentage = Math.round((current / total) * 100);
    const message = label 
      ? `${label}: ${percentage}% complete`
      : `Progress: ${percentage}%`;
    
    this.announce(message, 'polite');
  }

  announceSearch(resultCount: number, query: string): void {
    const message = resultCount === 1
      ? `1 result found for "${query}"`
      : `${resultCount} results found for "${query}"`;
    
    this.announce(message, 'polite');
  }

  clear(): void {
    this.announcementQueue = [];
    if (this.politeRegion) this.politeRegion.textContent = '';
    if (this.assertiveRegion) this.assertiveRegion.textContent = '';
  }
}

export class FocusManager {
  private focusStack: HTMLElement[] = [];
  private trapStack: Array<{ container: HTMLElement; cleanup: () => void }> = [];

  initialize(): void {
    this.setupGlobalFocusHandling();
    this.setupFocusVisible();
  }

  private setupGlobalFocusHandling(): void {
    // Track focus changes
    document.addEventListener('focusin', (event) => {
      if (event.target instanceof HTMLElement) {
        this.focusStack.push(event.target);
        
        // Limit stack size
        if (this.focusStack.length > 10) {
          this.focusStack.shift();
        }
      }
    });

    // Handle escape key to close modals/dropdowns
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        this.handleEscapeKey(event);
      }
    });
  }

  private setupFocusVisible(): void {
    // Add focus-visible polyfill behavior
    let hadKeyboardEvent = false;
    const keyboardThrottleTimeout = 100;

    const onPointerDown = () => {
      hadKeyboardEvent = false;
    };

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.metaKey || event.altKey || event.ctrlKey) {
        return;
      }
      hadKeyboardEvent = true;
    };

    const onFocus = (event: FocusEvent) => {
      if (event.target instanceof HTMLElement && hadKeyboardEvent) {
        event.target.classList.add('focus-visible');
      }
    };

    const onBlur = (event: FocusEvent) => {
      if (event.target instanceof HTMLElement) {
        event.target.classList.remove('focus-visible');
      }
    };

    document.addEventListener('keydown', onKeyDown, true);
    document.addEventListener('mousedown', onPointerDown, true);
    document.addEventListener('pointerdown', onPointerDown, true);
    document.addEventListener('touchstart', onPointerDown, true);
    document.addEventListener('focus', onFocus, true);
    document.addEventListener('blur', onBlur, true);
  }

  trapFocus(container: HTMLElement): () => void {
    const focusableElements = this.getFocusableElements(container);
    
    if (focusableElements.length === 0) {
      console.warn('No focusable elements found in container');
      return () => {};
    }

    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    // Store previously focused element
    const previouslyFocused = document.activeElement as HTMLElement;

    // Focus first element
    firstFocusable.focus();

    const handleTabKey = (event: KeyboardEvent) => {
      if (event.key !== 'Tab') return;

      if (event.shiftKey) {
        if (document.activeElement === firstFocusable) {
          event.preventDefault();
          lastFocusable.focus();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          event.preventDefault();
          firstFocusable.focus();
        }
      }
    };

    container.addEventListener('keydown', handleTabKey);

    const cleanup = () => {
      container.removeEventListener('keydown', handleTabKey);
      if (previouslyFocused && document.contains(previouslyFocused)) {
        previouslyFocused.focus();
      }
    };

    this.trapStack.push({ container, cleanup });
    return cleanup;
  }

  private getFocusableElements(container: HTMLElement): HTMLElement[] {
    const selectors = [
      'button:not([disabled])',
      '[href]',
      'input:not([disabled])',
      'select:not([disabled])',
      'textarea:not([disabled])',
      '[tabindex]:not([tabindex="-1"])',
      'details',
      'summary'
    ].join(', ');

    return Array.from(container.querySelectorAll(selectors))
      .filter((el) => this.isVisible(el as HTMLElement)) as HTMLElement[];
  }

  private isVisible(element: HTMLElement): boolean {
    return !!(
      element.offsetWidth ||
      element.offsetHeight ||
      element.getClientRects().length
    );
  }

  private handleEscapeKey(event: KeyboardEvent): void {
    // Close topmost modal or dropdown
    const activeModal = document.querySelector('[role="dialog"][aria-hidden="false"]');
    const activeDropdown = document.querySelector('[aria-expanded="true"]');

    if (activeModal) {
      const closeButton = activeModal.querySelector('[data-dismiss], [aria-label*="close"], .close');
      if (closeButton instanceof HTMLElement) {
        closeButton.click();
      }
    } else if (activeDropdown) {
      if (activeDropdown instanceof HTMLElement) {
        activeDropdown.setAttribute('aria-expanded', 'false');
        activeDropdown.focus();
      }
    }
  }

  focusFirst(container: HTMLElement): boolean {
    const focusableElements = this.getFocusableElements(container);
    if (focusableElements.length > 0) {
      focusableElements[0].focus();
      return true;
    }
    return false;
  }

  focusLast(container: HTMLElement): boolean {
    const focusableElements = this.getFocusableElements(container);
    if (focusableElements.length > 0) {
      focusableElements[focusableElements.length - 1].focus();
      return true;
    }
    return false;
  }

  restoreFocus(): boolean {
    if (this.focusStack.length > 0) {
      const lastFocused = this.focusStack.pop()!;
      if (document.contains(lastFocused)) {
        lastFocused.focus();
        return true;
      }
    }
    return false;
  }

  clearTrapStack(): void {
    this.trapStack.forEach(({ cleanup }) => cleanup());
    this.trapStack = [];
  }
}

export class ColorContrastAnalyzer {
  calculateContrast(foreground: string, background: string): ContrastRatio {
    const fgLuminance = this.getLuminance(foreground);
    const bgLuminance = this.getLuminance(background);
    
    const lighter = Math.max(fgLuminance, bgLuminance);
    const darker = Math.min(fgLuminance, bgLuminance);
    
    const ratio = (lighter + 0.05) / (darker + 0.05);
    
    return {
      ratio: Math.round(ratio * 100) / 100,
      passes: {
        aa: ratio >= 4.5,
        aaa: ratio >= 7,
        aaLarge: ratio >= 3,
        aaaLarge: ratio >= 4.5
      }
    };
  }

  private getLuminance(color: string): number {
    const rgb = this.hexToRgb(color) || this.parseRgb(color);
    if (!rgb) return 0;

    const [r, g, b] = rgb.map(c => {
      const normalized = c / 255;
      return normalized <= 0.03928
        ? normalized / 12.92
        : Math.pow((normalized + 0.055) / 1.055, 2.4);
    });

    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  }

  private hexToRgb(hex: string): [number, number, number] | null {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? [
          parseInt(result[1], 16),
          parseInt(result[2], 16),
          parseInt(result[3], 16)
        ]
      : null;
  }

  private parseRgb(rgb: string): [number, number, number] | null {
    const match = rgb.match(/rgb\((\d+),\s*(\d+),\s*(\d+)\)/);
    return match
      ? [parseInt(match[1]), parseInt(match[2]), parseInt(match[3])]
      : null;
  }

  findContrastIssues(element: HTMLElement): Array<{
    element: HTMLElement;
    foreground: string;
    background: string;
    contrast: ContrastRatio;
  }> {
    const issues: Array<{
      element: HTMLElement;
      foreground: string;
      background: string;
      contrast: ContrastRatio;
    }> = [];

    const walker = document.createTreeWalker(
      element,
      NodeFilter.SHOW_ELEMENT,
      {
        acceptNode: (node: Element) => {
          const el = node as HTMLElement;
          const hasText = el.textContent && el.textContent.trim().length > 0;
          return hasText ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
        }
      }
    );

    let currentElement: HTMLElement | null = walker.currentNode as HTMLElement;

    while (currentElement) {
      const styles = window.getComputedStyle(currentElement);
      const foreground = styles.color;
      const background = styles.backgroundColor;

      if (foreground && background && background !== 'rgba(0, 0, 0, 0)') {
        const contrast = this.calculateContrast(foreground, background);
        
        if (!contrast.passes.aa) {
          issues.push({
            element: currentElement,
            foreground,
            background,
            contrast
          });
        }
      }

      currentElement = walker.nextNode() as HTMLElement;
    }

    return issues;
  }
}

export class KeyboardNavigationManager {
  private shortcuts: Map<string, () => void> = new Map();
  private navigationGroups: Map<string, HTMLElement[]> = new Map();

  initialize(): void {
    this.setupGlobalShortcuts();
    this.setupArrowKeyNavigation();
    this.setupAccessKeys();
  }

  private setupGlobalShortcuts(): void {
    document.addEventListener('keydown', (event) => {
      const key = this.getShortcutKey(event);
      const handler = this.shortcuts.get(key);
      
      if (handler) {
        event.preventDefault();
        handler();
      }
    });
  }

  private setupArrowKeyNavigation(): void {
    // Setup for tab panels, menus, etc.
    document.addEventListener('keydown', (event) => {
      if (!['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
        return;
      }

      const target = event.target as HTMLElement;
      const role = target.getAttribute('role');

      if (role === 'tab' || role === 'menuitem' || role === 'option') {
        this.handleArrowNavigation(event, target);
      }
    });
  }

  private setupAccessKeys(): void {
    // Enhanced access key support
    const accessKeyElements = document.querySelectorAll('[accesskey]');
    
    accessKeyElements.forEach(element => {
      const accessKey = element.getAttribute('accesskey');
      if (accessKey) {
        const shortcut = `alt+${accessKey.toLowerCase()}`;
        this.addShortcut(shortcut, () => {
          if (element instanceof HTMLElement) {
            if (element.tagName === 'A' || element.tagName === 'BUTTON') {
              element.click();
            } else {
              element.focus();
            }
          }
        });
      }
    });
  }

  addShortcut(combination: string, handler: () => void): void {
    this.shortcuts.set(combination.toLowerCase(), handler);
  }

  removeShortcut(combination: string): void {
    this.shortcuts.delete(combination.toLowerCase());
  }

  private getShortcutKey(event: KeyboardEvent): string {
    const parts: string[] = [];
    
    if (event.ctrlKey) parts.push('ctrl');
    if (event.altKey) parts.push('alt');
    if (event.shiftKey) parts.push('shift');
    if (event.metaKey) parts.push('meta');
    
    parts.push(event.key.toLowerCase());
    
    return parts.join('+');
  }

  private handleArrowNavigation(event: KeyboardEvent, target: HTMLElement): void {
    const container = target.closest('[role="tablist"], [role="menu"], [role="listbox"]');
    if (!container) return;

    const items = Array.from(
      container.querySelectorAll('[role="tab"], [role="menuitem"], [role="option"]')
    ) as HTMLElement[];
    
    const currentIndex = items.indexOf(target);
    if (currentIndex === -1) return;

    let newIndex = currentIndex;
    const isHorizontal = container.getAttribute('aria-orientation') !== 'vertical';
    
    if ((isHorizontal && event.key === 'ArrowLeft') || 
        (!isHorizontal && event.key === 'ArrowUp')) {
      newIndex = currentIndex > 0 ? currentIndex - 1 : items.length - 1;
    } else if ((isHorizontal && event.key === 'ArrowRight') || 
               (!isHorizontal && event.key === 'ArrowDown')) {
      newIndex = currentIndex < items.length - 1 ? currentIndex + 1 : 0;
    } else if (event.key === 'Home') {
      newIndex = 0;
    } else if (event.key === 'End') {
      newIndex = items.length - 1;
    }

    if (newIndex !== currentIndex) {
      event.preventDefault();
      
      // Update tabindex for roving tabindex pattern
      items.forEach((item, index) => {
        item.setAttribute('tabindex', index === newIndex ? '0' : '-1');
      });
      
      items[newIndex].focus();
      
      // Trigger selection for tabs
      if (container.getAttribute('role') === 'tablist') {
        items[newIndex].click();
      }
    }
  }

  createNavigationGroup(name: string, elements: HTMLElement[]): void {
    this.navigationGroups.set(name, elements);
    
    // Setup navigation within group
    elements.forEach((element, index) => {
      element.addEventListener('keydown', (event) => {
        if (['ArrowUp', 'ArrowDown'].includes(event.key)) {
          event.preventDefault();
          
          let newIndex = index;
          if (event.key === 'ArrowDown') {
            newIndex = index < elements.length - 1 ? index + 1 : 0;
          } else {
            newIndex = index > 0 ? index - 1 : elements.length - 1;
          }
          
          elements[newIndex].focus();
        }
      });
    });
  }
}
```

### Phase 2: Form Accessibility and Validation (2-3 hours)

**Step 2.1: Accessible Form Components**

```typescript
// Accessible Form Components and Validation
// File: src/components/AccessibleForm.tsx

import React, { useRef, useState, useEffect } from 'react';

interface AccessibleFormProps {
  onSubmit: (data: FormData) => void | Promise<void>;
  children: React.ReactNode;
  noValidate?: boolean;
  ariaLabel?: string;
  ariaLabelledBy?: string;
  className?: string;
}

interface FieldError {
  field: string;
  message: string;
  type: string;
}

interface FormState {
  isSubmitting: boolean;
  errors: FieldError[];
  touched: Set<string>;
}

export const AccessibleForm: React.FC<AccessibleFormProps> = ({
  onSubmit,
  children,
  noValidate = true,
  ariaLabel,
  ariaLabelledBy,
  className = ''
}) => {
  const formRef = useRef<HTMLFormElement>(null);
  const [formState, setFormState] = useState<FormState>({
    isSubmitting: false,
    errors: [],
    touched: new Set()
  });

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    
    if (formState.isSubmitting) return;

    setFormState(prev => ({ ...prev, isSubmitting: true }));

    try {
      const formData = new FormData(event.currentTarget);
      await onSubmit(formData);
      
      // Clear form on successful submission
      event.currentTarget.reset();
      setFormState({ isSubmitting: false, errors: [], touched: new Set() });
      
      // Announce success to screen readers
      announceToScreenReader('Form submitted successfully', 'polite');
    } catch (error) {
      console.error('Form submission error:', error);
      announceToScreenReader('Form submission failed. Please correct the errors and try again.', 'assertive');
      
      setFormState(prev => ({ ...prev, isSubmitting: false }));
    }
  };

  const announceToScreenReader = (message: string, priority: 'polite' | 'assertive') => {
    const region = document.getElementById(
      priority === 'assertive' ? 'aria-live-assertive' : 'aria-live-polite'
    );
    
    if (region) {
      region.textContent = message;
      setTimeout(() => {
        region.textContent = '';
      }, 5000);
    }
  };

  return (
    <form
      ref={formRef}
      onSubmit={handleSubmit}
      noValidate={noValidate}
      aria-label={ariaLabel}
      aria-labelledby={ariaLabelledBy}
      className={`accessible-form ${className}`}
      role="form"
    >
      {formState.errors.length > 0 && (
        <div
          role="alert"
          className="form-errors"
          aria-labelledby="error-heading"
        >
          <h3 id="error-heading">Please correct the following errors:</h3>
          <ul>
            {formState.errors.map((error, index) => (
              <li key={index}>
                <a href={`#${error.field}`}>
                  {error.message}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
      
      {children}
      
      {formState.isSubmitting && (
        <div
          role="status"
          aria-live="polite"
          className="form-submitting"
        >
          <span className="sr-only">Submitting form...</span>
          <div className="loading-spinner" aria-hidden="true" />
        </div>
      )}
    </form>
  );
};

interface AccessibleInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  help?: string;
  required?: boolean;
  showRequiredIndicator?: boolean;
}

export const AccessibleInput: React.FC<AccessibleInputProps> = ({
  label,
  error,
  help,
  required = false,
  showRequiredIndicator = true,
  id,
  className = '',
  ...inputProps
}) => {
  const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`;
  const errorId = error ? `${inputId}-error` : undefined;
  const helpId = help ? `${inputId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');

  return (
    <div className={`form-field ${error ? 'has-error' : ''} ${className}`}>
      <label 
        htmlFor={inputId}
        className="form-label"
      >
        {label}
        {required && showRequiredIndicator && (
          <span className="required-indicator" aria-label="required">
            *
          </span>
        )}
      </label>
      
      <input
        {...inputProps}
        id={inputId}
        required={required}
        aria-describedby={describedBy || undefined}
        aria-invalid={error ? 'true' : 'false'}
        className="form-input"
      />
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </div>
  );
};

interface AccessibleSelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label: string;
  error?: string;
  help?: string;
  options: Array<{ value: string; label: string; disabled?: boolean }>;
  placeholder?: string;
  required?: boolean;
}

export const AccessibleSelect: React.FC<AccessibleSelectProps> = ({
  label,
  error,
  help,
  options,
  placeholder,
  required = false,
  id,
  className = '',
  ...selectProps
}) => {
  const selectId = id || `select-${Math.random().toString(36).substr(2, 9)}`;
  const errorId = error ? `${selectId}-error` : undefined;
  const helpId = help ? `${selectId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');

  return (
    <div className={`form-field ${error ? 'has-error' : ''} ${className}`}>
      <label 
        htmlFor={selectId}
        className="form-label"
      >
        {label}
        {required && (
          <span className="required-indicator" aria-label="required">
            *
          </span>
        )}
      </label>
      
      <select
        {...selectProps}
        id={selectId}
        required={required}
        aria-describedby={describedBy || undefined}
        aria-invalid={error ? 'true' : 'false'}
        className="form-select"
      >
        {placeholder && (
          <option value="" disabled>
            {placeholder}
          </option>
        )}
        
        {options.map((option, index) => (
          <option
            key={index}
            value={option.value}
            disabled={option.disabled}
          >
            {option.label}
          </option>
        ))}
      </select>
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </div>
  );
};

interface AccessibleCheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  help?: string;
  indeterminate?: boolean;
}

export const AccessibleCheckbox: React.FC<AccessibleCheckboxProps> = ({
  label,
  error,
  help,
  indeterminate = false,
  id,
  className = '',
  ...inputProps
}) => {
  const checkboxId = id || `checkbox-${Math.random().toString(36).substr(2, 9)}`;
  const errorId = error ? `${checkboxId}-error` : undefined;
  const helpId = help ? `${checkboxId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.indeterminate = indeterminate;
    }
  }, [indeterminate]);

  return (
    <div className={`form-field checkbox-field ${error ? 'has-error' : ''} ${className}`}>
      <div className="checkbox-wrapper">
        <input
          {...inputProps}
          ref={inputRef}
          type="checkbox"
          id={checkboxId}
          aria-describedby={describedBy || undefined}
          aria-invalid={error ? 'true' : 'false'}
          aria-checked={indeterminate ? 'mixed' : undefined}
          className="form-checkbox"
        />
        
        <label 
          htmlFor={checkboxId}
          className="checkbox-label"
        >
          {label}
        </label>
      </div>
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </div>
  );
};

interface AccessibleRadioGroupProps {
  name: string;
  label: string;
  error?: string;
  help?: string;
  options: Array<{ value: string; label: string; disabled?: boolean }>;
  value?: string;
  onChange: (value: string) => void;
  required?: boolean;
}

export const AccessibleRadioGroup: React.FC<AccessibleRadioGroupProps> = ({
  name,
  label,
  error,
  help,
  options,
  value,
  onChange,
  required = false,
  ...props
}) => {
  const groupId = `radio-group-${Math.random().toString(36).substr(2, 9)}`;
  const errorId = error ? `${groupId}-error` : undefined;
  const helpId = help ? `${groupId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');

  return (
    <fieldset 
      className={`form-field radio-group ${error ? 'has-error' : ''}`}
      aria-describedby={describedBy || undefined}
      aria-invalid={error ? 'true' : 'false'}
    >
      <legend className="form-label">
        {label}
        {required && (
          <span className="required-indicator" aria-label="required">
            *
          </span>
        )}
      </legend>
      
      {options.map((option, index) => {
        const radioId = `${groupId}-${index}`;
        
        return (
          <div key={index} className="radio-wrapper">
            <input
              type="radio"
              id={radioId}
              name={name}
              value={option.value}
              checked={value === option.value}
              onChange={(e) => onChange(e.target.value)}
              disabled={option.disabled}
              required={required}
              className="form-radio"
            />
            
            <label 
              htmlFor={radioId}
              className="radio-label"
            >
              {option.label}
            </label>
          </div>
        );
      })}
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </fieldset>
  );
};

// Advanced File Upload with Accessibility
interface AccessibleFileUploadProps {
  label: string;
  accept?: string;
  multiple?: boolean;
  maxSize?: number;
  error?: string;
  help?: string;
  onFilesSelected: (files: File[]) => void;
  required?: boolean;
}

export const AccessibleFileUpload: React.FC<AccessibleFileUploadProps> = ({
  label,
  accept,
  multiple = false,
  maxSize,
  error,
  help,
  onFilesSelected,
  required = false
}) => {
  const [dragOver, setDragOver] = useState(false);
  const [files, setFiles] = useState<File[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  
  const uploadId = `file-upload-${Math.random().toString(36).substr(2, 9)}`;
  const errorId = error ? `${uploadId}-error` : undefined;
  const helpId = help ? `${uploadId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');

  const handleFiles = (newFiles: FileList) => {
    const fileArray = Array.from(newFiles);
    const validFiles = fileArray.filter(file => {
      if (maxSize && file.size > maxSize) {
        // Show individual file error
        return false;
      }
      return true;
    });
    
    setFiles(validFiles);
    onFilesSelected(validFiles);
  };

  const handleDrop = (event: React.DragEvent) => {
    event.preventDefault();
    setDragOver(false);
    
    const droppedFiles = event.dataTransfer.files;
    if (droppedFiles.length > 0) {
      handleFiles(droppedFiles);
    }
  };

  const removeFile = (index: number) => {
    const newFiles = files.filter((_, i) => i !== index);
    setFiles(newFiles);
    onFilesSelected(newFiles);
  };

  return (
    <div className={`form-field file-upload ${error ? 'has-error' : ''}`}>
      <label 
        htmlFor={uploadId}
        className="form-label"
      >
        {label}
        {required && (
          <span className="required-indicator" aria-label="required">
            *
          </span>
        )}
      </label>
      
      <div
        className={`file-drop-zone ${dragOver ? 'drag-over' : ''}`}
        onDrop={handleDrop}
        onDragOver={(e) => {
          e.preventDefault();
          setDragOver(true);
        }}
        onDragLeave={() => setDragOver(false)}
        role="button"
        tabIndex={0}
        aria-describedby={describedBy || undefined}
        onClick={() => inputRef.current?.click()}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            inputRef.current?.click();
          }
        }}
      >
        <input
          ref={inputRef}
          type="file"
          id={uploadId}
          accept={accept}
          multiple={multiple}
          required={required}
          onChange={(e) => {
            if (e.target.files) {
              handleFiles(e.target.files);
            }
          }}
          className="sr-only"
          aria-describedby={describedBy || undefined}
        />
        
        <div className="drop-zone-content">
          <svg
            className="upload-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 48 48"
            aria-hidden="true"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
            />
          </svg>
          
          <p>
            <span className="upload-text">
              Click to upload or drag and drop
            </span>
          </p>
          
          {accept && (
            <p className="upload-hint">
              Accepted formats: {accept}
            </p>
          )}
          
          {maxSize && (
            <p className="upload-hint">
              Maximum file size: {Math.round(maxSize / 1024 / 1024)}MB
            </p>
          )}
        </div>
      </div>
      
      {files.length > 0 && (
        <div className="uploaded-files" aria-label="Uploaded files">
          {files.map((file, index) => (
            <div key={index} className="uploaded-file">
              <span className="file-name">{file.name}</span>
              <span className="file-size">
                {Math.round(file.size / 1024)}KB
              </span>
              <button
                type="button"
                onClick={() => removeFile(index)}
                className="remove-file"
                aria-label={`Remove ${file.name}`}
              >
                ×
              </button>
            </div>
          ))}
        </div>
      )}
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </div>
  );
};
```

**Step 2.2: Advanced Interactive Components**

```typescript
// Advanced Accessible Interactive Components
// File: src/components/AccessibleComponents.tsx

import React, { useState, useRef, useEffect, useCallback } from 'react';

// Accessible Modal/Dialog
interface AccessibleModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  size?: 'small' | 'medium' | 'large';
  closeOnBackdrop?: boolean;
  closeOnEscape?: boolean;
}

export const AccessibleModal: React.FC<AccessibleModalProps> = ({
  isOpen,
  onClose,
  title,
  children,
  size = 'medium',
  closeOnBackdrop = true,
  closeOnEscape = true
}) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const titleRef = useRef<HTMLHeadingElement>(null);
  const previousActiveElement = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      // Store previously focused element
      previousActiveElement.current = document.activeElement as HTMLElement;
      
      // Focus the modal title
      setTimeout(() => {
        titleRef.current?.focus();
      }, 100);

      // Trap focus within modal
      const handleKeyDown = (event: KeyboardEvent) => {
        if (!closeOnEscape) return;
        
        if (event.key === 'Escape') {
          onClose();
          return;
        }

        if (event.key === 'Tab' && modalRef.current) {
          const focusableElements = modalRef.current.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
          );

          const firstElement = focusableElements[0] as HTMLElement;
          const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

          if (event.shiftKey) {
            if (document.activeElement === firstElement) {
              event.preventDefault();
              lastElement.focus();
            }
          } else {
            if (document.activeElement === lastElement) {
              event.preventDefault();
              firstElement.focus();
            }
          }
        }
      };

      document.addEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'hidden';

      return () => {
        document.removeEventListener('keydown', handleKeyDown);
        document.body.style.overflow = '';
        
        // Restore focus to previously focused element
        if (previousActiveElement.current) {
          previousActiveElement.current.focus();
        }
      };
    }
  }, [isOpen, onClose, closeOnEscape]);

  if (!isOpen) return null;

  return (
    <div
      className="modal-backdrop"
      onClick={closeOnBackdrop ? onClose : undefined}
      aria-hidden="true"
    >
      <div
        ref={modalRef}
        className={`modal modal-${size}`}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="modal-header">
          <h2
            ref={titleRef}
            id="modal-title"
            className="modal-title"
            tabIndex={-1}
          >
            {title}
          </h2>
          
          <button
            className="modal-close"
            onClick={onClose}
            aria-label="Close dialog"
          >
            <span aria-hidden="true">×</span>
          </button>
        </div>
        
        <div className="modal-content">
          {children}
        </div>
      </div>
    </div>
  );
};

// Accessible Dropdown/Combobox
interface AccessibleDropdownProps {
  label: string;
  options: Array<{ value: string; label: string; disabled?: boolean }>;
  value?: string;
  onChange: (value: string) => void;
  placeholder?: string;
  filterable?: boolean;
  error?: string;
  help?: string;
  required?: boolean;
}

export const AccessibleDropdown: React.FC<AccessibleDropdownProps> = ({
  label,
  options,
  value,
  onChange,
  placeholder = 'Select an option',
  filterable = false,
  error,
  help,
  required = false
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [filter, setFilter] = useState('');
  const [activeIndex, setActiveIndex] = useState(-1);
  
  const comboboxRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLUListElement>(null);
  
  const dropdownId = `dropdown-${Math.random().toString(36).substr(2, 9)}`;
  const listId = `${dropdownId}-list`;
  const errorId = error ? `${dropdownId}-error` : undefined;
  const helpId = help ? `${dropdownId}-help` : undefined;
  
  const describedBy = [errorId, helpId].filter(Boolean).join(' ');

  const filteredOptions = options.filter(option =>
    !filterable || option.label.toLowerCase().includes(filter.toLowerCase())
  );

  const selectedOption = options.find(option => option.value === value);

  const handleKeyDown = (event: React.KeyboardEvent) => {
    switch (event.key) {
      case 'ArrowDown':
        event.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
          setActiveIndex(0);
        } else {
          setActiveIndex(prev => 
            prev < filteredOptions.length - 1 ? prev + 1 : 0
          );
        }
        break;

      case 'ArrowUp':
        event.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
          setActiveIndex(filteredOptions.length - 1);
        } else {
          setActiveIndex(prev => 
            prev > 0 ? prev - 1 : filteredOptions.length - 1
          );
        }
        break;

      case 'Enter':
      case ' ':
        event.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
        } else if (activeIndex >= 0) {
          onChange(filteredOptions[activeIndex].value);
          setIsOpen(false);
          setActiveIndex(-1);
        }
        break;

      case 'Escape':
        if (isOpen) {
          setIsOpen(false);
          setActiveIndex(-1);
          inputRef.current?.focus();
        }
        break;

      case 'Tab':
        setIsOpen(false);
        setActiveIndex(-1);
        break;
    }
  };

  const handleOptionClick = (optionValue: string) => {
    onChange(optionValue);
    setIsOpen(false);
    setActiveIndex(-1);
    inputRef.current?.focus();
  };

  useEffect(() => {
    if (isOpen && activeIndex >= 0 && listRef.current) {
      const activeOption = listRef.current.children[activeIndex] as HTMLElement;
      activeOption?.scrollIntoView({ block: 'nearest' });
    }
  }, [activeIndex, isOpen]);

  return (
    <div className={`form-field dropdown ${error ? 'has-error' : ''}`}>
      <label 
        htmlFor={dropdownId}
        className="form-label"
      >
        {label}
        {required && (
          <span className="required-indicator" aria-label="required">
            *
          </span>
        )}
      </label>
      
      <div
        ref={comboboxRef}
        className="dropdown-container"
      >
        <input
          ref={inputRef}
          id={dropdownId}
          role="combobox"
          aria-expanded={isOpen}
          aria-autocomplete={filterable ? 'list' : 'none'}
          aria-haspopup="listbox"
          aria-controls={listId}
          aria-describedby={describedBy || undefined}
          aria-invalid={error ? 'true' : 'false'}
          aria-activedescendant={
            isOpen && activeIndex >= 0 
              ? `${listId}-option-${activeIndex}` 
              : undefined
          }
          value={filterable ? filter : selectedOption?.label || ''}
          placeholder={placeholder}
          onChange={(e) => {
            if (filterable) {
              setFilter(e.target.value);
              if (!isOpen) setIsOpen(true);
            }
          }}
          onKeyDown={handleKeyDown}
          onFocus={() => {
            if (filterable) {
              setFilter('');
            }
          }}
          onBlur={(e) => {
            // Close dropdown when focus moves outside the component
            setTimeout(() => {
              if (!comboboxRef.current?.contains(document.activeElement)) {
                setIsOpen(false);
                setActiveIndex(-1);
                if (filterable && selectedOption) {
                  setFilter(selectedOption.label);
                }
              }
            }, 100);
          }}
          className="dropdown-input"
          required={required}
        />
        
        <button
          type="button"
          className="dropdown-trigger"
          aria-label="Open dropdown"
          onClick={() => {
            setIsOpen(!isOpen);
            inputRef.current?.focus();
          }}
        >
          <span className="dropdown-arrow" aria-hidden="true">
            {isOpen ? '▲' : '▼'}
          </span>
        </button>
        
        {isOpen && (
          <ul
            ref={listRef}
            id={listId}
            role="listbox"
            aria-label={label}
            className="dropdown-list"
          >
            {filteredOptions.length === 0 ? (
              <li role="option" className="dropdown-option no-options">
                No options found
              </li>
            ) : (
              filteredOptions.map((option, index) => (
                <li
                  key={option.value}
                  id={`${listId}-option-${index}`}
                  role="option"
                  aria-selected={option.value === value}
                  aria-disabled={option.disabled}
                  className={`dropdown-option ${
                    index === activeIndex ? 'active' : ''
                  } ${option.value === value ? 'selected' : ''} ${
                    option.disabled ? 'disabled' : ''
                  }`}
                  onClick={option.disabled ? undefined : () => handleOptionClick(option.value)}
                  onMouseEnter={() => setActiveIndex(index)}
                >
                  {option.label}
                </li>
              ))
            )}
          </ul>
        )}
      </div>
      
      {help && (
        <div 
          id={helpId}
          className="form-help"
        >
          {help}
        </div>
      )}
      
      {error && (
        <div 
          id={errorId}
          role="alert"
          className="form-error"
          aria-live="polite"
        >
          <span className="sr-only">Error: </span>
          {error}
        </div>
      )}
    </div>
  );
};

// Accessible Tabs Component
interface TabItem {
  id: string;
  label: string;
  content: React.ReactNode;
  disabled?: boolean;
}

interface AccessibleTabsProps {
  tabs: TabItem[];
  defaultActiveTab?: string;
  onTabChange?: (tabId: string) => void;
  orientation?: 'horizontal' | 'vertical';
}

export const AccessibleTabs: React.FC<AccessibleTabsProps> = ({
  tabs,
  defaultActiveTab,
  onTabChange,
  orientation = 'horizontal'
}) => {
  const [activeTab, setActiveTab] = useState(defaultActiveTab || tabs[0]?.id);
  const [focusedTab, setFocusedTab] = useState(activeTab);
  
  const tabListRef = useRef<HTMLDivElement>(null);
  const tabRefs = useRef<{ [key: string]: HTMLButtonElement }>({});

  const handleTabClick = (tabId: string) => {
    if (tabs.find(tab => tab.id === tabId && !tab.disabled)) {
      setActiveTab(tabId);
      setFocusedTab(tabId);
      onTabChange?.(tabId);
    }
  };

  const handleKeyDown = (event: React.KeyboardEvent, tabId: string) => {
    const currentIndex = tabs.findIndex(tab => tab.id === tabId);
    let newIndex = currentIndex;

    switch (event.key) {
      case 'ArrowRight':
      case 'ArrowDown':
        event.preventDefault();
        newIndex = (currentIndex + 1) % tabs.length;
        break;

      case 'ArrowLeft':
      case 'ArrowUp':
        event.preventDefault();
        newIndex = currentIndex === 0 ? tabs.length - 1 : currentIndex - 1;
        break;

      case 'Home':
        event.preventDefault();
        newIndex = 0;
        break;

      case 'End':
        event.preventDefault();
        newIndex = tabs.length - 1;
        break;

      case 'Enter':
      case ' ':
        event.preventDefault();
        handleTabClick(tabId);
        return;
    }

    // Skip disabled tabs
    while (tabs[newIndex]?.disabled && newIndex !== currentIndex) {
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
        newIndex = (newIndex + 1) % tabs.length;
      } else {
        newIndex = newIndex === 0 ? tabs.length - 1 : newIndex - 1;
      }
    }

    const newTabId = tabs[newIndex]?.id;
    if (newTabId && newTabId !== tabId) {
      setFocusedTab(newTabId);
      tabRefs.current[newTabId]?.focus();
    }
  };

  const activeTabContent = tabs.find(tab => tab.id === activeTab)?.content;

  return (
    <div className={`accessible-tabs tabs-${orientation}`}>
      <div
        ref={tabListRef}
        role="tablist"
        aria-orientation={orientation}
        className="tab-list"
      >
        {tabs.map((tab) => (
          <button
            key={tab.id}
            ref={(el) => {
              if (el) tabRefs.current[tab.id] = el;
            }}
            role="tab"
            id={`tab-${tab.id}`}
            aria-controls={`panel-${tab.id}`}
            aria-selected={tab.id === activeTab}
            aria-disabled={tab.disabled}
            tabIndex={tab.id === focusedTab ? 0 : -1}
            className={`tab ${tab.id === activeTab ? 'active' : ''} ${
              tab.disabled ? 'disabled' : ''
            }`}
            onClick={() => handleTabClick(tab.id)}
            onKeyDown={(e) => handleKeyDown(e, tab.id)}
            disabled={tab.disabled}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div
        id={`panel-${activeTab}`}
        role="tabpanel"
        aria-labelledby={`tab-${activeTab}`}
        className="tab-panel"
        tabIndex={0}
      >
        {activeTabContent}
      </div>
    </div>
  );
};

// Accessible Progress Indicator
interface AccessibleProgressProps {
  value: number;
  max?: number;
  label?: string;
  description?: string;
  showPercentage?: boolean;
  variant?: 'linear' | 'circular';
  size?: 'small' | 'medium' | 'large';
}

export const AccessibleProgress: React.FC<AccessibleProgressProps> = ({
  value,
  max = 100,
  label,
  description,
  showPercentage = true,
  variant = 'linear',
  size = 'medium'
}) => {
  const percentage = Math.min((value / max) * 100, 100);
  const progressId = `progress-${Math.random().toString(36).substr(2, 9)}`;
  const labelId = label ? `${progressId}-label` : undefined;
  const descId = description ? `${progressId}-desc` : undefined;

  const ariaLabel = label || `Progress: ${Math.round(percentage)}%`;
  const describedBy = [labelId, descId].filter(Boolean).join(' ');

  if (variant === 'circular') {
    const radius = size === 'small' ? 15 : size === 'large' ? 25 : 20;
    const circumference = 2 * Math.PI * radius;
    const strokeDashoffset = circumference - (percentage / 100) * circumference;

    return (
      <div 
        className={`progress-container progress-circular progress-${size}`}
        role="img"
        aria-labelledby={labelId}
        aria-describedby={descId || undefined}
      >
        {label && (
          <div id={labelId} className="progress-label">
            {label}
          </div>
        )}
        
        <svg
          className="progress-circle"
          width={radius * 2 + 10}
          height={radius * 2 + 10}
        >
          <circle
            cx={radius + 5}
            cy={radius + 5}
            r={radius}
            className="progress-track"
            fill="none"
            strokeWidth="3"
          />
          <circle
            cx={radius + 5}
            cy={radius + 5}
            r={radius}
            className="progress-fill"
            fill="none"
            strokeWidth="3"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            transform={`rotate(-90 ${radius + 5} ${radius + 5})`}
          />
          {showPercentage && (
            <text
              x={radius + 5}
              y={radius + 5}
              textAnchor="middle"
              dominantBaseline="central"
              className="progress-text"
            >
              {Math.round(percentage)}%
            </text>
          )}
        </svg>
        
        {description && (
          <div id={descId} className="progress-description">
            {description}
          </div>
        )}
      </div>
    );
  }

  return (
    <div 
      className={`progress-container progress-linear progress-${size}`}
      role="img"
      aria-labelledby={labelId}
      aria-describedby={descId || undefined}
    >
      {label && (
        <div id={labelId} className="progress-label">
          {label}
          {showPercentage && (
            <span className="progress-percentage">
              {Math.round(percentage)}%
            </span>
          )}
        </div>
      )}
      
      <div
        role="progressbar"
        aria-valuenow={value}
        aria-valuemin={0}
        aria-valuemax={max}
        aria-label={ariaLabel}
        className="progress-bar"
      >
        <div
          className="progress-fill"
          style={{ width: `${percentage}%` }}
        />
      </div>
      
      {description && (
        <div id={descId} className="progress-description">
          {description}
        </div>
      )}
    </div>
  );
};
```

## 📊 Success Criteria

### WCAG 2.1 Compliance Metrics
- **Level AA Compliance**: 100% conformance across all components and pages
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Keyboard Navigation**: 100% keyboard accessible functionality
- **Screen Reader Support**: Full compatibility with JAWS, NVDA, and VoiceOver

### User Experience Metrics
- **Task Completion Rate**: >95% for users with disabilities
- **Error Recovery**: <3 attempts average to correct form errors
- **Navigation Efficiency**: <20% increase in task time for keyboard users
- **User Satisfaction**: >4.5/5 rating from accessibility user testing

### Technical Implementation Quality
- **Semantic HTML**: 100% use of semantic markup where appropriate
- **ARIA Implementation**: Proper ARIA labels and roles on all interactive elements
- **Focus Management**: Logical focus order and visible focus indicators
- **Responsive Design**: Full accessibility across all screen sizes and orientations

## 🎯 Deliverables

Upon completion of comprehensive web accessibility and inclusive design implementation:

- ✅ **WCAG 2.1 AA Compliant Components** with comprehensive accessibility features
- ✅ **Advanced ARIA Implementation** with live regions, complex widget patterns, and screen reader optimization
- ✅ **Keyboard Navigation System** with focus management, skip links, and custom keyboard shortcuts
- ✅ **Accessible Form Components** with validation, error handling, and multi-step form support
- ✅ **Inclusive Design Patterns** supporting users with various disabilities and assistive technologies
- ✅ **Accessibility Testing Framework** with automated testing and manual testing procedures
- ✅ **User Preference Adaptation** respecting reduced motion, high contrast, and dark mode preferences
- ✅ **Documentation and Training** materials for maintaining accessibility standards

---

*This comprehensive web accessibility and inclusive design implementation ensures that all users, regardless of their abilities or circumstances, can effectively access and use web applications while meeting legal compliance requirements.*