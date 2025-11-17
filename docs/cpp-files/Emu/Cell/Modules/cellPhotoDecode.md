# cellPhotoDecode.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPhotoDecode.cpp`
- **类型**: 源文件
- **行数**: 181 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPhotoDecodeReturnParam`
- `CellPhotoDecodeSetParam`

### HLE 函数

- `cellPhotoDecodeFinalize()`
- `cellPhotoDecodeFromFile()`
- `cellPhotoDecodeInitialize()`
- `cellPhotoDecodeInitialize2()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/VFS.h"
#include "Emu/System.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellPhotoDecode);

// Return Codes
enum CellPhotoDecodeError : u32
{
	CELL_PHOTO_DECODE_ERROR_BUSY         = 0x8002c901,
	CELL_PHOTO_DECODE_ERROR_INTERNAL     = 0x8002c902,
	CELL_PHOTO_DECODE_ERROR_PARAM        = 0x8002c903,
	CELL_PHOTO_DECODE_ERROR_ACCESS_ERROR = 0x8002c904,
	CELL_PHOTO_DECODE_ERROR_INITIALIZE   = 0x8002c905,
	CELL_PHOTO_DECODE_ERROR_DECODE       = 0x8002c906,
};

template<>
void fmt_class_string<CellPhotoDecodeError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_PHOTO_DECODE_ERROR_BUSY);
			STR_CASE(CELL_PHOTO_DECODE_ERROR_INTERNAL);
			STR_CASE(CELL_PHOTO_DECODE_ERROR_PARAM);
			STR_CASE(CELL_PHOTO_DECODE_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_PHOTO_DECODE_ERROR_INITIALIZE);
			STR_CASE(CELL_PHOTO_DECODE_ERROR_DECODE);
		}

		return unknown;
	});
}

enum
{
	CELL_PHOTO_DECODE_VERSION_CURRENT = 0
};

struct CellPhotoDecodeSetParam
{
	vm::bptr<void> dstBuffer;
	be_t<u16> width;
	be_t<u16> height;
	vm::bptr<void> reserved1;
	vm::bptr<void> reserved2;
};

struct CellPhotoDecodeReturnParam
{
	be_t<u16> width;
	be_t<u16> height;
	vm::bptr<void> reserved1;
	vm::bptr<void> reserved2;
};

using CellPhotoDecodeFinishCallback = void(s32 result, vm::ptr<void> userdata);

error_code cellPhotoDecodeInitialize(u32 version, u32 container1, u32 container2, vm::ptr<CellPhotoDecodeFinishCallback> funcFinish, vm::ptr<void> userdata)
{
	cellPhotoDecode.warning("cellPhotoDecodeInitialize(version=0x%x, container1=0x%x, container2=0x%x, funcFinish=*0x%x, userdata=*0x%x)", version, container1, container2, funcFinish, userdata);

	if (version != CELL_PHOTO_DECODE_VERSION_CURRENT || !funcFinish)
	{
		return CELL_PHOTO_DECODE_ERROR_PARAM;
	}

	if (container1 != 0xffffffff && false) // TODO: size < 0x300000
	{
		return CELL_PHOTO_DECODE_ERROR_PARAM;
	}

	if (container2 != 0xffffffff && false) // TODO: size depends on image type, width and height
	{
		return CELL_PHOTO_DECODE_ERROR_PARAM;
	}
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/VFS.h"`
- `#include "Emu/System.h"`
- `#include "cellSysutil.h"`
