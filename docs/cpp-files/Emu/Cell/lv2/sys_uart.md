# sys_uart.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_uart.h`
- **类型**: 头文件
- **行数**: 763 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `ps3av_get_monitor_info_reply`
- `ps3av_header`
- `ps3av_info_color`
- `ps3av_info_resolution`
- `ps3av_pkt_acp_ctrl`
- `ps3av_pkt_add_signal_ctl`
- `ps3av_pkt_av_get_cec_config_reply`
- `ps3av_pkt_av_init`
- `ps3av_pkt_hdmi_plugged_event`
- `ps3av_pkt_video_set_pitch`

### 系统调用

- `sys_uart_get_params()`
- `sys_uart_initialize()`
- `sys_uart_receive()`
- `sys_uart_send()`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Memory/vm_ptr.h"
#include "Utilities/mutex.h"
#include "Utilities/cond.h"
#include "Utilities/simple_ringbuf.h"

enum : u32
{
	PS3AV_RX_BUF_SIZE                       = 0x800,
	PS3AV_TX_BUF_SIZE                       = 0x800,

	PS3AV_VERSION                           = 0x205,

	PS3AV_CID_AV_INIT                       = 0x00000001,
	PS3AV_CID_AV_FIN                        = 0x00000002,
	PS3AV_CID_AV_GET_HW_CONF                = 0x00000003,
	PS3AV_CID_AV_GET_MONITOR_INFO           = 0x00000004,
	PS3AV_CID_AV_GET_BKSV_LIST              = 0x00000005,
	PS3AV_CID_AV_ENABLE_EVENT               = 0x00000006,
	PS3AV_CID_AV_DISABLE_EVENT              = 0x00000007,
	PS3AV_CID_AV_GET_PORT_STATE             = 0x00000009,
	PS3AV_CID_AV_TV_MUTE                    = 0x0000000A,
	PS3AV_CID_AV_NULL_CMD                   = 0x0000000B,
	PS3AV_CID_AV_GET_AKSV                   = 0x0000000C,
	PS3AV_CID_AV_UNK4                       = 0x0000000D,
	PS3AV_CID_AV_UNK5                       = 0x0000000E,

	PS3AV_CID_AV_VIDEO_MUTE                 = 0x00010002,
	PS3AV_CID_AV_VIDEO_DISABLE_SIG          = 0x00010003,
	PS3AV_CID_AV_VIDEO_YTRAPCONTROL         = 0x00010004,
	PS3AV_CID_AV_VIDEO_UNK5                 = 0x00010005,
	PS3AV_CID_AV_VIDEO_UNK6                 = 0x00010006,
	PS3AV_CID_AV_AUDIO_MUTE                 = 0x00020002,
	PS3AV_CID_AV_ACP_CTRL                   = 0x00020003,
	PS3AV_CID_AV_SET_ACP_PACKET             = 0x00020004,
	PS3AV_CID_AV_ADD_SIGNAL_CTL             = 0x00030001,
	PS3AV_CID_AV_SET_CC_CODE                = 0x00030002,
	PS3AV_CID_AV_SET_CGMS_WSS               = 0x00030003,
	PS3AV_CID_AV_SET_MACROVISION            = 0x00030004,
	PS3AV_CID_AV_UNK7                       = 0x00030005,
	PS3AV_CID_AV_UNK8                       = 0x00030006,
	PS3AV_CID_AV_UNK9                       = 0x00030007,
	PS3AV_CID_AV_HDMI_MODE                  = 0x00040001,
	PS3AV_CID_AV_UNK15                      = 0x00050001,

	PS3AV_CID_AV_CEC_MESSAGE                = 0x000A0001,
	PS3AV_CID_AV_GET_CEC_CONFIG             = 0x000A0002,
	PS3AV_CID_AV_UNK11                      = 0x000A0003,
	PS3AV_CID_AV_UNK12                      = 0x000A0004,
	PS3AV_CID_AV_UNK13                      = 0x000A0005,
	PS3AV_CID_AV_UNK14                      = 0x000A0006,

	PS3AV_CID_VIDEO_INIT                    = 0x01000001,
	PS3AV_CID_VIDEO_MODE                    = 0x01000002,
	PS3AV_CID_VIDEO_ROUTE                   = 0x01000003,
	PS3AV_CID_VIDEO_FORMAT                  = 0x01000004,
	PS3AV_CID_VIDEO_PITCH                   = 0x01000005,
	PS3AV_CID_VIDEO_GET_HW_CONF             = 0x01000006,
	PS3AV_CID_VIDEO_GET_REG                 = 0x01000008,
	PS3AV_CID_VIDEO_UNK                     = 0x01000009,
	PS3AV_CID_VIDEO_UNK1                    = 0x0100000A,
	PS3AV_CID_VIDEO_UNK2                    = 0x0100000B,
	PS3AV_CID_VIDEO_UNK3                    = 0x0100000C,

	PS3AV_CID_AUDIO_INIT                    = 0x02000001,
	PS3AV_CID_AUDIO_MODE                    = 0x02000002,
	PS3AV_CID_AUDIO_MUTE                    = 0x02000003,
	PS3AV_CID_AUDIO_ACTIVE                  = 0x02000004,
	PS3AV_CID_AUDIO_INACTIVE                = 0x02000005,
	PS3AV_CID_AUDIO_SPDIF_BIT               = 0x02000006,
	PS3AV_CID_AUDIO_CTRL                    = 0x02000007,

	PS3AV_CID_AVB_PARAM                     = 0x04000001,

	PS3AV_CID_EVENT_UNPLUGGED               = 0x10000001,
	PS3AV_CID_EVENT_PLUGGED                 = 0x10000002,
	PS3AV_CID_EVENT_HDCP_DONE               = 0x10000003,
	PS3AV_CID_EVENT_HDCP_FAIL               = 0x10000004,
	PS3AV_CID_EVENT_HDCP_REAUTH             = 0x10000005,
```

## 🔗 依赖头文件

- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Utilities/mutex.h"`
- `#include "Utilities/cond.h"`
- `#include "Utilities/simple_ringbuf.h"`
