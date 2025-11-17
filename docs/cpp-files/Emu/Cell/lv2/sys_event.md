# sys_event.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_event.h`
- **类型**: 头文件
- **行数**: 154 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `cpu_thread`
- `lv2_event_port`
- `lv2_event_queue`
- `ppu_thread`
- `spu_thrread`
- `sys_event_queue_attribute_t`
- `sys_event_t`

### 系统调用

- `sys_event_port_connect_ipc()`
- `sys_event_port_connect_local()`
- `sys_event_port_create()`
- `sys_event_port_destroy()`
- `sys_event_port_disconnect()`
- `sys_event_port_send()`
- `sys_event_queue_create()`
- `sys_event_queue_destroy()`
- `sys_event_queue_drain()`
- `sys_event_queue_receive()`
- `sys_event_queue_tryreceive()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Memory/vm_ptr.h"

#include <deque>

class cpu_thread;
class spu_thrread;

// Event Queue Type
enum : u32
{
	SYS_PPU_QUEUE = 1,
	SYS_SPU_QUEUE = 2,
};

// Event Queue Destroy Mode
enum : s32
{
	SYS_EVENT_QUEUE_DESTROY_FORCE = 1,
};

// Event Queue Ipc Key
enum : u64
{
	SYS_EVENT_QUEUE_LOCAL = 0,
};

// Event Port Type
enum : s32
{
	SYS_EVENT_PORT_LOCAL = 1,
	SYS_EVENT_PORT_IPC   = 3, // Unofficial name
};

// Event Port Name
enum : u64
{
	SYS_EVENT_PORT_NO_NAME = 0,
};

// Event Source Type
enum : u32
{
	SYS_SPU_THREAD_EVENT_USER = 1,
	SYS_SPU_THREAD_EVENT_DMA  = 2, // not supported
};

// Event Source Key
enum : u64
{
	SYS_SPU_THREAD_EVENT_USER_KEY      = 0xFFFFFFFF53505501ull,
	SYS_SPU_THREAD_EVENT_DMA_KEY       = 0xFFFFFFFF53505502ull,
	SYS_SPU_THREAD_EVENT_EXCEPTION_KEY = 0xFFFFFFFF53505503ull,
};

struct sys_event_queue_attribute_t
{
	be_t<u32> protocol; // SYS_SYNC_PRIORITY or SYS_SYNC_FIFO
	be_t<s32> type; // SYS_PPU_QUEUE or SYS_SPU_QUEUE

	union
	{
		nse_t<u64, 1> name_u64;
		char name[sizeof(u64)];
	};
};

struct sys_event_t
{
	be_t<u64> source;
	be_t<u64> data1;
	be_t<u64> data2;
	be_t<u64> data3;
};

// Source, data1, data2, data3
using lv2_event = std::tuple<u64, u64, u64, u64>;
```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include <deque>`
