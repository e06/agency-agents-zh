# Windsurf 集成

全部 61 个 Agency 智能体已整合到单个 `.windsurfrules` 文件中。
规则是**项目级别**的——从你的项目根目录安装。

## 安装

```bash
# 从项目根目录运行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

## 激活智能体

在 Windsurf 中，在提示词中引用智能体名称：

```
Use the Frontend Developer agent to build this component.
```

## 重新生成

```bash
./scripts/convert.sh --tool windsurf
```
