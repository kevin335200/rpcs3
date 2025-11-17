# cellGameExec.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellGameExec.cpp`
- **类型**: 源文件
- **行数**: 148 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `game_exec_data`

### HLE 函数

- `cellGameDeleteGame()`
- `cellGameExecGame()`
- `cellGameGetBootGameInfo()`
- `cellGameGetExitGameInfo()`
- `cellGameGetHomeDataExportPath()`
- `cellGameGetHomeDataImportPath()`
- `cellGameGetHomeLaunchOptionPath()`
- `cellGameGetHomePath()`
- `cellGameGetList()`
- `cellGameSetExitParam()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/IdManager.h"
#include "Emu/System.h"

#include "cellGame.h"

LOG_CHANNEL(cellGameExec);

struct game_exec_data
{
	atomic_t<u32> execdata = 0; // TODO: pass this to the source application after closing the current application
};

error_code cellGameSetExitParam(u32 execdata)
{
	cellGameExec.todo("cellGameSetExitParam(execdata=0x%x)", execdata);

	g_fxo->get<game_exec_data>().execdata = execdata;

	return CELL_OK;
}

error_code cellGameGetHomeDataExportPath(vm::ptr<char> exportPath)
{
	cellGameExec.warning("cellGameGetHomeDataExportPath(exportPath=*0x%x)", exportPath);

	if (!exportPath)
	{
		return CELL_GAME_ERROR_PARAM;
	}

	// TODO: PlayStation home is defunct.

	return CELL_GAME_ERROR_NOAPP;
}

error_code cellGameGetHomePath(vm::ptr<char> homePath)
{
	cellGameExec.todo("cellGameGetHomePath(homePath=*0x%x)", homePath);

	if (!homePath)
	{
		return CELL_GAME_ERROR_PARAM;
	}

	// TODO: PlayStation home is defunct.

	return CELL_OK;
}

error_code cellGameGetHomeDataImportPath(vm::ptr<char> importPath)
{
	cellGameExec.warning("cellGameGetHomeDataImportPath(importPath=*0x%x)", importPath);

	if (!importPath)
	{
		return CELL_GAME_ERROR_PARAM;
	}

	// TODO: PlayStation home is defunct.

	return CELL_GAME_ERROR_NOAPP;
}

error_code cellGameGetHomeLaunchOptionPath(vm::ptr<char> commonPath, vm::ptr<char> personalPath)
{
	cellGameExec.todo("cellGameGetHomeLaunchOptionPath(commonPath=%s, personalPath=%s)", commonPath, personalPath);

	if (!commonPath || !personalPath)
	{
		return CELL_GAME_ERROR_PARAM;
	}

	// TODO: PlayStation home is not supported atm.
	return CELL_GAME_ERROR_NOAPP;
}

error_code cellGameExecGame(u32 type, vm::ptr<char> dirName, u32 options, u32 memContainer, u32 execData, u32 userData)
{
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/System.h"`
- `#include "cellGame.h"`
