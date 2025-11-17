# cellSysutilMisc.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSysutilMisc.cpp`
- **类型**: 源文件
- **行数**: 20 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### HLE 函数

- `cellSysutilGetLicenseArea()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/system_config.h"
#include "Emu/Cell/PPUModule.h"
#include "cellSysutil.h"

LOG_CHANNEL(cellSysutilMisc);

s32 cellSysutilGetLicenseArea()
{
	cellSysutilMisc.warning("cellSysutilGetLicenseArea()");

	const CellSysutilLicenseArea license_area = g_cfg.sys.license_area;
	cellSysutilMisc.notice("cellSysutilGetLicenseArea(): %s", license_area);
	return license_area;
}

DECLARE(ppu_module_manager::cellSysutilMisc)("cellSysutilMisc", []()
{
	REG_FUNC(cellSysutilMisc, cellSysutilGetLicenseArea);
});

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "cellSysutil.h"`
