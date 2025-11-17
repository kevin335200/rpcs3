# cellMusicSelectionContext.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellMusicSelectionContext.cpp`
- **类型**: 源文件
- **行数**: 371 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "cellMusic.h"
#include "util/yaml.hpp"
#include "Emu/VFS.h"

#include <random>

// This is just a helper and not a real cell entity

LOG_CHANNEL(cellMusicSelectionContext);

bool music_selection_context::set(const CellMusicSelectionContext& in)
{
	if (memcmp(in.data, magic, sizeof(magic)) != 0)
	{
		return false;
	}

	constexpr u32 pos = sizeof(magic);
	hash = &in.data[pos];

	return load_playlist();
}

CellMusicSelectionContext music_selection_context::get() const
{
	if (hash.size() + sizeof(magic) > CELL_MUSIC_SELECTION_CONTEXT_SIZE)
	{
		fmt::throw_exception("Contents of music_selection_context are too large");
	}

	CellMusicSelectionContext out{};
	u32 pos = 0;

	std::memset(out.data, 0, CELL_MUSIC_SELECTION_CONTEXT_SIZE);
	std::memcpy(out.data, magic, sizeof(magic));
	pos += sizeof(magic);
	std::memcpy(&out.data[pos], hash.c_str(), hash.size());

	return out;
}

std::string music_selection_context::to_string() const
{
	std::string str = fmt::format(".magic='%s', .content_type=%d, .repeat_mode=%d, .context_option=%d, .first_track=%d, .tracks=%d, .hash='%s', .playlist:",
		magic, static_cast<u32>(content_type), static_cast<u32>(repeat_mode), static_cast<u32>(context_option), first_track, playlist.size(), hash);

	for (usz i = 0; i < playlist.size(); i++)
	{
		fmt::append(str, "\n - Track %d: %s", i, ::at32(playlist, i));
	}

	return str;
}

std::string music_selection_context::get_next_hash()
{
	static u64 hash_counter = 0;
	return fmt::format("music_selection_context_%d", hash_counter++);
}

std::string music_selection_context::context_to_hex(const CellMusicSelectionContext& context)
{
	std::string dahex;

	for (usz i = 0; i < CELL_MUSIC_SELECTION_CONTEXT_SIZE; i++)
	{
		fmt::append(dahex, " %.2x", context.data[i]);
	}

	return dahex;
}

std::string music_selection_context::get_yaml_path() const
{
	std::string path = fs::get_cache_dir() + "cache/playlists/";

	if (!fs::create_path(path))
	{
		cellMusicSelectionContext.fatal("get_yaml_path: Failed to create path: %s (%s)", path, fs::g_tls_error);
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "cellMusic.h"`
- `#include "util/yaml.hpp"`
- `#include "Emu/VFS.h"`
- `#include <random>`
