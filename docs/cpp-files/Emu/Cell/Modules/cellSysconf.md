# cellSysconf.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSysconf.h`
- **类型**: 头文件
- **行数**: 36 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellSysconfBtDeviceInfo`
- `CellSysconfBtDeviceList`

### 关键函数

- `void()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

typedef void(CellSysconfCallback)(s32 result, vm::ptr<void> userdata);

struct CellSysconfBtDeviceInfo
{
	be_t<u64> deviceId;
	be_t<s32> deviceType; // CellSysconfBtDeviceType
	be_t<s32> state;      // CellSysconfBtDeviceState
	char name[64];
	be_t<u32> reserved[4];
};

struct CellSysconfBtDeviceList
{
	CellSysconfBtDeviceInfo device[16];
};

enum CellSysconfBtDeviceType : s32
{
	CELL_SYSCONF_BT_DEVICE_TYPE_AUDIO = 0x00000001,
	CELL_SYSCONF_BT_DEVICE_TYPE_HID   = 0x00000002,
};

enum CellSysconfBtDeviceState : s32
{
	CELL_SYSCONF_BT_DEVICE_STATE_UNAVAILABLE = 0,
	CELL_SYSCONF_BT_DEVICE_STATE_AVAILABLE   = 1,
};

enum CellSysConfError : u32
{
	CELL_SYSCONF_ERROR_PARAM = 0x8002bb01
};

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
