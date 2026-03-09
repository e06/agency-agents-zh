# Cursor 集成

将全部 61 个 Agency 代理转换为 Cursor `.mdc` 规则文件。规则是**项目级作用域**——从你的项目根目录安装。

## 安装

```bash
# 从你的项目根目录运行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

这将在你的项目中创建 `.cursor/rules/<agent-slug>.mdc` 文件。

## 激活规则

在 Cursor 中，在你的提示词中引用代理：

```
@frontend-developer 审查这个 React 组件的性能问题。
```

或者通过编辑规则的前言配置将其启用为始终启用：

```yaml
---
description: Expert frontend developer...
globs: "**/*.tsx,**/*.ts"
alwaysApply: true
---
```

## 重新生成

```bash
./scripts/convert.sh --tool cursor
```
