# sys_spu.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_spu.h`
- **类型**: 头文件
- **行数**: 422 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_memory_container`
- `lv2_spu_group`
- `lv2_spu_image`
- `ppu_thread`
- `reduced_sys_spu_thread_group_attribute`
- `sys_spu_image`
- `sys_spu_segment`
- `sys_spu_thread_argument`
- `sys_spu_thread_attribute`
- `sys_spu_thread_group_syscall_253_info`

### 系统调用

- `sys_isolated_spu_create()`
- `sys_isolated_spu_create_interrupt_tag()`
- `sys_isolated_spu_get_int_mask()`
- `sys_isolated_spu_get_spu_cfg()`
- `sys_isolated_spu_start()`
- `sys_raw_spu_destroy()`
- `sys_raw_spu_read_puint_mb()`
- `sys_raw_spu_set_int_stat()`
- `sys_spu_initialize()`
- `sys_spu_thread_group_connect_event()`
- `sys_spu_thread_group_create()`
- `sys_spu_thread_group_disconnect_event_all_threads()`
- `sys_spu_thread_group_set_cooperative_victims()`
- `sys_spu_thread_group_set_priority()`
- `sys_spu_thread_group_start()`
- `sys_spu_thread_group_suspend()`
- `sys_spu_thread_group_syscall_253()`
- `sys_spu_thread_initialize()`
- `sys_spu_thread_set_argument()`
- `sys_spu_thread_write_snr()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"
#include "sys_event.h"
#include "Emu/Cell/SPUThread.h"
#include "Emu/Cell/ErrorCodes.h"

#include "Emu/Memory/vm_ptr.h"
#include "Utilities/File.h"

#include <span>

struct lv2_memory_container;

enum : s32
{
	SYS_SPU_THREAD_GROUP_TYPE_NORMAL                = 0x00,
	//SYS_SPU_THREAD_GROUP_TYPE_SEQUENTIAL            = 0x01, doesn't exist
	SYS_SPU_THREAD_GROUP_TYPE_SYSTEM                = 0x02,
	SYS_SPU_THREAD_GROUP_TYPE_MEMORY_FROM_CONTAINER = 0x04,
	SYS_SPU_THREAD_GROUP_TYPE_NON_CONTEXT           = 0x08,
	SYS_SPU_THREAD_GROUP_TYPE_EXCLUSIVE_NON_CONTEXT = 0x18,
	SYS_SPU_THREAD_GROUP_TYPE_COOPERATE_WITH_SYSTEM = 0x20,
};

enum
{
	SYS_SPU_THREAD_GROUP_JOIN_GROUP_EXIT       = 0x0001,
	SYS_SPU_THREAD_GROUP_JOIN_ALL_THREADS_EXIT = 0x0002,
	SYS_SPU_THREAD_GROUP_JOIN_TERMINATED       = 0x0004
};

enum
{
	SYS_SPU_THREAD_GROUP_EVENT_RUN           = 1,
	SYS_SPU_THREAD_GROUP_EVENT_EXCEPTION     = 2,
	SYS_SPU_THREAD_GROUP_EVENT_SYSTEM_MODULE = 4,
};

enum : u64
{
	SYS_SPU_THREAD_GROUP_EVENT_RUN_KEY           = 0xFFFFFFFF53505500ull,
	SYS_SPU_THREAD_GROUP_EVENT_EXCEPTION_KEY     = 0xFFFFFFFF53505503ull,
	SYS_SPU_THREAD_GROUP_EVENT_SYSTEM_MODULE_KEY = 0xFFFFFFFF53505504ull,
};

enum
{
	SYS_SPU_THREAD_GROUP_LOG_ON         = 0x0,
	SYS_SPU_THREAD_GROUP_LOG_OFF        = 0x1,
	SYS_SPU_THREAD_GROUP_LOG_GET_STATUS = 0x2,
};

enum spu_group_status : u32
{
	SPU_THREAD_GROUP_STATUS_NOT_INITIALIZED,
	SPU_THREAD_GROUP_STATUS_INITIALIZED,
	SPU_THREAD_GROUP_STATUS_READY,
	SPU_THREAD_GROUP_STATUS_WAITING,
	SPU_THREAD_GROUP_STATUS_SUSPENDED,
	SPU_THREAD_GROUP_STATUS_WAITING_AND_SUSPENDED,
	SPU_THREAD_GROUP_STATUS_RUNNING,
	SPU_THREAD_GROUP_STATUS_STOPPED,
	SPU_THREAD_GROUP_STATUS_DESTROYED, // Internal state
	SPU_THREAD_GROUP_STATUS_UNKNOWN,
};

enum : s32
{
	SYS_SPU_SEGMENT_TYPE_COPY = 1,
	SYS_SPU_SEGMENT_TYPE_FILL = 2,
	SYS_SPU_SEGMENT_TYPE_INFO = 4,
};

enum spu_stop_syscall : u32
{
	SYS_SPU_THREAD_STOP_YIELD                = 0x0100,
	SYS_SPU_THREAD_STOP_GROUP_EXIT           = 0x0101,
	SYS_SPU_THREAD_STOP_THREAD_EXIT          = 0x0102,
	SYS_SPU_THREAD_STOP_RECEIVE_EVENT        = 0x0110,
```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "sys_event.h"`
- `#include "Emu/Cell/SPUThread.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Utilities/File.h"`
- `#include <span>`
