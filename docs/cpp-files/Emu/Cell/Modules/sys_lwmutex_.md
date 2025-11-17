# sys_lwmutex_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_lwmutex_.cpp`
- **类型**: 源文件
- **行数**: 419 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_lwmutex_create()`
- `sys_lwmutex_destroy()`
- `sys_lwmutex_lock()`
- `sys_lwmutex_trylock()`
- `sys_lwmutex_unlock()`
- `sys_mutex_create()`
- `sys_mutex_destroy()`
- `sys_mutex_lock()`
- `sys_mutex_trylock()`
- `sys_mutex_unlock()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/System.h"
#include "Emu/system_config.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/Cell/timers.hpp"
#include "Emu/Cell/lv2/sys_lwmutex.h"
#include "Emu/Cell/lv2/sys_mutex.h"
#include "sysPrxForUser.h"

#include "util/asm.hpp"

LOG_CHANNEL(sysPrxForUser);

error_code sys_lwmutex_create(ppu_thread& ppu, vm::ptr<sys_lwmutex_t> lwmutex, vm::ptr<sys_lwmutex_attribute_t> attr)
{
	sysPrxForUser.trace("sys_lwmutex_create(lwmutex=*0x%x, attr=*0x%x)", lwmutex, attr);

	const u32 recursive = attr->recursive;

	if (recursive != SYS_SYNC_RECURSIVE && recursive != SYS_SYNC_NOT_RECURSIVE)
	{
		sysPrxForUser.error("sys_lwmutex_create(): invalid recursive attribute (0x%x)", recursive);
		return CELL_EINVAL;
	}

	const u32 protocol = attr->protocol;

	switch (protocol)
	{
	case SYS_SYNC_FIFO: break;
	case SYS_SYNC_RETRY: break;
	case SYS_SYNC_PRIORITY: break;
	default: sysPrxForUser.error("sys_lwmutex_create(): invalid protocol (0x%x)", protocol); return CELL_EINVAL;
	}

	vm::var<u32> out_id;
	vm::var<sys_mutex_attribute_t> attrs;
	attrs->protocol  = protocol == SYS_SYNC_FIFO ? SYS_SYNC_FIFO : SYS_SYNC_PRIORITY;
	attrs->recursive = attr->recursive;
	attrs->pshared   = SYS_SYNC_NOT_PROCESS_SHARED;
	attrs->adaptive  = SYS_SYNC_NOT_ADAPTIVE;
	attrs->ipc_key   = 0;
	attrs->flags     = 0;
	attrs->name_u64  = attr->name_u64;

	if (error_code res = g_cfg.core.hle_lwmutex ? sys_mutex_create(ppu, out_id, attrs) : _sys_lwmutex_create(ppu, out_id, protocol, lwmutex, 0x80000001, std::bit_cast<be_t<u64>>(attr->name_u64)))
	{
		return res;
	}

	lwmutex->lock_var.store({ lwmutex_free, 0 });
	lwmutex->attribute = attr->recursive | attr->protocol;
	lwmutex->recursive_count = 0;
	lwmutex->sleep_queue = *out_id;
	return CELL_OK;
}

error_code sys_lwmutex_destroy(ppu_thread& ppu, vm::ptr<sys_lwmutex_t> lwmutex)
{
	sysPrxForUser.trace("sys_lwmutex_destroy(lwmutex=*0x%x)", lwmutex);

	if (g_cfg.core.hle_lwmutex)
	{
		return sys_mutex_destroy(ppu, lwmutex->sleep_queue);
	}

	// check to prevent recursive locking in the next call
	if (lwmutex->vars.owner.load() == ppu.id)
	{
		return CELL_EBUSY;
	}

	// attempt to lock the mutex
	if (error_code res = sys_lwmutex_trylock(ppu, lwmutex))
	{
		return res;
	}

	// call the syscall
	if (error_code res = _sys_lwmutex_destroy(ppu, lwmutex->sleep_queue))
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/System.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/timers.hpp"`
- `#include "Emu/Cell/lv2/sys_lwmutex.h"`
- `#include "Emu/Cell/lv2/sys_mutex.h"`
- `#include "sysPrxForUser.h"`
- `#include "util/asm.hpp"`
