# AArch64ASM.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.h`
- **类型**: 头文件
- **行数**: ~100行
- **所属模块**: ARM64 微汇编器

## 功能概述

AArch64ASM.h 定义了一个微汇编器（UASM）类，用于动态生成 ARM64 汇编指令。它提供了一个高级接口来生成 ARM64 机器码，支持多种寄存器操作、内存访问和分支指令，与 LLVM IR 紧密集成。

## 主要内容

### 命名空间和类定义

```cpp
namespace aarch64 {
    class UASM {
        // 微汇编器实现
    };
}
```

### 枚举和辅助类型

#### ArgType 枚举
定义了指令参数的类型：
- **Register**: 通用寄存器（gpr）
- **SRegister**: 特殊寄存器（spr）
- **Immediate**: 立即数
- **LLVMInt**: LLVM 整数值
- **LLVMPtr**: LLVM 指针值
- **LLVMReg**: LLVM 寄存器值

#### Arg 结构体
表示指令参数的变体类型：
```cpp
struct Arg {
    ArgType type;
    union {
        llvm::Value* value;  // 用于 LLVM 类型
        gpr reg;             // 通用寄存器
        spr sreg;            // 特殊寄存器
        s64 imm;             // 立即数
    };
    std::string to_string(int* id = nullptr) const;
};
```

### 内部结构

#### compiled_instruction_t
```cpp
struct compiled_instruction_t {
    std::string asm_;               // 汇编代码
    std::vector<std::string> constraints;  // 寄存器约束
    std::vector<llvm::Value*> args; // 参数值
};
```

存储编译后的指令信息。

#### 指令存储
```cpp
std::vector<compiled_instruction_t> m_instructions;  // 已编译指令列表
```

### 静态工厂方法

```cpp
static Arg Int(llvm::Value* v);      // 创建整数参数
static Arg Imm(s64 v);               // 创建立即数参数
static Arg Reg(gpr reg);             // 创建通用寄存器参数
static Arg Reg(spr reg);             // 创建特殊寄存器参数
static Arg Ptr(llvm::Value* v);      // 创建指针参数
static Arg Var(llvm::Value* v);      // 创建变量参数
```

### 低级发射方法

```cpp
void emit0(const char* inst);                    // 无操作数指令
void emit1(const char* inst, const Arg& arg0, const std::vector<gpr>& clobbered);
void emit2(const char* inst, const Arg& arg0, const Arg& arg1, const std::vector<gpr>& clobbered);
void emit3(const char* inst, const Arg& arg0, const Arg& arg1, const Arg& arg2, const std::vector<gpr>& clobbered);
void emit4(const char* inst, const Arg& arg0, const Arg& arg1, const Arg& arg2, const Arg& arg3, const std::vector<gpr>& clobbered);

void embed_args(compiled_instruction_t& instruction, const std::vector<Arg>& args, const std::vector<gpr>& clobbered);
```

处理指令编译和参数嵌入。`clobbered` 参数指定了由该指令修改的寄存器。

### 高级指令接口

#### 移动指令
```cpp
void mov(gpr dst, gpr src);                // 寄存器到寄存器移动
void mov(gpr dst, const Arg& src);         // 任意源到寄存器
void movnt(gpr dst, const Arg& src);       // 非时间移动（非临时）
```

#### 地址计算
```cpp
void adr(gpr dst, const Arg& src);  // 地址计算（相对于 PC）
```

#### 内存访问
```cpp
// 存储单个值
void str(gpr src, gpr base, const Arg& offset);
void str(gpr src, spr base, const Arg& offset);
void str(const Arg& src, gpr base, const Arg& offset);
void str(const Arg& src, spr base, const Arg& offset);

// 加载单个值
void ldr(gpr dst, gpr base, const Arg& offset);
void ldr(gpr dst, spr base, const Arg& offset);

// 存储对值（双字操作）
void stp(gpr src0, gpr src1, gpr base, const Arg& offset);
void stp(gpr src0, gpr src1, spr base, const Arg& offset);

// 加载对值（双字操作）
void ldp(gpr dst0, gpr dst1, gpr base, const Arg& offset);
void ldp(gpr dst0, gpr dst1, spr base, const Arg& offset);
```

#### 算术运算
```cpp
void add(spr dst, spr src0, const Arg& src1);  // 特殊寄存器加法
void add(gpr dst, gpr src0, const Arg& src1);  // 通用寄存器加法
void sub(spr dst, spr src0, const Arg& src1);  // 特殊寄存器减法
void sub(gpr dst, gpr src0, const Arg& src1);  // 通用寄存器减法
```

#### 控制流
```cpp
void b(const Arg& target);       // 无条件分支
void br(gpr target);             // 寄存器分支
void br(const Arg& target);      // 地址分支
void ret();                       // 返回（使用 x30）
```

#### 特殊指令
```cpp
void nop(const std::vector<Arg>& refs = {});  // 空操作（带可选依赖）
void brk(int mark = 0);                        // 断点指令
```

### 汇编器操作

#### 代码组合
```cpp
void append(const UASM& other);     // 追加另一个 UASM 的代码
void prepend(const UASM& other);    // 前置另一个 UASM 的代码
```

#### LLVM 集成
```cpp
void insert(llvm::IRBuilder<>* irb, llvm::LLVMContext& ctx) const;
```

将编译的汇编代码插入 LLVM IR（作为内联汇编块）。

## 代码分析

### 设计模式

1. **生成器模式**: UASM 作为汇编代码的生成器
2. **工厂方法**: 静态 Arg 创建方法
3. **流式接口**: 链式调用 emit* 方法来构建指令序列
4. **类型安全**: 强类型参数和编译时检查

### ARM64 特性支持

1. **寄存器变体**: 同一指令支持不同的寄存器类型
2. **灵活的寻址**: 支持各种寻址模式（基址+偏移）
3. **双字操作**: stp/ldp 用于高效的多值操作
4. **内联约束**: clobbered 向量指定受影响的寄存器

### 与 LLVM 的集成

1. **LLVM 值支持**: 可以将 LLVM 值作为参数传递
2. **内联汇编**: 通过 insert() 将汇编与 LLVM IR 混合
3. **寄存器约束**: 处理 LLVM 内联汇编的约束系统

### 应用场景

1. **运行时代码生成**:
   - 在 JIT 编译过程中动态生成汇编代码
   - 与 LLVM IR 无缝集成

2. **性能关键路径**:
   - 手工优化的汇编代码
   - 直接控制寄存器和指令调度

3. **虚拟机指令实现**:
   - 将 PS3 指令翻译为 ARM64 指令
   - 快速路径优化

4. **上下文切换**:
   - 生成序幕和收尾代码
   - 保存/恢复寄存器

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h` - 寄存器定义
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64JIT.h` - JIT 编译器
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h` - CPU 翻译器基类

## 学习要点

1. **微汇编器设计**: 实现一个高级的动态汇编代码生成器
2. **ARM64 指令集**: ARM64 架构的常见指令模式
3. **LLVM 内联汇编**: 如何在 LLVM IR 中嵌入汇编代码
4. **寄存器管理**: 追踪被修改的寄存器和寄存器约束
5. **生成器模式**: 使用 Builder 模式构造复杂对象
6. **JIT 编译**: 运行时代码生成的实际应用
