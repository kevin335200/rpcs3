# sys_process.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_process.h`
- **类型**: 头文件
- **行数**: 126 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `ps3_process_info_t`
- `sys_exit2_param`

### 系统调用

- `sys_process_detach_child()`
- `sys_process_exit3()`
- `sys_process_get_id()`
- `sys_process_get_id2()`
- `sys_process_get_number_of_object()`
- `sys_process_get_sdk_version()`
- `sys_process_get_status()`
- `sys_process_getpid()`
- `sys_process_getppid()`
- `sys_process_is_spu_lock_line_reservation_address()`
- `sys_process_kill()`
- `sys_process_spawns_a_self2()`
- `sys_process_wait_for_child()`
- `sys_process_wait_for_child2()`

## 💻 代码片段

```cpp
#pragma once

#include "Crypto/unself.h"
#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// Process Local Object Type
enum : u32
{
	SYS_MEM_OBJECT                   = 0x08,
	SYS_MUTEX_OBJECT                 = 0x85,
	SYS_COND_OBJECT                  = 0x86,
	SYS_RWLOCK_OBJECT                = 0x88,
	SYS_INTR_TAG_OBJECT              = 0x0A,
	SYS_INTR_SERVICE_HANDLE_OBJECT   = 0x0B,
	SYS_EVENT_QUEUE_OBJECT           = 0x8D,
	SYS_EVENT_PORT_OBJECT            = 0x0E,
	SYS_TRACE_OBJECT                 = 0x21,
	SYS_SPUIMAGE_OBJECT              = 0x22,
	SYS_PRX_OBJECT                   = 0x23,
	SYS_SPUPORT_OBJECT               = 0x24,
	SYS_OVERLAY_OBJECT               = 0x25,
	SYS_LWMUTEX_OBJECT               = 0x95,
	SYS_TIMER_OBJECT                 = 0x11,
	SYS_SEMAPHORE_OBJECT             = 0x96,
	SYS_FS_FD_OBJECT                 = 0x73,
	SYS_LWCOND_OBJECT                = 0x97,
	SYS_EVENT_FLAG_OBJECT            = 0x98,
	SYS_RSXAUDIO_OBJECT              = 0x60,
};

enum : u64
{
	SYS_PROCESS_PRIMARY_STACK_SIZE_32K  = 0x0000000000000010,
	SYS_PROCESS_PRIMARY_STACK_SIZE_64K  = 0x0000000000000020,
	SYS_PROCESS_PRIMARY_STACK_SIZE_96K  = 0x0000000000000030,
	SYS_PROCESS_PRIMARY_STACK_SIZE_128K = 0x0000000000000040,
	SYS_PROCESS_PRIMARY_STACK_SIZE_256K = 0x0000000000000050,
	SYS_PROCESS_PRIMARY_STACK_SIZE_512K = 0x0000000000000060,
	SYS_PROCESS_PRIMARY_STACK_SIZE_1M   = 0x0000000000000070,
};

constexpr auto SYS_PROCESS_PARAM_SECTION_NAME = ".sys_proc_param";

enum
{
	SYS_PROCESS_PARAM_INVALID_PRIO = -32768,
};

enum : u32
{
	SYS_PROCESS_PARAM_INVALID_STACK_SIZE = 0xffffffff,

	SYS_PROCESS_PARAM_STACK_SIZE_MIN = 0x1000,   // 4KB
	SYS_PROCESS_PARAM_STACK_SIZE_MAX = 0x100000, // 1MB

	SYS_PROCESS_PARAM_VERSION_INVALID = 0xffffffff,
	SYS_PROCESS_PARAM_VERSION_1       = 0x00000001, // for SDK 08X
	SYS_PROCESS_PARAM_VERSION_084_0   = 0x00008400,
	SYS_PROCESS_PARAM_VERSION_090_0   = 0x00009000,
	SYS_PROCESS_PARAM_VERSION_330_0   = 0x00330000,

	SYS_PROCESS_PARAM_MAGIC = 0x13bcc5f6,

	SYS_PROCESS_PARAM_MALLOC_PAGE_SIZE_NONE = 0x00000000,
	SYS_PROCESS_PARAM_MALLOC_PAGE_SIZE_64K  = 0x00010000,
	SYS_PROCESS_PARAM_MALLOC_PAGE_SIZE_1M   = 0x00100000,

	SYS_PROCESS_PARAM_PPC_SEG_DEFAULT       = 0x00000000,
	SYS_PROCESS_PARAM_PPC_SEG_OVLM          = 0x00000001,
	SYS_PROCESS_PARAM_PPC_SEG_FIXEDADDR_PRX = 0x00000002,

	SYS_PROCESS_PARAM_SDK_VERSION_UNKNOWN = 0xffffffff,
};

struct sys_exit2_param
{
	be_t<u64> x0; // 0x85
	be_t<u64> this_size; // 0x30
	be_t<u64> next_size;
```

## 🔗 依赖头文件

- `#include "Crypto/unself.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
