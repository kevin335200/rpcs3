# Utilities 工具库模块

## 📌 模块概述

Utilities 模块是 RPCS3 项目的基础设施层，提供整个项目所需的底层工具和抽象。这个模块包含了线程管理、文件操作、同步原语、配置系统等核心功能。

**位置**: `/Utilities/`

## 📂 文件列表

### 核心工具类
| 文件 | 用途 | 难度 |
|------|------|------|
| **types.hpp** | 基础类型定义 | ⭐ |
| **Thread.h/cpp** | 线程管理系统 | ⭐⭐⭐ |
| **File.h/cpp** | 文件系统抽象 | ⭐⭐ |
| **Config.h/cpp** | 配置系统 | ⭐⭐⭐ |
| **mutex.h/cpp** | 互斥锁 | ⭐⭐⭐ |
| **cond.h/cpp** | 条件变量 | ⭐⭐⭐ |
| **sema.h/cpp** | 信号量 | ⭐⭐ |
| **StrFmt.h/cpp** | 字符串格式化 | ⭐⭐ |
| **StrUtil.h** | 字符串工具 | ⭐ |

### JIT 相关
| 文件 | 用途 | 难度 |
|------|------|------|
| **JIT.h** | JIT 接口 | ⭐⭐⭐⭐ |
| **JITLLVM.cpp** | LLVM JIT 实现 | ⭐⭐⭐⭐⭐ |
| **JITASM.cpp** | 汇编 JIT | ⭐⭐⭐⭐ |

### 数据结构
| 文件 | 用途 | 难度 |
|------|------|------|
| **bit_set.h** | 位集合 | ⭐⭐ |
| **lockless.h** | 无锁数据结构 | ⭐⭐⭐⭐ |
| **simple_ringbuf.h/cpp** | 环形缓冲区 | ⭐⭐ |

### 其他工具
| 文件 | 用途 | 难度 |
|------|------|------|
| **Timer.h** | 计时器 | ⭐ |
| **version.h/cpp** | 版本信息 | ⭐ |
| **stack_trace.h/cpp** | 堆栈跟踪 | ⭐⭐⭐ |
| **bin_patch.h/cpp** | 二进制补丁 | ⭐⭐⭐ |
| **rXml.h/cpp** | XML 解析 | ⭐⭐ |

## 🔍 核心文件详解

### 1. util/types.hpp - 基础类型定义

这是整个项目的类型系统基础。

#### 基本类型别名
```cpp
// 有符号整数
using s8  = std::int8_t;    // 8位有符号
using s16 = std::int16_t;   // 16位有符号
using s32 = std::int32_t;   // 32位有符号
using s64 = std::int64_t;   // 64位有符号
using ssz = std::make_signed_t<std::size_t>; // 有符号 size_t

// 无符号整数
using u8  = std::uint8_t;   // 8位无符号
using u16 = std::uint16_t;  // 16位无符号
using u32 = std::uint32_t;  // 32位无符号
using u64 = std::uint64_t;  // 64位无符号
using usz = std::size_t;    // size_t 别名

// 其他类型
using uptr = std::uintptr_t; // 指针大小的整数
using schar  = signed char;
using uchar  = unsigned char;
using ushort = unsigned short;
using uint   = unsigned int;
```

#### 平台检测宏
```cpp
#if defined(__SSE2__) || defined(_M_X64) || ...
#define ARCH_X64 1       // x86-64 平台
#elif defined(__aarch64__) || ...
#define ARCH_ARM64 1     // ARM64 平台
#endif
```

#### 编译器属性宏
```cpp
#define FORCE_INLINE __forceinline         // 强制内联
#define NEVER_INLINE __declspec(noinline)  // 禁止内联
#define SAFE_BUFFERS(...) __declspec(safebuffers) // 缓冲区安全
```

#### 实用工具宏
```cpp
// 检查类型大小
#define CHECK_SIZE(type, size) static_assert(sizeof(type) == size, ...)

// 检查类型对齐
#define CHECK_ALIGN(type, align) static_assert(alignof(type) == align, ...)

// 简化 switch-case 字符串化
#define STR_CASE(...) case __VA_ARGS__: return #__VA_ARGS__

// Lambda 简化宏 - 非常实用！
#define FN(...) ::utils::fn_helper([&](...){ return (__VA_ARGS__); })
```

**学习要点**:
- RPCS3 使用这些短类型别名而非标准类型
- `u32`, `s64` 等比 `uint32_t` 更简洁
- 这是整个项目的类型基础，必须首先理解

---

### 2. Thread.h/cpp - 线程管理系统

线程系统是 RPCS3 的核心基础设施之一。

#### 线程类别枚举
```cpp
enum class thread_class : u32
{
    general = 0,    // 通用线程
    ppu = 1,        // PPU (PowerPC) 线程
    spu = 2,        // SPU 线程
    rsx = 0x55,     // RSX 图形线程
};
```

#### 线程状态枚举
```cpp
enum class thread_state : u32
{
    created = 0,   // 初始状态
    aborting = 1,  // 正在中止
    errored = 2,   // 错误状态
    finished = 3,  // 完成状态
    mask = 3,
    destroying_context = 7, // 销毁上下文
};
```

#### 核心布局枚举
```cpp
enum class native_core_arrangement : u32
{
    undefined,  // 未定义
    generic,    // 通用布局
    intel_ht,   // Intel 超线程
    amd_ccx     // AMD CCX 架构
};
```

#### 命名线程模板
```cpp
template <class Context>
class named_thread
{
    // 带有名称的线程抽象
    // Context: 线程执行的上下文类
};
```

#### 结果存储
```cpp
template <typename Ctx, typename... Args>
struct result_storage
{
    // 存储线程执行结果
    // 如果返回 void 则 empty = true
    // 否则使用 placement new 在 data 中构造结果
};
```

#### 任务队列（Future）
```cpp
class thread_future
{
    shared_ptr<thread_future> next{}; // 链表下一个节点
    thread_future* prev{};            // 链表前一个节点

    atomic_t<void(*)(const thread_base*, thread_future*)> exec{};
    // 原子执行函数指针
};
```

**学习要点**:
- 理解线程状态转换
- `named_thread` 是模板类，可以绑定任何可调用对象
- 使用链表实现任务队列
- 原子操作保证线程安全

---

### 3. File.h/cpp - 文件系统抽象

跨平台的文件系统抽象层。

#### 文件打开模式
```cpp
namespace fs
{
    enum class open_mode : u32
    {
        read,    // 读取
        write,   // 写入
        append,  // 追加
        create,  // 创建
        trunc,   // 截断
        excl,    // 排他（与 create 配合使用）
        lock,    // 锁定
        unread,  // 禁止读取
        isfile,  // 确保是文件而非目录
    };

    // 常用组合
    constexpr auto write_new = write + create + excl; // 创建新文件
    constexpr auto rewrite = write + create + trunc;  // 覆盖写入
}
```

**注意**: 这里使用了位集合（bitset），可以用 `+` 运算符组合标志。

#### 文件定位模式
```cpp
enum class seek_mode : u32
{
    seek_set, // 从文件开始
    seek_cur, // 从当前位置
    seek_end, // 从文件末尾
};
```

#### 文件属性结构
```cpp
struct stat_t
{
    bool is_directory; // 是否是目录
    bool is_symlink;   // 是否是符号链接
    bool is_writable;  // 是否可写
    u64 size;          // 文件大小
    s64 atime;         // 访问时间
    s64 mtime;         // 修改时间
    s64 ctime;         // 创建时间

    // 使用 enable_bitcopy 表示可以按位复制
    using enable_bitcopy = std::true_type;
};
```

#### 文件句柄基类
```cpp
struct file_base
{
    virtual ~file_base();

    virtual stat_t get_stat();                        // 获取文件信息
    virtual void sync();                              // 同步到磁盘
    virtual bool trunc(u64 length) = 0;               // 截断文件
    virtual u64 read(void* buffer, u64 size) = 0;     // 读取
    virtual u64 read_at(u64 offset, void* buffer, u64 size) = 0; // 定位读
    virtual u64 write(const void* buffer, u64 size) = 0; // 写入
    virtual u64 seek(s64 offset, seek_mode whence) = 0;  // 定位
    virtual u64 size() = 0;                           // 获取大小
    virtual native_handle get_handle();               // 获取原生句柄
    virtual file_id get_id();                         // 获取文件ID
    virtual u64 write_gather(const iovec_clone* buffers, u64 buf_count); // 聚集写
};
```

#### 目录条目
```cpp
struct dir_entry : stat_t
{
    std::string name{}; // 文件/目录名

    // 不能按位复制（包含 std::string）
    using enable_bitcopy = std::false_type;
};
```

#### 平台差异
```cpp
#ifdef _WIN32
    static constexpr auto& delim = "/\\";   // Windows 路径分隔符
    using native_handle = void*;            // Windows HANDLE
#else
    static constexpr auto& delim = "/";     // Unix 路径分隔符
    using native_handle = int;              // Unix 文件描述符
#endif
```

**学习要点**:
- 使用虚函数实现跨平台抽象
- `file_base` 是抽象基类，具体实现在 .cpp 文件中
- 使用 `enable_bitcopy` 特性标记类型是否可按位复制
- 位集合枚举允许组合多个标志

---

### 4. mutex.h/cpp - 共享互斥锁

小尺寸（仅 4 字节）的共享互斥锁实现。

#### 共享互斥锁
```cpp
class shared_mutex final
{
    enum : u32
    {
        c_one = 1u << 14, // 固定点 1.0 值（表示一个写者）
        c_sig = 1u << 30, // 信号位
        c_err = 1u << 31, // 错误位
    };

    atomic_t<u32> m_value{}; // 原子计数器

public:
    // 尝试获取共享锁（读锁）
    bool try_lock_shared()
    {
        const u32 value = m_value.load();
        // 如果读者数量 < c_one - 1，则可以获取
        return value < c_one - 1 &&
               m_value.compare_and_swap_test(value, value + 1);
    }

    // 获取共享锁
    void lock_shared()
    {
        const u32 value = m_value.load();
        if (value >= c_one - 1 ||
            !m_value.compare_and_swap_test(value, value + 1))
        {
            imp_lock_shared(value); // 慢路径
        }
    }

    // 释放共享锁
    void unlock_shared()
    {
        const u32 value = m_value.fetch_sub(1);
        if (value >= c_one) [[unlikely]]
        {
            imp_unlock_shared(value);
        }
    }

    // 获取独占锁（写锁）
    void lock()
    {
        const u32 value = m_value.compare_and_swap(0, c_one);
        if (value) [[unlikely]]
        {
            imp_lock(value);
        }
    }
};
```

#### HLE 优化版本
```cpp
// HLE (Hardware Lock Elision) - Intel TSX 优化
void lock_shared_hle()
{
    const u32 value = m_value.load();
    if (value < c_one - 1) [[likely]]
    {
        u32 old = value;
        if (atomic_storage<u32>::compare_exchange_hle_acq(
            m_value.raw(), old, value + 1)) [[likely]]
        {
            return; // 快路径成功
        }
    }
    imp_lock_shared(value); // 回退到慢路径
}
```

**学习要点**:
- 使用固定点表示法：`c_one = 1 << 14`
- 读者计数在低位，写者在高位
- 使用 CAS (Compare-And-Swap) 实现无锁快路径
- `[[likely]]` 和 `[[unlikely]]` 是 C++20 分支预测提示
- HLE 利用硬件事务内存加速

---

### 5. Config.h/cpp - 配置系统

YAML 配置树系统。

#### 配置类型枚举
```cpp
namespace cfg
{
    enum class type : unsigned
    {
        node = 0,    // 配置节点（容器）
        _bool,       // 布尔值
        _enum,       // 枚举值
        _int,        // 整数
        uint,        // 无符号整数
        uint128,     // 128位整数
        string,      // 字符串
        set,         // 集合
        map,         // 映射
        node_map,    // 节点映射
        log,         // 日志条目
        device,      // 设备条目
    };
}
```

#### 配置基类
```cpp
class _base
{
    const type m_type{};        // 配置类型
    _base* m_parent = nullptr;  // 父节点
    bool m_dynamic = true;      // 是否动态（运行时可修改）
    const std::string m_name{}; // 配置项名称
    u32 m_id = 0;               // 唯一 ID

public:
    // 获取类型
    type get_type() const { return m_type; }

    // 获取名称
    const std::string& get_name() const { return m_name; }

    // 重置为默认值
    virtual void from_default() = 0;

    // 恢复默认成员
    virtual void restore_defaults() = 0;

    // 转换为字符串
    virtual std::string to_string() const { return {}; }
};
```

**学习要点**:
- 使用继承和多态实现配置树
- 每个配置项都有唯一 ID
- `m_dynamic` 表示是否可在游戏运行时修改
- 所有配置项都可以序列化为字符串

---

## 🎯 模块间关系

```
types.hpp (基础类型)
    ↓
atomic.hpp (原子操作)
    ↓
Thread.h (线程系统) ← mutex.h (互斥锁)
    ↓                      ↓
CPUThread (CPU线程)    File.h (文件系统)
                           ↓
                       Config.h (配置)
```

## 💡 C++ 学习重点

### 1. 类型别名 (Type Aliases)
```cpp
using u32 = std::uint32_t;  // 推荐使用 using
typedef std::uint32_t u32;  // 旧式写法
```

### 2. 枚举类 (Enum Class)
```cpp
enum class thread_state : u32  // 指定底层类型
{
    created = 0,
    // ...
};

// 使用时需要完全限定
thread_state::created
```

### 3. 虚函数和纯虚函数
```cpp
class file_base
{
    // 纯虚函数 - 必须在派生类中实现
    virtual u64 read(void* buffer, u64 size) = 0;

    // 虚函数 - 可以在派生类中覆盖
    virtual void sync();
};
```

### 4. 模板编程
```cpp
template <typename Ctx, typename... Args>
struct result_storage
{
    // 可变参数模板
    // 编译期计算
};
```

### 5. constexpr 和 consteval
```cpp
constexpr auto read = +open_mode::read; // 编译期常量
static constexpr auto& delim = "/\\";   // 静态编译期常量
```

### 6. 原子操作
```cpp
atomic_t<u32> m_value{};           // 原子变量
m_value.load();                    // 原子读取
m_value.fetch_sub(1);              // 原子减法
m_value.compare_and_swap(0, 1);    // CAS 操作
```

### 7. C++20 特性
```cpp
// 三路比较运算符
constexpr bool operator==(const stat_t&) const = default;

// 分支预测
if (value >= c_one) [[unlikely]] { ... }

// Concepts
template <typename T>
concept NamedThreadName = requires (const T&)
{
    std::string(T::thread_name);
};
```

## 🔧 实践建议

### 新手入门顺序
1. **types.hpp** - 理解基础类型系统
2. **StrUtil.h** - 简单的字符串工具
3. **Timer.h** - 计时器的使用
4. **File.h** - 文件操作（熟悉虚函数）
5. **mutex.h** - 理解同步原语
6. **Thread.h** - 复杂的线程系统
7. **Config.h** - 配置树系统

### 调试技巧
```cpp
// 1. 添加日志
#include "util/logs.hpp"
cfg_log.notice("File opened: %s", filename);

// 2. 使用断言
AUDIT(value < max_value); // 调试模式检查

// 3. 检查类型大小
CHECK_SIZE(stat_t, 40);  // 编译期检查
```

### 常见陷阱
1. **别忘记 virtual 析构函数**: 基类需要虚析构
2. **注意枚举类作用域**: `thread_state::created` 而非 `created`
3. **理解原子操作**: 不能假设操作顺序
4. **小心线程安全**: 多线程环境下需要同步

## 📚 相关文档

- [下一章: CPU 模拟模块](./03-CPU-模拟.md)
- [返回总览](./01-RPCS3-项目总览.md)

## 📖 参考资源

- C++20 标准
- Intel 线程构建块 (TBB) 文档
- POSIX 线程编程指南
- YAML 1.2 规范

---

**提示**: Utilities 模块是理解整个项目的基础，建议花时间仔细研究这些基础设施代码。
