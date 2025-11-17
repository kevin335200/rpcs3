# cellDmuxPamf.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/cellDmuxPamf.h`
- **类型**: 头文件
- **行数**: 15 行

## 🎯 功能概述

PS3 HLE (High-Level Emulation) 模块实现。

## 📋 主要内容

### 类/结构体

- `CellDmuxPamfAttr`
- `CellDmuxPamfEsAttr`

## 💻 代码片段

```cpp
#pragma once

struct CellDmuxPamfAttr
{
	be_t<u32> maxEnabledEsNum;
	be_t<u32> version;
	be_t<u32> memSize;
};

struct CellDmuxPamfEsAttr
{
	be_t<u32> auQueueMaxSize;
	be_t<u32> memSize;
	be_t<u32> specificInfoSize;
};

```

