# sys_game_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_game_.cpp`
- **类型**: 源文件
- **行数**: 215 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_game_board_storage_read()`
- `sys_game_board_storage_write()`
- `sys_game_get_rtc_status()`
- `sys_game_get_system_sw_version()`
- `sys_game_get_temperature()`
- `sys_game_process_exitspawn()`
- `sys_game_process_exitspawn2()`
- `sys_game_watchdog_clear()`
- `sys_game_watchdog_start()`
- `sys_game_watchdog_stop()`
- `sys_mutex_lock()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_mutex.h"
#include "Emu/Cell/lv2/sys_process.h"
#include "sysPrxForUser.h"

LOG_CHANNEL(sysPrxForUser);

extern vm::gvar<u32> g_ppu_exit_mutex;
extern vm::gvar<vm::ptr<void()>> g_ppu_atexitspawn;
extern vm::gvar<vm::ptr<void()>> g_ppu_at_Exitspawn;

static u32 get_string_array_size(vm::cpptr<char> list, u32& out_count)
{
	//out_count = 0;
	u32 result = 8;

	for (u32 i = 0; list; i++)
	{
		if (const vm::cptr<char> str = list[i])
		{
			out_count++;
			result += ((static_cast<u32>(std::strlen(str.get_ptr())) + 0x10) & -0x10) + 8;
			continue;
		}
		break;
	}

	return result;
}

static u32 get_exitspawn_size(vm::cptr<char> path, vm::cpptr<char> argv, vm::cpptr<char> envp, u32& arg_count, u32& env_count)
{
	arg_count = 1;
	env_count = 0;

	u32 result = ((static_cast<u32>(std::strlen(path.get_ptr())) + 0x10) & -0x10) + 8;
	result += get_string_array_size(argv, arg_count);
	result += get_string_array_size(envp, env_count);

	if ((arg_count + env_count) % 2)
	{
		result += 8;
	}

	return result;
}

static void put_string_array(vm::pptr<char, u32, u64> pstr, vm::ptr<char>& str, u32 count, vm::cpptr<char> list)
{
	for (u32 i = 0; i < count; i++)
	{
		const u32 len = static_cast<u32>(std::strlen(list[i].get_ptr()));
		std::memcpy(str.get_ptr(), list[i].get_ptr(), len + 1);
		pstr[i] = str;
		str += (len + 0x10) & -0x10;
	}

	pstr[count] = vm::null;
}

static void put_exitspawn(vm::ptr<void> out, vm::cptr<char> path, u32 argc, vm::cpptr<char> argv, u32 envc, vm::cpptr<char> envp)
{
	vm::pptr<char, u32, u64> pstr = vm::cast(out.addr());
	vm::ptr<char> str = vm::static_ptr_cast<char>(out) + (argc + envc + (argc + envc) % 2) * 8 + 0x10;

	const u32 len = static_cast<u32>(std::strlen(path.get_ptr()));
	std::memcpy(str.get_ptr(), path.get_ptr(), len + 1);
	*pstr++ = str;
	str += (len + 0x10) & -0x10;

	put_string_array(pstr, str, argc - 1, argv);
	put_string_array(pstr + argc, str, envc, envp);
}

static void exitspawn(ppu_thread& ppu, vm::cptr<char> path, vm::cpptr<char> argv, vm::cpptr<char> envp, u32 data, u32 data_size, s32 prio, u64 _flags)
{
	sys_mutex_lock(ppu, *g_ppu_exit_mutex, 0);

```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_mutex.h"`
- `#include "Emu/Cell/lv2/sys_process.h"`
- `#include "sysPrxForUser.h"`
