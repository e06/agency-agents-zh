# ⚡ NEXUS 快速入门指南

> **在 5 分钟内从零开始构建编排好的多智能体流水线。**

---

## 什么是 NEXUS？

**NEXUS**（专家网络，战略统一，Network of EXperts, Unified in Strategy）将 Agency 的 AI 专家转化为协调一致的流水线。与其逐一激活智能体并期待它们协同工作，NEXUS 明确定义了谁做什么、何时做，以及如何在每一步验证质量。

## 选择你的模式

| 我想要... | 使用 | 智能体数量 | 时间 |
|-------------|-----|--------|------|
| 从零开始构建完整产品 | **NEXUS-Full** | 全部 | 12-24 周 |
| 构建一个功能或 MVP | **NEXUS-Sprint** | 15-25 | 2-6 周 |
| 执行特定任务（修复 bug、营销活动、审计） | **NEXUS-Micro** | 5-10 | 1-5 天 |

---

## 🚀 NEXUS-Full：启动完整项目

**复制此提示词以激活完整流水线：**

```
Activate Agents Orchestrator in NEXUS-Full mode.

Project: [YOUR PROJECT NAME]
Specification: [DESCRIBE YOUR PROJECT OR LINK TO SPEC]

Execute the complete NEXUS pipeline:
- Phase 0: Discovery (Trend Researcher, Feedback Synthesizer, UX Researcher, Analytics Reporter, Legal Compliance Checker, Tool Evaluator)
- Phase 1: Strategy (Studio Producer, Senior Project Manager, Sprint Prioritizer, UX Architect, Brand Guardian, Backend Architect, Finance Tracker)
- Phase 2: Foundation (DevOps Automator, Frontend Developer, Backend Architect, UX Architect, Infrastructure Maintainer)
- Phase 3: Build (Dev↔QA loops — all engineering + Evidence Collector)
- Phase 4: Harden (Reality Checker, Performance Benchmarker, API Tester, Legal Compliance Checker)
- Phase 5: Launch (Growth Hacker, Content Creator, all marketing agents, DevOps Automator)
- Phase 6: Operate (Analytics Reporter, Infrastructure Maintainer, Support Responder, ongoing)

Quality gates between every phase. Evidence required for all assessments.
Maximum 3 retries per task before escalation.
```

---

## 🏃 NEXUS-Sprint：构建功能或 MVP

**复制此提示词：**

```
Activate Agents Orchestrator in NEXUS-Sprint mode.

Feature/MVP: [DESCRIBE WHAT YOU'RE BUILDING]
Timeline: [TARGET WEEKS]
Skip Phase 0 (market already validated).

Sprint team:
- PM: Senior Project Manager, Sprint Prioritizer
- Design: UX Architect, Brand Guardian
- Engineering: Frontend Developer, Backend Architect, DevOps Automator
- QA: Evidence Collector, Reality Checker, API Tester
- Support: Analytics Reporter

Begin at Phase 1 with architecture and sprint planning.
Run Dev↔QA loops for all implementation tasks.
Reality Checker approval required before launch.
```

---

## 🎯 NEXUS-Micro：执行特定任务

**选择你的场景并复制提示词：**

### 修复 Bug
```
Activate Backend Architect to investigate and fix [BUG DESCRIPTION].
After fix, activate API Tester to verify the fix.
Then activate Evidence Collector to confirm no visual regressions.
```

### 运行营销活动
```
Activate Social Media Strategist as campaign lead for [CAMPAIGN DESCRIPTION].
Team: Content Creator, Twitter Engager, Instagram Curator, Reddit Community Builder.
Brand Guardian reviews all content before publishing.
Analytics Reporter tracks performance daily.
Growth Hacker optimizes channels weekly.
```

### 进行合规审计
```
Activate Legal Compliance Checker for comprehensive compliance audit.
Scope: [GDPR / CCPA / HIPAA / ALL]
After audit, activate Executive Summary Generator to create stakeholder report.
```

### 调查性能问题
```
Activate Performance Benchmarker to diagnose performance issues.
Scope: [API response times / Page load / Database queries / All]
After diagnosis, activate Infrastructure Maintainer for optimization.
DevOps Automator deploys any infrastructure changes.
```

### 市场研究
```
Activate Trend Researcher for market intelligence on [DOMAIN].
Deliverables: Competitive landscape, market sizing, trend forecast.
After research, activate Executive Summary Generator for executive brief.
```

### UX 改进
```
Activate UX Researcher to identify usability issues in [FEATURE/PRODUCT].
After research, activate UX Architect to design improvements.
Frontend Developer implements changes.
Evidence Collector verifies improvements.
```

---

## 📁 策略文档

| 文档 | 用途 | 位置 |
|----------|---------|----------|
| **主策略** | 完整的 NEXUS 原则 | `strategy/nexus-strategy.md` |
| **阶段 0 手册** | 发现与情报 | `strategy/playbooks/phase-0-discovery.md` |
| **阶段 1 手册** | 策略与架构 | `strategy/playbooks/phase-1-strategy.md` |
| **阶段 2 手册** | 基础与脚手架 | `strategy/playbooks/phase-2-foundation.md` |
| **阶段 3 手册** | 构建与迭代 | `strategy/playbooks/phase-3-build.md` |
| **阶段 4 手册** | 质量与加固 | `strategy/playbooks/phase-4-hardening.md` |
| **阶段 5 手册** | 发布与增长 | `strategy/playbooks/phase-5-launch.md` |
| **阶段 6 手册** | 运营与演进 | `strategy/playbooks/phase-6-operate.md` |
| **激活提示词** | 即用型智能体提示词 | `strategy/coordination/agent-activation-prompts.md` |
| **交接模板** | 标准化交接格式 | `strategy/coordination/handoff-templates.md` |
| **创业 MVP 运行手册** | 4-6 周 MVP 构建 | `strategy/runbooks/scenario-startup-mvp.md` |
| **企业功能运行手册** | 企业功能开发 | `strategy/runbooks/scenario-enterprise-feature.md` |
| **营销活动运行手册** | 多渠道营销活动 | `strategy/runbooks/scenario-marketing-campaign.md` |
| **事件响应运行手册** | 生产事件处理 | `strategy/runbooks/scenario-incident-response.md` |

---

## 🔑 30 秒核心概念

1. **质量关卡（Quality Gates）** — 没有基于证据的批准，任何阶段都不能推进
2. **Dev↔QA 循环** — 每个任务先构建再测试；通过才继续，失败则重试（最多 3 次）
3. **交接（Handoffs）** — 智能体之间结构化的上下文传递（从不零启动）
4. **Reality Checker** — 最终质量把关者；默认判断为"需要改进"
5. **Agents Orchestrator** — 管理整个流程的流水线控制器
6. **证据胜于声明** — 截图、测试结果和数据——而非断言

---

## 🎭 智能体一览

```
ENGINEERING         │ DESIGN              │ MARKETING
Frontend Developer  │ UI Designer         │ Growth Hacker
Backend Architect   │ UX Researcher       │ Content Creator
Mobile App Builder  │ UX Architect        │ Twitter Engager
AI Engineer         │ Brand Guardian      │ TikTok Strategist
DevOps Automator    │ Visual Storyteller  │ Instagram Curator
Rapid Prototyper    │ Whimsy Injector     │ Reddit Community Builder
Senior Developer    │ Image Prompt Eng.   │ App Store Optimizer
                    │                     │ Social Media Strategist
────────────────────┼─────────────────────┼──────────────────────
PRODUCT             │ PROJECT MGMT        │ TESTING
Sprint Prioritizer  │ Studio Producer     │ Evidence Collector
Trend Researcher    │ Project Shepherd    │ Reality Checker
Feedback Synthesizer│ Studio Operations   │ Test Results Analyzer
                    │ Experiment Tracker  │ Performance Benchmarker
                    │ Senior Project Mgr  │ API Tester
                    │                     │ Tool Evaluator
                    │                     │ Workflow Optimizer
────────────────────┼─────────────────────┼──────────────────────
SUPPORT             │ SPATIAL             │ SPECIALIZED
Support Responder   │ XR Interface Arch.  │ Agents Orchestrator
Analytics Reporter  │ macOS Spatial/Metal │ Data Analytics Reporter
Finance Tracker     │ XR Immersive Dev    │ LSP/Index Engineer
Infra Maintainer    │ XR Cockpit Spec.    │ Sales Data Extraction
Legal Compliance    │ visionOS Spatial    │ Data Consolidation
Exec Summary Gen.   │ Terminal Integration│ Report Distribution
```

---

<div align="center">

**选择一个模式。遵循手册。信任流水线。**

`strategy/nexus-strategy.md` — 完整原则

</div>
