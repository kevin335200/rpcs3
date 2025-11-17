# sys_rsx.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_rsx.h`
- **类型**: 头文件
- **行数**: 139 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `Head`
- `RsxDisplayInfo`
- `RsxDmaControl`
- `RsxDriverInfo`
- `RsxReports`
- `alignas`
- `cpu_thread`

### 系统调用

- `sys_rsx_attribute()`
- `sys_rsx_context_allocate()`
- `sys_rsx_context_attribute()`
- `sys_rsx_context_free()`
- `sys_rsx_context_iomap()`
- `sys_rsx_context_iounmap()`
- `sys_rsx_device_close()`
- `sys_rsx_device_map()`
- `sys_rsx_device_open()`
- `sys_rsx_device_unmap()`
- `sys_rsx_memory_allocate()`
- `sys_rsx_memory_free()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

class cpu_thread;

struct RsxDriverInfo
{
	be_t<u32> version_driver;     // 0x0
	be_t<u32> version_gpu;        // 0x4
	be_t<u32> memory_size;        // 0x8
	be_t<u32> hardware_channel;   // 0xC
	be_t<u32> nvcore_frequency;   // 0x10
	be_t<u32> memory_frequency;   // 0x14
	be_t<u32> unk1[4];            // 0x18 - 0x24
	be_t<u32> unk2;               // 0x28 -- pgraph stuff
	be_t<u32> reportsNotifyOffset;// 0x2C offset to notify memory
	be_t<u32> reportsOffset;      // 0x30 offset to reports memory
	be_t<u32> reportsReportOffset;// 0x34 offset to reports in reports memory
	be_t<u32> unk3[6];            // 0x38-0x54
	be_t<u32> systemModeFlags;    // 0x54
	u8 unk4[0x1064];              // 0x10B8

	struct Head
	{
		be_t<u64> lastFlipTime;    // 0x0 last flip time
		atomic_be_t<u32> flipFlags; // 0x8 flags to handle flip/queue
		be_t<u32> offset;          // 0xC
		be_t<u32> flipBufferId;    // 0x10
		be_t<u32> lastQueuedBufferId; // 0x14 todo: this is definately not this variable but its 'unused' so im using it for queueId to pass to flip handler
		be_t<u32> unk3;            // 0x18
		be_t<u32> lastVTimeLow;    // 0x1C last time for first vhandler freq (low 32-bits)
		atomic_be_t<u64> lastSecondVTime; // 0x20 last time for second vhandler freq
		be_t<u64> unk4;            // 0x28
		atomic_be_t<u64> vBlankCount; // 0x30
		be_t<u32> unk;             // 0x38 possible u32, 'flip field', top/bottom for interlaced
		be_t<u32> lastVTimeHigh;   // 0x3C last time for first vhandler freq (high 32-bits)
	} head[8]; // size = 0x40, 0x200

	be_t<u32> unk7;          // 0x12B8
	be_t<u32> unk8;          // 0x12BC
	atomic_be_t<u32> handlers; // 0x12C0 -- flags showing which handlers are set
	be_t<u32> unk9;          // 0x12C4
	be_t<u32> unk10;         // 0x12C8
	be_t<u32> userCmdParam;  // 0x12CC
	be_t<u32> handler_queue; // 0x12D0
	be_t<u32> unk11;         // 0x12D4
	be_t<u32> unk12;         // 0x12D8
	be_t<u32> unk13;         // 0x12DC
	be_t<u32> unk14;         // 0x12E0
	be_t<u32> unk15;         // 0x12E4
	be_t<u32> unk16;         // 0x12E8
	be_t<u32> unk17;         // 0x12F0
	be_t<u32> lastError;     // 0x12F4 error param for cellGcmSetGraphicsHandler
							 // todo: theres more to this
};

static_assert(sizeof(RsxDriverInfo) == 0x12F8, "rsxSizeTest");
static_assert(sizeof(RsxDriverInfo::Head) == 0x40, "rsxHeadSizeTest");

enum : u64
{
	// Unused
	SYS_RSX_IO_MAP_IS_STRICT = 1ull << 60
};

// Unofficial event names
enum : u64
{
	//SYS_RSX_EVENT_GRAPHICS_ERROR = 1 << 0,
	SYS_RSX_EVENT_VBLANK = 1 << 1,
	SYS_RSX_EVENT_FLIP_BASE = 1 << 3,
	SYS_RSX_EVENT_QUEUE_BASE = 1 << 5,
	SYS_RSX_EVENT_USER_CMD = 1 << 7,
	SYS_RSX_EVENT_SECOND_VBLANK_BASE = 1 << 10,
	SYS_RSX_EVENT_UNMAPPED_BASE = 1ull << 32,
};

struct RsxDmaControl
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
