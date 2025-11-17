# cellPng.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellPng.h`
- **类型**: 头文件
- **行数**: 176 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellPngCHRM`
- `CellPngGAMA`
- `CellPngPCAL`
- `CellPngSBIT`
- `CellPngSPLT`
- `CellPngSRGB`
- `CellPngTIME`
- `CellPngTRNS`
- `CellPngTextInfo`
- `CellPngUnknownChunk`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"

enum CellPngTxtType : s32
{
	CELL_PNG_TEXT = 0,
	CELL_PNG_ZTXT = 1,
	CELL_PNG_ITXT = 2,
};

enum CellPngUnknownLocation : s32
{
	CELL_PNG_BEFORE_PLTE = 1,
	CELL_PNG_BEFORE_IDAT = 2,
	CELL_PNG_AFTER_IDAT  = 8,
};

struct CellPngPLTEentry
{
	u8 red;
	u8 green;
	u8 blue;
};

struct CellPngPaletteEntries
{
	be_t<u16> red;
	be_t<u16> green;
	be_t<u16> blue;
	be_t<u16> alpha;
	be_t<u16> frequency;
};

struct CellPngSPLTentry
{
	vm::bptr<char> paletteName;
	u8 sampleDepth;
	vm::bptr<CellPngPaletteEntries> paletteEntries;
	be_t<u32> paletteEntriesNumber;
};

struct CellPngTextInfo
{
	be_t<s32> txtType; // CellPngTxtType
	vm::bptr<char> keyword;
	vm::bptr<char> text;
	be_t<u32> textLength;
	vm::bptr<char> languageTag;
	vm::bptr<char> translatedKeyword;
};

struct CellPngPLTE
{
	be_t<u32> paletteEntriesNumber;
	vm::bptr<CellPngPLTEentry> paletteEntries;
};

struct CellPngGAMA
{
	be_t<double> gamma;
};

struct CellPngSRGB
{
	be_t<u32> renderingIntent;
};

struct CellPngICCP
{
	vm::bptr<char> profileName;
	vm::bptr<char> profile;
	be_t<u32> profileLength;
};

struct CellPngSBIT
{
	be_t<u32> red;
	be_t<u32> green;
	be_t<u32> blue;
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
