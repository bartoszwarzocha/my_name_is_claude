# React Component Development and Testing

**Agent: frontend-engineer**
**Purpose: Develop scalable, reusable React components with comprehensive testing strategies**

---

## 🎯 Mission

Create high-quality React components that are maintainable, performant, accessible, and thoroughly tested, following modern development practices and design system principles.

## 📋 Component Development Process

### Step 1: Component Architecture Planning

**Component Design Principles:**
```typescript
// Component design specifications
interface ComponentDesign {
  // Single Responsibility Principle
  purpose: string;  // What this component does
  responsibilities: string[];  // Specific tasks it handles
  
  // Interface Design
  props: ComponentProps;  // External API
  state: ComponentState;  // Internal state management
  
  // Composition Strategy
  composition: 'container' | 'presentational' | 'compound';
  children?: ComponentType[];  // Child components
  
  // Performance Considerations
  memoization: boolean;  // React.memo usage
  lazy_loading: boolean;  // React.lazy for code splitting
  
  // Accessibility Requirements
  a11y: AccessibilitySpec;  // WCAG compliance
  keyboard_navigation: boolean;
  screen_reader_support: boolean;
}
```

**Component Hierarchy Planning:**
```
UserProfile/
├── UserProfileContainer.tsx        # Data fetching & state management
├── UserProfile.tsx                 # Main presentation component
├── components/
│   ├── UserAvatar.tsx             # Reusable avatar component
│   ├── UserInfo.tsx               # User information display
│   ├── UserActions.tsx            # Action buttons
│   └── UserStats.tsx              # Statistics display
├── hooks/
│   ├── useUserProfile.ts          # Custom hook for user data
│   ├── useUserActions.ts          # Custom hook for user actions
│   └── useUserStats.ts            # Custom hook for statistics
├── types/
│   └── UserProfile.types.ts       # TypeScript definitions
├── __tests__/
│   ├── UserProfile.test.tsx       # Component tests
│   ├── UserProfile.integration.test.tsx  # Integration tests
│   └── __mocks__/                 # Test mocks
└── UserProfile.stories.tsx        # Storybook stories
```

### Step 2: TypeScript Implementation

**Component Interface Definition:**
```typescript
// UserProfile.types.ts
export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  avatar?: string;
  role: UserRole;
  isActive: boolean;
  lastLogin?: Date;
  preferences: UserPreferences;
}

export interface UserProfileProps {
  userId: string;
  variant?: 'compact' | 'detailed' | 'card';
  editable?: boolean;
  showActions?: boolean;
  onEdit?: (user: User) => void;
  onDelete?: (userId: string) => void;
  onStatusChange?: (userId: string, status: boolean) => void;
  className?: string;
  testId?: string;
}

export interface UserProfileState {
  user: User | null;
  isLoading: boolean;
  error: string | null;
  isEditing: boolean;
}
```

**Main Component Implementation:**
```typescript
// UserProfile.tsx
import React, { useState, useCallback, memo } from 'react';
import { UserProfileProps, UserProfileState } from './types/UserProfile.types';
import { useUserProfile, useUserActions } from './hooks';
import { UserAvatar, UserInfo, UserActions } from './components';
import styles from './UserProfile.module.css';

const UserProfile: React.FC<UserProfileProps> = memo(({
  userId,
  variant = 'detailed',
  editable = false,
  showActions = true,
  onEdit,
  onDelete,
  onStatusChange,
  className,
  testId = 'user-profile'
}) => {
  // Custom hooks for data and actions
  const { user, isLoading, error } = useUserProfile(userId);
  const { updateUser, deleteUser, toggleUserStatus } = useUserActions();
  
  // Local state
  const [isEditing, setIsEditing] = useState(false);
  
  // Event handlers
  const handleEdit = useCallback(() => {
    if (user && onEdit) {
      onEdit(user);
    }
    setIsEditing(true);
  }, [user, onEdit]);
  
  const handleSave = useCallback(async (updatedUser: User) => {
    try {
      await updateUser(updatedUser);
      setIsEditing(false);
    } catch (error) {
      console.error('Failed to update user:', error);
    }
  }, [updateUser]);
  
  const handleDelete = useCallback(async () => {
    if (user && onDelete && window.confirm('Are you sure you want to delete this user?')) {
      await deleteUser(user.id);
      onDelete(user.id);
    }
  }, [user, onDelete, deleteUser]);
  
  const handleStatusToggle = useCallback(async () => {
    if (user) {
      await toggleUserStatus(user.id, !user.isActive);
      if (onStatusChange) {
        onStatusChange(user.id, !user.isActive);
      }
    }
  }, [user, onStatusChange, toggleUserStatus]);
  
  // Loading state
  if (isLoading) {
    return (
      <div className={styles.loading} data-testid={`${testId}-loading`}>
        <div className={styles.skeleton} />
      </div>
    );
  }
  
  // Error state
  if (error) {
    return (
      <div className={styles.error} data-testid={`${testId}-error`}>
        <p>Error loading user profile: {error}</p>
      </div>
    );
  }
  
  // No user found
  if (!user) {
    return (
      <div className={styles.notFound} data-testid={`${testId}-not-found`}>
        <p>User not found</p>
      </div>
    );
  }
  
  return (
    <article 
      className={`${styles.userProfile} ${styles[variant]} ${className || ''}`}
      data-testid={testId}
      role="region"
      aria-labelledby={`${testId}-name`}
    >
      <header className={styles.header}>
        <UserAvatar 
          user={user} 
          size={variant === 'compact' ? 'small' : 'large'}
          testId={`${testId}-avatar`}
        />
        <UserInfo 
          user={user} 
          variant={variant}
          isEditing={isEditing}
          onSave={handleSave}
          testId={`${testId}-info`}
        />
      </header>
      
      {showActions && (
        <footer className={styles.actions}>
          <UserActions
            user={user}
            editable={editable}
            onEdit={handleEdit}
            onDelete={handleDelete}
            onStatusToggle={handleStatusToggle}
            testId={`${testId}-actions`}
          />
        </footer>
      )}
    </article>
  );
});

UserProfile.displayName = 'UserProfile';

export default UserProfile;
```

**Custom Hooks Implementation:**
```typescript
// hooks/useUserProfile.ts
import { useState, useEffect } from 'react';
import { User } from '../types/UserProfile.types';
import { userService } from '../services/userService';

export const useUserProfile = (userId: string) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    let isMounted = true;
    
    const fetchUser = async () => {
      try {
        setIsLoading(true);
        setError(null);
        
        const userData = await userService.getUserById(userId);
        
        if (isMounted) {
          setUser(userData);
        }
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err.message : 'Failed to fetch user');
        }
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    };
    
    fetchUser();
    
    return () => {
      isMounted = false;
    };
  }, [userId]);
  
  return { user, isLoading, error };
};
```

### Step 3: Comprehensive Testing Strategy

**Unit Testing with Jest & Testing Library:**
```typescript
// __tests__/UserProfile.test.tsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { UserProfile } from '../UserProfile';
import { userService } from '../services/userService';

// Mock the service
jest.mock('../services/userService');
const mockUserService = userService as jest.Mocked<typeof userService>;

// Test data
const mockUser = {
  id: '1',
  email: 'john@example.com',
  firstName: 'John',
  lastName: 'Doe',
  avatar: 'https://example.com/avatar.jpg',
  role: 'user' as const,
  isActive: true,
  preferences: { theme: 'light', notifications: true }
};

describe('UserProfile', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });
  
  describe('Loading States', () => {
    it('displays loading state while fetching user data', () => {
      mockUserService.getUserById.mockImplementation(() => 
        new Promise(() => {}) // Never resolves
      );
      
      render(<UserProfile userId="1" />);
      
      expect(screen.getByTestId('user-profile-loading')).toBeInTheDocument();
      expect(screen.getByRole('region')).toHaveClass('loading');
    });
  });
  
  describe('Error States', () => {
    it('displays error message when user fetch fails', async () => {
      mockUserService.getUserById.mockRejectedValue(
        new Error('Network error')
      );
      
      render(<UserProfile userId="1" />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile-error')).toBeInTheDocument();
        expect(screen.getByText(/Error loading user profile/)).toBeInTheDocument();
      });
    });
    
    it('displays not found message when user does not exist', async () => {
      mockUserService.getUserById.mockResolvedValue(null);
      
      render(<UserProfile userId="1" />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile-not-found')).toBeInTheDocument();
        expect(screen.getByText('User not found')).toBeInTheDocument();
      });
    });
  });
  
  describe('User Data Display', () => {
    beforeEach(() => {
      mockUserService.getUserById.mockResolvedValue(mockUser);
    });
    
    it('renders user profile with all required information', async () => {
      render(<UserProfile userId="1" />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile')).toBeInTheDocument();
      });
      
      // Check avatar
      expect(screen.getByTestId('user-profile-avatar')).toBeInTheDocument();
      
      // Check user info
      expect(screen.getByText('John Doe')).toBeInTheDocument();
      expect(screen.getByText('john@example.com')).toBeInTheDocument();
      
      // Check actions
      expect(screen.getByTestId('user-profile-actions')).toBeInTheDocument();
    });
    
    it('applies correct variant styling', async () => {
      render(<UserProfile userId="1" variant="compact" />);
      
      await waitFor(() => {
        const profile = screen.getByTestId('user-profile');
        expect(profile).toHaveClass('compact');
      });
    });
  });
  
  describe('User Interactions', () => {
    beforeEach(() => {
      mockUserService.getUserById.mockResolvedValue(mockUser);
      mockUserService.updateUser.mockResolvedValue(mockUser);
    });
    
    it('calls onEdit when edit button is clicked', async () => {
      const onEdit = jest.fn();
      
      render(<UserProfile userId="1" editable onEdit={onEdit} />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile')).toBeInTheDocument();
      });
      
      const editButton = screen.getByRole('button', { name: /edit/i });
      await userEvent.click(editButton);
      
      expect(onEdit).toHaveBeenCalledWith(mockUser);
    });
    
    it('handles user deletion with confirmation', async () => {
      const onDelete = jest.fn();
      global.confirm = jest.fn().mockReturnValue(true);
      mockUserService.deleteUser.mockResolvedValue(undefined);
      
      render(<UserProfile userId="1" onDelete={onDelete} />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile')).toBeInTheDocument();
      });
      
      const deleteButton = screen.getByRole('button', { name: /delete/i });
      await userEvent.click(deleteButton);
      
      expect(global.confirm).toHaveBeenCalledWith(
        'Are you sure you want to delete this user?'
      );
      expect(mockUserService.deleteUser).toHaveBeenCalledWith('1');
      expect(onDelete).toHaveBeenCalledWith('1');
    });
  });
  
  describe('Accessibility', () => {
    beforeEach(() => {
      mockUserService.getUserById.mockResolvedValue(mockUser);
    });
    
    it('has proper ARIA labels and roles', async () => {
      render(<UserProfile userId="1" />);
      
      await waitFor(() => {
        const profile = screen.getByTestId('user-profile');
        expect(profile).toHaveAttribute('role', 'region');
        expect(profile).toHaveAttribute('aria-labelledby', 'user-profile-name');
      });
    });
    
    it('supports keyboard navigation', async () => {
      render(<UserProfile userId="1" editable />);
      
      await waitFor(() => {
        expect(screen.getByTestId('user-profile')).toBeInTheDocument();
      });
      
      // Tab to edit button
      await userEvent.tab();
      expect(screen.getByRole('button', { name: /edit/i })).toHaveFocus();
      
      // Tab to delete button
      await userEvent.tab();
      expect(screen.getByRole('button', { name: /delete/i })).toHaveFocus();
    });
  });
});
```

**Integration Testing:**
```typescript
// __tests__/UserProfile.integration.test.tsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { UserProfile } from '../UserProfile';
import { TestProvider } from '../../../test-utils/TestProvider';

describe('UserProfile Integration Tests', () => {
  it('integrates with user context and updates global state', async () => {
    render(
      <TestProvider>
        <UserProfile userId="1" />
      </TestProvider>
    );
    
    // Wait for user data to load
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    // Edit user
    const editButton = screen.getByRole('button', { name: /edit/i });
    await userEvent.click(editButton);
    
    // Update name
    const nameInput = screen.getByRole('textbox', { name: /first name/i });
    await userEvent.clear(nameInput);
    await userEvent.type(nameInput, 'Jane');
    
    // Save changes
    const saveButton = screen.getByRole('button', { name: /save/i });
    await userEvent.click(saveButton);
    
    // Verify update
    await waitFor(() => {
      expect(screen.getByText('Jane Doe')).toBeInTheDocument();
    });
  });
});
```

### Step 4: Storybook Documentation

**Component Stories:**
```typescript
// UserProfile.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { UserProfile } from './UserProfile';
import { mockUser, mockUserLoading, mockUserError } from './__mocks__/userMocks';

const meta: Meta<typeof UserProfile> = {
  title: 'Components/UserProfile',
  component: UserProfile,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: 'A comprehensive user profile component with support for different variants, editing, and actions.'
      }
    }
  },
  argTypes: {
    variant: {
      control: { type: 'select' },
      options: ['compact', 'detailed', 'card'],
      description: 'Visual variant of the profile'
    },
    editable: {
      control: { type: 'boolean' },
      description: 'Whether the profile can be edited'
    },
    showActions: {
      control: { type: 'boolean' },
      description: 'Whether to show action buttons'
    }
  }
};

export default meta;
type Story = StoryObj<typeof meta>;

// Default story
export const Default: Story = {
  args: {
    userId: '1',
    variant: 'detailed',
    editable: true,
    showActions: true
  },
  parameters: {
    mockData: mockUser
  }
};

// Compact variant
export const Compact: Story = {
  args: {
    ...Default.args,
    variant: 'compact'
  },
  parameters: {
    docs: {
      description: {
        story: 'Compact version suitable for lists or cards'
      }
    }
  }
};

// Loading state
export const Loading: Story = {
  args: {
    userId: 'loading'
  },
  parameters: {
    mockData: mockUserLoading,
    docs: {
      description: {
        story: 'Shows loading skeleton while fetching user data'
      }
    }
  }
};

// Error state
export const Error: Story = {
  args: {
    userId: 'error'
  },
  parameters: {
    mockData: mockUserError,
    docs: {
      description: {
        story: 'Error state when user data fails to load'
      }
    }
  }
};

// Read-only version
export const ReadOnly: Story = {
  args: {
    ...Default.args,
    editable: false,
    showActions: false
  },
  parameters: {
    docs: {
      description: {
        story: 'Read-only version without edit capabilities'
      }
    }
  }
};
```

## 🎨 CSS-in-JS and Styling

### Step 5: Modern Styling Approach

**CSS Modules Implementation:**
```css
/* UserProfile.module.css */
.userProfile {
  display: flex;
  flex-direction: column;
  background: var(--surface-color);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
  transition: all 0.2s ease-in-out;
}

.userProfile:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.userProfile.compact {
  flex-direction: row;
  align-items: center;
  padding: var(--spacing-md);
}

.userProfile.card {
  max-width: 300px;
  text-align: center;
}

.header {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}

.compact .header {
  margin-bottom: 0;
  flex: 1;
}

.actions {
  display: flex;
  gap: var(--spacing-sm);
  justify-content: flex-end;
  margin-top: auto;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 200px;
}

.skeleton {
  width: 100%;
  height: 20px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  border-radius: var(--border-radius-sm);
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.error {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100px;
  color: var(--error-color);
  text-align: center;
}

.notFound {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100px;
  color: var(--muted-color);
  text-align: center;
}

/* Responsive design */
@media (max-width: 768px) {
  .userProfile {
    padding: var(--spacing-md);
  }
  
  .header {
    flex-direction: column;
    text-align: center;
  }
  
  .actions {
    justify-content: center;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .skeleton {
    background: linear-gradient(90deg, #2a2a2a 25%, #3a3a3a 50%, #2a2a2a 75%);
  }
}

/* High contrast mode support */
@media (prefers-contrast: high) {
  .userProfile {
    border: 2px solid var(--border-color);
  }
  
  .userProfile:hover {
    border-color: var(--primary-color);
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .userProfile {
    transition: none;
  }
  
  .skeleton {
    animation: none;
    background: var(--muted-color);
  }
  
  .userProfile:hover {
    transform: none;
  }
}
```

## 📤 Deliverables

- **React Component Library** with TypeScript definitions and comprehensive testing
- **Storybook Documentation** with interactive examples and usage guidelines
- **Test Coverage Report** with unit, integration, and accessibility tests
- **Performance Metrics** with bundle size analysis and runtime performance
- **Accessibility Audit** with WCAG compliance verification
- **Component API Documentation** with props interface and usage examples
- **Style Guide Integration** with design system tokens and theming support

## 🤝 Collaboration Points

**With ux-designer:** Component design validation, accessibility requirements, and user experience testing
**With api-engineer:** Data fetching patterns, error handling, and API integration
**With qa-engineer:** Test strategy alignment, accessibility testing, and quality assurance
**With reviewer:** Code quality standards, performance optimization, and best practices validation
**With deployment-engineer:** Bundle optimization, lazy loading strategies, and production deployment

---
*Well-architected React components provide the foundation for maintainable, performant, and accessible user interfaces that scale with business requirements.*