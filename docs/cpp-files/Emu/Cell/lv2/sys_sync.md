# sys_sync.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_sync.h`
- **类型**: 头文件
- **行数**: 521 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_obj`
- `name_64`
- `notify_all_t`
- `ppu_non_sleeping_count_t`

### 关键函数

- `append()`
- `awake()`
- `awake_unlocked()`
- `count_non_sleeping_threads()`
- `enqueue_on_top()`
- `is_scheduler_ready()`
- `load()`
- `name64()`
- `notify_all()`
- `prepare_for_sleep()`
- `save()`
- `schedule_all()`
- `set_future_sleep()`
- `unqueue()`
- `wait_timeout()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/mutex.h"

#include "Emu/CPU/CPUThread.h"
#include "Emu/Cell/ErrorCodes.h"
#include "Emu/IdManager.h"
#include "Emu/IPC.h"

#include "util/shared_ptr.hpp"

// attr_protocol (waiting scheduling policy)
enum lv2_protocol : u8
{
	SYS_SYNC_FIFO                = 0x1, // First In, First Out Order
	SYS_SYNC_PRIORITY            = 0x2, // Priority Order
	SYS_SYNC_PRIORITY_INHERIT    = 0x3, // Basic Priority Inheritance Protocol
	SYS_SYNC_RETRY               = 0x4, // Not selected while unlocking
};

enum : u32
{
	SYS_SYNC_ATTR_PROTOCOL_MASK  = 0xf,
};

// attr_recursive (recursive locks policy)
enum
{
	SYS_SYNC_RECURSIVE           = 0x10,
	SYS_SYNC_NOT_RECURSIVE       = 0x20,
	SYS_SYNC_ATTR_RECURSIVE_MASK = 0xf0,
};

// attr_pshared (sharing among processes policy)
enum
{
	SYS_SYNC_PROCESS_SHARED      = 0x100,
	SYS_SYNC_NOT_PROCESS_SHARED  = 0x200,
	SYS_SYNC_ATTR_PSHARED_MASK   = 0xf00,
};

// attr_flags (creation policy)
enum
{
	SYS_SYNC_NEWLY_CREATED       = 0x1, // Create new object, fails if specified IPC key exists
	SYS_SYNC_NOT_CREATE          = 0x2, // Reference existing object, fails if IPC key not found
	SYS_SYNC_NOT_CARE            = 0x3, // Reference existing object, create new one if IPC key not found
	SYS_SYNC_ATTR_FLAGS_MASK     = 0xf,
};

// attr_adaptive
enum
{
	SYS_SYNC_ADAPTIVE            = 0x1000,
	SYS_SYNC_NOT_ADAPTIVE        = 0x2000,
	SYS_SYNC_ATTR_ADAPTIVE_MASK  = 0xf000,
};

enum ppu_thread_status : u32;

struct ppu_non_sleeping_count_t
{
	bool has_running; // no actual count for optimization sake
	u32 onproc_count;
};

// Base class for some kernel objects (shared set of 8192 objects).
struct lv2_obj
{
	static const u32 id_step = 0x100;
	static const u32 id_count = 8192;
	static constexpr std::pair<u32, u32> id_invl_range = {0, 8};

private:
	enum thread_cmd : s32
	{
		yield_cmd = smin,
		enqueue_cmd,
	};

```

## 🔗 依赖头文件

- `#include "Utilities/mutex.h"`
- `#include "Emu/CPU/CPUThread.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/IPC.h"`
- `#include "util/shared_ptr.hpp"`
