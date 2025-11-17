# cellPngDec.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPngDec.h`
- **类型**: 头文件
- **行数**: 349 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPngDecCbCtrlDisp`
- `CellPngDecDispInfo`
- `CellPngDecDispParam`
- `CellPngDecExtOutParam`
- `CellPngDecExtThreadInParam`
- `CellPngDecExtThreadOutParam`
- `CellPngDecInfo`
- `CellPngDecStrmInfo`
- `CellPngDecStrmParam`
- `PngHandle`

### HLE 函数

- `cellPngColorSpaceHasAlpha()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

#include "png.h"

enum : u32
{
	PNGDEC_CODEC_VERSION = 0x00420000,
};

// Return Codes
enum CellPngDecError
{
	CELL_PNGDEC_ERROR_HEADER        = 0x80611201,
	CELL_PNGDEC_ERROR_STREAM_FORMAT = 0x80611202,
	CELL_PNGDEC_ERROR_ARG           = 0x80611203,
	CELL_PNGDEC_ERROR_SEQ           = 0x80611204,
	CELL_PNGDEC_ERROR_BUSY          = 0x80611205,
	CELL_PNGDEC_ERROR_FATAL         = 0x80611206,
	CELL_PNGDEC_ERROR_OPEN_FILE     = 0x80611207,
	CELL_PNGDEC_ERROR_SPU_UNSUPPORT = 0x80611208,
	CELL_PNGDEC_ERROR_SPU_ERROR     = 0x80611209,
	CELL_PNGDEC_ERROR_CB_PARAM      = 0x8061120a,
};

// Consts
enum CellPngDecColorSpace : s32
{
	CELL_PNGDEC_GRAYSCALE       = 1,
	CELL_PNGDEC_RGB             = 2,
	CELL_PNGDEC_PALETTE         = 4,
	CELL_PNGDEC_GRAYSCALE_ALPHA = 9,
	CELL_PNGDEC_RGBA            = 10,
	CELL_PNGDEC_ARGB            = 20,
};

enum CellPngDecSpuThreadEna : s32
{
	CELL_PNGDEC_SPU_THREAD_DISABLE = 0,
	CELL_PNGDEC_SPU_THREAD_ENABLE  = 1,
};

enum CellPngDecStreamSrcSel : s32
{
	CELL_PNGDEC_FILE   = 0,
	CELL_PNGDEC_BUFFER = 1,
};

enum CellPngDecInterlaceMode : s32
{
	CELL_PNGDEC_NO_INTERLACE = 0,
	CELL_PNGDEC_ADAM7_INTERLACE = 1,
};

enum CellPngDecOutputMode : s32
{
	CELL_PNGDEC_TOP_TO_BOTTOM = 0,
	CELL_PNGDEC_BOTTOM_TO_TOP = 1,
};

enum CellPngDecPackFlag : s32
{
	CELL_PNGDEC_1BYTE_PER_NPIXEL = 0,
	CELL_PNGDEC_1BYTE_PER_1PIXEL = 1,
};

enum CellPngDecAlphaSelect : s32
{
	CELL_PNGDEC_STREAM_ALPHA = 0,
	CELL_PNGDEC_FIX_ALPHA    = 1,
};

enum CellPngDecCommand : s32
{
	CELL_PNGDEC_CONTINUE = 0,
	CELL_PNGDEC_STOP     = 1,
};

enum CellPngDecDecodeStatus : s32
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "png.h"`
