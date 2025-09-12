# Hierarchical TODO Management System

**Purpose: Multi-level task management with agent ownership and workflow integration**

---

## 🎯 System Overview

### Hierarchy Levels

```yaml
hierarchy_structure:
  epic:
    scope: "Business initiative or major feature set"
    duration: "4-12 weeks"
    owner_agents: ["business-analyst", "product-manager"]
    example: "Complete user authentication system overhaul"
    
  feature:
    scope: "Architectural component or user-facing capability"
    duration: "1-3 weeks"  
    owner_agents: ["software-architect", "ux-designer", "security-engineer", "data-engineer"]
    example: "OAuth2 implementation with multi-factor authentication"
    
  task:
    scope: "Implementation work item"
    duration: "1-3 days"
    owner_agents: ["frontend-engineer", "api-engineer", "data-engineer", "security-engineer", "qa-engineer"]
    example: "Implement JWT token refresh mechanism"
    
  subtask:
    scope: "Granular implementation detail"
    duration: "2-8 hours"
    owner_agents: ["Any technical agent"]
    example: "Add unit tests for token validation utility"
```

## 📋 TODO Data Structure

### Epic Level TODO

```typescript
interface EpicTodo {
  id: string;
  type: 'epic';
  title: string;
  description: string;
  business_value: string;
  success_criteria: string[];
  
  // Ownership & Assignment
  primary_agent: 'business-analyst' | 'product-manager';
  stakeholder_agents: AgentType[];
  
  // Lifecycle
  status: 'planned' | 'in_discovery' | 'in_progress' | 'validation' | 'completed';
  priority: 'critical' | 'high' | 'medium' | 'low';
  
  // Timeline
  estimated_duration: string; // "8 weeks"
  planned_start: Date;
  planned_end: Date;
  actual_start?: Date;
  actual_end?: Date;
  
  // Hierarchy
  features: FeatureTodo[];
  
  // Metadata
  created_by: string;
  created_at: Date;
  updated_at: Date;
  tags: string[];
  
  // Business Context
  business_impact: 'high' | 'medium' | 'low';
  user_segments: string[];
  revenue_impact?: number;
  compliance_requirements?: string[];
}
```

### Feature Level TODO

```typescript
interface FeatureTodo {
  id: string;
  type: 'feature';
  epic_id: string;
  title: string;
  description: string;
  
  // Technical Specifications
  architecture_requirements: string[];
  technical_dependencies: string[];
  integration_points: string[];
  
  // Ownership & Assignment
  primary_agent: 'software-architect' | 'ux-designer' | 'security-engineer' | 'data-engineer';
  supporting_agents: AgentType[];
  
  // Lifecycle
  status: 'planned' | 'design' | 'in_progress' | 'review' | 'testing' | 'completed';
  priority: 'critical' | 'high' | 'medium' | 'low';
  
  // Timeline
  estimated_duration: string; // "2 weeks"
  planned_start: Date;
  planned_end: Date;
  actual_start?: Date;
  actual_end?: Date;
  
  // Quality Gates
  design_approved: boolean;
  security_reviewed: boolean;
  architecture_validated: boolean;
  
  // Hierarchy
  epic: EpicTodo;
  tasks: TaskTodo[];
  
  // Metadata
  created_by: string;
  created_at: Date;
  updated_at: Date;
  tags: string[];
  
  // Technical Context
  complexity: 'high' | 'medium' | 'low';
  risk_level: 'high' | 'medium' | 'low';
  technology_stack: string[];
}
```

### Task Level TODO

```typescript
interface TaskTodo {
  id: string;
  type: 'task';
  feature_id: string;
  epic_id: string;
  title: string;
  description: string;
  
  // Implementation Details
  implementation_notes: string[];
  acceptance_criteria: string[];
  definition_of_done: string[];
  
  // Ownership & Assignment
  primary_agent: TechnicalAgentType;
  reviewer_agent?: 'reviewer';
  
  // Lifecycle
  status: 'todo' | 'in_progress' | 'code_review' | 'testing' | 'completed';
  priority: 'critical' | 'high' | 'medium' | 'low';
  
  // Timeline
  estimated_hours: number;
  planned_start: Date;
  planned_end: Date;
  actual_start?: Date;
  actual_end?: Date;
  actual_hours?: number;
  
  // Quality Tracking
  code_reviewed: boolean;
  tests_written: boolean;
  tests_passing: boolean;
  documentation_updated: boolean;
  
  // Hierarchy
  feature: FeatureTodo;
  epic: EpicTodo;
  subtasks: SubtaskTodo[];
  
  // Dependencies
  depends_on: string[]; // Other task IDs
  blocks: string[]; // Task IDs this blocks
  
  // Metadata
  created_by: string;
  created_at: Date;
  updated_at: Date;
  tags: string[];
  
  // Technical Context
  component: string;
  files_modified: string[];
  pull_request_url?: string;
}
```

### Subtask Level TODO

```typescript
interface SubtaskTodo {
  id: string;
  type: 'subtask';
  task_id: string;
  feature_id: string;
  epic_id: string;
  title: string;
  description: string;
  
  // Implementation Details
  implementation_steps: string[];
  
  // Ownership
  assigned_agent: AgentType;
  
  // Lifecycle
  status: 'todo' | 'in_progress' | 'completed';
  priority: 'high' | 'medium' | 'low';
  
  // Timeline
  estimated_minutes: number;
  actual_minutes?: number;
  completed_at?: Date;
  
  // Hierarchy
  task: TaskTodo;
  feature: FeatureTodo;
  epic: EpicTodo;
  
  // Metadata
  created_by: string;
  created_at: Date;
  updated_at: Date;
  
  // Context
  file_path?: string;
  line_number?: number;
  code_snippet?: string;
}
```

## 🔄 Workflow Integration

### Epic Creation Workflow

```yaml
epic_creation:
  trigger: "New business initiative identified"
  
  step_1:
    agent: business-analyst
    prompt: stakeholder-requirements-gathering.md
    output: business_requirements_document
    
  step_2:
    agent: product-manager  
    prompt: mvp-scoping-and-roadmap-planning.md
    input: business_requirements_document
    output: epic_definition
    
  step_3:
    agent: reviewer
    prompt: epic-validation-and-approval.md
    input: epic_definition
    output: validated_epic_todo
    
  auto_generated_todos:
    epic: 1
    estimated_features: 3-8
    estimated_tasks: 15-40
    estimated_subtasks: 50-200
```

### Feature Breakdown Workflow

```yaml
feature_breakdown:
  trigger: "Epic approved and ready for technical planning"
  
  parallel_analysis:
    architecture_agent:
      prompt: feature-architecture-planning.md
      output: technical_requirements
      
    ux_agent:
      prompt: feature-ux-planning.md  
      output: user_experience_requirements
      
    security_agent:
      prompt: feature-security-planning.md
      output: security_requirements
      
  consolidation:
    agent: software-architect
    prompt: feature-consolidation-and-tasking.md
    inputs: [technical_requirements, user_experience_requirements, security_requirements]
    output: feature_todos_with_tasks
```

### Task Assignment Algorithm

```typescript
class TaskAssignmentEngine {
  assignTaskToAgent(task: TaskTodo): AgentType {
    const assignmentRules = {
      // Frontend tasks
      'ui_component': 'frontend-engineer',
      'user_interface': 'frontend-engineer', 
      'responsive_design': 'frontend-engineer',
      'accessibility': 'frontend-engineer',
      
      // Backend tasks
      'api_endpoint': 'api-engineer',
      'microservice': 'api-engineer',
      'integration': 'api-engineer',
      'authentication': 'api-engineer',
      
      // Data tasks
      'database_schema': 'data-engineer',
      'migration': 'data-engineer',
      'etl_pipeline': 'data-engineer',
      'analytics': 'data-engineer',
      
      // Security tasks
      'security_control': 'security-engineer',
      'vulnerability_fix': 'security-engineer',
      'compliance': 'security-engineer',
      'encryption': 'security-engineer',
      
      // Testing tasks
      'test_automation': 'qa-engineer',
      'performance_test': 'qa-engineer',
      'integration_test': 'qa-engineer',
      'quality_gate': 'qa-engineer',
      
      // Infrastructure tasks
      'deployment_pipeline': 'deployment-engineer',
      'infrastructure': 'deployment-engineer',
      'monitoring': 'deployment-engineer',
      'scaling': 'deployment-engineer'
    };
    
    // Analyze task content for keywords
    const taskContent = `${task.title} ${task.description}`.toLowerCase();
    
    for (const [keyword, agent] of Object.entries(assignmentRules)) {
      if (taskContent.includes(keyword.replace('_', ' '))) {
        return agent as AgentType;
      }
    }
    
    // Default assignment based on feature primary agent
    return task.feature.primary_agent;
  }
  
  balanceWorkload(tasks: TaskTodo[]): TaskTodo[] {
    const agentWorkload = new Map<AgentType, number>();
    
    // Calculate current workload
    tasks.forEach(task => {
      if (task.status === 'in_progress' || task.status === 'todo') {
        const agent = task.primary_agent;
        const currentLoad = agentWorkload.get(agent) || 0;
        agentWorkload.set(agent, currentLoad + task.estimated_hours);
      }
    });
    
    // Reassign overloaded tasks
    return tasks.map(task => {
      if (task.status === 'todo') {
        const currentAgent = task.primary_agent;
        const currentLoad = agentWorkload.get(currentAgent) || 0;
        
        // If agent is overloaded (>40 hours), try to reassign
        if (currentLoad > 40) {
          const alternativeAgent = this.findLeastLoadedCompatibleAgent(task, agentWorkload);
          if (alternativeAgent && (agentWorkload.get(alternativeAgent) || 0) < currentLoad * 0.8) {
            task.primary_agent = alternativeAgent;
          }
        }
      }
      return task;
    });
  }
}
```

## 📊 Progress Tracking and Metrics

### Automatic Progress Calculation

```typescript
class ProgressCalculator {
  calculateEpicProgress(epic: EpicTodo): ProgressMetrics {
    const allFeatures = epic.features;
    const completedFeatures = allFeatures.filter(f => f.status === 'completed').length;
    const inProgressFeatures = allFeatures.filter(f => f.status === 'in_progress').length;
    
    const allTasks = allFeatures.flatMap(f => f.tasks);
    const completedTasks = allTasks.filter(t => t.status === 'completed').length;
    const inProgressTasks = allTasks.filter(t => t.status === 'in_progress').length;
    
    const totalEstimatedHours = allTasks.reduce((sum, task) => sum + task.estimated_hours, 0);
    const completedHours = allTasks.filter(t => t.status === 'completed')
      .reduce((sum, task) => sum + (task.actual_hours || task.estimated_hours), 0);
    
    return {
      epic_completion: (completedFeatures / allFeatures.length) * 100,
      feature_progress: {
        total: allFeatures.length,
        completed: completedFeatures,
        in_progress: inProgressFeatures,
        remaining: allFeatures.length - completedFeatures - inProgressFeatures
      },
      task_progress: {
        total: allTasks.length,
        completed: completedTasks,
        in_progress: inProgressTasks,
        remaining: allTasks.length - completedTasks - inProgressTasks
      },
      time_progress: {
        estimated_total_hours: totalEstimatedHours,
        completed_hours: completedHours,
        completion_percentage: (completedHours / totalEstimatedHours) * 100,
        estimated_remaining_hours: totalEstimatedHours - completedHours
      },
      velocity_metrics: this.calculateVelocity(epic),
      projected_completion: this.projectCompletion(epic)
    };
  }
  
  calculateVelocity(epic: EpicTodo): VelocityMetrics {
    const completedTasks = epic.features.flatMap(f => f.tasks)
      .filter(t => t.status === 'completed' && t.actual_end);
    
    // Calculate weekly velocity
    const weeksData = new Map<string, { tasks: number, hours: number }>();
    
    completedTasks.forEach(task => {
      const week = this.getWeekKey(task.actual_end!);
      const weekData = weeksData.get(week) || { tasks: 0, hours: 0 };
      weekData.tasks += 1;
      weekData.hours += task.actual_hours || task.estimated_hours;
      weeksData.set(week, weekData);
    });
    
    const velocityByWeek = Array.from(weeksData.entries()).map(([week, data]) => ({
      week,
      tasks_completed: data.tasks,
      hours_completed: data.hours
    }));
    
    const avgTasksPerWeek = velocityByWeek.reduce((sum, v) => sum + v.tasks_completed, 0) / velocityByWeek.length;
    const avgHoursPerWeek = velocityByWeek.reduce((sum, v) => sum + v.hours_completed, 0) / velocityByWeek.length;
    
    return {
      weekly_velocity: velocityByWeek,
      average_tasks_per_week: avgTasksPerWeek,
      average_hours_per_week: avgHoursPerWeek,
      velocity_trend: this.calculateTrend(velocityByWeek)
    };
  }
}
```

### Burndown Chart Integration

```typescript
interface BurndownData {
  epic_id: string;
  date: Date;
  remaining_story_points: number;
  remaining_hours: number;
  remaining_tasks: number;
  completed_today: number;
  ideal_remaining: number;
}

class BurndownTracker {
  generateBurndownChart(epic: EpicTodo): BurndownChart {
    const startDate = epic.actual_start || epic.planned_start;
    const endDate = epic.planned_end;
    const totalHours = this.calculateTotalHours(epic);
    
    const dailyData: BurndownData[] = [];
    let currentDate = new Date(startDate);
    
    while (currentDate <= endDate) {
      const remainingHours = this.calculateRemainingHours(epic, currentDate);
      const idealRemaining = this.calculateIdealRemaining(totalHours, startDate, endDate, currentDate);
      const completedToday = this.calculateCompletedToday(epic, currentDate);
      
      dailyData.push({
        epic_id: epic.id,
        date: new Date(currentDate),
        remaining_story_points: this.calculateRemainingStoryPoints(epic, currentDate),
        remaining_hours: remainingHours,
        remaining_tasks: this.calculateRemainingTasks(epic, currentDate),
        completed_today: completedToday,
        ideal_remaining: idealRemaining
      });
      
      currentDate.setDate(currentDate.getDate() + 1);
    }
    
    return {
      epic,
      data: dailyData,
      projection: this.calculateProjection(dailyData),
      alerts: this.generateAlerts(dailyData)
    };
  }
}
```

## 🚨 Smart Notifications and Alerts

### Automated Status Updates

```yaml
notification_triggers:
  task_overdue:
    condition: "task.planned_end < now() AND task.status != 'completed'"
    recipients: [task.primary_agent, task.feature.primary_agent]
    message: "Task '${task.title}' is overdue by ${days_overdue} days"
    
  epic_at_risk:
    condition: "epic.projected_completion > epic.planned_end"
    recipients: [epic.primary_agent, epic.stakeholder_agents]
    message: "Epic '${epic.title}' is at risk of missing deadline by ${days_late} days"
    
  quality_gate_failed:
    condition: "task.status == 'code_review' AND task.code_reviewed == false FOR 24 hours"
    recipients: [task.primary_agent, reviewer]
    message: "Task '${task.title}' has been waiting for code review for 24+ hours"
    
  dependency_blocking:
    condition: "task.depends_on contains incomplete tasks"
    recipients: [task.primary_agent]
    message: "Task '${task.title}' is blocked by ${blocked_by_count} incomplete dependencies"
```

### Intelligent Task Recommendations

```typescript
class TaskRecommendationEngine {
  recommendNextTasks(agent: AgentType, currentWorkload: number): TaskTodo[] {
    const availableTasks = this.getAvailableTasks(agent);
    const prioritizedTasks = this.prioritizeTasks(availableTasks);
    const filteredTasks = this.filterByCapacity(prioritizedTasks, currentWorkload);
    
    return filteredTasks.map(task => ({
      ...task,
      recommendation_score: this.calculateRecommendationScore(task, agent),
      recommendation_reason: this.explainRecommendation(task, agent)
    }));
  }
  
  private calculateRecommendationScore(task: TaskTodo, agent: AgentType): number {
    let score = 0;
    
    // Priority weight (40%)
    const priorityWeights = { critical: 10, high: 7, medium: 5, low: 2 };
    score += (priorityWeights[task.priority] || 0) * 0.4;
    
    // Agent expertise match (25%)
    const expertiseMatch = this.getExpertiseMatch(task, agent);
    score += expertiseMatch * 0.25;
    
    // Dependencies readiness (20%)
    const dependencyReadiness = this.getDependencyReadiness(task);
    score += dependencyReadiness * 0.2;
    
    // Feature criticality (15%)
    const featureCriticality = this.getFeatureCriticality(task.feature);
    score += featureCriticality * 0.15;
    
    return Math.round(score * 10) / 10;
  }
}
```

## 📤 Integration Points

### Claude Code TodoWrite Integration

```typescript
class ClaudeCodeTodoIntegration {
  syncToClaudeCode(todos: HierarchicalTodo[]): void {
    const claudeCodeTodos = todos.map(todo => ({
      content: this.formatTodoContent(todo),
      status: this.mapStatus(todo.status),
      activeForm: this.generateActiveForm(todo)
    }));
    
    // Use existing TodoWrite tool
    this.claudeCodeAPI.updateTodos(claudeCodeTodos);
  }
  
  private formatTodoContent(todo: HierarchicalTodo): string {
    switch (todo.type) {
      case 'epic':
        return `${todo.title} (${todo.features.length} features, ~${this.calculateTotalHours(todo)}h)`;
      case 'feature':
        return `${todo.title} (${todo.tasks.length} tasks, ~${this.calculateFeatureHours(todo)}h)`;
      case 'task':
        return `${todo.title} (${todo.estimated_hours}h, ${todo.primary_agent})`;
      case 'subtask':
        return `${todo.title} (${todo.estimated_minutes}min)`;
    }
  }
}
```

---

## 🎯 Next Steps

1. **Epic/Feature/Task Creation Tools** - Prompts for breaking down work
2. **Agent Assignment Automation** - Smart task routing
3. **Progress Tracking Dashboard** - Visual progress monitoring
4. **Dependency Management** - Automatic blocking/unblocking
5. **Velocity Analytics** - Team performance insights

Czy chcesz, żebym zaimplementował któryś z tych komponentów, czy przejdziemy do rozbudowy biblioteki promptów (punkt 1)?