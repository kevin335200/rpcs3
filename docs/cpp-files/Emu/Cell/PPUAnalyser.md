# PPUAnalyser.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUAnalyser.h`
- **类型**: 头文件
- **行数**: 1,427 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `main_ppu_module`
- `ppu_function`
- `ppu_iname`
- `ppu_itype`
- `ppu_module`
- `ppu_pattern`
- `ppu_pattern_array`
- `ppu_pattern_matrix`
- `ppu_reloc`
- `ppu_segment`

### 关键函数

- `analyse()`
- `as_span()`
- `copy_part()`
- `get_funcs()`
- `get_ptr()`
- `get_ref()`
- `get_relocs()`
- `save()`
- `validate()`

## 💻 代码片段

```cpp
#pragma once

#include <string>
#include <map>
#include <deque>
#include <span>
#include "util/types.hpp"
#include "util/asm.hpp"
#include "util/to_endian.hpp"

#include "Utilities/bit_set.h"
#include "PPUOpcodes.h"

// PPU Function Attributes
enum class ppu_attr : u8
{
	known_size,
	no_return,
	no_size,
	has_mfvscr,

	__bitset_enum_max
};

// PPU Function Information
struct ppu_function
{
	u32 addr = 0;
	u32 toc = 0;
	u32 size = 0;

	std::map<u32, u32> blocks{}; // Basic blocks: addr -> size

	struct iterator
	{
		const ppu_function* _this;
		typename std::map<u32, u32>::const_iterator it;
		usz index = 0;

		std::pair<const u32, u32> operator*() const
		{
			return _this->blocks.empty() ? std::pair<const u32, u32>(_this->addr, _this->size) : *it;
		}

		iterator& operator++()
		{
			index++;

			if (it != _this->blocks.end())
			{
				it++;
			}

			return *this;
		}

		bool operator==(const iterator& rhs) const noexcept
		{
			return it == rhs.it || (rhs.index == index && _this->blocks.empty());
		}

		bool operator!=(const iterator& rhs) const noexcept
		{
			return !operator==(rhs);
		}
	};

	iterator begin() const
	{
		return iterator{this, blocks.begin()};
	}

	iterator end() const
	{
		return iterator{this, blocks.end(), 1};
	}
};

// PPU Relocation Information
struct ppu_reloc
```

## 🔗 依赖头文件

- `#include <string>`
- `#include <map>`
- `#include <deque>`
- `#include <span>`
- `#include "util/types.hpp"`
- `#include "util/asm.hpp"`
- `#include "util/to_endian.hpp"`
- `#include "Utilities/bit_set.h"`
- `#include "PPUOpcodes.h"`
