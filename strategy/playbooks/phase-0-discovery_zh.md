# 🔍 第0阶段手册 — 情报与发现

> **周期**：3-7天 | **智能体数量**：6 | **把关人**：执行摘要生成器

---

## 目标

在投入资源之前验证机会。在理解问题、市场和监管环境之前，不进行构建。

## 前置条件

- [ ] 存在项目简报或初始概念
- [ ] 已确定利益相关者发起人
- [ ] 已批准发现阶段预算

## 智能体激活序列

### 第一波：并行启动（第1天）

#### 🔍 趋势研究员 — 市场情报负责人
```
Activate Trend Researcher for market intelligence on [PROJECT DOMAIN].

Deliverables required:
1. Competitive landscape analysis (direct + indirect competitors)
2. Market sizing: TAM, SAM, SOM with methodology
3. Trend lifecycle mapping: where is this market in the adoption curve?
4. 3-6 month trend forecast with confidence intervals
5. Investment and funding trends in the space

Sources: Minimum 15 unique, verified sources
Format: Strategic Report with executive summary
Timeline: 3 days
```

#### 💬 反馈综合器 — 用户需求分析
```
Activate Feedback Synthesizer for user needs analysis on [PROJECT DOMAIN].

Deliverables required:
1. Multi-channel feedback collection plan (surveys, interviews, reviews, social)
2. Sentiment analysis across existing user touchpoints
3. Pain point identification and prioritization (RICE scored)
4. Feature request analysis with business value estimation
5. Churn risk indicators from feedback patterns

Format: Synthesized Feedback Report with priority matrix
Timeline: 3 days
```

#### 🔍 UX研究员 — 用户行为分析
```
Activate UX Researcher for user behavior analysis on [PROJECT DOMAIN].

Deliverables required:
1. User interview plan (5-10 target users)
2. Persona development (3-5 primary personas)
3. Journey mapping for primary user flows
4. Usability heuristic evaluation of competitor products
5. Behavioral insights with statistical validation

Format: Research Findings Report with personas and journey maps
Timeline: 5 days
```

### 第二波：并行启动（第1天，与第一波独立）

#### 📊 分析报告器 — 数据环境评估
```
Activate Analytics Reporter for data landscape assessment on [PROJECT DOMAIN].

Deliverables required:
1. Existing data source audit (what data is available?)
2. Signal identification (what can we measure?)
3. Baseline metrics establishment
4. Data quality assessment with completeness scoring
5. Analytics infrastructure recommendations

Format: Data Audit Report with signal map
Timeline: 2 days
```

#### ⚖️ 法律合规检查器 — 监管扫描
```
Activate Legal Compliance Checker for regulatory scan on [PROJECT DOMAIN].

Deliverables required:
1. Applicable regulatory frameworks (GDPR, CCPA, HIPAA, etc.)
2. Data handling requirements and constraints
3. Jurisdiction mapping for target markets
4. Compliance risk assessment with severity ratings
5. Blocking vs. manageable compliance issues

Format: Compliance Requirements Matrix
Timeline: 3 days
```

#### 🛠️ 工具评估器 — 技术环境
```
Activate Tool Evaluator for technology landscape assessment on [PROJECT DOMAIN].

Deliverables required:
1. Technology stack assessment for the problem domain
2. Build vs. buy analysis for key components
3. Integration feasibility with existing systems
4. Open source vs. commercial evaluation
5. Technology risk assessment

Format: Tech Stack Assessment with recommendation matrix
Timeline: 2 days
```

## 汇聚点（第5-7天）

所有六个智能体提交报告。执行摘要生成器综合：

```
Activate Executive Summary Generator to synthesize Phase 0 findings.

Input documents:
1. Trend Researcher → Market Analysis Report
2. Feedback Synthesizer → Synthesized Feedback Report
3. UX Researcher → Research Findings Report
4. Analytics Reporter → Data Audit Report
5. Legal Compliance Checker → Compliance Requirements Matrix
6. Tool Evaluator → Tech Stack Assessment

Output: Executive Summary (≤500 words, SCQA format)
Decision required: GO / NO-GO / PIVOT
Include: Quantified market opportunity, validated user needs, regulatory path, technology feasibility
```

## 质量关卡检查清单

| # | 标准 | 证据来源 | 状态 |
|---|-----------|----------------|--------|
| 1 | 市场机会已验证，TAM > 最低可行阈值 | 趋势研究员报告 | ☐ |
| 2 | ≥3个已验证的用户痛点，有数据支持 | 反馈综合器 + UX研究员 | ☐ |
| 3 | 未发现阻塞性合规问题 | 法律合规检查器矩阵 | ☐ |
| 4 | 已确定关键指标和数据源 | 分析报告器审计 | ☐ |
| 5 | 技术栈可行且已评估 | 工具评估器评估 | ☐ |
| 6 | 执行摘要已交付，包含GO/NO-GO建议 | 执行摘要生成器 | ☐ |

## 关卡决策

- **GO（继续）**：进入第1阶段 — 战略与架构
- **NO-GO（不继续）**：归档发现结果，记录经验教训，重新分配资源
- **PIVOT（转型）**：根据发现结果修改范围/方向，重新运行针对性发现

## 移交至第1阶段

```markdown
## Phase 0 → Phase 1 Handoff Package

### Documents to carry forward:
1. Market Analysis Report (Trend Researcher)
2. Synthesized Feedback Report (Feedback Synthesizer)
3. User Personas and Journey Maps (UX Researcher)
4. Data Audit Report (Analytics Reporter)
5. Compliance Requirements Matrix (Legal Compliance Checker)
6. Tech Stack Assessment (Tool Evaluator)
7. Executive Summary with GO decision (Executive Summary Generator)

### Key constraints identified:
- [Regulatory constraints from Legal Compliance Checker]
- [Technical constraints from Tool Evaluator]
- [Market timing constraints from Trend Researcher]

### Priority user needs (for Sprint Prioritizer):
1. [Pain point 1 — from Feedback Synthesizer]
2. [Pain point 2 — from UX Researcher]
3. [Pain point 3 — from Feedback Synthesizer]
```

---

*第0阶段在执行摘要生成器交付GO决策并提供所有六个发现智能体的支持证据后完成。*
