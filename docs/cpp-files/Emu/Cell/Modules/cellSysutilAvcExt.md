# cellSysutilAvcExt.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSysutilAvcExt.cpp`
- **类型**: 源文件
- **行数**: 320 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### HLE 函数

- `cellSysutilAvcExtGetNamePlateShowStatus()`
- `cellSysutilAvcExtGetSurfacePointer()`
- `cellSysutilAvcExtGetWindowPosition()`
- `cellSysutilAvcExtHideWindow()`
- `cellSysutilAvcExtInitOptionParam()`
- `cellSysutilAvcExtIsCameraAttached()`
- `cellSysutilAvcExtLoadAsyncEx()`
- `cellSysutilAvcExtSetChatGroup()`
- `cellSysutilAvcExtSetHideNamePlate()`
- `cellSysutilAvcExtSetWindowPosition()`
- `cellSysutilAvcExtSetWindowRotation()`
- `cellSysutilAvcExtSetWindowSize()`
- `cellSysutilAvcExtSetWindowZorder()`
- `cellSysutilAvcExtShowPanelEx()`
- `cellSysutilAvcExtShowWindow()`
- `cellSysutilAvcExtStartMicDetection()`
- `cellSysutilAvcExtStopCameraDetection()`
- `cellSysutilAvcExtStopMicDetection()`
- `cellSysutilAvcLoadAsync()`
- `cellSysutilAvcSetAttribute()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/Cell/Modules/cellSysutilAvc.h"

LOG_CHANNEL(cellSysutilAvcExt);

error_code cellSysutilAvcSetAttribute(CellSysUtilAvcAttribute attr_id, vm::ptr<void> param);
error_code cellSysutilAvcLoadAsync(vm::ptr<CellSysutilAvcCallback> func, vm::ptr<void> userdata, sys_memory_container_t container, CellSysUtilAvcMediaType media, CellSysUtilAvcVideoQuality videoQuality, CellSysUtilAvcVoiceQuality voiceQuality, vm::ptr<CellSysutilAvcRequestId> request_id);

error_code cellSysutilAvcExtIsMicAttached(vm::ptr<s32> status)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtIsMicAttached(status=*0x%x)", status);

	ensure(!!status); // Not actually checked

	return CELL_OK;
}

error_code cellSysutilAvcExtStopCameraDetection()
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtStopCameraDetection()");
	return CELL_OK;
}

error_code cellSysutilAvcExtSetWindowRotation(vm::ptr<SceNpId> player_id, f32 rotation_x, f32 rotation_y, f32 rotation_z, CellSysutilAvcTransitionType transition_type)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtSetWindowRotation(player_id=*0x%x, rotation_x=%f, rotation_y=%f, rotation_z=%f, transition_type=0x%x)", player_id, rotation_x, rotation_y, rotation_z, +transition_type);
	return CELL_OK;
}

error_code cellSysutilAvcExtGetWindowPosition(vm::ptr<SceNpId> player_id, vm::ptr<f32> position_x, vm::ptr<f32> position_y, vm::ptr<f32> position_z)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtGetWindowPosition(player_id=*0x%x, position_x=*0x%x, position_y=*0x%x, position_z=*0x%x)", player_id, position_x, position_y, position_z);

	if (!player_id || !position_x || !position_y || !position_z)
		return CELL_AVC_ERROR_INVALID_ARGUMENT;

	return CELL_OK;
}

error_code cellSysutilAvcExtSetHideNamePlate()
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtSetHideNamePlate()");
	return CELL_OK;
}

error_code cellSysutilAvcExtSetWindowPosition(vm::ptr<SceNpId> player_id, f32 position_x, f32 position_y, f32 position_z, CellSysutilAvcTransitionType transition_type)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtSetWindowPosition(player_id=*0x%x, position_x=%f, position_y=%f, position_z=%f, transition_type=0x%x)", player_id, position_x, position_y, position_z, +transition_type);
	return CELL_OK;
}

error_code cellSysutilAvcExtGetWindowSize(vm::ptr<SceNpId> player_id, vm::ptr<f32> size_x, vm::ptr<f32> size_y)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtGetWindowSize(player_id=*0x%x, size_x=*0x%x, size_y=*0x%x)", player_id, size_x, size_y);

	if (!player_id || !size_x || !size_y)
		return CELL_AVC_ERROR_INVALID_ARGUMENT;

	return CELL_OK;
}

error_code cellSysutilAvcExtStartCameraDetection()
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtStartCameraDetection()");
	return CELL_OK;
}

error_code cellSysutilAvcExtGetWindowShowStatus(vm::ptr<SceNpId> player_id, vm::ptr<b8> is_visible)
{
	cellSysutilAvcExt.todo("cellSysutilAvcExtGetWindowShowStatus(player_id=*0x%x, is_visible=*0x%x)", player_id, is_visible);

	if (!player_id || !is_visible)
		return CELL_AVC_ERROR_INVALID_ARGUMENT;

	return CELL_OK;
}

error_code cellSysutilAvcExtSetChatMode(u32 mode)
{
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/Modules/cellSysutilAvc.h"`
