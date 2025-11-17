#!/usr/bin/env python3
"""
批量生成 RPCS3 Emu/Cell 模块文档
"""
import os
import re
from pathlib import Path

def count_lines(filepath):
    """统计文件行数"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return len(f.readlines())
    except:
        return 0

def extract_key_info(filepath, content):
    """提取文件关键信息"""
    info = {
        'classes': [],
        'functions': [],
        'syscalls': [],
        'hle_functions': [],
        'structs': [],
        'includes': []
    }

    lines = content.split('\n')

    # 提取类定义
    for line in lines:
        # 类定义
        if re.match(r'^\s*(class|struct)\s+(\w+)', line):
            match = re.match(r'^\s*(class|struct)\s+(\w+)', line)
            if match and not 'template' in line:
                info['classes'].append(match.group(2))

        # 函数定义 (简化版)
        if re.match(r'^\s*(\w+[\w\s\*&:<>,]*)\s+(\w+)\s*\([^)]*\)\s*[{;]?', line):
            if any(keyword in line for keyword in ['void', 'int', 'error_code', 'u32', 's32', 'u64', 's64', 'bool', 'static']):
                match = re.search(r'\s+(\w+)\s*\(', line)
                if match and not line.strip().startswith('//'):
                    func_name = match.group(1)
                    if func_name not in ['if', 'for', 'while', 'switch', 'return']:
                        info['functions'].append(func_name)

        # 系统调用 (sys_*)
        if re.search(r'\bsys_\w+\s*\(', line):
            match = re.search(r'\b(sys_\w+)\s*\(', line)
            if match:
                info['syscalls'].append(match.group(1))

        # HLE 函数 (cell*)
        if re.search(r'\bcell\w+\s*\(', line):
            match = re.search(r'\b(cell\w+)\s*\(', line)
            if match:
                info['hle_functions'].append(match.group(1))

        # #include
        if line.strip().startswith('#include'):
            info['includes'].append(line.strip())

    # 去重
    info['classes'] = list(set(info['classes']))[:10]
    info['functions'] = list(set(info['functions']))[:15]
    info['syscalls'] = list(set(info['syscalls']))[:20]
    info['hle_functions'] = list(set(info['hle_functions']))[:20]

    return info

def get_preview_lines(content, max_lines=80):
    """获取代码预览（前N行，跳过版权）"""
    lines = content.split('\n')
    start = 0

    # 跳过版权声明
    for i, line in enumerate(lines):
        if '#include' in line or 'namespace' in line or 'class' in line:
            start = max(0, i - 2)
            break

    preview_lines = lines[start:start + max_lines]
    return '\n'.join(preview_lines)

def generate_markdown(filepath, source_root, docs_root):
    """生成单个文件的 markdown 文档"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        print(f"  ⚠️  无法读取: {filepath}")
        return None

    # 计算相对路径
    rel_path = os.path.relpath(filepath, source_root)
    filename = os.path.basename(filepath)
    file_type = "头文件" if filepath.endswith('.h') else "源文件"
    line_count = count_lines(filepath)

    # 提取关键信息
    info = extract_key_info(filepath, content)

    # 生成文档路径
    doc_path = os.path.join(docs_root, rel_path.replace('.cpp', '.md').replace('.h', '.md'))
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)

    # 生成 markdown 内容
    md_content = f"""# {filename}

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/{rel_path.replace(os.sep, '/')}`
- **类型**: {file_type}
- **行数**: {line_count:,} 行

## 🎯 功能概述

"""

    # 根据文件类型添加描述
    if 'PPU' in filename:
        md_content += "PowerPC Processing Unit (PPU) 相关实现。"
    elif 'SPU' in filename:
        md_content += "Synergistic Processing Unit (SPU) 相关实现。"
    elif 'sys_' in filename:
        md_content += "PS3 LV2 系统调用实现。"
    elif 'cell' in filename.lower():
        md_content += "PS3 HLE (High-Level Emulation) 模块实现。"
    elif 'MFC' in filename:
        md_content += "Memory Flow Controller (MFC) 实现。"
    else:
        md_content += "Cell Broadband Engine 相关实现。"

    md_content += "\n\n## 📋 主要内容\n\n"

    # 添加类
    if info['classes']:
        md_content += "### 类/结构体\n\n"
        for cls in sorted(info['classes'])[:10]:
            md_content += f"- `{cls}`\n"
        md_content += "\n"

    # 添加系统调用
    if info['syscalls']:
        md_content += "### 系统调用\n\n"
        for syscall in sorted(set(info['syscalls']))[:20]:
            md_content += f"- `{syscall}()`\n"
        md_content += "\n"

    # 添加 HLE 函数
    if info['hle_functions']:
        md_content += "### HLE 函数\n\n"
        for hle in sorted(set(info['hle_functions']))[:20]:
            md_content += f"- `{hle}()`\n"
        md_content += "\n"

    # 添加关键函数
    if info['functions'] and not info['syscalls'] and not info['hle_functions']:
        md_content += "### 关键函数\n\n"
        for func in sorted(set(info['functions']))[:15]:
            md_content += f"- `{func}()`\n"
        md_content += "\n"

    # 代码预览
    preview = get_preview_lines(content, max_lines=80)
    if preview.strip():
        md_content += f"""## 💻 代码片段

```cpp
{preview}
```

"""

    # 相关文件
    if info['includes']:
        md_content += "## 🔗 依赖头文件\n\n"
        for inc in info['includes'][:10]:
            md_content += f"- `{inc}`\n"

    # 写入文件
    try:
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        return doc_path
    except Exception as e:
        print(f"  ❌ 写入失败 {doc_path}: {e}")
        return None

def process_batch(files, source_root, docs_root, batch_name):
    """处理一批文件"""
    print(f"\n{'='*60}")
    print(f"📦 处理批次: {batch_name}")
    print(f"{'='*60}")
    print(f"文件数量: {len(files)}")

    success_count = 0
    for i, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        print(f"  [{i}/{len(files)}] {filename}...", end=' ')

        doc_path = generate_markdown(filepath, source_root, docs_root)
        if doc_path:
            print("✅")
            success_count += 1
        else:
            print("❌")

    print(f"\n✨ 批次完成: {success_count}/{len(files)} 个文件成功生成文档")
    return success_count

def main():
    """主函数"""
    source_root = "/home/user/rpcs3/rpcs3/Emu/Cell"
    docs_root = "/home/user/rpcs3/docs/cpp-files/Emu/Cell"

    print("🚀 开始生成 RPCS3 Emu/Cell 模块文档")
    print(f"源码目录: {source_root}")
    print(f"文档目录: {docs_root}")

    # 获取所有文件
    import glob
    all_files = []
    for ext in ['*.cpp', '*.h']:
        all_files.extend(glob.glob(f"{source_root}/**/{ext}", recursive=True))

    all_files = sorted(all_files)
    print(f"\n总文件数: {len(all_files)}")

    # 分类文件
    root_files = [f for f in all_files if os.path.dirname(f) == source_root]
    lv2_files = [f for f in all_files if '/lv2/' in f]
    modules_files = [f for f in all_files if '/Modules/' in f]

    print(f"  - Cell 根目录: {len(root_files)} 个")
    print(f"  - lv2 目录: {len(lv2_files)} 个")
    print(f"  - Modules 目录: {len(modules_files)} 个")

    total_success = 0

    # 批次 1: Cell 根目录
    if root_files:
        total_success += process_batch(root_files, source_root, docs_root, "Cell 根目录 (PPU/SPU)")

    # 批次 2: lv2 目录 (分两批)
    if lv2_files:
        mid = len(lv2_files) // 2
        total_success += process_batch(lv2_files[:mid], source_root, docs_root, "lv2 系统调用 (第1批)")
        total_success += process_batch(lv2_files[mid:], source_root, docs_root, "lv2 系统调用 (第2批)")

    # 批次 3: Modules 目录 (分4批)
    if modules_files:
        batch_size = len(modules_files) // 4 + 1
        for i in range(4):
            start = i * batch_size
            end = min((i + 1) * batch_size, len(modules_files))
            if start < len(modules_files):
                batch = modules_files[start:end]
                total_success += process_batch(batch, source_root, docs_root, f"HLE Modules (第{i+1}/4批)")

    print(f"\n{'='*60}")
    print(f"🎉 文档生成完成!")
    print(f"{'='*60}")
    print(f"总计: {total_success}/{len(all_files)} 个文件成功生成文档")
    print(f"文档保存在: {docs_root}")

if __name__ == "__main__":
    main()
