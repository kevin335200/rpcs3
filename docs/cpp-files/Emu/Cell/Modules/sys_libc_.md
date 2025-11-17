# sys_libc_.cpp

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_libc_.cpp`
- **类型**: 源文件
- **行数**: 501 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `ps3_fmt_src`

### 系统调用

- `sys_tty_write()`

## 💻 代码片段

```cpp
#include "stdafx.h"
#include "Emu/Cell/lv2/sys_tty.h"
#include "Emu/Cell/PPUModule.h"
#include "Utilities/cfmt.h"

LOG_CHANNEL(sysPrxForUser);

// cfmt implementation (TODO)

using qsortcmp = s32(vm::cptr<void> e1, vm::cptr<void> e2);

struct ps3_fmt_src
{
	ppu_thread* ctx;
	u32 g_count;

	static bool test(usz)
	{
		return true;
	}

	template <typename T>
	T get(usz index) const
	{
		const u32 i = static_cast<u32>(index) + g_count;
		return ppu_gpr_cast<T>(i < 8 ? ctx->gpr[3 + i] : +*ctx->get_stack_arg(i));
	}

	void skip(usz extra)
	{
		g_count += static_cast<u32>(extra) + 1;
	}

	usz fmt_string(std::string& out, usz extra) const
	{
		const usz start = out.size();
		out += vm::_ptr<const char>(get<u32>(extra));
		return out.size() - start;
	}

	static usz type(usz)
	{
		return 0;
	}

	static constexpr usz size_char  = 1;
	static constexpr usz size_short = 2;
	static constexpr usz size_int   = 4;
	static constexpr usz size_long  = 4;
	static constexpr usz size_llong = 8;
	static constexpr usz size_size  = 4;
	static constexpr usz size_max   = 8;
	static constexpr usz size_diff  = 4;
};

template <>
f64 ps3_fmt_src::get<f64>(usz index) const
{
	return std::bit_cast<f64>(get<u64>(index));
}

static std::string ps3_fmt(ppu_thread& context, vm::cptr<char> fmt, u32 g_count)
{
	std::string result;

	cfmt_append(result, fmt.get_ptr(), ps3_fmt_src{&context, g_count});

	return result;
}

static const std::array<s16, 129> s_ctype_table
{
	0,
	0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x408,
	8, 8, 8, 8,
	0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
	0x18,
	0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10,
	4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
	0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10,
```

## 🔗 依赖头文件

- `#include "stdafx.h"`
- `#include "Emu/Cell/lv2/sys_tty.h"`
- `#include "Emu/Cell/PPUModule.h"`
- `#include "Utilities/cfmt.h"`
