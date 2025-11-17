# libsynth2.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/libsynth2.h`
- **类型**: 头文件
- **行数**: 19 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `CellSoundSynth2EffectAttr`

## 💻 代码片段

```cpp
#pragma once

// Error Codes
enum CellSoundSynth2Error : u32
{
	CELL_SOUND_SYNTH2_ERROR_FATAL = 0x80310201,
	CELL_SOUND_SYNTH2_ERROR_INVALID_PARAMETER = 0x80310202,
	CELL_SOUND_SYNTH2_ERROR_ALREADY_INITIALIZED = 0x80310203,
};

struct CellSoundSynth2EffectAttr
{
	be_t<u16> core;
	be_t<u16> mode;
	be_t<s16> depth_L;
	be_t<s16> depth_R;
	be_t<u16> delay;
	be_t<u16> feedback;
};

```

