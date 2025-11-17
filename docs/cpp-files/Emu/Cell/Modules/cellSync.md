# cellSync.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSync.h`
- **类型**: 头文件
- **行数**: 364 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellSyncBarrier`
- `CellSyncMutex`
- `Counter`
- `alignas`
- `pop1_t`
- `pop2_t`
- `pop3_t`
- `push1_t`
- `push2_t`
- `push3_t`

### HLE 函数

- `cellSyncLFQueueInitialize()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

#include "Utilities/BitField.h"

#include "Emu/Cell/ErrorCodes.h"

// Return Codes
enum CellSyncError : u32
{
	CELL_SYNC_ERROR_AGAIN                  = 0x80410101,
	CELL_SYNC_ERROR_INVAL                  = 0x80410102,
	CELL_SYNC_ERROR_NOSYS                  = 0x80410103,
	CELL_SYNC_ERROR_NOMEM                  = 0x80410104,
	CELL_SYNC_ERROR_SRCH                   = 0x80410105,
	CELL_SYNC_ERROR_NOENT                  = 0x80410106,
	CELL_SYNC_ERROR_NOEXEC                 = 0x80410107,
	CELL_SYNC_ERROR_DEADLK                 = 0x80410108,
	CELL_SYNC_ERROR_PERM                   = 0x80410109,
	CELL_SYNC_ERROR_BUSY                   = 0x8041010A,
	CELL_SYNC_ERROR_ABORT                  = 0x8041010C,
	CELL_SYNC_ERROR_FAULT                  = 0x8041010D,
	CELL_SYNC_ERROR_CHILD                  = 0x8041010E,
	CELL_SYNC_ERROR_STAT                   = 0x8041010F,
	CELL_SYNC_ERROR_ALIGN                  = 0x80410110,
	CELL_SYNC_ERROR_NULL_POINTER           = 0x80410111,
	CELL_SYNC_ERROR_NOT_SUPPORTED_THREAD   = 0x80410112,
	CELL_SYNC_ERROR_NO_NOTIFIER            = 0x80410113,
	CELL_SYNC_ERROR_NO_SPU_CONTEXT_STORAGE = 0x80410114,
};

enum CellSyncError1 : u32
{
	CELL_SYNC_ERROR_SHOTAGE                = 0x80410112,
	CELL_SYNC_ERROR_UNKNOWNKEY             = 0x80410113,
};

struct CellSyncMutex
{
	struct Counter
	{
		be_t<u16> rel;
		be_t<u16> acq;

		auto lock_begin()
		{
			return acq++;
		}

		bool try_lock()
		{
			if (rel != acq) [[unlikely]]
			{
				return false;
			}

			acq++;
			return true;
		}

		void unlock()
		{
			rel++;
		}
	};

	atomic_t<Counter> ctrl;
};

CHECK_SIZE_ALIGN(CellSyncMutex, 4, 4);

struct CellSyncBarrier
{
	struct alignas(4) ctrl_t
	{
		be_t<s16> value;
		be_t<u16> count;
	};

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Utilities/BitField.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
