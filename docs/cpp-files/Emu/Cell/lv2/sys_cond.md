# sys_cond.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_cond.h`
- **类型**: 头文件
- **行数**: 51 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_cond`
- `lv2_mutex`
- `ppu_thread`
- `sys_cond_attribute_t`

### 系统调用

- `sys_cond_create()`
- `sys_cond_destroy()`
- `sys_cond_signal()`
- `sys_cond_signal_all()`
- `sys_cond_signal_to()`
- `sys_cond_wait()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"
#include "sys_mutex.h"

struct lv2_mutex;

struct sys_cond_attribute_t
{
	be_t<u32> pshared;
	be_t<s32> flags;
	be_t<u64> ipc_key;

	union
	{
		nse_t<u64, 1> name_u64;
		char name[sizeof(u64)];
	};
};

struct lv2_cond final : lv2_obj
{
	static const u32 id_base = 0x86000000;

	const u64 key;
	const u64 name;
	const u32 mtx_id;

	lv2_mutex* mutex; // Associated Mutex
	shared_ptr<lv2_obj> _mutex;
	ppu_thread* sq{};

	lv2_cond(u64 key, u64 name, u32 mtx_id, shared_ptr<lv2_obj> mutex0) noexcept;

	lv2_cond(utils::serial& ar) noexcept;
	static std::function<void(void*)> load(utils::serial& ar);
	void save(utils::serial& ar);

	CellError on_id_create();
};

class ppu_thread;

// Syscalls

error_code sys_cond_create(ppu_thread& ppu, vm::ptr<u32> cond_id, u32 mutex_id, vm::ptr<sys_cond_attribute_t> attr);
error_code sys_cond_destroy(ppu_thread& ppu, u32 cond_id);
error_code sys_cond_wait(ppu_thread& ppu, u32 cond_id, u64 timeout);
error_code sys_cond_signal(ppu_thread& ppu, u32 cond_id);
error_code sys_cond_signal_all(ppu_thread& ppu, u32 cond_id);
error_code sys_cond_signal_to(ppu_thread& ppu, u32 cond_id, u32 thread_id);

```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "sys_mutex.h"`
