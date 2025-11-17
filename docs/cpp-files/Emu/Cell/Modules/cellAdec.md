# cellAdec.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellAdec.h`
- **类型**: 头文件
- **行数**: 1,432 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `AdecCmdQueue`
- `CellAdecAttr`
- `CellAdecLpcmInfo`
- `CellAdecMP3Info`
- `CellAdecParamAc3`
- `CellAdecParamLpcm`
- `CellAdecParamMP3`
- `CellAdecResourceSpurs`
- `LpcmDecContext`
- `entry`

### 系统调用

- `sys_cond_create()`
- `sys_cond_destroy()`
- `sys_cond_signal()`
- `sys_cond_wait()`
- `sys_mutex_create()`
- `sys_mutex_destroy()`
- `sys_mutex_lock()`
- `sys_mutex_unlock()`

### HLE 函数

- `cellAdecDecodeAu()`
- `cellAdecGetPcm()`
- `cellAdecGetPcmItem()`
- `cellAdecOpen()`

## 💻 代码片段

```cpp
#pragma once

#include "cellPamf.h" // CellCodecTimeStamp
#include "../lv2/sys_mutex.h"
#include "../lv2/sys_cond.h"

// Error Codes
enum CellAdecError : u32
{
	CELL_ADEC_ERROR_FATAL   = 0x80610001,
	CELL_ADEC_ERROR_SEQ     = 0x80610002,
	CELL_ADEC_ERROR_ARG     = 0x80610003,
	CELL_ADEC_ERROR_BUSY    = 0x80610004,
	CELL_ADEC_ERROR_EMPTY   = 0x80610005,

	CELL_ADEC_ERROR_CELP_BUSY         = 0x80612e01,
	CELL_ADEC_ERROR_CELP_EMPTY        = 0x80612e02,
	CELL_ADEC_ERROR_CELP_ARG          = 0x80612e03,
	CELL_ADEC_ERROR_CELP_SEQ          = 0x80612e04,
	CELL_ADEC_ERROR_CELP_CORE_FATAL   = 0x80612e81,
	CELL_ADEC_ERROR_CELP_CORE_ARG     = 0x80612e82,
	CELL_ADEC_ERROR_CELP_CORE_SEQ     = 0x80612e83,

	CELL_ADEC_ERROR_CELP8_BUSY         = 0x80612ea1,
	CELL_ADEC_ERROR_CELP8_EMPTY        = 0x80612ea2,
	CELL_ADEC_ERROR_CELP8_ARG          = 0x80612ea3,
	CELL_ADEC_ERROR_CELP8_SEQ          = 0x80612ea4,
	CELL_ADEC_ERROR_CELP8_CORE_FATAL   = 0x80612eb1,
	CELL_ADEC_ERROR_CELP8_CORE_ARG     = 0x80612eb2,
	CELL_ADEC_ERROR_CELP8_CORE_SEQ     = 0x80612eb3,

	CELL_ADEC_ERROR_M4AAC_FATAL                                   = 0x80612401,
	CELL_ADEC_ERROR_M4AAC_SEQ                                     = 0x80612402,
	CELL_ADEC_ERROR_M4AAC_ARG                                     = 0x80612403,
	CELL_ADEC_ERROR_M4AAC_BUSY                                    = 0x80612404,
	CELL_ADEC_ERROR_M4AAC_EMPTY                                   = 0x80612405,
	CELL_ADEC_ERROR_M4AAC_BUFFER_OVERFLOW                         = 0x80612406,
	CELL_ADEC_ERROR_M4AAC_END_OF_BITSTREAM                        = 0x80612407,

	/* Core */
	CELL_ADEC_ERROR_M4AAC_CH_CONFIG_INCONSISTENCY                 = 0x80612410,
	CELL_ADEC_ERROR_M4AAC_NO_CH_DEFAULT_POS                       = 0x80612411,
	CELL_ADEC_ERROR_M4AAC_INVALID_CH_POS                          = 0x80612412,
	CELL_ADEC_ERROR_M4AAC_UNANTICIPATED_COUPLING_CH               = 0x80612413,
	CELL_ADEC_ERROR_M4AAC_INVALID_LAYER_ID                        = 0x80612414,
	CELL_ADEC_ERROR_M4AAC_ADTS_SYNCWORD_ERROR                     = 0x80612415,
	CELL_ADEC_ERROR_M4AAC_INVALID_ADTS_ID                         = 0x80612416,
	CELL_ADEC_ERROR_M4AAC_CH_CHANGED                              = 0x80612417,
	CELL_ADEC_ERROR_M4AAC_SAMPLING_FREQ_CHANGED                   = 0x80612418,
	CELL_ADEC_ERROR_M4AAC_WRONG_SBR_CH                            = 0x80612419,
	CELL_ADEC_ERROR_M4AAC_WRONG_SCALE_FACTOR                      = 0x8061241a,
	CELL_ADEC_ERROR_M4AAC_INVALID_BOOKS                           = 0x8061241b,
	CELL_ADEC_ERROR_M4AAC_INVALID_SECTION_DATA                    = 0x8061241c,
	CELL_ADEC_ERROR_M4AAC_PULSE_IS_NOT_LONG                       = 0x8061241d,
	CELL_ADEC_ERROR_M4AAC_GC_IS_NOT_SUPPORTED                     = 0x8061241e,
	CELL_ADEC_ERROR_M4AAC_INVALID_ELEMENT_ID                      = 0x8061241f,
	CELL_ADEC_ERROR_M4AAC_NO_CH_CONFIG                            = 0x80612420,
	CELL_ADEC_ERROR_M4AAC_UNEXPECTED_OVERLAP_CRC                  = 0x80612421,
	CELL_ADEC_ERROR_M4AAC_CRC_BUFFER_EXCEEDED                     = 0x80612422,
	CELL_ADEC_ERROR_M4AAC_INVALID_CRC                             = 0x80612423,
	CELL_ADEC_ERROR_M4AAC_BAD_WINDOW_CODE                         = 0x80612424,
	CELL_ADEC_ERROR_M4AAC_INVALID_ADIF_HEADER_ID                  = 0x80612425,
	CELL_ADEC_ERROR_M4AAC_NOT_SUPPORTED_PROFILE                   = 0x80612426,
	CELL_ADEC_ERROR_M4AAC_PROG_NUMBER_NOT_FOUND                   = 0x80612427,
	CELL_ADEC_ERROR_M4AAC_INVALID_SAMP_RATE_INDEX                 = 0x80612428,
	CELL_ADEC_ERROR_M4AAC_UNANTICIPATED_CH_CONFIG                 = 0x80612429,
	CELL_ADEC_ERROR_M4AAC_PULSE_OVERFLOWED                        = 0x8061242a,
	CELL_ADEC_ERROR_M4AAC_CAN_NOT_UNPACK_INDEX                    = 0x8061242b,
	CELL_ADEC_ERROR_M4AAC_DEINTERLEAVE_FAILED                     = 0x8061242c,
	CELL_ADEC_ERROR_M4AAC_CALC_BAND_OFFSET_FAILED                 = 0x8061242d,
	CELL_ADEC_ERROR_M4AAC_GET_SCALE_FACTOR_FAILED                 = 0x8061242e,
	CELL_ADEC_ERROR_M4AAC_GET_CC_GAIN_FAILED                      = 0x8061242f,
	CELL_ADEC_ERROR_M4AAC_MIX_COUPLING_CH_FAILED                  = 0x80612430,
	CELL_ADEC_ERROR_M4AAC_GROUP_IS_INVALID                        = 0x80612431,
	CELL_ADEC_ERROR_M4AAC_PREDICT_FAILED                          = 0x80612432,
	CELL_ADEC_ERROR_M4AAC_INVALID_PREDICT_RESET_PATTERN           = 0x80612433,
	CELL_ADEC_ERROR_M4AAC_INVALID_TNS_FRAME_INFO                  = 0x80612434,
	CELL_ADEC_ERROR_M4AAC_GET_MASK_FAILED                         = 0x80612435,
	CELL_ADEC_ERROR_M4AAC_GET_GROUP_FAILED                        = 0x80612436,
	CELL_ADEC_ERROR_M4AAC_GET_LPFLAG_FAILED                       = 0x80612437,
```

## 🔗 依赖头文件

- `#include "cellPamf.h" // CellCodecTimeStamp`
- `#include "../lv2/sys_mutex.h"`
- `#include "../lv2/sys_cond.h"`
