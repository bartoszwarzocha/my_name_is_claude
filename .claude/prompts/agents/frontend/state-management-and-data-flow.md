# State Management and Data Flow Architecture

## Context and Purpose
You are architecting and implementing comprehensive state management solutions for complex frontend applications. This prompt focuses on designing scalable data flow patterns, implementing advanced state management architectures, and optimizing performance through strategic state organization and synchronization strategies.

## Expertise Areas
- Global state management with Redux Toolkit, Zustand, Valtio
- React Context API and Provider pattern optimization
- Server state synchronization with React Query/TanStack Query
- Real-time state updates with WebSockets and Server-Sent Events
- State persistence and hydration strategies
- Performance optimization through selective state updates
- Type-safe state management with TypeScript

## Implementation Framework

### Phase 1: State Architecture Analysis and Design

**Advanced State Management Architecture:**
```typescript
// Comprehensive state management framework
interface StateManagementArchitecture {
  globalState: {
    patterns: {
      fluxPattern: 'unidirectional_data_flow_redux_toolkit_implementation';
      atomicState: 'jotai_recoil_granular_state_updates';
      proxyBased: 'valtio_mobx_reactive_state_management';
      contextPattern: 'react_context_provider_optimization';
    };
    strategies: {
      stateNormalization: 'entity_adapter_relational_data_structure';
      stateColocation: 'component_local_vs_global_state_decisions';
      statePersistence: 'localStorage_sessionStorage_indexedDB_strategies';
      stateHydration: 'SSR_client_state_synchronization';
    };
  };
  
  serverState: {
    cachingStrategies: {
      staleWhileRevalidate: 'background_updates_immediate_response';
      cacheFirst: 'offline_first_progressive_enhancement';
      networkFirst: 'real_time_data_priority';
      optimisticUpdates: 'immediate_UI_feedback_rollback_handling';
    };
    synchronization: {
      polling: 'interval_based_data_refresh';
      websockets: 'real_time_bidirectional_updates';
      serverSentEvents: 'unidirectional_live_updates';
      conflictResolution: 'operational_transform_CRDT_patterns';
    };
  };
}

// Advanced Redux Toolkit implementation
interface ApplicationStore {
  // Feature slices with normalized state
  entities: {
    users: EntityState<User>;
    projects: EntityState<Project>;
    tasks: EntityState<Task>;
    comments: EntityState<Comment>;
  };
  
  // UI state management
  ui: {
    modals: ModalState;
    notifications: NotificationState;
    loading: LoadingState;
    filters: FilterState;
  };
  
  // Authentication and authorization
  auth: {
    user: AuthenticatedUser | null;
    permissions: PermissionSet;
    session: SessionState;
  };
  
  // Real-time features
  realtime: {
    connectionStatus: ConnectionStatus;
    subscriptions: SubscriptionMap;
    pendingActions: PendingActionQueue;
  };
}

// Type-safe slice implementation with RTK Query
const projectsSlice = createSlice({
  name: 'projects',
  initialState: projectsAdapter.getInitialState({
    selectedProjectId: null,
    lastUpdated: null,
    syncStatus: 'idle'
  }),
  reducers: {
    selectProject: (state, action: PayloadAction<string>) => {
      state.selectedProjectId = action.payload;
    },
    updateSyncStatus: (state, action: PayloadAction<SyncStatus>) => {
      state.syncStatus = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addMatcher(projectsApi.endpoints.getProjects.matchPending, (state) => {
        state.syncStatus = 'syncing';
      })
      .addMatcher(projectsApi.endpoints.getProjects.matchFulfilled, (state, action) => {
        projectsAdapter.setAll(state, action.payload);
        state.lastUpdated = Date.now();
        state.syncStatus = 'synced';
      })
      .addMatcher(projectsApi.endpoints.updateProject.matchPending, (state, action) => {
        // Optimistic update
        projectsAdapter.updateOne(state, {
          id: action.meta.arg.id,
          changes: action.meta.arg
        });
      });
  }
});
```

**Server State Management with Advanced Caching:**
```typescript
// Comprehensive React Query/TanStack Query setup
class AdvancedQueryClient {
  private queryClient: QueryClient;
  private websocketManager: WebSocketManager;
  private conflictResolver: ConflictResolver;

  constructor() {
    this.queryClient = new QueryClient({
      defaultOptions: {
        queries: {
          staleTime: 5 * 60 * 1000, // 5 minutes
          cacheTime: 10 * 60 * 1000, // 10 minutes
          refetchOnWindowFocus: false,
          retry: (failureCount, error) => {
            if (error instanceof NetworkError) return failureCount < 3;
            if (error instanceof AuthError) return false;
            return failureCount < 2;
          }
        },
        mutations: {
          retry: 1,
          onError: (error, variables, context) => {
            this.handleMutationError(error, variables, context);
          }
        }
      }
    });
    
    this.setupInvalidationStrategies();
    this.setupOptimisticUpdates();
    this.setupRealtimeSync();
  }

  // Advanced caching with selective invalidation
  private setupInvalidationStrategies() {
    this.queryClient.setMutationDefaults(['projects', 'create'], {
      mutationFn: createProject,
      onSuccess: () => {
        // Invalidate related queries intelligently
        this.queryClient.invalidateQueries({
          queryKey: ['projects'],
          exact: false
        });
        this.queryClient.invalidateQueries(['dashboard', 'stats']);
      }
    });
  }

  // Optimistic updates with rollback
  private setupOptimisticUpdates() {
    const updateProjectMutation = useMutation({
      mutationFn: updateProject,
      onMutate: async (updatedProject) => {
        // Cancel outgoing refetches
        await this.queryClient.cancelQueries(['projects', updatedProject.id]);
        
        // Snapshot previous value
        const previousProject = this.queryClient.getQueryData(['projects', updatedProject.id]);
        
        // Optimistically update
        this.queryClient.setQueryData(['projects', updatedProject.id], updatedProject);
        
        return { previousProject };
      },
      onError: (error, updatedProject, context) => {
        // Rollback on error
        if (context?.previousProject) {
          this.queryClient.setQueryData(['projects', updatedProject.id], context.previousProject);
        }
      },
      onSettled: (data, error, updatedProject) => {
        // Always refetch to ensure consistency
        this.queryClient.invalidateQueries(['projects', updatedProject.id]);
      }
    });
  }
}

// Real-time state synchronization
class RealtimeStateManager {
  private websocket: WebSocket;
  private eventHandlers: Map<string, EventHandler>;
  private conflictResolver: ConflictResolver;

  setupRealtimeSync() {
    this.websocket = new WebSocket(process.env.REACT_APP_WS_URL!);
    
    this.websocket.onmessage = (event) => {
      const { type, payload, timestamp } = JSON.parse(event.data);
      
      switch (type) {
        case 'ENTITY_UPDATED':
          this.handleEntityUpdate(payload, timestamp);
          break;
        case 'ENTITY_DELETED':
          this.handleEntityDeletion(payload);
          break;
        case 'CONFLICT_DETECTED':
          this.conflictResolver.resolve(payload);
          break;
      }
    };
  }

  private handleEntityUpdate(payload: EntityUpdate, serverTimestamp: number) {
    const queryKey = [payload.entityType, payload.id];
    const currentData = this.queryClient.getQueryData(queryKey);
    
    // Check for conflicts
    if (currentData && this.hasLocalModifications(currentData, serverTimestamp)) {
      this.conflictResolver.queueConflict({
        local: currentData,
        remote: payload.data,
        entityId: payload.id,
        entityType: payload.entityType
      });
      return;
    }
    
    // Apply update directly
    this.queryClient.setQueryData(queryKey, payload.data);
    
    // Invalidate related queries
    this.queryClient.invalidateQueries({
      predicate: (query) => this.isRelatedQuery(query.queryKey, payload)
    });
  }
}
```

### Phase 2: Advanced State Patterns and Performance Optimization

**Atomic State Management with Jotai/Recoil:**
```typescript
// Advanced atomic state architecture
interface AtomicStateArchitecture {
  atoms: {
    primitive: 'user_preferences_theme_language_settings';
    derived: 'computed_values_filtered_sorted_transformed_data';
    async: 'api_data_loading_error_states';
    family: 'parameterized_atoms_dynamic_state_creation';
  };
  
  patterns: {
    atomSplitting: 'granular_updates_minimal_rerenders';
    atomComposition: 'complex_state_from_simple_atoms';
    atomPersistence: 'localStorage_sync_state_hydration';
    atomDependencies: 'reactive_updates_cascading_changes';
  };
}

// Jotai implementation with advanced patterns
const userAtom = atom<User | null>(null);
const userPreferencesAtom = atom<UserPreferences>({
  theme: 'system',
  language: 'en',
  notifications: true,
  compactMode: false
});

// Derived atoms with complex logic
const filteredProjectsAtom = atom((get) => {
  const projects = get(projectsAtom);
  const filters = get(projectFiltersAtom);
  const user = get(userAtom);
  
  return projects
    .filter(project => {
      // Apply user permissions
      if (!hasProjectAccess(user, project)) return false;
      
      // Apply active filters
      if (filters.status && project.status !== filters.status) return false;
      if (filters.owner && project.ownerId !== filters.owner) return false;
      if (filters.dateRange) {
        const projectDate = new Date(project.createdAt);
        if (projectDate < filters.dateRange.start || projectDate > filters.dateRange.end) {
          return false;
        }
      }
      
      return true;
    })
    .sort((a, b) => {
      switch (filters.sortBy) {
        case 'name': return a.name.localeCompare(b.name);
        case 'date': return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
        case 'status': return a.status.localeCompare(b.status);
        default: return 0;
      }
    });
});

// Async atom with error handling
const projectStatsAtom = atom(async (get) => {
  const projects = get(filteredProjectsAtom);
  const user = get(userAtom);
  
  if (!user || projects.length === 0) {
    return { totalProjects: 0, completedProjects: 0, activeProjects: 0 };
  }
  
  try {
    const response = await fetch(`/api/projects/stats?userId=${user.id}&projectIds=${projects.map(p => p.id).join(',')}`);
    if (!response.ok) throw new Error('Failed to fetch project stats');
    return await response.json();
  } catch (error) {
    console.error('Error fetching project stats:', error);
    // Return computed fallback
    return {
      totalProjects: projects.length,
      completedProjects: projects.filter(p => p.status === 'completed').length,
      activeProjects: projects.filter(p => p.status === 'active').length
    };
  }
});

// Atom families for dynamic state
const projectAtomFamily = atomFamily((projectId: string) =>
  atom(async () => {
    const response = await fetch(`/api/projects/${projectId}`);
    if (!response.ok) throw new Error(`Failed to fetch project ${projectId}`);
    return response.json();
  })
);

// Persistent atoms with storage sync
const persistentUserPreferencesAtom = atomWithStorage('userPreferences', {
  theme: 'system' as Theme,
  language: 'en' as Language,
  notifications: true,
  compactMode: false
});
```

**Context API Optimization for Performance:**
```typescript
// Optimized context providers with selective updates
interface OptimizedContextArchitecture {
  strategies: {
    contextSplitting: 'separate_frequently_changing_rarely_changing_state';
    providerOptimization: 'memoized_values_minimal_provider_rerenders';
    consumerOptimization: 'selective_context_consumption_fine_grained_updates';
    contextComposition: 'multiple_contexts_layered_provider_architecture';
  };
}

// Split contexts for optimal performance
const UserContext = createContext<User | null>(null);
const UserActionsContext = createContext<UserActions | null>(null);
const UIContext = createContext<UIState | null>(null);
const UIActionsContext = createContext<UIActions | null>(null);

// Optimized provider implementation
const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [uiState, setUIState] = useState<UIState>({
    sidebarOpen: true,
    theme: 'system',
    notifications: []
  });

  // Memoize user actions to prevent unnecessary rerenders
  const userActions = useMemo<UserActions>(() => ({
    login: async (credentials) => {
      const user = await authService.login(credentials);
      setUser(user);
    },
    logout: () => {
      authService.logout();
      setUser(null);
    },
    updateProfile: async (updates) => {
      if (!user) return;
      const updatedUser = await userService.updateProfile(user.id, updates);
      setUser(updatedUser);
    }
  }), [user]);

  // Memoize UI actions
  const uiActions = useMemo<UIActions>(() => ({
    toggleSidebar: () => setUIState(prev => ({ ...prev, sidebarOpen: !prev.sidebarOpen })),
    setTheme: (theme) => setUIState(prev => ({ ...prev, theme })),
    addNotification: (notification) => setUIState(prev => ({
      ...prev,
      notifications: [...prev.notifications, notification]
    })),
    removeNotification: (id) => setUIState(prev => ({
      ...prev,
      notifications: prev.notifications.filter(n => n.id !== id)
    }))
  }), []);

  // Memoize context values to prevent cascading rerenders
  const userContextValue = useMemo(() => user, [user]);
  const userActionsContextValue = useMemo(() => userActions, [userActions]);
  const uiContextValue = useMemo(() => uiState, [uiState]);
  const uiActionsContextValue = useMemo(() => uiActions, [uiActions]);

  return (
    <UserContext.Provider value={userContextValue}>
      <UserActionsContext.Provider value={userActionsContextValue}>
        <UIContext.Provider value={uiContextValue}>
          <UIActionsContext.Provider value={uiActionsContextValue}>
            {children}
          </UIActionsContext.Provider>
        </UIContext.Provider>
      </UserActionsContext.Provider>
    </UserContext.Provider>
  );
};

// Custom hooks for selective consumption
const useUser = () => {
  const user = useContext(UserContext);
  return user;
};

const useUserActions = () => {
  const actions = useContext(UserActionsContext);
  if (!actions) throw new Error('useUserActions must be used within AppProvider');
  return actions;
};

// Optimized hook for specific UI state properties
const useUIProperty = <K extends keyof UIState>(property: K): UIState[K] => {
  const uiState = useContext(UIContext);
  if (!uiState) throw new Error('useUIProperty must be used within AppProvider');
  
  return useMemo(() => uiState[property], [uiState, property]);
};
```

### Phase 3: State Persistence and Synchronization

**Advanced State Persistence Strategies:**
```typescript
// Comprehensive state persistence framework
class StatePersistenceManager {
  private storage: StorageAdapter;
  private serializer: StateSerializer;
  private encryptor: StateEncryptor;
  private migrator: StateMigrator;

  constructor(config: PersistenceConfig) {
    this.storage = this.createStorageAdapter(config.storage);
    this.serializer = new StateSerializer(config.serialization);
    this.encryptor = new StateEncryptor(config.encryption);
    this.migrator = new StateMigrator(config.migrations);
  }

  // Multi-level persistence strategy
  async persistState(state: RootState): Promise<void> {
    try {
      // Determine what to persist based on configuration
      const persistableState = this.extractPersistableState(state);
      
      // Apply state transformations
      const transformedState = this.applyPersistenceTransforms(persistableState);
      
      // Encrypt sensitive data
      const encryptedState = await this.encryptor.encrypt(transformedState);
      
      // Serialize for storage
      const serializedState = this.serializer.serialize(encryptedState);
      
      // Store with versioning
      await this.storage.setItem('app-state', {
        data: serializedState,
        version: this.getCurrentVersion(),
        timestamp: Date.now()
      });
      
      // Store backup in IndexedDB for larger datasets
      if (serializedState.length > 50000) { // 50KB threshold
        await this.storage.setItemInDB('app-state-backup', serializedState);
      }
    } catch (error) {
      console.error('State persistence failed:', error);
      // Implement fallback strategies
      await this.handlePersistenceFailure(state, error);
    }
  }

  // Intelligent state hydration with conflict resolution
  async hydrateState(): Promise<Partial<RootState> | null> {
    try {
      const storedData = await this.storage.getItem('app-state');
      if (!storedData) return null;
      
      // Check version compatibility
      if (!this.isVersionCompatible(storedData.version)) {
        const migratedData = await this.migrator.migrate(storedData);
        if (!migratedData) return null;
        storedData.data = migratedData;
      }
      
      // Deserialize and decrypt
      const deserializedState = this.serializer.deserialize(storedData.data);
      const decryptedState = await this.encryptor.decrypt(deserializedState);
      
      // Validate state integrity
      if (!this.validateStateIntegrity(decryptedState)) {
        console.warn('State integrity check failed, using fallback');
        return await this.loadFallbackState();
      }
      
      // Apply hydration transforms
      const hydratedState = this.applyHydrationTransforms(decryptedState);
      
      return hydratedState;
    } catch (error) {
      console.error('State hydration failed:', error);
      return await this.loadFallbackState();
    }
  }

  // Selective persistence based on state slices
  private extractPersistableState(state: RootState): Partial<RootState> {
    const persistenceConfig = {
      auth: { persist: true, encrypt: true },
      userPreferences: { persist: true, encrypt: false },
      ui: { 
        persist: true, 
        encrypt: false,
        blacklist: ['loading', 'errors'] // Don't persist transient state
      },
      projects: { 
        persist: true, 
        encrypt: false,
        transform: (projects: ProjectState) => ({
          // Only persist IDs and essential metadata, not full entities
          recentProjectIds: projects.entities.ids.slice(0, 10),
          selectedProjectId: projects.selectedProjectId,
          lastUpdated: projects.lastUpdated
        })
      }
    };

    return Object.entries(persistenceConfig).reduce((acc, [key, config]) => {
      if (config.persist && state[key as keyof RootState]) {
        acc[key as keyof RootState] = config.transform 
          ? config.transform(state[key as keyof RootState])
          : state[key as keyof RootState];
      }
      return acc;
    }, {} as Partial<RootState>);
  }
}

// Advanced synchronization with conflict resolution
class StateSynchronizationManager {
  private websocket: WebSocket;
  private conflictResolver: ConflictResolver;
  private operationalTransform: OperationalTransform;

  // Real-time collaborative state updates
  setupCollaborativeSync() {
    this.websocket.onmessage = (event) => {
      const { type, payload, meta } = JSON.parse(event.data);
      
      switch (type) {
        case 'STATE_PATCH':
          this.handleStatePatch(payload, meta);
          break;
        case 'CONFLICT_RESOLUTION':
          this.handleConflictResolution(payload);
          break;
        case 'SYNC_REQUEST':
          this.handleSyncRequest(payload);
          break;
      }
    };
  }

  private async handleStatePatch(patch: StatePatch, meta: PatchMetadata) {
    const currentState = store.getState();
    
    // Check for conflicts
    if (this.hasConflict(patch, currentState, meta)) {
      const resolution = await this.conflictResolver.resolve({
        localState: currentState,
        remotePatch: patch,
        metadata: meta
      });
      
      if (resolution.strategy === 'merge') {
        const mergedPatch = this.operationalTransform.merge(patch, resolution.localChanges);
        store.dispatch(applyStatePatch(mergedPatch));
      } else if (resolution.strategy === 'replace') {
        store.dispatch(applyStatePatch(patch));
      }
    } else {
      // No conflict, apply patch directly
      store.dispatch(applyStatePatch(patch));
    }
  }
}
```

### Phase 4: Performance Monitoring and Optimization

**State Performance Analytics:**
```typescript
// Comprehensive performance monitoring for state management
class StatePerformanceMonitor {
  private metrics: PerformanceMetrics;
  private thresholds: PerformanceThresholds;
  private reporters: PerformanceReporter[];

  setupStatePerformanceMonitoring() {
    // Monitor Redux action performance
    const performanceMiddleware: Middleware = (store) => (next) => (action) => {
      const startTime = performance.now();
      const prevState = store.getState();
      
      const result = next(action);
      
      const endTime = performance.now();
      const nextState = store.getState();
      
      this.recordActionPerformance({
        actionType: action.type,
        duration: endTime - startTime,
        stateSize: this.calculateStateSize(nextState),
        stateDiff: this.calculateStateDiff(prevState, nextState),
        timestamp: Date.now()
      });
      
      return result;
    };

    // Monitor React Query cache performance
    this.queryClient.setDefaultOptions({
      queries: {
        onSuccess: (data, query) => {
          this.recordCachePerformance({
            queryKey: query.queryKey,
            dataSize: this.calculateDataSize(data),
            cacheHit: query.state.dataUpdatedAt > 0,
            fetchTime: query.state.dataUpdatedAt - (query.state.fetchedAt || 0)
          });
        }
      }
    });

    // Monitor component render performance
    this.setupRenderPerformanceTracking();
  }

  // Detect performance bottlenecks
  analyzePerformanceBottlenecks(): PerformanceReport {
    const report: PerformanceReport = {
      slowActions: this.metrics.actions
        .filter(action => action.duration > this.thresholds.actionDuration)
        .sort((a, b) => b.duration - a.duration),
      
      largeCacheEntries: this.metrics.cacheEntries
        .filter(entry => entry.dataSize > this.thresholds.cacheSize)
        .sort((a, b) => b.dataSize - a.dataSize),
      
      frequentRerenders: this.metrics.rerenders
        .filter(component => component.count > this.thresholds.rerenderCount)
        .sort((a, b) => b.count - a.count),
      
      recommendations: this.generateOptimizationRecommendations()
    };

    return report;
  }

  private generateOptimizationRecommendations(): OptimizationRecommendation[] {
    const recommendations: OptimizationRecommendation[] = [];

    // Analyze selector performance
    const slowSelectors = this.metrics.selectors
      .filter(selector => selector.averageDuration > 5);
    
    if (slowSelectors.length > 0) {
      recommendations.push({
        type: 'SELECTOR_OPTIMIZATION',
        priority: 'high',
        description: 'Consider memoizing expensive selectors or splitting complex computations',
        affectedSelectors: slowSelectors.map(s => s.name)
      });
    }

    // Analyze state normalization
    const denormalizedEntities = this.detectDenormalizedState();
    if (denormalizedEntities.length > 0) {
      recommendations.push({
        type: 'STATE_NORMALIZATION',
        priority: 'medium',
        description: 'Normalize nested entities to reduce update complexity',
        affectedEntities: denormalizedEntities
      });
    }

    return recommendations;
  }
}
```

## Success Criteria

1. **State Architecture Excellence:**
   - Implemented scalable global state management with proper separation of concerns
   - Server state synchronization with intelligent caching and conflict resolution
   - Atomic state patterns for granular updates and optimal performance

2. **Performance Optimization:**
   - Sub-100ms action execution times for 95% of state updates
   - Selective component updates with <5% unnecessary rerenders
   - Efficient memory usage with automatic cleanup of stale state

3. **Developer Experience:**
   - Type-safe state management with comprehensive TypeScript integration
   - Clear state flow patterns with predictable update mechanisms
   - Comprehensive debugging and performance monitoring tools

4. **Production Readiness:**
   - Robust error handling and fallback strategies
   - State persistence and hydration with data migration support
   - Real-time synchronization with collaborative editing capabilities

## Deliverables

- **State Architecture Documentation:** Complete system design with data flow diagrams
- **Implementation Code:** Production-ready state management setup with all patterns
- **Performance Monitoring:** Comprehensive analytics and optimization recommendations
- **Testing Strategy:** Unit and integration tests for all state management patterns
- **Migration Guide:** Documentation for transitioning from existing state management solutions