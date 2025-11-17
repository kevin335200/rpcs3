# cellUsbpspcm.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellUsbpspcm.cpp`
- **类型**: 源文件
- **行数**: 239 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### HLE 函数

- `cellUsbPspcmBindAsync()`
- `cellUsbPspcmCancelWaitData()`
- `cellUsbPspcmClose()`
- `cellUsbPspcmGetAddr()`
- `cellUsbPspcmPollBindAsync()`
- `cellUsbPspcmPollData()`
- `cellUsbPspcmPollRecvAsync()`
- `cellUsbPspcmPollResetAsync()`
- `cellUsbPspcmRecv()`
- `cellUsbPspcmRecvAsync()`
- `cellUsbPspcmRegister()`
- `cellUsbPspcmReset()`
- `cellUsbPspcmResetAsync()`
- `cellUsbPspcmSend()`
- `cellUsbPspcmSendAsync()`
- `cellUsbPspcmUnregister()`
- `cellUsbPspcmWaitBindAsync()`
- `cellUsbPspcmWaitRecvAsync()`
- `cellUsbPspcmWaitResetAsync()`
- `cellUsbPspcmWaitSendAsync()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

LOG_CHANNEL(cellUsbPspcm);

// Return Codes
enum CellUsbpspcmError : u32
{
	CELL_USBPSPCM_ERROR_NOT_INITIALIZED = 0x80110401,
	CELL_USBPSPCM_ERROR_ALREADY         = 0x80110402,
	CELL_USBPSPCM_ERROR_INVALID         = 0x80110403,
	CELL_USBPSPCM_ERROR_NO_MEMORY       = 0x80110404,
	CELL_USBPSPCM_ERROR_BUSY            = 0x80110405,
	CELL_USBPSPCM_ERROR_INPROGRESS      = 0x80110406,
	CELL_USBPSPCM_ERROR_NO_SPACE        = 0x80110407,
	CELL_USBPSPCM_ERROR_CANCELED        = 0x80110408,
	CELL_USBPSPCM_ERROR_RESETTING       = 0x80110409,
	CELL_USBPSPCM_ERROR_RESET_END       = 0x8011040A,
	CELL_USBPSPCM_ERROR_CLOSED          = 0x8011040B,
	CELL_USBPSPCM_ERROR_NO_DATA         = 0x8011040C,
};

template<>
void fmt_class_string<CellUsbpspcmError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_USBPSPCM_ERROR_NOT_INITIALIZED);
			STR_CASE(CELL_USBPSPCM_ERROR_ALREADY);
			STR_CASE(CELL_USBPSPCM_ERROR_INVALID);
			STR_CASE(CELL_USBPSPCM_ERROR_NO_MEMORY);
			STR_CASE(CELL_USBPSPCM_ERROR_BUSY);
			STR_CASE(CELL_USBPSPCM_ERROR_INPROGRESS);
			STR_CASE(CELL_USBPSPCM_ERROR_NO_SPACE);
			STR_CASE(CELL_USBPSPCM_ERROR_CANCELED);
			STR_CASE(CELL_USBPSPCM_ERROR_RESETTING);
			STR_CASE(CELL_USBPSPCM_ERROR_RESET_END);
			STR_CASE(CELL_USBPSPCM_ERROR_CLOSED);
			STR_CASE(CELL_USBPSPCM_ERROR_NO_DATA);
		}

		return unknown;
	});
}

error_code cellUsbPspcmInit()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
	return CELL_OK;
}

error_code cellUsbPspcmEnd()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
	return CELL_OK;
}

error_code cellUsbPspcmCalcPoolSize()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
	return CELL_OK;
}

error_code cellUsbPspcmRegister()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
	return CELL_OK;
}

error_code cellUsbPspcmUnregister()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
	return CELL_OK;
}

error_code cellUsbPspcmGetAddr()
{
	UNIMPLEMENTED_FUNC(cellUsbPspcm);
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
