# sys_gpio.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_gpio.h`
- **类型**: 头文件
- **行数**: 14 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_gpio_get()`
- `sys_gpio_set()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

enum : u64
{
	SYS_GPIO_UNKNOWN_DEVICE_ID    = 0x0,
	SYS_GPIO_LED_DEVICE_ID        = 0x1,
	SYS_GPIO_DIP_SWITCH_DEVICE_ID = 0x2,
};

error_code sys_gpio_get(u64 device_id, vm::ptr<u64> value);
error_code sys_gpio_set(u64 device_id, u64 mask, u64 value);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
