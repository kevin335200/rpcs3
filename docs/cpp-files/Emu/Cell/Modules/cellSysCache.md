# cellSysCache.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellSysCache.cpp`
- **类型**: 源文件
- **行数**: 268 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `syscache_info`

### HLE 函数

- `cellSysCacheClear()`
- `cellSysCacheMount()`
- `cellSysutil_SysCache_init()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/System.h"
#include "Emu/system_utils.hpp"
#include "Emu/VFS.h"
#include "Emu/IdManager.h"
#include "Emu/Cell/PPUModule.h"

#include "Emu/Cell/lv2/sys_fs.h"
#include "cellSysutil.h"
#include "util/init_mutex.hpp"
#include "Utilities/StrUtil.h"

LOG_CHANNEL(cellSysutil);

template<>
void fmt_class_string<CellSysCacheError>::format(std::string& out, u64 arg)
{
	format_enum(out, arg, [](auto error)
	{
		switch (error)
		{
			STR_CASE(CELL_SYSCACHE_ERROR_ACCESS_ERROR);
			STR_CASE(CELL_SYSCACHE_ERROR_INTERNAL);
			STR_CASE(CELL_SYSCACHE_ERROR_NOTMOUNTED);
			STR_CASE(CELL_SYSCACHE_ERROR_PARAM);
		}

		return unknown;
	});
}

extern lv2_fs_mount_point g_mp_sys_dev_hdd1;

extern std::string get_syscache_state_corruption_indicator_file_path(std::string_view dir_path);

struct syscache_info
{
	const std::string cache_root = rpcs3::utils::get_hdd1_dir() + "/caches/";

	stx::init_mutex init;

	std::string cache_id;

	bool retain_caches = false;

	syscache_info() noexcept
	{
		// Check if dev_hdd1 is mounted by parent process
		if (!Emu.hdd1.empty())
		{
			const auto lock = init.init();

			// Extract cache id from path
			std::string_view id = Emu.hdd1;
			id = id.substr(0, id.find_last_not_of(fs::delim) + 1);
			id = id.substr(id.find_last_of(fs::delim) + 1);
			cache_id = std::string{id};

			if (!Emu.DeserialManager() && !fs::write_file<true>(get_syscache_state_corruption_indicator_file_path(Emu.hdd1), fs::write_new))
			{
				fmt::throw_exception("Failed to create HDD1 corruption indicator file! (path='%s', reason='%s')", Emu.hdd1, fs::g_tls_error);
			}

			cellSysutil.success("Retained cache from parent process: %s", Emu.hdd1);
			return;
		}

		// Find existing cache at startup
		const std::string prefix = Emu.GetTitleID() + '_';

		for (auto&& entry : fs::dir(cache_root))
		{
			if (entry.is_directory && entry.name.starts_with(prefix))
			{
				cache_id = vfs::unescape(entry.name);

				if (fs::is_file(get_syscache_state_corruption_indicator_file_path(cache_root + '/' + cache_id)))
				{
					// State is not complete
					clear(true);
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/System.h"`
- `#include "Emu/system_utils.hpp"`
- `#include "Emu/VFS.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Emu/Cell/lv2/sys_fs.h"`
- `#include "cellSysutil.h"`
- `#include "util/init_mutex.hpp"`
- `#include "Utilities/StrUtil.h"`
