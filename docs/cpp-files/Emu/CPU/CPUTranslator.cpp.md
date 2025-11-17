# CPUTranslator.cpp

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.cpp`
- **类型**: 源文件（LLVM 依赖）
- **行数**: ~518行
- **所属模块**: CPU JIT 编译器框架

## 功能概述

CPUTranslator.cpp 是 cpu_translator 类的实现文件，提供了 LLVM 集成层的具体实现。主要负责 LLVM 上下文初始化、CPU 特性检测、内在函数注册以及代码转换管道的执行。

## 主要内容

### 全局状态

```cpp
llvm::LLVMContext g_llvm_ctx;  // 全局 LLVM 上下文
```

### 工具函数

#### peek_through_bitcasts()
```cpp
llvm::Value* peek_through_bitcasts(llvm::Value* arg)
```

通过递归去掉比特转换指令来"看穿"值的包装：
- 逐步遍历 BitCast 指令
- 返回原始的底层值
- 用于常数优化和值识别

### 构造函数和初始化

#### cpu_translator::cpu_translator(llvm::Module* _module, bool is_be)

```cpp
cpu_translator::cpu_translator(llvm::Module* _module, bool is_be)
    : m_context(g_llvm_ctx)
    , m_module(_module)
    , m_is_be(is_be)
```

**初始化工作**:
1. 设置 LLVM 模块和字节序标志
2. 注册内在函数处理器：
   - `x86_pshufb`: 字节洗牌（SSSE3 或软件实现）
   - `any_select_by_bit4`: 位选择操作

**内在函数处理**:

##### x86_pshufb 内在函数
实现 SSE3 的字节洗牌操作：
- **x86_64 实现**: 使用原生 LLVM SSSE3 内在函数
- **ARM64 实现**:
  - 屏蔽索引为 0x8F 的位
  - 使用 aarch64_neon_tbl1 进行表查找
- **软件回退**:
  - 循环遍历 16 个字节
  - 使用 extractElement/insertElement 实现

##### any_select_by_bit4 内在函数
通过移位的 64 位值的符号位选择：
- 移位 3 位（u64[2] -> s8[16]）
- 检查符号位并选择相应的值

### 特性检测 - initialize() 方法

```cpp
void cpu_translator::initialize(llvm::LLVMContext& context,
                                llvm::ExecutionEngine& engine)
```

#### CPU 名称获取
```cpp
auto cpu = m_engine->getTargetMachine()->getTargetCPU();
if (cpu == "generic")
    cpu = fallback_cpu_detection();  // 回退检测
```

#### SSSE3 支持检测
CPU 名称包含以下内容时禁用：`k8`、`opteron`、`athlon64`、`amdfam10`、`barcelona`

#### AVX 支持检测
启用于：`sandybridge`、`ivybridge`、`bdver1`

#### FMA 支持检测
启用于：
- Intel: Haswell, Broadwell, Skylake, Alderlake, Raptorlake, Meteorlake
- AMD: bdver2, bdver3, bdver4, Zen (v1-v3)
- 新型: Arrow Lake, Lunar Lake

#### AVX-512 支持检测
启用于：
- Skylake-AVX512, Cascade Lake, Cannonlake, Cooper Lake

#### VNNI (Vector Neural Network Instructions) 支持
启用于：Cascade Lake 及更新的 Intel 处理器，AMD Zen 4 及后续

#### GFNI (Galois Field New Instructions) 支持
启用于：Tremont 及更新的 Intel 处理器

#### Icelake 及更新的 AVX-512 特性
启用于：Icelake, Tiger Lake, Rocket Lake, Sapphire Rapids 及 AMD Zen 4+

### 类型和常数处理

#### bitcast 方法
```cpp
llvm::Value* cpu_translator::bitcast(llvm::Value* val, llvm::Type* type) const
```

执行类型安全的比特转换：
1. 验证源类型和目标类型的大小相同
2. 如果是常量，进行编译时常数折叠
3. 非常量值使用 CreateBitCast

#### get_const_vector 模板特化

```cpp
template <> std::pair<bool, v128> cpu_translator::get_const_vector<v128>
    (llvm::Value* c, u32 _pos, u32 _line)
```

从 LLVM 常量值提取 v128 向量：

**支持的格式**:
- 128 位整数常量
- 定长向量（i8x16, i16x8, i32x4, i64x2, f32x4, f64x2）
- 零初始化常量

**返回值**: `{success, extracted_v128_value}`

#### make_const_vector 模板特化

```cpp
template <> llvm::Constant* cpu_translator::make_const_vector<v128>
    (v128 v, llvm::Type* t, u32 _line)
```

从 v128 值创建 LLVM 常量向量：
- 128 位整数常量
- 各种向量类型（字节、字、双字、四字）
- 浮点向量（f32, f64）

### 内在函数替换

#### replace_intrinsics() 方法
```cpp
void cpu_translator::replace_intrinsics(llvm::Function& f)
```

**工作流**:
1. 遍历函数的所有基本块
2. 查找所有调用指令
3. 检查是否有注册的内在函数处理器
4. 如果有，调用对应的处理器替换调用
5. 递归处理替换后的新指令

**递归避免**: 使用 `names` 集合跟踪正在处理的函数，防止无限递归

### 转换管道

#### register_transform_pass()
```cpp
void cpu_translator::register_transform_pass(
    std::unique_ptr<translator_pass>& pass)
```
向管道添加新的转换通道。

#### clear_transforms()
删除所有注册的转换通道。

#### reset_transforms()
重置所有通道的内部状态（清除缓存等）。

#### run_transforms()
```cpp
void cpu_translator::run_transforms(llvm::Function& f)
```

**执行顺序**:
1. 首先运行 replace_intrinsics() 解决名称
2. 然后依次运行所有已注册的转换通道

### 辅助函数

#### erase_stores()
```cpp
void cpu_translator::erase_stores(llvm::ArrayRef<llvm::Value*> args)
```

删除对给定值的所有存储操作：
- 遍历每个值的使用链
- 跳过比特转换（通过 peek_through_bitcasts）
- 删除匹配的存储指令

## 代码分析

### CPU 特性检测策略

采用逐级递进的方式：
```
x86_64 CPU: SSSE3 (默认) → AVX → FMA → AVX-512 → VNNI → GFNI
ARM64: 基础 → FMA → NEON（隐式）
```

### 内在函数设计模式

1. **多后端支持**: 同一个逻辑内在函数有多个平台实现
2. **软件回退**: 当硬件特性不可用时，提供软件实现
3. **延迟替换**: 内在函数在 IR 生成后才被替换

### 常量优化

- 编译时常数折叠：避免运行时计算
- 向量常量预处理：直接从常数提取数据

### 转换管道架构

支持链式转换：
```
源代码 → 内在函数替换 → 用户定义通道 → LLVM 优化 → 本地代码
```

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h` - 头文件声明
- `/home/user/rpcs3/rpcs3/Emu/Cell/PPUTranslator.cpp` - PPU 翻译器实现
- `/home/user/rpcs3/rpcs3/Emu/Cell/SPUTranslator.cpp` - SPU 翻译器实现
- `/home/user/rpcs3/rpcs3/util/v128.hpp` - SIMD 向量类型
- `/home/user/rpcs3/rpcs3/Utilities/JIT.h` - JIT 框架

## 学习要点

1. **CPU 特性检测**: 如何在运行时检测并启用 CPU 特性
2. **内在函数设计**: 实现跨平台的内在函数替换机制
3. **LLVM 集成**: 实际的 LLVM IR 构建和优化管道
4. **常数折叠**: 编译时常数计算和优化技术
5. **模板特化**: C++ 模板特化在向量处理中的应用
6. **递归处理**: 安全地处理可能递归的转换
