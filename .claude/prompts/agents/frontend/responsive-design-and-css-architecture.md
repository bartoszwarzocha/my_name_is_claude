# Responsive Design and CSS Architecture

**Agent Type: frontend-engineer**
**Complexity Level: Expert**
**Estimated Duration: 6-10 hours**

---

## 🎯 Mission

Design and implement comprehensive responsive CSS architecture using modern CSS methodologies, design systems, and performance optimization techniques to create scalable, maintainable, and accessible user interfaces across all devices and screen sizes.

## 📋 Process Framework

### Phase 1: CSS Architecture Design (2-3 hours)

**Step 1.1: Scalable CSS Architecture Framework**

```scss
// Modern CSS Architecture Framework
// File: src/styles/architecture/_index.scss

// 1. Settings - Global variables, configuration
@import 'settings/variables';
@import 'settings/breakpoints';
@import 'settings/typography';
@import 'settings/colors';
@import 'settings/spacing';
@import 'settings/z-index';

// 2. Tools - Mixins and functions
@import 'tools/mixins';
@import 'tools/functions';
@import 'tools/breakpoint-mixins';
@import 'tools/utility-mixins';

// 3. Generic - Reset, normalize, box-sizing
@import 'generic/normalize';
@import 'generic/reset';
@import 'generic/box-sizing';

// 4. Elements - Base element styles
@import 'elements/typography';
@import 'elements/forms';
@import 'elements/tables';
@import 'elements/media';

// 5. Objects - Layout patterns, design patterns
@import 'objects/layout';
@import 'objects/grid';
@import 'objects/containers';
@import 'objects/media-object';

// 6. Components - UI components
@import 'components/buttons';
@import 'components/cards';
@import 'components/navigation';
@import 'components/modals';
@import 'components/forms';

// 7. Utilities - Helper classes, overrides
@import 'utilities/spacing';
@import 'utilities/typography';
@import 'utilities/colors';
@import 'utilities/display';
@import 'utilities/positioning';

// Advanced CSS Custom Properties System
:root {
  // Design Tokens - Spacing Scale
  --space-0: 0;
  --space-1: 0.25rem;  // 4px
  --space-2: 0.5rem;   // 8px
  --space-3: 0.75rem;  // 12px
  --space-4: 1rem;     // 16px
  --space-5: 1.25rem;  // 20px
  --space-6: 1.5rem;   // 24px
  --space-8: 2rem;     // 32px
  --space-10: 2.5rem;  // 40px
  --space-12: 3rem;    // 48px
  --space-16: 4rem;    // 64px
  --space-20: 5rem;    // 80px
  --space-24: 6rem;    // 96px
  --space-32: 8rem;    // 128px
  
  // Typography Scale (Perfect Fourth - 1.333)
  --text-xs: 0.75rem;    // 12px
  --text-sm: 0.875rem;   // 14px
  --text-base: 1rem;     // 16px
  --text-lg: 1.125rem;   // 18px
  --text-xl: 1.25rem;    // 20px
  --text-2xl: 1.5rem;    // 24px
  --text-3xl: 1.875rem;  // 30px
  --text-4xl: 2.25rem;   // 36px
  --text-5xl: 3rem;      // 48px
  --text-6xl: 3.75rem;   // 60px
  --text-7xl: 4.5rem;    // 72px
  --text-8xl: 6rem;      // 96px
  --text-9xl: 8rem;      // 128px
  
  // Line Heights
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
  
  // Font Weights
  --font-thin: 100;
  --font-extralight: 200;
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
  --font-black: 900;
  
  // Colors - Semantic Color System
  // Primary Colors
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-200: #bfdbfe;
  --color-primary-300: #93c5fd;
  --color-primary-400: #60a5fa;
  --color-primary-500: #3b82f6;
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-800: #1e40af;
  --color-primary-900: #1e3a8a;
  
  // Neutral Colors
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;
  
  // Semantic Colors
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  --color-info: #3b82f6;
  
  // Surface Colors
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-surface-variant: #f3f4f6;
  
  // Border Radius
  --radius-none: 0;
  --radius-sm: 0.125rem;
  --radius-base: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-2xl: 1rem;
  --radius-3xl: 1.5rem;
  --radius-full: 9999px;
  
  // Shadows
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-base: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
  
  // Transitions
  --transition-none: none;
  --transition-all: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-default: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-colors: color 150ms cubic-bezier(0.4, 0, 0.2, 1), 
                       background-color 150ms cubic-bezier(0.4, 0, 0.2, 1), 
                       border-color 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-opacity: opacity 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-shadow: box-shadow 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-transform: transform 150ms cubic-bezier(0.4, 0, 0.2, 1);
  
  // Z-Index Scale
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-modal-backdrop: 1040;
  --z-modal: 1050;
  --z-popover: 1060;
  --z-tooltip: 1070;
  --z-toast: 1080;
}

// Dark Mode Variables
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #0f172a;
    --color-surface: #1e293b;
    --color-surface-variant: #334155;
    
    --color-text-primary: #f8fafc;
    --color-text-secondary: #cbd5e1;
    --color-text-tertiary: #94a3b8;
  }
}

[data-theme="dark"] {
  --color-background: #0f172a;
  --color-surface: #1e293b;
  --color-surface-variant: #334155;
  
  --color-text-primary: #f8fafc;
  --color-text-secondary: #cbd5e1;
  --color-text-tertiary: #94a3b8;
}
```

**Step 1.2: Advanced Breakpoint and Grid System**

```scss
// Advanced Responsive Breakpoint System
// File: src/styles/tools/_breakpoint-mixins.scss

// Breakpoint Map
$breakpoints: (
  'xs': 0,
  'sm': 576px,
  'md': 768px,
  'lg': 992px,
  'xl': 1200px,
  'xxl': 1400px,
  '2xl': 1536px,
  '3xl': 1920px,
  '4xl': 2560px
) !default;

// Container Max Widths
$container-max-widths: (
  'sm': 540px,
  'md': 720px,
  'lg': 960px,
  'xl': 1140px,
  'xxl': 1320px,
  '2xl': 1440px,
  '3xl': 1800px,
  '4xl': 2400px
) !default;

// Advanced Breakpoint Mixin
@mixin breakpoint($size, $type: 'up') {
  @if map-has-key($breakpoints, $size) {
    $breakpoint: map-get($breakpoints, $size);
    
    @if $type == 'up' {
      @if $breakpoint == 0 {
        @content;
      } @else {
        @media (min-width: $breakpoint) {
          @content;
        }
      }
    } @else if $type == 'down' {
      @if $breakpoint == 0 {
        @content;
      } @else {
        @media (max-width: $breakpoint - 1px) {
          @content;
        }
      }
    } @else if $type == 'only' {
      $next-size: null;
      $breakpoint-keys: map-keys($breakpoints);
      $current-index: index($breakpoint-keys, $size);
      
      @if $current-index < length($breakpoint-keys) {
        $next-size: nth($breakpoint-keys, $current-index + 1);
      }
      
      @if $next-size {
        $next-breakpoint: map-get($breakpoints, $next-size);
        @media (min-width: $breakpoint) and (max-width: $next-breakpoint - 1px) {
          @content;
        }
      } @else {
        @media (min-width: $breakpoint) {
          @content;
        }
      }
    }
  } @else {
    @warn "Breakpoint '#{$size}' does not exist in $breakpoints map.";
  }
}

// Modern CSS Grid System
.grid {
  display: grid;
  gap: var(--space-4);
  
  // Responsive Grid Templates
  &--cols-1 { grid-template-columns: 1fr; }
  &--cols-2 { grid-template-columns: repeat(2, 1fr); }
  &--cols-3 { grid-template-columns: repeat(3, 1fr); }
  &--cols-4 { grid-template-columns: repeat(4, 1fr); }
  &--cols-5 { grid-template-columns: repeat(5, 1fr); }
  &--cols-6 { grid-template-columns: repeat(6, 1fr); }
  &--cols-12 { grid-template-columns: repeat(12, 1fr); }
  
  // Auto-fit grids
  &--auto-fit {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
  
  &--auto-fill {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
  
  // Responsive variations
  @include breakpoint('sm') {
    &--sm-cols-1 { grid-template-columns: 1fr; }
    &--sm-cols-2 { grid-template-columns: repeat(2, 1fr); }
    &--sm-cols-3 { grid-template-columns: repeat(3, 1fr); }
    &--sm-cols-4 { grid-template-columns: repeat(4, 1fr); }
  }
  
  @include breakpoint('md') {
    &--md-cols-1 { grid-template-columns: 1fr; }
    &--md-cols-2 { grid-template-columns: repeat(2, 1fr); }
    &--md-cols-3 { grid-template-columns: repeat(3, 1fr); }
    &--md-cols-4 { grid-template-columns: repeat(4, 1fr); }
    &--md-cols-6 { grid-template-columns: repeat(6, 1fr); }
  }
  
  @include breakpoint('lg') {
    &--lg-cols-1 { grid-template-columns: 1fr; }
    &--lg-cols-2 { grid-template-columns: repeat(2, 1fr); }
    &--lg-cols-3 { grid-template-columns: repeat(3, 1fr); }
    &--lg-cols-4 { grid-template-columns: repeat(4, 1fr); }
    &--lg-cols-6 { grid-template-columns: repeat(6, 1fr); }
    &--lg-cols-12 { grid-template-columns: repeat(12, 1fr); }
  }
}

// Advanced Flexbox System
.flex {
  display: flex;
  
  &--row { flex-direction: row; }
  &--col { flex-direction: column; }
  &--row-reverse { flex-direction: row-reverse; }
  &--col-reverse { flex-direction: column-reverse; }
  
  &--wrap { flex-wrap: wrap; }
  &--nowrap { flex-wrap: nowrap; }
  &--wrap-reverse { flex-wrap: wrap-reverse; }
  
  &--justify-start { justify-content: flex-start; }
  &--justify-end { justify-content: flex-end; }
  &--justify-center { justify-content: center; }
  &--justify-between { justify-content: space-between; }
  &--justify-around { justify-content: space-around; }
  &--justify-evenly { justify-content: space-evenly; }
  
  &--items-start { align-items: flex-start; }
  &--items-end { align-items: flex-end; }
  &--items-center { align-items: center; }
  &--items-baseline { align-items: baseline; }
  &--items-stretch { align-items: stretch; }
  
  &--content-start { align-content: flex-start; }
  &--content-end { align-content: flex-end; }
  &--content-center { align-content: center; }
  &--content-between { align-content: space-between; }
  &--content-around { align-content: space-around; }
  &--content-evenly { align-content: space-evenly; }
}

// Container System
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
  
  @each $breakpoint, $max-width in $container-max-widths {
    @include breakpoint($breakpoint) {
      max-width: $max-width;
    }
  }
  
  &--fluid {
    max-width: none;
  }
  
  &--narrow {
    @each $breakpoint, $max-width in $container-max-widths {
      @include breakpoint($breakpoint) {
        max-width: $max-width * 0.75;
      }
    }
  }
}
```

### Phase 2: Advanced CSS Techniques (2-3 hours)

**Step 2.1: Modern Layout Patterns**

```scss
// Advanced Layout Patterns
// File: src/styles/objects/_layout.scss

// CSS Subgrid Implementation
.layout-subgrid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
  
  &__item {
    display: grid;
    grid-template-columns: subgrid;
    grid-column: span 4;
    
    @supports not (grid-template-columns: subgrid) {
      // Fallback for browsers without subgrid support
      display: flex;
      flex-direction: column;
    }
  }
}

// Container Queries Implementation
.adaptive-card {
  container-type: inline-size;
  container-name: card;
  
  .card__content {
    padding: var(--space-4);
  }
  
  .card__image {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  // Container query breakpoints
  @container card (min-width: 300px) {
    .card__content {
      padding: var(--space-6);
    }
    
    .card__image {
      height: 250px;
    }
  }
  
  @container card (min-width: 400px) {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: var(--space-4);
    
    .card__image {
      height: auto;
    }
  }
}

// Advanced Grid Areas Layout
.dashboard-layout {
  display: grid;
  min-height: 100vh;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 250px 1fr;
  gap: var(--space-4);
  
  @include breakpoint('lg', 'down') {
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
    grid-template-columns: 1fr;
    grid-template-rows: auto 1fr auto auto;
  }
  
  &__header {
    grid-area: header;
    background: var(--color-surface);
    padding: var(--space-4);
    border-bottom: 1px solid var(--color-gray-200);
  }
  
  &__sidebar {
    grid-area: sidebar;
    background: var(--color-surface);
    padding: var(--space-4);
    border-right: 1px solid var(--color-gray-200);
    
    @include breakpoint('lg', 'down') {
      border-right: none;
      border-top: 1px solid var(--color-gray-200);
    }
  }
  
  &__main {
    grid-area: main;
    padding: var(--space-6);
    overflow-y: auto;
  }
  
  &__footer {
    grid-area: footer;
    background: var(--color-surface);
    padding: var(--space-4);
    border-top: 1px solid var(--color-gray-200);
  }
}

// Masonry Layout with CSS Grid
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: var(--space-4);
  
  &__item {
    break-inside: avoid;
    margin-bottom: var(--space-4);
    
    // Modern masonry with grid-template-rows: masonry
    @supports (grid-template-rows: masonry) {
      .masonry-grid {
        grid-template-rows: masonry;
        
        .masonry-grid__item {
          margin-bottom: 0;
        }
      }
    }
  }
}

// Sticky Header with CSS Variables
.sticky-header {
  --header-height: 60px;
  
  position: sticky;
  top: 0;
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--color-gray-200);
  z-index: var(--z-sticky);
  
  // Account for header height in main content
  ~ .main-content {
    scroll-margin-top: var(--header-height);
  }
}

// Responsive Typography with Clamp
.responsive-text {
  &--hero {
    font-size: clamp(2rem, 5vw, 4rem);
    line-height: clamp(2.2rem, 5.5vw, 4.4rem);
  }
  
  &--title {
    font-size: clamp(1.5rem, 3.5vw, 2.5rem);
    line-height: clamp(1.7rem, 4vw, 2.8rem);
  }
  
  &--body {
    font-size: clamp(1rem, 2.5vw, 1.125rem);
    line-height: clamp(1.5rem, 3.75vw, 1.6875rem);
  }
}
```

**Step 2.2: Advanced CSS Features and Animations**

```scss
// Advanced CSS Features
// File: src/styles/components/_advanced.scss

// CSS Logical Properties
.logical-spacing {
  margin-block: var(--space-4);
  margin-inline: var(--space-6);
  padding-block: var(--space-2);
  padding-inline: var(--space-4);
  border-inline-start: 2px solid var(--color-primary-500);
  border-radius: var(--radius-md);
}

// Modern CSS Scroll Snap
.scroll-container {
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  overflow-x: auto;
  display: flex;
  gap: var(--space-4);
  padding: var(--space-4);
  
  &__item {
    scroll-snap-align: start;
    scroll-snap-stop: always;
    flex: 0 0 auto;
    width: 300px;
    height: 200px;
    border-radius: var(--radius-lg);
    background: var(--color-surface);
    
    // Smooth scrolling enhancement
    scroll-margin-left: var(--space-4);
  }
  
  // Hide scrollbar while maintaining functionality
  scrollbar-width: none;
  -ms-overflow-style: none;
  
  &::-webkit-scrollbar {
    display: none;
  }
}

// Advanced CSS Animations
@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translate3d(0, 30px, 0);
  }
  to {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}

@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes shimmer {
  0% {
    background-position: -200px 0;
  }
  100% {
    background-position: calc(200px + 100%) 0;
  }
}

// Animation Utilities
.animate-slide-up {
  animation: slideInUp 0.3s ease-out;
}

.animate-fade-scale {
  animation: fadeInScale 0.2s ease-out;
}

.animate-shimmer {
  animation: shimmer 2s linear infinite;
  background: linear-gradient(
    90deg,
    var(--color-gray-200) 0%,
    var(--color-gray-100) 50%,
    var(--color-gray-200) 100%
  );
  background-size: 200px 100%;
}

// CSS Custom Animations with Variables
.loading-spinner {
  --size: 40px;
  --border-width: 4px;
  --speed: 1s;
  
  width: var(--size);
  height: var(--size);
  border: var(--border-width) solid var(--color-gray-200);
  border-top: var(--border-width) solid var(--color-primary-500);
  border-radius: 50%;
  animation: spin var(--speed) linear infinite;
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  &--small {
    --size: 20px;
    --border-width: 2px;
  }
  
  &--large {
    --size: 60px;
    --border-width: 6px;
  }
  
  &--slow {
    --speed: 2s;
  }
  
  &--fast {
    --speed: 0.5s;
  }
}

// Modern CSS Backdrop Filters
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  
  // Fallback for browsers without backdrop-filter
  @supports not (backdrop-filter: blur(10px)) {
    background: rgba(255, 255, 255, 0.9);
  }
}

// CSS Shapes and Clip Path
.hero-section {
  --clip-height: 100px;
  
  background: linear-gradient(135deg, var(--color-primary-500), var(--color-primary-600));
  padding: var(--space-20) 0;
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--clip-height)), 0 100%);
  color: white;
  
  @include breakpoint('md', 'down') {
    --clip-height: 50px;
  }
}

// Advanced CSS Houdini (if supported)
@supports (background: paint(worklet)) {
  .custom-border {
    background: paint(fancy-border);
    --border-color: var(--color-primary-500);
    --border-width: 2px;
  }
}

// Modern CSS Aspect Ratio
.aspect-ratio-container {
  aspect-ratio: 16 / 9;
  
  // Fallback for browsers without aspect-ratio support
  @supports not (aspect-ratio: 16 / 9) {
    position: relative;
    padding-bottom: 56.25%; // 9/16 = 0.5625
    height: 0;
    
    > * {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }
  }
  
  &--square {
    aspect-ratio: 1 / 1;
    
    @supports not (aspect-ratio: 1 / 1) {
      padding-bottom: 100%;
    }
  }
  
  &--portrait {
    aspect-ratio: 3 / 4;
    
    @supports not (aspect-ratio: 3 / 4) {
      padding-bottom: 133.33%;
    }
  }
}
```

### Phase 3: Performance Optimization and Accessibility (2-3 hours)

**Step 3.1: CSS Performance Optimization**

```scss
// Performance Optimization Strategies
// File: src/styles/optimization/_performance.scss

// Critical CSS Inlining Strategy
.above-fold {
  // Critical styles for above-the-fold content
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
  padding: var(--space-4);
  background: var(--color-background);
  color: var(--color-text-primary);
  font-family: system-ui, -apple-system, sans-serif;
  line-height: var(--leading-normal);
}

// Efficient Animation Classes
.will-animate {
  will-change: transform, opacity;
  
  &:not(.animating) {
    will-change: auto; // Remove will-change when not animating
  }
}

// GPU-Accelerated Transformations
.gpu-accelerated {
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 1000px;
}

// Efficient Hover Effects
.efficient-hover {
  transition: var(--transition-colors);
  
  @media (hover: hover) {
    &:hover {
      color: var(--color-primary-600);
      background-color: var(--color-primary-50);
    }
  }
  
  // Touch-friendly active states
  &:active {
    color: var(--color-primary-700);
    background-color: var(--color-primary-100);
  }
}

// Optimized Image Loading
.optimized-image {
  img {
    width: 100%;
    height: auto;
    loading: lazy;
    decoding: async;
    
    // Prevent layout shift during loading
    aspect-ratio: attr(width) / attr(height);
    object-fit: cover;
  }
  
  // Placeholder while loading
  &::before {
    content: '';
    display: block;
    background: var(--color-gray-200);
    animation: shimmer 2s ease-in-out infinite;
  }
  
  img[data-loaded="true"] + &::before {
    display: none;
  }
}

// Contain Layout Shifts
.layout-stable {
  contain: layout style paint;
  content-visibility: auto;
  contain-intrinsic-size: 200px;
}

// Efficient Typography Loading
.font-display-optimization {
  font-display: swap; // Use system font until custom font loads
  
  &.font-loaded {
    font-display: block; // Switch to block once loaded
  }
}

// Memory-Efficient Patterns
.memory-efficient {
  // Avoid expensive box-shadow animations
  transition: transform var(--transition-default);
  
  &:hover {
    transform: translateY(-2px);
  }
  
  // Use transform instead of changing position properties
  &.moved {
    transform: translate(100px, 50px);
  }
}
```

**Step 3.2: Comprehensive Accessibility Implementation**

```scss
// Accessibility-First CSS
// File: src/styles/accessibility/_a11y.scss

// Screen Reader Only Utility
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
  clip-path: inset(50%);
}

// Not Screen Reader Only (reveals sr-only content)
.not-sr-only {
  position: static !important;
  width: auto !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
  overflow: visible !important;
  clip: auto !important;
  white-space: normal !important;
  clip-path: none;
}

// Focus Management
.focus-visible-only {
  outline: none;
  
  &:focus-visible {
    outline: 2px solid var(--color-primary-500);
    outline-offset: 2px;
    border-radius: var(--radius-sm);
  }
}

.focus-ring {
  position: relative;
  
  &:focus-visible::after {
    content: '';
    position: absolute;
    inset: -2px;
    border: 2px solid var(--color-primary-500);
    border-radius: calc(var(--radius-md) + 2px);
    pointer-events: none;
  }
}

// Skip Links
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--color-background);
  color: var(--color-text-primary);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  text-decoration: none;
  font-weight: var(--font-medium);
  z-index: var(--z-tooltip);
  border: 2px solid var(--color-primary-500);
  
  &:focus {
    top: 6px;
  }
}

// High Contrast Mode Support
@media (prefers-contrast: high) {
  .high-contrast-support {
    border: 2px solid currentColor;
    background: Canvas;
    color: CanvasText;
  }
  
  .button {
    border: 2px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
    
    &:hover,
    &:focus {
      background: Highlight;
      color: HighlightText;
    }
  }
}

// Reduced Motion Support
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

// Color Contrast Utilities
.contrast-aa {
  // WCAG AA compliant text colors
  &--on-light {
    color: #212529; // 9.95:1 ratio on white
  }
  
  &--on-dark {
    color: #f8f9fa; // 17.35:1 ratio on black
  }
  
  &--primary {
    color: #0d47a1; // 4.5:1 ratio minimum
  }
}

.contrast-aaa {
  // WCAG AAA compliant text colors
  &--on-light {
    color: #000000; // 21:1 ratio on white
  }
  
  &--on-dark {
    color: #ffffff; // 21:1 ratio on black
  }
}

// Accessible Form Styling
.form-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  
  &__label {
    font-weight: var(--font-medium);
    color: var(--color-text-primary);
    
    &--required::after {
      content: ' *';
      color: var(--color-error);
      aria-label: 'required';
    }
  }
  
  &__input {
    padding: var(--space-3);
    border: 2px solid var(--color-gray-300);
    border-radius: var(--radius-md);
    font-size: var(--text-base);
    background: var(--color-background);
    color: var(--color-text-primary);
    transition: var(--transition-colors);
    
    &:focus {
      outline: none;
      border-color: var(--color-primary-500);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    &:invalid {
      border-color: var(--color-error);
    }
    
    &[aria-invalid="true"] {
      border-color: var(--color-error);
    }
  }
  
  &__error {
    color: var(--color-error);
    font-size: var(--text-sm);
    margin-top: var(--space-1);
    
    &::before {
      content: '⚠ ';
      margin-right: var(--space-1);
    }
  }
  
  &__help {
    color: var(--color-text-secondary);
    font-size: var(--text-sm);
  }
}

// Accessible Button States
.button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-4);
  border: none;
  border-radius: var(--radius-md);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
  transition: var(--transition-all);
  
  &:disabled {
    cursor: not-allowed;
    opacity: 0.6;
    
    &:hover,
    &:focus {
      transform: none;
    }
  }
  
  &[aria-pressed="true"] {
    background: var(--color-primary-600);
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  &--loading {
    color: transparent;
    
    &::after {
      content: '';
      position: absolute;
      width: 16px;
      height: 16px;
      border: 2px solid currentColor;
      border-top-color: transparent;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }
  }
}

// Accessible Modal/Dialog
.modal {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  
  &__backdrop {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(4px);
  }
  
  &__content {
    position: relative;
    background: var(--color-background);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-2xl);
    max-width: 500px;
    max-height: 90vh;
    overflow-y: auto;
    
    // Ensure focus stays within modal
    &:focus-within {
      outline: 2px solid var(--color-primary-500);
      outline-offset: -2px;
    }
  }
  
  &__close {
    position: absolute;
    top: var(--space-4);
    right: var(--space-4);
    padding: var(--space-2);
    background: none;
    border: none;
    font-size: var(--text-xl);
    cursor: pointer;
    border-radius: var(--radius-sm);
    
    &:focus-visible {
      outline: 2px solid var(--color-primary-500);
    }
  }
}
```

## 📊 Success Criteria

### Performance Metrics
- **First Contentful Paint**: <1.5s on 3G networks
- **Largest Contentful Paint**: <2.5s on 3G networks
- **Cumulative Layout Shift**: <0.1
- **CSS Bundle Size**: <50KB gzipped for critical CSS

### Accessibility Compliance
- **WCAG 2.1 AA Compliance**: 100% for all interactive elements
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Keyboard Navigation**: 100% keyboard accessible
- **Screen Reader Support**: Full compatibility with major screen readers

### Design System Consistency
- **Design Token Usage**: 100% use of design system tokens
- **Component Reusability**: >90% of components reused across projects
- **Cross-browser Compatibility**: Support for last 2 versions of major browsers
- **Responsive Coverage**: 100% responsive design across all breakpoints

## 🎯 Deliverables

Upon completion of responsive design and CSS architecture implementation:

- ✅ **Scalable CSS Architecture** with ITCSS methodology and modern CSS features
- ✅ **Comprehensive Design System** with design tokens and consistent patterns
- ✅ **Advanced Grid and Flexbox Systems** with responsive breakpoints and container queries
- ✅ **Performance-Optimized CSS** with critical CSS extraction and efficient animations
- ✅ **Accessibility-First Implementation** with WCAG 2.1 AA compliance and inclusive design
- ✅ **Modern CSS Features** including custom properties, logical properties, and advanced selectors
- ✅ **Cross-Device Compatibility** with responsive design and progressive enhancement
- ✅ **Documentation and Style Guide** with comprehensive usage examples and best practices

---

*This comprehensive responsive design and CSS architecture provides a scalable, maintainable, and accessible foundation for modern web applications using cutting-edge CSS techniques and performance optimization strategies.*