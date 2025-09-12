# Angular Component Development and Architecture

## Context and Purpose
You are architecting and implementing advanced Angular applications with enterprise-grade component architecture. This prompt focuses on Angular 17+ features, standalone components, signals, dependency injection, reactive programming, and scalable application architecture patterns.

## Expertise Areas
- Angular 17+ with standalone components and new control flow
- Advanced TypeScript integration and strict type safety
- RxJS reactive programming and state management
- Dependency injection and hierarchical injectors
- Angular Material and CDK for component libraries
- Performance optimization and change detection strategies
- Testing with Jasmine, Karma, and Angular Testing Utilities

## Implementation Framework

### Phase 1: Advanced Angular Architecture and Component Design

**Comprehensive Angular Application Architecture:**
```typescript
// Modern Angular 17+ architecture with standalone components
interface AngularArchitectureFramework {
  componentArchitecture: {
    standalone: 'modern_component_registration_without_ngmodules';
    composition: 'component_composition_patterns_reusable_logic';
    lifecycle: 'advanced_lifecycle_hooks_optimization_strategies';
    changeDetection: 'onpush_strategy_signals_zone_optimization';
  };
  
  stateManagement: {
    signals: 'angular_signals_reactive_state_management';
    rxjs: 'observables_operators_reactive_patterns';
    ngrx: 'redux_pattern_effects_entity_management';
    services: 'injectable_services_hierarchical_injection';
  };
  
  routing: {
    guards: 'route_guards_authentication_authorization';
    lazy: 'lazy_loading_code_splitting_optimization';
    preloading: 'route_preloading_strategies_performance';
    data: 'route_resolvers_data_fetching_strategies';
  };
}

// Advanced standalone component with signals and dependency injection
@Component({
  selector: 'app-advanced-component',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatInputModule,
    MatProgressSpinnerModule
  ],
  template: `
    <div class="component-container">
      <!-- New Angular 17 control flow -->
      @if (loading()) {
        <mat-spinner diameter="24"></mat-spinner>
      } @else if (error()) {
        <div class="error-message" role="alert">
          {{ error() }}
        </div>
      } @else {
        <div class="content">
          <!-- Enhanced form with reactive patterns -->
          <form [formGroup]="form" (ngSubmit)="onSubmit()" class="form-container">
            @for (field of formFields(); track field.key) {
              <mat-form-field class="form-field">
                <mat-label>{{ field.label }}</mat-label>
                <input
                  matInput
                  [type]="field.type"
                  [formControlName]="field.key"
                  [placeholder]="field.placeholder"
                  [attr.aria-describedby]="field.key + '-error'"
                  [readonly]="readonly()"
                >
                @if (form.get(field.key)?.invalid && form.get(field.key)?.touched) {
                  <mat-error [id]="field.key + '-error'">
                    {{ getFieldError(field.key) }}
                  </mat-error>
                }
              </mat-form-field>
            }
            
            <div class="form-actions">
              <button
                mat-raised-button
                color="primary"
                type="submit"
                [disabled]="form.invalid || submitting()"
              >
                @if (submitting()) {
                  <mat-spinner diameter="16"></mat-spinner>
                } @else {
                  {{ submitButtonText() }}
                }
              </button>
              
              <button
                mat-button
                type="button"
                (click)="onCancel()"
                [disabled]="submitting()"
              >
                Cancel
              </button>
            </div>
          </form>
          
          <!-- Data visualization with signals -->
          @if (data().length > 0) {
            <div class="data-display">
              <h3>Results ({{ data().length }})</h3>
              @for (item of paginatedData(); track item.id; let i = $index) {
                <div 
                  class="data-item"
                  [class.selected]="selectedItems().has(item.id)"
                  (click)="toggleSelection(item.id)"
                  [attr.aria-selected]="selectedItems().has(item.id)"
                  role="option"
                >
                  <div class="item-content">
                    <h4>{{ item.title }}</h4>
                    <p>{{ item.description }}</p>
                    <span class="item-meta">
                      Created: {{ item.createdAt | date:'short' }}
                    </span>
                  </div>
                  
                  <div class="item-actions">
                    <button
                      mat-icon-button
                      (click)="editItem(item); $event.stopPropagation()"
                      [attr.aria-label]="'Edit ' + item.title"
                    >
                      <mat-icon>edit</mat-icon>
                    </button>
                    
                    <button
                      mat-icon-button
                      color="warn"
                      (click)="deleteItem(item.id); $event.stopPropagation()"
                      [attr.aria-label]="'Delete ' + item.title"
                    >
                      <mat-icon>delete</mat-icon>
                    </button>
                  </div>
                </div>
              }
              
              <!-- Pagination controls -->
              <mat-paginator
                [length]="data().length"
                [pageSize]="pageSize()"
                [pageSizeOptions]="[10, 25, 50, 100]"
                (page)="onPageChange($event)"
                aria-label="Select page"
              ></mat-paginator>
            </div>
          }
        </div>
      }
    </div>
  `,
  styleUrl: './advanced-component.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [
    // Component-level providers for hierarchical injection
    {
      provide: DATA_SERVICE_CONFIG,
      useValue: { apiUrl: '/api/v1', timeout: 30000 }
    }
  ]
})
export class AdvancedComponent implements OnInit, OnDestroy, AfterViewInit {
  // Modern Angular signals for reactive state
  readonly loading = signal(false);
  readonly error = signal<string | null>(null);
  readonly data = signal<DataItem[]>([]);
  readonly selectedItems = signal(new Set<string>());
  readonly readonly = signal(false);
  readonly submitting = signal(false);
  readonly currentPage = signal(0);
  readonly pageSize = signal(10);

  // Computed signals for derived state
  readonly filteredData = computed(() => {
    const items = this.data();
    const filter = this.searchTerm();
    
    if (!filter) return items;
    
    return items.filter(item =>
      item.title.toLowerCase().includes(filter.toLowerCase()) ||
      item.description.toLowerCase().includes(filter.toLowerCase())
    );
  });

  readonly paginatedData = computed(() => {
    const filtered = this.filteredData();
    const page = this.currentPage();
    const size = this.pageSize();
    const start = page * size;
    const end = start + size;
    
    return filtered.slice(start, end);
  });

  readonly formFields = computed(() => [
    {
      key: 'title',
      label: 'Title',
      type: 'text',
      placeholder: 'Enter title',
      validators: [Validators.required, Validators.minLength(3)]
    },
    {
      key: 'description',
      label: 'Description',
      type: 'textarea',
      placeholder: 'Enter description',
      validators: [Validators.required, Validators.maxLength(500)]
    },
    {
      key: 'category',
      label: 'Category',
      type: 'select',
      options: this.categories(),
      validators: [Validators.required]
    }
  ]);

  readonly submitButtonText = computed(() => 
    this.editingItem() ? 'Update Item' : 'Create Item'
  );

  // Private signals for internal state
  private readonly searchTerm = signal('');
  private readonly editingItem = signal<DataItem | null>(null);
  private readonly categories = signal<SelectOption[]>([]);

  // Reactive form with advanced validation
  readonly form = this.fb.nonNullable.group({
    title: ['', [Validators.required, Validators.minLength(3)]],
    description: ['', [Validators.required, Validators.maxLength(500)]],
    category: ['', [Validators.required]],
    tags: this.fb.array<string>([]),
    priority: ['medium', [Validators.required]],
    dueDate: [null as Date | null],
    assignee: ['']
  });

  // Advanced dependency injection with hierarchical injectors
  constructor(
    private readonly fb: FormBuilder,
    private readonly dataService: DataService,
    private readonly notificationService: NotificationService,
    private readonly cdr: ChangeDetectorRef,
    private readonly destroyRef: DestroyRef,
    private readonly dialog: MatDialog,
    @Inject(DATA_SERVICE_CONFIG) private readonly config: DataServiceConfig,
    @Optional() @SkipSelf() private readonly parentComponent?: ParentComponent
  ) {
    // Setup reactive form validation effects
    this.setupFormValidation();
    
    // Initialize component state
    this.initializeComponent();
  }

  ngOnInit(): void {
    // Load initial data with error handling
    this.loadInitialData();
    
    // Setup reactive data streams
    this.setupDataStreams();
    
    // Setup keyboard shortcuts
    this.setupKeyboardShortcuts();
  }

  ngAfterViewInit(): void {
    // Setup view-dependent functionality
    this.setupViewInteractions();
  }

  ngOnDestroy(): void {
    // Cleanup handled by DestroyRef and takeUntilDestroyed
  }

  // Advanced form validation setup
  private setupFormValidation(): void {
    // Real-time validation with debouncing
    this.form.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(values => {
      this.validateFormValues(values);
    });

    // Cross-field validation
    this.form.get('dueDate')?.valueChanges.pipe(
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(dueDate => {
      this.validateDueDate(dueDate);
    });
  }

  // Reactive data loading with advanced error handling
  private loadInitialData(): void {
    this.loading.set(true);
    this.error.set(null);

    const loadData$ = forkJoin({
      items: this.dataService.getItems(),
      categories: this.dataService.getCategories(),
      userPreferences: this.dataService.getUserPreferences()
    }).pipe(
      retry({
        count: 3,
        delay: (error, retryCount) => timer(retryCount * 1000)
      }),
      catchError(error => {
        console.error('Failed to load initial data:', error);
        return of({
          items: [],
          categories: [],
          userPreferences: null
        });
      }),
      finalize(() => this.loading.set(false)),
      takeUntilDestroyed(this.destroyRef)
    );

    loadData$.subscribe({
      next: ({ items, categories, userPreferences }) => {
        this.data.set(items);
        this.categories.set(categories);
        
        if (userPreferences) {
          this.applyUserPreferences(userPreferences);
        }
      },
      error: error => {
        this.error.set('Failed to load data. Please try again.');
        this.notificationService.showError('Unable to load data');
      }
    });
  }

  // Advanced form submission with optimistic updates
  onSubmit(): void {
    if (this.form.invalid || this.submitting()) return;

    this.submitting.set(true);
    this.error.set(null);

    const formValue = this.form.getRawValue();
    const editingItem = this.editingItem();

    const operation$ = editingItem
      ? this.dataService.updateItem(editingItem.id, formValue)
      : this.dataService.createItem(formValue);

    // Optimistic update
    if (editingItem) {
      this.updateItemOptimistically(editingItem.id, formValue);
    } else {
      this.addItemOptimistically(formValue);
    }

    operation$.pipe(
      catchError(error => {
        // Rollback optimistic update
        this.rollbackOptimisticUpdate(editingItem?.id);
        return throwError(() => error);
      }),
      finalize(() => this.submitting.set(false)),
      takeUntilDestroyed(this.destroyRef)
    ).subscribe({
      next: (result) => {
        this.handleSubmissionSuccess(result);
        this.form.reset();
        this.editingItem.set(null);
      },
      error: (error) => {
        this.error.set('Failed to save item. Please try again.');
        this.notificationService.showError('Save failed');
        console.error('Submission error:', error);
      }
    });
  }

  // Advanced item selection with keyboard support
  toggleSelection(itemId: string): void {
    const selected = this.selectedItems();
    const newSelected = new Set(selected);
    
    if (selected.has(itemId)) {
      newSelected.delete(itemId);
    } else {
      newSelected.add(itemId);
    }
    
    this.selectedItems.set(newSelected);
    
    // Emit selection change event
    this.onSelectionChange(Array.from(newSelected));
  }

  // Bulk operations with confirmation
  async bulkDelete(): Promise<void> {
    const selectedIds = Array.from(this.selectedItems());
    if (selectedIds.length === 0) return;

    const confirmed = await this.confirmBulkAction(
      `Delete ${selectedIds.length} items?`,
      'This action cannot be undone.'
    );

    if (confirmed) {
      this.performBulkDelete(selectedIds);
    }
  }

  // Advanced edit functionality with form population
  editItem(item: DataItem): void {
    this.editingItem.set(item);
    
    // Populate form with item data
    this.form.patchValue({
      title: item.title,
      description: item.description,
      category: item.category,
      priority: item.priority,
      dueDate: item.dueDate ? new Date(item.dueDate) : null,
      assignee: item.assignee || ''
    });

    // Set tags form array
    const tagsArray = this.form.get('tags') as FormArray;
    tagsArray.clear();
    item.tags?.forEach(tag => {
      tagsArray.push(this.fb.control(tag));
    });

    // Scroll to form
    this.scrollToForm();
  }

  // Advanced pagination with URL sync
  onPageChange(event: PageEvent): void {
    this.currentPage.set(event.pageIndex);
    this.pageSize.set(event.pageSize);
    
    // Update URL parameters
    this.updateUrlParams({
      page: event.pageIndex.toString(),
      size: event.pageSize.toString()
    });
  }

  // Advanced search with debouncing and highlighting
  onSearchChange(term: string): void {
    this.searchTerm.set(term);
    this.currentPage.set(0); // Reset to first page
    
    // Update URL
    this.updateUrlParams({
      search: term,
      page: '0'
    });
  }

  // Form validation helper
  getFieldError(fieldName: string): string {
    const field = this.form.get(fieldName);
    if (!field?.errors || !field.touched) return '';

    const errors = field.errors;
    
    if (errors['required']) return `${fieldName} is required`;
    if (errors['minlength']) return `${fieldName} must be at least ${errors['minlength'].requiredLength} characters`;
    if (errors['maxlength']) return `${fieldName} cannot exceed ${errors['maxlength'].requiredLength} characters`;
    if (errors['email']) return 'Please enter a valid email address';
    if (errors['pattern']) return `${fieldName} format is invalid`;
    
    return 'Invalid input';
  }

  // Advanced keyboard shortcuts setup
  private setupKeyboardShortcuts(): void {
    fromEvent<KeyboardEvent>(document, 'keydown').pipe(
      filter(event => event.ctrlKey || event.metaKey),
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(event => {
      switch (event.key) {
        case 'n':
          event.preventDefault();
          this.startNewItem();
          break;
        case 's':
          event.preventDefault();
          if (this.form.valid) this.onSubmit();
          break;
        case 'Escape':
          this.cancelEdit();
          break;
      }
    });
  }

  // Optimistic update helpers
  private updateItemOptimistically(id: string, updates: Partial<DataItem>): void {
    const currentData = this.data();
    const updatedData = currentData.map(item =>
      item.id === id ? { ...item, ...updates } : item
    );
    this.data.set(updatedData);
  }

  private addItemOptimistically(newItem: Partial<DataItem>): void {
    const optimisticItem: DataItem = {
      id: 'temp-' + Date.now(),
      ...newItem,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    } as DataItem;

    const currentData = this.data();
    this.data.set([optimisticItem, ...currentData]);
  }

  private rollbackOptimisticUpdate(itemId?: string): void {
    // Reload data from server to ensure consistency
    this.dataService.getItems().pipe(
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(items => {
      this.data.set(items);
    });
  }

  // Advanced confirmation dialog
  private async confirmBulkAction(title: string, message: string): Promise<boolean> {
    const dialogRef = this.dialog.open(ConfirmationDialogComponent, {
      data: { title, message },
      autoFocus: false,
      restoreFocus: true
    });

    return dialogRef.afterClosed().pipe(
      map(result => result === true),
      take(1)
    ).toPromise() ?? false;
  }

  // URL parameter management
  private updateUrlParams(params: Record<string, string>): void {
    // Implementation would use Router for URL management
  }

  private scrollToForm(): void {
    // Smooth scroll to form element
    const formElement = document.querySelector('.form-container');
    formElement?.scrollIntoView({ behavior: 'smooth' });
  }
}

// Advanced data service with caching and error handling
@Injectable({
  providedIn: 'root'
})
export class DataService {
  private readonly cache = new Map<string, { data: any; expiry: number }>();
  private readonly CACHE_TTL = 5 * 60 * 1000; // 5 minutes

  constructor(
    private readonly http: HttpClient,
    @Inject(DATA_SERVICE_CONFIG) private readonly config: DataServiceConfig
  ) {}

  getItems(): Observable<DataItem[]> {
    return this.getCachedOrFetch('items', () =>
      this.http.get<DataItem[]>(`${this.config.apiUrl}/items`).pipe(
        timeout(this.config.timeout),
        retry({ count: 2, delay: 1000 })
      )
    );
  }

  createItem(item: Partial<DataItem>): Observable<DataItem> {
    return this.http.post<DataItem>(`${this.config.apiUrl}/items`, item).pipe(
      timeout(this.config.timeout),
      tap(() => this.invalidateCache('items'))
    );
  }

  updateItem(id: string, updates: Partial<DataItem>): Observable<DataItem> {
    return this.http.put<DataItem>(`${this.config.apiUrl}/items/${id}`, updates).pipe(
      timeout(this.config.timeout),
      tap(() => {
        this.invalidateCache('items');
        this.invalidateCache(`item-${id}`);
      })
    );
  }

  deleteItem(id: string): Observable<void> {
    return this.http.delete<void>(`${this.config.apiUrl}/items/${id}`).pipe(
      timeout(this.config.timeout),
      tap(() => {
        this.invalidateCache('items');
        this.invalidateCache(`item-${id}`);
      })
    );
  }

  private getCachedOrFetch<T>(key: string, fetchFn: () => Observable<T>): Observable<T> {
    const cached = this.cache.get(key);
    
    if (cached && cached.expiry > Date.now()) {
      return of(cached.data);
    }

    return fetchFn().pipe(
      tap(data => {
        this.cache.set(key, {
          data,
          expiry: Date.now() + this.CACHE_TTL
        });
      })
    );
  }

  private invalidateCache(key: string): void {
    this.cache.delete(key);
  }
}

// Type definitions
interface DataItem {
  id: string;
  title: string;
  description: string;
  category: string;
  tags?: string[];
  priority: 'low' | 'medium' | 'high';
  dueDate?: string;
  assignee?: string;
  createdAt: string;
  updatedAt: string;
}

interface SelectOption {
  value: string;
  label: string;
}

interface DataServiceConfig {
  apiUrl: string;
  timeout: number;
}

// Injection tokens
const DATA_SERVICE_CONFIG = new InjectionToken<DataServiceConfig>('DataServiceConfig');
```

### Phase 2: Advanced RxJS Reactive Programming

**Comprehensive Reactive Patterns:**
```typescript
// Advanced RxJS patterns for Angular applications
class ReactivePatternFramework {
  // Advanced state management with RxJS
  static createReactiveStateManager<T>(initialState: T): ReactiveStateManager<T> {
    const state$ = new BehaviorSubject<T>(initialState);
    
    return {
      // State selectors with memoization
      select: <K extends keyof T>(key: K): Observable<T[K]> =>
        state$.pipe(
          map(state => state[key]),
          distinctUntilChanged(),
          shareReplay(1)
        ),

      // Deep property selection
      selectDeep: <R>(selector: (state: T) => R): Observable<R> =>
        state$.pipe(
          map(selector),
          distinctUntilChanged(),
          shareReplay(1)
        ),

      // State updates with immutability
      update: (updater: (state: T) => T): void => {
        const currentState = state$.value;
        const newState = updater(currentState);
        state$.next(newState);
      },

      // Patch updates for partial state changes
      patch: (updates: Partial<T>): void => {
        const currentState = state$.value;
        const newState = { ...currentState, ...updates };
        state$.next(newState);
      },

      // Current state snapshot
      getSnapshot: (): T => state$.value,

      // Observable state stream
      state$: state$.asObservable()
    };
  }

  // Advanced HTTP request patterns
  static createHttpRequestManager(http: HttpClient): HttpRequestManager {
    const pendingRequests = new Map<string, Observable<any>>();
    const requestCache = new Map<string, { data: any; expiry: number }>();

    return {
      // Request deduplication
      request: <T>(key: string, request: () => Observable<T>): Observable<T> => {
        if (pendingRequests.has(key)) {
          return pendingRequests.get(key)!;
        }

        const request$ = request().pipe(
          finalize(() => pendingRequests.delete(key)),
          shareReplay(1)
        );

        pendingRequests.set(key, request$);
        return request$;
      },

      // Cached requests with TTL
      cachedRequest: <T>(
        key: string,
        request: () => Observable<T>,
        ttl: number = 300000 // 5 minutes
      ): Observable<T> => {
        const cached = requestCache.get(key);
        
        if (cached && cached.expiry > Date.now()) {
          return of(cached.data);
        }

        return this.request(key, request).pipe(
          tap(data => {
            requestCache.set(key, {
              data,
              expiry: Date.now() + ttl
            });
          })
        );
      },

      // Optimistic updates with rollback
      optimisticUpdate: <T, U>(
        updateFn: () => Observable<T>,
        rollbackFn: () => void,
        optimisticAction: () => void
      ): Observable<T> => {
        optimisticAction();

        return updateFn().pipe(
          catchError(error => {
            rollbackFn();
            return throwError(() => error);
          })
        );
      },

      // Polling with backoff
      poll: <T>(
        request: () => Observable<T>,
        interval: number = 30000,
        maxRetries: number = 3
      ): Observable<T> => {
        return defer(() => request()).pipe(
          repeatWhen(notifications =>
            notifications.pipe(
              delay(interval),
              take(maxRetries),
              concat(throwError(() => new Error('Max polling attempts reached')))
            )
          ),
          retry({
            count: maxRetries,
            delay: (error, retryCount) => timer(Math.pow(2, retryCount) * 1000)
          })
        );
      }
    };
  }

  // Advanced form reactive patterns
  static createReactiveFormHelpers(fb: FormBuilder): ReactiveFormHelpers {
    return {
      // Dynamic form generation
      createDynamicForm: (config: FormFieldConfig[]): FormGroup => {
        const group: Record<string, FormControl> = {};

        config.forEach(field => {
          const validators = field.validators || [];
          const asyncValidators = field.asyncValidators || [];
          
          group[field.name] = fb.control(
            field.defaultValue ?? '',
            validators,
            asyncValidators
          );
        });

        return fb.group(group);
      },

      // Cross-field validation
      createCrossFieldValidator: (
        field1: string,
        field2: string,
        validatorFn: (value1: any, value2: any) => ValidationErrors | null
      ): ValidatorFn => {
        return (control: AbstractControl): ValidationErrors | null => {
          if (!control.parent) return null;
          
          const value1 = control.parent.get(field1)?.value;
          const value2 = control.parent.get(field2)?.value;
          
          return validatorFn(value1, value2);
        };
      },

      // Async validation with debouncing
      createAsyncValidator: (
        validationFn: (value: any) => Observable<ValidationErrors | null>,
        debounceTime: number = 300
      ): AsyncValidatorFn => {
        return (control: AbstractControl): Observable<ValidationErrors | null> => {
          if (!control.value) {
            return of(null);
          }

          return timer(debounceTime).pipe(
            switchMap(() => validationFn(control.value)),
            catchError(() => of({ validationError: true }))
          );
        };
      },

      // Form state management
      getFormState$: (form: FormGroup): Observable<FormState> => {
        return combineLatest([
          form.statusChanges.pipe(startWith(form.status)),
          form.valueChanges.pipe(startWith(form.value))
        ]).pipe(
          map(([status, value]) => ({
            valid: status === 'VALID',
            invalid: status === 'INVALID',
            pending: status === 'PENDING',
            disabled: status === 'DISABLED',
            dirty: form.dirty,
            touched: form.touched,
            value,
            errors: form.errors
          }))
        );
      }
    };
  }
}

// Advanced component communication patterns
@Injectable()
export class ComponentCommunicationService {
  private readonly eventBus = new Subject<ComponentEvent>();
  
  // Event-driven communication
  emit<T>(type: string, payload?: T): void {
    this.eventBus.next({ type, payload, timestamp: Date.now() });
  }

  // Type-safe event listening
  on<T>(type: string): Observable<T> {
    return this.eventBus.pipe(
      filter(event => event.type === type),
      map(event => event.payload),
      share()
    );
  }

  // Request-response pattern
  request<TRequest, TResponse>(
    type: string,
    payload: TRequest,
    timeout: number = 5000
  ): Observable<TResponse> {
    const requestId = this.generateRequestId();
    const responseType = `${type}:response:${requestId}`;

    // Send request
    this.emit(`${type}:request`, { ...payload, requestId });

    // Wait for response
    return this.on<TResponse>(responseType).pipe(
      take(1),
      timeout(timeout),
      catchError(error => 
        throwError(() => new Error(`Request timeout: ${type}`))
      )
    );
  }

  // Component lifecycle notifications
  notifyLifecycle(component: string, lifecycle: ComponentLifecycle): void {
    this.emit('component:lifecycle', { component, lifecycle });
  }

  private generateRequestId(): string {
    return Math.random().toString(36).substr(2, 9);
  }
}

// Advanced error handling service
@Injectable({
  providedIn: 'root'
})
export class ErrorHandlingService {
  private readonly errorSubject = new Subject<AppError>();
  
  readonly errors$ = this.errorSubject.asObservable();

  // Global error handling
  handleError(error: any, context?: string): Observable<never> {
    const appError = this.createAppError(error, context);
    this.errorSubject.next(appError);
    
    // Log error
    console.error('Application Error:', appError);
    
    return throwError(() => appError);
  }

  // HTTP error handling
  handleHttpError(error: HttpErrorResponse): Observable<never> {
    let userMessage: string;
    
    switch (error.status) {
      case 0:
        userMessage = 'Network error. Please check your connection.';
        break;
      case 400:
        userMessage = 'Invalid request. Please check your input.';
        break;
      case 401:
        userMessage = 'Authentication required. Please log in.';
        break;
      case 403:
        userMessage = 'Access denied. You do not have permission.';
        break;
      case 404:
        userMessage = 'The requested resource was not found.';
        break;
      case 500:
        userMessage = 'Server error. Please try again later.';
        break;
      default:
        userMessage = 'An unexpected error occurred.';
    }

    const appError: AppError = {
      message: userMessage,
      originalError: error,
      type: 'HTTP_ERROR',
      status: error.status,
      timestamp: new Date(),
      context: error.url || undefined
    };

    return this.handleError(appError);
  }

  // Retry with exponential backoff
  retryWithBackoff<T>(
    operation: () => Observable<T>,
    maxRetries: number = 3,
    backoffMs: number = 1000
  ): Observable<T> {
    return defer(() => operation()).pipe(
      retry({
        count: maxRetries,
        delay: (error, retryCount) => {
          if (this.shouldRetry(error)) {
            return timer(backoffMs * Math.pow(2, retryCount - 1));
          }
          return throwError(() => error);
        }
      }),
      catchError(error => this.handleError(error))
    );
  }

  private createAppError(error: any, context?: string): AppError {
    if (error instanceof AppError) {
      return error;
    }

    return {
      message: error?.message || 'An unknown error occurred',
      originalError: error,
      type: 'GENERAL_ERROR',
      timestamp: new Date(),
      context
    };
  }

  private shouldRetry(error: any): boolean {
    // Don't retry client errors (4xx)
    if (error instanceof HttpErrorResponse) {
      return error.status >= 500 || error.status === 0;
    }
    
    return true;
  }
}

// Type definitions for reactive patterns
interface ReactiveStateManager<T> {
  select<K extends keyof T>(key: K): Observable<T[K]>;
  selectDeep<R>(selector: (state: T) => R): Observable<R>;
  update(updater: (state: T) => T): void;
  patch(updates: Partial<T>): void;
  getSnapshot(): T;
  state$: Observable<T>;
}

interface HttpRequestManager {
  request<T>(key: string, request: () => Observable<T>): Observable<T>;
  cachedRequest<T>(key: string, request: () => Observable<T>, ttl?: number): Observable<T>;
  optimisticUpdate<T, U>(updateFn: () => Observable<T>, rollbackFn: () => void, optimisticAction: () => void): Observable<T>;
  poll<T>(request: () => Observable<T>, interval?: number, maxRetries?: number): Observable<T>;
}

interface ComponentEvent {
  type: string;
  payload?: any;
  timestamp: number;
}

interface AppError {
  message: string;
  originalError?: any;
  type: string;
  status?: number;
  timestamp: Date;
  context?: string;
}

enum ComponentLifecycle {
  INIT = 'init',
  AFTER_VIEW_INIT = 'after_view_init',
  DESTROY = 'destroy'
}

interface FormState {
  valid: boolean;
  invalid: boolean;
  pending: boolean;
  disabled: boolean;
  dirty: boolean;
  touched: boolean;
  value: any;
  errors: ValidationErrors | null;
}

interface FormFieldConfig {
  name: string;
  defaultValue?: any;
  validators?: ValidatorFn[];
  asyncValidators?: AsyncValidatorFn[];
}
```

### Phase 3: Performance Optimization and Testing

**Advanced Performance Optimization:**
```typescript
// Comprehensive performance optimization strategies
class AngularPerformanceOptimizer {
  // OnPush change detection optimization
  static optimizeChangeDetection(component: any): void {
    // Implement OnPush strategy helpers
    const trackByFunctions = new Map<string, TrackByFunction<any>>();
    
    // Generic trackBy function generator
    const createTrackBy = <T>(keyExtractor: (item: T) => any): TrackByFunction<T> => {
      return (index: number, item: T) => keyExtractor(item);
    };

    // Common trackBy functions
    trackByFunctions.set('id', createTrackBy((item: any) => item.id));
    trackByFunctions.set('index', (index: number) => index);
    
    return {
      trackByFunctions,
      createTrackBy,
      
      // Memoized computed properties
      memoize: <T, R>(fn: (arg: T) => R): (arg: T) => R => {
        const cache = new Map<T, R>();
        return (arg: T) => {
          if (cache.has(arg)) {
            return cache.get(arg)!;
          }
          const result = fn(arg);
          cache.set(arg, result);
          return result;
        };
      }
    };
  }

  // Bundle optimization and lazy loading
  static implementLazyLoading(): LazyLoadingConfig {
    return {
      // Route-based lazy loading
      routes: [
        {
          path: 'dashboard',
          loadComponent: () => import('./dashboard/dashboard.component').then(m => m.DashboardComponent)
        },
        {
          path: 'admin',
          loadChildren: () => import('./admin/admin.routes').then(m => m.ADMIN_ROUTES),
          canMatch: [AdminGuard]
        }
      ],

      // Component-level lazy loading
      lazyComponents: {
        'heavy-chart': () => import('./charts/heavy-chart.component').then(m => m.HeavyChartComponent),
        'data-table': () => import('./tables/data-table.component').then(m => m.DataTableComponent)
      },

      // Service lazy loading
      lazyServices: {
        'analytics': () => import('./services/analytics.service').then(m => m.AnalyticsService),
        'reporting': () => import('./services/reporting.service').then(m => m.ReportingService)
      }
    };
  }

  // Virtual scrolling and pagination
  static implementVirtualScrolling(): VirtualScrollConfig {
    return {
      // CDK Virtual Scrolling configuration
      virtualScrollOptions: {
        itemSize: 50,
        bufferSize: 5,
        viewportSize: 400
      },

      // Custom virtual scroll implementation
      createVirtualScrollDataSource: <T>(items: T[]): VirtualScrollDataSource<T> => {
        return {
          length: items.length,
          getItem: (index: number) => items[index],
          getRange: (start: number, end: number) => items.slice(start, end)
        };
      },

      // Intersection Observer for infinite scrolling
      createInfiniteScroll: (loadMore: () => void): IntersectionObserver => {
        return new IntersectionObserver(
          (entries) => {
            entries.forEach(entry => {
              if (entry.isIntersecting) {
                loadMore();
              }
            });
          },
          { threshold: 0.1 }
        );
      }
    };
  }

  // Memory management and leak prevention
  static implementMemoryManagement(): MemoryManagementConfig {
    return {
      // Subscription management
      createSubscriptionManager: (): SubscriptionManager => {
        const subscriptions = new Set<Subscription>();
        
        return {
          add: (subscription: Subscription) => {
            subscriptions.add(subscription);
          },
          
          unsubscribe: () => {
            subscriptions.forEach(sub => sub.unsubscribe());
            subscriptions.clear();
          },
          
          size: () => subscriptions.size
        };
      },

      // Weak reference management
      createWeakCache: <K extends object, V>(): WeakCache<K, V> => {
        const cache = new WeakMap<K, V>();
        
        return {
          set: (key: K, value: V) => cache.set(key, value),
          get: (key: K) => cache.get(key),
          has: (key: K) => cache.has(key),
          delete: (key: K) => cache.delete(key)
        };
      },

      // Event listener cleanup
      createEventManager: (): EventManager => {
        const listeners = new Map<string, (() => void)[]>();
        
        return {
          addEventListener: (event: string, handler: () => void, element: EventTarget = window) => {
            const cleanup = () => element.removeEventListener(event, handler);
            
            if (!listeners.has(event)) {
              listeners.set(event, []);
            }
            listeners.get(event)!.push(cleanup);
            
            element.addEventListener(event, handler);
            return cleanup;
          },
          
          removeAllListeners: () => {
            listeners.forEach(cleanupFns => {
              cleanupFns.forEach(cleanup => cleanup());
            });
            listeners.clear();
          }
        };
      }
    };
  }
}

// Advanced testing framework for Angular
class AngularTestingFramework {
  // Component testing with TestBed
  static createComponentTest<T>(componentClass: Type<T>): ComponentTestBuilder<T> {
    return {
      // Enhanced TestBed configuration
      configureTestBed: (config?: Partial<TestBedConfig>) => {
        const defaultConfig: TestBedConfig = {
          declarations: [],
          imports: [
            CommonModule,
            FormsModule,
            ReactiveFormsModule,
            NoopAnimationsModule
          ],
          providers: [],
          schemas: [NO_ERRORS_SCHEMA]
        };

        const mergedConfig = { ...defaultConfig, ...config };
        
        beforeEach(async () => {
          await TestBed.configureTestingModule({
            declarations: [componentClass, ...mergedConfig.declarations],
            imports: mergedConfig.imports,
            providers: mergedConfig.providers,
            schemas: mergedConfig.schemas
          }).compileComponents();
        });

        return this;
      },

      // Component fixture helpers
      createFixtureHelpers: (): FixtureHelpers<T> => {
        let fixture: ComponentFixture<T>;
        let component: T;

        beforeEach(() => {
          fixture = TestBed.createComponent(componentClass);
          component = fixture.componentInstance;
        });

        return {
          get fixture() { return fixture; },
          get component() { return component; },
          
          detectChanges: () => fixture.detectChanges(),
          
          getByTestId: (testId: string) => 
            fixture.debugElement.query(By.css(`[data-testid="${testId}"]`)),
          
          getAllByTestId: (testId: string) =>
            fixture.debugElement.queryAll(By.css(`[data-testid="${testId}"]`)),
          
          getByText: (text: string) =>
            fixture.debugElement.query(By.css('*')).nativeElement.textContent?.includes(text),
          
          triggerEvent: (element: DebugElement, eventType: string, eventData?: any) => {
            element.triggerEventHandler(eventType, eventData);
            fixture.detectChanges();
          }
        };
      }
    };
  }

  // Service testing with dependency injection
  static createServiceTest<T>(serviceClass: Type<T>): ServiceTestBuilder<T> {
    return {
      // Mock dependencies configuration
      configureDependencies: (mocks: Record<string, any> = {}) => {
        const providers = Object.entries(mocks).map(([token, mock]) => ({
          provide: token,
          useValue: mock
        }));

        beforeEach(() => {
          TestBed.configureTestingModule({
            providers: [
              serviceClass,
              ...providers
            ]
          });
        });

        return this;
      },

      // Service instance helpers
      createServiceHelpers: (): ServiceHelpers<T> => {
        let service: T;

        beforeEach(() => {
          service = TestBed.inject(serviceClass);
        });

        return {
          get service() { return service; },
          
          // HTTP testing helpers
          expectHttpCall: (httpMock: HttpTestingController, method: string, url: string) => {
            const req = httpMock.expectOne(url);
            expect(req.request.method).toBe(method);
            return req;
          },
          
          // Observable testing helpers
          expectObservableValue: <V>(observable: Observable<V>, expectedValue: V) => {
            let actualValue: V;
            observable.subscribe(value => actualValue = value);
            expect(actualValue!).toEqual(expectedValue);
          },
          
          expectObservableError: (observable: Observable<any>, expectedError: any) => {
            let actualError: any;
            observable.subscribe({
              error: error => actualError = error
            });
            expect(actualError).toEqual(expectedError);
          }
        };
      }
    };
  }

  // E2E testing with Protractor/Cypress patterns
  static createE2ETest(): E2ETestHelpers {
    return {
      // Page Object Model helpers
      createPageObject: (selectors: Record<string, string>) => {
        return Object.entries(selectors).reduce((page, [name, selector]) => {
          page[name] = {
            element: () => cy.get(selector),
            click: () => cy.get(selector).click(),
            type: (text: string) => cy.get(selector).type(text),
            should: (assertion: string, value?: any) => 
              value ? cy.get(selector).should(assertion, value) : cy.get(selector).should(assertion)
          };
          return page;
        }, {} as any);
      },

      // Custom commands
      addCommands: () => {
        Cypress.Commands.add('login', (email: string, password: string) => {
          cy.visit('/login');
          cy.get('[data-testid="email"]').type(email);
          cy.get('[data-testid="password"]').type(password);
          cy.get('[data-testid="login-button"]').click();
          cy.url().should('not.include', '/login');
        });

        Cypress.Commands.add('waitForAngular', () => {
          cy.window().then(win => {
            return new Cypress.Promise((resolve) => {
              const checkAngular = () => {
                if ((win as any).getAllAngularTestabilities) {
                  const testabilities = (win as any).getAllAngularTestabilities();
                  if (testabilities.every((t: any) => t.isStable())) {
                    resolve();
                  } else {
                    setTimeout(checkAngular, 10);
                  }
                } else {
                  resolve();
                }
              };
              checkAngular();
            });
          });
        });
      }
    };
  }
}

// Type definitions for performance and testing
interface LazyLoadingConfig {
  routes: Route[];
  lazyComponents: Record<string, () => Promise<any>>;
  lazyServices: Record<string, () => Promise<any>>;
}

interface VirtualScrollConfig {
  virtualScrollOptions: {
    itemSize: number;
    bufferSize: number;
    viewportSize: number;
  };
  createVirtualScrollDataSource<T>(items: T[]): VirtualScrollDataSource<T>;
  createInfiniteScroll(loadMore: () => void): IntersectionObserver;
}

interface VirtualScrollDataSource<T> {
  length: number;
  getItem(index: number): T;
  getRange(start: number, end: number): T[];
}

interface MemoryManagementConfig {
  createSubscriptionManager(): SubscriptionManager;
  createWeakCache<K extends object, V>(): WeakCache<K, V>;
  createEventManager(): EventManager;
}

interface SubscriptionManager {
  add(subscription: Subscription): void;
  unsubscribe(): void;
  size(): number;
}

interface WeakCache<K extends object, V> {
  set(key: K, value: V): void;
  get(key: K): V | undefined;
  has(key: K): boolean;
  delete(key: K): boolean;
}

interface EventManager {
  addEventListener(event: string, handler: () => void, element?: EventTarget): () => void;
  removeAllListeners(): void;
}

interface ComponentTestBuilder<T> {
  configureTestBed(config?: Partial<TestBedConfig>): this;
  createFixtureHelpers(): FixtureHelpers<T>;
}

interface ServiceTestBuilder<T> {
  configureDependencies(mocks?: Record<string, any>): this;
  createServiceHelpers(): ServiceHelpers<T>;
}

interface FixtureHelpers<T> {
  readonly fixture: ComponentFixture<T>;
  readonly component: T;
  detectChanges(): void;
  getByTestId(testId: string): DebugElement;
  getAllByTestId(testId: string): DebugElement[];
  getByText(text: string): boolean;
  triggerEvent(element: DebugElement, eventType: string, eventData?: any): void;
}

interface ServiceHelpers<T> {
  readonly service: T;
  expectHttpCall(httpMock: HttpTestingController, method: string, url: string): TestRequest;
  expectObservableValue<V>(observable: Observable<V>, expectedValue: V): void;
  expectObservableError(observable: Observable<any>, expectedError: any): void;
}

interface E2ETestHelpers {
  createPageObject(selectors: Record<string, string>): any;
  addCommands(): void;
}

interface TestBedConfig {
  declarations: any[];
  imports: any[];
  providers: any[];
  schemas: any[];
}
```

## Success Criteria

1. **Angular Architecture Excellence:**
   - Modern Angular 17+ implementation with standalone components and signals
   - Advanced dependency injection with hierarchical injectors
   - Reactive programming mastery with RxJS patterns and operators

2. **Performance Optimization:**
   - OnPush change detection strategy with optimized trackBy functions
   - Lazy loading implementation for routes, components, and services
   - Virtual scrolling for large datasets with memory management

3. **Developer Experience:**
   - Type-safe development with strict TypeScript configuration
   - Comprehensive testing framework with unit, integration, and E2E tests
   - Advanced debugging capabilities with Angular DevTools integration

4. **Production Readiness:**
   - Scalable component architecture with reusable patterns
   - Error handling and resilience with retry mechanisms
   - Security best practices with sanitization and validation

## Deliverables

- **Component Library:** Complete Angular component architecture with advanced patterns
- **State Management:** Comprehensive reactive state management with RxJS
- **Performance Framework:** Optimization strategies and virtual scrolling implementation
- **Testing Suite:** Complete testing framework with utilities and helpers
- **Production Configuration:** Build optimization and deployment strategies
- **Documentation:** Complete Angular development guide with best practices and patterns