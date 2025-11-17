# CPUDisAsm.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/CPUDisAsm.h`
- **类型**: 头文件
- **行数**: ~150行
- **所属模块**: CPU 反汇编和调试

## 功能概述

CPUDisAsm.h 定义了一个抽象的 CPU 反汇编接口，用于将机器码解析并转换为可读的汇编指令。这个接口支持多种模式（转储、解释器、正常、编译器等），并集成了调试和性能分析功能。

## 主要内容

### 枚举定义

#### cpu_disasm_mode 枚举
定义了反汇编的不同输出模式：
- **dump**: 转储模式，输出完整的机器码十六进制表示
- **interpreter**: 解释器模式，在每条指令前加上地址和机器码
- **normal**: 普通模式，仅输出汇编助记符
- **compiler_elf**: ELF编译器模式，用于编译输出
- **list**: RSX 专属模式，列表格式输出
- **survey_cmd_size**: RSX 专属模式，用于统计命令大小

### 类定义

#### CPUDisAsm 抽象类

**访问权限**:
- protected: 构造函数、虚方法、内部实现
- public: 接口方法、状态查询

**成员变量**:
```cpp
cpu_disasm_mode m_mode{};              // 当前反汇编模式
const u8* m_offset{};                  // 内存偏移指针
const u32 m_start_pc;                  // 起始程序计数器
std::add_pointer_t<const cpu_thread> m_cpu{};  // CPU 线程指针
shared_ptr<cpu_thread> m_cpu_handle;   // CPU 线程智能指针
u32 m_op = 0;                          // 当前操作码

// 公开成员
std::string last_opcode{};             // 最后一条反汇编指令
u32 dump_pc{};                         // 转储时的程序计数器
```

**构造函数**:
```cpp
protected:
CPUDisAsm(cpu_disasm_mode mode, const u8* offset, u32 start_pc = 0,
          const cpu_thread* cpu = nullptr);
```
- `mode`: 反汇编模式
- `offset`: 内存地址（会减去 start_pc）
- `start_pc`: PC 起始值
- `cpu`: 可选的 CPU 线程上下文

**模式管理**:
```cpp
cpu_disasm_mode change_mode(cpu_disasm_mode mode);  // 切换模式并返回旧模式
const u8* change_ptr(const u8* ptr);                 // 切换指针并返回旧指针
```

**CPU 上下文管理**:
```cpp
cpu_thread* get_cpu() const;                         // 获取 CPU 指针
void set_cpu_handle(shared_ptr<cpu_thread> cpu);    // 设置 CPU 智能指针
```

### 格式化方法

#### format_by_mode()
根据当前模式格式化最后一条指令：
- **dump 模式**: `\t<address>:\t<hex_bytes>\t<instruction>\n`
- **interpreter 模式**: `[<address>]  <hex_bytes>: <instruction>`
- **compiler_elf 模式**: `<instruction>\n`
- **normal 模式**: 仅保留指令文本

**示例**:
```
dump 模式输出:
	0x80000000:	3c 60 80 00	lis r3, 0x8000

interpreter 模式输出:
[0x80000000]  3c 60 80 00: lis r3, 0x8000

normal 模式输出:
lis r3, 0x8000
```

### 工具函数

#### SignedHex 模板函数
```cpp
template <typename T>
requires std::is_integral_v<T>
static std::string SignedHex(T value);
```
将有符号整数转换为十六进制或十进制字符串：
- 如果值是 INT_MIN，返回 "-0x<value>"
- 如果绝对值 < 10，返回十进制
- 否则返回十六进制（带符号）

**示例**:
```cpp
SignedHex(5) -> "5"
SignedHex(-256) -> "-0x100"
SignedHex(-1) -> "-0x1"
```

#### PadOp 函数
```cpp
int PadOp(std::string_view op = {}, int min_spaces = 0) const;
```
计算指令格式所需的填充空间：
- normal 模式: `op.size() + min_spaces`
- 其他模式: 固定 10 个字符

用于对齐输出格式中的操作数。

### 虚函数接口

**必须由派生类实现**:

```cpp
virtual u32 disasm(u32 pc) = 0;
```
反汇编一条指令，返回指令字节大小。

**参数**:
- `pc`: 要反汇编的程序计数器
- 返回: 指令的字节大小（通常为 4，可变指令集可能不同）

```cpp
virtual std::pair<const void*, usz> get_memory_span() const = 0;
```
获取反汇编器的内存范围。

**返回值**:
- `first`: 内存起始指针
- `second`: 内存大小

```cpp
virtual std::unique_ptr<CPUDisAsm> copy_type_erased() const = 0;
```
创建一个类型擦除的反汇编器副本（用于多态复制）。

### 虚方法

```cpp
virtual u32 DisAsmBranchTarget(s32 imm);
```
计算分支目标地址（基类实现返回 0）。

## 代码分析

### 设计模式
1. **模板方法模式**: format_by_mode() 根据 m_mode 调用不同的格式化方式
2. **策略模式**: 不同的 cpu_disasm_mode 代表不同的输出策略
3. **抽象工厂**: copy_type_erased() 支持多态对象克隆

### 用途和应用场景

1. **调试器集成**:
   - 在调试会话中显示当前执行的指令
   - normal 模式提供清晰的汇编输出

2. **转储分析**:
   - dump 模式用于生成完整的代码转储
   - 包含地址和原始机器码便于分析

3. **解释器日志**:
   - interpreter 模式用于逐指令跟踪执行
   - 带有完整的地址和机器码信息

4. **编译器输出**:
   - compiler_elf 模式用于编译结果验证
   - 适合 ELF 二进制生成

5. **性能分析**:
   - 与 CPU 线程的 block_hash 配合
   - 帮助分析热点代码

### 内存管理
- 使用 shared_ptr 管理 CPU 线程生命周期
- m_cpu_handle 确保反汇编器持有有效的 CPU 引用
- m_cpu 指针用于快速访问

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.h` - CPU 线程定义
- `/home/user/rpcs3/rpcs3/Emu/Cell/PPUDisasm.h` - PPU 反汇编实现
- `/home/user/rpcs3/rpcs3/Emu/Cell/SPUDisasm.h` - SPU 反汇编实现
- `/home/user/rpcs3/rpcs3/Emu/RSX/RSXDisAsm.h` - RSX 反汇编实现

## 学习要点

1. **反汇编器架构**: 如何设计支持多种架构的统一反汇编接口
2. **输出格式控制**: 使用模式枚举实现灵活的输出格式转换
3. **内存管理**: CPU 线程上下文的安全管理和生命周期
4. **调试工具设计**: 为调试器和分析工具提供的接口抽象
5. **指令格式化**: SignedHex 和 PadOp 等工具函数的使用
