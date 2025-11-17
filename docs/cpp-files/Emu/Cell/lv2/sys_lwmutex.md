# sys_lwmutex.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_lwmutex.h`
- **类型**: 头文件
- **行数**: 206 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `alignas`
- `lv2_lwmutex`
- `ppu_thread`
- `sys_lwmutex_attribute_t`
- `sys_lwmutex_t`

### 关键函数

- `_sys_lwmutex_create()`
- `_sys_lwmutex_destroy()`
- `_sys_lwmutex_lock()`
- `_sys_lwmutex_trylock()`
- `_sys_lwmutex_unlock()`
- `_sys_lwmutex_unlock2()`
- `reown()`
- `save()`
- `try_own()`
- `try_unlock()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Memory/vm_ptr.h"

struct sys_lwmutex_attribute_t
{
	be_t<u32> protocol;
	be_t<u32> recursive;

	union
	{
		nse_t<u64, 1> name_u64;
		char name[sizeof(u64)];
	};
};

enum : u32
{
	lwmutex_free     = 0xffffffffu,
	lwmutex_dead     = 0xfffffffeu,
	lwmutex_reserved = 0xfffffffdu,
};

struct sys_lwmutex_t
{
	struct alignas(8) sync_var_t
	{
		be_t<u32> owner;
		be_t<u32> waiter;
	};

	union
	{
		atomic_t<sync_var_t> lock_var;

		struct
		{
			atomic_be_t<u32> owner;
			atomic_be_t<u32> waiter;
		}
		vars;

		atomic_be_t<u64> all_info;
	};

	be_t<u32> attribute;
	be_t<u32> recursive_count;
	be_t<u32> sleep_queue; // lwmutex pseudo-id
	be_t<u32> pad;
};

struct lv2_lwmutex final : lv2_obj
{
	static const u32 id_base = 0x95000000;

	const lv2_protocol protocol;
	const vm::ptr<sys_lwmutex_t> control;
	const be_t<u64> name;

	shared_mutex mutex;
	atomic_t<s32> lwcond_waiters{0};

	struct alignas(16) control_data_t
	{
		s32 signaled{0};
		u32 reserved{};
		ppu_thread* sq{};
	};

	atomic_t<control_data_t> lv2_control{};

	lv2_lwmutex(u32 protocol, vm::ptr<sys_lwmutex_t> control, u64 name) noexcept
		: protocol{static_cast<u8>(protocol)}
		, control(control)
		, name(std::bit_cast<be_t<u64>>(name))
	{
	}

```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Memory/vm_ptr.h"`
