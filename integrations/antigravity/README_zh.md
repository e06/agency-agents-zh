# Antigravity 集成

将全部 61 个 Agency 代理安装为 Antigravity 技能。每个代理都以 `agency-` 为前缀，以避免与现有技能冲突。

## 安装

```bash
./scripts/install.sh --tool antigravity
```

此命令会将 `integrations/antigravity/` 中的文件复制到 `~/.gemini/antigravity/skills/`。

## 激活技能

在 Antigravity 中，通过别名激活代理：

```
Use the agency-frontend-developer skill to review this component.
```

可用的别名遵循 `agency-<agent-name>` 的命名模式，例如：
- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-reality-checker`
- `agency-growth-hacker`

## 重新生成

修改代理后，重新生成技能文件：

```bash
./scripts/convert.sh --tool antigravity
```

## 文件格式

每个技能都是一个包含 Antigravity 兼容前置元数据的 `SKILL.md` 文件：

```yaml
---
name: agency-frontend-developer
description: Expert frontend developer specializing in...
risk: low
source: community
date_added: '2026-03-08'
---
```
