# cellCamera.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellCamera.h`
- **类型**: 头文件
- **行数**: 487 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellCameraInfo`
- `CellCameraInfoEx`
- `CellCameraReadEx`
- `attr_t`
- `camera_context`
- `gem_camera_shared`
- `notify_event_data`

### HLE 函数

- `cellCamera()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/Thread.h"
#include "Emu/Io/camera_handler_base.h"
#include "Emu/Memory/vm_ptr.h"
#include "Utilities/mutex.h"

#include <map>


// Error Codes
enum CellCameraError : u32
{
	CELL_CAMERA_ERROR_ALREADY_INIT       = 0x80140801,
	CELL_CAMERA_ERROR_NOT_INIT           = 0x80140803,
	CELL_CAMERA_ERROR_PARAM              = 0x80140804,
	CELL_CAMERA_ERROR_ALREADY_OPEN       = 0x80140805,
	CELL_CAMERA_ERROR_NOT_OPEN           = 0x80140806,
	CELL_CAMERA_ERROR_DEVICE_NOT_FOUND   = 0x80140807,
	CELL_CAMERA_ERROR_DEVICE_DEACTIVATED = 0x80140808,
	CELL_CAMERA_ERROR_NOT_STARTED        = 0x80140809,
	CELL_CAMERA_ERROR_FORMAT_UNKNOWN     = 0x8014080a,
	CELL_CAMERA_ERROR_RESOLUTION_UNKNOWN = 0x8014080b,
	CELL_CAMERA_ERROR_BAD_FRAMERATE      = 0x8014080c,
	CELL_CAMERA_ERROR_TIMEOUT            = 0x8014080d,
	CELL_CAMERA_ERROR_BUSY               = 0x8014080e,
	CELL_CAMERA_ERROR_FATAL              = 0x8014080f,
	CELL_CAMERA_ERROR_MUTEX              = 0x80140810,
};

// Event masks
enum
{
	CELL_CAMERA_EFLAG_FRAME_UPDATE = 0x00000001,
	CELL_CAMERA_EFLAG_OPEN         = 0x00000002,
	CELL_CAMERA_EFLAG_CLOSE        = 0x00000004,
	CELL_CAMERA_EFLAG_START        = 0x00000008,
	CELL_CAMERA_EFLAG_STOP         = 0x00000010,
	CELL_CAMERA_EFLAG_RESET        = 0x00000020,
};

// Event types
enum
{
	CELL_CAMERA_DETACH       = 0,
	CELL_CAMERA_ATTACH       = 1,
	CELL_CAMERA_FRAME_UPDATE = 2,
	CELL_CAMERA_OPEN         = 3,
	CELL_CAMERA_CLOSE        = 4,
	CELL_CAMERA_START        = 5,
	CELL_CAMERA_STOP         = 6,
	CELL_CAMERA_RESET        = 7
};

// Read mode
enum
{
	CELL_CAMERA_READ_FUNCCALL = 0,
	CELL_CAMERA_READ_DIRECT   = 1,
};

// Colormatching
enum
{
	CELL_CAMERA_CM_CP_UNSPECIFIED = 0,
	CELL_CAMERA_CM_CP_BT709_sRGB  = 1,
	CELL_CAMERA_CM_CP_BT470_2M    = 2,
	CELL_CAMERA_CM_CP_BT470_2BG   = 3,
	CELL_CAMERA_CM_CP_SMPTE170M   = 4,
	CELL_CAMERA_CM_CP_SMPTE240M   = 5,

	CELL_CAMERA_CM_TC_UNSPECIFIED = 0,
	CELL_CAMERA_CM_TC_BT709       = 1,
	CELL_CAMERA_CM_TC_BT470_2M    = 2,
	CELL_CAMERA_CM_TC_BT470_2BG   = 3,
	CELL_CAMERA_CM_TC_SMPTE170M   = 4,
	CELL_CAMERA_CM_TC_SMPTE240M   = 5,
	CELL_CAMERA_CM_TC_LINEAR      = 6,
	CELL_CAMERA_CM_TC_sRGB        = 7,

```

## 🔗 依赖头文件

- `#include "Utilities/Thread.h"`
- `#include "Emu/Io/camera_handler_base.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Utilities/mutex.h"`
- `#include <map>`
