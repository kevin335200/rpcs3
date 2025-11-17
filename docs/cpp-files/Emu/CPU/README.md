# RPCS3 Emu/CPU 模块文档

## 概述

RPCS3 Emu/CPU 模块是PS3仿真器的CPU模拟核心。它实现了对Cell处理器（PPU和SPU）以及RSX图形处理器的CPU线程管理和JIT编译。该模块提供了一个统一的线程管理框架和多架构后端支持（x86_64和ARM64）。

## 目录结构

```
Emu/CPU/
├── 核心文件
│   ├── CPUThread.h          - CPU线程基类定义
│   ├── CPUThread.cpp        - CPU线程实现
│   ├── CPUTranslator.h      - LLVM JIT编译器框架
│   ├── CPUTranslator.cpp    - LLVM集成实现
│   ├── CPUDisAsm.h          - 反汇编接口定义
│   ├── Hypervisor.h         - 超级管理程序上下文
│   └── sse2neon.h           - SSE到NEON转换库
│
└── Backends/AArch64/
    ├── AArch64Common.h      - ARM64寄存器定义
    ├── AArch64Common.cpp    - ARM64通用功能实现
    ├── AArch64ASM.h         - ARM64微汇编器
    ├── AArch64ASM.cpp       - ARM64汇编实现
    ├── AArch64JIT.h         - ARM64 JIT编译器后端
    ├── AArch64JIT.cpp       - ARM64 JIT实现
    ├── AArch64Signal.h      - ARM64信号处理
    └── AArch64Signal.cpp    - ARM64信号处理实现
```

## 核心模块

### CPU线程管理

#### [CPUThread.h](./CPUThread.h.md)
CPU线程的基类定义，提供了统一的线程接口。

**关键类**:
- `cpu_thread`: CPU线程基类
- `cpu_flag`: 线程状态标志枚举

**关键功能**:
- 线程生命周期管理
- 原子状态管理（16+种状态标志）
- 全局挂起机制 (suspend_all)
- 线程类型转换接口

**派生类**:
- `ppu_thread`: Power CPU线程
- `spu_thread`: Synergistic Processor Unit线程
- `rsx::thread`: RSX图形处理器线程

#### [CPUThread.cpp](./CPUThread.cpp.md)
CPU线程的具体实现。

**主要内容**:
- 线程状态检查 (check_state)
- 全局挂起实现 (suspend_all)
- CPU性能分析器 (cpu_prof)
- 线程计数和管理
- 转储和调试功能

### JIT编译框架

#### [CPUTranslator.h](./CPUTranslator.h.md)
LLVM JIT编译器的抽象框架。

**关键功能**:
- LLVM集成和IR生成
- C++类型到LLVM类型的映射
- CPU特性检测（SSSE3、AVX、FMA等）
- DSL支持用于表达式化编程
- 内在函数注册和替换

**支持的特性**:
- x86_64: SSE3→AVX→FMA→AVX-512
- ARM64: FMA、NEON
- 特定CPU优化

#### [CPUTranslator.cpp](./CPUTranslator.cpp.md)
LLVM框架的实现。

**主要内容**:
- CPU特性自动检测
- 内在函数处理 (x86_pshufb, any_select_by_bit4)
- 向量常数优化
- 转换管道执行
- 常量折叠和优化

### 反汇编和调试

#### [CPUDisAsm.h](./CPUDisAsm.h.md)
CPU反汇编接口定义。

**关键功能**:
- 多种反汇编输出模式
- 调试器集成
- 分支目标计算
- 内存范围管理

**反汇编模式**:
- `dump`: 完整转储（地址+机器码+汇编）
- `interpreter`: 解释器日志
- `normal`: 普通汇编输出
- `compiler_elf`: ELF编译器模式
- `list`: RSX列表格式
- `survey_cmd_size`: RSX命令统计

### 超级管理程序

#### [Hypervisor.h](./Hypervisor.h.md)
虚拟机管理层的上下文定义。

**主要内容**:
- 平台特定的寄存器上下文
- x86_64: RSP（栈指针）
- ARM64: PC、SP、通用寄存器(x18-x30)

## ARM64后端

### 核心定义

#### [AArch64Common.h](./Backends/AArch64/AArch64Common.h.md)
ARM64寄存器和基本定义。

**关键内容**:
- 通用寄存器枚举 (x0-x30, 31个)
- 特殊寄存器 (xzr, pc, sp)
- 寄存器名称常量
- CPU检测函数

**ARM64 ABI寄存器约定**:
- x0-x7: 参数/返回值
- x9-x15: 临时寄存器
- x19-x28: 被调用者保存
- x29: 帧指针(FP)
- x30: 链接寄存器(LR)

#### [AArch64Common.cpp](./Backends/AArch64/AArch64Common.cpp.md)
ARM64通用功能实现。

### 微汇编器

#### [AArch64ASM.h](./Backends/AArch64/AArch64ASM.h.md)
ARM64微汇编器接口。

**关键类**:
- `UASM`: 微汇编器

**指令支持**:
- 数据移动: mov, movnt, ldr, str, ldp, stp
- 算术: add, sub
- 控制流: b, br, ret
- 特殊: nop, brk, adr

**特点**:
- LLVM集成
- 寄存器约束管理
- 灵活的参数类型

#### [AArch64ASM.cpp](./Backends/AArch64/AArch64ASM.cpp.md)
微汇编器实现。

### JIT编译器后端

#### [AArch64JIT.h](./Backends/AArch64/AArch64JIT.h.md)
ARM64 JIT编译器后端（GHC栈管理）。

**关键概念**:
- GHC栈无关（stackless）执行模型
- 栈帧保留转换
- 尾调用优化
- 叶子函数优化

**分析结构**:
- `function_info_t`: 函数级分析
- `instruction_info_t`: 指令级分析
- `config_t`: 配置参数

**工作流**:
1. 函数预处理和分析
2. 指令解码和分类
3. 栈帧分配（非叶子函数）
4. 序幕/收尾生成
5. 尾调用优化

#### [AArch64JIT.cpp](./Backends/AArch64/AArch64JIT.cpp.md)
JIT后端实现。

**主要功能**:
- 栈帧布局设计
- 寄存器保存/恢复代码生成
- 序幕和收尾代码生成
- 尾调用处理
- 叶子函数优化

### 信号处理

#### [AArch64Signal.h](./Backends/AArch64/AArch64Signal.h.md)
ARM64信号处理接口。

#### [AArch64Signal.cpp](./Backends/AArch64/AArch64Signal.cpp.md)
信号处理实现。

**主要功能**:
- SIGSEGV处理
- 内存预留追踪
- 异常恢复
- 上下文保存/恢复

## SIMD转换

### [sse2neon.h](./sse2neon.h.md)
x86 SSE到ARM NEON的转换库。

**用途**:
- 跨平台SIMD代码支持
- 为x86编写的代码在ARM64上运行
- 性能关键的SIMD操作

**覆盖**:
- SSE/SSE2/SSE3/SSSE3
- SSE4.1/SSE4.2
- 部分AVX/AVX2支持

**特性**:
- 精度控制选项
- 多编译器支持
- 无外部依赖

## 架构设计

### 线程模型

```
┌─────────────────────────────────────┐
│         CPU线程管理层               │
│  (cpu_thread, cpu_flag, check_state) │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┬──────────────┐
      │                 │              │
   ┌──▼──┐         ┌──▼──┐        ┌──▼──┐
   │ PPU │         │ SPU │        │ RSX │
   └─────┘         └─────┘        └─────┘
```

### JIT编译管道

```
高级代码 (PPU/SPU 指令)
    │
    ▼
┌─────────────────┐
│  CPUTranslator  │ (类型映射、内在函数)
└────────┬────────┘
         │
    ┌────▼────┐
    │ LLVM IR │
    └────┬────┘
         │
    ┌────▼──────────────────┐
    │ 转换管道               │
    │ (AArch64JIT等)        │
    └────┬──────────────────┘
         │
    ┌────▼──────────┐
    │ LLVM 优化器    │
    └────┬──────────┘
         │
    ┌────▼──────────┐
    │ 本地代码生成  │
    └────┬──────────┘
         │
    ▼
ARM64 机器码
```

### 状态管理

```
线程状态转换:

初始: [stop|wait]
    │
    ▼
运行: (执行 cpu_task)
    │
    ▼
检查: check_state() 处理标志
    │
    ├─▶ 暂停: [suspend|dbg_pause|yield]
    ├─▶ 等待: [wait]
    └─▶ 继续: 循环到运行
    │
    ▼
停止: [stop|exit|again]
```

## 关键概念

### 全局挂起 (suspend_all)

允许在所有CPU线程同步的情况下执行操作：

1. 为所有线程设置pause标志
2. 等待所有线程进入wait状态
3. 执行待处理的工作
4. 清除pause标志并唤醒线程

### 性能分析

CPU线程集成了轻量级采样分析：

- `block_hash`: 当前执行块的哈希值
- `cpu_prof`: 后台分析线程
- 收集热点代码（频繁执行的块）

### GHC 栈管理

在ARM64上，RPCS3维持GHC的stackless（栈无关）执行模型：

- SP作为临时数据指针，不是传统栈
- 为每个函数分配显式栈帧以符合C++ ABI
- 复杂的序幕/收尾代码生成
- 尾调用优化以减少栈使用

## 使用流程

### CPU线程创建

```cpp
// 创建PPU线程
auto ppu = idm::make_ptr<named_thread<ppu_thread>>(id);
// 启动线程
ppu->state -= cpu_flag::stop;
```

### JIT编译

```cpp
// 初始化翻译器
cpu_translator translator(module, is_be);
translator.initialize(context, engine);

// 编译指令块
for (each instruction) {
    // 生成 LLVM IR
    translator.some_operation();
}

// 执行转换管道
translator.run_transforms(function);
```

### 状态检查

```cpp
// 在执行循环中
while (!(state & cpu_flag::exit)) {
    cpu_task();  // 执行指令
    if (check_state()) {
        break;  // 需要停止
    }
}
```

## 相关模块

- `/Emu/Cell/PPUThread.h/.cpp` - PPU实现
- `/Emu/Cell/SPUThread.h/.cpp` - SPU实现
- `/Emu/RSX/RSXThread.h/.cpp` - RSX实现
- `/Emu/Memory/` - 虚拟内存管理
- `/Emu/IdManager.h` - 线程ID管理

## 学习路径

1. **基础**: 理解CPUThread的线程模型和状态机
2. **进阶**: 学习JIT编译框架和LLVM集成
3. **优化**: 研究ARM64后端和栈管理
4. **性能**: 分析分析器和优化技术
5. **调试**: 使用反汇编器和状态转储功能

## 常见问题

### Q: CPUThread 为什么使用这么多状态标志？
A: CPU线程需要支持多种操作：暂停、调试、内存操作等。多个标志允许精细的状态控制和异步操作。

### Q: suspend_all 的目的是什么？
A: 允许在所有线程同步的点执行全局操作，如状态保存、内存操作等。

### Q: 为什么 ARM64 需要特殊的栈管理？
A: GHC 在 ARM64 上使用 stackless 执行，但 C++ ABI 期望传统栈，因此需要转换。

### Q: sse2neon 何时使用？
A: 当 SIMD 代码在 ARM64 上运行时，自动将 SSE 调用转换为 NEON。

## 相关资源

- LLVM 官方文档: https://llvm.org/docs/
- ARM64 ABI: https://github.com/ARM-software/abi-aa
- NEON 内在函数: https://developer.arm.com/architectures/instruction-sets/simd-isas/neon
- GHC Runtime: https://ghc.haskell.org/

## 许可证

RPCS3 采用 GPLv2 许可证。详见项目根目录的 LICENSE 文件。

---

**最后更新**: 2025-11-17
**文档版本**: 1.0

