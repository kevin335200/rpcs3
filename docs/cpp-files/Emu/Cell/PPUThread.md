# PPUThread.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUThread.h`
- **类型**: 头文件
- **行数**: 471 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `call_history_t`
- `cmd64`
- `entry_t`
- `hle_func_call_with_toc_info_t`
- `pair_t`
- `ppu_func_opd_t`
- `ppu_gpr_cast_impl`
- `ppu_thread`
- `ppu_thread_params`
- `syscall_history_t`

### 关键函数

- `cmd_pop()`
- `cmd_push()`
- `cpu_on_stop()`
- `cpu_sleep()`
- `dump_all()`
- `dump_callstack_list()`
- `dump_regs()`
- `exec_task()`
- `fast_call()`
- `savable()`
- `save()`
- `serialize_common()`
- `stack_pop_verbose()`
- `stack_push()`
- `to()`

## 💻 代码片段

```cpp
#pragma once

#include "../CPU/CPUThread.h"
#include "../CPU/Hypervisor.h"
#include "../Memory/vm_ptr.h"
#include "Utilities/lockless.h"
#include "Utilities/BitField.h"

#include "util/logs.hpp"
#include "util/v128.hpp"

LOG_CHANNEL(ppu_log, "PPU");

enum class ppu_cmd : u32
{
	null,

	opcode, // Execute PPU instruction from arg
	set_gpr, // Set gpr[arg] (+1 cmd)
	set_args, // Set general-purpose args (+arg cmd)
	lle_call, // Load addr and rtoc at *arg or *gpr[arg] and execute
	hle_call, // Execute function by index (arg)
	ptr_call, // Execute function by pointer
	opd_call, // Execute function by provided rtoc and address (unlike lle_call, does not read memory)
	cia_call, // Execute from current CIA, mo GPR modification applied
	entry_call, // Load addr and rtoc from entry_func
	initialize, // ppu_initialize()
	sleep,
	reset_stack, // resets stack address
};

enum class ppu_join_status : u32
{
	joinable = 0,
	detached = 1,
	zombie = 2,
	exited = 3,
	max = 4, // Values above it indicate PPU id of joining thread
};

enum ppu_thread_status : u32
{
	PPU_THREAD_STATUS_IDLE,
	PPU_THREAD_STATUS_RUNNABLE,
	PPU_THREAD_STATUS_ONPROC,
	PPU_THREAD_STATUS_SLEEP,
	PPU_THREAD_STATUS_STOP,
	PPU_THREAD_STATUS_ZOMBIE,
	PPU_THREAD_STATUS_DELETED,
	PPU_THREAD_STATUS_UNKNOWN,
};

// Formatting helper
enum class ppu_syscall_code : u64
{
};

enum : u32
{
	ppu_stack_start_offset = 0x70,
};

// ppu function descriptor
struct ppu_func_opd_t
{
	be_t<u32> addr;
	be_t<u32> rtoc;
};

// ppu_thread constructor argument
struct ppu_thread_params
{
	vm::addr_t stack_addr;
	u32 stack_size;
	u32 tls_addr;
	ppu_func_opd_t entry;
	u64 arg0;
	u64 arg1;
};

```

## 🔗 依赖头文件

- `#include "../CPU/CPUThread.h"`
- `#include "../CPU/Hypervisor.h"`
- `#include "../Memory/vm_ptr.h"`
- `#include "Utilities/lockless.h"`
- `#include "Utilities/BitField.h"`
- `#include "util/logs.hpp"`
- `#include "util/v128.hpp"`
