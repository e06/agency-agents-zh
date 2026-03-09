# Aider 集成

所有 61 个 Agency 智能体已整合到一个 `CONVENTIONS.md` 文件中。
当该文件位于您的项目根目录时，Aider 会自动读取它。

## 安装

```bash
# 在项目根目录下运行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

## 激活智能体

在 Aider 会话中，通过名称引用智能体：

```
使用 Frontend Developer 智能体重构此组件。
```

```
应用 Reality Checker 智能体验证是否可上线。
```

## 手动使用

您也可以直接传递约定文件：

```bash
aider --read CONVENTIONS.md
```

## 重新生成

```bash
./scripts/convert.sh --tool aider
```
