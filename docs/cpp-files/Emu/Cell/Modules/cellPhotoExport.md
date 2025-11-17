# cellPhotoExport.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPhotoExport.cpp`
- **类型**: 源文件
- **行数**: 487 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPhotoExportSetParam`
- `photo_export`

### HLE 函数

- `cellPhotoExportFinalize()`
- `cellPhotoExportFromFile()`
- `cellPhotoExportFromFileWithCopy()`
- `cellPhotoExportInitialize()`
- `cellPhotoExportInitialize2()`
- `cellPhotoExportProgress()`
- `cellPhotoFinalize()`
- `cellPhotoInitialize()`
- `cellPhotoRegistFromFile()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/VFS.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellPhotoExport);

// Return Codes
enum CellPhotoExportError : u32
{
	CELL_PHOTO_EXPORT_UTIL_ERROR_BUSY         = 0x8002c201,
	CELL_PHOTO_EXPORT_UTIL_ERROR_INTERNAL     = 0x8002c202,
	CELL_PHOTO_EXPORT_UTIL_ERROR_PARAM        = 0x8002c203,
	CELL_PHOTO_EXPORT_UTIL_ERROR_ACCESS_ERROR = 0x8002c204,
	CELL_PHOTO_EXPORT_UTIL_ERROR_DB_INTERNAL  = 0x8002c205,
	CELL_PHOTO_EXPORT_UTIL_ERROR_DB_REGIST    = 0x8002c206,
	CELL_PHOTO_EXPORT_UTIL_ERROR_SET_META     = 0x8002c207,
	CELL_PHOTO_EXPORT_UTIL_ERROR_FLUSH_META   = 0x8002c208,
	CELL_PHOTO_EXPORT_UTIL_ERROR_MOVE         = 0x8002c209,
	CELL_PHOTO_EXPORT_UTIL_ERROR_INITIALIZE   = 0x8002c20a,
};

template<>
void fmt_class_string<CellPhotoExportError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_BUSY);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_INTERNAL);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_PARAM);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_DB_INTERNAL);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_DB_REGIST);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_SET_META);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_FLUSH_META);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_MOVE);
			STR_CASE(CELL_PHOTO_EXPORT_UTIL_ERROR_INITIALIZE);
		}

		return unknown;
	});
}

enum
{
	CELL_PHOTO_EXPORT_UTIL_VERSION_CURRENT = 0
};

enum
{
	CELL_PHOTO_EXPORT_UTIL_HDD_PATH_MAX           = 1055,
	CELL_PHOTO_EXPORT_UTIL_PHOTO_TITLE_MAX_LENGTH = 64,
	CELL_PHOTO_EXPORT_UTIL_GAME_TITLE_MAX_LENGTH  = 64,
	CELL_PHOTO_EXPORT_UTIL_GAME_COMMENT_MAX_SIZE  = 1024,
};

struct CellPhotoExportSetParam
{
	vm::bptr<char> photo_title;
	vm::bptr<char> game_title;
	vm::bptr<char> game_comment;
	vm::bptr<void> reserved;
};

using CellPhotoExportUtilFinishCallback = void(s32 result, vm::ptr<void> userdata);

struct photo_export
{
	atomic_t<s32> progress = 0; // 0x0-0xFFFF for 0-100%
};


bool check_photo_path(const std::string& file_path)
{
	if (file_path.size() >= CELL_PHOTO_EXPORT_UTIL_HDD_PATH_MAX)
	{
		return false;
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/VFS.h"`
- `#include "cellSysutil.h"`
