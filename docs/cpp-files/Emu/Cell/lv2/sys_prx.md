# sys_prx.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_prx.h`
- **类型**: 头文件
- **行数**: 271 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `sys_prx_get_module_id_by_name_option_t`
- `sys_prx_get_module_list_option_t`
- `sys_prx_module_info_option_t`
- `sys_prx_module_info_t`
- `sys_prx_register_module_0x20_t`
- `sys_prx_register_module_0x30_type_1_t`
- `sys_prx_start_module_option_t`
- `sys_prx_start_stop_module_option_t`
- `sys_prx_stop_module_option_t`
- `sys_prx_unload_module_option_t`

### 系统调用

- `sys_prx_get_ppu_guid()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Cell/PPUAnalyser.h"
#include "Emu/Cell/ErrorCodes.h"
#include "Emu/Memory/vm_ptr.h"

// Return codes
enum CellPrxError : u32
{
	CELL_PRX_ERROR_ERROR                       = 0x80011001, // Error state
	CELL_PRX_ERROR_ILLEGAL_PERM                = 0x800110d1, // No permission to execute API
	CELL_PRX_ERROR_UNKNOWN_MODULE              = 0x8001112e, // Specified PRX could not be found
	CELL_PRX_ERROR_ALREADY_STARTED             = 0x80011133, // Specified PRX is already started
	CELL_PRX_ERROR_NOT_STARTED                 = 0x80011134, // Specified PRX is not started
	CELL_PRX_ERROR_ALREADY_STOPPED             = 0x80011135, // Specified PRX is already stopped
	CELL_PRX_ERROR_CAN_NOT_STOP                = 0x80011136, // Specified PRX must not be stopped
	CELL_PRX_ERROR_NOT_REMOVABLE               = 0x80011138, // Specified PRX must not be deleted
	CELL_PRX_ERROR_LIBRARY_NOT_YET_LINKED      = 0x8001113a, // Called unlinked function
	CELL_PRX_ERROR_LIBRARY_FOUND               = 0x8001113b, // Specified library is already registered
	CELL_PRX_ERROR_LIBRARY_NOTFOUND            = 0x8001113c, // Specified library is not registered
	CELL_PRX_ERROR_ILLEGAL_LIBRARY             = 0x8001113d, // Library structure is invalid
	CELL_PRX_ERROR_LIBRARY_INUSE               = 0x8001113e, // Library cannot be deleted because it is linked
	CELL_PRX_ERROR_ALREADY_STOPPING            = 0x8001113f, // Specified PRX is in the process of stopping
	CELL_PRX_ERROR_UNSUPPORTED_PRX_TYPE        = 0x80011148, // Specified PRX format is invalid and cannot be loaded
	CELL_PRX_ERROR_INVAL                       = 0x80011324, // Argument value is invalid
	CELL_PRX_ERROR_ILLEGAL_PROCESS             = 0x80011801, // Specified process does not exist
	CELL_PRX_ERROR_NO_LIBLV2                   = 0x80011881, // liblv2.sprx does not exist
	CELL_PRX_ERROR_UNSUPPORTED_ELF_TYPE        = 0x80011901, // ELF type of specified file is not supported
	CELL_PRX_ERROR_UNSUPPORTED_ELF_CLASS       = 0x80011902, // ELF class of specified file is not supported
	CELL_PRX_ERROR_UNDEFINED_SYMBOL            = 0x80011904, // References undefined symbols
	CELL_PRX_ERROR_UNSUPPORTED_RELOCATION_TYPE = 0x80011905, // Uses unsupported relocation type
	CELL_PRX_ERROR_ELF_IS_REGISTERED           = 0x80011910, // Fixed ELF is already registered
	CELL_PRX_ERROR_NO_EXIT_ENTRY               = 0x80011911,
};

enum
{
	SYS_PRX_MODULE_FILENAME_SIZE = 512
};

struct sys_prx_get_module_id_by_name_option_t
{
	be_t<u64> size;
	vm::ptr<void> base;
};

struct sys_prx_load_module_option_t
{
	be_t<u64> size;
	vm::bptr<void> base_addr;
};

struct sys_prx_segment_info_t
{
	be_t<u64> base;
	be_t<u64> filesz;
	be_t<u64> memsz;
	be_t<u64> index;
	be_t<u64> type;
};

struct sys_prx_module_info_t
{
	be_t<u64> size; // 0
	char name[30]; // 8
	char version[2]; // 0x26
	be_t<u32> modattribute; // 0x28
	be_t<u32> start_entry; // 0x2c
	be_t<u32> stop_entry; // 0x30
	be_t<u32> all_segments_num; // 0x34
	vm::bptr<char> filename; // 0x38
	be_t<u32> filename_size; // 0x3c
	vm::bptr<sys_prx_segment_info_t> segments; // 0x40
	be_t<u32> segments_num; // 0x44
};

struct sys_prx_module_info_v2_t : sys_prx_module_info_t
{
```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Cell/PPUAnalyser.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "Emu/Memory/vm_ptr.h"`
