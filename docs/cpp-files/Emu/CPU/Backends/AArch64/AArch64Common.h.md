# AArch64Common.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h`
- **类型**: 头文件
- **行数**: ~43行
- **所属模块**: ARM64 (AArch64) CPU 后端

## 功能概述

AArch64Common.h 定义了 ARM64 架构特定的 CPU 寄存器枚举和通用定义。作为 ARM64 后端实现的基础，它提供了通用寄存器（GPR）和特殊寄存器（SPR）的标准定义，用于 JIT 编译和汇编生成。

## 主要内容

### 枚举定义

#### gpr 枚举 - 通用寄存器（General Purpose Registers）
```cpp
enum gpr : s32 {
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9,
    x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
    x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30
};
```

**共 31 个通用寄存器** (x0-x30)

**ARM64 ABI 寄存器约定**:
- **x0-x7**: 参数/结果寄存器（参数传递和返回值）
- **x8**: 间接返回地址寄存器
- **x9-x15**: 临时寄存器（被调用者不需保存）
- **x16-x17**: 内联和平台寄存器（被调用者不需保存）
- **x18**: 平台寄存器（保留给平台使用）
- **x19-x28**: 被调用者保存的寄存器（函数必须保存和恢复）
- **x29**: 帧指针 (FP)（被调用者保存）
- **x30**: 链接寄存器 (LR)（保存返回地址）

#### spr 枚举 - 特殊寄存器（Special Registers）
```cpp
enum spr : s32 {
    xzr = 0,  // 零寄存器（读取总是 0，写入被丢弃）
    pc,       // 程序计数器
    sp        // 栈指针
};
```

**特殊寄存器说明**:
- **xzr**: 硬连线为零的寄存器（x31 的别名）
- **pc**: 程序计数器（指向当前执行的指令）
- **sp**: 栈指针（x31 的别名）

### 寄存器名称常量

#### gpr_names 数组
```cpp
static const char* gpr_names[] = {
    "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9",
    "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19",
    "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30"
};
```

用于调试输出和寄存器转储。

#### spr_names 数组
```cpp
static const char* spr_names[] = {
    "xzr", "pc", "sp"
};
```

用于指代特殊寄存器的符号名称。

#### spr_asm_names 数组
```cpp
static const char* spr_asm_names[] = {
    "xzr", ".", "sp"
};
```

用于汇编代码生成的寄存器名称：
- "xzr": ARM64 汇编中的零寄存器
- ".": PC 的特殊汇编表示（点代表当前位置）
- "sp": 栈指针

### 函数声明

```cpp
std::string get_cpu_name();
std::string get_cpu_brand();
```

获取 CPU 的名称和品牌信息（具体实现在 AArch64Common.cpp）。

## 代码分析

### ARM64 架构特点

1. **32 个通用寄存器**: x0-x31（其中 x31 有特殊用途）
2. **一致的寄存器宽度**: 所有 GPR 都是 64 位
3. **丰富的寄存器集**: 相比 x86_64 提供了更多的通用寄存器
4. **特殊寄存器**: PC、SP 和 XZR（零寄存器）

### 设计模式

1. **枚举值对齐**: 使用连续的枚举值便于数组索引
2. **符号和汇编名称**: 分离逻辑名称和汇编表示
3. **类型安全**: 使用强类型枚举避免混淆 GPR 和 SPR

### 应用场景

1. **JIT 代码生成**:
   - 在生成 ARM64 机器码时选择合适的寄存器
   - 遵守 ARM64 ABI 的寄存器保存约定

2. **寄存器分配**:
   - 为不同的操作分配合适的寄存器
   - 跟踪被调用者保存的寄存器

3. **调试和监控**:
   - 显示寄存器状态
   - 生成易读的汇编代码

4. **编译器后端**:
   - 指令选择和寄存器分配
   - 函数序幕和收尾代码生成

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.h` - 微汇编器
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64JIT.h` - JIT 编译器
- `/home/user/rpcs3/rpcs3/Emu/CPU/Hypervisor.h` - 超级管理程序上下文

## 学习要点

1. **ARM64 ABI**: ARM 架构调用约定和寄存器使用
2. **寄存器分类**: 临时/被调用者保存寄存器的区分
3. **特殊寄存器**: XZR、PC、SP 在 ARM64 中的角色
4. **编译器设计**: 后端代码生成的寄存器定义
5. **多架构支持**: RPCS3 如何支持不同的 CPU 架构
