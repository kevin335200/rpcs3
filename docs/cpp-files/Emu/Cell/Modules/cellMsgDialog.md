# cellMsgDialog.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellMsgDialog.h`
- **类型**: 头文件
- **行数**: 136 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `MsgDialogBase`

### 关键函数

- `Close()`
- `Create()`
- `ProgressBarInc()`
- `ProgressBarReset()`
- `ProgressBarSetLimit()`
- `ProgressBarSetMsg()`
- `ProgressBarSetTaskbarIndex()`
- `ProgressBarSetValue()`
- `SetMsg()`
- `close_msg_dialog()`
- `open_exit_dialog()`
- `open_msg_dialog()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"
#include "util/atomic.hpp"
#include "Utilities/BitField.h"
#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

#include <string>
#include <functional>

enum
{
	CELL_MSGDIALOG_PROGRESSBAR_STRING_SIZE = 64,
	CELL_MSGDIALOG_STRING_SIZE             = 512,
};

enum CellMsgDialogError : u32
{
	CELL_MSGDIALOG_ERROR_PARAM             = 0x8002b301,
	CELL_MSGDIALOG_ERROR_DIALOG_NOT_OPENED = 0x8002b302,
};

enum : u32
{
	CELL_MSGDIALOG_TYPE_SE_TYPE_ERROR       = 0 << 0,
	CELL_MSGDIALOG_TYPE_SE_TYPE_NORMAL      = 1 << 0,

	CELL_MSGDIALOG_TYPE_SE_MUTE_OFF         = 0 << 1,
	CELL_MSGDIALOG_TYPE_SE_MUTE_ON          = 1 << 1,

	CELL_MSGDIALOG_TYPE_BG_VISIBLE          = 0 << 2,
	CELL_MSGDIALOG_TYPE_BG_INVISIBLE        = 1 << 2,

	CELL_MSGDIALOG_TYPE_BUTTON_TYPE_NONE    = 0 << 4,
	CELL_MSGDIALOG_TYPE_BUTTON_TYPE_YESNO   = 1 << 4,
	CELL_MSGDIALOG_TYPE_BUTTON_TYPE_OK      = 2 << 4,

	CELL_MSGDIALOG_TYPE_DISABLE_CANCEL_OFF  = 0 << 7,
	CELL_MSGDIALOG_TYPE_DISABLE_CANCEL_ON   = 1 << 7,

	CELL_MSGDIALOG_TYPE_DEFAULT_CURSOR_NONE = 0 << 8,
	CELL_MSGDIALOG_TYPE_DEFAULT_CURSOR_YES  = 0 << 8,
	CELL_MSGDIALOG_TYPE_DEFAULT_CURSOR_NO   = 1 << 8,
	CELL_MSGDIALOG_TYPE_DEFAULT_CURSOR_OK   = 0 << 8,

	CELL_MSGDIALOG_TYPE_PROGRESSBAR_NONE    = 0 << 12,
	CELL_MSGDIALOG_TYPE_PROGRESSBAR_SINGLE  = 1 << 12,
	CELL_MSGDIALOG_TYPE_PROGRESSBAR_DOUBLE  = 2 << 12,
};

// MsgDialog Button Type
enum : s32
{
	CELL_MSGDIALOG_BUTTON_NONE    = -1,
	CELL_MSGDIALOG_BUTTON_INVALID = 0,
	CELL_MSGDIALOG_BUTTON_OK      = 1,
	CELL_MSGDIALOG_BUTTON_YES     = 1,
	CELL_MSGDIALOG_BUTTON_NO      = 2,
	CELL_MSGDIALOG_BUTTON_ESCAPE  = 3,
};

enum CellMsgDialogProgressBarIndex
{
	CELL_MSGDIALOG_PROGRESSBAR_INDEX_SINGLE       = 0, // the only bar in a single bar dialog
	CELL_MSGDIALOG_PROGRESSBAR_INDEX_DOUBLE_UPPER = 0, // the upper bar in a double bar dialog
	CELL_MSGDIALOG_PROGRESSBAR_INDEX_DOUBLE_LOWER = 1, // the lower bar in a double bar dialog
};

using CellMsgDialogCallback = void(s32 buttonType, vm::ptr<void> userData);

union MsgDialogType
{
	u32 value;

	bf_t<u32, 0, 1> se_normal;
	bf_t<u32, 1, 1> se_mute_on;
	bf_t<u32, 2, 1> bg_invisible;
	bf_t<u32, 4, 3> button_type;
	bf_t<u32, 7, 1> disable_cancel;
```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
- `#include "util/atomic.hpp"`
- `#include "Utilities/BitField.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include <string>`
- `#include <functional>`
