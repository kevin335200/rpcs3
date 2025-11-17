# LV2 系统调用实现

## 📚 概述

LV2 (Level 2) 是 PlayStation 3 的游戏操作系统层，提供系统调用接口供游戏和应用程序使用。本目录包含 **100 个文件**，实现了 PS3 的所有主要系统调用。

## 📊 统计信息

- **文件总数**: 100 个 (.cpp + .h)
- **系统调用模块**: 44 个主要模块
- **网络相关**: 10 个文件 (sys_net/)

## 🗂️ 系统调用分类

### 🔹 1. 线程同步原语 (14 个文件)

用于线程间同步和互斥的基本原语。

| 模块 | 头文件 | 源文件 | 说明 |
|------|--------|--------|------|
| **sys_mutex** | [sys_mutex.h](sys_mutex.md) | [sys_mutex.cpp](sys_mutex.md) | 互斥锁 |
| **sys_cond** | [sys_cond.h](sys_cond.md) | [sys_cond.cpp](sys_cond.md) | 条件变量 |
| **sys_rwlock** | [sys_rwlock.h](sys_rwlock.md) | [sys_rwlock.cpp](sys_rwlock.md) | 读写锁 |
| **sys_semaphore** | [sys_semaphore.h](sys_semaphore.md) | [sys_semaphore.cpp](sys_semaphore.md) | 信号量 |
| **sys_lwmutex** | [sys_lwmutex.h](sys_lwmutex.md) | [sys_lwmutex.cpp](sys_lwmutex.md) | 轻量级互斥锁 |
| **sys_lwcond** | [sys_lwcond.h](sys_lwcond.md) | [sys_lwcond.cpp](sys_lwcond.md) | 轻量级条件变量 |
| **sys_event_flag** | [sys_event_flag.h](sys_event_flag.md) | [sys_event_flag.cpp](sys_event_flag.md) | 事件标志 |

**关键系统调用**:
- `sys_mutex_create`, `sys_mutex_lock`, `sys_mutex_unlock`
- `sys_cond_wait`, `sys_cond_signal`
- `sys_rwlock_rlock`, `sys_rwlock_wlock`
- `sys_semaphore_wait`, `sys_semaphore_post`

### 🔹 2. 事件系统 (4 个文件)

事件队列和事件端口，用于异步事件通知。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_event** | [sys_event.h](sys_event.md) / [sys_event.cpp](sys_event.md) | 事件队列和事件端口 |
| **sys_event_flag** | 见上方同步原语 | 事件标志 (也是同步原语) |

**关键系统调用**:
- `sys_event_queue_create`, `sys_event_queue_receive`
- `sys_event_port_create`, `sys_event_port_send`

### 🔹 3. SPU 管理 (6 个文件)

管理 SPU 线程组和 SPU 线程的执行。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_spu** | [sys_spu.h](sys_spu.md) / [sys_spu.cpp](sys_spu.md) | SPU 线程组管理 |
| **sys_interrupt** | [sys_interrupt.h](sys_interrupt.md) / [sys_interrupt.cpp](sys_interrupt.md) | SPU 中断处理 |
| **sys_sync** | [sys_sync.h](sys_sync.md) | SPU 同步原语头文件 |

**关键系统调用**:
- `sys_spu_thread_group_create`, `sys_spu_thread_group_start`
- `sys_spu_thread_initialize`, `sys_spu_thread_write_ls`
- `sys_spu_image_open`, `sys_interrupt_thread_establish`

### 🔹 4. 内存管理 (8 个文件)

虚拟内存、物理内存分配和映射。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_memory** | [sys_memory.h](sys_memory.md) / [sys_memory.cpp](sys_memory.md) | 内存容器和分配 |
| **sys_mmapper** | [sys_mmapper.h](sys_mmapper.md) / [sys_mmapper.cpp](sys_mmapper.md) | 内存映射器 |
| **sys_vm** | [sys_vm.h](sys_vm.md) / [sys_vm.cpp](sys_vm.md) | 虚拟内存管理 |
| **sys_overlay** | [sys_overlay.h](sys_overlay.md) / [sys_overlay.cpp](sys_overlay.md) | 内存覆盖 (Overlay) |

**关键系统调用**:
- `sys_memory_allocate`, `sys_memory_free`
- `sys_memory_container_create`
- `sys_mmapper_allocate_address`, `sys_mmapper_map_memory`
- `sys_vm_memory_map`, `sys_overlay_load_module`

### 🔹 5. 进程和线程管理 (6 个文件)

进程生命周期和 PPU 线程管理。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_process** | [sys_process.h](sys_process.md) / [sys_process.cpp](sys_process.md) | 进程管理 |
| **sys_ppu_thread** | [sys_ppu_thread.h](sys_ppu_thread.md) / [sys_ppu_thread.cpp](sys_ppu_thread.md) | PPU 线程管理 |
| **sys_game** | [sys_game.h](sys_game.md) / [sys_game.cpp](sys_game.md) | 游戏进程信息 |

**关键系统调用**:
- `sys_process_exit`, `sys_process_get_paramsfo`
- `sys_ppu_thread_create`, `sys_ppu_thread_exit`
- `sys_game_process_exitspawn2`

### 🔹 6. 文件系统 (2 个文件)

虚拟文件系统接口。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_fs** | [sys_fs.h](sys_fs.md) / [sys_fs.cpp](sys_fs.md) | 文件系统操作 |

**关键系统调用**:
- `sys_fs_open`, `sys_fs_read`, `sys_fs_write`, `sys_fs_close`
- `sys_fs_opendir`, `sys_fs_readdir`
- `sys_fs_stat`, `sys_fs_mkdir`

### 🔹 7. 时间和定时器 (6 个文件)

系统时间、高精度时钟和定时器。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_time** | [sys_time.h](sys_time.md) / [sys_time.cpp](sys_time.md) | 系统时间 |
| **sys_timer** | [sys_timer.h](sys_timer.md) / [sys_timer.cpp](sys_timer.md) | 定时器 |
| **sys_trace** | [sys_trace.h](sys_trace.md) / [sys_trace.cpp](sys_trace.md) | 性能追踪 |

**关键系统调用**:
- `sys_time_get_current_time`, `sys_time_get_system_time`
- `sys_timer_create`, `sys_timer_start`

### 🔹 8. 网络 (12 个文件)

BSD Socket 接口和 P2P 网络。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_net** | [sys_net.h](sys_net.md) / [sys_net.cpp](sys_net.md) | 网络初始化 |
| **lv2_socket** | [sys_net/lv2_socket.h](sys_net/lv2_socket.md) / [.cpp](sys_net/lv2_socket.md) | 主 Socket 实现 |
| **lv2_socket_native** | [sys_net/lv2_socket_native.*](sys_net/lv2_socket_native.md) | 原生 TCP/UDP Socket |
| **lv2_socket_p2p** | [sys_net/lv2_socket_p2p.*](sys_net/lv2_socket_p2p.md) | P2P Socket |
| **lv2_socket_p2ps** | [sys_net/lv2_socket_p2ps.*](sys_net/lv2_socket_p2ps.md) | P2P Server Socket |
| **lv2_socket_raw** | [sys_net/lv2_socket_raw.*](sys_net/lv2_socket_raw.md) | Raw Socket |
| **network_context** | [sys_net/network_context.*](sys_net/network_context.md) | 网络上下文 |
| **nt_p2p_port** | [sys_net/nt_p2p_port.*](sys_net/nt_p2p_port.md) | P2P 端口管理 |
| **sys_net_helpers** | [sys_net/sys_net_helpers.*](sys_net/sys_net_helpers.md) | 网络辅助函数 |

**关键系统调用**:
- `sys_net_initialize_network_ex`
- `socket`, `bind`, `listen`, `accept`, `connect`
- `send`, `recv`, `sendto`, `recvfrom`
- `setsockopt`, `getsockopt`

### 🔹 9. 动态库和模块 (4 个文件)

PRX 动态库加载和管理。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_prx** | [sys_prx.h](sys_prx.md) / [sys_prx.cpp](sys_prx.md) | PRX 模块加载器 |
| **sys_overlay** | [sys_overlay.*](sys_overlay.md) | Overlay 模块 (见内存管理) |

**关键系统调用**:
- `sys_prx_load_module`, `sys_prx_start_module`
- `sys_prx_get_module_info`

### 🔹 10. RSX 图形 (4 个文件)

RSX (Reality Synthesizer) 图形处理器接口。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_rsx** | [sys_rsx.h](sys_rsx.md) / [sys_rsx.cpp](sys_rsx.md) | RSX 设备管理 |
| **sys_rsxaudio** | [sys_rsxaudio.h](sys_rsxaudio.md) / [sys_rsxaudio.cpp](sys_rsxaudio.md) | RSX 音频 (HDMI) |

**关键系统调用**:
- `sys_rsx_device_open`, `sys_rsx_context_allocate`
- `sys_rsx_memory_allocate`, `sys_rsx_context_iomap`

### 🔹 11. 设备和外设 (14 个文件)

存储、USB、游戏手柄等设备。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_storage** | [sys_storage.h](sys_storage.md) / [sys_storage.cpp](sys_storage.md) | 存储设备 (HDD/BD) |
| **sys_usbd** | [sys_usbd.h](sys_usbd.md) / [sys_usbd.cpp](sys_usbd.md) | USB 设备管理 |
| **sys_gamepad** | [sys_gamepad.h](sys_gamepad.md) / [sys_gamepad.cpp](sys_gamepad.md) | 游戏手柄 |
| **sys_hid** | [sys_hid.h](sys_hid.md) / [sys_hid.cpp](sys_hid.md) | HID 设备 (键盘/鼠标) |
| **sys_gpio** | [sys_gpio.h](sys_gpio.md) / [sys_gpio.cpp](sys_gpio.md) | GPIO 接口 |
| **sys_uart** | [sys_uart.h](sys_uart.md) / [sys_uart.cpp](sys_uart.md) | UART 串口 |
| **sys_bdemu** | [sys_bdemu.h](sys_bdemu.md) / [sys_bdemu.cpp](sys_bdemu.md) | 蓝光模拟 |

**关键系统调用**:
- `sys_storage_open`, `sys_storage_read`
- `sys_usbd_register_ldd`
- `sys_gamepad_ycon_if`

### 🔹 12. 系统服务 (12 个文件)

配置、调试、加密等系统服务。

| 模块 | 文件 | 说明 |
|------|------|------|
| **sys_config** | [sys_config.h](sys_config.md) / [sys_config.cpp](sys_config.md) | 系统配置 |
| **sys_dbg** | [sys_dbg.h](sys_dbg.md) / [sys_dbg.cpp](sys_dbg.md) | 调试接口 |
| **sys_tty** | [sys_tty.h](sys_tty.md) / [sys_tty.cpp](sys_tty.md) | TTY 终端 |
| **sys_console** | [sys_console.h](sys_console.md) / [sys_console.cpp](sys_console.md) | 控制台 |
| **sys_crypto_engine** | [sys_crypto_engine.*](sys_crypto_engine.md) | 加密引擎 |
| **sys_btsetting** | [sys_btsetting.*](sys_btsetting.md) | 蓝牙设置 |
| **sys_io** | [sys_io.h](sys_io.md) / [sys_io.cpp](sys_io.md) | I/O 管理 |
| **sys_sm** | [sys_sm.h](sys_sm.md) / [sys_sm.cpp](sys_sm.md) | 服务管理器 |
| **sys_ss** | [sys_ss.h](sys_ss.md) / [sys_ss.cpp](sys_ss.md) | 安全服务 |

### 🔹 13. 核心 LV2 (2 个文件)

| 模块 | 文件 | 说明 |
|------|------|------|
| **lv2** | [lv2.cpp](lv2.md) | LV2 核心初始化和系统调用表 |

## 📖 完整文件列表

### 主目录文件 (44 个)

<details>
<summary>点击展开查看所有文件</summary>

1. [lv2.cpp](lv2.md) - LV2 核心
2. [sys_bdemu.*](sys_bdemu.md) - 蓝光模拟
3. [sys_btsetting.*](sys_btsetting.md) - 蓝牙设置
4. [sys_cond.*](sys_cond.md) - 条件变量
5. [sys_config.*](sys_config.md) - 系统配置
6. [sys_console.*](sys_console.md) - 控制台
7. [sys_crypto_engine.*](sys_crypto_engine.md) - 加密引擎
8. [sys_dbg.*](sys_dbg.md) - 调试接口
9. [sys_event.*](sys_event.md) - 事件队列
10. [sys_event_flag.*](sys_event_flag.md) - 事件标志
11. [sys_fs.*](sys_fs.md) - 文件系统
12. [sys_game.*](sys_game.md) - 游戏进程
13. [sys_gamepad.*](sys_gamepad.md) - 游戏手柄
14. [sys_gpio.*](sys_gpio.md) - GPIO
15. [sys_hid.*](sys_hid.md) - HID 设备
16. [sys_interrupt.*](sys_interrupt.md) - 中断处理
17. [sys_io.*](sys_io.md) - I/O 管理
18. [sys_lwcond.*](sys_lwcond.md) - 轻量级条件变量
19. [sys_lwmutex.*](sys_lwmutex.md) - 轻量级互斥锁
20. [sys_memory.*](sys_memory.md) - 内存管理
21. [sys_mmapper.*](sys_mmapper.md) - 内存映射
22. [sys_mutex.*](sys_mutex.md) - 互斥锁
23. [sys_net.*](sys_net.md) - 网络
24. [sys_overlay.*](sys_overlay.md) - 覆盖模块
25. [sys_ppu_thread.*](sys_ppu_thread.md) - PPU 线程
26. [sys_process.*](sys_process.md) - 进程管理
27. [sys_prx.*](sys_prx.md) - PRX 模块
28. [sys_rsx.*](sys_rsx.md) - RSX 图形
29. [sys_rsxaudio.*](sys_rsxaudio.md) - RSX 音频
30. [sys_rwlock.*](sys_rwlock.md) - 读写锁
31. [sys_semaphore.*](sys_semaphore.md) - 信号量
32. [sys_sm.*](sys_sm.md) - 服务管理器
33. [sys_spu.*](sys_spu.md) - SPU 管理
34. [sys_ss.*](sys_ss.md) - 安全服务
35. [sys_storage.*](sys_storage.md) - 存储设备
36. [sys_sync.h](sys_sync.md) - 同步原语
37. [sys_time.*](sys_time.md) - 时间
38. [sys_timer.*](sys_timer.md) - 定时器
39. [sys_trace.*](sys_trace.md) - 性能追踪
40. [sys_tty.*](sys_tty.md) - TTY 终端
41. [sys_uart.*](sys_uart.md) - UART 串口
42. [sys_usbd.*](sys_usbd.md) - USB 设备
43. [sys_vm.*](sys_vm.md) - 虚拟内存

</details>

### sys_net/ 子目录 (10 个文件)

1. [sys_net/lv2_socket.*](sys_net/lv2_socket.md) - 主 Socket 实现
2. [sys_net/lv2_socket_native.*](sys_net/lv2_socket_native.md) - 原生 Socket
3. [sys_net/lv2_socket_p2p.*](sys_net/lv2_socket_p2p.md) - P2P Socket
4. [sys_net/lv2_socket_p2ps.*](sys_net/lv2_socket_p2ps.md) - P2P Server
5. [sys_net/lv2_socket_raw.*](sys_net/lv2_socket_raw.md) - Raw Socket
6. [sys_net/network_context.*](sys_net/network_context.md) - 网络上下文
7. [sys_net/nt_p2p_port.*](sys_net/nt_p2p_port.md) - P2P 端口
8. [sys_net/sys_net_helpers.*](sys_net/sys_net_helpers.md) - 辅助函数

## 🔍 快速查找

### 按功能查找
- **我需要线程同步**: [sys_mutex](sys_mutex.md), [sys_cond](sys_cond.md)
- **我需要分配内存**: [sys_memory](sys_memory.md), [sys_mmapper](sys_mmapper.md)
- **我需要创建线程**: [sys_ppu_thread](sys_ppu_thread.md)
- **我需要加载 PRX**: [sys_prx](sys_prx.md)
- **我需要文件操作**: [sys_fs](sys_fs.md)
- **我需要网络功能**: [sys_net](sys_net.md), [sys_net/](sys_net/)
- **我需要 SPU 操作**: [sys_spu](sys_spu.md)
- **我需要图形接口**: [sys_rsx](sys_rsx.md)

## 📖 相关文档

- [Cell 模块主文档](../README.md)
- [HLE Modules 文档](../Modules/README.md)
- [PPU 线程实现](../PPUThread.md)
- [SPU 线程实现](../SPUThread.md)

---

**文件总数**: 100 个
**系统调用模块**: 44 个
