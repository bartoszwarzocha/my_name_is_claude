# React Component Development with TypeScript

**Agent Type: frontend-engineer**
**Complexity Level: Expert**
**Estimated Duration: 4-8 hours**

---

## 🎯 Mission

Develop high-quality, reusable React components using TypeScript with focus on performance, accessibility, maintainability, and modern React patterns including hooks, context, and concurrent features.

## 📋 Process Framework

### Phase 1: Component Architecture and Design (1-2 hours)

**Step 1.1: Component Architecture Planning**

```typescript
// Modern React Component Architecture Framework
interface ComponentArchitectureFramework {
  designPatterns: {
    compositionPattern: {
      compoundComponents: 'tabs_modal_accordion_flexible_api_design';
      renderProps: 'data_fetching_state_management_logic_sharing';
      higherOrderComponents: 'cross_cutting_concerns_authentication_logging';
      customHooks: 'stateful_logic_reuse_business_logic_extraction';
    };
    stateManagement: {
      localState: 'component_specific_ui_state_useState_useReducer';
      contextApi: 'global_theme_user_settings_cross_component_state';
      externalState: 'redux_zustand_jotai_complex_application_state';
      serverState: 'react_query_swr_apollo_server_data_management';
    };
    performancePatterns: {
      memoization: 'react_memo_useMemo_useCallback_expensive_calculations';
      lazyLoading: 'react_lazy_suspense_code_splitting_route_components';
      virtualization: 'react_window_react_virtualized_large_list_performance';
      concurrentFeatures: 'concurrent_mode_suspense_transitions_user_experience';
    };
  };
}

class ReactComponentArchitect {
  private designSystem: DesignSystem;
  private performanceRequirements: PerformanceRequirements;
  
  constructor(designSystem: DesignSystem, requirements: PerformanceRequirements) {
    this.designSystem = designSystem;
    this.performanceRequirements = requirements;
  }
  
  planComponentHierarchy(): ComponentHierarchyPlan {
    return {
      atomicDesignStructure: this.createAtomicDesignStructure(),
      componentComposition: this.planComponentComposition(),
      stateArchitecture: this.designStateArchitecture(),
      performanceStrategy: this.createPerformanceStrategy()
    };
  }
  
  private createAtomicDesignStructure(): AtomicDesignStructure {
    return {
      atoms: {
        purpose: 'basic_building_blocks_ui_elements',
        examples: [
          'Button', 'Input', 'Label', 'Icon', 'Avatar', 'Badge', 'Spinner'
        ],
        characteristics: [
          'no_dependencies_other_components',
          'highly_reusable_consistent_styling',
          'minimal_props_simple_api',
          'comprehensive_prop_types_validation'
        ]
      },
      molecules: {
        purpose: 'simple_component_combinations_specific_functionality',
        examples: [
          'SearchBox', 'FormField', 'NavigationItem', 'Card', 'DropdownMenu'
        ],
        characteristics: [
          'composed_of_atoms_minimal_molecules',
          'single_responsibility_focused_functionality',
          'reusable_across_different_contexts',
          'event_handling_user_interaction_logic'
        ]
      },
      organisms: {
        purpose: 'complex_ui_sections_business_logic_integration',
        examples: [
          'Header', 'ProductList', 'UserProfile', 'Dashboard', 'DataTable'
        ],
        characteristics: [
          'composed_of_molecules_atoms',
          'business_logic_integration_data_fetching',
          'context_specific_functionality',
          'state_management_side_effects'
        ]
      },
      templates: {
        purpose: 'page_layout_structure_content_placement',
        examples: [
          'PageLayout', 'AuthLayout', 'DashboardLayout', 'FormLayout'
        ],
        characteristics: [
          'layout_grid_responsive_design',
          'content_area_definition_slot_management',
          'routing_navigation_integration',
          'global_state_context_providers'
        ]
      },
      pages: {
        purpose: 'complete_user_interfaces_route_components',
        examples: [
          'HomePage', 'ProductPage', 'UserDashboard', 'CheckoutPage'
        ],
        characteristics: [
          'route_level_components_url_mapping',
          'data_fetching_server_state_management',
          'seo_meta_tags_social_sharing',
          'error_boundary_fallback_handling'
        ]
      }
    };
  }
  
  private planComponentComposition(): ComponentCompositionPlan {
    return {
      compoundComponentPattern: {
        implementation: `
        // Compound Component Pattern Example
        interface TabsContextValue {
          activeTab: string;
          setActiveTab: (tab: string) => void;
        }
        
        const TabsContext = createContext<TabsContextValue | null>(null);
        
        export const Tabs = ({ 
          children, 
          defaultTab, 
          onChange 
        }: TabsProps) => {
          const [activeTab, setActiveTab] = useState(defaultTab);
          
          const handleTabChange = useCallback((tab: string) => {
            setActiveTab(tab);
            onChange?.(tab);
          }, [onChange]);
          
          const value = useMemo(() => ({
            activeTab,
            setActiveTab: handleTabChange
          }), [activeTab, handleTabChange]);
          
          return (
            <TabsContext.Provider value={value}>
              <div className="tabs-container" role="tablist">
                {children}
              </div>
            </TabsContext.Provider>
          );
        };
        
        export const TabsList = ({ children }: TabsListProps) => (
          <div className="tabs-list" role="tablist">
            {children}
          </div>
        );
        
        export const TabsTrigger = ({ 
          value, 
          children, 
          disabled 
        }: TabsTriggerProps) => {
          const context = useContext(TabsContext);
          if (!context) throw new Error('TabsTrigger must be used within Tabs');
          
          const { activeTab, setActiveTab } = context;
          const isActive = activeTab === value;
          
          return (
            <button
              role="tab"
              aria-selected={isActive}
              aria-controls={\`panel-\${value}\`}
              disabled={disabled}
              className={\`tab-trigger \${isActive ? 'active' : ''}\`}
              onClick={() => setActiveTab(value)}
            >
              {children}
            </button>
          );
        };
        
        export const TabsContent = ({ 
          value, 
          children 
        }: TabsContentProps) => {
          const context = useContext(TabsContext);
          if (!context) throw new Error('TabsContent must be used within Tabs');
          
          const { activeTab } = context;
          
          if (activeTab !== value) return null;
          
          return (
            <div
              role="tabpanel"
              id={\`panel-\${value}\`}
              aria-labelledby={\`tab-\${value}\`}
              className="tab-content"
            >
              {children}
            </div>
          );
        };
        
        // Usage:
        // <Tabs defaultTab="overview">
        //   <TabsList>
        //     <TabsTrigger value="overview">Overview</TabsTrigger>
        //     <TabsTrigger value="analytics">Analytics</TabsTrigger>
        //   </TabsList>
        //   <TabsContent value="overview">Overview content</TabsContent>
        //   <TabsContent value="analytics">Analytics content</TabsContent>
        // </Tabs>
        `,
        benefits: [
          'flexible_api_consumer_control_composition',
          'implicit_state_sharing_context_communication',
          'extensible_design_new_parts_easy_addition',
          'accessibility_built_in_proper_aria_attributes'
        ]
      },
      renderPropPattern: {
        implementation: `
        // Render Props Pattern for Data Fetching
        interface DataFetcherProps<T> {
          url: string;
          children: (state: {
            data: T | null;
            loading: boolean;
            error: Error | null;
            refetch: () => void;
          }) => React.ReactNode;
          onSuccess?: (data: T) => void;
          onError?: (error: Error) => void;
        }
        
        export function DataFetcher<T>({ 
          url, 
          children, 
          onSuccess, 
          onError 
        }: DataFetcherProps<T>) {
          const [data, setData] = useState<T | null>(null);
          const [loading, setLoading] = useState(false);
          const [error, setError] = useState<Error | null>(null);
          
          const fetchData = useCallback(async () => {
            try {
              setLoading(true);
              setError(null);
              const response = await fetch(url);
              if (!response.ok) throw new Error(response.statusText);
              const result = await response.json();
              setData(result);
              onSuccess?.(result);
            } catch (err) {
              const error = err instanceof Error ? err : new Error('Unknown error');
              setError(error);
              onError?.(error);
            } finally {
              setLoading(false);
            }
          }, [url, onSuccess, onError]);
          
          useEffect(() => {
            fetchData();
          }, [fetchData]);
          
          return <>{children({ data, loading, error, refetch: fetchData })}</>;
        }
        
        // Usage:
        // <DataFetcher<User[]> url="/api/users">
        //   {({ data, loading, error, refetch }) => {
        //     if (loading) return <LoadingSpinner />;
        //     if (error) return <ErrorMessage error={error} onRetry={refetch} />;
        //     return <UserList users={data} />;
        //   }}
        // </DataFetcher>
        `,
        benefits: [
          'logic_reuse_different_ui_implementations',
          'inversion_of_control_consumer_decides_rendering',
          'testability_logic_ui_separate_testing',
          'flexibility_different_loading_error_states'
        ]
      }
    };
  }
}
```

**Step 1.2: TypeScript Integration and Type Safety**

```typescript
// Advanced TypeScript Patterns for React Components
interface TypeSafetyFramework {
  strictTypeDefinitions: {
    componentProps: 'comprehensive_prop_types_optional_required_validation';
    eventHandlers: 'type_safe_event_handler_parameter_validation';
    genericComponents: 'reusable_components_type_parameter_flexibility';
    forwardedRefs: 'ref_forwarding_imperative_handle_type_safety';
  };
}

// Generic Type-Safe Component Patterns
interface BaseComponentProps {
  className?: string;
  children?: React.ReactNode;
  testId?: string;
}

// Discriminated Union Props Pattern
type ButtonVariant = 'primary' | 'secondary' | 'destructive';
type ButtonSize = 'sm' | 'md' | 'lg';

interface BaseButtonProps extends BaseComponentProps {
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: boolean;
  loading?: boolean;
}

interface ButtonWithOnClick extends BaseButtonProps {
  onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
  href?: never;
  type?: 'button' | 'submit' | 'reset';
}

interface ButtonAsLink extends BaseButtonProps {
  href: string;
  onClick?: never;
  type?: never;
  target?: '_blank' | '_self';
  rel?: string;
}

type ButtonProps = ButtonWithOnClick | ButtonAsLink;

// Type-Safe Button Component Implementation
export const Button = React.forwardRef<HTMLButtonElement | HTMLAnchorElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', className, children, testId, ...props }, ref) => {
    const baseClasses = `btn btn-${variant} btn-${size}`;
    const classes = className ? `${baseClasses} ${className}` : baseClasses;
    
    // Type guard to determine component type
    if ('href' in props) {
      return (
        <a
          ref={ref as React.Ref<HTMLAnchorElement>}
          href={props.href}
          target={props.target}
          rel={props.target === '_blank' ? 'noopener noreferrer' : props.rel}
          className={classes}
          data-testid={testId}
        >
          {children}
        </a>
      );
    }
    
    return (
      <button
        ref={ref as React.Ref<HTMLButtonElement>}
        type={props.type || 'button'}
        onClick={props.onClick}
        disabled={props.disabled || props.loading}
        className={classes}
        data-testid={testId}
        aria-busy={props.loading}
      >
        {props.loading ? (
          <>
            <LoadingSpinner size="sm" />
            <span className="sr-only">Loading...</span>
          </>
        ) : (
          children
        )}
      </button>
    );
  }
);

Button.displayName = 'Button';

// Generic Data Display Component with Type Safety
interface DataDisplayProps<T> {
  data: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string | number;
  emptyState?: React.ReactNode;
  loading?: boolean;
  error?: Error | null;
  className?: string;
  virtualized?: boolean;
  itemHeight?: number;
}

export function DataDisplay<T>({
  data,
  renderItem,
  keyExtractor,
  emptyState,
  loading,
  error,
  className,
  virtualized = false,
  itemHeight = 50
}: DataDisplayProps<T>) {
  // Loading state
  if (loading) {
    return (
      <div className={`data-display loading ${className || ''}`}>
        <LoadingSpinner />
      </div>
    );
  }
  
  // Error state
  if (error) {
    return (
      <div className={`data-display error ${className || ''}`}>
        <ErrorMessage error={error} />
      </div>
    );
  }
  
  // Empty state
  if (data.length === 0) {
    return (
      <div className={`data-display empty ${className || ''}`}>
        {emptyState || <div>No data available</div>}
      </div>
    );
  }
  
  // Virtualized rendering for large datasets
  if (virtualized) {
    return (
      <FixedSizeList
        height={400}
        itemCount={data.length}
        itemSize={itemHeight}
        className={className}
      >
        {({ index, style }) => (
          <div style={style} key={keyExtractor(data[index])}>
            {renderItem(data[index], index)}
          </div>
        )}
      </FixedSizeList>
    );
  }
  
  // Standard rendering
  return (
    <div className={`data-display ${className || ''}`}>
      {data.map((item, index) => (
        <div key={keyExtractor(item)}>
          {renderItem(item, index)}
        </div>
      ))}
    </div>
  );
}

// Advanced Hook Patterns with TypeScript
interface UseToggleReturn {
  value: boolean;
  toggle: () => void;
  setTrue: () => void;
  setFalse: () => void;
  setValue: (value: boolean) => void;
}

export function useToggle(initialValue = false): UseToggleReturn {
  const [value, setValue] = useState(initialValue);
  
  const toggle = useCallback(() => setValue(prev => !prev), []);
  const setTrue = useCallback(() => setValue(true), []);
  const setFalse = useCallback(() => setValue(false), []);
  const setValueCallback = useCallback((newValue: boolean) => setValue(newValue), []);
  
  return useMemo(
    () => ({
      value,
      toggle,
      setTrue,
      setFalse,
      setValue: setValueCallback
    }),
    [value, toggle, setTrue, setFalse, setValueCallback]
  );
}

// Type-safe API hook with error handling
interface ApiState<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
}

interface UseApiReturn<T> extends ApiState<T> {
  refetch: () => Promise<void>;
  mutate: (data: T) => void;
}

export function useApi<T>(url: string): UseApiReturn<T> {
  const [state, setState] = useState<ApiState<T>>({
    data: null,
    loading: true,
    error: null
  });
  
  const fetchData = useCallback(async () => {
    try {
      setState(prev => ({ ...prev, loading: true, error: null }));
      const response = await fetch(url);
      if (!response.ok) throw new Error(response.statusText);
      const data = await response.json();
      setState({ data, loading: false, error: null });
    } catch (error) {
      setState({
        data: null,
        loading: false,
        error: error instanceof Error ? error : new Error('Unknown error')
      });
    }
  }, [url]);
  
  const mutate = useCallback((newData: T) => {
    setState(prev => ({ ...prev, data: newData }));
  }, []);
  
  useEffect(() => {
    fetchData();
  }, [fetchData]);
  
  return {
    ...state,
    refetch: fetchData,
    mutate
  };
}
```

### Phase 2: Modern React Patterns Implementation (2-3 hours)

**Step 2.1: Concurrent Features and Suspense**

```typescript
// React Concurrent Features Implementation
import { 
  Suspense, 
  lazy, 
  startTransition, 
  useDeferredValue, 
  useTransition,
  useMemo,
  useState,
  useCallback
} from 'react';

// Code Splitting with React.lazy and Suspense
const LazyDashboard = lazy(() => import('./Dashboard'));
const LazyUserProfile = lazy(() => import('./UserProfile'));
const LazySettings = lazy(() => import('./Settings'));

// Route-level code splitting
export const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route
          path="/dashboard"
          element={
            <Suspense fallback={<PageLoadingSkeleton />}>
              <LazyDashboard />
            </Suspense>
          }
        />
        <Route
          path="/profile"
          element={
            <Suspense fallback={<PageLoadingSkeleton />}>
              <LazyUserProfile />
            </Suspense>
          }
        />
        <Route
          path="/settings"
          element={
            <Suspense fallback={<PageLoadingSkeleton />}>
              <LazySettings />
            </Suspense>
          }
        />
      </Routes>
    </Router>
  );
};

// Advanced Search with useTransition for non-blocking updates
interface SearchResultsProps {
  query: string;
  filters: SearchFilters;
}

export const SearchResults: React.FC<SearchResultsProps> = ({ 
  query, 
  filters 
}) => {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isPending, startTransition] = useTransition();
  
  // Defer expensive filtering operations
  const deferredQuery = useDeferredValue(query);
  const deferredFilters = useDeferredValue(filters);
  
  // Expensive search operation
  const filteredResults = useMemo(() => {
    if (!deferredQuery.trim()) return [];
    
    return results.filter(result => {
      // Complex filtering logic
      const matchesQuery = result.title
        .toLowerCase()
        .includes(deferredQuery.toLowerCase());
      const matchesFilters = Object.entries(deferredFilters).every(
        ([key, value]) => {
          if (!value) return true;
          return result[key as keyof SearchResult] === value;
        }
      );
      
      return matchesQuery && matchesFilters;
    });
  }, [results, deferredQuery, deferredFilters]);
  
  // Non-blocking search API call
  const handleSearch = useCallback((newQuery: string) => {
    startTransition(() => {
      // Simulate API call
      fetchSearchResults(newQuery).then(setResults);
    });
  }, []);
  
  useEffect(() => {
    if (deferredQuery) {
      handleSearch(deferredQuery);
    }
  }, [deferredQuery, handleSearch]);
  
  return (
    <div className="search-results">
      {isPending && (
        <div className="search-pending">
          <LoadingSpinner size="sm" />
          <span>Searching...</span>
        </div>
      )}
      
      <Suspense fallback={<SearchResultsSkeleton />}>
        <VirtualizedList
          items={filteredResults}
          renderItem={(result) => <SearchResultItem result={result} />}
          keyExtractor={(result) => result.id}
        />
      </Suspense>
    </div>
  );
};

// Error Boundaries for Concurrent Features
interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

class ConcurrentErrorBoundary extends Component<
  { children: React.ReactNode; fallback?: React.ComponentType<{ error: Error }> },
  ErrorBoundaryState
> {
  constructor(props: any) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }
  
  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    // Log error to monitoring service
    console.error('Concurrent feature error:', error, errorInfo);
    
    // Report to error tracking service
    reportError(error, {
      component: 'ConcurrentErrorBoundary',
      errorInfo,
      timestamp: new Date().toISOString()
    });
  }
  
  render() {
    if (this.state.hasError) {
      const FallbackComponent = this.props.fallback || DefaultErrorFallback;
      return <FallbackComponent error={this.state.error!} />;
    }
    
    return this.props.children;
  }
}

// Suspense-enabled Data Fetching Component
interface SuspenseDataFetcherProps<T> {
  resource: SuspenseResource<T>;
  children: (data: T) => React.ReactNode;
}

export function SuspenseDataFetcher<T>({ 
  resource, 
  children 
}: SuspenseDataFetcherProps<T>) {
  const data = resource.read();
  return <>{children(data)}</>;
}

// Resource pattern for Suspense
class SuspenseResource<T> {
  private promise: Promise<T> | null = null;
  private status: 'pending' | 'success' | 'error' = 'pending';
  private result: T | Error | null = null;
  
  constructor(private fetcher: () => Promise<T>) {}
  
  read(): T {
    if (this.status === 'pending') {
      if (!this.promise) {
        this.promise = this.fetcher()
          .then(
            (data) => {
              this.status = 'success';
              this.result = data;
            },
            (error) => {
              this.status = 'error';
              this.result = error;
            }
          );
      }
      throw this.promise;
    }
    
    if (this.status === 'error') {
      throw this.result;
    }
    
    return this.result as T;
  }
}

// Usage with Suspense
export const UserDashboard = () => {
  const userResource = useMemo(
    () => new SuspenseResource(() => fetchUser()),
    []
  );
  
  return (
    <ConcurrentErrorBoundary fallback={UserErrorFallback}>
      <Suspense fallback={<UserDashboardSkeleton />}>
        <SuspenseDataFetcher resource={userResource}>
          {(user) => (
            <div className="user-dashboard">
              <UserProfile user={user} />
              <UserActivity userId={user.id} />
              <UserSettings userId={user.id} />
            </div>
          )}
        </SuspenseDataFetcher>
      </Suspense>
    </ConcurrentErrorBoundary>
  );
};
```

**Step 2.2: Performance Optimization Patterns**

```typescript
// Advanced Performance Optimization Patterns
import { 
  memo, 
  useMemo, 
  useCallback, 
  useRef, 
  useLayoutEffect,
  useImperativeHandle,
  forwardRef
} from 'react';

// Memoization Best Practices
interface ExpensiveListItemProps {
  item: ListItem;
  onSelect: (id: string) => void;
  isSelected: boolean;
  index: number;
}

const ExpensiveListItem = memo<ExpensiveListItemProps>(({
  item,
  onSelect,
  isSelected,
  index
}) => {
  // Memoize expensive calculations
  const processedData = useMemo(() => {
    // Simulate expensive computation
    return processComplexData(item);
  }, [item]);
  
  // Memoize event handlers to prevent child re-renders
  const handleClick = useCallback(() => {
    onSelect(item.id);
  }, [item.id, onSelect]);
  
  // Memoize complex styles
  const itemStyles = useMemo(() => ({
    backgroundColor: isSelected ? '#e3f2fd' : 'transparent',
    transform: `translateY(${index * 2}px)`,
    transition: 'all 0.2s ease-in-out'
  }), [isSelected, index]);
  
  return (
    <div 
      className="list-item" 
      style={itemStyles}
      onClick={handleClick}
    >
      <h3>{processedData.title}</h3>
      <p>{processedData.description}</p>
      <div className="metadata">
        {processedData.tags.map(tag => (
          <span key={tag} className="tag">{tag}</span>
        ))}
      </div>
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for optimization
  return (
    prevProps.item.id === nextProps.item.id &&
    prevProps.isSelected === nextProps.isSelected &&
    prevProps.index === nextProps.index &&
    prevProps.item.updatedAt === nextProps.item.updatedAt
  );
});

ExpensiveListItem.displayName = 'ExpensiveListItem';

// Virtual Scrolling Implementation
interface VirtualScrollerProps<T> {
  items: T[];
  itemHeight: number;
  containerHeight: number;
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string;
  overscan?: number;
}

export function VirtualScroller<T>({
  items,
  itemHeight,
  containerHeight,
  renderItem,
  keyExtractor,
  overscan = 5
}: VirtualScrollerProps<T>) {
  const [scrollTop, setScrollTop] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);
  
  // Calculate visible range
  const visibleRange = useMemo(() => {
    const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan);
    const endIndex = Math.min(
      items.length - 1,
      Math.ceil((scrollTop + containerHeight) / itemHeight) + overscan
    );
    return { startIndex, endIndex };
  }, [scrollTop, itemHeight, containerHeight, items.length, overscan]);
  
  // Generate visible items
  const visibleItems = useMemo(() => {
    const { startIndex, endIndex } = visibleRange;
    return items.slice(startIndex, endIndex + 1).map((item, index) => ({
      item,
      index: startIndex + index,
      key: keyExtractor(item)
    }));
  }, [items, visibleRange, keyExtractor]);
  
  // Handle scroll with requestAnimationFrame throttling
  const handleScroll = useCallback(
    throttle((event: React.UIEvent<HTMLDivElement>) => {
      setScrollTop(event.currentTarget.scrollTop);
    }, 16),
    []
  );
  
  const totalHeight = items.length * itemHeight;
  const { startIndex } = visibleRange;
  
  return (
    <div
      ref={containerRef}
      className="virtual-scroller"
      style={{ height: containerHeight, overflow: 'auto' }}
      onScroll={handleScroll}
    >
      <div style={{ height: totalHeight, position: 'relative' }}>
        {visibleItems.map(({ item, index, key }) => (
          <div
            key={key}
            style={{
              position: 'absolute',
              top: index * itemHeight,
              width: '100%',
              height: itemHeight
            }}
          >
            {renderItem(item, index)}
          </div>
        ))}
      </div>
    </div>
  );
}

// Intersection Observer Hook for Lazy Loading
interface UseIntersectionObserverOptions {
  threshold?: number;
  rootMargin?: string;
  root?: Element | null;
}

export function useIntersectionObserver(
  options: UseIntersectionObserverOptions = {}
) {
  const [isIntersecting, setIsIntersecting] = useState(false);
  const [entry, setEntry] = useState<IntersectionObserverEntry | null>(null);
  const elementRef = useRef<HTMLElement>(null);
  
  const { threshold = 0, rootMargin = '0px', root = null } = options;
  
  useLayoutEffect(() => {
    const element = elementRef.current;
    if (!element) return;
    
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
        setEntry(entry);
      },
      { threshold, rootMargin, root }
    );
    
    observer.observe(element);
    
    return () => {
      observer.unobserve(element);
      observer.disconnect();
    };
  }, [threshold, rootMargin, root]);
  
  return { elementRef, isIntersecting, entry };
}

// Lazy Image Component with Intersection Observer
interface LazyImageProps {
  src: string;
  alt: string;
  placeholder?: string;
  className?: string;
  width?: number;
  height?: number;
  onLoad?: () => void;
  onError?: () => void;
}

export const LazyImage: React.FC<LazyImageProps> = ({
  src,
  alt,
  placeholder,
  className,
  width,
  height,
  onLoad,
  onError
}) => {
  const { elementRef, isIntersecting } = useIntersectionObserver({
    threshold: 0.1,
    rootMargin: '50px'
  });
  
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState(false);
  
  const handleLoad = useCallback(() => {
    setLoaded(true);
    onLoad?.();
  }, [onLoad]);
  
  const handleError = useCallback(() => {
    setError(true);
    onError?.();
  }, [onError]);
  
  return (
    <div 
      ref={elementRef as React.RefObject<HTMLDivElement>}
      className={`lazy-image-container ${className || ''}`}
      style={{ width, height }}
    >
      {isIntersecting && !error && (
        <img
          src={src}
          alt={alt}
          className={`lazy-image ${loaded ? 'loaded' : 'loading'}`}
          onLoad={handleLoad}
          onError={handleError}
          style={{ width, height }}
        />
      )}
      {(!isIntersecting || !loaded || error) && (
        <div 
          className="lazy-image-placeholder"
          style={{ 
            width, 
            height, 
            backgroundImage: placeholder ? `url(${placeholder})` : undefined 
          }}
        />
      )}
    </div>
  );
};

// Performance Monitoring Hook
interface PerformanceMetrics {
  renderTime: number;
  componentUpdates: number;
  memoryUsage?: number;
}

export function usePerformanceMonitoring(componentName: string) {
  const renderCount = useRef(0);
  const renderStartTime = useRef<number>(0);
  const [metrics, setMetrics] = useState<PerformanceMetrics>({
    renderTime: 0,
    componentUpdates: 0
  });
  
  useLayoutEffect(() => {
    renderStartTime.current = performance.now();
  });
  
  useEffect(() => {
    renderCount.current += 1;
    const renderTime = performance.now() - renderStartTime.current;
    
    setMetrics(prev => ({
      renderTime,
      componentUpdates: renderCount.current,
      memoryUsage: (performance as any).memory?.usedJSHeapSize
    }));
    
    // Report metrics to monitoring service in development
    if (process.env.NODE_ENV === 'development') {
      console.log(`${componentName} Performance:`, {
        renderTime: `${renderTime.toFixed(2)}ms`,
        updates: renderCount.current,
        memoryUsage: metrics.memoryUsage ? `${(metrics.memoryUsage / 1024 / 1024).toFixed(2)}MB` : 'N/A'
      });
    }
  });
  
  return metrics;
}
```

### Phase 3: Testing and Quality Assurance (1-2 hours)

**Step 3.1: Comprehensive Testing Strategy**

```typescript
// Comprehensive Testing Framework for React Components
import { 
  render, 
  screen, 
  fireEvent, 
  waitFor, 
  within,
  act
} from '@testing-library/react';
import { renderHook, act as hookAct } from '@testing-library/react-hooks';
import userEvent from '@testing-library/user-event';
import { axe, toHaveNoViolations } from 'jest-axe';

// Extend Jest matchers
expect.extend(toHaveNoViolations);

// Test Utilities and Helpers
interface TestWrapperProps {
  children: React.ReactNode;
  theme?: Theme;
  router?: boolean;
  queryClient?: QueryClient;
}

const TestWrapper: React.FC<TestWrapperProps> = ({ 
  children, 
  theme = defaultTheme,
  router = false,
  queryClient
}) => {
  const wrapper = (
    <ThemeProvider theme={theme}>
      {queryClient ? (
        <QueryClientProvider client={queryClient}>
          {children}
        </QueryClientProvider>
      ) : (
        children
      )}
    </ThemeProvider>
  );
  
  return router ? (
    <MemoryRouter>
      {wrapper}
    </MemoryRouter>
  ) : (
    wrapper
  );
};

// Custom render function with providers
const customRender = (
  ui: React.ReactElement,
  options: {
    theme?: Theme;
    router?: boolean;
    queryClient?: QueryClient;
    ...renderOptions?: RenderOptions;
  } = {}
) => {
  const { theme, router, queryClient, ...renderOptions } = options;
  
  return render(ui, {
    wrapper: ({ children }) => (
      <TestWrapper theme={theme} router={router} queryClient={queryClient}>
        {children}
      </TestWrapper>
    ),
    ...renderOptions
  });
};

// Component Testing Examples
describe('Button Component', () => {
  it('renders with correct text and variant', () => {
    customRender(
      <Button variant="primary" onClick={jest.fn()}>
        Click me
      </Button>
    );
    
    const button = screen.getByRole('button', { name: /click me/i });
    expect(button).toBeInTheDocument();
    expect(button).toHaveClass('btn-primary');
  });
  
  it('handles click events correctly', async () => {
    const handleClick = jest.fn();
    const user = userEvent.setup();
    
    customRender(
      <Button onClick={handleClick}>
        Click me
      </Button>
    );
    
    const button = screen.getByRole('button');
    await user.click(button);
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('shows loading state correctly', () => {
    customRender(
      <Button loading onClick={jest.fn()}>
        Submit
      </Button>
    );
    
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveAttribute('aria-busy', 'true');
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });
  
  it('renders as link when href is provided', () => {
    customRender(
      <Button href="/dashboard">
        Go to Dashboard
      </Button>
    );
    
    const link = screen.getByRole('link');
    expect(link).toHaveAttribute('href', '/dashboard');
  });
  
  it('has no accessibility violations', async () => {
    const { container } = customRender(
      <Button onClick={jest.fn()}>
        Accessible Button
      </Button>
    );
    
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});

// Complex Component Integration Testing
describe('SearchResults Component', () => {
  let mockQueryClient: QueryClient;
  
  beforeEach(() => {
    mockQueryClient = new QueryClient({
      defaultOptions: {
        queries: { retry: false },
        mutations: { retry: false }
      }
    });
  });
  
  it('displays search results correctly', async () => {
    const mockResults = [
      { id: '1', title: 'Result 1', description: 'Description 1' },
      { id: '2', title: 'Result 2', description: 'Description 2' }
    ];
    
    // Mock API response
    mockQueryClient.setQueryData(['search', 'test query'], mockResults);
    
    customRender(
      <SearchResults query="test query" />,
      { queryClient: mockQueryClient }
    );
    
    await waitFor(() => {
      expect(screen.getByText('Result 1')).toBeInTheDocument();
      expect(screen.getByText('Result 2')).toBeInTheDocument();
    });
  });
  
  it('handles empty search results', async () => {
    mockQueryClient.setQueryData(['search', 'empty query'], []);
    
    customRender(
      <SearchResults query="empty query" />,
      { queryClient: mockQueryClient }
    );
    
    await waitFor(() => {
      expect(screen.getByText(/no results found/i)).toBeInTheDocument();
    });
  });
  
  it('handles search errors gracefully', async () => {
    mockQueryClient.setQueryData(
      ['search', 'error query'], 
      new Error('Search failed')
    );
    
    customRender(
      <SearchResults query="error query" />,
      { queryClient: mockQueryClient }
    );
    
    await waitFor(() => {
      expect(screen.getByText(/search failed/i)).toBeInTheDocument();
    });
  });
});

// Hook Testing Examples
describe('useToggle Hook', () => {
  it('initializes with correct default value', () => {
    const { result } = renderHook(() => useToggle());
    
    expect(result.current.value).toBe(false);
  });
  
  it('initializes with provided value', () => {
    const { result } = renderHook(() => useToggle(true));
    
    expect(result.current.value).toBe(true);
  });
  
  it('toggles value correctly', () => {
    const { result } = renderHook(() => useToggle(false));
    
    hookAct(() => {
      result.current.toggle();
    });
    
    expect(result.current.value).toBe(true);
    
    hookAct(() => {
      result.current.toggle();
    });
    
    expect(result.current.value).toBe(false);
  });
  
  it('sets value to true and false correctly', () => {
    const { result } = renderHook(() => useToggle(false));
    
    hookAct(() => {
      result.current.setTrue();
    });
    
    expect(result.current.value).toBe(true);
    
    hookAct(() => {
      result.current.setFalse();
    });
    
    expect(result.current.value).toBe(false);
  });
});

// Performance Testing
describe('VirtualScroller Performance', () => {
  it('renders large lists efficiently', async () => {
    const largeDataSet = Array.from({ length: 10000 }, (_, index) => ({
      id: index.toString(),
      title: `Item ${index}`,
      content: `Content for item ${index}`
    }));
    
    const renderStart = performance.now();
    
    customRender(
      <VirtualScroller
        items={largeDataSet}
        itemHeight={50}
        containerHeight={400}
        renderItem={(item) => <div>{item.title}</div>}
        keyExtractor={(item) => item.id}
      />
    );
    
    const renderTime = performance.now() - renderStart;
    
    // Should render in less than 100ms
    expect(renderTime).toBeLessThan(100);
    
    // Only visible items should be rendered initially
    expect(screen.getAllByText(/Item \d+/)).toHaveLength(8); // ~8 visible items
  });
});

// Visual Regression Testing Setup
describe('Visual Regression Tests', () => {
  it('matches button component snapshot', () => {
    const { container } = customRender(
      <div>
        <Button variant="primary">Primary Button</Button>
        <Button variant="secondary">Secondary Button</Button>
        <Button variant="destructive">Destructive Button</Button>
      </div>
    );
    
    expect(container.firstChild).toMatchSnapshot();
  });
  
  it('matches complex component layout', () => {
    const { container } = customRender(
      <Card>
        <CardHeader>
          <CardTitle>Test Card</CardTitle>
        </CardHeader>
        <CardContent>
          <p>This is a test card with various content.</p>
          <Button>Action Button</Button>
        </CardContent>
      </Card>
    );
    
    expect(container.firstChild).toMatchSnapshot();
  });
});
```

## 📊 Success Criteria

### Component Quality Metrics
- **Type Safety**: 100% TypeScript coverage with strict mode enabled
- **Test Coverage**: >90% line coverage for all components and hooks
- **Performance**: <100ms initial render time for complex components
- **Accessibility**: 100% compliance with WCAG 2.1 AA standards

### Code Quality Standards
- **Bundle Size**: Individual components <10KB gzipped
- **Reusability**: >80% of components used in multiple contexts
- **API Consistency**: Standardized prop naming and patterns across all components
- **Documentation**: Complete JSDoc and Storybook coverage

## 🎯 Deliverables

Upon completion of React component development implementation:

- ✅ **Component Library** with atomic design structure and consistent API patterns
- ✅ **TypeScript Integration** with comprehensive type definitions and generic patterns
- ✅ **Performance Optimization** with memoization, virtualization, and concurrent features
- ✅ **Testing Framework** with unit, integration, and accessibility test coverage
- ✅ **Documentation** with Storybook stories and comprehensive component guides
- ✅ **Modern React Patterns** including hooks, context, suspense, and concurrent features
- ✅ **Build Configuration** with code splitting, tree shaking, and optimization
- ✅ **Developer Experience** with hot reloading, debugging tools, and error boundaries

---

*This comprehensive React component development approach ensures high-quality, performant, and maintainable frontend components using modern React patterns and TypeScript best practices.*