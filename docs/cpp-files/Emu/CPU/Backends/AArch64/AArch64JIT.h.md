# AArch64JIT.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64JIT.h`
- **类型**: 头文件（仅在 ARM64 架构上编译）
- **行数**: ~90行
- **所属模块**: ARM64 JIT 编译器后端

## 功能概述

AArch64JIT.h 定义了 GHC（Glasgow Haskell Compiler）栈管理的帧保留转换通道，用于在 ARM64 架构上实现栈无关（stackless）执行的虚拟机。这个文件实现了一个关键的优化，在 ARM64 上保持 GHC 栈管理的行为，同时符合 C++ ABI 的期望。

## 主要内容

### 编译条件

```cpp
#ifndef ARCH_ARM64
#error "You have included an arm-only header"
#endif
```

仅在 ARM64 架构上编译。

### 命名空间

```cpp
namespace aarch64 {
    class GHC_frame_preservation_pass : public translator_pass { ... };
}
```

### GHC_frame_preservation_pass 类

ARM64 上 GHC 栈管理的转换通道，处理栈帧保留以实现栈无关虚拟机。

#### 嵌套类型定义

##### function_info_t 结构体
存储函数级别的分析信息：

```cpp
struct function_info_t {
    u32 instruction_count;        // 函数中的指令数量
    u32 num_external_calls;       // 外部函数调用的数量
    u32 stack_frame_size;         // 栈帧大小（猜测值，关键用于向量重指令）
    bool clobbers_x30;            // 函数是否修改 x30 (LR)
    bool is_leaf;                 // 函数是否为叶子函数（不调用其他函数）
};
```

**字段说明**:
- `instruction_count`: 控制流分析的基础
- `num_external_calls`: 确定是否需要帧保存
- `stack_frame_size`: 对于向量重代码（spilling）的关键估计
- `clobbers_x30`: 优化 LR 保存策略
- `is_leaf`: 叶子函数可以进行特殊优化

##### instruction_info_t 结构体
存储单条指令级别的分析：

```cpp
struct instruction_info_t {
    bool is_call_inst;        // 是函数调用
    bool preserve_stack;      // 在此调用周围保留栈
    bool is_returning;        // 指令"返回"到下一条指令
    bool callee_is_GHC;       // 被调用函数是否使用 GHC 约定
    bool is_tail_call;        // 尾调用（假设为退出/终止）
    bool is_indirect;         // 间接调用（目标是第一个操作数）
    llvm::Function* callee;   // 被调用函数指针
    std::string callee_name;  // 被调用函数名称
};
```

**字段说明**:
- `is_call_inst`: 核心分类
- `preserve_stack`: 是否需要栈保留
- `is_returning`: 区分调用和跳转
- `callee_is_GHC`: 调用约定选择
- `is_tail_call`: 优化机会
- `is_indirect`: 寻址方式

##### config_t 结构体
转换通道的配置参数：

```cpp
struct config_t {
    bool debug_info = false;           // 记录调试信息
    bool use_stack_frames = true;      // 为每个函数分配栈帧
    bool optimize = true;              // 优化指令生成
    u32 hypervisor_context_offset = 0; // 超级管理程序上下文偏移
    std::function<bool(const std::string&)> exclusion_callback;
    std::vector<std::pair<std::string, gpr>> base_register_lookup;
    std::vector<std::string> faux_function_list;
};
```

**配置说明**:
- `debug_info`: 用于调试不可靠的代码生成
- `use_stack_frames`: false 时使用全局栈替代每函数栈
- `optimize`: false 时禁用指令级优化，便于调试
- `hypervisor_context_offset`: 线程对象中的寄存器上下文位置
- `exclusion_callback`: 排除特定函数的处理
- `base_register_lookup`: 从函数名称查找寄存器位置
- `faux_function_list`: 不可信的"假"函数（代码洞）

#### 保护成员

##### 处理和分析方法

```cpp
std::unordered_set<std::string> m_visited_functions;  // 已访问函数追踪

config_t m_config;  // 配置参数

// 分析和转换方法
void force_tail_call_terminators(llvm::Function& f);
function_info_t preprocess_function(const llvm::Function& f);
instruction_info_t decode_instruction(const llvm::Function& f, const llvm::Instruction* i);

bool is_ret_instruction(const llvm::Instruction* i);
bool is_inlined_call(const llvm::CallInst* ci);
bool is_faux_function(const std::string& function_name);

gpr get_base_register_for_call(const std::string& callee_name, gpr default_reg = gpr::x19);

void process_leaf_function(llvm::IRBuilder<>* irb, llvm::Function& f);

llvm::BasicBlock::iterator patch_tail_call(
    llvm::IRBuilder<>* irb,
    llvm::Function& f,
    llvm::BasicBlock::iterator where,
    const instruction_info_t& instruction_info,
    const function_info_t& function_info,
    const ASMBlock& frame_epilogue);
```

**方法说明**:
- `force_tail_call_terminators()`: 确保尾调用是块终止符
- `preprocess_function()`: 函数级别分析
- `decode_instruction()`: 指令级别分析
- `is_ret_instruction()`: 识别返回指令
- `is_inlined_call()`: 识别内联调用
- `is_faux_function()`: 识别不可信函数
- `get_base_register_for_call()`: 查找线程上下文寄存器
- `process_leaf_function()`: 叶子函数优化
- `patch_tail_call()`: 尾调用处理

#### 公开接口

```cpp
GHC_frame_preservation_pass(const config_t& configuration);
~GHC_frame_preservation_pass() = default;

void run(llvm::IRBuilder<>* irb, llvm::Function& f) override;
void reset() override;
```

### 使用场景

#### ASMBlock 类型定义
```cpp
using ASMBlock = UASM;  // ARM64 汇编块别名
```

## 代码分析

### 设计模式

1. **转换通道模式**: 继承 `translator_pass` 接口
2. **访问者模式**: 递归访问函数和指令
3. **策略模式**: config_t 定义多种处理策略

### GHC 栈管理

**GHC 的独特性**:
- GHC 在非 x86 架构上运行"栈无关"（stackless）
- SP 被当作指向临时内存（scratchpad）的指针
- 这与宿主 C++ ABI 的期望冲突

**解决方案**:
- 为每个函数添加栈帧
- 保存/恢复被调用者保存的寄存器
- 在调用前后管理栈

### 优化策略

1. **叶子函数优化**: 不调用其他函数的函数不需要栈帧
2. **尾调用优化**: 尾调用可以重用当前栈帧
3. **寄存器保留**: 仅保存被修改的寄存器
4. **栈大小估计**: 准确估计向量溢出所需空间

### ARM64 特定考虑

1. **寄存器窗口**: ARM64 没有滑动寄存器窗口，需要显式保存
2. **链接寄存器**: x30 需要特殊处理（返回地址）
3. **帧指针**: x29 用于栈回追

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64ASM.h` - 微汇编器
- `/home/user/rpcs3/rpcs3/Emu/CPU/Backends/AArch64/AArch64Common.h` - 寄存器定义
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h` - CPU 翻译器基类
- `/home/user/rpcs3/rpcs3/Emu/CPU/Hypervisor.h` - 超级管理程序上下文

## 学习要点

1. **GHC 栈管理**: Glasgow Haskell Compiler 的栈无关执行模型
2. **ARM64 ABI**: ARM 架构调用约定的实现细节
3. **编译器通道**: LLVM 转换通道的设计和实现
4. **函数分析**: 函数级和指令级的代码分析
5. **代码生成**: 运行时序幕/收尾代码生成
6. **优化技术**: 尾调用优化和叶子函数优化
