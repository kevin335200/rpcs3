# sys_mempool.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_mempool.cpp`
- **类型**: 源文件
- **行数**: 226 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `memory_pool_t`

### 系统调用

- `sys_cond_create()`
- `sys_cond_destroy()`
- `sys_cond_signal()`
- `sys_cond_wait()`
- `sys_mempool_allocate_block()`
- `sys_mempool_create()`
- `sys_mempool_destroy()`
- `sys_mempool_free_block()`
- `sys_mempool_get_count()`
- `sys_mempool_try_allocate_block()`
- `sys_mutex_create()`
- `sys_mutex_destroy()`
- `sys_mutex_lock()`
- `sys_mutex_unlock()`

## 💻 代码片段

```cpp
#include "stdafx.h"

#include "Utilities/StrUtil.h"

#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_mutex.h"
#include "Emu/Cell/lv2/sys_cond.h"

LOG_CHANNEL(sysPrxForUser);

using sys_mempool_t = u32;

struct memory_pool_t
{
	static const u32 id_base = 1;
	static const u32 id_step = 1;
	static const u32 id_count = 1023;
	SAVESTATE_INIT_POS(21);

	u32 mutexid;
	u32 condid;

	vm::ptr<void> chunk;
	u64 chunk_size;
	u64 block_size;
	u64 ralignment;
	std::vector<vm::ptr<void>> free_blocks;
};

error_code sys_mempool_create(ppu_thread& ppu, vm::ptr<sys_mempool_t> mempool, vm::ptr<void> chunk, const u64 chunk_size, const u64 block_size, const u64 ralignment)
{
	sysPrxForUser.warning("sys_mempool_create(mempool=*0x%x, chunk=*0x%x, chunk_size=%d, block_size=%d, ralignment=%d)", mempool, chunk, chunk_size, block_size, ralignment);

	if (block_size > chunk_size)
	{
		return CELL_EINVAL;
	}

	u64 alignment = ralignment;
	if (ralignment == 0 || ralignment == 2)
	{
		alignment = 4;
	}

	// Check if alignment is power of two
	if ((alignment & (alignment - 1)) != 0)
	{
		return CELL_EINVAL;
	}

	// Test chunk address aligment
	if (!chunk.aligned(8))
	{
		return CELL_EINVAL;
	}

	auto id = idm::make<memory_pool_t>();
	*mempool = id;

	auto memory_pool = idm::get_unlocked<memory_pool_t>(id);

	memory_pool->chunk = chunk;
	memory_pool->chunk_size = chunk_size;
	memory_pool->block_size = block_size;
	memory_pool->ralignment = alignment;

	// TODO: check blocks alignment wrt ralignment
	u64 num_blocks = chunk_size / block_size;
	memory_pool->free_blocks.resize(num_blocks);
	for (u32 i = 0; i < num_blocks; ++i)
	{
		memory_pool->free_blocks[i] = vm::ptr<void>::make(chunk.addr() + i * static_cast<u32>(block_size));
	}

	// Create synchronization variables
	vm::var<u32> mutexid;
	vm::var<sys_mutex_attribute_t> attr;
	attr->protocol = SYS_SYNC_PRIORITY;
	attr->recursive = SYS_SYNC_NOT_RECURSIVE;
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Utilities/StrUtil.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_mutex.h"`
- `#include "Emu/Cell/lv2/sys_cond.h"`
