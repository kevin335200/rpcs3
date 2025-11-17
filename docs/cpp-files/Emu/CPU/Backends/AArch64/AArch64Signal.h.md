# AArch64Signal.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Signal.h`
- **类型**: 头文件（ARM64 特定）
- **行数**: 未详细分析（信号处理相关）
- **所属模块**: ARM64 信号处理

## 功能概述

AArch64Signal.h 定义了 ARM64 架构上的信号处理机制。该文件提供了处理 CPU 异常和中断的接口，用于在 JIT 编译代码执行期间处理如内存访问异常、浮点异常等系统信号。

## 主要用途

1. **SIGSEGV 处理**: 处理非法内存访问
2. **保留追踪**: 跟踪内存预留操作
3. **JIT 异常处理**: 在动态生成的代码中处理异常
4. **调试支持**: 提供异常状态的调试信息

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Signal.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h` - 寄存器定义
- `/home/user/rpcs3/rpcs3/Emu/Memory/vm_reservation.h` - 内存预留机制

## 学习要点

1. **信号处理**: POSIX 信号在虚拟机中的应用
2. **异常恢复**: JIT 代码中的异常处理机制
3. **ARM64 上下文**: ARM64 异常处理的特殊考虑
