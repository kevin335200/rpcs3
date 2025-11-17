# cellAudio.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellAudio.h`
- **类型**: 头文件
- **行数**: 436 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellAudioPortConfig`
- `CellAudioPortParam`
- `audio_port`
- `audio_ringbuffer`
- `cell_audio_config`
- `cell_audio_thread`
- `key_info`
- `level_set_t`
- `lv2_event_queue`
- `raw_config`

### HLE 函数

- `cell_audio_config()`
- `cell_audio_thread()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Utilities/Thread.h"
#include "Utilities/simple_ringbuf.h"
#include "Emu/Memory/vm.h"
#include "Emu/Audio/AudioBackend.h"
#include "Emu/Audio/AudioDumper.h"
#include "Emu/Audio/audio_resampler.h"
#include "Emu/system_config_types.h"

struct lv2_event_queue;

// Error codes
enum CellAudioError : u32
{
	CELL_AUDIO_ERROR_ALREADY_INIT               = 0x80310701,
	CELL_AUDIO_ERROR_AUDIOSYSTEM                = 0x80310702,
	CELL_AUDIO_ERROR_NOT_INIT                   = 0x80310703,
	CELL_AUDIO_ERROR_PARAM                      = 0x80310704,
	CELL_AUDIO_ERROR_PORT_FULL                  = 0x80310705,
	CELL_AUDIO_ERROR_PORT_ALREADY_RUN           = 0x80310706,
	CELL_AUDIO_ERROR_PORT_NOT_OPEN              = 0x80310707,
	CELL_AUDIO_ERROR_PORT_NOT_RUN               = 0x80310708,
	CELL_AUDIO_ERROR_TRANS_EVENT                = 0x80310709,
	CELL_AUDIO_ERROR_PORT_OPEN                  = 0x8031070a,
	CELL_AUDIO_ERROR_SHAREDMEMORY               = 0x8031070b,
	CELL_AUDIO_ERROR_MUTEX                      = 0x8031070c,
	CELL_AUDIO_ERROR_EVENT_QUEUE                = 0x8031070d,
	CELL_AUDIO_ERROR_AUDIOSYSTEM_NOT_FOUND      = 0x8031070e,
	CELL_AUDIO_ERROR_TAG_NOT_FOUND              = 0x8031070f,
};

// constants
enum
{
	CELL_AUDIO_BLOCK_8                 = 8,
	CELL_AUDIO_BLOCK_16                = 16,
	CELL_AUDIO_BLOCK_32                = 32,
	CELL_AUDIO_BLOCK_SAMPLES           = 256,

	CELL_AUDIO_CREATEEVENTFLAG_SPU     = 0x00000001,

	CELL_AUDIO_EVENT_MIX               = 0,
	CELL_AUDIO_EVENT_HEADPHONE         = 1,

	CELL_AUDIO_EVENTFLAG_BEFOREMIX     = 0x80000000,
	CELL_AUDIO_EVENTFLAG_DECIMATE_2    = 0x08000000,
	CELL_AUDIO_EVENTFLAG_DECIMATE_4    = 0x10000000,
	CELL_AUDIO_EVENTFLAG_HEADPHONE     = 0x20000000,
	CELL_AUDIO_EVENTFLAG_NOMIX         = 0x40000000,

	CELL_AUDIO_MAX_PORT                = 4,
	CELL_AUDIO_MAX_PORT_2              = 8,

	CELL_AUDIO_MISC_ACCVOL_ALLDEVICE   = 0x0000ffffUL,
	CELL_AUDIO_PERSONAL_DEVICE_PRIMARY = 0x8000,

	CELL_AUDIO_PORT_2CH                = 2,
	CELL_AUDIO_PORT_8CH                = 8,

	CELL_AUDIO_PORTATTR_BGM            = 0x0000000000000010ULL,
	CELL_AUDIO_PORTATTR_INITLEVEL      = 0x0000000000001000ULL,
	CELL_AUDIO_PORTATTR_OUT_NO_ROUTE   = 0x0000000000100000ULL,
	CELL_AUDIO_PORTATTR_OUT_PERSONAL_0 = 0x0000000001000000ULL,
	CELL_AUDIO_PORTATTR_OUT_PERSONAL_1 = 0x0000000002000000ULL,
	CELL_AUDIO_PORTATTR_OUT_PERSONAL_2 = 0x0000000004000000ULL,
	CELL_AUDIO_PORTATTR_OUT_PERSONAL_3 = 0x0000000008000000ULL,
	CELL_AUDIO_PORTATTR_OUT_SECONDARY  = 0x0000000000000001ULL,
	CELL_AUDIO_PORTATTR_OUT_STREAM1    = 0x0000000000000001ULL,

	CELL_AUDIO_STATUS_CLOSE            = 0x1010,
	CELL_AUDIO_STATUS_READY            = 1,
	CELL_AUDIO_STATUS_RUN              = 2,
};

enum class audio_backend_update : u32
{
	NONE,
	PARAM,
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Utilities/Thread.h"`
- `#include "Utilities/simple_ringbuf.h"`
- `#include "Emu/Memory/vm.h"`
- `#include "Emu/Audio/AudioBackend.h"`
- `#include "Emu/Audio/AudioDumper.h"`
- `#include "Emu/Audio/audio_resampler.h"`
- `#include "Emu/system_config_types.h"`
