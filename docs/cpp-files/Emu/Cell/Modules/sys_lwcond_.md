# sys_lwcond_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_lwcond_.cpp`
- **类型**: 源文件
- **行数**: 391 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_cond_create()`
- `sys_cond_destroy()`
- `sys_cond_signal()`
- `sys_cond_signal_all()`
- `sys_cond_signal_to()`
- `sys_cond_wait()`
- `sys_lwcond_create()`
- `sys_lwcond_destroy()`
- `sys_lwcond_signal()`
- `sys_lwcond_signal_all()`
- `sys_lwcond_signal_to()`
- `sys_lwcond_wait()`
- `sys_lwmutex_lock()`
- `sys_lwmutex_trylock()`
- `sys_lwmutex_unlock()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/system_config.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/Cell/lv2/sys_lwmutex.h"
#include "Emu/Cell/lv2/sys_lwcond.h"
#include "Emu/Cell/lv2/sys_cond.h"
#include "sysPrxForUser.h"

LOG_CHANNEL(sysPrxForUser);

error_code sys_lwcond_create(ppu_thread& ppu, vm::ptr<sys_lwcond_t> lwcond, vm::ptr<sys_lwmutex_t> lwmutex, vm::ptr<sys_lwcond_attribute_t> attr)
{
	sysPrxForUser.trace("sys_lwcond_create(lwcond=*0x%x, lwmutex=*0x%x, attr=*0x%x)", lwcond, lwmutex, attr);

	vm::var<u32> out_id;
	vm::var<sys_cond_attribute_t> attrs;
	attrs->pshared  = SYS_SYNC_NOT_PROCESS_SHARED;
	attrs->name_u64 = attr->name_u64;

	if (auto res = g_cfg.core.hle_lwmutex ? sys_cond_create(ppu, out_id, lwmutex->sleep_queue, attrs) : _sys_lwcond_create(ppu, out_id, lwmutex->sleep_queue, lwcond, std::bit_cast<be_t<u64>>(attr->name_u64)))
	{
		return res;
	}

	lwcond->lwmutex      = lwmutex;
	lwcond->lwcond_queue = *out_id;
	return CELL_OK;
}

error_code sys_lwcond_destroy(ppu_thread& ppu, vm::ptr<sys_lwcond_t> lwcond)
{
	sysPrxForUser.trace("sys_lwcond_destroy(lwcond=*0x%x)", lwcond);

	if (g_cfg.core.hle_lwmutex)
	{
		return sys_cond_destroy(ppu, lwcond->lwcond_queue);
	}

	if (error_code res = _sys_lwcond_destroy(ppu, lwcond->lwcond_queue))
	{
		return res;
	}

	lwcond->lwcond_queue = lwmutex_dead;
	return CELL_OK;
}

error_code sys_lwcond_signal(ppu_thread& ppu, vm::ptr<sys_lwcond_t> lwcond)
{
	sysPrxForUser.trace("sys_lwcond_signal(lwcond=*0x%x)", lwcond);

	if (g_cfg.core.hle_lwmutex)
	{
		return sys_cond_signal(ppu, lwcond->lwcond_queue);
	}

	const vm::ptr<sys_lwmutex_t> lwmutex = lwcond->lwmutex;

	if ((lwmutex->attribute & SYS_SYNC_ATTR_PROTOCOL_MASK) == SYS_SYNC_RETRY)
	{
		return _sys_lwcond_signal(ppu, lwcond->lwcond_queue, 0, u32{umax}, 2);
	}

	if (lwmutex->vars.owner.load() == ppu.id)
	{
		// if owns the mutex
		lwmutex->all_info++;

		// call the syscall
		if (error_code res = _sys_lwcond_signal(ppu, lwcond->lwcond_queue, lwmutex->sleep_queue, u32{umax}, 1))
		{
			static_cast<void>(ppu.test_stopped());

			lwmutex->all_info--;

			if (res + 0u != CELL_EPERM)
			{
				return res;
			}
		}
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/system_config.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_lwmutex.h"`
- `#include "Emu/Cell/lv2/sys_lwcond.h"`
- `#include "Emu/Cell/lv2/sys_cond.h"`
- `#include "sysPrxForUser.h"`
