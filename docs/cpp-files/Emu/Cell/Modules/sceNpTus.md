# sceNpTus.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sceNpTus.h`
- **类型**: 头文件
- **行数**: 173 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `SceNpTssDataStatus`
- `SceNpTssGetDataOptParam`
- `SceNpTusAddAndGetVariableOptParam`
- `SceNpTusDataStatus`
- `SceNpTusSetDataOptParam`
- `SceNpTusTryAndSetVariableOptParam`
- `SceNpTusVariable`
- `sce_np_tus_manager`
- `sce_np_tus_title_context`
- `sce_np_tus_transaction_context`

### 关键函数

- `add_title_context()`
- `add_transaction_context()`
- `check_title_context_id()`
- `check_transaction_context_id()`
- `get_title_context()`
- `get_transaction_context()`
- `remove_title_context_id()`
- `remove_transaction_context_id()`
- `terminate()`

## 💻 代码片段

```cpp
#pragma once

#include "cellRtc.h"
#include "sceNp.h"

#include <map>

// Constants for TUS functions and structures
enum
{
	SCE_NP_TUS_DATA_INFO_MAX_SIZE = 384,
	SCE_NP_TUS_MAX_CTX_NUM = 32,
	SCE_NP_TUS_MAX_SLOT_NUM_PER_TRANS = 64,
	SCE_NP_TUS_MAX_USER_NUM_PER_TRANS = 101,
	SCE_NP_TUS_MAX_SELECTED_FRIENDS_NUM = 100,
};

enum
{
	SCE_NP_TUS_OPETYPE_EQUAL = 1,
	SCE_NP_TUS_OPETYPE_NOT_EQUAL,
	SCE_NP_TUS_OPETYPE_GREATER_THAN,
	SCE_NP_TUS_OPETYPE_GREATER_OR_EQUAL,
	SCE_NP_TUS_OPETYPE_LESS_THAN,
	SCE_NP_TUS_OPETYPE_LESS_OR_EQUAL
};

enum
{
	SCE_NP_TUS_VARIABLE_SORTTYPE_DESCENDING_DATE = 1,
	SCE_NP_TUS_VARIABLE_SORTTYPE_ASCENDING_DATE,
	SCE_NP_TUS_VARIABLE_SORTTYPE_DESCENDING_VALUE,
	SCE_NP_TUS_VARIABLE_SORTTYPE_ASCENDING_VALUE
};

enum
{
	SCE_NP_TUS_DATASTATUS_SORTTYPE_DESCENDING_DATE = 1,
	SCE_NP_TUS_DATASTATUS_SORTTYPE_ASCENDING_DATE
};

enum SceNpTssStatusCodeType
{
	SCE_NP_TSS_STATUS_TYPE_OK,
	SCE_NP_TSS_STATUS_TYPE_PARTIAL,
	SCE_NP_TSS_STATUS_TYPE_NOT_MODIFIED
};

enum SceNpTssIfType
{
	SCE_NP_TSS_IFTYPE_IF_MODIFIED_SINCE,
	SCE_NP_TSS_IFTYPE_IF_RANGE
};

using SceNpTssSlotId = s32;
using SceNpTusSlotId = s32;
using SceNpTusVirtualUserId = SceNpOnlineId;

// Structure for representing a TUS variable
struct SceNpTusVariable
{
	SceNpId ownerId;
	be_t<s32> hasData;
	CellRtcTick lastChangedDate;
	u8 pad[4];
	SceNpId lastChangedAuthorId;
	be_t<s64> variable;
	be_t<s64> oldVariable;
	u8 reserved[16];
};

// Structure for representing the accessory information of a TUS data
struct SceNpTusDataInfo
{
	be_t<u32> infoSize;
	u8 pad[4];
	u8 data[SCE_NP_TUS_DATA_INFO_MAX_SIZE];
};

// Structure for respreseting the status of TUS data
```

## 🔗 依赖头文件

- `#include "cellRtc.h"`
- `#include "sceNp.h"`
- `#include <map>`
