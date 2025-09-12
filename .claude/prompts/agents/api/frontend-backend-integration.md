# Frontend-Backend Integration

## Mission
Implement comprehensive integration between frontend and backend applications, adapting to the technology stack specified in CLAUDE.md. Create seamless communication, robust authentication, proper error handling, and efficient data flow between frontend and backend layers.

## Pre-Implementation Analysis

### Step 1: Technology Stack Detection
**CRITICAL: Always analyze CLAUDE.md first to determine frontend and backend technologies:**
```bash
# Read project configuration
cat CLAUDE.md | grep -A 10 "Frontend\|Backend\|primary_language"
```

**Frontend technology detection:**
```bash
# Angular projects
find . -name "angular.json" -o -name "package.json" | head -3
grep -r "@angular" package.json 2>/dev/null

# React projects
find . -name "package.json" | head -3
grep -r "react" package.json 2>/dev/null

# Vue projects
grep -r "vue" package.json 2>/dev/null

# Check existing API integration
find . -name "*.service.ts" -o -name "*api*" -o -name "*http*" | head -5
```

**Backend technology detection:**
```bash
# Java/Spring Boot
find . -name "pom.xml" -o -name "*.java" | head -3
grep -r "spring-boot" pom.xml 2>/dev/null

# .NET Core
find . -name "*.csproj" -o -name "*.cs" | head -3
grep -r "Microsoft.AspNetCore" . --include="*.csproj" 2>/dev/null

# Node.js
find . -name "package.json" | grep -v node_modules | head -3
grep -r "express\|fastify\|koa" package.json 2>/dev/null

# Python
find . -name "requirements.txt" -o -name "*.py" | head -3
grep -r "django\|flask\|fastapi" requirements.txt 2>/dev/null
```

### Step 2: Existing Integration Analysis
```bash
# Check API configuration
find . -name "*config*" -o -name "*env*" | grep -v node_modules | head -5
grep -r "API_URL\|BASE_URL\|BACKEND" . --include="*.ts" --include="*.js" --include="*.env" 2>/dev/null | head -5

# Check authentication setup
find . -name "*auth*" -o -name "*jwt*" -o -name "*token*" | grep -v node_modules | head -5
```

## Technology-Specific Integration Patterns

**⚠️ IMPORTANT: Select integration approach based on CLAUDE.md frontend and backend technology specification**

### Angular + Spring Boot Integration

**Use when CLAUDE.md specifies: Angular frontend, Java/Spring Boot backend**

```typescript
// src/app/core/services/api.service.ts - Angular HTTP service
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, throwError, BehaviorSubject } from 'rxjs';
import { catchError, retry, timeout, finalize } from 'rxjs/operators';
import { environment } from '../../../environments/environment';

export interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
  timestamp: string;
}

export interface ErrorResponse {
  error: string;
  message: string;
  details?: any[];
  timestamp: string;
  path: string;
  status: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly baseUrl = environment.apiUrl;
  private readonly defaultTimeout = 30000; // 30 seconds
  private loadingSubject = new BehaviorSubject<boolean>(false);
  
  public loading$ = this.loadingSubject.asObservable();

  constructor(private http: HttpClient) {}

  /**
   * GET request with proper error handling
   */
  get<T>(endpoint: string, params?: HttpParams, options?: {
    timeout?: number;
    retries?: number;
    requireAuth?: boolean;
  }): Observable<ApiResponse<T>> {
    
    const url = `${this.baseUrl}/${endpoint.replace(/^\//, '')}`;
    const httpOptions = this.buildHttpOptions(params, options?.requireAuth);
    
    this.setLoading(true);
    
    return this.http.get<ApiResponse<T>>(url, httpOptions)
      .pipe(
        timeout(options?.timeout || this.defaultTimeout),
        retry(options?.retries || 1),
        catchError(this.handleError.bind(this)),
        finalize(() => this.setLoading(false))
      );
  }

  /**
   * POST request with proper error handling
   */
  post<T>(endpoint: string, body: any, options?: {
    timeout?: number;
    retries?: number;
    requireAuth?: boolean;
  }): Observable<ApiResponse<T>> {
    
    const url = `${this.baseUrl}/${endpoint.replace(/^\//, '')}`;
    const httpOptions = this.buildHttpOptions(undefined, options?.requireAuth);
    
    this.setLoading(true);
    
    return this.http.post<ApiResponse<T>>(url, body, httpOptions)
      .pipe(
        timeout(options?.timeout || this.defaultTimeout),
        retry(options?.retries || 0), // Don't retry POST by default
        catchError(this.handleError.bind(this)),
        finalize(() => this.setLoading(false))
      );
  }

  /**
   * PUT request with proper error handling
   */
  put<T>(endpoint: string, body: any, options?: {
    timeout?: number;
    requireAuth?: boolean;
  }): Observable<ApiResponse<T>> {
    
    const url = `${this.baseUrl}/${endpoint.replace(/^\//, '')}`;
    const httpOptions = this.buildHttpOptions(undefined, options?.requireAuth);
    
    this.setLoading(true);
    
    return this.http.put<ApiResponse<T>>(url, body, httpOptions)
      .pipe(
        timeout(options?.timeout || this.defaultTimeout),
        catchError(this.handleError.bind(this)),
        finalize(() => this.setLoading(false))
      );
  }

  /**
   * DELETE request with proper error handling
   */
  delete<T>(endpoint: string, options?: {
    timeout?: number;
    requireAuth?: boolean;
  }): Observable<ApiResponse<T>> {
    
    const url = `${this.baseUrl}/${endpoint.replace(/^\//, '')}`;
    const httpOptions = this.buildHttpOptions(undefined, options?.requireAuth);
    
    this.setLoading(true);
    
    return this.http.delete<ApiResponse<T>>(url, httpOptions)
      .pipe(
        timeout(options?.timeout || this.defaultTimeout),
        catchError(this.handleError.bind(this)),
        finalize(() => this.setLoading(false))
      );
  }

  private buildHttpOptions(params?: HttpParams, requireAuth: boolean = true): any {
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });

    if (requireAuth) {
      const token = this.getAuthToken();
      if (token) {
        headers = headers.set('Authorization', `Bearer ${token}`);
      }
    }

    return {
      headers,
      params,
      observe: 'response' as const
    };
  }

  private getAuthToken(): string | null {
    return localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An unexpected error occurred';
    let errorDetails: any = null;

    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = `Client Error: ${error.error.message}`;
    } else {
      // Server-side error
      if (error.error && error.error.message) {
        errorMessage = error.error.message;
        errorDetails = error.error.details;
      } else {
        switch (error.status) {
          case 400:
            errorMessage = 'Bad Request - Please check your input';
            break;
          case 401:
            errorMessage = 'Unauthorized - Please log in again';
            // Redirect to login
            this.handleUnauthorized();
            break;
          case 403:
            errorMessage = 'Forbidden - You do not have permission to access this resource';
            break;
          case 404:
            errorMessage = 'Not Found - The requested resource was not found';
            break;
          case 409:
            errorMessage = 'Conflict - The resource already exists or there is a conflict';
            break;
          case 422:
            errorMessage = 'Validation Error - Please check your input';
            break;
          case 429:
            errorMessage = 'Too Many Requests - Please try again later';
            break;
          case 500:
            errorMessage = 'Internal Server Error - Please try again later';
            break;
          case 503:
            errorMessage = 'Service Unavailable - Please try again later';
            break;
          default:
            errorMessage = `HTTP Error ${error.status}: ${error.statusText}`;
        }
      }
    }

    console.error('API Error:', error);

    const errorResponse: ErrorResponse = {
      error: error.error?.error || 'API_ERROR',
      message: errorMessage,
      details: errorDetails,
      timestamp: new Date().toISOString(),
      path: error.url || '',
      status: error.status
    };

    return throwError(() => errorResponse);
  }

  private handleUnauthorized(): void {
    // Clear stored tokens
    localStorage.removeItem('access_token');
    sessionStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    
    // Redirect to login page
    window.location.href = '/login';
  }

  private setLoading(loading: boolean): void {
    this.loadingSubject.next(loading);
  }
}
```

```java
// src/main/java/com/company/config/CorsConfig.java - Spring Boot CORS configuration
package com.company.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.Arrays;
import java.util.List;

@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Value("${app.cors.allowed-origins}")
    private List<String> allowedOrigins;

    @Value("${app.cors.allowed-methods}")
    private List<String> allowedMethods;

    @Value("${app.cors.allowed-headers}")
    private List<String> allowedHeaders;

    @Value("${app.cors.allow-credentials:true}")
    private boolean allowCredentials;

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins(allowedOrigins.toArray(new String[0]))
                .allowedMethods(allowedMethods.toArray(new String[0]))
                .allowedHeaders(allowedHeaders.toArray(new String[0]))
                .allowCredentials(allowCredentials)
                .maxAge(3600); // 1 hour
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();
        
        // Allow specific origins
        configuration.setAllowedOriginPatterns(allowedOrigins);
        
        // Allow specific methods
        configuration.setAllowedMethods(allowedMethods);
        
        // Allow specific headers
        configuration.setAllowedHeaders(allowedHeaders);
        
        // Allow credentials
        configuration.setAllowCredentials(allowCredentials);
        
        // Expose specific headers to the client
        configuration.setExposedHeaders(Arrays.asList(
            "Authorization",
            "Content-Disposition",
            "X-Total-Count",
            "X-Page-Number",
            "X-Page-Size"
        ));

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", configuration);
        
        return source;
    }
}
```

```java
// src/main/java/com/company/dto/ApiResponse.java - Standardized response format
package com.company.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ApiResponse<T> {
    
    private T data;
    private String message;
    
    @Builder.Default
    private boolean success = true;
    
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss")
    @Builder.Default
    private LocalDateTime timestamp = LocalDateTime.now();
    
    // Metadata for pagination
    private PaginationMetadata pagination;
    
    public static <T> ApiResponse<T> success(T data) {
        return ApiResponse.<T>builder()
                .data(data)
                .success(true)
                .build();
    }
    
    public static <T> ApiResponse<T> success(T data, String message) {
        return ApiResponse.<T>builder()
                .data(data)
                .message(message)
                .success(true)
                .build();
    }
    
    public static <T> ApiResponse<T> error(String message) {
        return ApiResponse.<T>builder()
                .message(message)
                .success(false)
                .build();
    }
    
    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class PaginationMetadata {
        private int page;
        private int size;
        private long totalElements;
        private int totalPages;
        private boolean hasNext;
        private boolean hasPrevious;
    }
}
```

### Angular + .NET Core Integration

**Use when CLAUDE.md specifies: Angular frontend, .NET Core backend**

```typescript
// src/app/core/services/auth.service.ts - Angular authentication service
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, of, throwError } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { environment } from '../../../environments/environment';

export interface LoginRequest {
  username: string;
  password: string;
  rememberMe?: boolean;
}

export interface LoginResponse {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
  tokenType: string;
  user: UserInfo;
}

export interface UserInfo {
  id: string;
  username: string;
  email: string;
  firstName: string;
  lastName: string;
  roles: string[];
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly apiUrl = environment.apiUrl;
  private currentUserSubject = new BehaviorSubject<UserInfo | null>(null);
  private jwtHelper = new JwtHelperService();
  
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(
    private http: HttpClient,
    private router: Router
  ) {
    this.initializeAuthState();
  }

  private initializeAuthState(): void {
    const token = this.getAccessToken();
    if (token && !this.jwtHelper.isTokenExpired(token)) {
      try {
        const decodedToken = this.jwtHelper.decodeToken(token);
        const user: UserInfo = {
          id: decodedToken.sub,
          username: decodedToken.username,
          email: decodedToken.email,
          firstName: decodedToken.given_name,
          lastName: decodedToken.family_name,
          roles: decodedToken.roles || []
        };
        this.currentUserSubject.next(user);
      } catch (error) {
        console.error('Error decoding token:', error);
        this.clearTokens();
      }
    }
  }

  login(credentials: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.apiUrl}/auth/login`, credentials)
      .pipe(
        tap(response => this.handleLoginSuccess(response, credentials.rememberMe)),
        catchError(this.handleAuthError.bind(this))
      );
  }

  logout(): void {
    const refreshToken = this.getRefreshToken();
    
    if (refreshToken) {
      this.http.post(`${this.apiUrl}/auth/logout`, { refreshToken })
        .pipe(catchError(() => of(null)))
        .subscribe();
    }
    
    this.clearTokens();
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }

  refreshToken(): Observable<LoginResponse> {
    const refreshToken = this.getRefreshToken();
    
    if (!refreshToken) {
      return throwError(() => new Error('No refresh token available'));
    }

    return this.http.post<LoginResponse>(`${this.apiUrl}/auth/refresh`, {
      refreshToken: refreshToken
    }).pipe(
      tap(response => this.handleLoginSuccess(response, true)),
      catchError(error => {
        this.logout();
        return throwError(() => error);
      })
    );
  }

  isAuthenticated(): boolean {
    const token = this.getAccessToken();
    return token != null && !this.jwtHelper.isTokenExpired(token);
  }

  hasRole(role: string): boolean {
    const user = this.currentUserSubject.value;
    return user?.roles?.includes(role) || false;
  }

  hasAnyRole(roles: string[]): boolean {
    return roles.some(role => this.hasRole(role));
  }

  getCurrentUser(): UserInfo | null {
    return this.currentUserSubject.value;
  }

  getAccessToken(): string | null {
    return localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
  }

  private getRefreshToken(): string | null {
    return localStorage.getItem('refresh_token') || sessionStorage.getItem('refresh_token');
  }

  private handleLoginSuccess(response: LoginResponse, rememberMe: boolean = false): void {
    const storage = rememberMe ? localStorage : sessionStorage;
    
    storage.setItem('access_token', response.accessToken);
    storage.setItem('refresh_token', response.refreshToken);
    
    // Clear the other storage to avoid conflicts
    const otherStorage = rememberMe ? sessionStorage : localStorage;
    otherStorage.removeItem('access_token');
    otherStorage.removeItem('refresh_token');
    
    this.currentUserSubject.next(response.user);
  }

  private handleAuthError(error: any): Observable<never> {
    if (error.status === 401) {
      this.clearTokens();
      this.currentUserSubject.next(null);
    }
    return throwError(() => error);
  }

  private clearTokens(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    sessionStorage.removeItem('access_token');
    sessionStorage.removeItem('refresh_token');
  }
}
```

```csharp
// Controllers/AuthController.cs - .NET Core authentication controller
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Identity;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using DesktopApp.Models;
using DesktopApp.DTOs;

namespace DesktopApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly SignInManager<ApplicationUser> _signInManager;
        private readonly IConfiguration _configuration;
        private readonly ILogger<AuthController> _logger;

        public AuthController(
            UserManager<ApplicationUser> userManager,
            SignInManager<ApplicationUser> signInManager,
            IConfiguration configuration,
            ILogger<AuthController> logger)
        {
            _userManager = userManager;
            _signInManager = signInManager;
            _configuration = configuration;
            _logger = logger;
        }

        [HttpPost("login")]
        public async Task<ActionResult<ApiResponse<LoginResponse>>> Login(
            [FromBody] LoginRequest request)
        {
            try
            {
                if (!ModelState.IsValid)
                {
                    return BadRequest(ApiResponse<LoginResponse>.Error("Invalid request data"));
                }

                var user = await _userManager.FindByNameAsync(request.Username) ??
                          await _userManager.FindByEmailAsync(request.Username);

                if (user == null)
                {
                    _logger.LogWarning("Login attempt with invalid username: {Username}", request.Username);
                    return Unauthorized(ApiResponse<LoginResponse>.Error("Invalid credentials"));
                }

                var result = await _signInManager.CheckPasswordSignInAsync(user, request.Password, lockoutOnFailure: true);

                if (!result.Succeeded)
                {
                    if (result.IsLockedOut)
                    {
                        _logger.LogWarning("Account locked for user: {UserId}", user.Id);
                        return Unauthorized(ApiResponse<LoginResponse>.Error("Account is locked out"));
                    }

                    _logger.LogWarning("Failed login attempt for user: {UserId}", user.Id);
                    return Unauthorized(ApiResponse<LoginResponse>.Error("Invalid credentials"));
                }

                var tokens = await GenerateTokensAsync(user);
                var userInfo = await CreateUserInfoAsync(user);

                var loginResponse = new LoginResponse
                {
                    AccessToken = tokens.AccessToken,
                    RefreshToken = tokens.RefreshToken,
                    ExpiresIn = tokens.ExpiresIn,
                    TokenType = "Bearer",
                    User = userInfo
                };

                _logger.LogInformation("User logged in successfully: {UserId}", user.Id);
                return Ok(ApiResponse<LoginResponse>.Success(loginResponse, "Login successful"));
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error during login process");
                return StatusCode(500, ApiResponse<LoginResponse>.Error("An error occurred during login"));
            }
        }

        [HttpPost("refresh")]
        public async Task<ActionResult<ApiResponse<LoginResponse>>> RefreshToken(
            [FromBody] RefreshTokenRequest request)
        {
            try
            {
                var principal = GetPrincipalFromExpiredToken(request.RefreshToken);
                if (principal == null)
                {
                    return Unauthorized(ApiResponse<LoginResponse>.Error("Invalid refresh token"));
                }

                var username = principal.Identity?.Name;
                var user = await _userManager.FindByNameAsync(username);

                if (user == null)
                {
                    return Unauthorized(ApiResponse<LoginResponse>.Error("Invalid refresh token"));
                }

                // Validate refresh token from database
                if (!await ValidateRefreshTokenAsync(user, request.RefreshToken))
                {
                    return Unauthorized(ApiResponse<LoginResponse>.Error("Invalid refresh token"));
                }

                var tokens = await GenerateTokensAsync(user);
                var userInfo = await CreateUserInfoAsync(user);

                var loginResponse = new LoginResponse
                {
                    AccessToken = tokens.AccessToken,
                    RefreshToken = tokens.RefreshToken,
                    ExpiresIn = tokens.ExpiresIn,
                    TokenType = "Bearer",
                    User = userInfo
                };

                return Ok(ApiResponse<LoginResponse>.Success(loginResponse, "Token refreshed successfully"));
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error during token refresh");
                return StatusCode(500, ApiResponse<LoginResponse>.Error("An error occurred during token refresh"));
            }
        }

        [HttpPost("logout")]
        public async Task<ActionResult<ApiResponse<object>>> Logout(
            [FromBody] LogoutRequest request)
        {
            try
            {
                // Invalidate refresh token in database
                await InvalidateRefreshTokenAsync(request.RefreshToken);

                return Ok(ApiResponse<object>.Success(null, "Logged out successfully"));
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error during logout");
                return StatusCode(500, ApiResponse<object>.Error("An error occurred during logout"));
            }
        }

        private async Task<TokenResponse> GenerateTokensAsync(ApplicationUser user)
        {
            var roles = await _userManager.GetRolesAsync(user);
            
            var claims = new List<Claim>
            {
                new(ClaimTypes.NameIdentifier, user.Id),
                new(ClaimTypes.Name, user.UserName),
                new(ClaimTypes.Email, user.Email),
                new("username", user.UserName),
                new("given_name", user.FirstName ?? ""),
                new("family_name", user.LastName ?? ""),
                new(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()),
                new(JwtRegisteredClaimNames.Iat, 
                    new DateTimeOffset(DateTime.UtcNow).ToUnixTimeSeconds().ToString(), 
                    ClaimValueTypes.Integer64)
            };

            // Add role claims
            foreach (var role in roles)
            {
                claims.Add(new Claim(ClaimTypes.Role, role));
                claims.Add(new Claim("roles", role));
            }

            var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["Jwt:Key"]));
            var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);
            var expiresIn = int.Parse(_configuration["Jwt:ExpirationInMinutes"]);

            var token = new JwtSecurityToken(
                issuer: _configuration["Jwt:Issuer"],
                audience: _configuration["Jwt:Audience"],
                claims: claims,
                expires: DateTime.UtcNow.AddMinutes(expiresIn),
                signingCredentials: credentials
            );

            var accessToken = new JwtSecurityTokenHandler().WriteToken(token);
            var refreshToken = GenerateRefreshToken();

            // Store refresh token in database
            await StoreRefreshTokenAsync(user, refreshToken);

            return new TokenResponse
            {
                AccessToken = accessToken,
                RefreshToken = refreshToken,
                ExpiresIn = expiresIn * 60 // Convert to seconds
            };
        }

        private async Task<UserInfo> CreateUserInfoAsync(ApplicationUser user)
        {
            var roles = await _userManager.GetRolesAsync(user);

            return new UserInfo
            {
                Id = user.Id,
                Username = user.UserName,
                Email = user.Email,
                FirstName = user.FirstName,
                LastName = user.LastName,
                Roles = roles.ToArray()
            };
        }

        private ClaimsPrincipal? GetPrincipalFromExpiredToken(string token)
        {
            var tokenValidationParameters = new TokenValidationParameters
            {
                ValidateAudience = false,
                ValidateIssuer = false,
                ValidateIssuerSigningKey = true,
                IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["Jwt:Key"])),
                ValidateLifetime = false
            };

            var tokenHandler = new JwtSecurityTokenHandler();
            try
            {
                var principal = tokenHandler.ValidateToken(token, tokenValidationParameters, out SecurityToken securityToken);
                if (securityToken is not JwtSecurityToken jwtSecurityToken || 
                    !jwtSecurityToken.Header.Alg.Equals(SecurityAlgorithms.HmacSha256, StringComparison.InvariantCultureIgnoreCase))
                {
                    return null;
                }

                return principal;
            }
            catch
            {
                return null;
            }
        }

        private string GenerateRefreshToken()
        {
            return Guid.NewGuid().ToString();
        }

        private async Task StoreRefreshTokenAsync(ApplicationUser user, string refreshToken)
        {
            // Implementation depends on your data model
            // Store refresh token with expiration date
        }

        private async Task<bool> ValidateRefreshTokenAsync(ApplicationUser user, string refreshToken)
        {
            // Implementation depends on your data model
            // Validate refresh token exists and is not expired
            return true;
        }

        private async Task InvalidateRefreshTokenAsync(string refreshToken)
        {
            // Implementation depends on your data model
            // Mark refresh token as invalid
        }
    }

    public class TokenResponse
    {
        public string AccessToken { get; set; }
        public string RefreshToken { get; set; }
        public int ExpiresIn { get; set; }
    }
}
```

### React + Node.js Integration

**Use when CLAUDE.md specifies: React frontend, Node.js backend**

```javascript
// src/services/apiService.js - React API service with Axios
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:3001/api';
const REQUEST_TIMEOUT = 30000;

class ApiService {
  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: REQUEST_TIMEOUT,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    });

    this.setupInterceptors();
  }

  setupInterceptors() {
    // Request interceptor for auth tokens
    this.client.interceptors.request.use(
      (config) => {
        const token = this.getAuthToken();
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        
        // Add request ID for tracing
        config.headers['X-Request-ID'] = this.generateRequestId();
        
        console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
        return config;
      },
      (error) => {
        console.error('Request interceptor error:', error);
        return Promise.reject(error);
      }
    );

    // Response interceptor for error handling
    this.client.interceptors.response.use(
      (response) => {
        console.log(`API Response: ${response.status} ${response.config.url}`);
        return response;
      },
      async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;
          
          try {
            await this.refreshToken();
            // Retry original request with new token
            const token = this.getAuthToken();
            if (token) {
              originalRequest.headers.Authorization = `Bearer ${token}`;
            }
            return this.client(originalRequest);
          } catch (refreshError) {
            this.handleAuthenticationError();
            return Promise.reject(refreshError);
          }
        }

        return Promise.reject(this.handleError(error));
      }
    );
  }

  async get(endpoint, params = {}, options = {}) {
    try {
      const response = await this.client.get(endpoint, { 
        params, 
        ...options 
      });
      return this.handleSuccess(response);
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async post(endpoint, data = {}, options = {}) {
    try {
      const response = await this.client.post(endpoint, data, options);
      return this.handleSuccess(response);
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async put(endpoint, data = {}, options = {}) {
    try {
      const response = await this.client.put(endpoint, data, options);
      return this.handleSuccess(response);
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async delete(endpoint, options = {}) {
    try {
      const response = await this.client.delete(endpoint, options);
      return this.handleSuccess(response);
    } catch (error) {
      throw this.handleError(error);
    }
  }

  handleSuccess(response) {
    return {
      data: response.data,
      status: response.status,
      headers: response.headers,
      success: true
    };
  }

  handleError(error) {
    console.error('API Error:', error);

    if (error.response) {
      // Server responded with error status
      return {
        error: error.response.data?.error || 'SERVER_ERROR',
        message: error.response.data?.message || 'An error occurred on the server',
        details: error.response.data?.details,
        status: error.response.status,
        success: false
      };
    } else if (error.request) {
      // Network error
      return {
        error: 'NETWORK_ERROR',
        message: 'Network error - please check your connection',
        status: 0,
        success: false
      };
    } else {
      // Other error
      return {
        error: 'CLIENT_ERROR',
        message: error.message || 'An unexpected error occurred',
        success: false
      };
    }
  }

  async refreshToken() {
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) {
      throw new Error('No refresh token available');
    }

    try {
      const response = await axios.post(`${API_BASE_URL}/auth/refresh`, {
        refreshToken: refreshToken
      });

      const { accessToken, refreshToken: newRefreshToken } = response.data;
      localStorage.setItem('access_token', accessToken);
      localStorage.setItem('refresh_token', newRefreshToken);

      return accessToken;
    } catch (error) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      throw error;
    }
  }

  getAuthToken() {
    return localStorage.getItem('access_token');
  }

  handleAuthenticationError() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    
    // Redirect to login page
    window.location.href = '/login';
  }

  generateRequestId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
  }

  // File upload with progress
  async uploadFile(endpoint, file, onProgress = null) {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await this.client.post(endpoint, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        onUploadProgress: (progressEvent) => {
          if (onProgress) {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            onProgress(percentCompleted);
          }
        }
      });
      return this.handleSuccess(response);
    } catch (error) {
      throw this.handleError(error);
    }
  }
}

export default new ApiService();
```

## Quality Gates

### ✅ Integration Compliance
- [ ] Frontend-backend integration matches CLAUDE.md technology specification
- [ ] API communication patterns properly implemented
- [ ] Authentication and authorization working correctly
- [ ] Error handling comprehensive and user-friendly

### ✅ Security & Performance
- [ ] CORS configuration appropriate for deployment environment
- [ ] Token refresh mechanism implemented correctly
- [ ] Request/response interceptors handle errors gracefully
- [ ] API endpoints follow RESTful principles

### ✅ User Experience
- [ ] Loading states handled appropriately
- [ ] Error messages user-friendly and actionable
- [ ] Offline/network error handling implemented
- [ ] Authentication state management reliable

**This prompt ensures seamless integration between frontend and backend technologies specified in CLAUDE.md, providing robust communication, proper authentication, and excellent error handling.**