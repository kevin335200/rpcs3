# cellAudioOut.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellAudioOut.h`
- **类型**: 头文件
- **行数**: 226 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellAudioOutConfiguration`
- `CellAudioOutDeviceConfiguration`
- `CellAudioOutDeviceInfo`
- `CellAudioOutDeviceInfo2`
- `CellAudioOutOption`
- `CellAudioOutRegistrationOption`
- `CellAudioOutSoundMode`
- `CellAudioOutSoundMode2`
- `CellAudioOutState`
- `audio_out_configuration`

### 关键函数

- `s32()`
- `save()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Audio/AudioBackend.h"
#include "Emu/Memory/vm_ptr.h"

// Error codes
enum CellAudioOutError : u32
{
	CELL_AUDIO_OUT_ERROR_NOT_IMPLEMENTED        = 0x8002b240,
	CELL_AUDIO_OUT_ERROR_ILLEGAL_CONFIGURATION  = 0x8002b241,
	CELL_AUDIO_OUT_ERROR_ILLEGAL_PARAMETER      = 0x8002b242,
	CELL_AUDIO_OUT_ERROR_PARAMETER_OUT_OF_RANGE = 0x8002b243,
	CELL_AUDIO_OUT_ERROR_DEVICE_NOT_FOUND       = 0x8002b244,
	CELL_AUDIO_OUT_ERROR_UNSUPPORTED_AUDIO_OUT  = 0x8002b245,
	CELL_AUDIO_OUT_ERROR_UNSUPPORTED_SOUND_MODE = 0x8002b246,
	CELL_AUDIO_OUT_ERROR_CONDITION_BUSY         = 0x8002b247,
};

enum CellAudioOut
{
	CELL_AUDIO_OUT_PRIMARY   = 0,
	CELL_AUDIO_OUT_SECONDARY = 1,
};

enum CellAudioOutDownMixer
{
	CELL_AUDIO_OUT_DOWNMIXER_NONE   = 0,
	CELL_AUDIO_OUT_DOWNMIXER_TYPE_A = 1,
	CELL_AUDIO_OUT_DOWNMIXER_TYPE_B = 2,
};

enum CellAudioOutDeviceMode
{
	CELL_AUDIO_OUT_SINGLE_DEVICE_MODE  = 0,
	CELL_AUDIO_OUT_MULTI_DEVICE_MODE   = 1,
	CELL_AUDIO_OUT_MULTI_DEVICE_MODE_2 = 2,
};

enum CellAudioOutPortType
{
	CELL_AUDIO_OUT_PORT_HDMI      = 0,
	CELL_AUDIO_OUT_PORT_SPDIF     = 1,
	CELL_AUDIO_OUT_PORT_ANALOG    = 2,
	CELL_AUDIO_OUT_PORT_USB       = 3,
	CELL_AUDIO_OUT_PORT_BLUETOOTH = 4,
	CELL_AUDIO_OUT_PORT_NETWORK   = 5,
};

enum CellAudioOutDeviceState
{
	CELL_AUDIO_OUT_DEVICE_STATE_UNAVAILABLE = 0,
	CELL_AUDIO_OUT_DEVICE_STATE_AVAILABLE   = 1,
};

enum CellAudioOutOutputState
{
	CELL_AUDIO_OUT_OUTPUT_STATE_ENABLED   = 0,
	CELL_AUDIO_OUT_OUTPUT_STATE_DISABLED  = 1,
	CELL_AUDIO_OUT_OUTPUT_STATE_PREPARING = 2,
};

enum CellAudioOutCodingType
{
	CELL_AUDIO_OUT_CODING_TYPE_LPCM               = 0,
	CELL_AUDIO_OUT_CODING_TYPE_AC3                = 1,
	CELL_AUDIO_OUT_CODING_TYPE_MPEG1              = 2,
	CELL_AUDIO_OUT_CODING_TYPE_MP3                = 3,
	CELL_AUDIO_OUT_CODING_TYPE_MPEG2              = 4,
	CELL_AUDIO_OUT_CODING_TYPE_AAC                = 5,
	CELL_AUDIO_OUT_CODING_TYPE_DTS                = 6,
	CELL_AUDIO_OUT_CODING_TYPE_ATRAC              = 7,
	CELL_AUDIO_OUT_CODING_TYPE_DOLBY_TRUE_HD      = 8, // Speculative name
	CELL_AUDIO_OUT_CODING_TYPE_DOLBY_DIGITAL_PLUS = 9,
	CELL_AUDIO_OUT_CODING_TYPE_DTS_HD_HIGHRES     = 10, // Speculative name
	CELL_AUDIO_OUT_CODING_TYPE_DTS_HD_MASTER      = 11, // Speculative name
	CELL_AUDIO_OUT_CODING_TYPE_BITSTREAM          = 0xff,
};

enum CellAudioOutChnum
{
```

## 🔗 依赖头文件

- `#include "Emu/Audio/AudioBackend.h"`
- `#include "Emu/Memory/vm_ptr.h"`
