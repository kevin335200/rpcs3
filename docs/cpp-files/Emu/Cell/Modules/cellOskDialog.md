# cellOskDialog.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellOskDialog.h`
- **类型**: 头文件
- **行数**: 380 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellOskDialogCallbackReturnParam`
- `CellOskDialogImeDictionaryInfo`
- `CellOskDialogInputFieldInfo`
- `CellOskDialogKeyMessage`
- `CellOskDialogParam`
- `OskDialogBase`
- `color`
- `osk_info`
- `osk_params`
- `osk_window_layout`

### 关键函数

- `Clear()`
- `Close()`
- `Create()`
- `Insert()`
- `SetText()`
- `get_aligned_x()`
- `get_aligned_y()`
- `reset()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"
#include "util/atomic.hpp"
#include "util/init_mutex.hpp"
#include "Utilities/mutex.h"
#include "Emu/Memory/vm_ptr.h"
#include <string>
#include <functional>

// error codes
enum CellOskDialogError : u32
{
	CELL_OSKDIALOG_ERROR_IME_ALREADY_IN_USE = 0x8002b501,
	CELL_OSKDIALOG_ERROR_GET_SIZE_ERROR     = 0x8002b502,
	CELL_OSKDIALOG_ERROR_UNKNOWN            = 0x8002b503,
	CELL_OSKDIALOG_ERROR_PARAM              = 0x8002b504,
};

// OSK status for the callback
enum
{
	CELL_SYSUTIL_OSKDIALOG_LOADED               = 0x0502,
	CELL_SYSUTIL_OSKDIALOG_FINISHED             = 0x0503,
	CELL_SYSUTIL_OSKDIALOG_UNLOADED             = 0x0504,
	CELL_SYSUTIL_OSKDIALOG_INPUT_ENTERED        = 0x0505,
	CELL_SYSUTIL_OSKDIALOG_INPUT_CANCELED       = 0x0506,
	CELL_SYSUTIL_OSKDIALOG_INPUT_DEVICE_CHANGED = 0x0507,
	CELL_SYSUTIL_OSKDIALOG_DISPLAY_CHANGED      = 0x0508,
};

enum CellOskDialogInputFieldResult
{
	CELL_OSKDIALOG_INPUT_FIELD_RESULT_OK = 0,
	CELL_OSKDIALOG_INPUT_FIELD_RESULT_CANCELED = 1,
	CELL_OSKDIALOG_INPUT_FIELD_RESULT_ABORT = 2,
	CELL_OSKDIALOG_INPUT_FIELD_RESULT_NO_INPUT_TEXT = 3,
};

enum CellOskDialogInitialKeyLayout
{
	CELL_OSKDIALOG_INITIAL_PANEL_LAYOUT_SYSTEM = 0,
	CELL_OSKDIALOG_INITIAL_PANEL_LAYOUT_10KEY = 1,
	CELL_OSKDIALOG_INITIAL_PANEL_LAYOUT_FULLKEY = 2,
};

enum CellOskDialogInputDevice
{
	CELL_OSKDIALOG_INPUT_DEVICE_PAD = 0,
	CELL_OSKDIALOG_INPUT_DEVICE_KEYBOARD = 1,
};

enum CellOskDialogContinuousMode
{
	CELL_OSKDIALOG_CONTINUOUS_MODE_NONE = 0,
	CELL_OSKDIALOG_CONTINUOUS_MODE_REMAIN_OPEN = 1,
	CELL_OSKDIALOG_CONTINUOUS_MODE_HIDE = 2,
	CELL_OSKDIALOG_CONTINUOUS_MODE_SHOW = 3,
};

enum CellOskDialogDisplayStatus
{
	CELL_OSKDIALOG_DISPLAY_STATUS_HIDE = 0,
	CELL_OSKDIALOG_DISPLAY_STATUS_SHOW = 1,
};

enum CellOskDialogFilterCallbackReturnValue
{
	CELL_OSKDIALOG_NOT_CHANGE = 0,
	CELL_OSKDIALOG_CHANGE_WORD = 1,
};

enum CellOskDialogActionValue
{
	CELL_OSKDIALOG_CHANGE_NO_EVENT = 0,
	CELL_OSKDIALOG_CHANGE_EVENT_CANCEL = 1,
	CELL_OSKDIALOG_CHANGE_WORDS_INPUT = 3,
	CELL_OSKDIALOG_CHANGE_WORDS_INSERT = 4,
	CELL_OSKDIALOG_CHANGE_WORDS_REPLACE_ALL = 6,
};
```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
- `#include "util/atomic.hpp"`
- `#include "util/init_mutex.hpp"`
- `#include "Utilities/mutex.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include <string>`
- `#include <functional>`
