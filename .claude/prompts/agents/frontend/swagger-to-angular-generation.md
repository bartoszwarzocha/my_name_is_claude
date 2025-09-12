# Angular Services and Models Generation from Swagger Documentation

## Mission
Generate complete, type-safe Angular services and data models from Swagger/OpenAPI specifications, ensuring seamless integration with Angular applications, proper TypeScript typing, and production-ready error handling and HTTP client configuration.

## Process

### Phase 1: Swagger Analysis and Angular Architecture Planning

#### 1.1 Swagger Specification Analysis
```bash
# Install required tools
npm install -g @openapitools/openapi-generator-cli
npm install @angular/common @angular/core rxjs

# Validate and analyze Swagger specification
openapi-generator-cli validate -i swagger.yml
npx swagger-codegen-cli config-help -l typescript-angular
```

**Key Analysis Points:**
- **API Endpoints:** All paths and HTTP methods
- **Data Models:** Component schemas and their relationships
- **Authentication:** Security schemes and requirements
- **Error Handling:** Error response formats
- **Business Logic:** Extract service patterns from descriptions

#### 1.2 Angular Project Structure Assessment
```bash
# Analyze current Angular structure
tree src/app -I "node_modules|dist" -L 3
ls -la src/app/services/ src/app/models/ src/app/interfaces/ 2>/dev/null
ng version
```

**Architecture Planning:**
- Service organization and module structure
- Model interfaces and type definitions
- HTTP interceptor configuration
- Error handling strategy
- Authentication integration patterns

### Phase 2: TypeScript Models and Interfaces Generation

#### 2.1 Core Model Interfaces
```typescript
// models/user.models.ts - Generated from Swagger components
export interface UserDetailResponse {
  /** Unique user identifier */
  id: number;
  
  /** Unique username for authentication */
  username: string;
  
  /** User's primary email address */
  email: string;
  
  /** User's profile information */
  profile?: UserProfile;
  
  /** User's assigned roles */
  roles: UserRole[];
  
  /** User's preferences */
  preferences?: UserPreferences;
  
  /** Account creation timestamp */
  createdAt: string;
  
  /** Last profile update timestamp */
  updatedAt?: string;
  
  /** Account status */
  isActive: boolean;
}

export interface UserProfile {
  /** User's first name */
  firstName?: string;
  
  /** User's last name */
  lastName?: string;
  
  /** URL to user's profile picture */
  avatar?: string;
  
  /** User's biography */
  bio?: string;
  
  /** User's location */
  location?: string;
}

export interface CreateUserRequest {
  /** Unique username for authentication */
  username: string;
  
  /** User's primary email address */
  email: string;
  
  /** User's password */
  password: string;
  
  /** User's profile information */
  profile?: UserProfile;
  
  /** User's assigned roles */
  roles?: string[];
}

export interface UpdateUserRequest {
  /** User's primary email address */
  email?: string;
  
  /** User's profile information */
  profile?: UserProfile;
  
  /** User's assigned roles */
  roles?: string[];
  
  /** Account status */
  isActive?: boolean;
}

// Enums for type safety
export enum UserRole {
  USER = 'user',
  ADMIN = 'admin',
  MODERATOR = 'moderator',
  GUEST = 'guest'
}

export enum ErrorCode {
  VALIDATION_ERROR = 'VALIDATION_ERROR',
  UNAUTHORIZED = 'UNAUTHORIZED',
  FORBIDDEN = 'FORBIDDEN',
  NOT_FOUND = 'NOT_FOUND',
  CONFLICT = 'CONFLICT',
  RATE_LIMIT_EXCEEDED = 'RATE_LIMIT_EXCEEDED',
  INTERNAL_ERROR = 'INTERNAL_ERROR'
}

// Response wrapper types
export interface ApiResponse<T> {
  data: T;
  success: boolean;
  message?: string;
  timestamp: string;
  requestId: string;
}

export interface ApiError {
  error: ErrorCode;
  message: string;
  details?: ValidationError[];
  timestamp: string;
  requestId: string;
}

export interface ValidationError {
  field: string;
  message: string;
  code: string;
}

// Pagination interfaces
export interface PaginatedRequest {
  page?: number;
  pageSize?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
  search?: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    currentPage: number;
    pageSize: number;
    totalPages: number;
    totalItems: number;
    hasNext: boolean;
    hasPrevious: boolean;
  };
}

// Query parameter interfaces
export interface GetUserOptions {
  include?: ('profile' | 'preferences' | 'roles')[];
}

export interface ListUsersOptions extends PaginatedRequest {
  role?: UserRole;
  isActive?: boolean;
  createdAfter?: string;
  createdBefore?: string;
}
```

#### 2.2 HTTP Configuration and Interceptors
```typescript
// services/http-config.service.ts
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, finalize } from 'rxjs/operators';
import { LoadingService } from './loading.service';
import { NotificationService } from './notification.service';
import { AuthService } from './auth.service';
import { ApiError } from '../models/user.models';

@Injectable()
export class ApiInterceptor implements HttpInterceptor {
  constructor(
    private loadingService: LoadingService,
    private notificationService: NotificationService,
    private authService: AuthService
  ) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Show loading indicator
    this.loadingService.show();

    // Add authentication header
    const authToken = this.authService.getToken();
    const authReq = authToken 
      ? req.clone({
          setHeaders: {
            'Authorization': `Bearer ${authToken}`,
            'Content-Type': 'application/json'
          }
        })
      : req.clone({
          setHeaders: {
            'Content-Type': 'application/json'
          }
        });

    // Add request ID for tracing
    const requestId = this.generateRequestId();
    const finalReq = authReq.clone({
      setHeaders: {
        ...authReq.headers,
        'X-Request-ID': requestId
      }
    });

    return next.handle(finalReq).pipe(
      tap((event: HttpEvent<any>) => {
        if (event instanceof HttpResponse) {
          // Log successful responses
          console.log(`HTTP ${finalReq.method} ${finalReq.url} - ${event.status}`, event.body);
        }
      }),
      catchError((error: HttpErrorResponse) => {
        // Handle different types of HTTP errors
        return this.handleHttpError(error, finalReq);
      }),
      finalize(() => {
        // Hide loading indicator
        this.loadingService.hide();
      })
    );
  }

  private handleHttpError(error: HttpErrorResponse, request: HttpRequest<any>): Observable<never> {
    let apiError: ApiError;

    if (error.error && typeof error.error === 'object') {
      // Structured API error response
      apiError = error.error as ApiError;
    } else {
      // Generic HTTP error
      apiError = {
        error: this.mapHttpStatusToErrorCode(error.status),
        message: error.message || 'An unexpected error occurred',
        timestamp: new Date().toISOString(),
        requestId: request.headers.get('X-Request-ID') || 'unknown'
      };
    }

    // Log error for debugging
    console.error(`HTTP Error ${error.status} for ${request.method} ${request.url}:`, apiError);

    // Handle specific error scenarios
    switch (error.status) {
      case 401:
        this.authService.logout();
        this.notificationService.showError('Session expired. Please log in again.');
        break;
      case 403:
        this.notificationService.showError('Access denied. You don\'t have permission for this action.');
        break;
      case 404:
        this.notificationService.showError('Requested resource not found.');
        break;
      case 409:
        this.notificationService.showError('Conflict: The resource already exists or is in use.');
        break;
      case 429:
        this.notificationService.showError('Too many requests. Please try again later.');
        break;
      case 500:
        this.notificationService.showError('Server error. Please try again later.');
        break;
      default:
        if (apiError.message) {
          this.notificationService.showError(apiError.message);
        }
    }

    return throwError(() => apiError);
  }

  private mapHttpStatusToErrorCode(status: number): string {
    const statusMap: Record<number, string> = {
      400: 'VALIDATION_ERROR',
      401: 'UNAUTHORIZED',
      403: 'FORBIDDEN',
      404: 'NOT_FOUND',
      409: 'CONFLICT',
      429: 'RATE_LIMIT_EXCEEDED',
      500: 'INTERNAL_ERROR'
    };
    return statusMap[status] || 'UNKNOWN_ERROR';
  }

  private generateRequestId(): string {
    return 'req_' + Math.random().toString(36).substr(2, 9);
  }
}
```

### Phase 3: Angular Service Implementation

#### 3.1 Core User Service
```typescript
// services/user.service.ts - Generated from Swagger specification
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, BehaviorSubject, throwError } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';
import { environment } from '../../environments/environment';
import {
  UserDetailResponse,
  CreateUserRequest,
  UpdateUserRequest,
  GetUserOptions,
  ListUsersOptions,
  PaginatedResponse,
  ApiError,
  UserRole
} from '../models/user.models';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private readonly baseUrl = `${environment.apiUrl}/api/users`;
  private currentUserSubject = new BehaviorSubject<UserDetailResponse | null>(null);
  
  // Public observables
  public readonly currentUser$ = this.currentUserSubject.asObservable();

  constructor(private http: HttpClient) {}

  /**
   * Get user by ID
   * @param id User identifier
   * @param options Query options
   * @returns Observable of user details
   */
  getUserById(id: number, options?: GetUserOptions): Observable<UserDetailResponse> {
    let params = new HttpParams();
    
    if (options?.include && options.include.length > 0) {
      // Handle array parameters correctly
      options.include.forEach(include => {
        params = params.append('include', include);
      });
    }

    return this.http.get<UserDetailResponse>(`${this.baseUrl}/${id}`, { params })
      .pipe(
        tap(user => {
          console.log('User retrieved:', user);
        }),
        catchError(error => this.handleServiceError('getUserById', error))
      );
  }

  /**
   * Get current authenticated user
   * @param options Query options
   * @returns Observable of current user details
   */
  getCurrentUser(options?: GetUserOptions): Observable<UserDetailResponse> {
    return this.getUserById(-1, options) // -1 represents current user in API
      .pipe(
        tap(user => {
          this.currentUserSubject.next(user);
        })
      );
  }

  /**
   * List users with pagination and filtering
   * @param options List options and filters
   * @returns Observable of paginated users
   */
  listUsers(options?: ListUsersOptions): Observable<PaginatedResponse<UserDetailResponse>> {
    let params = new HttpParams();

    if (options) {
      // Pagination parameters
      if (options.page !== undefined) {
        params = params.set('page', options.page.toString());
      }
      if (options.pageSize !== undefined) {
        params = params.set('pageSize', options.pageSize.toString());
      }
      
      // Sorting parameters
      if (options.sortBy) {
        params = params.set('sortBy', options.sortBy);
      }
      if (options.sortOrder) {
        params = params.set('sortOrder', options.sortOrder);
      }
      
      // Search parameters
      if (options.search) {
        params = params.set('search', options.search);
      }
      
      // Filter parameters
      if (options.role) {
        params = params.set('role', options.role);
      }
      if (options.isActive !== undefined) {
        params = params.set('isActive', options.isActive.toString());
      }
      if (options.createdAfter) {
        params = params.set('createdAfter', options.createdAfter);
      }
      if (options.createdBefore) {
        params = params.set('createdBefore', options.createdBefore);
      }
    }

    return this.http.get<PaginatedResponse<UserDetailResponse>>(this.baseUrl, { params })
      .pipe(
        tap(response => {
          console.log('Users listed:', response.pagination);
        }),
        catchError(error => this.handleServiceError('listUsers', error))
      );
  }

  /**
   * Create new user
   * @param userData User creation data
   * @returns Observable of created user
   */
  createUser(userData: CreateUserRequest): Observable<UserDetailResponse> {
    // Validate required fields
    if (!userData.username?.trim()) {
      return throwError(() => ({
        error: 'VALIDATION_ERROR',
        message: 'Username is required',
        timestamp: new Date().toISOString(),
        requestId: 'client-validation'
      } as ApiError));
    }

    if (!userData.email?.trim()) {
      return throwError(() => ({
        error: 'VALIDATION_ERROR',
        message: 'Email is required',
        timestamp: new Date().toISOString(),
        requestId: 'client-validation'
      } as ApiError));
    }

    if (!userData.password?.trim()) {
      return throwError(() => ({
        error: 'VALIDATION_ERROR',
        message: 'Password is required',
        timestamp: new Date().toISOString(),
        requestId: 'client-validation'
      } as ApiError));
    }

    return this.http.post<UserDetailResponse>(this.baseUrl, userData)
      .pipe(
        tap(user => {
          console.log('User created:', user);
        }),
        catchError(error => this.handleServiceError('createUser', error))
      );
  }

  /**
   * Update existing user
   * @param id User identifier
   * @param userData User update data
   * @returns Observable of updated user
   */
  updateUser(id: number, userData: UpdateUserRequest): Observable<UserDetailResponse> {
    if (id <= 0) {
      return throwError(() => ({
        error: 'VALIDATION_ERROR',
        message: 'Invalid user ID',
        timestamp: new Date().toISOString(),
        requestId: 'client-validation'
      } as ApiError));
    }

    return this.http.put<UserDetailResponse>(`${this.baseUrl}/${id}`, userData)
      .pipe(
        tap(user => {
          console.log('User updated:', user);
          // Update current user if updating self
          if (this.currentUserSubject.value?.id === user.id) {
            this.currentUserSubject.next(user);
          }
        }),
        catchError(error => this.handleServiceError('updateUser', error))
      );
  }

  /**
   * Delete user
   * @param id User identifier
   * @returns Observable of deletion result
   */
  deleteUser(id: number): Observable<void> {
    if (id <= 0) {
      return throwError(() => ({
        error: 'VALIDATION_ERROR',
        message: 'Invalid user ID',
        timestamp: new Date().toISOString(),
        requestId: 'client-validation'
      } as ApiError));
    }

    return this.http.delete<void>(`${this.baseUrl}/${id}`)
      .pipe(
        tap(() => {
          console.log('User deleted:', id);
        }),
        catchError(error => this.handleServiceError('deleteUser', error))
      );
  }

  /**
   * Change user password
   * @param id User identifier
   * @param currentPassword Current password
   * @param newPassword New password
   * @returns Observable of password change result
   */
  changePassword(id: number, currentPassword: string, newPassword: string): Observable<void> {
    const passwordData = {
      currentPassword,
      newPassword
    };

    return this.http.post<void>(`${this.baseUrl}/${id}/change-password`, passwordData)
      .pipe(
        tap(() => {
          console.log('Password changed for user:', id);
        }),
        catchError(error => this.handleServiceError('changePassword', error))
      );
  }

  /**
   * Upload user avatar
   * @param id User identifier
   * @param file Avatar image file
   * @returns Observable of updated user
   */
  uploadAvatar(id: number, file: File): Observable<UserDetailResponse> {
    const formData = new FormData();
    formData.append('avatar', file);

    return this.http.post<UserDetailResponse>(`${this.baseUrl}/${id}/avatar`, formData)
      .pipe(
        tap(user => {
          console.log('Avatar uploaded for user:', user);
          // Update current user if uploading self
          if (this.currentUserSubject.value?.id === user.id) {
            this.currentUserSubject.next(user);
          }
        }),
        catchError(error => this.handleServiceError('uploadAvatar', error))
      );
  }

  /**
   * Search users by query
   * @param query Search query
   * @param options Additional search options
   * @returns Observable of search results
   */
  searchUsers(query: string, options?: ListUsersOptions): Observable<PaginatedResponse<UserDetailResponse>> {
    const searchOptions: ListUsersOptions = {
      ...options,
      search: query
    };

    return this.listUsers(searchOptions);
  }

  /**
   * Get users by role
   * @param role User role to filter by
   * @param options Additional options
   * @returns Observable of users with specified role
   */
  getUsersByRole(role: UserRole, options?: ListUsersOptions): Observable<PaginatedResponse<UserDetailResponse>> {
    const roleOptions: ListUsersOptions = {
      ...options,
      role
    };

    return this.listUsers(roleOptions);
  }

  /**
   * Clear current user data
   */
  clearCurrentUser(): void {
    this.currentUserSubject.next(null);
  }

  /**
   * Handle service errors consistently
   * @param operation Operation name
   * @param error Error object
   * @returns Observable error
   */
  private handleServiceError(operation: string, error: any): Observable<never> {
    console.error(`UserService.${operation} failed:`, error);
    
    // If it's already an ApiError, pass it through
    if (error && error.error && error.message && error.timestamp) {
      return throwError(() => error);
    }

    // Convert generic errors to ApiError format
    const apiError: ApiError = {
      error: 'INTERNAL_ERROR',
      message: error.message || `${operation} failed`,
      timestamp: new Date().toISOString(),
      requestId: 'unknown'
    };

    return throwError(() => apiError);
  }
}
```

#### 3.2 Service Helper Utilities
```typescript
// services/api-helper.service.ts
import { Injectable } from '@angular/core';
import { HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiHelperService {
  
  /**
   * Build HTTP parameters from object
   * @param params Parameter object
   * @returns HttpParams instance
   */
  buildHttpParams(params: Record<string, any>): HttpParams {
    let httpParams = new HttpParams();

    Object.keys(params).forEach(key => {
      const value = params[key];
      
      if (value !== null && value !== undefined) {
        if (Array.isArray(value)) {
          // Handle array parameters
          value.forEach(item => {
            httpParams = httpParams.append(key, item.toString());
          });
        } else {
          httpParams = httpParams.set(key, value.toString());
        }
      }
    });

    return httpParams;
  }

  /**
   * Transform API response data
   * @param response API response
   * @returns Transformed data
   */
  transformResponse<T>(response: any): T {
    // Add any response transformation logic here
    return response;
  }

  /**
   * Validate email format
   * @param email Email address
   * @returns True if valid
   */
  isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  /**
   * Validate password strength
   * @param password Password
   * @returns Validation result
   */
  validatePassword(password: string): { isValid: boolean; message?: string } {
    if (password.length < 8) {
      return { isValid: false, message: 'Password must be at least 8 characters long' };
    }

    if (!/(?=.*[a-z])/.test(password)) {
      return { isValid: false, message: 'Password must contain at least one lowercase letter' };
    }

    if (!/(?=.*[A-Z])/.test(password)) {
      return { isValid: false, message: 'Password must contain at least one uppercase letter' };
    }

    if (!/(?=.*\d)/.test(password)) {
      return { isValid: false, message: 'Password must contain at least one digit' };
    }

    if (!/(?=.*[@$!%*?&])/.test(password)) {
      return { isValid: false, message: 'Password must contain at least one special character' };
    }

    return { isValid: true };
  }

  /**
   * Format date for API
   * @param date Date object
   * @returns ISO string
   */
  formatDateForApi(date: Date): string {
    return date.toISOString();
  }

  /**
   * Parse API date
   * @param dateString API date string
   * @returns Date object
   */
  parseApiDate(dateString: string): Date {
    return new Date(dateString);
  }
}
```

### Phase 4: Angular Component Integration Examples

#### 4.1 User List Component
```typescript
// components/user-list/user-list.component.ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subject, takeUntil, debounceTime, distinctUntilChanged } from 'rxjs';
import { UserService } from '../../services/user.service';
import { UserDetailResponse, ListUsersOptions, UserRole } from '../../models/user.models';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit, OnDestroy {
  users: UserDetailResponse[] = [];
  loading = false;
  error: string | null = null;
  
  // Pagination
  currentPage = 1;
  pageSize = 10;
  totalPages = 0;
  totalItems = 0;
  
  // Search
  searchControl = new FormControl('');
  
  // Filters
  selectedRole: UserRole | null = null;
  showActiveOnly = true;
  
  // Sorting
  sortBy = 'username';
  sortOrder: 'asc' | 'desc' = 'asc';
  
  // Available roles for filter
  roles = Object.values(UserRole);
  
  private destroy$ = new Subject<void>();

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.setupSearch();
    this.loadUsers();
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  private setupSearch(): void {
    this.searchControl.valueChanges
      .pipe(
        debounceTime(300),
        distinctUntilChanged(),
        takeUntil(this.destroy$)
      )
      .subscribe(() => {
        this.currentPage = 1; // Reset to first page
        this.loadUsers();
      });
  }

  loadUsers(): void {
    this.loading = true;
    this.error = null;

    const options: ListUsersOptions = {
      page: this.currentPage,
      pageSize: this.pageSize,
      sortBy: this.sortBy,
      sortOrder: this.sortOrder,
      search: this.searchControl.value || undefined,
      role: this.selectedRole || undefined,
      isActive: this.showActiveOnly
    };

    this.userService.listUsers(options)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: (response) => {
          this.users = response.data;
          this.totalPages = response.pagination.totalPages;
          this.totalItems = response.pagination.totalItems;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error loading users:', error);
          this.error = error.message || 'Failed to load users';
          this.loading = false;
        }
      });
  }

  onPageChange(page: number): void {
    this.currentPage = page;
    this.loadUsers();
  }

  onSortChange(field: string): void {
    if (this.sortBy === field) {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortBy = field;
      this.sortOrder = 'asc';
    }
    this.loadUsers();
  }

  onRoleFilter(role: UserRole | null): void {
    this.selectedRole = role;
    this.currentPage = 1;
    this.loadUsers();
  }

  onActiveFilter(showActiveOnly: boolean): void {
    this.showActiveOnly = showActiveOnly;
    this.currentPage = 1;
    this.loadUsers();
  }

  trackByUserId(index: number, user: UserDetailResponse): number {
    return user.id;
  }
}
```

#### 4.2 User Form Component
```typescript
// components/user-form/user-form.component.ts
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl } from '@angular/forms';
import { UserService } from '../../services/user.service';
import { ApiHelperService } from '../../services/api-helper.service';
import { UserDetailResponse, CreateUserRequest, UpdateUserRequest } from '../../models/user.models';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.scss']
})
export class UserFormComponent implements OnInit {
  @Input() user: UserDetailResponse | null = null;
  @Input() isEditMode = false;
  @Output() userSaved = new EventEmitter<UserDetailResponse>();
  @Output() cancelled = new EventEmitter<void>();

  userForm: FormGroup;
  loading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private apiHelper: ApiHelperService
  ) {
    this.userForm = this.createForm();
  }

  ngOnInit(): void {
    if (this.user) {
      this.populateForm(this.user);
    }
  }

  private createForm(): FormGroup {
    return this.fb.group({
      username: ['', [
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(30),
        Validators.pattern(/^[a-zA-Z0-9_-]+$/)
      ]],
      email: ['', [
        Validators.required,
        Validators.email
      ]],
      password: ['', this.isEditMode ? [] : [
        Validators.required,
        this.passwordValidator.bind(this)
      ]],
      profile: this.fb.group({
        firstName: ['', [Validators.maxLength(50)]],
        lastName: ['', [Validators.maxLength(50)]],
        bio: ['', [Validators.maxLength(500)]],
        location: ['', [Validators.maxLength(100)]]
      })
    });
  }

  private populateForm(user: UserDetailResponse): void {
    this.userForm.patchValue({
      username: user.username,
      email: user.email,
      profile: {
        firstName: user.profile?.firstName || '',
        lastName: user.profile?.lastName || '',
        bio: user.profile?.bio || '',
        location: user.profile?.location || ''
      }
    });

    if (this.isEditMode) {
      // Disable username in edit mode
      this.userForm.get('username')?.disable();
      // Make password optional in edit mode
      this.userForm.get('password')?.clearValidators();
      this.userForm.get('password')?.updateValueAndValidity();
    }
  }

  private passwordValidator(control: AbstractControl): { [key: string]: any } | null {
    if (!control.value) {
      return null; // Let required validator handle empty values
    }

    const result = this.apiHelper.validatePassword(control.value);
    return result.isValid ? null : { passwordStrength: { message: result.message } };
  }

  get usernameControl() { return this.userForm.get('username'); }
  get emailControl() { return this.userForm.get('email'); }
  get passwordControl() { return this.userForm.get('password'); }

  onSubmit(): void {
    if (this.userForm.invalid) {
      this.markFormGroupTouched();
      return;
    }

    this.loading = true;
    this.error = null;

    const formData = this.userForm.value;

    if (this.isEditMode && this.user) {
      // Update existing user
      const updateData: UpdateUserRequest = {
        email: formData.email,
        profile: formData.profile
      };

      this.userService.updateUser(this.user.id, updateData).subscribe({
        next: (updatedUser) => {
          this.userSaved.emit(updatedUser);
          this.loading = false;
        },
        error: (error) => {
          this.error = error.message || 'Failed to update user';
          this.loading = false;
        }
      });
    } else {
      // Create new user
      const createData: CreateUserRequest = formData;

      this.userService.createUser(createData).subscribe({
        next: (newUser) => {
          this.userSaved.emit(newUser);
          this.loading = false;
        },
        error: (error) => {
          this.error = error.message || 'Failed to create user';
          this.loading = false;
        }
      });
    }
  }

  onCancel(): void {
    this.cancelled.emit();
  }

  private markFormGroupTouched(): void {
    Object.keys(this.userForm.controls).forEach(key => {
      const control = this.userForm.get(key);
      control?.markAsTouched();

      if (control instanceof FormGroup) {
        this.markFormGroupTouched();
      }
    });
  }
}
```

## Deliverables

### 1. Complete TypeScript Models
- **Interface Definitions:** All Swagger schemas as TypeScript interfaces
- **Type Safety:** Proper typing for all API interactions
- **Enums and Constants:** Type-safe enumerations for API values
- **Validation Models:** Client-side validation interfaces

### 2. Production-Ready Services
- **HTTP Services:** Complete API integration with error handling
- **Observables:** RxJS-based reactive programming patterns
- **Interceptors:** Authentication and error handling middleware
- **Caching:** Service-level caching strategies

### 3. Angular Integration
- **Dependency Injection:** Proper service registration
- **Module Configuration:** HTTP client and interceptor setup
- **Component Examples:** Usage examples with forms and lists
- **Reactive Forms:** Form validation and user input handling

### 4. Developer Experience
- **TypeScript Support:** Full IntelliSense and type checking
- **Error Handling:** Consistent error management
- **Documentation:** Code comments and usage examples
- **Testing Setup:** Unit test examples and mocks

## Quality Gates

### ✅ Type Safety
- [ ] All models match Swagger specification
- [ ] Proper TypeScript typing throughout
- [ ] No `any` types in production code
- [ ] Enum usage for restricted values
- [ ] Interface composition for complex types

### ✅ Service Quality
- [ ] Complete CRUD operations implemented
- [ ] Proper error handling and user feedback
- [ ] Observable patterns correctly implemented
- [ ] HTTP interceptors configured
- [ ] Authentication integration complete

### ✅ Angular Best Practices
- [ ] Proper service lifecycle management
- [ ] Memory leak prevention with takeUntil
- [ ] Reactive forms with validation
- [ ] Component separation of concerns
- [ ] Performance optimization with trackBy

This prompt provides comprehensive guidance for generating production-ready Angular services and models from Swagger documentation, ensuring type safety and Angular best practices.