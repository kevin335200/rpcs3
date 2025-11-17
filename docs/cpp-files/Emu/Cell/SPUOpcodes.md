# SPUOpcodes.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/SPUOpcodes.h`
- **类型**: 头文件
- **行数**: 317 行

## 🎯 功能概述

Synergistic Processing Unit (SPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `instruction_info`
- `spu_decoder`

### 关键函数

- `_first()`
- `decode()`
- `op_branch_targets()`
- `spu_branch_target()`
- `spu_decode()`
- `spu_ls_target()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/BitField.h"

union spu_opcode_t
{
	u32 opcode;

	bf_t<u32, 0, 7> rt; // 25..31, for 3-op instructions
	bf_t<u32, 0, 7> rc; // 25..31
	bf_t<u32, 7, 7> ra; // 18..24
	bf_t<u32, 14, 7> rb; // 11..17
	bf_t<u32, 21, 7> rt4; // 4..10, for 4-op instructions
	bf_t<u32, 18, 1> e; // 13, "enable interrupts" bit
	bf_t<u32, 19, 1> d; // 12, "disable interrupts" bit
	bf_t<u32, 18, 2> de; // 12..13 combined 'e' and 'd' bits
	bf_t<u32, 20, 1> c; // 11, "C" bit for SYNC instruction
	bf_t<s32, 23, 2> r0h; // 7..8, signed
	bf_t<s32, 14, 2> roh; // 16..17, signed
	bf_t<u32, 14, 7> i7; // 11..17
	bf_t<s32, 14, 7> si7; // 11..17, signed
	bf_t<u32, 14, 8> i8; // 10..17
	bf_t<s32, 14, 10> si10; // 8..17, signed
	bf_t<u32, 7, 16> i16; // 9..24
	bf_t<s32, 7, 16> si16; // 9..24, signed
	bf_t<u32, 7, 18> i18; // 7..24
};

constexpr u32 spu_branch_target(u32 pc, u32 imm = 0)
{
	return (pc + (imm << 2)) & 0x3fffc;
}

constexpr u32 spu_ls_target(u32 pc, u32 imm = 0)
{
	return (pc + (imm << 2)) & 0x3fff0;
}

constexpr u32 spu_decode(u32 inst)
{
	return inst >> 21;
}

std::array<u32, 2> op_branch_targets(u32 pc, spu_opcode_t op);

// SPU decoder object. D provides functions. T is function pointer type returned.
template <typename D, typename T = decltype(&D::UNK)>
class spu_decoder
{
	// Fast lookup table
	std::array<T, 2048> m_table{};

	struct instruction_info
	{
		u32 magn; // Count = 2 ^ magn
		u32 value;
		T pointer;

		instruction_info(u32 m, u32 v, T p) noexcept
			: magn(m)
			, value(v)
			, pointer(p)
		{
		}

		instruction_info(u32 m, u32 v, const T* p) noexcept
			: magn(m)
			, value(v)
			, pointer(*p)
		{
		}
	};

	// Helper
	static const D& _first(const D& arg)
	{
		return arg;
	}

public:
```

## 🔗 依赖头文件

- `#include "Utilities/BitField.h"`
