# Claude Code 集成

The Agency 专为 Claude Code 构建。无需转换 — Agent 以现有的 `.md` + YAML frontmatter 格式原生运行。

## 安装

```bash
# 将所有 Agent 复制到你的 Claude Code agents 目录
./scripts/install.sh --tool claude-code

# 或手动复制某个分类
cp engineering/*.md ~/.claude/agents/
```

## 激活 Agent

在任何 Claude Code 会话中，通过名称引用 Agent：

```
激活 Frontend Developer 并帮我构建一个 React 组件。
```

```
使用 Reality Checker agent 来验证此功能是否已准备好上线。
```

## Agent 目录

Agent 按部门组织。完整名单请参阅 [主 README](../../README_zh.md)，共 61 位专家。
