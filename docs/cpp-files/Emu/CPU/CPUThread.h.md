# CPUThread.h

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.h`
- **类型**: 头文件
- **行数**: ~314行
- **所属模块**: CPU 模拟核心

## 功能概述

CPUThread.h 是 RPCS3 CPU 模拟的核心基类定义文件。它定义了 CPU 线程的基础结构、状态管理、标志位控制和线程生命周期管理。该文件为 PPU、SPU 和 RSX 线程提供统一的接口。

## 主要内容

### 枚举和标志位

#### cpu_flag 枚举
定义了 CPU 线程的各种状态标志：
- **stop**: 线程未运行（HLE、初始状态）
- **exit**: 不可逆的退出
- **wait**: 等待状态，由线程自身设置
- **temp**: 线程无法在 check_state() 后正确返回的临时标志
- **pause**: 线程被 suspend_all 挂起
- **suspend**: 线程挂起
- **ret**: 回调返回请求
- **again**: 线程必须在反序列化后完成系统调用
- **signal**: 线程收到信号（HLE）
- **memory**: 线程必须解锁内存互斥锁
- **pending**: 线程有待处理工作
- **pending_recheck**: 线程需要在 ::pending 移除前重新检查待处理工作
- **notify**: 原子通知状态的标志
- **yield**: 线程被请求让出执行时间
- **preempt**: 线程被请求抢占所有 CPU 线程
- **dbg_global_pause**: 全局模拟暂停
- **dbg_pause**: 线程暂停
- **dbg_step**: 线程强制单步暂停

#### 状态测试函数
- `is_stopped(bs_t<cpu_flag> state)`: 测试线程停止状态
- `is_paused(bs_t<cpu_flag> state)`: 测试线程暂停状态

### 类定义

#### cpu_thread 类
**基础字段**:
- `u64 block_hash`: 当前执行块的哈希值（用于性能分析）
- `const u32 id`: 线程ID
- `atomic_bs_t<cpu_flag> state`: 原子线程状态

**关键方法**:
- `bool check_state() noexcept`: 处理线程状态，返回检查器是否必须返回
- `bool test_stopped()`: 测试线程是否停止（非阻塞）
- `u32 get_pc() const`: 获取当前程序计数器
- `u32* get_pc2()`: 获取调试器的最后 PC（用于单步）
- `cpu_thread* get_next_cpu()`: 访问 next_cpu 成员
- `void notify()`: 通知线程状态变化
- `void add_remove_flags()`: 原子添加/删除 CPU 状态标志

**虚函数接口**:
- `virtual void cpu_task() = 0`: 线程入口点（由派生类实现）
- `virtual void cpu_sleep()`: cpu_flag::suspend 回调
- `virtual void cpu_work()`: cpu_flag::pending 回调
- `virtual void cpu_return()`: cpu_flag::ret 回调
- `virtual void cpu_wait(bs_t<cpu_flag> old)`: RSX 等待回调
- `virtual void cpu_on_stop()`: 线程停止回调
- `virtual void dump_all(std::string&) const`: 获取完整 CPU 状态转储
- `virtual void dump_regs(std::string& ret, std::any& custom_data) const`: 获取寄存器转储
- `virtual std::string dump_callstack() const`: 获取调用栈转储
- `virtual std::vector<std::pair<u32, u32>> dump_callstack_list() const`: 获取调用栈列表
- `virtual std::string dump_misc() const`: 获取杂项信息转储

**悬挂机制**:
```cpp
suspend_work 结构体 {
    u8 prio;                      // 任务优先级
    bool cancel_if_not_suspended; // 如果未挂起则取消
    bool was_posted;              // 是否已发布
    u32 prf_size;                 // 预取列表大小
    void* const* prf_list;        // 预取列表
    void* func_ptr;               // 函数指针
    void* res_buf;                // 结果缓冲区
    void (*exec)(void*, void*);   // 执行函数
    suspend_work* next;           // 链表中的下一个
    bool push(cpu_thread*) noexcept;
};
```

**静态方法**:
- `template<u8 Prio=0, typename F> static auto suspend_all()`: 挂起所有线程并执行操作
- `template<u8 Prio=0, typename F> static suspend_work suspend_post()`: 发布待处理工作
- `template<u8 Prio=0, typename F> static bool if_suspended()`: 仅在线程被挂起时执行
- `static void cleanup() noexcept`: 清理线程计数信息
- `static void flush_profilers() noexcept`: 向分析器发送刷新信号
- `template<DerivedFrom<cpu_thread> T> static T* get_current()`: 获取当前线程

### 线程计数统计
```cpp
static atomic_t<u64> g_threads_created;    // 已创建线程总数
static atomic_t<u64> g_threads_deleted;    // 已删除线程总数
static atomic_t<u64> g_suspend_counter;    // 挂起计数器
```

### 模板支持
- **DerivedFrom 概念**: 用于编译时验证继承关系
- **try_get<T>()**: 安全地尝试转换为派生类型
- **id_type()**: 从线程 ID 提取类型信息

## 代码分析

### 核心设计模式

1. **原子状态管理**: 使用 `atomic_bs_t<cpu_flag>` 实现线程安全的状态管理
2. **虚函数接口**: 定义统一的 CPU 线程接口，支持 PPU、SPU、RSX 等不同架构
3. **类型安全的强制转换**: 通过 `try_get<T>()` 模板提供安全的派生类访问
4. **全局挂起机制**: `suspend_all()` 支持在保持所有 CPU 线程同步的情况下执行全局操作

### 状态流转
```
初始: stop + wait
↓
运行: cpu_task() 执行
↓
检查: check_state() 处理各种标志
↓
暂停/等待: suspend、dbg_pause、yield 等
↓
退出: exit 标志
```

### 性能特性
- **低开销的原子操作**: 使用 fetch_op 等原子操作最小化锁定
- **SIMD 亲和性**: 支持线程亲和性设置
- **分析集成**: 内建性能计数器支持（block_hash 用于采样）

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.cpp` - 实现文件
- `/home/user/rpcs3/rpcs3/Emu/Cell/PPUThread.h` - PPU 线程实现
- `/home/user/rpcs3/rpcs3/Emu/Cell/SPUThread.h` - SPU 线程实现
- `/home/user/rpcs3/rpcs3/Emu/RSX/RSXThread.h` - RSX 线程实现
- `/home/user/rpcs3/rpcs3/Emu/Memory/vm_locking.h` - 内存锁定机制

## 学习要点

1. **CPU 线程模型**: RPCS3 如何统一管理不同类型的 CPU 线程
2. **原子状态管理**: 无锁编程中的状态同步技术
3. **虚拟机线程管理**: 仿真器线程与主机操作系统线程的交互
4. **性能分析**: 通过块哈希进行低开销的采样分析
5. **同步原语**: fetch_op 等高性能原子操作的使用
6. **内存同步**: 通过 vm_locking 确保内存操作的原子性
