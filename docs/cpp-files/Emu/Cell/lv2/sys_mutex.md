# sys_mutex.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_mutex.h`
- **类型**: 头文件
- **行数**: 207 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `alignas`
- `lv2_mutex`
- `ppu_thread`
- `sys_mutex_attribute_t`

### 系统调用

- `sys_mutex_create()`
- `sys_mutex_destroy()`
- `sys_mutex_lock()`
- `sys_mutex_trylock()`
- `sys_mutex_unlock()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Memory/vm_ptr.h"

#include "Emu/Cell/PPUThread.h"

struct sys_mutex_attribute_t
{
	be_t<u32> protocol; // SYS_SYNC_FIFO, SYS_SYNC_PRIORITY or SYS_SYNC_PRIORITY_INHERIT
	be_t<u32> recursive; // SYS_SYNC_RECURSIVE or SYS_SYNC_NOT_RECURSIVE
	be_t<u32> pshared;
	be_t<u32> adaptive;
	be_t<u64> ipc_key;
	be_t<s32> flags;
	be_t<u32> pad;

	union
	{
		nse_t<u64, 1> name_u64;
		char name[sizeof(u64)];
	};
};

class ppu_thread;

struct lv2_mutex final : lv2_obj
{
	static const u32 id_base = 0x85000000;

	const lv2_protocol protocol;
	const u32 recursive;
	const u32 adaptive;
	const u64 key;
	const u64 name;

	u32 cond_count = 0; // Condition Variables
	shared_mutex mutex;
	atomic_t<u32> lock_count{0}; // Recursive Locks

	struct alignas(16) control_data_t
	{
		u32 owner{};
		u32 reserved{};
		ppu_thread* sq{};
	};

	atomic_t<control_data_t> control{};

	lv2_mutex(u32 protocol, u32 recursive,u32 adaptive, u64 key, u64 name) noexcept
		: protocol{static_cast<u8>(protocol)}
		, recursive(recursive)
		, adaptive(adaptive)
		, key(key)
		, name(name)
	{
	}

	lv2_mutex(utils::serial& ar);
	static std::function<void(void*)> load(utils::serial& ar);
	void save(utils::serial& ar);

	template <typename T>
	CellError try_lock(T& cpu)
	{
		auto it = control.load();

		if (!it.owner)
		{
			auto store = it;
			store.owner = cpu.id;
			if (!control.compare_and_swap_test(it, store))
			{
				return CELL_EBUSY;
			}

			return {};
		}

```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/PPUThread.h"`
