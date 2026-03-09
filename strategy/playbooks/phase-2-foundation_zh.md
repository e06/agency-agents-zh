# ⚙️ 第2阶段手册 — 基础与脚手架

> **周期**：3-5天 | **智能体**：6个 | **关卡守护者**：DevOps自动化工程师 + 证据收集员

---

## 目标

构建所有后续工作所依赖的技术和运营基础。在添加肌肉之前先让骨架站立起来。此阶段完成后，每位开发者都拥有可工作的环境、可部署的流水线，以及可用的设计系统。

## 前置条件

- [ ] 第1阶段质量关卡已通过（架构方案已批准）
- [ ] 第1阶段交接包已接收
- [ ] 所有架构文档已最终确定

## 智能体激活序列

### 工作流A：基础设施（第1-3天，并行）

#### 🚀 DevOps自动化工程师 — CI/CD流水线 + 基础设施
```
Activate DevOps Automator for infrastructure setup on [PROJECT].

Input: Backend Architect system architecture + deployment requirements
Deliverables required:
1. CI/CD Pipeline (GitHub Actions / GitLab CI)
   - Security scanning stage
   - Automated testing stage
   - Build and containerization stage
   - Deployment stage (blue-green or canary)
   - Automated rollback capability
2. Infrastructure as Code
   - Environment provisioning (dev, staging, production)
   - Container orchestration setup
   - Network and security configuration
3. Environment Configuration
   - Secrets management
   - Environment variable management
   - Multi-environment parity

Files to create:
- .github/workflows/ci-cd.yml (or equivalent)
- infrastructure/ (Terraform/CDK templates)
- docker-compose.yml
- Dockerfile(s)

Format: Working CI/CD pipeline with IaC templates
Timeline: 3 days
```

#### 🏗️ 基础设施维护员 — 云基础设施 + 监控
```
Activate Infrastructure Maintainer for monitoring setup on [PROJECT].

Input: DevOps Automator infrastructure + Backend Architect architecture
Deliverables required:
1. Cloud Resource Provisioning
   - Compute, storage, networking resources
   - Auto-scaling configuration
   - Load balancer setup
2. Monitoring Stack
   - Application metrics (Prometheus/DataDog)
   - Infrastructure metrics
   - Custom dashboards (Grafana)
3. Logging and Alerting
   - Centralized log aggregation
   - Alert rules for critical thresholds
   - On-call notification setup
4. Security Hardening
   - Firewall rules
   - SSL/TLS configuration
   - Access control policies

Format: Infrastructure Readiness Report with dashboard access
Timeline: 3 days
```

#### ⚙️ 工作室运营 — 流程设置
```
Activate Studio Operations for process setup on [PROJECT].

Input: Sprint Prioritizer plan + Project Shepherd coordination needs
Deliverables required:
1. Git Workflow
   - Branch strategy (GitFlow / trunk-based)
   - PR review process
   - Merge policies
2. Communication Channels
   - Team channels setup
   - Notification routing
   - Status update cadence
3. Documentation Templates
   - PR template
   - Issue template
   - Decision log template
4. Collaboration Tools
   - Project board setup
   - Sprint tracking configuration

Format: Operations Playbook
Timeline: 2 days
```

### 工作流B：应用基础（第1-4天，并行）

#### 🎨 前端开发者 — 项目脚手架 + 组件库
```
Activate Frontend Developer for project scaffolding on [PROJECT].

Input: UX Architect CSS Design System + Brand Guardian identity
Deliverables required:
1. Project Scaffolding
   - Framework setup (React/Vue/Angular per architecture)
   - TypeScript configuration
   - Build tooling (Vite/Webpack/Next.js)
   - Testing framework (Jest/Vitest + Testing Library)
2. Design System Implementation
   - CSS design tokens from UX Architect
   - Base component library (Button, Input, Card, Layout)
   - Theme system (light/dark/system toggle)
   - Responsive utilities
3. Application Shell
   - Routing setup
   - Layout components (Header, Footer, Sidebar)
   - Error boundary implementation
   - Loading states

Files to create:
- src/ (application source)
- src/components/ (component library)
- src/styles/ (design tokens)
- src/layouts/ (layout components)

Format: Working application skeleton with component library
Timeline: 3 days
```

#### 🏗️ 后端架构师 — 数据库 + API基础
```
Activate Backend Architect for API foundation on [PROJECT].

Input: System Architecture Specification + Database Schema Design
Deliverables required:
1. Database Setup
   - Schema deployment (migrations)
   - Index creation
   - Seed data for development
   - Connection pooling configuration
2. API Scaffold
   - Framework setup (Express/FastAPI/etc.)
   - Route structure matching architecture
   - Middleware stack (auth, validation, error handling, CORS)
   - Health check endpoints
3. Authentication System
   - Auth provider integration
   - JWT/session management
   - Role-based access control scaffold
4. Service Communication
   - API versioning setup
   - Request/response serialization
   - Error response standardization

Files to create:
- api/ or server/ (backend source)
- migrations/ (database migrations)
- docs/api-spec.yaml (OpenAPI specification)

Format: Working API scaffold with database and auth
Timeline: 4 days
```

#### 🏛️ UX架构师 — CSS系统实现
```
Activate UX Architect for CSS system implementation on [PROJECT].

Input: Brand Guardian identity + own Phase 1 CSS Design System spec
Deliverables required:
1. Design Tokens Implementation
   - CSS custom properties (colors, typography, spacing)
   - Brand color palette with semantic naming
   - Typography scale with responsive adjustments
2. Layout System
   - Container system (responsive breakpoints)
   - Grid patterns (2-col, 3-col, sidebar)
   - Flexbox utilities
3. Theme System
   - Light theme variables
   - Dark theme variables
   - System preference detection
   - Theme toggle component
   - Smooth transition between themes

Files to create/update:
- css/design-system.css (or equivalent in framework)
- css/layout.css
- css/components.css
- js/theme-manager.js

Format: Implemented CSS design system with theme toggle
Timeline: 2 days
```

## 验证检查点（第4-5天）

### 证据收集员验证
```
Activate Evidence Collector for Phase 2 foundation verification.

Verify the following with screenshot evidence:
1. CI/CD pipeline executes successfully (show pipeline logs)
2. Application skeleton loads in browser (desktop screenshot)
3. Application skeleton loads on mobile (mobile screenshot)
4. Theme toggle works (light + dark screenshots)
5. API health check responds (curl output)
6. Database is accessible (migration status)
7. Monitoring dashboards are active (dashboard screenshot)
8. Component library renders (component demo page)

Format: Evidence Package with screenshots
Verdict: PASS / FAIL with specific issues
```

## 质量关卡检查表

| # | 标准 | 证据来源 | 状态 |
|---|-----------|----------------|--------|
| 1 | CI/CD流水线构建、测试并部署 | 流水线执行日志 | ☐ |
| 2 | 数据库架构已部署所有表/索引 | 迁移成功输出 | ☐ |
| 3 | API脚手架健康检查响应 | curl响应证据 | ☐ |
| 4 | 前端骨架在浏览器中渲染 | 证据收集员截图 | ☐ |
| 5 | 监控仪表板显示指标 | 仪表板截图 | ☐ |
| 6 | 设计系统令牌已实现 | 组件库演示 | ☐ |
| 7 | 主题切换功能正常（浅色/深色/系统） | 前后截图对比 | ☐ |
| 8 | Git工作流程和流程已文档化 | 工作室运营手册 | ☐ |

## 关卡决策

**需要双重签核**：DevOps自动化工程师（基础设施）+ 证据收集员（视觉）

- **通过**：骨架应用正常运行，完整的DevOps流水线 → 激活第3阶段
- **失败**：存在特定的基础设施或应用问题 → 修复并重新验证

## 交接至第3阶段

```markdown
## Phase 2 → Phase 3 Handoff Package

### For all Developer Agents:
- Working CI/CD pipeline (auto-deploys on merge)
- Design system tokens and component library
- API scaffold with auth and health checks
- Database with schema and seed data
- Git workflow and PR process

### For Evidence Collector (ongoing QA):
- Application URLs (dev, staging)
- Screenshot capture methodology
- Component library reference
- Brand guidelines for visual verification

### For Agents Orchestrator (Dev↔QA loop management):
- Sprint Prioritizer backlog (from Phase 1)
- Task list with acceptance criteria (from Phase 1)
- Agent assignment matrix (from NEXUS strategy)
- Quality thresholds for each task type

### Environment Access:
- Dev environment: [URL]
- Staging environment: [URL]
- Monitoring dashboard: [URL]
- CI/CD pipeline: [URL]
- API documentation: [URL]
```

---

*当骨架应用运行中、CI/CD流水线可操作、且证据收集员已通过截图验证所有基础元素时，第2阶段即完成。*
