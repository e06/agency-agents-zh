#!/usr/bin/env python3
"""
项目文档翻译脚本
递归遍历目录下的 .md 文档，使用 iflow SDK 翻译成中文
"""

import asyncio
import os
from pathlib import Path
from iflow_sdk import query, IFlowOptions, ApprovalMode


def should_ignore_file(file_path: Path) -> bool:
    """判断文件是否应该被忽略"""
    # 忽略 .ex、.ev、.codebuddy 和 .agents 目录下的文件
    if ".e" in file_path.parts or ".ex" in file_path.parts or ".ev" in file_path.parts or ".codebuddy" in file_path.parts or ".agents" in file_path.parts:
        return True
    
    # 过滤掉 *_zh.md 文件
    if file_path.name.endswith("_zh.md"):
        return True
    
    # 过滤掉 CODEBUDDY.md
    if file_path.name == "CODEBUDDY.md":
        return True
    
    if file_path.name == "CONTRIBUTING.md":
        return True
    
    return False


def get_output_path(input_path: Path) -> Path:
    """根据输入文件路径生成输出文件路径"""
    # 将 .md 替换为 _zh.md
    output_name = input_path.stem + "_zh.md"
    return input_path.parent / output_name


async def translate_file(input_path: Path, output_path: Path) -> bool:
    """翻译单个文件，返回是否成功"""
    print(f"\n{'='*60}")
    print(f"正在翻译: {input_path}")
    print(f"输出到: {output_path}")
    print(f"{'='*60}")
    
    # 构建翻译 prompt
    prompt = f"""将"{input_path}"全文翻译成中文，保存在"{output_path}"中。
尽量保持 markdown 结构。
注意保留所有的代码块，不需要翻译。
"""
    print("---")
    print(prompt)
    print("---")
    # return False

    # 配置选项：使用 YOLO 模式自动执行工具
    options = IFlowOptions(
        approval_mode=ApprovalMode.YOLO,
    )
    
    try:
        # 调用 iflow 进行翻译
        result = await query(prompt=prompt, options=options)
        print(result)
        print()  # 换行
        print(f"✓ 翻译完成: {output_path}")
        return True
    except Exception as e:
        print(f"✗ 翻译失败: {e}")
        return False


async def main():
    """主函数"""
    # 当前工作目录
    base_dir = Path("/workspace/src/agency-agents-zh")
    
    # 递归查找所有 .md 文件
    md_files = sorted(base_dir.rglob("*.md"))
    
    # 统计
    total_files = 0
    translated_files = 0
    skipped_files = 0
    failed_files = 0
    
    print(f"找到 {len(md_files)} 个 .md 文件")
    
    # 翻译文件
    for md_file in md_files:
        # 跳过应该忽略的文件
        if should_ignore_file(md_file):
            continue
        
        total_files += 1
        
        # 获取输出路径
        output_path = get_output_path(md_file)
        
        # 如果输出文件已存在，跳过
        if output_path.exists():
            print(f"跳过已存在的翻译文件: {output_path}")
            skipped_files += 1
            continue
        
        # 翻译文件
        success = await translate_file(md_file, output_path)
        if success:
            translated_files += 1
        else:
            failed_files += 1
    
    # 输出统计
    print(f"\n{'='*60}")
    print("翻译完成!")
    print(f"总计需要翻译: {total_files} 个文件")
    print(f"已翻译: {translated_files} 个文件")
    print(f"已跳过（已存在）: {skipped_files} 个文件")
    print(f"翻译失败: {failed_files} 个文件")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
