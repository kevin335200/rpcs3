# SPURecompiler.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPURecompiler.h`
- **类型**: 头文件
- **行数**: 459 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `block_info`
- `func_info`
- `pattern_info`
- `precompile_data_t`
- `reg_state_t`
- `spu_cache`
- `spu_item`
- `spu_program`
- `spu_recompiler_base`
- `spu_runtime`

### 关键函数

- `alloc_tag()`
- `analyse()`
- `dispatch()`
- `dump()`
- `get_known_ones()`
- `get_known_zeroes()`
- `init()`
- `is_const()`
- `is_less_than()`
- `make_asmjit_recompiler()`
- `make_branch_patchpoint()`
- `make_fast_llvm_recompiler()`
- `merge()`
- `old_interpreter()`
- `unequal_with_mask_indifference()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/File.h"
#include "Utilities/lockless.h"
#include "Utilities/address_range.h"
#include "SPUThread.h"
#include <vector>
#include <bitset>
#include <memory>
#include <string>
#include <deque>

// Helper class
class spu_cache
{
	fs::file m_file;

public:
	spu_cache() = default;

	spu_cache(const std::string& loc);

	spu_cache(spu_cache&&) noexcept = default;

	spu_cache& operator=(spu_cache&&) noexcept = default;

	~spu_cache();

	operator bool() const
	{
		return m_file.operator bool();
	}

	std::deque<struct spu_program> get();

	void add(const struct spu_program& func);

	static void initialize(bool build_existing_cache = true);

	struct precompile_data_t
	{
		u32 vaddr;
		std::vector<u32> inst_data;
		std::vector<u32> funcs;
	};

	bool collect_funcs_to_precompile = true;

	lf_queue<precompile_data_t> precompile_funcs;
};

struct spu_program
{
	// Address of the entry point in LS
	u32 entry_point;

	// Address of the data in LS
	u32 lower_bound;

	// Program data with intentionally wrong endianness (on LE platform opcode values are swapped)
	std::vector<u32> data;

	bool operator==(const spu_program& rhs) const noexcept;

	bool operator<(const spu_program& rhs) const noexcept;
};

class spu_item
{
public:
	// SPU program
	const spu_program data;

	// Compiled function pointer
	atomic_t<spu_function_t> compiled = nullptr;

	// Ubertrampoline generated for this item when it was latest
	atomic_t<spu_function_t> trampoline = nullptr;

	atomic_t<u8> cached = false;
```

## 🔗 依赖头文件

- `#include "Utilities/File.h"`
- `#include "Utilities/lockless.h"`
- `#include "Utilities/address_range.h"`
- `#include "SPUThread.h"`
- `#include <vector>`
- `#include <bitset>`
- `#include <memory>`
- `#include <string>`
- `#include <deque>`
