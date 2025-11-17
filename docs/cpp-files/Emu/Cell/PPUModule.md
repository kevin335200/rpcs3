# PPUModule.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUModule.h`
- **类型**: 头文件
- **行数**: 332 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `ppu_module_manager`
- `ppu_static_function`
- `ppu_static_module`
- `ppu_static_variable`
- `registered`

### 关键函数

- `access_static_function()`
- `access_static_variable()`
- `add_init_func()`
- `find_static_function()`
- `flag()`
- `get()`
- `get_module()`
- `initialize()`
- `initialize_modules()`
- `ppu_generate_id()`
- `ppu_select_name()`
- `register_module()`
- `register_static_function()`
- `register_static_variable()`

## 💻 代码片段

```cpp
#pragma once

#include "PPUFunction.h"
#include "PPUCallback.h"
#include "ErrorCodes.h"
#include "Emu/Memory/vm_var.h"

// Helper function
constexpr const char* ppu_select_name(const char* name, u32 /*id*/)
{
	return name;
}

// Helper function
constexpr const char* ppu_select_name(const char* /*name*/, const char* orig_name)
{
	return orig_name;
}

// Generate FNID or VNID for given name
extern u32 ppu_generate_id(std::string_view name);

// Overload for REG_FNID, REG_VNID macro
constexpr u32 ppu_generate_id(u32 id)
{
	return id;
}

// Flags set with REG_FUNC
enum ppu_static_module_flags : u32
{
	MFF_FORCED_HLE = (1 << 0), // Always call HLE function
	MFF_PERFECT    = (1 << 1), // Indicates complete implementation and LLE interchangeability
	MFF_HIDDEN     = (1 << 2), // Invisible variable for internal use (TODO)
};

// HLE function information
struct ppu_static_function
{
	const char* name;
	u32 index; // Index for ppu_function_manager
	u32 flags;
	std::vector<const char*> args; // Arg names
	const u32* export_addr;

	ppu_static_function& flag(ppu_static_module_flags value)
	{
		flags |= value;
		return *this;
	}
};

// HLE variable information
struct ppu_static_variable
{
	const char* name;
	u32* var; // Pointer to variable address storage
	void(*init)(); // Variable initialization function
	u32 size;
	u32 align;
	u32 flags;
	u32 addr;
	const u32* export_addr;

	ppu_static_variable& flag(ppu_static_module_flags value)
	{
		flags |= value;
		return *this;
	}
};

// HLE module information
class ppu_static_module final
{
	std::vector<void(*)(ppu_static_module*)> m_on_init;

public:
	const std::string name;

	std::unordered_map<u32, ppu_static_function, value_hash<u32>> functions{};
```

## 🔗 依赖头文件

- `#include "PPUFunction.h"`
- `#include "PPUCallback.h"`
- `#include "ErrorCodes.h"`
- `#include "Emu/Memory/vm_var.h"`
