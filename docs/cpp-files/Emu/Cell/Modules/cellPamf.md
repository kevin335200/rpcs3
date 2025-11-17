# cellPamf.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPamf.h`
- **类型**: 头文件
- **行数**: 938 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellCodecEsFilterId`
- `CellPamfAc3Info`
- `CellPamfEpUnk`
- `PamfGroup`
- `PsmfEpHeader`
- `PsmfGroupingPeriod`
- `PsmfHeader`
- `PsmfSequenceInfo`
- `PsmfStreamHeader`
- `squeue_data_t`

### HLE 函数

- `cellPamfReaderInitialize()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

// Error Codes
enum CellPamfError : u32
{
	CELL_PAMF_ERROR_STREAM_NOT_FOUND    = 0x80610501,
	CELL_PAMF_ERROR_INVALID_PAMF        = 0x80610502,
	CELL_PAMF_ERROR_INVALID_ARG         = 0x80610503,
	CELL_PAMF_ERROR_UNKNOWN_TYPE        = 0x80610504,
	CELL_PAMF_ERROR_UNSUPPORTED_VERSION = 0x80610505,
	CELL_PAMF_ERROR_UNKNOWN_STREAM      = 0x80610506,
	CELL_PAMF_ERROR_EP_NOT_FOUND        = 0x80610507,
	CELL_PAMF_ERROR_NOT_AVAILABLE       = 0x80610508,
};

// PamfReaderInitialize Attribute Flags
enum
{
	CELL_PAMF_ATTRIBUTE_VERIFY_ON = 1,
	CELL_PAMF_ATTRIBUTE_MINIMUM_HEADER = 2,
};

enum CellPamfStreamType
{
	CELL_PAMF_STREAM_TYPE_AVC             = 0,
	CELL_PAMF_STREAM_TYPE_M2V             = 1,
	CELL_PAMF_STREAM_TYPE_ATRAC3PLUS      = 2,
	CELL_PAMF_STREAM_TYPE_PAMF_LPCM       = 3,
	CELL_PAMF_STREAM_TYPE_AC3             = 4,
	CELL_PAMF_STREAM_TYPE_USER_DATA       = 5,
	CELL_PAMF_STREAM_TYPE_PSMF_AVC        = 6,
	CELL_PAMF_STREAM_TYPE_PSMF_ATRAC3PLUS = 7,
	CELL_PAMF_STREAM_TYPE_PSMF_LPCM       = 8,
	CELL_PAMF_STREAM_TYPE_PSMF_USER_DATA  = 9,
	CELL_PAMF_STREAM_TYPE_VIDEO           = 20,
	CELL_PAMF_STREAM_TYPE_AUDIO           = 21,
	CELL_PAMF_STREAM_TYPE_UNK             = 22,
};

enum PamfStreamCodingType : u8
{
	PAMF_STREAM_CODING_TYPE_M2V        = 0x02,
	PAMF_STREAM_CODING_TYPE_AVC        = 0x1b,
	PAMF_STREAM_CODING_TYPE_PAMF_LPCM  = 0x80,
	PAMF_STREAM_CODING_TYPE_AC3        = 0x81,
	PAMF_STREAM_CODING_TYPE_ATRAC3PLUS = 0xdc,
	PAMF_STREAM_CODING_TYPE_USER_DATA  = 0xdd,
	PAMF_STREAM_CODING_TYPE_PSMF       = 0xff,
};

enum
{
	CELL_PAMF_FS_48kHz = 1,
};

enum
{
	CELL_PAMF_BIT_LENGTH_16 = 1,
	CELL_PAMF_BIT_LENGTH_24 = 3,
};

enum
{
	CELL_PAMF_AVC_PROFILE_MAIN = 77,
	CELL_PAMF_AVC_PROFILE_HIGH = 100,
};

enum
{
	CELL_PAMF_AVC_LEVEL_2P1 = 21,
	CELL_PAMF_AVC_LEVEL_3P0 = 30,
	CELL_PAMF_AVC_LEVEL_3P1 = 31,
	CELL_PAMF_AVC_LEVEL_3P2 = 32,
	CELL_PAMF_AVC_LEVEL_4P1 = 41,
	CELL_PAMF_AVC_LEVEL_4P2 = 42,
};

enum
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include <mutex>`
- `#include <condition_variable>`
