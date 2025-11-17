# AArch64ASM.cpp

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.cpp`
- **类型**: 源文件
- **行数**: ~600行
- **所属模块**: ARM64 微汇编器实现

## 功能概述

AArch64ASM.cpp 是 ARM64 微汇编器（UASM）的实现文件。它提供了动态生成 ARM64 汇编指令的具体实现，包括参数处理、寄存器约束管理和 LLVM IR 生成。

## 主要内容

### 参数处理

#### Arg::to_string()
将参数转换为可读的字符串表示：
- 通用寄存器：使用 gpr_names 数组
- 特殊寄存器：使用 spr_names 数组
- 立即数：格式化为十六进制或十进制
- LLVM 值：生成 LLVM SSA 值的引用

### 指令发射

#### emit0-4 方法
低级汇编指令发射：
1. 将指令名称和参数组合成汇编字符串
2. 提取寄存器约束
3. 收集 LLVM 值参数
4. 生成内联汇编块

#### embed_args()
处理参数与 LLVM 值的绑定：
- 转换 ArgType 为 LLVM 约束字符串
- 管理输入/输出约束
- 追踪被修改的寄存器

### 高级指令接口实现

所有 mov、ldr、str、add、sub、b 等指令都通过 emit*() 方法实现。

### LLVM IR 集成

#### insert() 方法
将编译的汇编代码插入 LLVM IR：
1. 创建内联汇编块
2. 设置约束和参数
3. 将块插入当前构建位置

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.h` - 头文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h` - CPU 翻译器

## 学习要点

1. **内联汇编**: LLVM 内联汇编的使用
2. **寄存器约束**: GNU 约束字符串的处理
3. **汇编生成**: 动态生成汇编代码的技术
