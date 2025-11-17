# sys_event_flag.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_event_flag.h`
- **类型**: 头文件
- **行数**: 123 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_event_flag`
- `ppu_thread`
- `sys_event_flag_attribute_t`

### 系统调用

- `sys_event_flag_cancel()`
- `sys_event_flag_clear()`
- `sys_event_flag_create()`
- `sys_event_flag_destroy()`
- `sys_event_flag_get()`
- `sys_event_flag_set()`
- `sys_event_flag_trywait()`
- `sys_event_flag_wait()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Memory/vm_ptr.h"

enum
{
	SYS_SYNC_WAITER_SINGLE = 0x10000,
	SYS_SYNC_WAITER_MULTIPLE = 0x20000,

	SYS_EVENT_FLAG_WAIT_AND = 0x01,
	SYS_EVENT_FLAG_WAIT_OR = 0x02,

	SYS_EVENT_FLAG_WAIT_CLEAR = 0x10,
	SYS_EVENT_FLAG_WAIT_CLEAR_ALL = 0x20,
};

struct sys_event_flag_attribute_t
{
	be_t<u32> protocol;
	be_t<u32> pshared;
	be_t<u64> ipc_key;
	be_t<s32> flags;
	be_t<s32> type;

	union
	{
		nse_t<u64, 1> name_u64;
		char name[sizeof(u64)];
	};
};

struct lv2_event_flag final : lv2_obj
{
	static const u32 id_base = 0x98000000;

	const lv2_protocol protocol;
	const u64 key;
	const s32 type;
	const u64 name;

	shared_mutex mutex;
	atomic_t<u64> pattern;
	ppu_thread* sq{};

	lv2_event_flag(u32 protocol, u64 key, s32 type, u64 name, u64 pattern) noexcept
		: protocol{static_cast<u8>(protocol)}
		, key(key)
		, type(type)
		, name(name)
		, pattern(pattern)
	{
	}

	lv2_event_flag(utils::serial& ar);
	static std::function<void(void*)> load(utils::serial& ar);
	void save(utils::serial& ar);

	// Check mode arg
	static bool check_mode(u32 mode)
	{
		switch (mode & 0xf)
		{
		case SYS_EVENT_FLAG_WAIT_AND: break;
		case SYS_EVENT_FLAG_WAIT_OR: break;
		default: return false;
		}

		switch (mode & ~0xf)
		{
		case 0: break;
		case SYS_EVENT_FLAG_WAIT_CLEAR: break;
		case SYS_EVENT_FLAG_WAIT_CLEAR_ALL: break;
		default: return false;
		}

		return true;
	}

```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Memory/vm_ptr.h"`
