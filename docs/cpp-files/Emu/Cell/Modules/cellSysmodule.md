# cellSysmodule.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSysmodule.cpp`
- **类型**: 源文件
- **行数**: 424 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### HLE 函数

- `cellSysmoduleFetchImage()`
- `cellSysmoduleFinalize()`
- `cellSysmoduleGetImagesize()`
- `cellSysmoduleInitialize()`
- `cellSysmoduleIsLoaded()`
- `cellSysmoduleIsLoadedEx()`
- `cellSysmoduleLoadModule()`
- `cellSysmoduleLoadModuleEx()`
- `cellSysmoduleLoadModuleInternal()`
- `cellSysmoduleSetMemcontainer()`
- `cellSysmoduleUnloadModule()`
- `cellSysmoduleUnloadModuleEx()`
- `cellSysmoduleUnloadModuleInternal()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

LOG_CHANNEL(cellSysmodule);

constexpr auto CELL_SYSMODULE_LOADED = CELL_OK;

enum CellSysmoduleError : u32
{
	CELL_SYSMODULE_ERROR_DUPLICATED           = 0x80012001,
	CELL_SYSMODULE_ERROR_UNKNOWN              = 0x80012002,
	CELL_SYSMODULE_ERROR_UNLOADED             = 0x80012003,
	CELL_SYSMODULE_ERROR_INVALID_MEMCONTAINER = 0x80012004,
	CELL_SYSMODULE_ERROR_FATAL                = 0x800120ff,
};

template<>
void fmt_class_string<CellSysmoduleError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_SYSMODULE_ERROR_DUPLICATED);
			STR_CASE(CELL_SYSMODULE_ERROR_UNKNOWN);
			STR_CASE(CELL_SYSMODULE_ERROR_UNLOADED);
			STR_CASE(CELL_SYSMODULE_ERROR_INVALID_MEMCONTAINER);
			STR_CASE(CELL_SYSMODULE_ERROR_FATAL);
		}

		return unknown;
	});
}

static const char* get_module_name(u16 id)
{
	switch (id)
	{
	case 0x0000: return "sys_net";
	case 0x0001: return "cellHttp";
	case 0x0002: return "cellHttpUtil";
	case 0x0003: return "cellSsl";
	case 0x0004: return "cellHttps";
	case 0x0005: return "libvdec";
	case 0x0006: return "cellAdec";
	case 0x0007: return "cellDmux";
	case 0x0008: return "cellVpost";
	case 0x0009: return "cellRtc";
	case 0x000a: return "cellSpurs";
	case 0x000b: return "cellOvis";
	case 0x000c: return "cellSheap";
	case 0x000d: return "cellSync";
	case 0x000e: return "sys_fs";
	case 0x000f: return "cellJpgDec";
	case 0x0010: return "cellGcmSys";
	case 0x0011: return "cellAudio";
	case 0x0012: return "cellPamf";
	case 0x0013: return "cellAtrac";
	case 0x0014: return "cellNetCtl";
	case 0x0015: return "cellSysutil";
	case 0x0016: return "sceNp";
	case 0x0017: return "sys_io";
	case 0x0018: return "cellPngDec";
	case 0x0019: return "cellFont";
	case 0x001a: return "cellFontFT";
	case 0x001b: return "cell_FreeType2";
	case 0x001c: return "cellUsbd";
	case 0x001d: return "cellSail";
	case 0x001e: return "cellL10n";
	case 0x001f: return "cellResc";
	case 0x0020: return "cellDaisy";
	case 0x0021: return "cellKey2char";
	case 0x0022: return "cellMic";
	case 0x0023: return "cellCamera";
	case 0x0024: return "cellVdecMpeg2";
	case 0x0025: return "cellVdecAvc";
	case 0x0026: return "cellAdecLpcm";
	case 0x0027: return "cellAdecAc3";
	case 0x0028: return "cellAdecAtx";
	case 0x0029: return "cellAdecAt3";
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
