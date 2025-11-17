# cellSaveData.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSaveData.h`
- **类型**: 头文件
- **行数**: 365 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellSaveDataFileStat`
- `CellSaveDataListGet`
- `CellSaveDataListNewData`
- `CellSaveDataListSet`
- `CellSaveDataNewDataIcon`
- `CellSaveDataSetBuf`
- `CellSaveDataSetList`
- `CellSaveDataSystemFileParam`
- `SaveDataEntry`
- `SaveDialogBase`

### 关键函数

- `ShowSaveDataList()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"
#include "Emu/Memory/vm_ptr.h"
#include <string>
#include <vector>

// Return codes
enum CellSaveDataError : u32
{
	CELL_SAVEDATA_ERROR_CBRESULT        = 0x8002b401,
	CELL_SAVEDATA_ERROR_ACCESS_ERROR    = 0x8002b402,
	CELL_SAVEDATA_ERROR_INTERNAL        = 0x8002b403,
	CELL_SAVEDATA_ERROR_PARAM           = 0x8002b404,
	CELL_SAVEDATA_ERROR_NOSPACE         = 0x8002b405,
	CELL_SAVEDATA_ERROR_BROKEN          = 0x8002b406,
	CELL_SAVEDATA_ERROR_FAILURE         = 0x8002b407,
	CELL_SAVEDATA_ERROR_BUSY            = 0x8002b408,
	CELL_SAVEDATA_ERROR_NOUSER          = 0x8002b409,
	CELL_SAVEDATA_ERROR_SIZEOVER        = 0x8002b40a,
	CELL_SAVEDATA_ERROR_NODATA          = 0x8002b40b,
	CELL_SAVEDATA_ERROR_NOTSUPPORTED    = 0x8002b40c,
};

// Callback return codes
enum
{
	CELL_SAVEDATA_CBRESULT_OK_LAST_NOCONFIRM  =  2,
	CELL_SAVEDATA_CBRESULT_OK_LAST            =  1,
	CELL_SAVEDATA_CBRESULT_OK_NEXT            =  0,
	CELL_SAVEDATA_CBRESULT_ERR_NOSPACE        = -1,
	CELL_SAVEDATA_CBRESULT_ERR_FAILURE        = -2,
	CELL_SAVEDATA_CBRESULT_ERR_BROKEN         = -3,
	CELL_SAVEDATA_CBRESULT_ERR_NODATA         = -4,
	CELL_SAVEDATA_CBRESULT_ERR_INVALID        = -5,
};

// Bind stat return codes
enum
{
	CELL_SAVEDATA_BINDSTAT_OK             = 0,
	CELL_SAVEDATA_BINDSTAT_ERR_CONSOLE    = 1 << 0,
	CELL_SAVEDATA_BINDSTAT_ERR_DISC       = 1 << 1,
	CELL_SAVEDATA_BINDSTAT_ERR_PROGRAM    = 1 << 2,
	CELL_SAVEDATA_BINDSTAT_ERR_NOACCOUNTI = 1 << 3,
	CELL_SAVEDATA_BINDSTAT_ERR_NOUSER     = 1 << 3,
	CELL_SAVEDATA_BINDSTAT_ERR_ACCOUNTID  = 1 << 4,
	CELL_SAVEDATA_BINDSTAT_ERR_OTHERS     = 1 << 4,
	CELL_SAVEDATA_BINDSTAT_ERR_NOUSERID   = 1 << 5,
	CELL_SAVEDATA_BINDSTAT_ERR_USERID     = 1 << 6,
	CELL_SAVEDATA_BINDSTAT_ERR_NOOWNER    = 1 << 8,
	CELL_SAVEDATA_BINDSTAT_ERR_OWNER      = 1 << 9,
	CELL_SAVEDATA_BINDSTAT_ERR_LOCALOWNER = 1 << 10,
};

// Constants
enum
{
	// CellSaveDataParamSize
	CELL_SAVEDATA_DIRNAME_SIZE          = 32,
	CELL_SAVEDATA_FILENAME_SIZE         = 13,
	CELL_SAVEDATA_SECUREFILEID_SIZE     = 16,
	CELL_SAVEDATA_PREFIX_SIZE           = 256,
	CELL_SAVEDATA_LISTITEM_MAX          = 2048,
	CELL_SAVEDATA_SECUREFILE_MAX        = 113,
	CELL_SAVEDATA_DIRLIST_MAX           = 2048,
	CELL_SAVEDATA_INVALIDMSG_MAX        = 256,
	CELL_SAVEDATA_INDICATORMSG_MAX      = 64,

	// CellSaveDataSystemParamSize
	CELL_SAVEDATA_SYSP_TITLE_SIZE       = 128,
	CELL_SAVEDATA_SYSP_SUBTITLE_SIZE    = 128,
	CELL_SAVEDATA_SYSP_DETAIL_SIZE      = 1024,
	CELL_SAVEDATA_SYSP_LPARAM_SIZE      = 8,

	// CellSaveDataSortType
	CELL_SAVEDATA_SORTTYPE_MODIFIEDTIME = 0,
	CELL_SAVEDATA_SORTTYPE_SUBTITLE     = 1,

	// CellSaveDataSortOrder
```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include <string>`
- `#include <vector>`
