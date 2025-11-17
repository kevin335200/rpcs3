# sys_rsxaudio.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_rsxaudio.h`
- **类型**: 头文件
- **行数**: 635 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `backend_config`
- `ctrl_t`
- `entry_t`
- `hdmi_ch_cfg_t`
- `kevent`
- `rsxaudio_backend_thread`
- `rsxaudio_data_container`
- `rsxaudio_data_thread`
- `rsxaudio_hw_param_t`
- `vtimer`

### 系统调用

- `sys_rsxaudio_close_connection()`
- `sys_rsxaudio_create_connection()`
- `sys_rsxaudio_finalize()`
- `sys_rsxaudio_get_dma_param()`
- `sys_rsxaudio_import_shared_memory()`
- `sys_rsxaudio_initialize()`
- `sys_rsxaudio_prepare_process()`
- `sys_rsxaudio_start_process()`
- `sys_rsxaudio_stop_process()`
- `sys_rsxaudio_unimport_shared_memory()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"
#include "sys_event.h"
#include "Utilities/simple_ringbuf.h"
#include "Utilities/transactional_storage.h"
#include "Utilities/cond.h"
#include "Emu/system_config_types.h"
#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"
#include "Emu/Audio/AudioDumper.h"
#include "Emu/Audio/AudioBackend.h"
#include "Emu/Audio/audio_resampler.h"

#if defined(unix) || defined(__unix) || defined(__unix__)
// For BSD detection
#include <sys/param.h>
#endif

#ifdef _WIN32
#include <windows.h>
#elif defined(BSD) || defined(__APPLE__)
#include <sys/event.h>
#endif

enum : u32
{
	SYS_RSXAUDIO_SERIAL_STREAM_CNT        = 4,
	SYS_RSXAUDIO_STREAM_DATA_BLK_CNT      = 4,
	SYS_RSXAUDIO_DATA_BLK_SIZE            = 256,
	SYS_RSXAUDIO_STREAM_SIZE              = SYS_RSXAUDIO_DATA_BLK_SIZE * SYS_RSXAUDIO_STREAM_DATA_BLK_CNT,
	SYS_RSXAUDIO_CH_PER_STREAM            = 2,
	SYS_RSXAUDIO_SERIAL_MAX_CH            = 8,
	SYS_RSXAUDIO_SPDIF_MAX_CH             = 2,
	SYS_RSXAUDIO_STREAM_SAMPLE_CNT        = SYS_RSXAUDIO_STREAM_SIZE / SYS_RSXAUDIO_CH_PER_STREAM / sizeof(f32),

	SYS_RSXAUDIO_RINGBUF_BLK_SZ_SERIAL    = SYS_RSXAUDIO_STREAM_SIZE * SYS_RSXAUDIO_SERIAL_STREAM_CNT,
	SYS_RSXAUDIO_RINGBUF_BLK_SZ_SPDIF     = SYS_RSXAUDIO_STREAM_SIZE,

	SYS_RSXAUDIO_RINGBUF_SZ	              = 16,

	SYS_RSXAUDIO_AVPORT_CNT               = 5,

	SYS_RSXAUDIO_FREQ_BASE_384K           = 384000,
	SYS_RSXAUDIO_FREQ_BASE_352K           = 352800,

	SYS_RSXAUDIO_PORT_CNT                 = 3,

	SYS_RSXAUDIO_SPDIF_CNT                = 2,
};

enum class RsxaudioAvportIdx : u8
{
	HDMI_0  = 0,
	HDMI_1  = 1,
	AVMULTI = 2,
	SPDIF_0 = 3,
	SPDIF_1 = 4,
};

enum class RsxaudioPort : u8
{
	SERIAL  = 0,
	SPDIF_0 = 1,
	SPDIF_1 = 2,
	INVALID = 0xFF,
};

enum class RsxaudioSampleSize : u8
{
	_16BIT = 2,
	_32BIT = 4,
};

struct rsxaudio_shmem
{
	struct ringbuf_t
	{
		struct entry_t
		{
```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "sys_event.h"`
- `#include "Utilities/simple_ringbuf.h"`
- `#include "Utilities/transactional_storage.h"`
- `#include "Utilities/cond.h"`
- `#include "Emu/system_config_types.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "Emu/Audio/AudioDumper.h"`
- `#include "Emu/Audio/AudioBackend.h"`
