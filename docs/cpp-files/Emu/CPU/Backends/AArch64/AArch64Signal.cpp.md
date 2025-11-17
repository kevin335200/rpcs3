# AArch64Signal.cpp

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Signal.cpp`
- **类型**: 源文件
- **行数**: ~700行
- **所属模块**: ARM64 信号处理

## 功能概述

AArch64Signal.cpp 实现了 ARM64 架构上的信号处理机制，特别是用于处理内存访问异常（SIGSEGV）和预留追踪。该文件处理 JIT 编译代码执行期间的异常情况。

## 主要内容

### 信号处理器

#### SIGSEGV 处理
当访问受保护的内存时触发：
1. 识别异常地址
2. 检查是否为已知的预留区域
3. 提供恢复机制
4. 更新虚拟机状态

#### 预留追踪
处理内存预留操作：
- 通过信号检测预留冲突
- 更新预留时间戳
- 触发重新检查

### 异常恢复

#### 上下文保存/恢复
处理寄存器状态：
- 保存所有通用寄存器
- 保存特殊寄存器（PC、SP）
- 保存浮点寄存器

#### 异常处理流程
1. 捕获信号
2. 识别异常类型
3. 检查预留状态
4. 恢复执行或抛出异常

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Signal.h` - 头文件
- `/home/user/rpcs3/rpcs3/Emu/Memory/vm_reservation.h` - 内存预留
- `/home/user/rpcs3/rpcs3/Emu/CPU/Hypervisor.h` - 超级管理程序

## 学习要点

1. **信号处理**: POSIX 信号在虚拟机中的应用
2. **异常恢复**: JIT 代码中的异常恢复机制
3. **内存预留**: 追踪内存读/写预留
4. **ARM64 异常**: ARM64 异常处理的特殊考虑
