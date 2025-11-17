# sys_mmapper.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_mmapper.h`
- **类型**: 头文件
- **行数**: 117 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_memory`
- `lv2_memory_container`
- `mmapper_unk_entry_struct0`
- `page_fault_event_entries`
- `page_fault_notification_entries`
- `page_fault_notification_entry`
- `ppu_thread`
- `shm`

### 系统调用

- `sys_mmapper_allocate_address()`
- `sys_mmapper_allocate_fixed_address()`
- `sys_mmapper_allocate_shared_memory()`
- `sys_mmapper_allocate_shared_memory_ext()`
- `sys_mmapper_allocate_shared_memory_from_container()`
- `sys_mmapper_allocate_shared_memory_from_container_ext()`
- `sys_mmapper_change_address_access_right()`
- `sys_mmapper_enable_page_fault_notification()`
- `sys_mmapper_free_address()`
- `sys_mmapper_free_shared_memory()`
- `sys_mmapper_map_shared_memory()`
- `sys_mmapper_search_and_map()`
- `sys_mmapper_unmap_shared_memory()`

## 💻 代码片段

```cpp
#pragma once

#include "sys_sync.h"

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

#include "util/shared_ptr.hpp"

#include <vector>

struct lv2_memory_container;

namespace utils
{
	class shm;
}

struct lv2_memory : lv2_obj
{
	static const u32 id_base = 0x08000000;

	const u32 size; // Memory size
	const u32 align; // Alignment required
	const u64 flags;
	const u64 key; // IPC key
	const bool pshared; // Process shared flag
	lv2_memory_container* const ct; // Associated memory container
	atomic_ptr<std::shared_ptr<utils::shm>> shm;

	atomic_t<u32> counter{0};

	lv2_memory(u32 size, u32 align, u64 flags, u64 key, bool pshared, lv2_memory_container* ct);

	lv2_memory(utils::serial& ar);
	static std::function<void(void*)> load(utils::serial& ar);
	void save(utils::serial& ar);

	CellError on_id_create();
};

enum : u64
{
	SYS_MEMORY_PAGE_FAULT_EVENT_KEY	       = 0xfffe000000000000ULL,
};

enum : u64
{
	SYS_MMAPPER_NO_SHM_KEY = 0xffff000000000000ull, // Unofficial name
};

enum : u64
{
	SYS_MEMORY_PAGE_FAULT_CAUSE_NON_MAPPED = 0x2ULL,
	SYS_MEMORY_PAGE_FAULT_CAUSE_READ_ONLY  = 0x1ULL,
	SYS_MEMORY_PAGE_FAULT_TYPE_PPU_THREAD  = 0x0ULL,
	SYS_MEMORY_PAGE_FAULT_TYPE_SPU_THREAD  = 0x1ULL,
	SYS_MEMORY_PAGE_FAULT_TYPE_RAW_SPU     = 0x2ULL,
};

struct page_fault_notification_entry
{
	ENABLE_BITWISE_SERIALIZATION;

	u32 start_addr; // Starting address of region to monitor.
	u32 event_queue_id; // Queue to be notified.
	u32 port_id; // Port used to notify the queue.
};

// Used to hold list of queues to be notified on page fault event.
struct page_fault_notification_entries
{
	std::vector<page_fault_notification_entry> entries;
	shared_mutex mutex;

	SAVESTATE_INIT_POS(44);

	page_fault_notification_entries() = default;
	page_fault_notification_entries(utils::serial& ar);
	void save(utils::serial& ar);
```

## 🔗 依赖头文件

- `#include "sys_sync.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "util/shared_ptr.hpp"`
- `#include <vector>`
