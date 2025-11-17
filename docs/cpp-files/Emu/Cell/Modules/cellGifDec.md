# cellGifDec.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellGifDec.h`
- **类型**: 头文件
- **行数**: 248 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellGifDecDataOutInfo`
- `CellGifDecDispParam`
- `CellGifDecExtInfo`
- `CellGifDecExtThreadInParam`
- `CellGifDecExtension`
- `CellGifDecInParam`
- `CellGifDecOpnInfo`
- `CellGifDecOutParam`
- `CellGifDecStrmInfo`
- `CellGifDecStrmParam`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

// Return Codes
enum CellGifDecError : u32
{
	CELL_GIFDEC_ERROR_OPEN_FILE     = 0x80611300,
	CELL_GIFDEC_ERROR_STREAM_FORMAT = 0x80611301,
	CELL_GIFDEC_ERROR_SEQ           = 0x80611302,
	CELL_GIFDEC_ERROR_ARG           = 0x80611303,
	CELL_GIFDEC_ERROR_FATAL         = 0x80611304,
	CELL_GIFDEC_ERROR_SPU_UNSUPPORT = 0x80611305,
	CELL_GIFDEC_ERROR_SPU_ERROR     = 0x80611306,
	CELL_GIFDEC_ERROR_CB_PARAM      = 0x80611307,
};

enum CellGifDecStreamSrcSel : s32
{
	CELL_GIFDEC_FILE   = 0, // Input from a file
	CELL_GIFDEC_BUFFER = 1, // Input from a buffer
};

enum CellGifDecSpuThreadEna : s32
{
	CELL_GIFDEC_SPU_THREAD_DISABLE = 0, // Do not use SPU threads
	CELL_GIFDEC_SPU_THREAD_ENABLE  = 1, // Use SPU threads
};

enum CellGifDecRecordType : s32
{
	CELL_GIFDEC_RECORD_TYPE_IMAGE_DESC = 1, // Image data block
	CELL_GIFDEC_RECORD_TYPE_EXTENSION  = 2, // Extension block
	CELL_GIFDEC_RECORD_TYPE_TERMINATE  = 3, // Trailer block
};

enum CellGifDecColorSpace : s32
{
	CELL_GIFDEC_RGBA = 10, // RGBA
	CELL_GIFDEC_ARGB = 20, // ARGB
};

enum CellGifDecCommand : s32
{
	CELL_GIFDEC_CONTINUE = 0, // Continue decoding
	CELL_GIFDEC_STOP     = 1, // Force decoding to stop
};

enum CellGifDecDecodeStatus : s32
{
	CELL_GIFDEC_DEC_STATUS_FINISH = 0, // Decoding finished
	CELL_GIFDEC_DEC_STATUS_STOP   = 1, // Decoding was stopped
};

enum CellGifDecBufferMode : s32
{
	CELL_GIFDEC_LINE_MODE = 1
};

enum CellGifDecSpuMode : s32
{
    CELL_GIFDEC_RECEIVE_EVENT    = 0,
    CELL_GIFDEC_TRYRECEIVE_EVENT = 1
};

enum CellGifDecInterlaceMode : s32
{
    CELL_GIFDEC_NO_INTERLACE = 0,
    CELL_GIFDEC_INTERLACE    = 1
};

// Callbacks for memory management
using CellGifDecCbControlMalloc = vm::ptr<void>(u32 size, vm::ptr<void> cbCtrlMallocArg);
using CellGifDecCbControlFree = s32(vm::ptr<void> ptr, vm::ptr<void> cbCtrlFreeArg);

// Structs
struct CellGifDecThreadInParam
{
	be_t<s32> spuThreadEnable; // CellGifDecSpuThreadEna
	be_t<u32> ppuThreadPriority;
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
