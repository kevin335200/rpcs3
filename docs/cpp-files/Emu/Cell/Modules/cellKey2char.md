# cellKey2char.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellKey2char.cpp`
- **类型**: 源文件
- **行数**: 193 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellKey2CharHandle`
- `CellKey2CharKeyData`

### HLE 函数

- `cellKey2CharClose()`
- `cellKey2CharGetChar()`
- `cellKey2CharOpen()`
- `cellKey2CharSetArrangement()`
- `cellKey2CharSetMode()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/Io/Keyboard.h"

LOG_CHANNEL(cellKey2char);

// Return Codes
enum CellKey2CharError : u32
{
	CELL_K2C_ERROR_FATAL               = 0x80121301,
	CELL_K2C_ERROR_INVALID_HANDLE      = 0x80121302,
	CELL_K2C_ERROR_INVALID_PARAMETER   = 0x80121303,
	CELL_K2C_ERROR_ALREADY_INITIALIZED = 0x80121304,
	CELL_K2C_ERROR_UNINITIALIZED       = 0x80121305,
	CELL_K2C_ERROR_OTHER               = 0x80121306,
};

// Modes
enum
{
	CELL_KEY2CHAR_MODE_ENGLISH = 0,
	CELL_KEY2CHAR_MODE_NATIVE  = 1,
	CELL_KEY2CHAR_MODE_NATIVE2 = 2
};

// Constants
enum
{
	SCE_KEY2CHAR_HANDLE_SIZE = 128
};

struct CellKey2CharKeyData
{
	be_t<u32> led;
	be_t<u32> mkey;
	be_t<u16> keycode;
};

struct CellKey2CharHandle
{
	u8 data[SCE_KEY2CHAR_HANDLE_SIZE];
};

template<>
void fmt_class_string<CellKey2CharError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_K2C_ERROR_FATAL);
			STR_CASE(CELL_K2C_ERROR_INVALID_HANDLE);
			STR_CASE(CELL_K2C_ERROR_INVALID_PARAMETER);
			STR_CASE(CELL_K2C_ERROR_ALREADY_INITIALIZED);
			STR_CASE(CELL_K2C_ERROR_UNINITIALIZED);
			STR_CASE(CELL_K2C_ERROR_OTHER);
		}

		return unknown;
	});
}

error_code cellKey2CharOpen(vm::ptr<CellKey2CharHandle> handle)
{
	cellKey2char.todo("cellKey2CharOpen(handle=*0x%x)", handle);

	if (!handle)
		return CELL_K2C_ERROR_INVALID_HANDLE;

	if (handle->data[8] != 0)
		return CELL_K2C_ERROR_ALREADY_INITIALIZED;

	// TODO

	return CELL_OK;
}

error_code cellKey2CharClose(vm::ptr<CellKey2CharHandle> handle)
{
	cellKey2char.todo("cellKey2CharClose(handle=*0x%x)", handle);
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Io/Keyboard.h"`
