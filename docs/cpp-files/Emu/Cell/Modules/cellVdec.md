# cellVdec.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellVdec.h`
- **类型**: 头文件
- **行数**: 674 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellVdecAuInfo`
- `CellVdecAvcInfo`
- `CellVdecCb`
- `CellVdecDivxInfo`
- `CellVdecDivxSpecificInfo`
- `CellVdecMpeg2Info`
- `CellVdecResource`
- `CellVdecResourceEx`
- `CellVdecType`
- `CellVdecTypeEx`

## 💻 代码片段

```cpp
#pragma once

// Error Codes
enum CellVdecError : u32
{
	CELL_VDEC_ERROR_ARG   = 0x80610101,
	CELL_VDEC_ERROR_SEQ   = 0x80610102,
	CELL_VDEC_ERROR_BUSY  = 0x80610103,
	CELL_VDEC_ERROR_EMPTY = 0x80610104,
	CELL_VDEC_ERROR_AU    = 0x80610105,
	CELL_VDEC_ERROR_PIC   = 0x80610106,
	CELL_VDEC_ERROR_FATAL = 0x80610180,
};

enum CellVdecCodecType : s32
{
	CELL_VDEC_CODEC_TYPE_MPEG2 = 0,
	CELL_VDEC_CODEC_TYPE_AVC   = 1,
	CELL_VDEC_CODEC_TYPE_DIVX  = 5,
	CELL_VDEC_CODEC_TYPE_MAX
};

// Callback Messages
enum CellVdecMsgType : s32
{
	CELL_VDEC_MSG_TYPE_AUDONE  = 0, // decoding finished
	CELL_VDEC_MSG_TYPE_PICOUT  = 1, // picture done
	CELL_VDEC_MSG_TYPE_SEQDONE = 2, // finishing done
	CELL_VDEC_MSG_TYPE_ERROR   = 3, // fatal error
};

// Decoder Operation Mode
enum CellVdecDecodeMode : s32
{
	CELL_VDEC_DEC_MODE_NORMAL,
	CELL_VDEC_DEC_MODE_B_SKIP,
	CELL_VDEC_DEC_MODE_PB_SKIP,
};

// Output Picture Format Type
enum CellVdecPicFormatType : u32
{
	CELL_VDEC_PICFMT_ARGB32_ILV,
	CELL_VDEC_PICFMT_RGBA32_ILV,
	CELL_VDEC_PICFMT_UYVY422_ILV,
	CELL_VDEC_PICFMT_YUV420_PLANAR,
};

// Output Color Matrix Coef
enum CellVdecColorMatrixType : u32
{
	CELL_VDEC_COLOR_MATRIX_TYPE_BT601,
	CELL_VDEC_COLOR_MATRIX_TYPE_BT709,
};

enum CellVdecPicAttr : s32
{
	CELL_VDEC_PICITEM_ATTR_NORMAL,
	CELL_VDEC_PICITEM_ATTR_SKIPPED,
};

// Universal Frame Rate Code
enum CellVdecFrameRate : s32
{
	CELL_VDEC_FRC_24000DIV1001 = 0x80,
	CELL_VDEC_FRC_24           = 0x81,
	CELL_VDEC_FRC_25           = 0x82,
	CELL_VDEC_FRC_30000DIV1001 = 0x83,
	CELL_VDEC_FRC_30           = 0x84,
	CELL_VDEC_FRC_50           = 0x85,
	CELL_VDEC_FRC_60000DIV1001 = 0x86,
	CELL_VDEC_FRC_60           = 0x87,
};

enum
{
	CELL_CODEC_PTS_INVALID = 0xffffffff,
	CELL_CODEC_DTS_INVALID = 0xffffffff,
};

```

