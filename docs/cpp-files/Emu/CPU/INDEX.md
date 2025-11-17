# RPCS3 Emu/CPU 模块 - 文件索引

## 快速导航

### 核心文件 (6个)

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [CPUThread.h](./CPUThread.h.md) | 头文件 | CPU线程基类定义（314行） |
| [CPUThread.cpp](./CPUThread.cpp.md) | 源文件 | CPU线程实现、状态管理、分析器（1750行） |
| [CPUTranslator.h](./CPUTranslator.h.md) | 头文件 | LLVM JIT编译框架（3200+行） |
| [CPUTranslator.cpp](./CPUTranslator.cpp.md) | 源文件 | LLVM集成、特性检测、转换管道（518行） |
| [CPUDisAsm.h](./CPUDisAsm.h.md) | 头文件 | 反汇编接口定义（150行） |
| [Hypervisor.h](./Hypervisor.h.md) | 头文件 | 超级管理程序上下文（47行） |

### SIMD 转换库

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [sse2neon.h](./sse2neon.h.md) | 头文件 | x86 SSE → ARM NEON 转换（2000行） |

### ARM64 后端 (8个)

#### 核心定义

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md) | 头文件 | ARM64寄存器定义（43行） |
| [AArch64Common.cpp](./Backends/AArch64/AArch64Common.cpp.md) | 源文件 | ARM64通用功能实现 |

#### 微汇编器

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [AArch64ASM.h](./Backends/AArch64/AArch64ASM.h.md) | 头文件 | ARM64微汇编器接口（100行） |
| [AArch64ASM.cpp](./Backends/AArch64/AArch64ASM.cpp.md) | 源文件 | ARM64汇编实现（600行） |

#### JIT编译器

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [AArch64JIT.h](./Backends/AArch64/AArch64JIT.h.md) | 头文件 | ARM64 JIT编译器、GHC栈管理（90行） |
| [AArch64JIT.cpp](./Backends/AArch64/AArch64JIT.cpp.md) | 源文件 | ARM64 JIT实现、栈帧管理（2000行） |

#### 信号处理

| 文件名 | 类型 | 描述 |
|--------|------|------|
| [AArch64Signal.h](./Backends/AArch64/AArch64Signal.h.md) | 头文件 | ARM64信号处理接口 |
| [AArch64Signal.cpp](./Backends/AArch64/AArch64Signal.cpp.md) | 源文件 | ARM64信号处理实现（700行） |

---

## 按功能分类

### 线程管理
- [CPUThread.h](./CPUThread.h.md) - 线程基类
- [CPUThread.cpp](./CPUThread.cpp.md) - 线程实现

### JIT 编译
- [CPUTranslator.h](./CPUTranslator.h.md) - LLVM框架
- [CPUTranslator.cpp](./CPUTranslator.cpp.md) - LLVM实现
- [AArch64JIT.h](./Backends/AArch64/AArch64JIT.h.md) - ARM64 JIT
- [AArch64JIT.cpp](./Backends/AArch64/AArch64JIT.cpp.md) - ARM64 JIT实现

### 汇编生成
- [AArch64ASM.h](./Backends/AArch64/AArch64ASM.h.md) - 微汇编器
- [AArch64ASM.cpp](./Backends/AArch64/AArch64ASM.cpp.md) - 汇编实现

### 寄存器管理
- [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md) - 寄存器定义
- [AArch64Common.cpp](./Backends/AArch64/AArch64Common.cpp.md) - 寄存器实现

### 异常处理
- [AArch64Signal.h](./Backends/AArch64/AArch64Signal.h.md) - 信号处理接口
- [AArch64Signal.cpp](./Backends/AArch64/AArch64Signal.cpp.md) - 信号处理实现

### 调试和反汇编
- [CPUDisAsm.h](./CPUDisAsm.h.md) - 反汇编接口

### SIMD 跨平台
- [sse2neon.h](./sse2neon.h.md) - SSE到NEON转换

### 虚拟机管理
- [Hypervisor.h](./Hypervisor.h.md) - 超级管理程序上下文

---

## 按复杂度排序

### 简单 (100-300行)
1. [Hypervisor.h](./Hypervisor.h.md) - 47行
2. [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md) - 43行
3. [CPUDisAsm.h](./CPUDisAsm.h.md) - 150行
4. [AArch64ASM.h](./Backends/AArch64/AArch64ASM.h.md) - 100行

### 中等 (300-800行)
1. [CPUTranslator.cpp](./CPUTranslator.cpp.md) - 518行
2. [AArch64Common.cpp](./Backends/AArch64/AArch64Common.cpp.md) - 变量
3. [CPUThread.h](./CPUThread.h.md) - 314行
4. [AArch64ASM.cpp](./Backends/AArch64/AArch64ASM.cpp.md) - 600行
5. [AArch64Signal.cpp](./Backends/AArch64/AArch64Signal.cpp.md) - 700行

### 复杂 (1000+行)
1. [CPUThread.cpp](./CPUThread.cpp.md) - 1750行
2. [AArch64JIT.cpp](./Backends/AArch64/AArch64JIT.cpp.md) - 2000行
3. [CPUTranslator.h](./CPUTranslator.h.md) - 3200+行
4. [sse2neon.h](./sse2neon.h.md) - 2000行

---

## 核心概念速查表

### 线程状态标志
- `stop`: 线程未运行
- `exit`: 不可逆退出
- `suspend`: 线程挂起
- `wait`: 等待状态
- `dbg_pause`: 调试暂停

详见: [CPUThread.h](./CPUThread.h.md)

### ARM64 寄存器
- **x0-x7**: 参数/返回值
- **x19-x28**: 被调用者保存
- **x29**: 帧指针(FP)
- **x30**: 链接寄存器(LR)

详见: [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md)

### JIT 编译流程
1. CPU 指令 → LLVM IR
2. 特性检测 → 优化选择
3. 内在函数替换
4. 转换管道 (ARM64JIT等)
5. LLVM 优化
6. 本地代码生成

详见: [CPUTranslator.h](./CPUTranslator.h.md)

### 全局挂起 (suspend_all)
1. 设置 pause 标志
2. 等待 wait 确认
3. 执行待处理工作
4. 清除 pause 标志

详见: [CPUThread.cpp](./CPUThread.cpp.md)

---

## 推荐学习路径

### 初级（理解基础）
1. 读 [Hypervisor.h](./Hypervisor.h.md) - 理解上下文结构
2. 读 [CPUThread.h](./CPUThread.h.md) - 理解线程模型
3. 读 [CPUDisAsm.h](./CPUDisAsm.h.md) - 理解反汇编

### 中级（学习线程管理）
4. 读 [CPUThread.cpp](./CPUThread.cpp.md) - 学习状态检查和挂起
5. 读 [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md) - 学习寄存器定义

### 高级（深入 JIT 编译）
6. 读 [CPUTranslator.h](./CPUTranslator.h.md) - 理解 LLVM 框架
7. 读 [CPUTranslator.cpp](./CPUTranslator.cpp.md) - 学习特性检测
8. 读 [AArch64JIT.h](./Backends/AArch64/AArch64JIT.h.md) - 理解 GHC 栈管理
9. 读 [AArch64JIT.cpp](./Backends/AArch64/AArch64JIT.cpp.md) - 学习栈帧生成

### 专项（特定技术）
- **汇编**: [AArch64ASM.h](./Backends/AArch64/AArch64ASM.h.md) → [AArch64ASM.cpp](./Backends/AArch64/AArch64ASM.cpp.md)
- **信号处理**: [AArch64Signal.h](./Backends/AArch64/AArch64Signal.h.md) → [AArch64Signal.cpp](./Backends/AArch64/AArch64Signal.cpp.md)
- **SIMD**: [sse2neon.h](./sse2neon.h.md)

---

## 文件关系图

```
CPUThread.h/cpp (核心)
    ├── CPUTranslator.h/cpp (JIT编译)
    │   ├── AArch64JIT.h/cpp
    │   │   ├── AArch64ASM.h/cpp
    │   │   └── AArch64Signal.h/cpp
    │   └── sse2neon.h
    ├── CPUDisAsm.h (反汇编)
    └── Hypervisor.h (上下文)
        └── AArch64Common.h/cpp (寄存器)
```

---

## 统计信息

### 总行数: ~10,000+行

| 分类 | 文件数 | 行数 | 平均每文件 |
|------|--------|------|-----------|
| 头文件 | 8 | ~3,800 | 475 |
| 源文件 | 8 | ~6,200+ | 775+ |
| 总计 | 16 | ~10,000+ | 625 |

### 按功能分布

| 功能 | 文件数 | 行数 |
|------|--------|------|
| 线程管理 | 2 | ~2,064 |
| JIT编译 | 4 | ~5,718 |
| 汇编生成 | 2 | ~700 |
| SIMD转换 | 1 | ~2,000 |
| 其他 | 7 | ~518 |

---

## 最后更新

- **日期**: 2025-11-17
- **版本**: 1.0
- **文档格式**: Markdown
- **总文档数**: 16个

