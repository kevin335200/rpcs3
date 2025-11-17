# sys_prx_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_prx_.cpp`
- **类型**: 源文件
- **行数**: 281 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_prx_exitspawn_with_level()`
- `sys_prx_get_module_id_by_address()`
- `sys_prx_get_module_id_by_name()`
- `sys_prx_get_module_info()`
- `sys_prx_get_module_list()`
- `sys_prx_get_my_module_id()`
- `sys_prx_load_module()`
- `sys_prx_load_module_by_fd()`
- `sys_prx_load_module_list()`
- `sys_prx_load_module_list_on_memcontainer()`
- `sys_prx_load_module_on_memcontainer()`
- `sys_prx_load_module_on_memcontainer_by_fd()`
- `sys_prx_register_library()`
- `sys_prx_start_module()`
- `sys_prx_stop_module()`
- `sys_prx_unload_module()`
- `sys_prx_unregister_library()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_lwmutex.h"
#include "Emu/Cell/lv2/sys_prx.h"
#include "sysPrxForUser.h"

LOG_CHANNEL(sysPrxForUser);

extern vm::gvar<sys_lwmutex_t> g_ppu_prx_lwm;

// Convert the array of 32-bit pointers to 64-bit pointers using stack allocation
static auto convert_path_list(vm::cpptr<char> path_list, s32 count)
{
	return vm::var<vm::cptr<char, u64>[]>(count, path_list.get_ptr());
}

// Execute start or stop module function
static void entryx(ppu_thread& ppu, vm::ptr<sys_prx_start_stop_module_option_t> opt, u32 args, vm::ptr<void> argp, vm::ptr<s32> res)
{
	if (opt->entry2.addr() != umax)
	{
		*res = opt->entry2(ppu, opt->entry, args, argp);
		return;
	}

	if (opt->entry.addr() != umax)
	{
		*res = opt->entry(ppu, args, argp);
		return;
	}

	*res = 0;
}

error_code sys_prx_load_module(ppu_thread& ppu, vm::cptr<char> path, u64 flags, vm::ptr<sys_prx_load_module_option_t> pOpt)
{
	sysPrxForUser.warning("sys_prx_load_module(path=%s, flags=0x%x, pOpt=*0x%x)", path, flags, pOpt);

	sys_lwmutex_locker lock(ppu, g_ppu_prx_lwm);

	return _sys_prx_load_module(ppu, path, flags, pOpt);
}

error_code sys_prx_load_module_by_fd(ppu_thread& ppu, s32 fd, u64 offset, u64 flags, vm::ptr<sys_prx_load_module_option_t> pOpt)
{
	sysPrxForUser.warning("sys_prx_load_module_by_fd(fd=%d, offset=0x%x, flags=0x%x, pOpt=*0x%x)", fd, offset, flags, pOpt);

	sys_lwmutex_locker lock(ppu, g_ppu_prx_lwm);

	return _sys_prx_load_module_by_fd(ppu, fd, offset, flags, pOpt);
}

error_code sys_prx_load_module_on_memcontainer(ppu_thread& ppu, vm::cptr<char> path, u32 mem_ct, u64 flags, vm::ptr<sys_prx_load_module_option_t> pOpt)
{
	sysPrxForUser.warning("sys_prx_load_module_on_memcontainer(path=%s, mem_ct=0x%x, flags=0x%x, pOpt=*0x%x)", path, mem_ct, flags, pOpt);

	sys_lwmutex_locker lock(ppu, g_ppu_prx_lwm);

	return _sys_prx_load_module_on_memcontainer(ppu, path, mem_ct, flags, pOpt);
}

error_code sys_prx_load_module_on_memcontainer_by_fd(ppu_thread& ppu, s32 fd, u64 offset, u32 mem_ct, u64 flags, vm::ptr<sys_prx_load_module_option_t> pOpt)
{
	sysPrxForUser.warning("sys_prx_load_module_on_memcontainer_by_fd(fd=%d, offset=0x%x, mem_ct=0x%x, flags=0x%x, pOpt=*0x%x)", fd, offset, mem_ct, flags, pOpt);

	sys_lwmutex_locker lock(ppu, g_ppu_prx_lwm);

	return _sys_prx_load_module_on_memcontainer_by_fd(ppu, fd, offset, mem_ct, flags, pOpt);
}

error_code sys_prx_load_module_list(ppu_thread& ppu, s32 count, vm::cpptr<char> path_list, u64 flags, vm::ptr<sys_prx_load_module_option_t> pOpt, vm::ptr<u32> id_list)
{
	sysPrxForUser.todo("sys_prx_load_module_list(count=%d, path_list=**0x%x, flags=0x%x, pOpt=*0x%x, id_list=*0x%x)", count, path_list, flags, pOpt, id_list);

	sys_lwmutex_locker lock(ppu, g_ppu_prx_lwm);

	return _sys_prx_load_module_list(ppu, count, convert_path_list(path_list, count), flags, pOpt, id_list);
}

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_lwmutex.h"`
- `#include "Emu/Cell/lv2/sys_prx.h"`
- `#include "sysPrxForUser.h"`
