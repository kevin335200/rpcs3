# cellFontFT.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellFontFT.h`
- **类型**: 头文件
- **行数**: 13 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellFontLibraryConfigFT`

## 💻 代码片段

```cpp
#pragma once

#include "cellFont.h"

#include "Emu/Memory/vm_ptr.h"

struct CellFontLibraryConfigFT
{
	vm::bptr<void> library;
	CellFontMemoryInterface MemoryIF;
};

using CellFontRendererConfigFT = CellFontRendererConfig;

```

## 🔗 依赖头文件

- `#include "cellFont.h"`
- `#include "Emu/Memory/vm_ptr.h"`
