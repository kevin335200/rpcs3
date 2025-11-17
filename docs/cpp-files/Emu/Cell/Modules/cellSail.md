# cellSail.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSail.h`
- **类型**: 头文件
- **行数**: 1,278 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellSailAuInfo`
- `CellSailAuReceiver`
- `CellSailAudioFormat`
- `CellSailGraphicsAdapter`
- `CellSailMemAllocatorFuncs`
- `CellSailRendererAudio`
- `CellSailRendererVideoAttribute`
- `audio`
- `frame`
- `video`

### 关键函数

- `ParameterCodeToName()`
- `to()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "cellVpost.h"

// Error Codes
enum CellSailError : u32
{
	CELL_SAIL_ERROR_INVALID_ARG        = 0x80610701,
	CELL_SAIL_ERROR_INVALID_STATE      = 0x80610702,
	CELL_SAIL_ERROR_UNSUPPORTED_STREAM = 0x80610703,
	CELL_SAIL_ERROR_INDEX_OUT_OF_RANGE = 0x80610704,
	CELL_SAIL_ERROR_EMPTY              = 0x80610705,
	CELL_SAIL_ERROR_FULLED             = 0x80610706,
	CELL_SAIL_ERROR_USING              = 0x80610707,
	CELL_SAIL_ERROR_NOT_AVAILABLE      = 0x80610708,
	CELL_SAIL_ERROR_CANCEL             = 0x80610709,
	CELL_SAIL_ERROR_MEMORY             = 0x806107F0,
	CELL_SAIL_ERROR_INVALID_FD         = 0x806107F1,
	CELL_SAIL_ERROR_FATAL              = 0x806107FF,
};

// Call types
enum
{
	CELL_SAIL_PLAYER_CALL_NONE                  = 0,
	CELL_SAIL_PLAYER_CALL_BOOT                  = 1,
	CELL_SAIL_PLAYER_CALL_OPEN_STREAM           = 2,
	CELL_SAIL_PLAYER_CALL_CLOSE_STREAM          = 3,
	CELL_SAIL_PLAYER_CALL_OPEN_ES_AUDIO         = 4,
	CELL_SAIL_PLAYER_CALL_OPEN_ES_VIDEO         = 5,
	CELL_SAIL_PLAYER_CALL_OPEN_ES_USER          = 6,
	CELL_SAIL_PLAYER_CALL_CLOSE_ES_AUDIO        = 7,
	CELL_SAIL_PLAYER_CALL_CLOSE_ES_VIDEO        = 8,
	CELL_SAIL_PLAYER_CALL_CLOSE_ES_USER         = 9,
	CELL_SAIL_PLAYER_CALL_START                 = 10,
	CELL_SAIL_PLAYER_CALL_STOP                  = 11,
	CELL_SAIL_PLAYER_CALL_NEXT                  = 12,
	CELL_SAIL_PLAYER_CALL_REOPEN_ES_AUDIO       = 13,
	CELL_SAIL_PLAYER_CALL_REOPEN_ES_VIDEO       = 14,
	CELL_SAIL_PLAYER_CALL_REOPEN_ES_USER        = 15,

	_CELL_SAIL_PLAYER_CALL_TYPE_NUM_OF_ELEMENTS = 16, // Never used?
};

// State types
enum
{
	CELL_SAIL_PLAYER_STATE_INITIALIZED           = 0,
	CELL_SAIL_PLAYER_STATE_BOOT_TRANSITION       = 1,
	CELL_SAIL_PLAYER_STATE_CLOSED                = 2,
	CELL_SAIL_PLAYER_STATE_OPEN_TRANSITION       = 3,
	CELL_SAIL_PLAYER_STATE_OPENED                = 4,
	CELL_SAIL_PLAYER_STATE_START_TRANSITION      = 5,
	CELL_SAIL_PLAYER_STATE_RUNNING               = 6,
	CELL_SAIL_PLAYER_STATE_STOP_TRANSITION       = 7,
	CELL_SAIL_PLAYER_STATE_CLOSE_TRANSITION      = 8,
	CELL_SAIL_PLAYER_STATE_LOST                  = 9,
	_CELL_SAIL_PLAYER_STATE_TYPE_NUM_OF_ELEMENTS = 10, // Never used?
};

// Preset types
enum
{
	CELL_SAIL_PLAYER_PRESET_AV_SYNC             = 0, // Deprecated, same as 59_94HZ
	CELL_SAIL_PLAYER_PRESET_AS_IS               = 1,
	CELL_SAIL_PLAYER_PRESET_AV_SYNC_59_94HZ     = 2,
	CELL_SAIL_PLAYER_PRESET_AV_SYNC_29_97HZ     = 3,
	CELL_SAIL_PLAYER_PRESET_AV_SYNC_50HZ        = 4,
	CELL_SAIL_PLAYER_PRESET_AV_SYNC_25HZ        = 5,
	CELL_SAIL_PLAYER_PRESET_AV_SYNC_AUTO_DETECT = 6,
};

// Event types
enum
{
	CELL_SAIL_EVENT_EMPTY                 = 0, // NEVER USED
	CELL_SAIL_EVENT_ERROR_OCCURED         = 1,
	CELL_SAIL_EVENT_PLAYER_CALL_COMPLETED = 2,
	CELL_SAIL_EVENT_PLAYER_STATE_CHANGED  = 3,
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "cellVpost.h"`
