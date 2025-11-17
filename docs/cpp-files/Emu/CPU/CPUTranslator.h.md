# CPUTranslator.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.h`
- **类型**: 头文件（LLVM 依赖）
- **行数**: 3200+ 行
- **所属模块**: CPU JIT 编译器框架

## 功能概述

CPUTranslator.h 是 RPCS3 的 JIT 编译基础框架，提供了一个强大的 LLVM 集成层。它为 CPU 指令转换为本地代码定义了类型系统、DSL 支持和编译管道。该文件支持多种 SIMD 特性检测和高级编译优化。

## 主要内容

### 编译条件和依赖

- **LLVM_AVAILABLE**: 仅在 LLVM 可用时编译
- **依赖库**:
  - LLVM IR, ExecutionEngine, IRBuilder
  - x86/ARM64 SIMD 内在函数
  - 自定义 JIT 和类型系统

### 类型系统 (llvm_value_t)

#### 类型映射框架
```cpp
template <typename T = void>
struct llvm_value_t;
```

一个模板结构体，将 C++ 类型映射到 LLVM 类型：

**支持的类型**:
- 整数: bool, i2, i4, u8, s8, u16, s16, u32, int, u64, s64, u128
- 浮点: float (f32), double (f64)
- 向量: u8[16], u16[8], u32[4], u64[2], f32[4], f64[2]
- 指针: T*
- 数组: T[N]

**类型信息成员**:
```cpp
using type = T;                    // 原始类型
static constexpr uint esize = ...  // 元素位大小
static constexpr bool is_int = ... // 是否整数类型
static constexpr bool is_sint = .. // 是否有符号
static constexpr bool is_uint = .. // 是否无符号
static constexpr bool is_float = . // 是否浮点
static constexpr uint is_array = . // 是否数组
static constexpr uint is_vector =. // 是否向量
```

**关键方法**:
```cpp
static llvm::Type* get_type(llvm::LLVMContext&);
llvm::Value* eval(llvm::IRBuilder<>*);
std::tuple<> match(llvm::Value*&, llvm::Module*);
```

### DSL 支持

#### 概念定义
```cpp
template <typename T>
concept LLVMType = ...      // LLVM 类型指针

template <typename T>
concept LLVMValue = ...     // LLVM 值指针

template <typename T>
concept DSLValue = requires(T& v, llvm::IRBuilder<>* ir) {
    { v.eval(ir) } -> LLVMValue;
};
```

支持一个独特的嵌入式 DSL（Domain Specific Language），允许：
- 表达式即函数：`eval()` 返回 LLVM 值
- 类型安全的编译时检查
- 高级中间代码生成

### cpu_translator 类

#### 成员变量

**LLVM 环境**:
```cpp
std::reference_wrapper<llvm::LLVMContext> m_context;  // LLVM 上下文
llvm::Module* m_module;                               // LLVM 模块
llvm::ExecutionEngine* m_engine;                      // JIT 执行引擎
llvm::IRBuilder<>* m_ir;                              // IR 构建器
```

**CPU 特性标志**:
```cpp
bool m_use_ssse3 = true;        // SSSE3 支持（x86）
bool m_use_fma = false;         // FMA 支持
bool m_use_avx = false;         // AVX 支持
bool m_use_avx512 = false;      // AVX-512 支持
bool m_use_vnni = false;        // VNNI 支持
bool m_use_gfni = false;        // GFNI 支持
bool m_use_avx512_icl = false;  // Icelake AVX-512
bool m_is_be;                   // 大端字节序标志
```

**转换管道**:
```cpp
std::vector<std::unique_ptr<translator_pass>> m_transform_passes;
```

#### 关键方法

**初始化和特性检测**:
```cpp
void initialize(llvm::LLVMContext& context, llvm::ExecutionEngine& engine);
```
- 检测 CPU 特性（SSSE3、AVX、FMA 等）
- 初始化 LLVM 执行引擎
- 设置 m_ir 构建器

**类型转换**:
```cpp
template <typename T> llvm::Type* get_type();
template <typename R, typename... Args> llvm::FunctionType* get_ftype();
template <typename T> value_t<T> value(llvm::Value*);
```

**值包装**:
```cpp
template <typename T> auto eval(T&& expr);
```

**函数调用接口**:
```cpp
template <typename RetT, typename RT, typename... FArgs, LLVMValue... Args>
llvm::CallInst* call(std::string_view name, RT(*_func)(FArgs...), Args... args);

template <typename RT, typename... FArgs, DSLValue... Args>
auto call(std::string_view name, RT(*_func)(FArgs...), Args&&... args);

template <typename RT, DSLValue... Args>
auto callf(llvm::Function* func, Args&&... args);
```

**类型位操作**:
```cpp
llvm::Value* bitcast(llvm::Value* val, llvm::Type* type) const;
template <typename T> llvm::Value* bitcast(llvm::Value* val);
```

**内在函数管理**:
```cpp
void replace_intrinsics(llvm::Function&);
```

**转换管道**:
```cpp
void register_transform_pass(std::unique_ptr<translator_pass>& pass);
void clear_transforms();
void reset_transforms();
void run_transforms(llvm::Function& f);
```

### 内在函数支持

通过 `register_intrinsic()` 支持自定义内在函数：
- **x86_pshufb**: 字节洗牌操作
- **any_select_by_bit4**: 位选择操作
- ARM64 NEON 对等物

### 常量计算

```cpp
template <> std::pair<bool, v128> get_const_vector<v128>(llvm::Value*, u32, u32);
template <> llvm::Constant* make_const_vector<v128>(v128, llvm::Type*, u32);
```

用于编译时向量常量的求值和生成。

## 代码分析

### 架构和设计

1. **类型安全**: 使用 C++ 模板和概念实现编译时类型检查
2. **多后端支持**: 支持 x86_64 和 ARM64 后端
3. **特性检测**: 自动检测和启用 CPU 特性（AVX、FMA 等）
4. **DSL 集成**: 允许用类似表达式的语法生成 LLVM IR
5. **转换管道**: 支持可组合的代码转换通道

### SIMD 特性自动检测

根据目标 CPU：
- **x86_64**: SSSE3（默认）→ AVX → FMA → AVX-512 → VNNI
- **ARM64**: FMA 和 NEON 支持
- **特定 CPU**: Haswell、Skylake、Zen 系列等

### 性能优化

1. **常量折叠**: 编译时计算常数表达式
2. **比特强制转换**: 支持带常数折叠的比特转换
3. **内在函数替换**: 用高效的本地指令替换通用内在函数
4. **TailCall 禁用**: 避免某些情况下的尾调用优化

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUTranslator.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/Emu/Cell/PPUTranslator.h` - PPU 特定翻译器
- `/home/user/rpcs3/rpcs3/Emu/Cell/SPUTranslator.h` - SPU 特定翻译器
- `/home/user/rpcs3/rpcs3/util/v128.hpp` - SIMD 向量类型
- `/home/user/rpcs3/rpcs3/Utilities/JIT.h` - JIT 框架

## 学习要点

1. **LLVM 集成**: 如何在 C++ 应用中集成和使用 LLVM
2. **类型系统设计**: 构建可扩展的编译时类型映射系统
3. **DSL 实现**: 创建嵌入式领域特定语言的技术
4. **多架构支持**: 支持多个 CPU 架构和特性的策略
5. **JIT 编译管道**: 设计高效的即时编译管道
6. **模板元编程**: 高级 C++ 模板技术应用
