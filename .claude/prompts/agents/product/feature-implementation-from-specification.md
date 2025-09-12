# Feature Implementation from Specification Document

## Mission
Implement complete application features based on detailed specification documents, coordinating across frontend, backend, and data layers to deliver production-ready functionality that meets all business requirements, user experience standards, and technical specifications.

## Process

### Phase 1: Specification Analysis and Requirements Extraction

#### 1.1 Document Analysis and Parsing
```bash
# Analyze specification document structure
file specification.md specification.docx specification.pdf
head -50 specification.md
grep -i "requirement\|feature\|user.*story\|acceptance.*criteria" specification.md
```

**Key Analysis Areas:**
- **Business Requirements:** Core functionality and business rules
- **User Stories:** User personas, scenarios, and acceptance criteria
- **Technical Requirements:** Performance, security, and integration needs
- **UI/UX Specifications:** Design requirements and user experience flows
- **Data Requirements:** Data models, storage, and processing needs

#### 1.2 Feature Decomposition Matrix
```markdown
# Feature Analysis Template

## 1. Feature Overview
- **Feature Name:** [Extract from specification]
- **Business Value:** [Why this feature is needed]
- **Target Users:** [Who will use this feature]
- **Priority:** [High/Medium/Low]
- **Dependencies:** [Other features or systems required]

## 2. Functional Requirements
### User Stories
- As a [user type], I want [functionality] so that [benefit]
- As a [user type], I want [functionality] so that [benefit]

### Acceptance Criteria
- [ ] Given [precondition], when [action], then [expected result]
- [ ] Given [precondition], when [action], then [expected result]

### Business Rules
- [Rule 1]: [Description and implementation requirements]
- [Rule 2]: [Description and implementation requirements]

## 3. Technical Requirements
### Frontend Requirements
- **UI Components:** [List of required components]
- **User Interactions:** [Forms, buttons, navigation]
- **Responsive Design:** [Mobile, tablet, desktop requirements]
- **Accessibility:** [WCAG compliance requirements]

### Backend Requirements
- **API Endpoints:** [List of required endpoints with methods]
- **Business Logic:** [Services and calculations needed]
- **Data Validation:** [Input validation and business rules]
- **Security:** [Authentication, authorization, data protection]

### Data Requirements
- **Database Changes:** [New tables, columns, relationships]
- **Data Migration:** [Existing data handling]
- **Storage Requirements:** [File storage, caching needs]
- **Performance:** [Query optimization, indexing]

## 4. Integration Requirements
- **External APIs:** [Third-party integrations]
- **Internal Services:** [Microservice communications]
- **Event Handling:** [Real-time updates, notifications]
- **Reporting:** [Analytics and reporting needs]
```

### Phase 2: Architecture Planning and Design

#### 2.1 Multi-Layer Architecture Design
```typescript
// architecture-plan.ts - Feature architecture overview
interface FeatureArchitecture {
  feature: {
    name: string;
    description: string;
    components: {
      frontend: FrontendComponent[];
      backend: BackendComponent[];
      database: DatabaseComponent[];
      integration: IntegrationComponent[];
    };
  };
}

interface FrontendComponent {
  name: string;
  type: 'component' | 'service' | 'guard' | 'interceptor' | 'pipe';
  path: string;
  dependencies: string[];
  interfaces: string[];
}

interface BackendComponent {
  name: string;
  type: 'controller' | 'service' | 'repository' | 'middleware' | 'validator';
  path: string;
  endpoints?: ApiEndpoint[];
  dependencies: string[];
}

interface DatabaseComponent {
  name: string;
  type: 'table' | 'view' | 'procedure' | 'function' | 'index';
  sql: string;
  relationships: string[];
}

interface IntegrationComponent {
  name: string;
  type: 'external-api' | 'webhook' | 'event' | 'queue' | 'notification';
  configuration: Record<string, any>;
}

// Example: User Profile Management Feature
const userProfileFeature: FeatureArchitecture = {
  feature: {
    name: "User Profile Management",
    description: "Allow users to view and edit their profile information",
    components: {
      frontend: [
        {
          name: "UserProfileComponent",
          type: "component",
          path: "src/app/features/user-profile/user-profile.component.ts",
          dependencies: ["UserProfileService", "UserValidationService"],
          interfaces: ["OnInit", "OnDestroy"]
        },
        {
          name: "UserProfileService",
          type: "service",
          path: "src/app/features/user-profile/services/user-profile.service.ts",
          dependencies: ["HttpClient", "AuthService"],
          interfaces: []
        }
      ],
      backend: [
        {
          name: "UserProfileController",
          type: "controller",
          path: "Controllers/UserProfileController.cs",
          endpoints: [
            { method: "GET", path: "/api/users/{id}/profile", action: "GetProfile" },
            { method: "PUT", path: "/api/users/{id}/profile", action: "UpdateProfile" },
            { method: "POST", path: "/api/users/{id}/profile/avatar", action: "UploadAvatar" }
          ],
          dependencies: ["IUserProfileService", "IMapper"]
        },
        {
          name: "UserProfileService",
          type: "service",
          path: "Services/UserProfileService.cs",
          dependencies: ["IUserRepository", "IFileStorage"],
          endpoints: []
        }
      ],
      database: [
        {
          name: "UserProfiles",
          type: "table",
          sql: "CREATE TABLE UserProfiles (...)",
          relationships: ["Users", "ProfileImages"]
        }
      ],
      integration: [
        {
          name: "ImageOptimization",
          type: "external-api",
          configuration: {
            service: "AWS S3 + CloudFront",
            purpose: "Avatar image optimization and delivery"
          }
        }
      ]
    }
  }
};
```

#### 2.2 Implementation Task Breakdown
```markdown
# Implementation Tasks

## Frontend Tasks (Frontend Engineer)
### 1. Component Development
- [ ] Create UserProfileComponent with form handling
- [ ] Implement avatar upload with preview
- [ ] Add validation with real-time feedback
- [ ] Create responsive design for mobile/desktop
- [ ] Implement loading states and error handling

### 2. Service Integration
- [ ] Create UserProfileService with HTTP operations
- [ ] Implement caching for profile data
- [ ] Add offline support with local storage
- [ ] Create validation service for profile rules
- [ ] Implement image compression for uploads

### 3. User Experience
- [ ] Add progress indicators for uploads
- [ ] Implement undo/redo functionality
- [ ] Create confirmation dialogs for destructive actions
- [ ] Add keyboard navigation support
- [ ] Implement accessibility features (ARIA labels, screen reader support)

## Backend Tasks (API Engineer)
### 1. API Development
- [ ] Create UserProfileController with CRUD operations
- [ ] Implement file upload handling with validation
- [ ] Add business logic for profile updates
- [ ] Create audit logging for profile changes
- [ ] Implement rate limiting for uploads

### 2. Business Logic
- [ ] Create profile validation service
- [ ] Implement image processing pipeline
- [ ] Add duplicate detection for avatars
- [ ] Create profile completeness scoring
- [ ] Implement privacy controls

### 3. Security & Performance
- [ ] Add input sanitization and validation
- [ ] Implement file type and size restrictions
- [ ] Create secure file storage with CDN
- [ ] Add SQL injection prevention
- [ ] Implement caching strategies

## Database Tasks (Data Engineer)
### 1. Schema Changes
- [ ] Create UserProfiles table with proper indexes
- [ ] Add foreign key relationships
- [ ] Create audit tables for profile changes
- [ ] Add database constraints and triggers
- [ ] Create backup and recovery procedures

### 2. Data Migration
- [ ] Migrate existing profile data
- [ ] Create data validation procedures
- [ ] Implement rollback procedures
- [ ] Add performance monitoring
- [ ] Create data archiving strategy
```

### Phase 3: Coordinated Implementation

#### 3.1 Frontend Implementation (Angular)
```typescript
// user-profile.component.ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Subject, takeUntil, debounceTime, distinctUntilChanged } from 'rxjs';
import { UserProfileService } from './services/user-profile.service';
import { UserProfile, UpdateProfileRequest } from './models/user-profile.models';
import { NotificationService } from '../shared/services/notification.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit, OnDestroy {
  profileForm: FormGroup;
  profile: UserProfile | null = null;
  loading = false;
  saving = false;
  uploadingAvatar = false;
  
  avatarPreview: string | null = null;
  selectedAvatarFile: File | null = null;
  
  private destroy$ = new Subject<void>();

  constructor(
    private fb: FormBuilder,
    private userProfileService: UserProfileService,
    private notificationService: NotificationService
  ) {
    this.profileForm = this.createForm();
  }

  ngOnInit(): void {
    this.loadProfile();
    this.setupFormValidation();
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  private createForm(): FormGroup {
    return this.fb.group({
      firstName: ['', [Validators.required, Validators.maxLength(50)]],
      lastName: ['', [Validators.required, Validators.maxLength(50)]],
      email: ['', [Validators.required, Validators.email]],
      bio: ['', [Validators.maxLength(500)]],
      location: ['', [Validators.maxLength(100)]],
      website: ['', [Validators.pattern(/^https?:\/\/.+/)]],
      socialMedia: this.fb.group({
        twitter: ['', [Validators.pattern(/^@?[\w]+$/)]],
        linkedin: ['', [Validators.pattern(/^[\w-]+$/)]],
        github: ['', [Validators.pattern(/^[\w-]+$/)]]
      }),
      privacy: this.fb.group({
        showEmail: [false],
        showLocation: [false],
        allowMessages: [true]
      })
    });
  }

  private setupFormValidation(): void {
    // Real-time validation feedback
    this.profileForm.valueChanges
      .pipe(
        debounceTime(300),
        distinctUntilChanged(),
        takeUntil(this.destroy$)
      )
      .subscribe(() => {
        this.validateForm();
      });
  }

  private validateForm(): void {
    // Custom validation logic
    const bioControl = this.profileForm.get('bio');
    if (bioControl?.value?.length > 450) {
      // Warning at 450 characters, error at 500
      bioControl.setErrors({ ...bioControl.errors, warning: true });
    }
  }

  async loadProfile(): Promise<void> {
    this.loading = true;
    
    try {
      this.profile = await this.userProfileService.getCurrentUserProfile();
      this.populateForm(this.profile);
    } catch (error) {
      this.notificationService.showError('Failed to load profile');
      console.error('Error loading profile:', error);
    } finally {
      this.loading = false;
    }
  }

  private populateForm(profile: UserProfile): void {
    this.profileForm.patchValue({
      firstName: profile.firstName,
      lastName: profile.lastName,
      email: profile.email,
      bio: profile.bio,
      location: profile.location,
      website: profile.website,
      socialMedia: {
        twitter: profile.socialMedia?.twitter || '',
        linkedin: profile.socialMedia?.linkedin || '',
        github: profile.socialMedia?.github || ''
      },
      privacy: {
        showEmail: profile.privacy?.showEmail || false,
        showLocation: profile.privacy?.showLocation || false,
        allowMessages: profile.privacy?.allowMessages || true
      }
    });

    if (profile.avatar) {
      this.avatarPreview = profile.avatar;
    }
  }

  async onSubmit(): Promise<void> {
    if (this.profileForm.invalid) {
      this.markFormGroupTouched();
      return;
    }

    this.saving = true;

    try {
      const updateRequest: UpdateProfileRequest = {
        ...this.profileForm.value,
        id: this.profile?.id
      };

      const updatedProfile = await this.userProfileService.updateProfile(updateRequest);
      this.profile = updatedProfile;
      this.notificationService.showSuccess('Profile updated successfully');
      
      // Reset form pristine state
      this.profileForm.markAsPristine();
    } catch (error) {
      this.notificationService.showError('Failed to update profile');
      console.error('Error updating profile:', error);
    } finally {
      this.saving = false;
    }
  }

  onAvatarSelected(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) return;

    // Validate file
    if (!this.isValidImageFile(file)) {
      this.notificationService.showError('Please select a valid image file (JPG, PNG, GIF)');
      return;
    }

    if (file.size > 5 * 1024 * 1024) { // 5MB limit
      this.notificationService.showError('Image file size must be less than 5MB');
      return;
    }

    this.selectedAvatarFile = file;
    
    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
      this.avatarPreview = e.target?.result as string;
    };
    reader.readAsDataURL(file);
  }

  async uploadAvatar(): Promise<void> {
    if (!this.selectedAvatarFile || !this.profile) return;

    this.uploadingAvatar = true;

    try {
      const avatarUrl = await this.userProfileService.uploadAvatar(
        this.profile.id, 
        this.selectedAvatarFile
      );
      
      this.profile.avatar = avatarUrl;
      this.avatarPreview = avatarUrl;
      this.selectedAvatarFile = null;
      
      this.notificationService.showSuccess('Avatar updated successfully');
    } catch (error) {
      this.notificationService.showError('Failed to upload avatar');
      console.error('Error uploading avatar:', error);
    } finally {
      this.uploadingAvatar = false;
    }
  }

  removeAvatar(): void {
    // Show confirmation dialog
    if (confirm('Are you sure you want to remove your avatar?')) {
      this.avatarPreview = null;
      this.selectedAvatarFile = null;
      // Call API to remove avatar
      this.userProfileService.removeAvatar(this.profile!.id)
        .then(() => {
          this.profile!.avatar = null;
          this.notificationService.showSuccess('Avatar removed successfully');
        })
        .catch(() => {
          this.notificationService.showError('Failed to remove avatar');
        });
    }
  }

  private isValidImageFile(file: File): boolean {
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
    return allowedTypes.includes(file.type);
  }

  private markFormGroupTouched(): void {
    Object.keys(this.profileForm.controls).forEach(key => {
      const control = this.profileForm.get(key);
      control?.markAsTouched();

      if (control instanceof FormGroup) {
        this.markNestedFormGroupTouched(control);
      }
    });
  }

  private markNestedFormGroupTouched(formGroup: FormGroup): void {
    Object.keys(formGroup.controls).forEach(key => {
      const control = formGroup.get(key);
      control?.markAsTouched();
    });
  }

  // Getters for template
  get hasUnsavedChanges(): boolean {
    return this.profileForm.dirty && !this.saving;
  }

  get profileCompleteness(): number {
    if (!this.profile) return 0;
    
    const fields = [
      this.profile.firstName,
      this.profile.lastName,
      this.profile.bio,
      this.profile.location,
      this.profile.avatar
    ];
    
    const completedFields = fields.filter(field => field && field.trim().length > 0).length;
    return Math.round((completedFields / fields.length) * 100);
  }
}
```

#### 3.2 Backend Implementation (ASP.NET Core)
```csharp
// Controllers/UserProfileController.cs
[ApiController]
[Route("api/users/{userId}/profile")]
[Authorize]
[ProducesResponseType(typeof(ErrorResponse), 500)]
public class UserProfileController : ControllerBase
{
    private readonly IUserProfileService _userProfileService;
    private readonly IMapper _mapper;
    private readonly ILogger<UserProfileController> _logger;
    private readonly IFileStorageService _fileStorageService;

    public UserProfileController(
        IUserProfileService userProfileService,
        IMapper mapper,
        ILogger<UserProfileController> logger,
        IFileStorageService fileStorageService)
    {
        _userProfileService = userProfileService;
        _mapper = mapper;
        _logger = logger;
        _fileStorageService = fileStorageService;
    }

    [HttpGet]
    [ProducesResponseType(typeof(UserProfileResponse), 200)]
    [ProducesResponseType(typeof(ErrorResponse), 404)]
    public async Task<ActionResult<UserProfileResponse>> GetProfile(
        long userId,
        CancellationToken cancellationToken = default)
    {
        try
        {
            // Authorization check
            var currentUserId = GetCurrentUserId();
            if (!await CanAccessProfile(currentUserId, userId))
            {
                return Forbid();
            }

            var profile = await _userProfileService.GetProfileAsync(userId, cancellationToken);
            if (profile == null)
            {
                return NotFound(CreateErrorResponse("NOT_FOUND", "Profile not found"));
            }

            var response = _mapper.Map<UserProfileResponse>(profile);
            return Ok(response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error retrieving profile for user {UserId}", userId);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    [HttpPut]
    [ProducesResponseType(typeof(UserProfileResponse), 200)]
    [ProducesResponseType(typeof(ErrorResponse), 400)]
    [ProducesResponseType(typeof(ErrorResponse), 404)]
    public async Task<ActionResult<UserProfileResponse>> UpdateProfile(
        long userId,
        [FromBody] UpdateUserProfileRequest request,
        CancellationToken cancellationToken = default)
    {
        try
        {
            // Authorization check
            var currentUserId = GetCurrentUserId();
            if (currentUserId != userId && !await IsAdmin(currentUserId))
            {
                return Forbid();
            }

            // Validation
            if (!ModelState.IsValid)
            {
                return BadRequest(CreateValidationErrorResponse());
            }

            // Business validation
            var existingProfile = await _userProfileService.GetProfileAsync(userId, cancellationToken);
            if (existingProfile == null)
            {
                return NotFound(CreateErrorResponse("NOT_FOUND", "Profile not found"));
            }

            // Email uniqueness check (if email is being changed)
            if (!string.Equals(existingProfile.Email, request.Email, StringComparison.OrdinalIgnoreCase))
            {
                if (await _userProfileService.EmailExistsAsync(request.Email, userId, cancellationToken))
                {
                    return BadRequest(CreateErrorResponse("EMAIL_EXISTS", "Email address is already in use"));
                }
            }

            // Update profile
            var updateData = _mapper.Map<UserProfile>(request);
            updateData.Id = userId;
            updateData.UpdatedAt = DateTime.UtcNow;
            updateData.UpdatedBy = currentUserId;

            var updatedProfile = await _userProfileService.UpdateProfileAsync(updateData, cancellationToken);
            var response = _mapper.Map<UserProfileResponse>(updatedProfile);

            _logger.LogInformation("Profile updated for user {UserId}", userId);
            return Ok(response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error updating profile for user {UserId}", userId);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    [HttpPost("avatar")]
    [ProducesResponseType(typeof(UserProfileResponse), 200)]
    [ProducesResponseType(typeof(ErrorResponse), 400)]
    [RequestSizeLimit(5 * 1024 * 1024)] // 5MB limit
    public async Task<ActionResult<UserProfileResponse>> UploadAvatar(
        long userId,
        IFormFile avatar,
        CancellationToken cancellationToken = default)
    {
        try
        {
            // Authorization check
            var currentUserId = GetCurrentUserId();
            if (currentUserId != userId && !await IsAdmin(currentUserId))
            {
                return Forbid();
            }

            // Validate file
            if (avatar == null || avatar.Length == 0)
            {
                return BadRequest(CreateErrorResponse("INVALID_FILE", "No file provided"));
            }

            if (!IsValidImageFile(avatar))
            {
                return BadRequest(CreateErrorResponse("INVALID_FILE_TYPE", "Only JPG, PNG, GIF, and WebP files are allowed"));
            }

            if (avatar.Length > 5 * 1024 * 1024) // 5MB
            {
                return BadRequest(CreateErrorResponse("FILE_TOO_LARGE", "File size must be less than 5MB"));
            }

            // Upload and process avatar
            var avatarUrl = await _userProfileService.UploadAvatarAsync(userId, avatar, cancellationToken);
            
            // Get updated profile
            var profile = await _userProfileService.GetProfileAsync(userId, cancellationToken);
            var response = _mapper.Map<UserProfileResponse>(profile);

            _logger.LogInformation("Avatar uploaded for user {UserId}", userId);
            return Ok(response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error uploading avatar for user {UserId}", userId);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    [HttpDelete("avatar")]
    [ProducesResponseType(typeof(UserProfileResponse), 200)]
    public async Task<ActionResult<UserProfileResponse>> RemoveAvatar(
        long userId,
        CancellationToken cancellationToken = default)
    {
        try
        {
            // Authorization check
            var currentUserId = GetCurrentUserId();
            if (currentUserId != userId && !await IsAdmin(currentUserId))
            {
                return Forbid();
            }

            await _userProfileService.RemoveAvatarAsync(userId, cancellationToken);
            
            var profile = await _userProfileService.GetProfileAsync(userId, cancellationToken);
            var response = _mapper.Map<UserProfileResponse>(profile);

            _logger.LogInformation("Avatar removed for user {UserId}", userId);
            return Ok(response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error removing avatar for user {UserId}", userId);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    [HttpGet("completeness")]
    [ProducesResponseType(typeof(ProfileCompletenessResponse), 200)]
    public async Task<ActionResult<ProfileCompletenessResponse>> GetProfileCompleteness(
        long userId,
        CancellationToken cancellationToken = default)
    {
        try
        {
            var currentUserId = GetCurrentUserId();
            if (!await CanAccessProfile(currentUserId, userId))
            {
                return Forbid();
            }

            var completeness = await _userProfileService.GetProfileCompletenessAsync(userId, cancellationToken);
            return Ok(completeness);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error calculating profile completeness for user {UserId}", userId);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    // Helper methods
    private long GetCurrentUserId()
    {
        var userIdClaim = HttpContext.User.FindFirst("sub")?.Value;
        return long.TryParse(userIdClaim, out var userId) ? userId : 0;
    }

    private async Task<bool> CanAccessProfile(long currentUserId, long targetUserId)
    {
        if (currentUserId == targetUserId)
            return true;

        return await IsAdmin(currentUserId);
    }

    private async Task<bool> IsAdmin(long userId)
    {
        // Implementation for admin check
        return false; // Placeholder
    }

    private bool IsValidImageFile(IFormFile file)
    {
        var allowedTypes = new[] { "image/jpeg", "image/png", "image/gif", "image/webp" };
        return allowedTypes.Contains(file.ContentType.ToLower());
    }

    private ErrorResponse CreateErrorResponse(string error, string message)
    {
        return new ErrorResponse
        {
            Error = error,
            Message = message,
            Timestamp = DateTime.UtcNow,
            RequestId = HttpContext.TraceIdentifier
        };
    }

    private ErrorResponse CreateValidationErrorResponse()
    {
        var errors = ModelState
            .Where(x => x.Value.Errors.Count > 0)
            .Select(x => new ValidationError
            {
                Field = x.Key,
                Message = x.Value.Errors.First().ErrorMessage,
                Code = "VALIDATION_ERROR"
            })
            .ToArray();

        return new ErrorResponse
        {
            Error = "VALIDATION_ERROR",
            Message = "Request validation failed",
            Details = errors,
            Timestamp = DateTime.UtcNow,
            RequestId = HttpContext.TraceIdentifier
        };
    }
}
```

#### 3.3 Service Layer Implementation
```csharp
// Services/UserProfileService.cs
public interface IUserProfileService
{
    Task<UserProfile?> GetProfileAsync(long userId, CancellationToken cancellationToken = default);
    Task<UserProfile> UpdateProfileAsync(UserProfile profile, CancellationToken cancellationToken = default);
    Task<string> UploadAvatarAsync(long userId, IFormFile file, CancellationToken cancellationToken = default);
    Task RemoveAvatarAsync(long userId, CancellationToken cancellationToken = default);
    Task<bool> EmailExistsAsync(string email, long? excludeUserId = null, CancellationToken cancellationToken = default);
    Task<ProfileCompletenessResponse> GetProfileCompletenessAsync(long userId, CancellationToken cancellationToken = default);
}

public class UserProfileService : IUserProfileService
{
    private readonly IUserRepository _userRepository;
    private readonly IFileStorageService _fileStorageService;
    private readonly IImageProcessingService _imageProcessingService;
    private readonly ICacheService _cacheService;
    private readonly ILogger<UserProfileService> _logger;

    public UserProfileService(
        IUserRepository userRepository,
        IFileStorageService fileStorageService,
        IImageProcessingService imageProcessingService,
        ICacheService cacheService,
        ILogger<UserProfileService> logger)
    {
        _userRepository = userRepository;
        _fileStorageService = fileStorageService;
        _imageProcessingService = imageProcessingService;
        _cacheService = cacheService;
        _logger = logger;
    }

    public async Task<UserProfile?> GetProfileAsync(long userId, CancellationToken cancellationToken = default)
    {
        var cacheKey = $"user_profile_{userId}";
        
        // Try cache first
        var cachedProfile = await _cacheService.GetAsync<UserProfile>(cacheKey);
        if (cachedProfile != null)
        {
            return cachedProfile;
        }

        // Get from database
        var user = await _userRepository.GetByIdAsync(userId, cancellationToken);
        if (user == null)
        {
            return null;
        }

        var profile = MapUserToProfile(user);
        
        // Cache for 30 minutes
        await _cacheService.SetAsync(cacheKey, profile, TimeSpan.FromMinutes(30));
        
        return profile;
    }

    public async Task<UserProfile> UpdateProfileAsync(UserProfile profile, CancellationToken cancellationToken = default)
    {
        var user = await _userRepository.GetByIdAsync(profile.Id, cancellationToken);
        if (user == null)
        {
            throw new NotFoundException("User not found");
        }

        // Update user entity
        MapProfileToUser(profile, user);
        
        _userRepository.Update(user);
        await _userRepository.SaveChangesAsync(cancellationToken);

        // Update cache
        var cacheKey = $"user_profile_{profile.Id}";
        await _cacheService.RemoveAsync(cacheKey);
        await _cacheService.SetAsync(cacheKey, profile, TimeSpan.FromMinutes(30));

        _logger.LogInformation("Profile updated for user {UserId}", profile.Id);
        
        return profile;
    }

    public async Task<string> UploadAvatarAsync(long userId, IFormFile file, CancellationToken cancellationToken = default)
    {
        var user = await _userRepository.GetByIdAsync(userId, cancellationToken);
        if (user == null)
        {
            throw new NotFoundException("User not found");
        }

        try
        {
            // Process image (resize, optimize)
            using var processedImage = await _imageProcessingService.ProcessAvatarAsync(file, cancellationToken);
            
            // Generate unique filename
            var fileName = $"avatars/{userId}/{Guid.NewGuid()}.jpg";
            
            // Upload to storage
            var avatarUrl = await _fileStorageService.UploadAsync(fileName, processedImage, "image/jpeg", cancellationToken);
            
            // Delete old avatar if exists
            if (!string.IsNullOrEmpty(user.Avatar))
            {
                await _fileStorageService.DeleteAsync(ExtractFileNameFromUrl(user.Avatar), cancellationToken);
            }

            // Update user record
            user.Avatar = avatarUrl;
            user.UpdatedAt = DateTime.UtcNow;
            
            _userRepository.Update(user);
            await _userRepository.SaveChangesAsync(cancellationToken);

            // Clear cache
            var cacheKey = $"user_profile_{userId}";
            await _cacheService.RemoveAsync(cacheKey);

            _logger.LogInformation("Avatar uploaded for user {UserId}: {AvatarUrl}", userId, avatarUrl);
            
            return avatarUrl;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error uploading avatar for user {UserId}", userId);
            throw;
        }
    }

    public async Task RemoveAvatarAsync(long userId, CancellationToken cancellationToken = default)
    {
        var user = await _userRepository.GetByIdAsync(userId, cancellationToken);
        if (user == null)
        {
            throw new NotFoundException("User not found");
        }

        if (!string.IsNullOrEmpty(user.Avatar))
        {
            // Delete from storage
            await _fileStorageService.DeleteAsync(ExtractFileNameFromUrl(user.Avatar), cancellationToken);
            
            // Update user record
            user.Avatar = null;
            user.UpdatedAt = DateTime.UtcNow;
            
            _userRepository.Update(user);
            await _userRepository.SaveChangesAsync(cancellationToken);

            // Clear cache
            var cacheKey = $"user_profile_{userId}";
            await _cacheService.RemoveAsync(cacheKey);

            _logger.LogInformation("Avatar removed for user {UserId}", userId);
        }
    }

    public async Task<bool> EmailExistsAsync(string email, long? excludeUserId = null, CancellationToken cancellationToken = default)
    {
        return await _userRepository.EmailExistsAsync(email, excludeUserId, cancellationToken);
    }

    public async Task<ProfileCompletenessResponse> GetProfileCompletenessAsync(long userId, CancellationToken cancellationToken = default)
    {
        var profile = await GetProfileAsync(userId, cancellationToken);
        if (profile == null)
        {
            throw new NotFoundException("Profile not found");
        }

        var completeness = CalculateProfileCompleteness(profile);
        
        return new ProfileCompletenessResponse
        {
            UserId = userId,
            CompletenessPercentage = completeness.Percentage,
            CompletedFields = completeness.CompletedFields,
            MissingFields = completeness.MissingFields,
            Suggestions = completeness.Suggestions
        };
    }

    private ProfileCompletenessInfo CalculateProfileCompleteness(UserProfile profile)
    {
        var fields = new Dictionary<string, bool>
        {
            { "FirstName", !string.IsNullOrWhiteSpace(profile.FirstName) },
            { "LastName", !string.IsNullOrWhiteSpace(profile.LastName) },
            { "Bio", !string.IsNullOrWhiteSpace(profile.Bio) },
            { "Location", !string.IsNullOrWhiteSpace(profile.Location) },
            { "Avatar", !string.IsNullOrWhiteSpace(profile.Avatar) },
            { "Website", !string.IsNullOrWhiteSpace(profile.Website) },
            { "Social Media", profile.SocialMedia != null && (
                !string.IsNullOrWhiteSpace(profile.SocialMedia.Twitter) ||
                !string.IsNullOrWhiteSpace(profile.SocialMedia.LinkedIn) ||
                !string.IsNullOrWhiteSpace(profile.SocialMedia.GitHub)
            )}
        };

        var completedFields = fields.Where(f => f.Value).Select(f => f.Key).ToList();
        var missingFields = fields.Where(f => !f.Value).Select(f => f.Key).ToList();
        var percentage = (int)Math.Round((double)completedFields.Count / fields.Count * 100);

        var suggestions = GenerateCompletionSuggestions(missingFields);

        return new ProfileCompletenessInfo
        {
            Percentage = percentage,
            CompletedFields = completedFields,
            MissingFields = missingFields,
            Suggestions = suggestions
        };
    }

    private List<string> GenerateCompletionSuggestions(List<string> missingFields)
    {
        var suggestions = new List<string>();

        if (missingFields.Contains("Avatar"))
            suggestions.Add("Add a profile picture to help others recognize you");

        if (missingFields.Contains("Bio"))
            suggestions.Add("Write a short bio to tell others about yourself");

        if (missingFields.Contains("Location"))
            suggestions.Add("Add your location to connect with nearby professionals");

        if (missingFields.Contains("Website"))
            suggestions.Add("Share your website or portfolio to showcase your work");

        if (missingFields.Contains("Social Media"))
            suggestions.Add("Connect your social media profiles to expand your network");

        return suggestions;
    }

    // Helper methods for mapping and utilities...
}
```

## Deliverables

### 1. Complete Feature Implementation
- **Frontend Components:** Angular components with full user interaction
- **Backend APIs:** RESTful endpoints with business logic
- **Database Integration:** Data persistence and retrieval
- **File Management:** Upload, processing, and storage handling

### 2. Business Logic Implementation
- **Validation Rules:** Client and server-side validation
- **Security Controls:** Authentication, authorization, input sanitization
- **Performance Optimization:** Caching, image processing, efficient queries
- **Error Handling:** Comprehensive error management and user feedback

### 3. User Experience Features
- **Responsive Design:** Mobile and desktop optimization
- **Accessibility:** WCAG compliance and keyboard navigation
- **Real-time Feedback:** Progress indicators and validation messages
- **Offline Support:** Local storage and sync capabilities

### 4. Production Readiness
- **Monitoring:** Logging and performance tracking
- **Testing:** Unit, integration, and end-to-end tests
- **Documentation:** API documentation and user guides
- **Deployment:** CI/CD pipeline integration

## Quality Gates

### ✅ Feature Completeness
- [ ] All specification requirements implemented
- [ ] User acceptance criteria met
- [ ] Business rules enforced correctly
- [ ] Error scenarios handled appropriately
- [ ] Performance requirements satisfied

### ✅ Code Quality
- [ ] Clean architecture and separation of concerns
- [ ] Proper error handling and logging
- [ ] Security best practices implemented
- [ ] Performance optimization applied
- [ ] Code coverage targets achieved

### ✅ User Experience
- [ ] Responsive design across devices
- [ ] Accessibility standards met
- [ ] User feedback and validation implemented
- [ ] Loading states and error messages
- [ ] Intuitive navigation and interaction

This prompt provides comprehensive guidance for implementing complete features from specification documents, ensuring coordination across all application layers and delivering production-ready functionality.