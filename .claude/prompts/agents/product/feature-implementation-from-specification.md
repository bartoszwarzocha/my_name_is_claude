# Feature Implementation from Specification Document

**Agent: product-manager**  
**Purpose: Implement complete features from specification documents with technology-adaptive patterns and coordinated development**

---

## Context Analysis

The product-manager will analyze the CLAUDE.md file to determine:
- **Technology Stack**: Frontend framework (React, Angular, Vue), backend framework (Java/Spring, .NET Core, Node.js, Python/FastAPI) for appropriate implementation patterns
- **Architecture Pattern**: Monolithic vs microservices, component organization, and layer separation strategies
- **Business Domain**: Industry-specific requirements, compliance needs (GDPR, HIPAA), and feature complexity patterns
- **Project Scale**: Development team size, feature complexity, and integration requirements for coordinated implementation
- **Development Stage**: MVP requirements, production readiness needs, and feature prioritization strategies

Based on this analysis, the product manager will select appropriate feature implementation patterns, coordinate development across teams, and ensure technology-specific best practices are followed.

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

## Technology-Adaptive Implementation

### React + TypeScript + Next.js

**Recommended Pattern:** Component-driven architecture with React hooks, TypeScript interfaces, and Next.js API routes

```tsx
// components/UserProfile/UserProfileForm.tsx
import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { UserProfileService } from '@/services/user-profile.service';
import { Button, Input, Textarea, Avatar, Progress, Alert } from '@/components/ui';
import { useToast } from '@/hooks/use-toast';
import { ImageUpload } from '@/components/ui/image-upload';

// Validation schema
const userProfileSchema = z.object({
  firstName: z.string().min(2, 'First name must be at least 2 characters').max(50),
  lastName: z.string().min(2, 'Last name must be at least 2 characters').max(50),
  email: z.string().email('Invalid email address'),
  bio: z.string().max(500, 'Bio must be less than 500 characters').optional(),
  location: z.string().max(100, 'Location must be less than 100 characters').optional(),
  website: z.string().url('Invalid website URL').optional().or(z.literal('')),
  socialMedia: z.object({
    twitter: z.string().regex(/^@?[\w]+$/, 'Invalid Twitter handle').optional().or(z.literal('')),
    linkedin: z.string().regex(/^[\w-]+$/, 'Invalid LinkedIn username').optional().or(z.literal('')),
    github: z.string().regex(/^[\w-]+$/, 'Invalid GitHub username').optional().or(z.literal(''))
  }),
  privacy: z.object({
    showEmail: z.boolean(),
    showLocation: z.boolean(),
    allowMessages: z.boolean()
  })
});

type UserProfileFormData = z.infer<typeof userProfileSchema>;

interface UserProfile extends UserProfileFormData {
  id: string;
  avatar?: string;
  createdAt: string;
  updatedAt: string;
}

interface UserProfileFormProps {
  userId: string;
}

export const UserProfileForm: React.FC<UserProfileFormProps> = ({ userId }) => {
  const [avatarFile, setAvatarFile] = useState<File | null>(null);
  const [avatarPreview, setAvatarPreview] = useState<string | null>(null);
  const { toast } = useToast();
  const queryClient = useQueryClient();

  // Form setup with React Hook Form and Zod validation
  const {
    register,
    handleSubmit,
    watch,
    setValue,
    reset,
    formState: { errors, isDirty, isSubmitting }
  } = useForm<UserProfileFormData>({
    resolver: zodResolver(userProfileSchema),
    defaultValues: {
      socialMedia: { twitter: '', linkedin: '', github: '' },
      privacy: { showEmail: false, showLocation: false, allowMessages: true }
    }
  });

  // Fetch user profile
  const { data: profile, isLoading, error } = useQuery({
    queryKey: ['userProfile', userId],
    queryFn: () => UserProfileService.getProfile(userId),
    onSuccess: (data) => {
      reset(data);
      setAvatarPreview(data.avatar || null);
    }
  });

  // Update profile mutation
  const updateProfileMutation = useMutation({
    mutationFn: (data: UserProfileFormData) => 
      UserProfileService.updateProfile(userId, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['userProfile', userId] });
      toast({ title: 'Success', description: 'Profile updated successfully' });
    },
    onError: (error: any) => {
      toast({
        title: 'Error',
        description: error?.message || 'Failed to update profile',
        variant: 'destructive'
      });
    }
  });

  // Upload avatar mutation
  const uploadAvatarMutation = useMutation({
    mutationFn: (file: File) => UserProfileService.uploadAvatar(userId, file),
    onSuccess: (avatarUrl) => {
      queryClient.invalidateQueries({ queryKey: ['userProfile', userId] });
      setAvatarPreview(avatarUrl);
      setAvatarFile(null);
      toast({ title: 'Success', description: 'Avatar uploaded successfully' });
    },
    onError: (error: any) => {
      toast({
        title: 'Error',
        description: error?.message || 'Failed to upload avatar',
        variant: 'destructive'
      });
    }
  });

  // Form submission handler
  const onSubmit: SubmitHandler<UserProfileFormData> = useCallback(
    async (data) => {
      await updateProfileMutation.mutateAsync(data);
    },
    [updateProfileMutation]
  );

  // Avatar upload handler
  const handleAvatarUpload = useCallback((file: File) => {
    // Validate file
    if (!file.type.match(/^image\/(jpeg|png|gif|webp)$/)) {
      toast({
        title: 'Error',
        description: 'Please select a valid image file (JPG, PNG, GIF, WebP)',
        variant: 'destructive'
      });
      return;
    }

    if (file.size > 5 * 1024 * 1024) { // 5MB limit
      toast({
        title: 'Error',
        description: 'Image file size must be less than 5MB',
        variant: 'destructive'
      });
      return;
    }

    setAvatarFile(file);
    
    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
      setAvatarPreview(e.target?.result as string);
    };
    reader.readAsDataURL(file);
  }, [toast]);

  // Upload avatar when file is selected
  useEffect(() => {
    if (avatarFile) {
      uploadAvatarMutation.mutate(avatarFile);
    }
  }, [avatarFile, uploadAvatarMutation]);

  // Calculate profile completeness
  const profileCompleteness = useMemo(() => {
    if (!profile) return 0;
    
    const fields = [
      profile.firstName,
      profile.lastName,
      profile.bio,
      profile.location,
      profile.avatar
    ];
    
    const completedFields = fields.filter(field => field && field.trim().length > 0).length;
    return Math.round((completedFields / fields.length) * 100);
  }, [profile]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (error) {
    return (
      <Alert variant="destructive">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load profile. Please try again.
        </AlertDescription>
      </Alert>
    );
  }

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      {/* Profile Completeness */}
      <div className="bg-card p-6 rounded-lg border">
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-lg font-semibold">Profile Completeness</h3>
          <span className="text-sm font-medium">{profileCompleteness}%</span>
        </div>
        <Progress value={profileCompleteness} className="w-full" />
        {profileCompleteness < 100 && (
          <p className="text-sm text-muted-foreground mt-2">
            Complete your profile to help others connect with you
          </p>
        )}
      </div>

      {/* Avatar Section */}
      <div className="bg-card p-6 rounded-lg border">
        <h3 className="text-lg font-semibold mb-4">Profile Picture</h3>
        <div className="flex items-center space-x-4">
          <Avatar className="h-20 w-20">
            {avatarPreview ? (
              <img src={avatarPreview} alt="Profile" className="object-cover" />
            ) : (
              <div className="bg-primary/10 flex items-center justify-center text-primary font-semibold text-lg">
                {profile?.firstName?.[0]}{profile?.lastName?.[0]}
              </div>
            )}
          </Avatar>
          <div className="flex-1">
            <ImageUpload
              onImageSelect={handleAvatarUpload}
              accept="image/jpeg,image/png,image/gif,image/webp"
              maxSize={5 * 1024 * 1024}
              className="w-full"
            >
              <Button variant="outline" disabled={uploadAvatarMutation.isPending}>
                {uploadAvatarMutation.isPending ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-current mr-2" />
                    Uploading...
                  </>
                ) : (
                  'Upload Photo'
                )}
              </Button>
            </ImageUpload>
            <p className="text-sm text-muted-foreground mt-1">
              JPG, PNG, GIF or WebP. Max size 5MB.
            </p>
          </div>
        </div>
      </div>

      {/* Profile Form */}
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div className="bg-card p-6 rounded-lg border space-y-4">
          <h3 className="text-lg font-semibold">Basic Information</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <Input
                {...register('firstName')}
                placeholder="First Name"
                error={errors.firstName?.message}
              />
            </div>
            <div>
              <Input
                {...register('lastName')}
                placeholder="Last Name"
                error={errors.lastName?.message}
              />
            </div>
          </div>
          
          <Input
            {...register('email')}
            type="email"
            placeholder="Email Address"
            error={errors.email?.message}
          />
          
          <Textarea
            {...register('bio')}
            placeholder="Tell us about yourself..."
            maxLength={500}
            error={errors.bio?.message}
            helperText={`${watch('bio')?.length || 0}/500 characters`}
          />
        </div>

        <div className="bg-card p-6 rounded-lg border space-y-4">
          <h3 className="text-lg font-semibold">Location & Links</h3>
          
          <Input
            {...register('location')}
            placeholder="Location"
            error={errors.location?.message}
          />
          
          <Input
            {...register('website')}
            placeholder="Website URL"
            error={errors.website?.message}
          />
        </div>

        <div className="bg-card p-6 rounded-lg border space-y-4">
          <h3 className="text-lg font-semibold">Social Media</h3>
          
          <Input
            {...register('socialMedia.twitter')}
            placeholder="Twitter handle (without @)"
            error={errors.socialMedia?.twitter?.message}
          />
          
          <Input
            {...register('socialMedia.linkedin')}
            placeholder="LinkedIn username"
            error={errors.socialMedia?.linkedin?.message}
          />
          
          <Input
            {...register('socialMedia.github')}
            placeholder="GitHub username"
            error={errors.socialMedia?.github?.message}
          />
        </div>

        <div className="bg-card p-6 rounded-lg border space-y-4">
          <h3 className="text-lg font-semibold">Privacy Settings</h3>
          
          <div className="space-y-3">
            <label className="flex items-center space-x-2">
              <input
                type="checkbox"
                {...register('privacy.showEmail')}
                className="rounded border-gray-300"
              />
              <span className="text-sm">Show email address on profile</span>
            </label>
            
            <label className="flex items-center space-x-2">
              <input
                type="checkbox"
                {...register('privacy.showLocation')}
                className="rounded border-gray-300"
              />
              <span className="text-sm">Show location on profile</span>
            </label>
            
            <label className="flex items-center space-x-2">
              <input
                type="checkbox"
                {...register('privacy.allowMessages')}
                className="rounded border-gray-300"
              />
              <span className="text-sm">Allow other users to send me messages</span>
            </label>
          </div>
        </div>

        <div className="flex justify-end space-x-3">
          <Button
            type="button"
            variant="outline"
            onClick={() => reset(profile)}
            disabled={!isDirty || isSubmitting}
          >
            Cancel
          </Button>
          <Button
            type="submit"
            disabled={!isDirty || isSubmitting}
          >
            {isSubmitting ? (
              <>
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-current mr-2" />
                Saving...
              </>
            ) : (
              'Save Changes'
            )}
          </Button>
        </div>
      </form>
    </div>
  );
};

// Service layer implementation
// services/user-profile.service.ts
class UserProfileServiceImpl {
  private readonly baseUrl = '/api/users';

  async getProfile(userId: string): Promise<UserProfile> {
    const response = await fetch(`${this.baseUrl}/${userId}/profile`, {
      headers: {
        'Authorization': `Bearer ${this.getAuthToken()}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error('Failed to fetch profile');
    }

    return response.json();
  }

  async updateProfile(userId: string, data: UserProfileFormData): Promise<UserProfile> {
    const response = await fetch(`${this.baseUrl}/${userId}/profile`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${this.getAuthToken()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Failed to update profile');
    }

    return response.json();
  }

  async uploadAvatar(userId: string, file: File): Promise<string> {
    const formData = new FormData();
    formData.append('avatar', file);

    const response = await fetch(`${this.baseUrl}/${userId}/profile/avatar`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.getAuthToken()}`
      },
      body: formData
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Failed to upload avatar');
    }

    const result = await response.json();
    return result.avatar;
  }

  private getAuthToken(): string {
    // Implementation depends on your auth system
    return localStorage.getItem('authToken') || '';
  }
}

export const UserProfileService = new UserProfileServiceImpl();

// API Routes (Next.js)
// pages/api/users/[userId]/profile.ts
import { NextApiRequest, NextApiResponse } from 'next';
import { getSession } from 'next-auth/react';
import { PrismaClient } from '@prisma/client';
import { z } from 'zod';

const prisma = new PrismaClient();

const updateProfileSchema = z.object({
  firstName: z.string().min(2).max(50),
  lastName: z.string().min(2).max(50),
  email: z.string().email(),
  bio: z.string().max(500).optional(),
  location: z.string().max(100).optional(),
  website: z.string().url().optional().or(z.literal('')),
  socialMedia: z.object({
    twitter: z.string().optional(),
    linkedin: z.string().optional(),
    github: z.string().optional()
  }),
  privacy: z.object({
    showEmail: z.boolean(),
    showLocation: z.boolean(),
    allowMessages: z.boolean()
  })
});

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const session = await getSession({ req });
  if (!session) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const { userId } = req.query;
  const currentUserId = session.user.id;

  // Authorization check
  if (currentUserId !== userId && !session.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  try {
    if (req.method === 'GET') {
      const profile = await prisma.user.findUnique({
        where: { id: userId as string },
        select: {
          id: true,
          firstName: true,
          lastName: true,
          email: true,
          bio: true,
          location: true,
          website: true,
          avatar: true,
          socialMedia: true,
          privacy: true,
          createdAt: true,
          updatedAt: true
        }
      });

      if (!profile) {
        return res.status(404).json({ error: 'Profile not found' });
      }

      return res.status(200).json(profile);
    }

    if (req.method === 'PUT') {
      // Validate request body
      const validation = updateProfileSchema.safeParse(req.body);
      if (!validation.success) {
        return res.status(400).json({
          error: 'Validation failed',
          details: validation.error.errors
        });
      }

      const data = validation.data;

      // Check if email is already taken (if changed)
      const existingProfile = await prisma.user.findUnique({
        where: { id: userId as string }
      });

      if (!existingProfile) {
        return res.status(404).json({ error: 'Profile not found' });
      }

      if (data.email !== existingProfile.email) {
        const emailExists = await prisma.user.findUnique({
          where: { email: data.email }
        });

        if (emailExists) {
          return res.status(400).json({ error: 'Email already in use' });
        }
      }

      // Update profile
      const updatedProfile = await prisma.user.update({
        where: { id: userId as string },
        data: {
          ...data,
          updatedAt: new Date()
        },
        select: {
          id: true,
          firstName: true,
          lastName: true,
          email: true,
          bio: true,
          location: true,
          website: true,
          avatar: true,
          socialMedia: true,
          privacy: true,
          createdAt: true,
          updatedAt: true
        }
      });

      return res.status(200).json(updatedProfile);
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch (error) {
    console.error('Profile API error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
```

### Angular + TypeScript + NestJS

**Recommended Pattern:** Component-based architecture with reactive forms, TypeScript decorators, and NestJS backend

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

### Node.js + NestJS + TypeORM

**Recommended Pattern:** Decorator-based architecture with DTOs, Guards, and Interceptors

```typescript
// user-profile.controller.ts
import {
  Controller,
  Get,
  Put,
  Post,
  Delete,
  Body,
  Param,
  UseGuards,
  UseInterceptors,
  UploadedFile,
  ParseIntPipe,
  HttpStatus,
  HttpException
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { ApiTags, ApiOperation, ApiResponse, ApiBearerAuth } from '@nestjs/swagger';
import { JwtAuthGuard } from '../auth/guards/jwt-auth.guard';
import { CurrentUser } from '../auth/decorators/current-user.decorator';
import { UserProfileService } from './user-profile.service';
import { UpdateUserProfileDto, UserProfileResponseDto } from './dto';
import { User } from '../auth/entities/user.entity';
import { ProfileOwnerGuard } from './guards/profile-owner.guard';
import { FileValidationPipe } from './pipes/file-validation.pipe';

@ApiTags('User Profile')
@Controller('api/users/:userId/profile')
@UseGuards(JwtAuthGuard)
@ApiBearerAuth()
export class UserProfileController {
  constructor(private readonly userProfileService: UserProfileService) {}

  @Get()
  @ApiOperation({ summary: 'Get user profile' })
  @ApiResponse({
    status: HttpStatus.OK,
    description: 'Profile retrieved successfully',
    type: UserProfileResponseDto
  })
  @UseGuards(ProfileOwnerGuard)
  async getProfile(
    @Param('userId', ParseIntPipe) userId: number
  ): Promise<UserProfileResponseDto> {
    const profile = await this.userProfileService.getProfile(userId);
    if (!profile) {
      throw new HttpException('Profile not found', HttpStatus.NOT_FOUND);
    }
    return profile;
  }

  @Put()
  @ApiOperation({ summary: 'Update user profile' })
  @ApiResponse({
    status: HttpStatus.OK,
    description: 'Profile updated successfully',
    type: UserProfileResponseDto
  })
  @UseGuards(ProfileOwnerGuard)
  async updateProfile(
    @Param('userId', ParseIntPipe) userId: number,
    @Body() updateProfileDto: UpdateUserProfileDto,
    @CurrentUser() currentUser: User
  ): Promise<UserProfileResponseDto> {
    return await this.userProfileService.updateProfile(
      userId,
      updateProfileDto,
      currentUser.id
    );
  }

  @Post('avatar')
  @ApiOperation({ summary: 'Upload profile avatar' })
  @UseInterceptors(FileInterceptor('avatar'))
  @UseGuards(ProfileOwnerGuard)
  async uploadAvatar(
    @Param('userId', ParseIntPipe) userId: number,
    @UploadedFile(FileValidationPipe) file: Express.Multer.File,
    @CurrentUser() currentUser: User
  ): Promise<{ avatarUrl: string }> {
    const avatarUrl = await this.userProfileService.uploadAvatar(
      userId,
      file,
      currentUser.id
    );
    return { avatarUrl };
  }

  @Delete('avatar')
  @ApiOperation({ summary: 'Remove profile avatar' })
  @UseGuards(ProfileOwnerGuard)
  async removeAvatar(
    @Param('userId', ParseIntPipe) userId: number,
    @CurrentUser() currentUser: User
  ): Promise<{ message: string }> {
    await this.userProfileService.removeAvatar(userId, currentUser.id);
    return { message: 'Avatar removed successfully' };
  }
}

// user-profile.service.ts
import { Injectable, HttpException, HttpStatus, Logger } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from '../auth/entities/user.entity';
import { UpdateUserProfileDto, UserProfileResponseDto } from './dto';
import { FileStorageService } from '../storage/file-storage.service';
import { ImageProcessingService } from '../media/image-processing.service';
import { CacheService } from '../cache/cache.service';

@Injectable()
export class UserProfileService {
  private readonly logger = new Logger(UserProfileService.name);

  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
    private readonly fileStorageService: FileStorageService,
    private readonly imageProcessingService: ImageProcessingService,
    private readonly cacheService: CacheService
  ) {}

  async getProfile(userId: number): Promise<UserProfileResponseDto | null> {
    const cacheKey = `user_profile_${userId}`;
    
    // Try cache first
    let profile = await this.cacheService.get<UserProfileResponseDto>(cacheKey);
    if (profile) {
      return profile;
    }

    // Get from database
    const user = await this.userRepository.findOne({
      where: { id: userId },
      select: [
        'id', 'email', 'firstName', 'lastName', 'bio', 'location',
        'website', 'avatar', 'socialMedia', 'privacy', 'createdAt', 'updatedAt'
      ]
    });

    if (!user) {
      return null;
    }

    profile = this.mapUserToProfileDto(user);
    
    // Cache for 30 minutes
    await this.cacheService.set(cacheKey, profile, 30 * 60);
    
    return profile;
  }

  async updateProfile(
    userId: number,
    updateDto: UpdateUserProfileDto,
    updatedBy: number
  ): Promise<UserProfileResponseDto> {
    const user = await this.userRepository.findOne({ where: { id: userId } });
    if (!user) {
      throw new HttpException('User not found', HttpStatus.NOT_FOUND);
    }

    // Check email uniqueness if changed
    if (updateDto.email && updateDto.email !== user.email) {
      const existingUser = await this.userRepository.findOne({
        where: { email: updateDto.email }
      });
      if (existingUser && existingUser.id !== userId) {
        throw new HttpException('Email already in use', HttpStatus.BAD_REQUEST);
      }
    }

    // Update user entity
    Object.assign(user, {
      ...updateDto,
      updatedAt: new Date(),
      updatedBy
    });

    await this.userRepository.save(user);

    // Clear cache
    const cacheKey = `user_profile_${userId}`;
    await this.cacheService.del(cacheKey);

    this.logger.log(`Profile updated for user ${userId}`);
    
    return this.mapUserToProfileDto(user);
  }

  async uploadAvatar(
    userId: number,
    file: Express.Multer.File,
    updatedBy: number
  ): Promise<string> {
    const user = await this.userRepository.findOne({ where: { id: userId } });
    if (!user) {
      throw new HttpException('User not found', HttpStatus.NOT_FOUND);
    }

    try {
      // Process image
      const processedBuffer = await this.imageProcessingService.processAvatar(
        file.buffer,
        { width: 200, height: 200, quality: 80 }
      );

      // Upload to storage
      const fileName = `avatars/${userId}/${Date.now()}.jpg`;
      const avatarUrl = await this.fileStorageService.upload(
        fileName,
        processedBuffer,
        'image/jpeg'
      );

      // Delete old avatar if exists
      if (user.avatar) {
        await this.fileStorageService.delete(
          this.extractFileNameFromUrl(user.avatar)
        );
      }

      // Update user record
      user.avatar = avatarUrl;
      user.updatedAt = new Date();
      user.updatedBy = updatedBy;
      
      await this.userRepository.save(user);

      // Clear cache
      const cacheKey = `user_profile_${userId}`;
      await this.cacheService.del(cacheKey);

      this.logger.log(`Avatar uploaded for user ${userId}: ${avatarUrl}`);
      
      return avatarUrl;
    } catch (error) {
      this.logger.error(`Error uploading avatar for user ${userId}`, error);
      throw new HttpException(
        'Failed to upload avatar',
        HttpStatus.INTERNAL_SERVER_ERROR
      );
    }
  }

  async removeAvatar(userId: number, updatedBy: number): Promise<void> {
    const user = await this.userRepository.findOne({ where: { id: userId } });
    if (!user) {
      throw new HttpException('User not found', HttpStatus.NOT_FOUND);
    }

    if (user.avatar) {
      // Delete from storage
      await this.fileStorageService.delete(
        this.extractFileNameFromUrl(user.avatar)
      );
      
      // Update user record
      user.avatar = null;
      user.updatedAt = new Date();
      user.updatedBy = updatedBy;
      
      await this.userRepository.save(user);

      // Clear cache
      const cacheKey = `user_profile_${userId}`;
      await this.cacheService.del(cacheKey);

      this.logger.log(`Avatar removed for user ${userId}`);
    }
  }

  private mapUserToProfileDto(user: User): UserProfileResponseDto {
    return {
      id: user.id,
      email: user.email,
      firstName: user.firstName,
      lastName: user.lastName,
      fullName: `${user.firstName} ${user.lastName}`,
      bio: user.bio,
      location: user.location,
      website: user.website,
      avatar: user.avatar,
      socialMedia: user.socialMedia,
      privacy: user.privacy,
      completeness: this.calculateCompleteness(user),
      createdAt: user.createdAt,
      updatedAt: user.updatedAt
    };
  }

  private calculateCompleteness(user: User): number {
    const fields = [
      user.firstName,
      user.lastName,
      user.bio,
      user.location,
      user.avatar
    ];
    
    const completedFields = fields.filter(field => field && field.trim()).length;
    return Math.round((completedFields / fields.length) * 100);
  }

  private extractFileNameFromUrl(url: string): string {
    return url.split('/').slice(-2).join('/');
  }
}
```

### Python + FastAPI + SQLAlchemy

**Recommended Pattern:** Async API with Pydantic models and dependency injection

```python
# routers/user_profile.py
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
import logging
import uuid
from pathlib import Path

from ..database import get_async_session
from ..auth.dependencies import get_current_user, require_profile_access
from ..models.user import User
from ..schemas.user_profile import UserProfileResponse, UserProfileUpdate
from ..services.user_profile_service import UserProfileService
from ..services.file_storage_service import FileStorageService
from ..core.exceptions import UserNotFoundError, EmailAlreadyExistsError

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/users/{user_id}/profile", tags=["User Profile"])
security = HTTPBearer()

@router.get("", response_model=UserProfileResponse)
async def get_user_profile(
    user_id: int,
    current_user: User = Depends(get_current_user),
    profile_access: bool = Depends(require_profile_access),
    session: AsyncSession = Depends(get_async_session),
    user_service: UserProfileService = Depends()
) -> UserProfileResponse:
    """Get user profile information"""
    try:
        profile = await user_service.get_profile(session, user_id)
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        return profile
    except Exception as e:
        logger.error(f"Error retrieving profile for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve profile"
        )

@router.put("", response_model=UserProfileResponse)
async def update_user_profile(
    user_id: int,
    profile_update: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    profile_access: bool = Depends(require_profile_access),
    session: AsyncSession = Depends(get_async_session),
    user_service: UserProfileService = Depends()
) -> UserProfileResponse:
    """Update user profile information"""
    try:
        updated_profile = await user_service.update_profile(
            session, user_id, profile_update, current_user.id
        )
        return updated_profile
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address is already in use"
        )
    except Exception as e:
        logger.error(f"Error updating profile for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update profile"
        )

@router.post("/avatar")
async def upload_avatar(
    user_id: int,
    avatar: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    profile_access: bool = Depends(require_profile_access),
    session: AsyncSession = Depends(get_async_session),
    user_service: UserProfileService = Depends(),
    file_service: FileStorageService = Depends()
) -> dict:
    """Upload user avatar image"""
    # Validate file
    if not avatar.content_type.startswith('image/'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be an image"
        )
    
    allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    if avatar.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported image format. Use JPEG, PNG, GIF, or WebP"
        )
    
    if avatar.size > 5 * 1024 * 1024:  # 5MB limit
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Image file size must be less than 5MB"
        )
    
    try:
        avatar_url = await user_service.upload_avatar(
            session, user_id, avatar, current_user.id, file_service
        )
        return {"avatar_url": avatar_url, "message": "Avatar uploaded successfully"}
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception as e:
        logger.error(f"Error uploading avatar for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload avatar"
        )

@router.delete("/avatar")
async def remove_avatar(
    user_id: int,
    current_user: User = Depends(get_current_user),
    profile_access: bool = Depends(require_profile_access),
    session: AsyncSession = Depends(get_async_session),
    user_service: UserProfileService = Depends(),
    file_service: FileStorageService = Depends()
) -> dict:
    """Remove user avatar"""
    try:
        await user_service.remove_avatar(
            session, user_id, current_user.id, file_service
        )
        return {"message": "Avatar removed successfully"}
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception as e:
        logger.error(f"Error removing avatar for user {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to remove avatar"
        )

# services/user_profile_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from fastapi import UploadFile
from typing import Optional, Dict, Any
import asyncio
import logging
from datetime import datetime
from PIL import Image
import io

from ..models.user import User
from ..schemas.user_profile import UserProfileResponse, UserProfileUpdate
from ..services.file_storage_service import FileStorageService
from ..services.cache_service import CacheService
from ..core.exceptions import UserNotFoundError, EmailAlreadyExistsError

logger = logging.getLogger(__name__)

class UserProfileService:
    def __init__(self, cache_service: CacheService):
        self.cache_service = cache_service
    
    async def get_profile(
        self, 
        session: AsyncSession, 
        user_id: int
    ) -> Optional[UserProfileResponse]:
        """Get user profile with caching"""
        cache_key = f"user_profile_{user_id}"
        
        # Try cache first
        cached_profile = await self.cache_service.get(cache_key)
        if cached_profile:
            return UserProfileResponse.parse_obj(cached_profile)
        
        # Get from database
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return None
        
        profile = self._map_user_to_profile(user)
        
        # Cache for 30 minutes
        await self.cache_service.set(cache_key, profile.dict(), ttl=30 * 60)
        
        return profile
    
    async def update_profile(
        self,
        session: AsyncSession,
        user_id: int,
        profile_update: UserProfileUpdate,
        updated_by: int
    ) -> UserProfileResponse:
        """Update user profile"""
        # Get existing user
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        
        # Check email uniqueness if changed
        if profile_update.email and profile_update.email != user.email:
            email_result = await session.execute(
                select(User).where(
                    and_(
                        User.email == profile_update.email,
                        User.id != user_id
                    )
                )
            )
            if email_result.scalar_one_or_none():
                raise EmailAlreadyExistsError("Email address is already in use")
        
        # Update user fields
        update_data = profile_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if hasattr(user, field):
                setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        user.updated_by = updated_by
        
        await session.commit()
        await session.refresh(user)
        
        # Clear cache
        cache_key = f"user_profile_{user_id}"
        await self.cache_service.delete(cache_key)
        
        logger.info(f"Profile updated for user {user_id}")
        
        return self._map_user_to_profile(user)
    
    async def upload_avatar(
        self,
        session: AsyncSession,
        user_id: int,
        avatar_file: UploadFile,
        updated_by: int,
        file_service: FileStorageService
    ) -> str:
        """Upload and process user avatar"""
        # Get user
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        
        try:
            # Read and process image
            image_data = await avatar_file.read()
            processed_image = await self._process_avatar_image(image_data)
            
            # Generate file path
            file_name = f"avatars/{user_id}/{uuid.uuid4().hex}.jpg"
            
            # Upload to storage
            avatar_url = await file_service.upload(
                file_name, processed_image, "image/jpeg"
            )
            
            # Delete old avatar if exists
            if user.avatar:
                old_file_name = self._extract_file_name_from_url(user.avatar)
                await file_service.delete(old_file_name)
            
            # Update user record
            user.avatar = avatar_url
            user.updated_at = datetime.utcnow()
            user.updated_by = updated_by
            
            await session.commit()
            
            # Clear cache
            cache_key = f"user_profile_{user_id}"
            await self.cache_service.delete(cache_key)
            
            logger.info(f"Avatar uploaded for user {user_id}: {avatar_url}")
            
            return avatar_url
            
        except Exception as e:
            logger.error(f"Error uploading avatar for user {user_id}: {e}")
            await session.rollback()
            raise
    
    async def remove_avatar(
        self,
        session: AsyncSession,
        user_id: int,
        updated_by: int,
        file_service: FileStorageService
    ) -> None:
        """Remove user avatar"""
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        
        if user.avatar:
            # Delete from storage
            file_name = self._extract_file_name_from_url(user.avatar)
            await file_service.delete(file_name)
            
            # Update user record
            user.avatar = None
            user.updated_at = datetime.utcnow()
            user.updated_by = updated_by
            
            await session.commit()
            
            # Clear cache
            cache_key = f"user_profile_{user_id}"
            await self.cache_service.delete(cache_key)
            
            logger.info(f"Avatar removed for user {user_id}")
    
    def _map_user_to_profile(self, user: User) -> UserProfileResponse:
        """Map User entity to ProfileResponse"""
        return UserProfileResponse(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            full_name=f"{user.first_name} {user.last_name}",
            bio=user.bio,
            location=user.location,
            website=user.website,
            avatar=user.avatar,
            social_media=user.social_media,
            privacy=user.privacy,
            completeness=self._calculate_completeness(user),
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    
    def _calculate_completeness(self, user: User) -> int:
        """Calculate profile completeness percentage"""
        fields = [
            user.first_name,
            user.last_name,
            user.bio,
            user.location,
            user.avatar
        ]
        
        completed_fields = sum(1 for field in fields if field and field.strip())
        return round((completed_fields / len(fields)) * 100)
    
    async def _process_avatar_image(self, image_data: bytes) -> bytes:
        """Process avatar image - resize and optimize"""
        def process_image():
            with Image.open(io.BytesIO(image_data)) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Resize to 200x200
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                
                # Save as JPEG with optimization
                output = io.BytesIO()
                img.save(output, format='JPEG', quality=85, optimize=True)
                return output.getvalue()
        
        # Run image processing in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, process_image)
    
    def _extract_file_name_from_url(self, url: str) -> str:
        """Extract file name from storage URL"""
        return '/'.join(url.split('/')[-2:])
```

### ASP.NET Core + Entity Framework

**Recommended Pattern:** Controller-Service-Repository with comprehensive validation and error handling

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

### Generic/Fallback Implementation

For unsupported technologies, provide generic implementation patterns:

```yaml
# Generic Feature Implementation Configuration
feature_implementation:
  approach: "specification_driven"  # or "agile", "iterative", "prototype_first"
  
  analysis_principles:
    - "requirement_extraction_and_decomposition"
    - "user_story_mapping_and_acceptance_criteria"
    - "technical_requirement_identification"
    - "dependency_analysis_and_risk_assessment"
    - "architecture_planning_and_design"
    
  implementation_patterns:
    frontend:
      - "component_based_architecture"
      - "reactive_forms_with_validation"
      - "responsive_design_principles"
      - "accessibility_compliance_wcag"
      - "progressive_enhancement"
    
    backend:
      - "api_first_design_approach"
      - "business_logic_separation"
      - "comprehensive_input_validation"
      - "security_first_implementation"
      - "performance_optimization"
    
    database:
      - "schema_migration_strategy"
      - "data_integrity_constraints"
      - "query_optimization_techniques"
      - "backup_and_recovery_procedures"
      - "performance_monitoring"
    
  quality_assurance:
    - "unit_testing_for_business_logic"
    - "integration_testing_for_apis"
    - "end_to_end_testing_for_user_flows"
    - "performance_testing_under_load"
    - "security_testing_and_vulnerability_assessment"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Frontend Framework** from primary_language and technology preferences (React for modern development, Angular for enterprise, Vue for rapid prototyping)
- **Backend Framework** based on technology stack (Java/Spring for enterprise, .NET Core for Microsoft environments, Node.js for JavaScript-first teams, Python/FastAPI for data-heavy applications)
- **Architecture Pattern** to select appropriate implementation approaches (component-based for SPAs, MVC for traditional apps, microservices for scalable systems)
- **Business Domain** for industry-specific features, compliance requirements, and user experience patterns

### 2. Feature Implementation Approach

Select implementation patterns based on detected requirements:
- **Component Architecture**: Technology-specific component patterns with proper separation of concerns
- **State Management**: Framework-appropriate state handling (Redux/Zustand for React, NgRx for Angular, Vuex for Vue)
- **Form Handling**: Technology-specific form validation and submission patterns
- **File Upload**: Framework-appropriate file handling with progress tracking and validation

### 3. API Integration Strategy

Apply technology-specific API patterns:
- **REST API Design**: Technology-appropriate endpoint structure and HTTP method usage
- **Data Validation**: Framework-specific input validation and sanitization
- **Error Handling**: Comprehensive error management with user-friendly feedback
- **Authentication**: Technology-appropriate security implementation and authorization patterns

### 4. Success Criteria

Feature implementation validation checklist:
- **Specification Compliance**: All specification requirements implemented according to acceptance criteria
- **Technology Alignment**: Implementation follows framework best practices and patterns
- **User Experience**: Responsive design, accessibility compliance, and intuitive user interactions
- **Performance**: Fast loading times, optimized API calls, and efficient data processing
- **Security**: Input validation, authorization checks, and protection against common vulnerabilities

---
*Effective feature implementation coordinates across all application layers to deliver production-ready functionality that meets business requirements and technical standards.*