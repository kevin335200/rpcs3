# cellPad.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPad.h`
- **类型**: 头文件
- **行数**: 144 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPadActParam`
- `CellPadCapabilityInfo`
- `CellPadFilterIIRSos`
- `CellPadInfo`
- `CellPadInfo2`
- `CellPadPeriphData`
- `CellPadPeriphInfo`
- `pad_data_internal`
- `pad_info`

### HLE 函数

- `cellPadGetData()`
- `cellPadInit()`
- `cellPadSetPortSetting()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Io/pad_types.h"

#include <array>

enum CellPadError : u32
{
	CELL_PAD_ERROR_FATAL                      = 0x80121101,
	CELL_PAD_ERROR_INVALID_PARAMETER          = 0x80121102,
	CELL_PAD_ERROR_ALREADY_INITIALIZED        = 0x80121103,
	CELL_PAD_ERROR_UNINITIALIZED              = 0x80121104,
	CELL_PAD_ERROR_RESOURCE_ALLOCATION_FAILED = 0x80121105,
	CELL_PAD_ERROR_DATA_READ_FAILED           = 0x80121106,
	CELL_PAD_ERROR_NO_DEVICE                  = 0x80121107,
	CELL_PAD_ERROR_UNSUPPORTED_GAMEPAD        = 0x80121108,
	CELL_PAD_ERROR_TOO_MANY_DEVICES           = 0x80121109,
	CELL_PAD_ERROR_EBUSY                      = 0x8012110a,
};

enum CellPadFilterError : u32
{
	CELL_PADFILTER_ERROR_INVALID_PARAMETER = 0x80121401,
};

// Length returned in CellPadData struct
enum
{
	CELL_PAD_LEN_NO_CHANGE = 0,
	CELL_PAD_LEN_CHANGE_DEFAULT = 8,
	CELL_PAD_LEN_CHANGE_PRESS_ON = 20,
	CELL_PAD_LEN_CHANGE_SENSOR_ON = 24,
};

enum
{
	CELL_PADFILTER_IIR_CUTOFF_2ND_LPF_BT_050 = 0, // 50% Nyquist frequency
	CELL_PADFILTER_IIR_CUTOFF_2ND_LPF_BT_020 = 1, // 20% Nyquist frequency
	CELL_PADFILTER_IIR_CUTOFF_2ND_LPF_BT_010 = 2, // 10% Nyquist frequency
};

struct pad_data_internal
{
	u16 vendor_id = 0;
	u16 product_id = 0;
	u32 port_status = 0;
	u32 device_capability = 0;
	u32 device_type = 0;
	u32 pclass_type = 0;
	u32 pclass_profile = 0;

	ENABLE_BITWISE_SERIALIZATION;
};

struct CellPadInfo
{
	be_t<u32> max_connect;
	be_t<u32> now_connect;
	be_t<u32> system_info;
	be_t<u16> vendor_id[CELL_MAX_PADS];
	be_t<u16> product_id[CELL_MAX_PADS];
	u8 status[CELL_MAX_PADS];
};

struct CellPadInfo2
{
	be_t<u32> max_connect;
	be_t<u32> now_connect;
	be_t<u32> system_info;
	be_t<u32> port_status[CELL_PAD_MAX_PORT_NUM];
	be_t<u32> port_setting[CELL_PAD_MAX_PORT_NUM];
	be_t<u32> device_capability[CELL_PAD_MAX_PORT_NUM];
	be_t<u32> device_type[CELL_PAD_MAX_PORT_NUM];
};

struct CellPadPeriphInfo
{
	be_t<u32> max_connect;
	be_t<u32> now_connect;
	be_t<u32> system_info;
```

## 🔗 依赖头文件

- `#include "Emu/Io/pad_types.h"`
- `#include <array>`
