# sys_ss.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_ss.h`
- **类型**: 头文件
- **行数**: 33 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `CellSsOpenPSID`

### 系统调用

- `sys_ss_access_control_engine()`
- `sys_ss_appliance_info_manager()`
- `sys_ss_get_boot_device()`
- `sys_ss_get_cache_of_flash_ext_flag()`
- `sys_ss_get_cache_of_product_mode()`
- `sys_ss_get_console_id()`
- `sys_ss_get_open_psid()`
- `sys_ss_individual_info_manager()`
- `sys_ss_random_number_generator()`
- `sys_ss_secure_rtc()`
- `sys_ss_update_manager()`
- `sys_ss_virtual_trm_manager()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

// Unofficial error code names
enum sys_ss_rng_error : u32
{
	SYS_SS_RNG_ERROR_INVALID_PKG = 0x80010500,
	SYS_SS_RNG_ERROR_ENOMEM = 0x80010501,
	SYS_SS_RNG_ERROR_EAGAIN = 0x80010503,
	SYS_SS_RNG_ERROR_EFAULT = 0x80010509,
	SYS_SS_RTC_ERROR_UNK = 0x8001050f,
};

struct CellSsOpenPSID
{
	be_t<u64> high;
	be_t<u64> low;
};

error_code sys_ss_random_number_generator(u64 pkg_id, vm::ptr<void> buf, u64 size);
error_code sys_ss_access_control_engine(u64 pkg_id, u64 a2, u64 a3);
error_code sys_ss_get_console_id(vm::ptr<u8> buf);
error_code sys_ss_get_open_psid(vm::ptr<CellSsOpenPSID> psid);
error_code sys_ss_appliance_info_manager(u32 code, vm::ptr<u8> buffer);
error_code sys_ss_get_cache_of_product_mode(vm::ptr<u8> ptr);
error_code sys_ss_secure_rtc(u64 cmd, u64 a2, u64 a3, u64 a4);
error_code sys_ss_get_cache_of_flash_ext_flag(vm::ptr<u64> flag);
error_code sys_ss_get_boot_device(vm::ptr<u64> dev);
error_code sys_ss_update_manager(u64 pkg_id, u64 a1, u64 a2, u64 a3, u64 a4, u64 a5, u64 a6);
error_code sys_ss_virtual_trm_manager(u64 pkg_id, u64 a1, u64 a2, u64 a3, u64 a4);
error_code sys_ss_individual_info_manager(u64 pkg_id, u64 a2, vm::ptr<u64> out_size, u64 a4, u64 a5, u64 a6);

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
