# CPU 模拟模块

## 📌 模块概述

CPU 模拟模块是 RPCS3 的核心组件，负责模拟 PlayStation 3 的 Cell 处理器架构。Cell 处理器包含一个主处理器单元（PPU - PowerPC Processing Unit）和多个协同处理单元（SPU - Synergistic Processing Unit）。

**位置**: `/rpcs3/Emu/CPU/`

## 🏗️ Cell 处理器架构简介

PlayStation 3 的 Cell 处理器架构：
```
┌─────────────────────────────────────┐
│        Cell Broadband Engine        │
├─────────────────────────────────────┤
│  PPU (PowerPC 64-bit)               │
│  - 主处理器                          │
│  - 2 线程 (SMT)                      │
│  - 3.2 GHz                           │
├─────────────────────────────────────┤
│  SPU × 8 (实际可用 6-7 个)           │
│  - 128 位 SIMD 处理器                │
│  - 每个有 256KB 本地存储              │
│  - 独立指令集                        │
└─────────────────────────────────────┘
```

## 📂 目录结构

```
rpcs3/Emu/CPU/
├── CPUThread.h/cpp        # CPU 线程基类
├── CPUDisAsm.h            # 反汇编接口
├── CPUTranslator.h/cpp    # CPU 指令翻译器（LLVM）
├── Hypervisor.h           # Hypervisor 层
├── sse2neon.h             # SSE2 到 NEON 的转换
│
└── Backends/              # 后端实现
    └── AArch64/           # ARM64 后端
        ├── AArch64JIT.h/cpp     # ARM64 JIT 编译器
        ├── AArch64ASM.h/cpp     # ARM64 汇编生成
        ├── AArch64Common.h/cpp  # ARM64 公共代码
        └── AArch64Signal.h/cpp  # ARM64 信号处理

rpcs3/Emu/Cell/
├── PPUThread.h/cpp        # PPU 线程实现
├── PPUDisAsm.h/cpp        # PPU 反汇编
├── PPUInterpreter.h       # PPU 解释器
├── PPUTranslator.cpp      # PPU LLVM 翻译器
├── PPUAnalyser.cpp        # PPU 代码分析器
├── PPUOpcodes.h           # PPU 指令定义
├── PPUFunction.h          # PPU 函数信息
│
├── SPUThread.h/cpp        # SPU 线程实现
├── SPUDisAsm.h/cpp        # SPU 反汇编
├── SPUInterpreter.h/cpp   # SPU 解释器
├── SPULLVMRecompiler.cpp  # SPU LLVM 重编译器
├── SPUASMJITRecompiler.h/cpp # SPU ASMJIT 重编译器
├── SPUCommonRecompiler.cpp   # SPU 公共重编译代码
├── SPUAnalyser.h          # SPU 代码分析器
│
├── RawSPUThread.cpp       # Raw SPU 线程
└── MFC.h/cpp              # 内存流控制器
```

## 🎯 核心类详解

### 1. cpu_thread - CPU 线程基类

所有 CPU 线程的抽象基类。

```cpp
class cpu_thread
{
public:
    // 线程 ID
    const u32 id;

    // 线程状态（位集合）
    atomic_bs_t<cpu_flag> state{cpu_flag::stop + cpu_flag::wait};

    // 阻塞哈希（用于 JIT 缓存）
    u64 block_hash = 0;

    // 检查线程状态
    bool check_state() noexcept;

    // 测试是否停止
    [[nodiscard]] bool test_stopped()
    {
        if (state)
        {
            if (check_state())
                return true;
        }
        return false;
    }

    // 纯虚函数 - 在派生类中实现
    virtual void cpu_task() = 0;
    virtual void cpu_sleep() = 0;
    virtual void cpu_mem() = 0;
    virtual void cpu_unmem() = 0;
};
```

### 2. cpu_flag - CPU 线程状态标志

使用位集合表示线程的多个状态。

```cpp
enum class cpu_flag : u32
{
    stop,     // 线程未运行（HLE，初始状态）
    exit,     // 不可逆退出
    wait,     // 等待状态，由线程自己设置
    temp,     // 线程在下次 check_state() 后无法正常返回
    pause,    // 线程被 suspend_all 技术暂停
    suspend,  // 线程挂起
    ret,      // 请求回调返回
    again,    // 线程必须在反序列化后完成系统调用
    signal,   // 线程收到信号 (HLE)
    memory,   // 线程必须解锁内存互斥锁
    pending,  // 线程有待处理工作
    pending_recheck, // 线程需要重新检查是否有待处理工作
    notify,   // 仅用于允许在状态上进行原子通知的标志
    yield,    // 线程被请求让出执行时间
    preempt,  // 线程被请求抢占所有 CPU 线程的执行

    dbg_global_pause, // 模拟器暂停
    dbg_pause,        // 线程暂停
    dbg_step,         // 单步执行

    __bitset_enum_max
};
```

#### 状态测试辅助函数
```cpp
// 测试停止状态
constexpr bool is_stopped(bs_t<cpu_flag> state)
{
    return !!(state & (cpu_flag::stop + cpu_flag::exit + cpu_flag::again));
}

// 测试暂停状态
constexpr bool is_paused(bs_t<cpu_flag> state)
{
    return !!(state & (cpu_flag::suspend +
                       cpu_flag::dbg_global_pause +
                       cpu_flag::dbg_pause)) &&
           !is_stopped(state);
}
```

### 3. CPUTranslator - LLVM JIT 翻译器基类

将 PS3 指令翻译为 LLVM IR，然后编译为本地代码。

```cpp
// LLVM 类型概念
template <typename T>
concept LLVMType = (std::is_pointer_v<T>) &&
                   (std::is_base_of_v<llvm::Type, std::remove_pointer_t<T>>);

// LLVM 值概念
template <typename T>
concept LLVMValue = (std::is_pointer_v<T>) &&
                    (std::is_base_of_v<llvm::Value, std::remove_pointer_t<T>>);

// DSL 值概念（领域特定语言）
template <typename T>
concept DSLValue = requires(T& v, llvm::IRBuilder<>* ir) {
    { v.eval(ir) } -> LLVMValue;
};
```

#### 整数位宽模板
```cpp
template <usz N>
struct get_int_bits {};

template <>
struct get_int_bits<1>
{
    using utype = bool;  // 1 位 -> bool
};

template <>
struct get_int_bits<8>
{
    using utype = u8;    // 8 位 -> u8
};

template <>
struct get_int_bits<16>
{
    using utype = u16;   // 16 位 -> u16
};

// ... 等等
```

**学习要点**:
- 使用 C++20 concepts 进行编译期类型检查
- LLVM 翻译器将 PowerPC/SPU 指令转换为 LLVM IR
- 使用模板元编程处理不同位宽的整数类型

---

## 🎮 PPU (PowerPC Processing Unit)

### PPU 特点
- **架构**: 64 位 PowerPC (POWER5 架构)
- **频率**: 3.2 GHz
- **线程**: 2 个硬件线程 (SMT)
- **缓存**: 32 KB L1 指令缓存，32 KB L1 数据缓存，512 KB L2 缓存
- **指令集**: PowerPC 2.02 + VMX (AltiVec)

### PPU 相关文件

#### PPUThread.h/cpp - PPU 线程
```cpp
class ppu_thread : public cpu_thread
{
public:
    // PPU 通用寄存器 (GPR)
    u64 gpr[32]{};

    // PPU 浮点寄存器 (FPR)
    f64 fpr[32]{};

    // PPU 向量寄存器 (VPR) - AltiVec/VMX
    v128 vpr[32]{};

    // 特殊寄存器
    u64 cr{};      // 条件寄存器
    u64 lr{};      // 链接寄存器
    u64 ctr{};     // 计数器寄存器
    u32 xer{};     // 扩展寄存器
    u32 fpscr{};   // 浮点状态控制寄存器
    u32 vscr{};    // 向量状态控制寄存器

    // 程序计数器
    u32 pc{};

    // 执行 PPU 指令
    virtual void cpu_task() override;
};
```

#### PPU 指令格式
PowerPC 指令都是 32 位固定长度：

```cpp
// PPUOpcodes.h
struct ppu_opcode_t
{
    u32 opcode;  // 6 位主操作码
    u32 ra;      // 5 位寄存器 A
    u32 rb;      // 5 位寄存器 B
    u32 rc;      // 5 位寄存器 C
    // ...
};
```

#### PPU 执行模式
1. **解释器模式** (PPUInterpreter.h)
   - 逐条解释执行指令
   - 慢但兼容性好
   - 用于调试

2. **LLVM 重编译模式** (PPUTranslator.cpp)
   - 将 PPU 代码翻译为 LLVM IR
   - LLVM 优化后生成本地代码
   - 快且准确

3. **分析器** (PPUAnalyser.cpp)
   - 分析 PPU 代码
   - 识别函数边界
   - 优化重编译

---

## 🔷 SPU (Synergistic Processing Unit)

### SPU 特点
- **架构**: 128 位 SIMD 处理器
- **数量**: 8 个（PS3 通常只能使用 6-7 个）
- **本地存储**: 每个 SPU 有 256 KB LS (Local Store)
- **寄存器**: 128 个 128 位寄存器
- **频率**: 3.2 GHz
- **指令**: 固定 32 位，所有操作都是 128 位

### SPU 独特设计
- **没有缓存**: 只有 256 KB 本地存储
- **DMA 传输**: 通过 MFC (Memory Flow Controller) 与主内存通信
- **所有操作都是 SIMD**: 即使是标量操作也使用 128 位寄存器
- **分支延迟**: 分支指令有固定延迟

### SPUThread.h/cpp - SPU 线程
```cpp
class spu_thread : public cpu_thread
{
public:
    // SPU 通用寄存器（128 个 128 位寄存器）
    v128 gpr[128]{};

    // 程序计数器
    u32 pc{};

    // 本地存储（256 KB）
    std::shared_ptr<utils::shm> shm;

    // MFC 队列
    struct mfc_cmd
    {
        u64 eah;   // 有效地址高位
        u32 eal;   // 有效地址低位
        u16 tag;   // DMA 标签
        u16 size;  // 传输大小
        // ...
    };

    std::array<mfc_cmd, 16> mfc_queue{};

    // SPU 执行方法
    virtual void cpu_task() override;
};
```

### SPU 执行模式

#### 1. 解释器模式 (SPUInterpreter.cpp)
```cpp
// 逐条解释执行 SPU 指令
// 示例：128 位加法指令
void A(spu_thread& spu, spu_opcode_t op)
{
    // rt = ra + rb (128 位向量加法)
    spu.gpr[op.rt] = spu.gpr[op.ra] + spu.gpr[op.rb];
}
```

#### 2. LLVM 重编译器 (SPULLVMRecompiler.cpp)
- 将 SPU 代码翻译为 LLVM IR
- 利用 LLVM 的优化管道
- 生成高效的本地代码

#### 3. ASMJIT 重编译器 (SPUASMJITRecompiler.cpp)
- 直接生成 x86-64 机器码
- 比 LLVM 更快的编译速度
- 适用于快速重编译场景

### MFC - Memory Flow Controller

SPU 通过 MFC 访问主内存。

```cpp
// MFC 命令类型
enum : u32
{
    MFC_PUT_CMD    = 0x20, // 从 LS 写到主内存
    MFC_GET_CMD    = 0x40, // 从主内存读到 LS
    MFC_BARRIER_CMD = 0xC0, // 内存屏障
    // ...
};

// DMA 传输
void do_dma_transfer(spu_thread& spu, const mfc_cmd& cmd)
{
    // 根据命令类型执行 DMA 传输
    switch (cmd.cmd & 0xFF)
    {
    case MFC_PUT_CMD:
        // 将数据从 LS 复制到主内存
        break;
    case MFC_GET_CMD:
        // 将数据从主内存复制到 LS
        break;
    }
}
```

---

## 🔧 后端实现

### AArch64 后端（ARM64 平台）

在 ARM64 平台上运行时，使用原生 ARM64 JIT。

#### AArch64JIT.h/cpp
```cpp
class aarch64_jit
{
public:
    // 编译 PPU/SPU 代码为 ARM64 机器码
    void compile(u32 addr, const u8* code, u32 size);

    // 执行编译后的代码
    void execute(u32 addr);
};
```

#### AArch64ASM.h/cpp
ARM64 汇编生成器：
```cpp
class aarch64_asm
{
public:
    // 生成加法指令
    void add(reg_t rd, reg_t rn, reg_t rm);

    // 生成加载指令
    void ldr(reg_t rt, reg_t rn, s32 offset);

    // 生成分支指令
    void b(label_t label);
};
```

#### AArch64Signal.h/cpp
处理 ARM64 平台的信号（异常）：
```cpp
// 信号处理器
void handle_access_violation(u64 addr, bool is_write)
{
    // 处理内存访问违规
    // 可能是页面错误，需要映射内存
}
```

---

## 🎓 学习要点

### 1. 理解 PS3 的 Cell 架构
- PPU：通用处理器，运行操作系统和主游戏逻辑
- SPU：专用处理器，处理图形、物理、音频等并行任务
- 异构计算：PPU 和 SPU 协同工作

### 2. JIT 编译概念
```
PS3 机器码
    ↓
[分析器] → 识别函数、基本块
    ↓
[翻译器] → 转换为 LLVM IR
    ↓
[LLVM 优化器] → 优化 IR
    ↓
[代码生成器] → 生成本地机器码
    ↓
本地执行
```

### 3. 位集合状态管理
```cpp
// 设置多个标志
state += cpu_flag::pause;
state += cpu_flag::suspend;

// 测试标志
if (state & cpu_flag::stop)
{
    // 处理停止
}

// 原子操作
state.fetch_add(cpu_flag::signal);
```

### 4. 线程状态转换
```
created → running → wait/suspend → running → finished
                 ↘ pause →
                 ↘ exit (不可逆)
```

### 5. LLVM IR 示例
```cpp
// PPU 加法指令: add r3, r4, r5
// 翻译为 LLVM IR:

%r4 = load i64, i64* %gpr_4
%r5 = load i64, i64* %gpr_5
%result = add i64 %r4, %r5
store i64 %result, i64* %gpr_3
```

---

## 🔍 调试技巧

### 1. 反汇编输出
```cpp
// 使用 PPUDisAsm 查看指令
PPUDisAsm disasm;
disasm.disasm(pc);
std::string instruction = disasm.last_opcode;
```

### 2. 线程状态转储
```cpp
// CPUThread.cpp 中的转储函数
void cpu_thread::dump_all(std::string& out)
{
    fmt::append(out, "Thread ID: 0x%08x\n", id);
    fmt::append(out, "State: %s\n", state);
    fmt::append(out, "PC: 0x%08x\n", pc);
}
```

### 3. 性能分析
```cpp
// 使用性能计数器
LOG_CHANNEL(profiler);
profiler.notice("PPU block compiled: addr=0x%x, size=%u", addr, size);
```

---

## 💻 实际代码示例

### 示例 1: 创建 PPU 线程
```cpp
// 创建 PPU 线程
auto ppu = idm::make_ptr<named_thread<ppu_thread>>(
    "PPU[0x1000000] Main Thread",  // 线程名
    0x1000000,                      // 线程 ID
    entry_point,                    // 入口地址
    stack_addr,                     // 栈地址
    stack_size                      // 栈大小
);

// 启动线程
ppu->run();
```

### 示例 2: SPU DMA 传输
```cpp
// SPU 从主内存加载数据到本地存储
mfc_cmd cmd;
cmd.eal = main_memory_addr;  // 主内存地址
cmd.lsa = 0x0000;             // 本地存储地址
cmd.size = 1024;              // 传输大小
cmd.tag = 0;                  // DMA 标签
cmd.cmd = MFC_GET_CMD;        // GET 命令

// 执行 DMA
spu.do_dma_transfer(cmd);

// 等待 DMA 完成
spu.wait_for_dma_completion(0);
```

### 示例 3: 检查线程状态
```cpp
void some_function(cpu_thread& cpu)
{
    // 定期检查线程状态
    if (cpu.test_stopped())
    {
        // 线程被请求停止
        return;
    }

    // 继续执行...
}
```

---

## 📊 性能考虑

### 1. JIT 缓存
- 编译后的代码被缓存在内存中
- 使用 `block_hash` 标识代码块
- 避免重复编译相同的代码

### 2. 优化级别
- **解释器**: 最慢，但兼容性最好
- **ASMJIT**: 中等速度，编译快
- **LLVM**: 最快，但编译时间较长

### 3. 线程调度
- PPU 线程优先级较高
- SPU 线程可以并行执行
- RSX 线程单独调度

---

## 🔗 相关模块

- **Memory**: 内存管理和虚拟地址转换
- **Cell/lv2**: PS3 操作系统层（系统调用）
- **RSX**: 图形处理单元
- **Loader**: 加载和解析可执行文件

---

## 📚 下一步

- [返回总览](./01-RPCS3-项目总览.md)
- [上一章: Utilities 工具库](./02-Utilities-工具库.md)
- [下一章: RSX 图形系统](./04-RSX-图形系统.md)

---

**提示**: CPU 模拟是 RPCS3 最复杂的部分之一。建议先理解基础的 cpu_thread 和线程状态管理，然后再深入 JIT 编译器的实现细节。
