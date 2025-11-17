# sceNpUtil.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sceNpUtil.h`
- **类型**: 头文件
- **行数**: 16 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `SceNpUtilBandwidthTestResult`

## 💻 代码片段

```cpp
#pragma once

enum
{
	SCE_NP_UTIL_BANDWIDTH_TEST_STATUS_NONE = 0,
	SCE_NP_UTIL_BANDWIDTH_TEST_STATUS_RUNNING = 1,
	SCE_NP_UTIL_BANDWIDTH_TEST_STATUS_FINISHED = 2
};

struct SceNpUtilBandwidthTestResult
{
	be_t<f64> upload_bps;
	be_t<f64> download_bps;
	be_t<s32> result;
	s8 padding[4];
};

```

