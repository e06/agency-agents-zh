# OpenCode 集成

OpenCode 使用与 Claude Code 相同的 Agent 格式 —— 带有 YAML frontmatter 的 `.md` 文件，存储在 `.opencode/agent/` 目录中。技术上不需要转换，但此集成将 Agent 打包到正确的目录结构中，以便开箱即用。

## 安装

```bash
# 在项目根目录下运行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

这将在您的项目目录中创建 `.opencode/agent/<slug>.md` 文件。

## 激活 Agent

在 OpenCode 中，通过名称或描述来引用 Agent：

```
Use the Frontend Developer agent to help build this component.
```

```
Activate the Reality Checker agent and review this PR.
```

您也可以从 OpenCode UI 的 Agent 选择器中选择 Agent。

## Agent 格式

OpenCode Agent 使用与 Claude Code 相同的 frontmatter：

```yaml
---
name: Frontend Developer
description: Expert frontend developer specializing in modern web technologies...
color: cyan
---
```

## 项目级与全局级

`.opencode/agent/` 中的 Agent 是**项目级作用域**。要使它们在所有项目中全局可用，请将它们复制到您的 OpenCode 配置目录：

```bash
mkdir -p ~/.config/opencode/agent
cp integrations/opencode/agent/*.md ~/.config/opencode/agent/
```

## 重新生成

```bash
./scripts/convert.sh --tool opencode
```
