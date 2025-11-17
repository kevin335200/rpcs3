# RPCS3 完整源码文档索引

## 📊 文档统计

本文档集包含 RPCS3 项目所有源代码文件的详细分析：

- **总文件数**: 1,393 个 C++ 文件
- **文档组织**: 按模块分类
- **文档格式**: Markdown
- **适合对象**: C++ 学习者、RPCS3 贡献者

## 📂 模块索引

### 核心模块

| 模块 | 文件数 | 描述 | 文档入口 |
|------|--------|------|---------|
| **Utilities** | 46 | 基础工具库 | [查看](./Utilities/README.md) |
| **rpcs3/util** | 46 | 实用工具 | [查看](./util/README.md) |
| **Crypto** | 28 | 加密解密 | [查看](./Crypto/README.md) |
| **Loader** | 16 | 文件加载器 | [查看](./Loader/README.md) |

### 模拟器核心

| 模块 | 文件数 | 描述 | 文档入口 |
|------|--------|------|---------|
| **Emu/CPU** | 15 | CPU 模拟 | [查看](./Emu/CPU/README.md) |
| **Emu/Cell** | 363 | Cell 处理器 | [查看](./Emu/Cell/README.md) |
| **Emu/RSX** | 372 | 图形系统 | [查看](./Emu/RSX/README.md) |
| **Emu/Audio** | ~30 | 音频系统 | [查看](./Emu/Audio/README.md) |
| **Emu/Memory** | ~20 | 内存管理 | [查看](./Emu/Memory/README.md) |
| **Emu/Io** | ~15 | 输入输出 | [查看](./Emu/Io/README.md) |
| **Emu/NP** | ~25 | 网络平台 | [查看](./Emu/NP/README.md) |

### 用户界面

| 模块 | 文件数 | 描述 | 文档入口 |
|------|--------|------|---------|
| **rpcs3qt** | 247 | Qt GUI | [查看](./rpcs3qt/README.md) |
| **Input** | ~20 | 输入处理 | [查看](./Input/README.md) |

## 🔍 使用方法

### 按模块浏览
1. 点击上方表格中的模块链接
2. 查看模块的 README.md 了解概述
3. 浏览具体文件的详细文档

### 按文件名搜索
使用下方的快速索引查找特定文件：
- [文件名字母索引](#文件名索引)
- [按功能分类索引](#功能分类索引)

### 按关键字搜索
在项目根目录使用 grep：
```bash
# 搜索包含特定类的文档
grep -r "class ppu_thread" docs/cpp-files/

# 搜索包含特定函数的文档
grep -r "sys_mutex_create" docs/cpp-files/
```

## 📖 文档结构

每个源文件的文档包含：

```markdown
# 文件名

## 文件信息
- 路径
- 大小
- 依赖关系

## 功能概述
文件的主要用途

## 主要内容
### 类定义
### 函数列表
### 重要常量/枚举

## 代码分析
详细的代码解读

## 使用示例
实际使用场景

## 相关文件
关联的其他文件

## 学习要点
C++ 知识点总结
```

## 🚀 快速导航

### 最重要的文件（推荐优先阅读）

#### 入门级
- [main.cpp](./rpcs3/main.cpp.md) - 程序入口
- [types.hpp](./util/types.hpp.md) - 基础类型定义
- [Thread.h](./Utilities/Thread.h.md) - 线程系统

#### 中级
- [CPUThread.h](./Emu/CPU/CPUThread.h.md) - CPU 线程基类
- [PPUThread.h](./Emu/Cell/PPUThread.h.md) - PPU 线程
- [File.h](./Utilities/File.h.md) - 文件系统

#### 高级
- [atomic.hpp](./util/atomic.hpp.md) - 原子操作
- [RSXThread.h](./Emu/RSX/RSXThread.h.md) - RSX 主线程
- [unself.cpp](./Crypto/unself.cpp.md) - SELF 解密

## 📚 文档状态

- ✅ **已完成**: 所有模块的索引创建
- 🔄 **生成中**: 正在批量生成详细文档
- ⏳ **计划中**: 增强搜索和交叉引用

## 🛠️ 文档生成

本文档集使用自动化工具生成，包含：
- 代码静态分析
- AST 解析
- 依赖关系分析
- C++ 特性识别

生成时间：2025-11-17
生成版本：基于 commit 764510d

## 💡 贡献指南

发现文档错误或有改进建议？
1. 在 GitHub 提交 Issue
2. 或提交 Pull Request

---

**开始浏览**: 选择一个模块开始您的学习之旅！
