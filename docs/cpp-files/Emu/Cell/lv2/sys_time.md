# sys_time.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_time.h`
- **类型**: 头文件
- **行数**: 15 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_time_get_current_time()`
- `sys_time_get_rtc()`
- `sys_time_get_timebase_frequency()`
- `sys_time_get_timezone()`
- `sys_time_set_current_time()`
- `sys_time_set_timezone()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// SysCalls

error_code sys_time_set_timezone(s32 timezone, s32 summertime);
error_code sys_time_get_timezone(vm::ptr<s32> timezone, vm::ptr<s32> summertime);
error_code sys_time_get_current_time(vm::ptr<s64> sec, vm::ptr<s64> nsec);
error_code sys_time_set_current_time(s64 sec, s64 nsec);
u64 sys_time_get_timebase_frequency();
error_code sys_time_get_rtc(vm::ptr<u64> rtc);

extern u64 g_timebase_offs;

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
