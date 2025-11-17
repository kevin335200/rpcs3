# cellFs.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellFs.h`
- **类型**: 头文件
- **行数**: 42 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellFsAio`
- `CellFsRingBuffer`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

// CellFsRingBuffer.copy
enum : s32
{
	CELL_FS_ST_COPY     = 0,
	CELL_FS_ST_COPYLESS = 1,
};

struct CellFsRingBuffer
{
	be_t<u64> ringbuf_size;
	be_t<u64> block_size;
	be_t<u64> transfer_rate;
	be_t<s32> copy;
};

// cellFsStReadGetStatus status
enum : u64
{
	CELL_FS_ST_INITIALIZED     = 0x0001,
	CELL_FS_ST_NOT_INITIALIZED = 0x0002,
	CELL_FS_ST_STOP            = 0x0100,
	CELL_FS_ST_PROGRESS        = 0x0200,
};

enum : s32
{
	CELL_FS_AIO_MAX_FS      = 10, // cellFsAioInit limit
	CELL_FS_AIO_MAX_REQUEST = 32, // cellFsAioRead request limit per mount point
};

struct CellFsAio
{
	be_t<u32> fd;
	be_t<u64> offset;
	vm::bptrb<void> buf;
	be_t<u64> size;
	be_t<u64> user_data;
};

```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
