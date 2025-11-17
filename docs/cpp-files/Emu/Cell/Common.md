# Common.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Common.h`
- **类型**: 头文件
- **行数**: 201 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 关键函数

- `fexpf()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"

// Floating-point rounding mode (for both PPU and SPU)
enum FPSCR_RN
{
	FPSCR_RN_NEAR = 0,
	FPSCR_RN_ZERO = 1,
	FPSCR_RN_PINF = 2,
	FPSCR_RN_MINF = 3,
};

// Get the exponent of a float
inline int fexpf(float x)
{
	return (std::bit_cast<u32>(x) >> 23) & 0xff;
}

constexpr u32 ppu_fres_mantissas[128] =
{
	0x007f0000,
	0x007d0800,
	0x007b1800,
	0x00793000,
	0x00775000,
	0x00757000,
	0x0073a000,
	0x0071e000,
	0x00700000,
	0x006e4000,
	0x006ca000,
	0x006ae000,
	0x00694000,
	0x00678000,
	0x00660000,
	0x00646000,
	0x0062c000,
	0x00614000,
	0x005fc000,
	0x005e4000,
	0x005cc000,
	0x005b4000,
	0x0059c000,
	0x00584000,
	0x00570000,
	0x00558000,
	0x00540000,
	0x0052c000,
	0x00518000,
	0x00500000,
	0x004ec000,
	0x004d8000,
	0x004c0000,
	0x004b0000,
	0x00498000,
	0x00488000,
	0x00474000,
	0x00460000,
	0x0044c000,
	0x00438000,
	0x00428000,
	0x00418000,
	0x00400000,
	0x003f0000,
	0x003e0000,
	0x003d0000,
	0x003bc000,
	0x003ac000,
	0x00398000,
	0x00388000,
	0x00378000,
	0x00368000,
	0x00358000,
	0x00348000,
	0x00338000,
	0x00328000,
	0x00318000,
	0x00308000,
	0x002f8000,
```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
