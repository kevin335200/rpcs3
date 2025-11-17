# fence.hpp

## 文件信息
- **路径**: /home/user/rpcs3/rpcs3/util/fence.hpp
- **类型**: 头文件
- **行数**: 29行

## 功能概述
提供低级内存栅栏操作，用于同步和内存可见性保证。

## 主要内容

### 核心函数
- `utils::lfence()`: 加载栅栏
  - x86: `_mm_lfence()` 或 `__builtin_ia32_lfence()`
  - ARM64: `isb` 指令

## 学习要点

### 架构特定指令
- x86: SSE指令
- ARM64: 内存屏障指令
