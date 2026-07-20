---
name: thoroughness
description: Use when implementing complex multi-step tasks, fixing critical bugs,
  or when quality and completeness matter more than speed - ensures comprehensive
  implementation without shortcuts through systematic analysis, implementation, and
  verification phases
metadata:
  mind.id: ai.medrix.skill.thoroughness
  mind.distribution: marketplace
  mind.market-primary: productivity-tools
  mind.market-categories: '["productivity-tools"]'
  mind.marketplace-summary: thoroughness (pr-pm)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Use when implementing complex multi-step tasks, fixing critical bugs, or when quality and completeness matter more than speed - ensures comprehensive implementation without shortcuts through systematic analysis, implementation, and verification phases","starter_prompts":["Help me use thoroughness for my task. Start by asking for the goal, inputs, deadline, constraints, and desired output, then complete the workflow.","Apply thoroughness to the material I provide, identify missing or inefficient steps, and produce a clearer, more reliable result.","Review my existing approach with thoroughness and turn it into a practical checklist or plan with priorities, owners, and validation steps."]},"zh-CN":{"description":"用于复杂多步骤实施、关键缺陷修复或质量与完整性优先的任务，通过系统化分析、实施和验证避免捷径。","starter_prompts":["请帮我用thoroughness完成任务。先询问目标、输入、截止时间、约束和所需输出，然后完成整个流程。","请对我提供的材料应用thoroughness，找出缺失或低效步骤，并产出更清晰、更可靠的结果。","请使用thoroughness审查我现有的方法，并将其整理为包含优先级、负责人和验证步骤的实用清单或计划。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/pr-pm/prpm
  mind.upstream.commit: 903b956417062bd9fbbb1df7cee44ca8a8291126
  mind.upstream.path: .claude/skills/thoroughness/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/pr-pm/prpm/blob/903b956417062bd9fbbb1df7cee44ca8a8291126/LICENSE",
    "https://raw.githubusercontent.com/pr-pm/prpm/903b956417062bd9fbbb1df7cee44ca8a8291126/.claude/skills/thoroughness/SKILL.md"]'
license: MIT
---

# Thoroughness

## Purpose
This skill ensures comprehensive, complete implementation of complex tasks without shortcuts. Use this when quality and completeness matter more than speed.

## When to Use
- Fixing critical bugs or compilation errors
- Implementing complex multi-step features
- Debugging test failures
- Refactoring large codebases
- Production deployments
- Any task where shortcuts could cause future problems

## Methodology

### Phase 1: Comprehensive Analysis (20% of time)
1. **Identify All Issues**
   - List every error, warning, and failing test
   - Group related issues together
   - Prioritize by dependency order
   - Create issue hierarchy (what blocks what)

2. **Root Cause Analysis**
   - Don't fix symptoms, find root causes
   - Trace errors to their source
   - Identify patterns in failures
   - Document assumptions that were wrong

3. **Create Detailed Plan**
   - Break down into atomic steps
   - Estimate time for each step
   - Identify dependencies between steps
   - Plan verification for each step
   - Schedule breaks/checkpoints

### Phase 2: Systematic Implementation (60% of time)
1. **Fix Issues in Dependency Order**
   - Start with foundational issues
   - Fix one thing completely before moving on
   - Test after each fix
   - Document what was changed and why

2. **Verify Each Fix**
   - Write/run tests for the specific fix
   - Check for side effects
   - Verify related functionality still works
   - Document test results

3. **Track Progress**
   - Mark issues as completed
   - Update plan with new discoveries
   - Adjust time estimates
   - Note any blockers immediately

### Phase 3: Comprehensive Verification (20% of time)
1. **Run All Tests**
   - Unit tests
   - Integration tests
   - E2E tests
   - Manual verification

2. **Cross-Check Everything**
   - Review all changed files
   - Verify compilation succeeds
   - Check for console errors/warnings
   - Test edge cases

3. **Documentation**
   - Update relevant docs
   - Add inline comments for complex fixes
   - Document known limitations
   - Create issues for future work

## Anti-Patterns to Avoid
- ❌ Fixing multiple unrelated issues at once
- ❌ Moving on before verifying a fix works
- ❌ Assuming similar errors have the same cause
- ❌ Skipping test writing "to save time"
- ❌ Copy-pasting solutions without understanding
- ❌ Ignoring warnings "because it compiles"
- ❌ Making changes without reading existing code first

## Quality Checkpoints
- [ ] Can I explain why this fix works?
- [ ] Have I tested this specific change?
- [ ] Are there any side effects?
- [ ] Is this the root cause or a symptom?
- [ ] Will this prevent similar issues in the future?
- [ ] Is the code readable and maintainable?
- [ ] Have I documented non-obvious decisions?

## Example Workflow

### Bad Approach (Shortcut-Driven)
```
1. See 24 TypeScript errors
2. Add @ts-ignore to all of them
3. Hope tests pass
4. Move on
```

### Good Approach (Thoroughness-Driven)
```
1. List all 24 errors systematically
2. Group by error type (7 missing types, 10 unknown casts, 7 property access)
3. Find root causes:
   - Missing @types/tar package
   - No type assertions on fetch responses
   - Implicit any types in callbacks
4. Fix by category:
   - Install @types/tar (fixes 7 errors)
   - Add proper type assertions to registry-client.ts (fixes 10 errors)
   - Add explicit parameter types (fixes 7 errors)
5. Test after each category
6. Run full test suite
7. Document what was learned
```

## Time Investment
- Initial: 2-3x slower than shortcuts
- Long-term: 10x faster (no debugging later, no rework)
- Quality: Near-perfect first time
- Maintenance: Minimal

## Success Metrics
- ✅ 100% of tests passing
- ✅ Zero warnings in production build
- ✅ All code has test coverage
- ✅ Documentation is complete and accurate
- ✅ No known issues or TODOs left behind
- ✅ Future developers can understand the code

## Mantras
- "Slow is smooth, smooth is fast"
- "Do it right the first time"
- "Test everything, assume nothing"
- "Document for your future self"
- "Root causes, not symptoms"
