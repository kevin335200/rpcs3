# Cell 处理器模块

## 📌 模块概述

Cell 模块实现了 PlayStation 3 的 Cell 处理器架构，包括操作系统层（Lv2 Kernel）、系统调用、以及各种 HLE (High-Level Emulation) 模块。

**位置**: `/rpcs3/Emu/Cell/`

## 🏗️ Cell 架构层次

```
┌─────────────────────────────────────────┐
│          PS3 应用程序                    │
├─────────────────────────────────────────┤
│       Lv2 Kernel (操作系统)              │
│  - 进程/线程管理                          │
│  - 内存管理                              │
│  - 系统调用                              │
├─────────────────────────────────────────┤
│         HLE 模块 (系统库)                 │
│  - cellFs (文件系统)                     │
│  - cellGame (游戏)                       │
│  - cellAudio (音频)                      │
│  - cellGcmSys (图形)                     │
│  - ... 100+ 模块                         │
├─────────────────────────────────────────┤
│      硬件抽象层                           │
│  - PPU/SPU 线程                          │
│  - MFC (内存流控制)                       │
└─────────────────────────────────────────┘
```

## 📂 目录结构

```
rpcs3/Emu/Cell/
├── PPU相关
│   ├── PPUThread.h/cpp        # PPU 线程实现
│   ├── PPUInterpreter.h       # PPU 解释器
│   ├── PPUTranslator.cpp      # PPU LLVM 翻译器
│   ├── PPUAnalyser.cpp        # PPU 代码分析
│   ├── PPUDisAsm.h/cpp        # PPU 反汇编
│   ├── PPUOpcodes.h           # PPU 指令定义
│   ├── PPUFunction.h          # PPU 函数信息
│   └── PPUCallback.h          # PPU 回调
│
├── SPU相关
│   ├── SPUThread.h/cpp        # SPU 线程实现
│   ├── SPUInterpreter.h/cpp   # SPU 解释器
│   ├── SPULLVMRecompiler.cpp  # SPU LLVM 重编译
│   ├── SPUASMJITRecompiler.h/cpp # SPU ASMJIT 重编译
│   ├── SPUCommonRecompiler.cpp   # SPU 公共重编译
│   ├── SPUAnalyser.h          # SPU 代码分析
│   ├── SPUDisAsm.h/cpp        # SPU 反汇编
│   ├── RawSPUThread.cpp       # Raw SPU 线程
│   └── SPURecompiler.h        # SPU 重编译器接口
│
├── 系统层
│   ├── lv2/                   # Lv2 Kernel
│   │   ├── sys_event.h/cpp        # 事件队列
│   │   ├── sys_lwmutex.h/cpp      # 轻量互斥锁
│   │   ├── sys_mutex.h/cpp        # 互斥锁
│   │   ├── sys_cond.h/cpp         # 条件变量
│   │   ├── sys_semaphore.h/cpp    # 信号量
│   │   ├── sys_rwlock.h/cpp       # 读写锁
│   │   ├── sys_memory.h/cpp       # 内存管理
│   │   ├── sys_process.h/cpp      # 进程管理
│   │   ├── sys_ppu_thread.h/cpp   # PPU 线程管理
│   │   ├── sys_spu.h/cpp          # SPU 管理
│   │   ├── sys_fs.h/cpp           # 文件系统
│   │   ├── sys_timer.h/cpp        # 计时器
│   │   ├── sys_time.h/cpp         # 时间
│   │   └── sys_net/               # 网络子系统
│   │
│   └── Modules/               # HLE 模块
│       ├── cellFs.h/cpp           # 文件系统
│       ├── cellGame.h/cpp         # 游戏相关
│       ├── cellAudio.h/cpp        # 音频
│       ├── cellGcmSys.h/cpp       # GCM 系统
│       ├── cellSysutil.h/cpp      # 系统工具
│       ├── cellPad.h/cpp          # 手柄
│       ├── cellKb.h/cpp           # 键盘
│       ├── cellMouse.h/cpp        # 鼠标
│       ├── cellFont.h/cpp         # 字体
│       ├── cellJpgDec.h/cpp       # JPEG 解码
│       ├── cellPngDec.h/cpp       # PNG 解码
│       └── ... (100+ 模块)
│
├── 其他
│   ├── Common.h               # 通用定义
│   ├── ErrorCodes.h/cpp       # 错误代码
│   └── MFC.h/cpp              # 内存流控制器
```

## 🎯 Lv2 系统调用

### sys_ppu_thread - PPU 线程管理

```cpp
// 创建 PPU 线程
error_code sys_ppu_thread_create(
    ppu_thread& ppu,
    vm::ptr<u32> thread_id,          // 输出: 线程 ID
    vm::ptr<void(u64)> entry,        // 入口函数
    u64 arg,                          // 参数
    s32 prio,                         // 优先级
    u32 stacksize,                    // 栈大小
    u64 flags,                        // 标志
    vm::ptr<const char> threadname    // 线程名
)
{
    // 创建新的 PPU 线程
    auto thread = idm::make_ptr<named_thread<ppu_thread>>(
        threadname.get_ptr(), prio, stacksize);

    // 设置入口点
    thread->pc = entry.addr();
    thread->gpr[3] = arg;  // 参数通过 r3 传递

    // 返回线程 ID
    *thread_id = thread->id;

    return CELL_OK;
}

// 退出当前线程
void sys_ppu_thread_exit(ppu_thread& ppu, u64 val)
{
    ppu.state += cpu_flag::exit;
    // 线程将在检查状态后退出
}

// 等待线程结束
error_code sys_ppu_thread_join(
    ppu_thread& ppu,
    u32 thread_id,
    vm::ptr<u64> vptr)  // 输出: 退出值
{
    const auto thread = idm::get<named_thread<ppu_thread>>(thread_id);

    if (!thread)
    {
        return CELL_ESRCH;  // 线程不存在
    }

    // 等待线程完成
    thread->join();

    return CELL_OK;
}
```

### sys_mutex - 互斥锁

```cpp
// 互斥锁结构
struct lv2_mutex
{
    const u32 protocol;      // 协议 (FIFO, Priority, etc.)
    const bool recursive;    // 是否递归
    const std::string name;  // 名称

    std::deque<cpu_thread*> sq;  // 等待队列
    std::atomic<u32> owner{0};   // 拥有者线程 ID
    u32 lock_count = 0;          // 锁计数（递归）

    // 锁定
    error_code lock(cpu_thread& cpu, u64 timeout)
    {
        const u32 tid = cpu.id;

        if (owner == tid && recursive)
        {
            // 递归锁定
            lock_count++;
            return CELL_OK;
        }

        // 尝试获取锁
        u32 old = 0;
        if (!owner.compare_exchange_strong(old, tid))
        {
            // 锁已被占用，加入等待队列
            sq.push_back(&cpu);

            // 等待
            cpu.state += cpu_flag::suspend;

            // ... 等待逻辑
        }

        lock_count = 1;
        return CELL_OK;
    }

    // 解锁
    error_code unlock()
    {
        if (owner == 0)
        {
            return CELL_EPERM;  // 未锁定
        }

        if (--lock_count == 0)
        {
            owner = 0;

            // 唤醒等待线程
            if (!sq.empty())
            {
                cpu_thread* next = sq.front();
                sq.pop_front();

                owner = next->id;
                lock_count = 1;

                // 唤醒线程
                next->state -= cpu_flag::suspend;
                next->notify();
            }
        }

        return CELL_OK;
    }
};

// 创建互斥锁
error_code sys_mutex_create(
    ppu_thread& ppu,
    vm::ptr<u32> mutex_id,
    vm::ptr<sys_mutex_attribute_t> attr)
{
    auto mutex = std::make_shared<lv2_mutex>(
        attr->protocol,
        attr->recursive,
        attr->name);

    *mutex_id = idm::import<lv2_obj, lv2_mutex>(
        [&]() { return mutex; });

    return CELL_OK;
}
```

### sys_event_queue - 事件队列

```cpp
// 事件队列
struct lv2_event_queue
{
    const u32 protocol;         // 协议
    const s32 type;             // 类型 (PPU/SPU)
    const std::string name;     // 名称
    const u64 key;              // 键值

    std::deque<sys_event_t> events;  // 事件队列
    std::deque<cpu_thread*> sq;      // 等待队列

    // 发送事件
    error_code send(u64 source, u64 data1, u64 data2, u64 data3)
    {
        sys_event_t event;
        event.source = source;
        event.data1 = data1;
        event.data2 = data2;
        event.data3 = data3;

        if (sq.empty())
        {
            // 无等待线程，放入队列
            events.push_back(event);
        }
        else
        {
            // 有等待线程，直接发送
            cpu_thread* thread = sq.front();
            sq.pop_front();

            // 将事件数据写入线程
            // ...

            // 唤醒线程
            thread->state -= cpu_flag::wait;
            thread->notify();
        }

        return CELL_OK;
    }

    // 接收事件
    error_code receive(
        ppu_thread& ppu,
        vm::ptr<sys_event_t> event,
        u64 timeout)
    {
        if (events.empty())
        {
            // 无事件，等待
            sq.push_back(&ppu);
            ppu.state += cpu_flag::wait;

            // 等待超时或事件到来
            // ...
        }
        else
        {
            // 有事件，取出
            *event = events.front();
            events.pop_front();
        }

        return CELL_OK;
    }
};
```

## 📚 HLE 模块

### cellFs - 文件系统模块

```cpp
// 文件打开
error_code cellFsOpen(
    ppu_thread& ppu,
    vm::cptr<char> path,
    s32 flags,
    vm::ptr<u32> fd,         // 输出: 文件描述符
    vm::cptr<void> arg,
    u64 size)
{
    // 转换 PS3 路径到主机路径
    std::string vfs_path = vfs::get(path.get_ptr());

    // 转换打开标志
    fs::open_mode mode = {};
    if (flags & CELL_FS_O_RDONLY) mode += fs::read;
    if (flags & CELL_FS_O_WRONLY) mode += fs::write;
    if (flags & CELL_FS_O_CREAT) mode += fs::create;

    // 打开文件
    fs::file file(vfs_path, mode);

    if (!file)
    {
        return CELL_ENOENT;  // 文件不存在
    }

    // 创建文件对象
    *fd = idm::make<lv2_fs_object>(std::move(file));

    return CELL_OK;
}

// 文件读取
error_code cellFsRead(
    ppu_thread& ppu,
    u32 fd,
    vm::ptr<void> buf,
    u64 nbytes,
    vm::ptr<u64> nread)
{
    const auto file = idm::get<lv2_fs_object>(fd);

    if (!file)
    {
        return CELL_EBADF;  // 无效文件描述符
    }

    // 读取数据
    *nread = file->file.read(buf.get_ptr(), nbytes);

    return CELL_OK;
}
```

### cellGcmSys - GCM 系统模块

```cpp
// 设置显示缓冲区
error_code cellGcmSetDisplayBuffer(
    ppu_thread& ppu,
    u32 id,                    // 缓冲区 ID
    u32 offset,                // 偏移
    u32 pitch,                 // 行距
    u32 width,                 // 宽度
    u32 height)                // 高度
{
    auto& gcm = g_fxo->get<gcm_config>();

    gcm_display_info& disp = gcm.display[id];
    disp.offset = offset;
    disp.pitch = pitch;
    disp.width = width;
    disp.height = height;

    return CELL_OK;
}

// 获取当前绘制缓冲区
u32 cellGcmGetCurrentBuffer(ppu_thread& ppu)
{
    auto& gcm = g_fxo->get<gcm_config>();
    return gcm.current_buffer;
}

// 设置翻转模式
error_code cellGcmSetFlipMode(ppu_thread& ppu, u32 mode)
{
    auto& gcm = g_fxo->get<gcm_config>();
    gcm.flip_mode = mode;

    return CELL_OK;
}
```

### cellAudio - 音频模块

```cpp
// 音频端口配置
struct CellAudioPortConfig
{
    u64 readIndexAddr;    // 读索引地址
    u32 status;           // 状态
    u64 nBlock;           // 块数
    u64 portSize;         // 端口大小
    u32 portAddr;         // 端口地址
};

// 初始化音频系统
error_code cellAudioInit()
{
    // 初始化音频后端
    g_fxo->get<cell_audio>().init();

    return CELL_OK;
}

// 打开音频端口
error_code cellAudioPortOpen(
    ppu_thread& ppu,
    vm::ptr<CellAudioPortParam> param,
    vm::ptr<u32> port_num)
{
    auto& audio = g_fxo->get<cell_audio>();

    // 查找空闲端口
    for (u32 i = 0; i < 8; i++)
    {
        if (!audio.ports[i].opened)
        {
            audio.ports[i].opened = true;
            audio.ports[i].num_channels = param->nChannel;
            audio.ports[i].num_blocks = param->nBlock;
            audio.ports[i].level = param->level;

            *port_num = i;
            return CELL_OK;
        }
    }

    return CELL_AUDIO_ERROR_PORT_FULL;
}

// 添加音频数据
error_code cellAudioAddData(
    ppu_thread& ppu,
    u32 port_num,
    vm::ptr<f32> src,       // 源数据
    u32 samples,            // 采样数
    f32 volume)             // 音量
{
    auto& audio = g_fxo->get<cell_audio>();
    auto& port = audio.ports[port_num];

    // 添加数据到音频缓冲区
    for (u32 i = 0; i < samples * port.num_channels; i++)
    {
        port.buffer[port.write_index++] = src[i] * volume;
    }

    return CELL_OK;
}
```

## 🎓 学习要点

### 1. 系统调用机制

```
用户态代码
    ↓
[sc 指令] → PowerPC 系统调用指令
    ↓
[PPU 解释器/JIT 拦截]
    ↓
[查找系统调用表] → 通过调用号查找
    ↓
[执行 C++ 函数] → 实现在 lv2/ 目录
    ↓
返回用户态
```

### 2. 同步原语层次

```
应用层 API
    ↓
sys_mutex, sys_cond, sys_semaphore, etc.
    ↓
lv2_mutex, lv2_cond, lv2_sem (C++ 对象)
    ↓
cpu_thread::state (原子操作)
    ↓
主机操作系统同步原语
```

### 3. HLE vs LLE

**HLE (High-Level Emulation)**:
- 用 C++ 重新实现 PS3 系统库
- 优点: 快速、易调试
- 缺点: 可能不完全准确

**LLE (Low-Level Emulation)**:
- 运行真实的 PS3 系统库（SPU 模块）
- 优点: 完全准确
- 缺点: 慢、需要系统文件

## 💻 实际代码示例

### 示例 1: 线程同步
```cpp
// PS3 游戏代码（伪代码）
sys_mutex_t mutex;
sys_mutex_create(&mutex, NULL);

void thread_a()
{
    sys_mutex_lock(mutex, 0);
    // 临界区
    shared_data++;
    sys_mutex_unlock(mutex);
}

void thread_b()
{
    sys_mutex_lock(mutex, 0);
    // 临界区
    shared_data--;
    sys_mutex_unlock(mutex);
}
```

### 示例 2: 事件通信
```cpp
// 生产者线程
sys_event_queue_t queue;
sys_event_queue_create(&queue, &attr);

// 发送事件
sys_event_t event;
event.data1 = 0x1234;
sys_event_queue_send(queue, &event);

// 消费者线程
sys_event_t received;
sys_event_queue_receive(queue, &received, 0);
// 处理事件: received.data1 == 0x1234
```

### 示例 3: 文件操作
```cpp
// 读取文件
int fd;
cellFsOpen("/dev_hdd0/game/data.bin", CELL_FS_O_RDONLY, &fd, NULL, 0);

char buffer[1024];
uint64_t nread;
cellFsRead(fd, buffer, sizeof(buffer), &nread);

cellFsClose(fd);
```

## 🔍 调试技巧

### 1. 系统调用追踪
```cpp
// 在系统调用入口记录
sys_log.trace("sys_ppu_thread_create(prio=%d, stack=%d, name=%s)",
              prio, stacksize, threadname.get_ptr());
```

### 2. 线程状态转储
```cpp
// 查看所有线程状态
idm::select<named_thread<ppu_thread>>([](u32 id, ppu_thread& ppu)
{
    sys_log.notice("Thread 0x%x: state=%s, pc=0x%x",
                   id, ppu.state, ppu.pc);
});
```

## 📚 错误代码

```cpp
// ErrorCodes.h
enum CellError : u32
{
    CELL_OK                  = 0x00000000,
    CELL_EAGAIN              = 0x80010001,  // 资源暂时不可用
    CELL_EINVAL              = 0x80010002,  // 无效参数
    CELL_ENOSYS              = 0x80010003,  // 未实现
    CELL_ENOMEM              = 0x80010004,  // 内存不足
    CELL_ESRCH               = 0x80010005,  // 线程不存在
    CELL_ENOENT              = 0x80010006,  // 文件不存在
    CELL_EEXIST              = 0x80010008,  // 已存在
    CELL_EDEADLK             = 0x8001000B,  // 死锁
    CELL_EPERM               = 0x8001000C,  // 权限拒绝
    CELL_EBUSY               = 0x8001000D,  // 资源忙
    CELL_ETIMEDOUT           = 0x8001000E,  // 超时
    // ... 更多
};
```

---

## 📚 下一步

- [返回总览](./01-RPCS3-项目总览.md)
- [上一章: RSX 图形系统](./04-RSX-图形系统.md)
- [下一章: Crypto 加密](./06-Crypto-加密.md)

---

**提示**: Cell 模块的 lv2 系统调用和 HLE 模块是理解 PS3 软件如何工作的关键。建议从简单的系统调用（如 sys_time）开始学习。
