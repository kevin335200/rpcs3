# cellRtcAlarm.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellRtcAlarm.cpp`
- **类型**: 源文件
- **行数**: 43 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### HLE 函数

- `cellRtcAlarmGetStatus()`
- `cellRtcAlarmNotification()`
- `cellRtcAlarmRegister()`
- `cellRtcAlarmStopRunning()`
- `cellRtcAlarmUnregister()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

LOG_CHANNEL(cellRtcAlarm);

error_code cellRtcAlarmRegister()
{
	UNIMPLEMENTED_FUNC(cellRtcAlarm);
	return CELL_OK;
}

error_code cellRtcAlarmUnregister()
{
	UNIMPLEMENTED_FUNC(cellRtcAlarm);
	return CELL_OK;
}

error_code cellRtcAlarmNotification()
{
	UNIMPLEMENTED_FUNC(cellRtcAlarm);
	return CELL_OK;
}

error_code cellRtcAlarmStopRunning()
{
	UNIMPLEMENTED_FUNC(cellRtcAlarm);
	return CELL_OK;
}

error_code cellRtcAlarmGetStatus()
{
	UNIMPLEMENTED_FUNC(cellRtcAlarm);
	return CELL_OK;
}

DECLARE(ppu_module_manager::cellRtcAlarm)("cellRtcAlarm", []()
{
	REG_FUNC(cellRtcAlarm, cellRtcAlarmRegister);
	REG_FUNC(cellRtcAlarm, cellRtcAlarmUnregister);
	REG_FUNC(cellRtcAlarm, cellRtcAlarmNotification);
	REG_FUNC(cellRtcAlarm, cellRtcAlarmStopRunning);
	REG_FUNC(cellRtcAlarm, cellRtcAlarmGetStatus);
});

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
