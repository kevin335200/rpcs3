# sys_ppu_thread_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_ppu_thread_.cpp`
- **类型**: 源文件
- **行数**: 287 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_initialize_tls()`
- `sys_interrupt_thread_disestablish()`
- `sys_lwmutex_create()`
- `sys_lwmutex_lock()`
- `sys_lwmutex_unlock()`
- `sys_mutex_create()`
- `sys_mutex_lock()`
- `sys_mutex_unlock()`
- `sys_ppu_thread_create()`
- `sys_ppu_thread_exit()`
- `sys_ppu_thread_get_id()`
- `sys_ppu_thread_once()`
- `sys_ppu_thread_register_atexit()`
- `sys_ppu_thread_start()`
- `sys_ppu_thread_unregister_atexit()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"
#include "Emu/Cell/lv2/sys_ppu_thread.h"
#include "Emu/Cell/lv2/sys_interrupt.h"
#include "Emu/Cell/lv2/sys_lwmutex.h"
#include "Emu/Cell/lv2/sys_mutex.h"
#include "sysPrxForUser.h"

LOG_CHANNEL(sysPrxForUser);

vm::gvar<sys_lwmutex_t> g_ppu_atexit_lwm;
vm::gvar<vm::ptr<void()>[8]> g_ppu_atexit;
vm::gvar<u32> g_ppu_exit_mutex; // sys_process_exit2 mutex
vm::gvar<u32> g_ppu_once_mutex;
vm::gvar<sys_lwmutex_t> g_ppu_prx_lwm;

static u32 s_tls_addr = 0; // TLS image address
static u32 s_tls_file = 0; // TLS image size
static u32 s_tls_zero = 0; // TLS zeroed area size (TLS mem size - TLS image size)
static u32 s_tls_size = 0; // Size of TLS area per thread
static u32 s_tls_area = 0; // Start of TLS memory area
static u32 s_tls_max = 0; // Max number of threads
static std::unique_ptr<atomic_t<bool>[]> s_tls_map; // I'd like to make it std::vector but it won't work

static u32 ppu_alloc_tls()
{
	u32 addr = 0;

	for (u32 i = 0; i < s_tls_max; i++)
	{
		if (!s_tls_map[i] && s_tls_map[i].exchange(true) == false)
		{
			// Default (small) TLS allocation
			addr = s_tls_area + i * s_tls_size;
			break;
		}
	}

	if (!addr)
	{
		// Alternative (big) TLS allocation
		addr = vm::alloc(s_tls_size, vm::main);
	}

	std::memset(vm::base(addr), 0, 0x30); // Clear system area (TODO)
	std::memcpy(vm::base(addr + 0x30), vm::base(s_tls_addr), s_tls_file); // Copy TLS image
	std::memset(vm::base(addr + 0x30 + s_tls_file), 0, s_tls_zero); // Clear the rest
	return addr;
}

static void ppu_free_tls(u32 addr)
{
	// Calculate TLS position
	const u32 i = (addr - s_tls_area) / s_tls_size;

	if (addr < s_tls_area || i >= s_tls_max || (addr - s_tls_area) % s_tls_size)
	{
		// Alternative TLS allocation detected
		ensure(vm::dealloc(addr, vm::main));
		return;
	}

	if (s_tls_map[i].exchange(false) == false)
	{
		sysPrxForUser.error("ppu_free_tls(0x%x): deallocation failed", addr);
		return;
	}
}

void sys_initialize_tls(ppu_thread& ppu, u64 main_thread_id, u32 tls_seg_addr, u32 tls_seg_size, u32 tls_mem_size)
{
	sysPrxForUser.notice("sys_initialize_tls(thread_id=0x%llx, addr=*0x%x, size=0x%x, mem_size=0x%x)", main_thread_id, tls_seg_addr, tls_seg_size, tls_mem_size);

	// Uninitialized TLS expected.
	if (ppu.gpr[13] != 0) return;

	// Initialize TLS memory
	s_tls_addr = tls_seg_addr;
	s_tls_file = tls_seg_size;
	s_tls_zero = tls_mem_size - tls_seg_size;
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_ppu_thread.h"`
- `#include "Emu/Cell/lv2/sys_interrupt.h"`
- `#include "Emu/Cell/lv2/sys_lwmutex.h"`
- `#include "Emu/Cell/lv2/sys_mutex.h"`
- `#include "sysPrxForUser.h"`
