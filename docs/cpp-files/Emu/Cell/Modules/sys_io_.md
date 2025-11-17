# sys_io_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_io_.cpp`
- **类型**: 源文件
- **行数**: 252 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `libio_sys_config`

### 系统调用

- `sys_config_add_service_listener()`
- `sys_config_register_io_error_handler()`
- `sys_config_register_service()`
- `sys_config_remove_service_listener()`
- `sys_config_start()`
- `sys_config_stop()`
- `sys_config_unregister_io_error_handler()`
- `sys_config_unregister_service()`
- `sys_event_queue_create()`
- `sys_event_queue_destroy()`
- `sys_event_queue_receive()`
- `sys_io_serialize()`
- `sys_ppu_thread_join()`

### HLE 函数

- `cellKb_init()`
- `cellMouse_init()`
- `cellPad_NotifyStateChange()`
- `cellPad_init()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/System.h"
#include "Emu/IdManager.h"
#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_event.h"
#include "Emu/Cell/lv2/sys_ppu_thread.h"
#include "Emu/Cell/Modules/sysPrxForUser.h"

LOG_CHANNEL(sys_io);

extern void cellPad_init();
extern void cellKb_init();
extern void cellMouse_init();

struct libio_sys_config
{
	shared_mutex mtx;
	s32 init_ctr = 0;
	u32 ppu_id = 0;
	u32 queue_id = 0;

	~libio_sys_config() noexcept
	{
	}

	void save_or_load(utils::serial& ar)
	{
		ar(init_ctr, ppu_id, queue_id);
	}
};

extern void sys_io_serialize(utils::serial& ar)
{
	// Do not assign a serialization tag for now, call it from cellPad serialization
	ensure(g_fxo->try_get<libio_sys_config>())->save_or_load(ar);
}

extern bool cellPad_NotifyStateChange(usz index, u64 state, bool lock = true, bool is_blocking = true);

void config_event_entry(ppu_thread& ppu)
{
	ppu.state += cpu_flag::wait;

	auto& cfg = *ensure(g_fxo->try_get<libio_sys_config>());

	if (!ppu.loaded_from_savestate)
	{
		// Ensure awake
		ppu.check_state();
	}

	const u32 queue_id = cfg.queue_id;
	auto queue = idm::get_unlocked<lv2_obj, lv2_event_queue>(queue_id);

	while (queue && sys_event_queue_receive(ppu, queue_id, vm::null, 0) == CELL_OK)
	{
		if (ppu.is_stopped())
		{
			ppu.state += cpu_flag::again;
			return;
		}

		// Some delay
		thread_ctrl::wait_for(10000);

		// Wakeup
		ppu.check_state();
		ppu.state += cpu_flag::wait;

		const u64 arg1 = ppu.gpr[5];
		const u64 arg2 = ppu.gpr[6];
		const u64 arg3 = ppu.gpr[7];

		// TODO: Reverse-engineer proper event system

		if (arg1 == 1)
		{
			while (!cellPad_NotifyStateChange(arg2, arg3, false))
			{
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/System.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_event.h"`
- `#include "Emu/Cell/lv2/sys_ppu_thread.h"`
- `#include "Emu/Cell/Modules/sysPrxForUser.h"`
