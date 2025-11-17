# sceNp.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sceNp.h`
- **类型**: 头文件
- **行数**: 1,865 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `SceNpCommunicationPassphrase`
- `SceNpEntitlementId`
- `SceNpScoreClanBasicInfo`
- `SceNpScoreClanIdRankData`
- `SceNpScoreNpIdPcId`
- `SceNpScorePlayerRankData`
- `SceNpScoreRankData_deprecated`
- `SceNpScoreVariableSizeGameInfo`
- `SceNpSignalingNetInfo`
- `np_in_addr`

### 关键函数

- `Exec()`
- `callback_handler()`
- `matching_create_room()`
- `matching_get_room_info()`
- `matching_get_room_member_list()`
- `matching_join_room()`
- `matching_set_room_info()`
- `print()`
- `sceNpInit()`
- `sceNpTerm()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/NP/rpcn_types.h"
#include "cellRtc.h"
#include "Emu/Cell/ErrorCodes.h"
#include "util/shared_ptr.hpp"

#include <set>

error_code sceNpInit(u32 poolsize, vm::ptr<void> poolptr);
error_code sceNpTerm();

using np_in_addr_t   = u32;
using np_in_port_t   = u16;
using np_sa_family_t = u8;
using np_socklen_t   = u32;

struct np_in_addr
{
	np_in_addr_t np_s_addr; // TODO: alignment?
};

using sys_memory_container_t = u32;

using system_time_t = u64; // s64 in documentation. But since this is in microseconds, it doesn't seem to make much sense.
using second_t = u32;
using usecond_t = u64;

using SceNpBasicAttachmentDataId = u32;
using SceNpBasicMessageId = u64;
using SceNpBasicMessageRecvAction = u32;

using SceNpClanId = u32;
using SceNpClansMessageId = u32;
using SceNpClansMemberStatus = s32;

using SceNpCustomMenuIndexMask = u32;
using SceNpCustomMenuSelectedType = u32;

using SceNpFriendlistCustomOptions = u64;

using SceNpPlatformType = s32;

using SceNpScoreBoardId = u32;
using SceNpScoreClansBoardId = u32;
using SceNpScorePcId = s32;
using SceNpScoreRankNumber = u32;
using SceNpScoreValue = s64;

using SceNpTime = s64;

// Error Codes
enum SceNpError : u32
{
	// NP Manager Utility
	SCE_NP_ERROR_NOT_INITIALIZED            = 0x8002aa01,
	SCE_NP_ERROR_ALREADY_INITIALIZED        = 0x8002aa02,
	SCE_NP_ERROR_INVALID_ARGUMENT           = 0x8002aa03,
	SCE_NP_ERROR_OUT_OF_MEMORY              = 0x8002aa04,
	SCE_NP_ERROR_ID_NO_SPACE                = 0x8002aa05,
	SCE_NP_ERROR_ID_NOT_FOUND               = 0x8002aa06,
	SCE_NP_ERROR_SESSION_RUNNING            = 0x8002aa07,
	SCE_NP_ERROR_LOGINID_ALREADY_EXISTS     = 0x8002aa08,
	SCE_NP_ERROR_INVALID_TICKET_SIZE        = 0x8002aa09,
	SCE_NP_ERROR_INVALID_STATE              = 0x8002aa0a,
	SCE_NP_ERROR_ABORTED                    = 0x8002aa0b,
	SCE_NP_ERROR_OFFLINE                    = 0x8002aa0c,
	SCE_NP_ERROR_VARIANT_ACCOUNT_ID         = 0x8002aa0d,
	SCE_NP_ERROR_GET_CLOCK                  = 0x8002aa0e,
	SCE_NP_ERROR_INSUFFICIENT_BUFFER        = 0x8002aa0f,
	SCE_NP_ERROR_EXPIRED_TICKET             = 0x8002aa10,
	SCE_NP_ERROR_TICKET_PARAM_NOT_FOUND     = 0x8002aa11,
	SCE_NP_ERROR_UNSUPPORTED_TICKET_VERSION = 0x8002aa12,
	SCE_NP_ERROR_TICKET_STATUS_CODE_INVALID = 0x8002aa13,
	SCE_NP_ERROR_INVALID_TICKET_VERSION     = 0x8002aa14,
	SCE_NP_ERROR_ALREADY_USED               = 0x8002aa15,
	SCE_NP_ERROR_DIFFERENT_USER             = 0x8002aa16,
	SCE_NP_ERROR_ALREADY_DONE               = 0x8002aa17,

	// NP Basic Utility
```

## 🔗 依赖头文件

- `#include "Emu/NP/rpcn_types.h"`
- `#include "cellRtc.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include "util/shared_ptr.hpp"`
- `#include <set>`
