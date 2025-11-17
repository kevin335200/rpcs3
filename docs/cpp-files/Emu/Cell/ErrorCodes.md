# ErrorCodes.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/ErrorCodes.h`
- **类型**: 头文件
- **行数**: 166 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `error_code`
- `message`
- `ppu_gpr_cast_impl`

### 关键函数

- `error_report()`
- `from()`
- `requires()`
- `s32()`
- `to()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"
#include "Utilities/StrFmt.h"

namespace logs
{
	struct message;
}

// Error code type (return type), implements error reporting.
class error_code
{
	s32 value;

	// Common constructor
	template <typename ET> requires requires (ET v) { static_cast<s32>(v); }
	error_code(const logs::message* ch, const ET& value) noexcept
		: value(error_report(static_cast<s32>(value), ch, " : %s", fmt::type_info_v<ET>, fmt_args_t<ET>{fmt_unveil<ET>::get(value)}))
	{
	}

	// Error constructor (2 args)
	template <typename ET, typename T> requires requires (ET v) { static_cast<s32>(v); }
	error_code(const logs::message* ch, const ET& value, const T& arg) noexcept
		: value(error_report(static_cast<s32>(value), ch, " : %s, %s", fmt::type_info_v<ET, T>, fmt_args_t<ET, T>{fmt_unveil<ET>::get(value), fmt_unveil<T>::get(arg)}))
	{
	}

	// Formatting constructor (error, format string, variadic list)
	template <typename ET, typename... Args> requires requires (ET v) { static_cast<s32>(v); }
	error_code(const logs::message* ch, const ET& value, const const_str& fmt, const Args&... args) noexcept
		: value(error_report(static_cast<s32>(value), ch, fmt, fmt::type_info_v<Args...>, fmt_args_t<Args...>{fmt_unveil<Args>::get(args)...}))
	{
	}

public:
	// Implementation must be provided independently
	static s32 error_report(s32 result, const logs::message* channel, const char* fmt, const fmt_type_info* sup, const u64* args);

	error_code() = default;

	// Constructor without channel
	template <typename... Args> requires (sizeof...(Args) > 0 && !(std::is_same_v<std::decay_t<std::remove_pointer_t<Args>>, logs::message> || ...))
	error_code(const Args&... args) noexcept
		: error_code(std::add_pointer_t<const logs::message>{}, args...)
	{
	}

	// Constructor with channel
	template <typename... Args>
	error_code(const logs::message& ch, const Args&... args) noexcept
		: error_code(std::addressof(ch), args...)
	{
	}

	operator s32() const
	{
		return value;
	}

	ENABLE_BITWISE_SERIALIZATION;
};

enum CellNotAnError : s32
{
	CELL_OK     = 0,
	CELL_CANCEL = 1,
};

// Constructor specialization that doesn't trigger reporting
template <>
constexpr FORCE_INLINE error_code::error_code(const CellNotAnError& value) noexcept
	: value(value)
{
}

// Helper function for error_code
template <typename T>
constexpr FORCE_INLINE CellNotAnError not_an_error(const T& value)
```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
- `#include "Utilities/StrFmt.h"`
