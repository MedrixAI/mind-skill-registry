---
name: devops
description: Deploy to Cloudflare (Workers, R2, D1), Docker, GCP (Cloud Run, GKE),
  Kubernetes (kubectl, Helm). Use for serverless, containers, CI/CD, GitOps, security
  audit.
license: NOASSERTION
version: 2.0.0
metadata:
  mind.id: ai.medrix.skill.devops
  mind.distribution: marketplace
  mind.market-primary: development-tools
  mind.market-categories: '["development-tools"]'
  mind.marketplace-summary: devops
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Deploy to Cloudflare (Workers, R2, D1), Docker, GCP (Cloud Run, GKE), Kubernetes (kubectl, Helm). Use for serverless, containers, CI/CD, GitOps, security audit.","starter_prompts":["Help me with devops. Start by asking for the repository or system context, environment, constraints, and acceptance criteria, then implement or configure the solution.","Use devops to diagnose the issue I provide, identify the root cause, make the smallest safe fix, and explain how to verify it.","Review my current devops approach for correctness, security, and maintainability, then return prioritized improvements and validation steps."]},"zh-CN":{"description":"部署和管理 Cloudflare Workers、R2、D1、Docker、GCP Cloud Run、GKE 与 Kubernetes。适用于无服务器、容器、CI/CD、GitOps 和安全审计。","starter_prompts":["请帮我完成devops。先询问仓库或系统上下文、运行环境、约束和验收标准，然后实施或配置解决方案。","请使用devops诊断我提供的问题，定位根因，完成最小且安全的修复，并说明如何验证。","请从正确性、安全性和可维护性角度审查我当前的devops方案，并给出按优先级排序的改进和验证步骤。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/mrgoonie/claudekit-skills
  mind.upstream.commit: 80113d86bc4407f105af40a2c4ea58194f7c370a
  mind.upstream.license: NOASSERTION
  mind.upstream.path: .claude/skills/devops/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/mrgoonie/claudekit-skills/80113d86bc4407f105af40a2c4ea58194f7c370a/.claude/skills/devops/SKILL.md"]'
---

# DevOps Skill

Deploy and manage cloud infrastructure across Cloudflare, Docker, Google Cloud, and Kubernetes.

## When to Use

- Deploy serverless apps to Cloudflare Workers/Pages
- Containerize apps with Docker, Docker Compose
- Manage GCP with gcloud CLI (Cloud Run, GKE, Cloud SQL)
- Kubernetes cluster management (kubectl, Helm)
- GitOps workflows (Argo CD, Flux)
- CI/CD pipelines, multi-region deployments
- Security audits, RBAC, network policies

## Platform Selection

| Need | Choose |
|------|--------|
| Sub-50ms latency globally | Cloudflare Workers |
| Large file storage (zero egress) | Cloudflare R2 |
| SQL database (global reads) | Cloudflare D1 |
| Containerized workloads | Docker + Cloud Run/GKE |
| Enterprise Kubernetes | GKE |
| Managed relational DB | Cloud SQL |
| Static site + API | Cloudflare Pages |
| Container orchestration | Kubernetes |
| Package management for K8s | Helm |

## Quick Start

```bash
# Cloudflare Worker
wrangler init my-worker && cd my-worker && wrangler deploy

# Docker
docker build -t myapp . && docker run -p 3000:3000 myapp

# GCP Cloud Run
gcloud run deploy my-service --image gcr.io/project/image --region us-central1

# Kubernetes
kubectl apply -f manifests/ && kubectl get pods
```

## Reference Navigation

### Cloudflare Platform
- `cloudflare-platform.md` - Edge computing overview
- `cloudflare-workers-basics.md` - Handler types, patterns
- `cloudflare-workers-advanced.md` - Performance, optimization
- `cloudflare-workers-apis.md` - Runtime APIs, bindings
- `cloudflare-r2-storage.md` - Object storage, S3 compatibility
- `cloudflare-d1-kv.md` - D1 SQLite, KV store
- `browser-rendering.md` - Puppeteer automation

### Docker
- `docker-basics.md` - Dockerfile, images, containers
- `docker-compose.md` - Multi-container apps

### Google Cloud
- `gcloud-platform.md` - gcloud CLI, authentication
- `gcloud-services.md` - Compute Engine, GKE, Cloud Run

### Kubernetes
- `kubernetes-basics.md` - Core concepts, architecture, workloads
- `kubernetes-kubectl.md` - Essential commands, debugging workflow
- `kubernetes-helm.md` / `kubernetes-helm-advanced.md` - Helm charts, templates
- `kubernetes-security.md` / `kubernetes-security-advanced.md` - RBAC, secrets
- `kubernetes-workflows.md` / `kubernetes-workflows-advanced.md` - GitOps, CI/CD
- `kubernetes-troubleshooting.md` / `kubernetes-troubleshooting-advanced.md` - Debug

### Scripts
- `scripts/cloudflare-deploy.py` - Automate Worker deployments
- `scripts/docker-optimize.py` - Analyze Dockerfiles

## Best Practices

**Security:** Non-root containers, RBAC, secrets in env vars, image scanning
**Performance:** Multi-stage builds, edge caching, resource limits
**Cost:** R2 for large egress, caching, right-size resources
**Development:** Docker Compose local dev, wrangler dev, version control IaC

## Resources

- Cloudflare: https://developers.cloudflare.com
- Docker: https://docs.docker.com
- GCP: https://cloud.google.com/docs
- Kubernetes: https://kubernetes.io/docs
- Helm: https://helm.sh/docs
