---
name: steeb-task-debugger
description: Debug and fix task-related issues in STEEB app. This skill should be
  used when encountering task creation, completion, deletion, or state management
  problems in the STEEB task management system.
metadata:
  mind.id: ai.medrix.skill.steeb-task-debugger
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: steeb-task-debugger (Hiizzzo)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Debug and fix task-related issues in STEEB app. This skill should be used when encountering task creation, completion, deletion, or state management problems in the STEEB task management system.","starter_prompts":["Help me use steeb task debugger for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply steeb task debugger to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with steeb task debugger and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"调试并修复 STEEB 应用中的任务问题。适用于任务创建、完成、删除或状态管理异常。","starter_prompts":["请帮我用steeb task debugger完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用steeb task debugger，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用steeb task debugger审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/Hiizzzo/Steeb
  mind.upstream.commit: d374899e98154d1bbcf33914e9c05060902e2634
  mind.upstream.license: NOASSERTION
  mind.upstream.path: .claude/skills/steeb-task-debugger/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/Hiizzzo/Steeb/d374899e98154d1bbcf33914e9c05060902e2634/.claude/skills/steeb-task-debugger/SKILL.md"]'
license: NOASSERTION
---

# STEEB Task Debugger

This skill helps debug and resolve issues with task management in the STEEB application.

## When to Use This Skill

Use this skill when encountering:
- Tasks not completing correctly
- Task state inconsistencies between components
- Firestore synchronization errors
- Tasks disappearing or duplicating
- UI not reflecting task changes
- Performance issues with task operations

## Debugging Workflow

### Step 1: Identify the Issue Type

First, determine the type of task issue:

**Task Creation Issues:**
- Check if `addTask` function is being called correctly
- Verify task data structure matches expected `Task` interface
- Check for duplicate task IDs or missing required fields

**Task Completion/Toggle Issues:**
- Verify `toggleTask` is called with correct task ID
- Check if optimistic updates are working
- Verify Firestore synchronization (if enabled)

**Task Deletion Issues:**
- Confirm task exists before deletion attempt
- Check if `deleteTask` function removes from local state
- Verify UI re-renders after deletion

**State Management Issues:**
- Check if tasks are properly synchronized between components
- Verify Zustand store updates trigger re-renders
- Check for stale state or race conditions

### Step 2: Run Diagnostic Commands

Execute these commands to diagnose the problem:

```bash
# Check current task state in console
console.log('Current tasks:', useTaskStore.getState().tasks);

# Check specific task properties
const task = useTaskStore.getState().tasks.find(t => t.id === 'task-id');
console.log('Task details:', task);

# Check store state
console.log('Store state:', useTaskStore.getState());
```

### Step 3: Verify Store Functions

Test the core task management functions:

```javascript
// Test task creation
const testTask = {
  title: 'Debug test task',
  completed: false,
  status: 'pending',
  createdAt: new Date().toISOString()
};
await useTaskStore.getState().addTask(testTask);

// Test task toggle
const taskId = 'existing-task-id';
await useTaskStore.getState().toggleTask(taskId);

// Test task deletion
await useTaskStore.getState().deleteTask(taskId);
```

### Step 4: Check Component Integration

Verify components are using the store correctly:

**SteebChatAI Component:**
- Ensure `toggleTask` and `deleteTask` are properly imported
- Check if button onClick handlers prevent multiple clicks
- Verify error handling in async operations

**Dashboard Component:**
- Ensure tasks are filtered correctly (pending vs completed)
- Check if `useTaskStore` updates trigger re-renders
- Verify statistics calculations are accurate

### Step 5: Common Solutions

**Multiple Click Issues:**
```javascript
// Add this pattern to prevent multiple clicks
const [isProcessing, setIsProcessing] = useState(false);

const handleTaskAction = async (taskId) => {
  if (isProcessing) return;

  setIsProcessing(true);
  try {
    await toggleTask(taskId);
  } catch (error) {
    console.error('Task action failed:', error);
  } finally {
    setIsProcessing(false);
  }
};
```

**State Not Updating:**
```javascript
// Force re-render after store update
setForceUpdate(prev => prev + 1);
// Or use proper React state management
const { tasks, toggleTask } = useTaskStore();
```

**Firebase Errors:**
```javascript
// Handle Firestore errors gracefully
try {
  await FirestoreTaskService.updateTask(id, updates);
} catch (error) {
  console.warn('Firestore sync failed, local changes kept:', error);
  // Continue with local state only
}
```

### Step 6: Performance Optimization

For large task lists:
- Implement virtual scrolling
- Add pagination or lazy loading
- Use React.memo for task components
- Debounce search/filter operations

## Scripts

The following scripts are available for automated debugging:

### Quick Task Validation
```bash
# Run quick task validation
python .claude/skills/steeb-task-debugger/scripts/quick_validate.py
```

### Task State Analyzer
```bash
# Analyze task state consistency
python .claude/skills/steeb-task-debugger/scripts/analyze_task_state.py
```

## References

- Task interface definition in `src/types/index.ts`
- Task store implementation in `src/store/useTaskStore.ts`
- Firestore service in `src/services/firestoreTaskService.ts`
- Task components in `src/components/Task*.tsx`

## Assets

- Debug checklist template for common issues
- Task state flow diagram
- Performance profiling guidelines