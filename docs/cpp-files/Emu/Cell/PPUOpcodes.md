# PPUOpcodes.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/PPUOpcodes.h`
- **类型**: 头文件
- **行数**: 744 行

## 🎯 功能概述

PowerPC Processing Unit (PPU) 相关实现。

## 📋 主要内容

### 类/结构体

- `instruction_info`
- `ppu_decoder`

### 关键函数

- `ADDIS()`
- `BCCTR()`
- `BCTRL()`
- `CMPWI()`
- `MFCTR()`
- `MR()`
- `NOP()`
- `RLDICR()`
- `STD()`
- `STDU()`
- `STVX()`
- `TRAP()`
- `_first()`
- `fill_table()`
- `ppu_rotate_mask()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/BitField.h"

template<typename T, u32 I, u32 N> using ppu_bf_t = bf_t<T, sizeof(T) * 8 - N - I, N>;

union ppu_opcode_t
{
	u32 opcode;

	ppu_bf_t<u32, 0, 6> main; // 0..5
	cf_t<ppu_bf_t<u32, 30, 1>, ppu_bf_t<u32, 16, 5>> sh64; // 30 + 16..20
	cf_t<ppu_bf_t<u32, 26, 1>, ppu_bf_t<u32, 21, 5>> mbe64; // 26 + 21..25
	ppu_bf_t<u32, 11, 5> vuimm; // 11..15
	ppu_bf_t<u32, 6, 5> vs; // 6..10
	ppu_bf_t<u32, 22, 4> vsh; // 22..25
	ppu_bf_t<u32, 21, 1> oe; // 21
	ppu_bf_t<u32, 11, 10> spr; // 11..20
	ppu_bf_t<u32, 21, 5> vc; // 21..25
	ppu_bf_t<u32, 16, 5> vb; // 16..20
	ppu_bf_t<u32, 11, 5> va; // 11..15
	ppu_bf_t<u32, 6, 5> vd; // 6..10
	ppu_bf_t<u32, 31, 1> lk; // 31
	ppu_bf_t<u32, 30, 1> aa; // 30
	ppu_bf_t<u32, 16, 5> rb; // 16..20
	ppu_bf_t<u32, 11, 5> ra; // 11..15
	ppu_bf_t<u32, 6, 5> rd; // 6..10
	ppu_bf_t<u32, 16, 16> uimm16; // 16..31
	ppu_bf_t<u32, 11, 1> l11; // 11
	ppu_bf_t<u32, 6, 5> rs; // 6..10
	ppu_bf_t<s32, 16, 16> simm16; // 16..31, signed
	ppu_bf_t<s32, 16, 14> ds; // 16..29, signed
	ppu_bf_t<s32, 11, 5> vsimm; // 11..15, signed
	ppu_bf_t<s32, 6, 26> ll; // 6..31, signed
	ppu_bf_t<s32, 6, 24> li; // 6..29, signed
	ppu_bf_t<u32, 20, 7> lev; // 20..26
	ppu_bf_t<u32, 16, 4> i; // 16..19
	ppu_bf_t<u32, 11, 3> crfs; // 11..13
	ppu_bf_t<u32, 10, 1> l10; // 10
	ppu_bf_t<u32, 6, 3> crfd; // 6..8
	ppu_bf_t<u32, 16, 5> crbb; // 16..20
	ppu_bf_t<u32, 11, 5> crba; // 11..15
	ppu_bf_t<u32, 6, 5> crbd; // 6..10
	ppu_bf_t<u32, 31, 1> rc; // 31
	ppu_bf_t<u32, 26, 5> me32; // 26..30
	ppu_bf_t<u32, 21, 5> mb32; // 21..25
	ppu_bf_t<u32, 16, 5> sh32; // 16..20
	ppu_bf_t<u32, 11, 5> bi; // 11..15
	ppu_bf_t<u32, 6, 5> bo; // 6..10
	ppu_bf_t<u32, 19, 2> bh; // 19..20
	ppu_bf_t<u32, 21, 5> frc; // 21..25
	ppu_bf_t<u32, 16, 5> frb; // 16..20
	ppu_bf_t<u32, 11, 5> fra; // 11..15
	ppu_bf_t<u32, 6, 5> frd; // 6..10
	ppu_bf_t<u32, 12, 8> crm; // 12..19
	ppu_bf_t<u32, 6, 5> frs; // 6..10
	ppu_bf_t<u32, 7, 8> flm; // 7..14
	ppu_bf_t<u32, 6, 1> l6; // 6
	ppu_bf_t<u32, 15, 1> l15; // 15
	cf_t<ppu_bf_t<s32, 16, 14>, ff_t<u32, 0, 2>> bt14;
	cf_t<ppu_bf_t<s32, 6, 24>, ff_t<u32, 0, 2>> bt24;
};

constexpr u64 ppu_rotate_mask(u32 mb, u32 me)
{
	const u64 mask = ~0ull << (~(me - mb) & 63);
	return (mask >> (mb & 63)) | (mask << ((64 - mb) & 63));
}

constexpr u32 ppu_decode(u32 inst)
{
	return ((inst >> 26) | (inst << 6)) & 0x1ffff; // Rotate + mask
}

std::array<u32, 2> op_branch_targets(u32 pc, ppu_opcode_t op);

// PPU decoder object. D provides functions. T is function pointer type returned.
template <typename D, typename T = decltype(&D::UNK)>
class ppu_decoder
{
```

## 🔗 依赖头文件

- `#include "Utilities/BitField.h"`
