# cellGame.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellGame.h`
- **类型**: 头文件
- **行数**: 353 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellDiscGameSystemFileParam`
- `CellGameContentSize`
- `CellGameDataCBResult`
- `CellGameDataStatGet`
- `CellGameDataStatSet`
- `CellGameDataSystemFileParam`
- `CellGameSetInitParams`
- `disc_change_manager`

### 关键函数

- `eject_disc()`
- `insert_disc()`
- `register_callbacks()`
- `s32()`
- `unregister_callbacks()`
- `void()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

// Return Codes
enum
{
	CELL_GAME_RET_OK                   = 0,
	CELL_GAME_RET_CANCEL               = 1,
	CELL_GAME_RET_NONE                 = 2,
};

enum CellGameError : u32
{
	CELL_GAME_ERROR_NOTFOUND           = 0x8002cb04,
	CELL_GAME_ERROR_BROKEN             = 0x8002cb05,
	CELL_GAME_ERROR_INTERNAL           = 0x8002cb06,
	CELL_GAME_ERROR_PARAM              = 0x8002cb07,
	CELL_GAME_ERROR_NOAPP              = 0x8002cb08,
	CELL_GAME_ERROR_ACCESS_ERROR       = 0x8002cb09,
	CELL_GAME_ERROR_NOSPACE            = 0x8002cb20,
	CELL_GAME_ERROR_NOTSUPPORTED       = 0x8002cb21,
	CELL_GAME_ERROR_FAILURE            = 0x8002cb22,
	CELL_GAME_ERROR_BUSY               = 0x8002cb23,
	CELL_GAME_ERROR_IN_SHUTDOWN        = 0x8002cb24,
	CELL_GAME_ERROR_INVALID_ID         = 0x8002cb25,
	CELL_GAME_ERROR_EXIST              = 0x8002cb26,
	CELL_GAME_ERROR_NOTPATCH           = 0x8002cb27,
	CELL_GAME_ERROR_INVALID_THEME_FILE = 0x8002cb28,
	CELL_GAME_ERROR_BOOTPATH           = 0x8002cb50,
};

enum CellGameDataError : u32
{
	CELL_GAMEDATA_ERROR_CBRESULT     = 0x8002b601,
	CELL_GAMEDATA_ERROR_ACCESS_ERROR = 0x8002b602,
	CELL_GAMEDATA_ERROR_INTERNAL     = 0x8002b603,
	CELL_GAMEDATA_ERROR_PARAM        = 0x8002b604,
	CELL_GAMEDATA_ERROR_NOSPACE      = 0x8002b605,
	CELL_GAMEDATA_ERROR_BROKEN       = 0x8002b606,
	CELL_GAMEDATA_ERROR_FAILURE      = 0x8002b607,
};

enum CellDiscGameError : u32
{
	CELL_DISCGAME_ERROR_INTERNAL      = 0x8002bd01,
	CELL_DISCGAME_ERROR_NOT_DISCBOOT  = 0x8002bd02,
	CELL_DISCGAME_ERROR_PARAM         = 0x8002bd03,
};

// Definitions
enum
{
	CELL_GAME_PATH_MAX           = 128,
	CELL_GAME_DIRNAME_SIZE       = 32,
	CELL_GAME_HDDGAMEPATH_SIZE   = 128,
	CELL_GAME_THEMEFILENAME_SIZE = 48,

	CELL_GAME_SYSP_LANGUAGE_NUM  = 20,
	CELL_GAME_SYSP_TITLE_SIZE    = 128,
	CELL_GAME_SYSP_TITLEID_SIZE  = 10,
	CELL_GAME_SYSP_VERSION_SIZE  = 6,
	CELL_GAME_SYSP_PS3_SYSTEM_VER_SIZE = 8,
	CELL_GAME_SYSP_APP_VER_SIZE  = 6,

	CELL_GAME_GAMETYPE_SYS      = 0,
	CELL_GAME_GAMETYPE_DISC     = 1,
	CELL_GAME_GAMETYPE_HDD      = 2,
	CELL_GAME_GAMETYPE_GAMEDATA = 3,
	CELL_GAME_GAMETYPE_HOME     = 4,

	CELL_GAME_SIZEKB_NOTCALC = -1,

	CELL_GAME_THEMEINSTALL_BUFSIZE_MIN = 4096,

	CELL_GAME_ATTRIBUTE_PATCH               = 0x1,
	CELL_GAME_ATTRIBUTE_APP_HOME            = 0x2,
	CELL_GAME_ATTRIBUTE_DEBUG               = 0x4,
	CELL_GAME_ATTRIBUTE_XMBBUY              = 0x8,
	CELL_GAME_ATTRIBUTE_COMMERCE2_BROWSER   = 0x10,
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
