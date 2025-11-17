# CPUThread.cpp

## 文件信息
- **路径**: `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.cpp`
- **类型**: 源文件
- **行数**: ~1750行
- **所属模块**: CPU 模拟核心

## 功能概述

CPUThread.cpp 是 CPU 线程管理的实现文件，包含线程状态管理、挂起机制、性能分析和线程同步的具体实现。主要负责 CPU 线程的生命周期管理、状态检查和全局挂起操作。

## 主要内容

### 全局状态管理

#### 线程计数与统计
```cpp
atomic_t<u64> cpu_thread::g_threads_created{0};
atomic_t<u64> cpu_thread::g_threads_deleted{0};
atomic_t<u64> cpu_thread::g_suspend_counter{0};
```

#### 线程局部存储
```cpp
thread_local u32 s_tls_thread_slot = -1;        // 线程在挂起列表中的槽位
thread_local u64 s_tls_sctr = -1;               // 挂起计数器时间戳
thread_local cpu_thread* g_tls_this_thread;     // 当前线程指针
```

#### 全局挂起状态
```cpp
static atomic_t<cpu_thread::suspend_work*> s_pushed{};    // 待处理工作队列头部
static shared_mutex s_cpu_lock;                           // CPU 操作锁
static atomic_t<u128> s_cpu_bits{};                        // CPU 位图（最多128个线程）
static atomic_t<cpu_thread*> s_cpu_list[128]{};          // CPU 线程数组
```

### 核心类和结构体

#### cpu_prof 结构体 - CPU 性能分析器
**职责**: 在后台线程中采样 CPU 线程的执行情况

**关键成员**:
- `lf_queue<u32> registered`: 注册用于分析的线程ID队列
- `sample_info all_threads_info`: 所有线程的聚合信息
- `std::unordered_map<shared_ptr<cpu_thread>, sample_info> threads`: 线程信息映射

**sample_info 结构体**:
- `std::unordered_map<u64, u64> freq`: 块哈希到样本计数的映射（CPU代码热点）
- `u64 samples, idle, reservation_samples`: 各类样本计数
- `u64 new_samples`: 自上次打印以来的新样本数

**分析工作流**:
1. 定期采样每个线程的 block_hash
2. 统计执行频率
3. 如果 idle 时间过长，记录为 idle
4. 如果在 SPU 预留操作中，记录为 reservation_samples

#### cpu_counter 命名空间
提供线程计数和悬挂列表管理：

**add(cpu_thread* _this)**
- 将线程注册到全局 CPU 列表
- 为线程分配一个槽位（0-127）
- 管理位图 s_cpu_bits

**remove(cpu_thread* _this)**
- 从全局列表中注销线程
- 释放分配的槽位

**for_all_cpu(u128 copy, F func)**
- 遍历所有活跃 CPU 线程
- 支持两种回调签名：`F(cpu_thread*)` 或 `F(cpu_thread*, u32 index)`
- 用于批量操作所有线程

### 关键实现

#### 构造函数 - cpu_thread::cpu_thread(u32 id)
```cpp
- 初始化线程ID
- 处理竞态条件（暂停/退出状态）
- 初始化 dbg_step_pc
- 更新 g_threads_created 计数
```

#### 运算符重载 - cpu_thread::operator()()
线程入口点的实现：
1. 注册分析器（如果启用）
2. 设置线程亲和性
3. 执行主线程循环：
   - 检查 cpu_flag::exit
   - 调用 cpu_task()
   - 处理返回标志
4. 进行清理

#### 状态检查 - cpu_thread::check_state() noexcept
这是最复杂的方法，处理所有线程状态标志：

**状态转换逻辑**:
```
1. 如果设置了 pause 标志：
   - 保存挂起计数器快照
   - 等待挂起操作完成

2. 如果设置了 temp 标志：
   - 不允许返回 true（线程不能停止）

3. 如果设置了 dbg_step 标志：
   - 检查 PC 是否改变
   - 如果改变，设置 dbg_pause

4. 如果设置了内存标志：
   - 获取 VM 被动锁

5. 如果设置了 preempt 标志：
   - 给所有其他线程设置 yield 标志
```

**核心逻辑决策**:
- 如果线程未停止且没有 ret 标志，检查暂停标志
- 如果有暂停标志，设置 wait 并留在 check_state() 中
- 否则继续执行

#### 全局挂起 - cpu_thread::suspend_work::push()
实现全局线程同步操作：

**步骤**:
1. **初始化**: 如果是第一个 work，获取 s_cpu_lock
2. **收集线程**: 预取所有 CPU 的 state 字段
3. **递增计数器**: g_suspend_counter += 2（初始化）
4. **设置暂停标志**: 对所有线程设置 cpu_flag::pause
5. **等待确认**: 等待所有线程设置 wait 标志
6. **执行工作**: 按优先级执行所有待处理的 work
7. **递增计数器**: g_suspend_counter++（第二次递增）
8. **清除暂停**: 从所有线程移除 pause 标志
9. **唤醒线程**: 通知所有线程

### 转储和调试功能

#### dump_all(std::string& ret)
完整的 CPU 状态转储，包括：
- 杂项信息（type, state）
- 寄存器状态
- 调用栈
- 当前代码片段（反汇编）

#### dump_regs()
获取寄存器转储（由派生类实现）

#### dump_callstack()
获取格式化的调用栈字符串

#### dump_misc()
获取线程类型和状态信息

## 代码分析

### 线程同步策略
1. **分层锁定**: 使用 s_cpu_lock（shared_mutex）保护全局操作
2. **位图管理**: 使用 u128 位图快速查询活跃线程
3. **计数器方案**: 使用 g_suspend_counter 的奇偶性指示挂起进度

### 性能优化
1. **预取优化**: 在并发操作前预取 CPU->state 地址
2. **忙等待策略**: 使用 busy_wait 和 atomic_wait 混合策略
3. **线程本地缓存**: s_tls_sctr 缓存挂起计数快照

### 内存同步
- 使用 atomic_storage<> 确保原子读写
- VM 被动锁处理内存预留操作
- 通知机制用于线程唤醒

## 相关文件
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUThread.h` - 头文件声明
- `/home/user/rpcs3/rpcs3/Emu/CPU/CPUDisAsm.h` - 反汇编接口
- `/home/user/rpcs3/rpcs3/Emu/Cell/PPUThread.h` - PPU 实现
- `/home/user/rpcs3/rpcs3/Emu/Cell/SPUThread.h` - SPU 实现
- `/home/user/rpcs3/rpcs3/Emu/Memory/vm_locking.h` - VM 锁定
- `/home/user/rpcs3/rpcs3/Emu/perf_meter.hpp` - 性能计量

## 学习要点

1. **全局挂起实现**: 如何在无锁环境中同步所有线程
2. **性能分析集成**: 低开销的采样分析实现
3. **复杂状态机**: 16+ 种状态标志的协调
4. **线程本地存储**: 为每个线程缓存频繁访问的数据
5. **竞态条件处理**: 构造函数中的同步问题解决
6. **采样分析器**: 后台采样线程执行的实现方式
