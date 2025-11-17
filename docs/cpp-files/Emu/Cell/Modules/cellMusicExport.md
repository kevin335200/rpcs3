# cellMusicExport.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellMusicExport.cpp`
- **类型**: 源文件
- **行数**: 311 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellMusicExportSetParam`
- `music_export`

### HLE 函数

- `cellMusicExportFinalize()`
- `cellMusicExportFromFile()`
- `cellMusicExportInitialize()`
- `cellMusicExportInitialize2()`
- `cellMusicExportProgress()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/VFS.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellMusicExport);

// Return Codes
enum CellMusicExportError : u32
{
	CELL_MUSIC_EXPORT_UTIL_ERROR_BUSY         = 0x8002c601,
	CELL_MUSIC_EXPORT_UTIL_ERROR_INTERNAL     = 0x8002c602,
	CELL_MUSIC_EXPORT_UTIL_ERROR_PARAM        = 0x8002c603,
	CELL_MUSIC_EXPORT_UTIL_ERROR_ACCESS_ERROR = 0x8002c604,
	CELL_MUSIC_EXPORT_UTIL_ERROR_DB_INTERNAL  = 0x8002c605,
	CELL_MUSIC_EXPORT_UTIL_ERROR_DB_REGIST    = 0x8002c606,
	CELL_MUSIC_EXPORT_UTIL_ERROR_SET_META     = 0x8002c607,
	CELL_MUSIC_EXPORT_UTIL_ERROR_FLUSH_META   = 0x8002c608,
	CELL_MUSIC_EXPORT_UTIL_ERROR_MOVE         = 0x8002c609,
	CELL_MUSIC_EXPORT_UTIL_ERROR_INITIALIZE   = 0x8002c60a,
};

template<>
void fmt_class_string<CellMusicExportError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_BUSY);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_INTERNAL);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_PARAM);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_DB_INTERNAL);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_DB_REGIST);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_SET_META);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_FLUSH_META);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_MOVE);
			STR_CASE(CELL_MUSIC_EXPORT_UTIL_ERROR_INITIALIZE);
		}

		return unknown;
	});
}

enum
{
	CELL_MUSIC_EXPORT_UTIL_VERSION_CURRENT        = 0,
	CELL_MUSIC_EXPORT_UTIL_HDD_PATH_MAX           = 1055,
	CELL_MUSIC_EXPORT_UTIL_MUSIC_TITLE_MAX_LENGTH = 64,
	CELL_MUSIC_EXPORT_UTIL_GAME_TITLE_MAX_LENGTH  = 64,
	CELL_MUSIC_EXPORT_UTIL_GAME_COMMENT_MAX_SIZE  = 1024,
};

struct CellMusicExportSetParam
{
	vm::bptr<char> title;
	vm::bptr<char> game_title;
	vm::bptr<char> artist;
	vm::bptr<char> genre;
	vm::bptr<char> game_comment;
	vm::bptr<char> reserved1;
	vm::bptr<void> reserved2;
};

using CellMusicExportUtilFinishCallback = void(s32 result, vm::ptr<void> userdata);

struct music_export
{
	atomic_t<s32> progress = 0; // 0x0-0xFFFF for 0-100%
};


bool check_music_path(const std::string& file_path)
{
	if (file_path.size() >= CELL_MUSIC_EXPORT_UTIL_HDD_PATH_MAX)
	{
		return false;
	}
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/VFS.h"`
- `#include "cellSysutil.h"`
