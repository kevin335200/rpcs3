# Hypervisor.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Hypervisor.h`
- **类型**: 头文件
- **行数**: ~47行
- **所属模块**: 超级管理程序上下文

## 功能概述

Hypervisor.h 定义了超级管理程序（虚拟机管理层）的上下文结构。该头文件提供了一个平台无关的寄存器上下文联合体，用于在不同 CPU 架构间统一管理线程执行环境。

## 主要内容

### 联合体定义

#### hypervisor_context_t
一个平台特定的联合体，定义了超级管理程序的寄存器上下文。

### 架构特定的实现

#### x86_64 架构 (ARCH_x64)
```cpp
union hypervisor_context_t
{
    u64 regs[1];           // 通用寄存器数组
    struct {
        u64 rsp;           // 栈指针（RSP）
    } x86;
};

static_assert(sizeof(hypervisor_context_t) == 8);
```

**成员说明**:
- **regs[1]**: 通用寄存器数组，目前仅包含 1 个 64 位元素
- **x86.rsp**: x86_64 的栈指针寄存器

**大小**: 8 字节（一个 64 位寄存器）

**设计含义**:
- x86_64 平台上，只需要保存栈指针（RSP）
- 其他寄存器由操作系统或运行时环境管理
- 紧凑的设计减少内存开销

#### ARM64 架构 (ARCH_ARM64 或其他)
```cpp
union alignas(16) hypervisor_context_t
{
    u64 regs[16];          // 通用寄存器数组
    struct {
        u64 pc;            // 程序计数器
        u64 sp;            // 栈指针
        u64 x18 - x30;     // 通用寄存器 x18-x30（13个）
    } aarch64;
};
```

**成员说明**:
- **regs[16]**: 16 个 64 位寄存器
- **aarch64.pc**: ARM64 程序计数器
- **aarch64.sp**: ARM64 栈指针
- **aarch64.x18-x30**: ARM64 通用寄存器
  - x18-x28: 系统保留/通用（10个）
  - x29: 帧指针（FP）
  - x30: 链接寄存器（LR）

**对齐**: 16 字节（支持 SIMD 操作）

**寄存器映射**:
```
regs[0]  -> pc       (程序计数器)
regs[1]  -> sp       (栈指针)
regs[2]  -> x18
regs[3]  -> x19
...
regs[14] -> x29 (FP)
regs[15] -> x30 (LR)
```

## 代码分析

### 平台适配策略

**条件编译**:
```cpp
#if defined(ARCH_x64)
    // x86_64 实现
#else
    // ARM64 实现
#endif
```

### 设计特点

1. **联合体设计**:
   - 支持两种访问方式：数组方式和结构体方式
   - 数组方式便于通用遍历
   - 结构体方式提供有语义的字段名

2. **最小化上下文**:
   - x86_64: 仅 8 字节（RSP）
   - ARM64: 16 字节（考虑 SIMD 对齐）
   - 只保存必要的寄存器状态

3. **架构差异**:
   - x86_64: 栈操作隐含在指令中，只需保存 RSP
   - ARM64: 显式的 PC 和 SP，需要更多寄存器保存

### 使用场景

1. **线程上下文切换**:
   - 保存/恢复超级管理程序层的寄存器状态
   - 在虚拟机和宿主机间切换

2. **虚拟机启动**:
   - 初始化线程的执行上下文
   - 设置初始 PC、SP 等寄存器

3. **调试器集成**:
   - 提供统一的寄存器视图
   - 支持跨平台的调试信息

4. **保存点/恢复**:
   - 在模拟状态保存时记录上下文
   - 在加载状态时恢复上下文

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h` - ARM64 CPU 定义
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64JIT.h` - ARM64 JIT 编译器
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.h` - CPU 线程定义
- `/home/user/rpcs3/rpcs3/util/types.hpp` - 基本类型定义

## 学习要点

1. **平台适配**: 如何在单一代码库中支持多个 CPU 架构
2. **联合体应用**: 使用 C++ 联合体同时提供多种访问方式
3. **寄存器管理**: 虚拟机中必需和可选寄存器的区分
4. **对齐要求**: SIMD 操作对数据对齐的要求
5. **最小化设计**: 在满足功能要求下最小化内存占用
6. **条件编译**: 使用 C 预处理器实现平台特定的编译

## 扩展阅读

- ARM64 寄存器约定（Procedure Call Standard）
- x86_64 ABI 寄存器使用约定
- 虚拟机的上下文切换实现
- GHC（Glasgow Haskell Compiler）的栈管理模型
