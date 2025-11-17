# cellGem.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellGem.h`
- **类型**: 头文件
- **行数**: 280 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellGemAttribute`
- `CellGemCameraState`
- `CellGemExtPortData`
- `CellGemImageState`
- `CellGemInertialState`
- `CellGemInfo`
- `CellGemPadData`
- `CellGemState`
- `CellGemVideoConvertAttribute`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

static const float CELL_GEM_SPHERE_RADIUS_MM = 22.5f;

// Error codes
enum CellGemError : u32
{
	CELL_GEM_ERROR_RESOURCE_ALLOCATION_FAILED = 0x80121801,
	CELL_GEM_ERROR_ALREADY_INITIALIZED        = 0x80121802,
	CELL_GEM_ERROR_UNINITIALIZED              = 0x80121803,
	CELL_GEM_ERROR_INVALID_PARAMETER          = 0x80121804,
	CELL_GEM_ERROR_INVALID_ALIGNMENT          = 0x80121805,
	CELL_GEM_ERROR_UPDATE_NOT_FINISHED        = 0x80121806,
	CELL_GEM_ERROR_UPDATE_NOT_STARTED         = 0x80121807,
	CELL_GEM_ERROR_CONVERT_NOT_FINISHED       = 0x80121808,
	CELL_GEM_ERROR_CONVERT_NOT_STARTED        = 0x80121809,
	CELL_GEM_ERROR_WRITE_NOT_FINISHED         = 0x8012180A,
	CELL_GEM_ERROR_NOT_A_HUE                  = 0x8012180B,
};

// Runtime statuses
enum CellGemStatus : u32
{
	CELL_GEM_NOT_CONNECTED              = 1,
	CELL_GEM_SPHERE_NOT_CALIBRATED      = 2,
	CELL_GEM_SPHERE_CALIBRATING         = 3,
	CELL_GEM_COMPUTING_AVAILABLE_COLORS = 4,
	CELL_GEM_HUE_NOT_SET                = 5,
	CELL_GEM_NO_VIDEO                   = 6,
	CELL_GEM_TIME_OUT_OF_RANGE          = 7,
	CELL_GEM_NOT_CALIBRATED             = 8,
	CELL_GEM_NO_EXTERNAL_PORT_DEVICE    = 9,
};

// CellGemInfo status flags.
enum
{
	CELL_GEM_STATUS_DISCONNECTED = 0,
	CELL_GEM_STATUS_READY        = 1,
};

// CellGemPadData defines for bit assignment of digital buttons.
enum
{
	CELL_GEM_CTRL_SELECT   = 1 << 0,
	CELL_GEM_CTRL_T        = 1 << 1,
	CELL_GEM_CTRL_MOVE     = 1 << 2,
	CELL_GEM_CTRL_START    = 1 << 3,
	CELL_GEM_CTRL_TRIANGLE = 1 << 4,
	CELL_GEM_CTRL_CIRCLE   = 1 << 5,
	CELL_GEM_CTRL_CROSS    = 1 << 6,
	CELL_GEM_CTRL_SQUARE   = 1 << 7,
};

// Bit assignments for CellGemExtPortData status member.
enum
{
	CELL_GEM_EXT_CONNECTED = 1 << 0,
	CELL_GEM_EXT_EXT0      = 1 << 1,
	CELL_GEM_EXT_EXT1      = 1 << 2,
};

// Values used to describe characteristics of the extension connector.
enum
{
	CELL_GEM_EXTERNAL_PORT_DEVICE_INFO_SIZE = 38,
	CELL_GEM_EXTERNAL_PORT_OUTPUT_SIZE      = 40,
};

// Limits for cellGemPrepareCamera max_exposure argument.
enum
{
	CELL_GEM_MIN_CAMERA_EXPOSURE = 40,
	CELL_GEM_MAX_CAMERA_EXPOSURE = 511,
};

// Flags for cellGemGetState.
enum
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
