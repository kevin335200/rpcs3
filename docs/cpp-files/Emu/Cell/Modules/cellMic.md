# cellMic.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellMic.h`
- **类型**: 头文件
- **行数**: 411 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellMicInputDefinition`
- `CellMicInputFormatI`
- `CellMicInputStream`
- `CellMicStatus`
- `mic_context`
- `mic_device`
- `microphone_device`
- `simple_ringbuf`

### 关键函数

- `add_device()`
- `convert_16_bit_pcm_to_float()`
- `enumerate_devices()`
- `get_dsp()`
- `get_raw_samplingrate()`
- `open_device()`
- `open_microphone()`
- `operator()`
- `read_bytes()`
- `read_dsp()`
- `read_raw()`
- `register_device()`
- `set_registered()`
- `stop_microphone()`
- `variable_byteswap()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/Thread.h"
#include "Utilities/mutex.h"

#include "alc.h"

// Error Codes
enum CellMicInError : u32
{
	CELL_MICIN_ERROR_ALREADY_INIT       = 0x80140101,
	CELL_MICIN_ERROR_DEVICE             = 0x80140102,
	CELL_MICIN_ERROR_NOT_INIT           = 0x80140103,
	CELL_MICIN_ERROR_PARAM              = 0x80140104,
	CELL_MICIN_ERROR_PORT_FULL          = 0x80140105,
	CELL_MICIN_ERROR_ALREADY_OPEN       = 0x80140106,
	CELL_MICIN_ERROR_NOT_OPEN           = 0x80140107,
	CELL_MICIN_ERROR_NOT_RUN            = 0x80140108,
	CELL_MICIN_ERROR_TRANS_EVENT        = 0x80140109,
	CELL_MICIN_ERROR_OPEN               = 0x8014010a,
	CELL_MICIN_ERROR_SHAREDMEMORY       = 0x8014010b,
	CELL_MICIN_ERROR_MUTEX              = 0x8014010c,
	CELL_MICIN_ERROR_EVENT_QUEUE        = 0x8014010d,
	CELL_MICIN_ERROR_DEVICE_NOT_FOUND   = 0x8014010e,
	CELL_MICIN_ERROR_FATAL              = 0x8014010f,
	CELL_MICIN_ERROR_DEVICE_NOT_SUPPORT = 0x80140110,
	// CELL_MICIN_ERROR_SYSTEM             = CELL_MICIN_ERROR_DEVICE,
	// CELL_MICIN_ERROR_SYSTEM_NOT_FOUND   = CELL_MICIN_ERROR_DEVICE_NOT_FOUND,
	// CELL_MICIN_ERROR_SYSTEM_NOT_SUPPORT = CELL_MICIN_ERROR_DEVICE_NOT_SUPPORT
};

enum CellMicInErrorDsp : u32
{
	CELL_MICIN_ERROR_DSP              = 0x80140200,
	CELL_MICIN_ERROR_DSP_ASSERT       = 0x80140201,
	CELL_MICIN_ERROR_DSP_PATH         = 0x80140202,
	CELL_MICIN_ERROR_DSP_FILE         = 0x80140203,
	CELL_MICIN_ERROR_DSP_PARAM        = 0x80140204,
	CELL_MICIN_ERROR_DSP_MEMALLOC     = 0x80140205,
	CELL_MICIN_ERROR_DSP_POINTER      = 0x80140206,
	CELL_MICIN_ERROR_DSP_FUNC         = 0x80140207,
	CELL_MICIN_ERROR_DSP_MEM          = 0x80140208,
	CELL_MICIN_ERROR_DSP_ALIGN16      = 0x80140209,
	CELL_MICIN_ERROR_DSP_ALIGN128     = 0x8014020a,
	CELL_MICIN_ERROR_DSP_EAALIGN128   = 0x8014020b,
	CELL_MICIN_ERROR_DSP_LIB_HANDLER  = 0x80140216,
	CELL_MICIN_ERROR_DSP_LIB_INPARAM  = 0x80140217,
	CELL_MICIN_ERROR_DSP_LIB_NOSPU    = 0x80140218,
	CELL_MICIN_ERROR_DSP_LIB_SAMPRATE = 0x80140219,
};

enum CellMicSignalState : u32
{
	CELLMIC_SIGSTATE_LOCTALK = 0,
	CELLMIC_SIGSTATE_FARTALK = 1,
	CELLMIC_SIGSTATE_NSR     = 3,
	CELLMIC_SIGSTATE_AGC     = 4,
	CELLMIC_SIGSTATE_MICENG  = 5,
	CELLMIC_SIGSTATE_SPKENG  = 6,
};

enum CellMicCommand
{
	CELLMIC_INIT = 0,
	CELLMIC_END,
	CELLMIC_ATTACH,
	CELLMIC_DETACH,
	CELLMIC_SWITCH,
	CELLMIC_DATA,
	CELLMIC_OPEN,
	CELLMIC_CLOSE,
	CELLMIC_START,
	CELLMIC_STOP,
	CELLMIC_QUERY,
	CELLMIC_CONFIG,
	CELLMIC_CALLBACK,
	CELLMIC_RESET,
	CELLMIC_STATUS,
	CELLMIC_IPC,
	CELLMIC_CALLBACK2,
```

## 🔗 依赖头文件

- `#include "Utilities/Thread.h"`
- `#include "Utilities/mutex.h"`
- `#include "alc.h"`
