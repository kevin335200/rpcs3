# cellPhotoImport.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPhotoImport.cpp`
- **类型**: 源文件
- **行数**: 342 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPhotoImportFileData`
- `CellPhotoImportFileDataSub`
- `CellPhotoImportSetParam`
- `photo_import`

### HLE 函数

- `cellPhotoImport()`
- `cellPhotoImport2()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/Cell/lv2/sys_fs.h"
#include "Emu/RSX/Overlays/overlay_media_list_dialog.h"
#include "Emu/VFS.h"
#include "Emu/System.h"
#include "Utilities/StrUtil.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellPhotoImportUtil, "cellPhotoImport");

// Return Codes
enum CellPhotoImportError : u32
{
	CELL_PHOTO_IMPORT_ERROR_BUSY         = 0x8002c701,
	CELL_PHOTO_IMPORT_ERROR_INTERNAL     = 0x8002c702,
	CELL_PHOTO_IMPORT_ERROR_PARAM        = 0x8002c703,
	CELL_PHOTO_IMPORT_ERROR_ACCESS_ERROR = 0x8002c704,
	CELL_PHOTO_IMPORT_ERROR_COPY         = 0x8002c705,
	CELL_PHOTO_IMPORT_ERROR_INITIALIZE   = 0x8002c706,
};

template<>
void fmt_class_string<CellPhotoImportError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_BUSY);
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_INTERNAL);
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_PARAM);
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_COPY);
			STR_CASE(CELL_PHOTO_IMPORT_ERROR_INITIALIZE);
		}

		return unknown;
	});
}

enum CellPhotoImportVersion : u32
{
	CELL_PHOTO_IMPORT_VERSION_CURRENT = 0,
};

enum
{
	CELL_PHOTO_IMPORT_HDD_PATH_MAX           = 1055,
	CELL_PHOTO_IMPORT_PHOTO_TITLE_MAX_LENGTH = 64,
	CELL_PHOTO_IMPORT_GAME_TITLE_MAX_SIZE    = 128,
	CELL_PHOTO_IMPORT_GAME_COMMENT_MAX_SIZE  = 1024
};

enum CellPhotoImportFormatType
{
	CELL_PHOTO_IMPORT_FT_UNKNOWN = 0,
	CELL_PHOTO_IMPORT_FT_JPEG,
	CELL_PHOTO_IMPORT_FT_PNG,
	CELL_PHOTO_IMPORT_FT_GIF,
	CELL_PHOTO_IMPORT_FT_BMP,
	CELL_PHOTO_IMPORT_FT_TIFF,
	CELL_PHOTO_IMPORT_FT_MPO,
};

enum CellPhotoImportTexRot
{
	CELL_PHOTO_IMPORT_TEX_ROT_0 = 0,
	CELL_PHOTO_IMPORT_TEX_ROT_90,
	CELL_PHOTO_IMPORT_TEX_ROT_180,
	CELL_PHOTO_IMPORT_TEX_ROT_270,
};

struct CellPhotoImportFileDataSub
{
	be_t<s32> width;
	be_t<s32> height;
	be_t<CellPhotoImportFormatType> format;
	be_t<CellPhotoImportTexRot> rotate;
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/Cell/lv2/sys_fs.h"`
- `#include "Emu/RSX/Overlays/overlay_media_list_dialog.h"`
- `#include "Emu/VFS.h"`
- `#include "Emu/System.h"`
- `#include "Utilities/StrUtil.h"`
- `#include "cellSysutil.h"`
