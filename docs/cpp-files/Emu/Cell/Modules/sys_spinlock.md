# sys_spinlock.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_spinlock.cpp`
- **类型**: 源文件
- **行数**: 58 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_spinlock_initialize()`
- `sys_spinlock_lock()`
- `sys_spinlock_trylock()`
- `sys_spinlock_unlock()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

LOG_CHANNEL(sysPrxForUser);

void sys_spinlock_initialize(vm::ptr<atomic_be_t<u32>> lock)
{
	sysPrxForUser.trace("sys_spinlock_initialize(lock=*0x%x)", lock);

	if (*lock)
	{
		*lock = 0;
	}
}

error_code sys_spinlock_lock(ppu_thread& ppu, vm::ptr<atomic_be_t<u32>> lock)
{
	sysPrxForUser.trace("sys_spinlock_lock(lock=*0x%x)", lock);

	// Try to exchange with 0xabadcafe, repeat until exchanged with 0
	while (*lock || lock->exchange(0xabadcafe))
	{
		if (ppu.test_stopped())
		{
			ppu.state += cpu_flag::again;
			return {};
		}
	}

	return CELL_OK;
}

error_code sys_spinlock_trylock(vm::ptr<atomic_be_t<u32>> lock)
{
	sysPrxForUser.trace("sys_spinlock_trylock(lock=*0x%x)", lock);

	if (*lock || lock->exchange(0xabadcafe))
	{
		return not_an_error(CELL_EBUSY);
	}

	return CELL_OK;
}

void sys_spinlock_unlock(vm::ptr<atomic_be_t<u32>> lock)
{
	sysPrxForUser.trace("sys_spinlock_unlock(lock=*0x%x)", lock);

	*lock = 0;
}

void sysPrxForUser_sys_spinlock_init()
{
	REG_FUNC(sysPrxForUser, sys_spinlock_initialize);
	REG_FUNC(sysPrxForUser, sys_spinlock_lock);
	REG_FUNC(sysPrxForUser, sys_spinlock_trylock);
	REG_FUNC(sysPrxForUser, sys_spinlock_unlock);
}

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
