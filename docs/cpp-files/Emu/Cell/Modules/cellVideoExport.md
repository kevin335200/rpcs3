# cellVideoExport.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellVideoExport.cpp`
- **类型**: 源文件
- **行数**: 385 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellVideoExportSetParam`
- `video_export`

### HLE 函数

- `cellVideoExportFinalize()`
- `cellVideoExportFromFile()`
- `cellVideoExportFromFileWithCopy()`
- `cellVideoExportInitialize()`
- `cellVideoExportInitialize2()`
- `cellVideoExportProgress()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/VFS.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellVideoExport);

enum CellVideoExportUtilError : u32
{
	CELL_VIDEO_EXPORT_UTIL_ERROR_BUSY         = 0x8002ca01,
	CELL_VIDEO_EXPORT_UTIL_ERROR_INTERNAL     = 0x8002ca02,
	CELL_VIDEO_EXPORT_UTIL_ERROR_PARAM        = 0x8002ca03,
	CELL_VIDEO_EXPORT_UTIL_ERROR_ACCESS_ERROR = 0x8002ca04,
	CELL_VIDEO_EXPORT_UTIL_ERROR_DB_INTERNAL  = 0x8002ca05,
	CELL_VIDEO_EXPORT_UTIL_ERROR_DB_REGIST    = 0x8002ca06,
	CELL_VIDEO_EXPORT_UTIL_ERROR_SET_META     = 0x8002ca07,
	CELL_VIDEO_EXPORT_UTIL_ERROR_FLUSH_META   = 0x8002ca08,
	CELL_VIDEO_EXPORT_UTIL_ERROR_MOVE         = 0x8002ca09,
	CELL_VIDEO_EXPORT_UTIL_ERROR_INITIALIZE   = 0x8002ca0a,
};

enum
{
	CELL_VIDEO_EXPORT_UTIL_RET_OK     = 0,
	CELL_VIDEO_EXPORT_UTIL_RET_CANCEL = 1,
};

enum
{
	CELL_VIDEO_EXPORT_UTIL_VERSION_CURRENT        = 0,
	CELL_VIDEO_EXPORT_UTIL_HDD_PATH_MAX           = 1055,
	CELL_VIDEO_EXPORT_UTIL_VIDEO_TITLE_MAX_LENGTH = 64,
	CELL_VIDEO_EXPORT_UTIL_GAME_TITLE_MAX_LENGTH  = 64,
	CELL_VIDEO_EXPORT_UTIL_GAME_COMMENT_MAX_SIZE  = 1024,
};

template<>
void fmt_class_string<CellVideoExportUtilError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_BUSY);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_INTERNAL);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_PARAM);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_DB_INTERNAL);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_DB_REGIST);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_SET_META);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_FLUSH_META);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_MOVE);
			STR_CASE(CELL_VIDEO_EXPORT_UTIL_ERROR_INITIALIZE);
		}

		return unknown;
	});
}

struct CellVideoExportSetParam
{
	vm::bptr<char> title;
	vm::bptr<char> game_title;
	vm::bptr<char> game_comment;
	be_t<s32> editable;
	vm::bptr<void> reserved2;
};

using CellVideoExportUtilFinishCallback = void(s32 result, vm::ptr<void> userdata);


struct video_export
{
	atomic_t<s32> progress = 0; // 0x0-0xFFFF for 0-100%
};


bool check_movie_path(const std::string& file_path)
{
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/VFS.h"`
- `#include "cellSysutil.h"`
