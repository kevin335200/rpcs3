# sys_net.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_net.h`
- **类型**: 头文件
- **行数**: 368 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `ppu_thread`
- `sys_net_in_addr`
- `sys_net_iovec`
- `sys_net_ip_mreq`
- `sys_net_linger`
- `sys_net_msghdr`
- `sys_net_sockaddr`
- `sys_net_sockaddr_in`
- `sys_net_sockaddr_in_p2p`
- `sys_net_timeval`

### 系统调用

- `sys_net_abort()`
- `sys_net_bnet_accept()`
- `sys_net_bnet_bind()`
- `sys_net_bnet_connect()`
- `sys_net_bnet_getpeername()`
- `sys_net_bnet_getsockname()`
- `sys_net_bnet_getsockopt()`
- `sys_net_bnet_ioctl()`
- `sys_net_bnet_listen()`
- `sys_net_bnet_recvfrom()`
- `sys_net_bnet_recvmsg()`
- `sys_net_bnet_select()`
- `sys_net_bnet_sendmsg()`
- `sys_net_bnet_sendto()`
- `sys_net_bnet_shutdown()`
- `sys_net_bnet_socket()`
- `sys_net_bnet_sysctl()`
- `sys_net_control()`
- `sys_net_eurus_post_command()`
- `sys_net_infoctl()`

## 💻 代码片段

```cpp
#pragma once

#include "Utilities/bit_set.h"
#include "Utilities/mutex.h"

#include "Emu/Memory/vm_ptr.h"
#include "Emu/Cell/ErrorCodes.h"

#include <vector>
#include <utility>
#include <functional>
#include <queue>

// Error codes
enum sys_net_error : s32
{
	SYS_NET_ENOENT          = 2,
	SYS_NET_EINTR           = 4,
	SYS_NET_EBADF           = 9,
	SYS_NET_ENOMEM          = 12,
	SYS_NET_EACCES          = 13,
	SYS_NET_EFAULT          = 14,
	SYS_NET_EBUSY           = 16,
	SYS_NET_EINVAL          = 22,
	SYS_NET_EMFILE          = 24,
	SYS_NET_ENOSPC          = 28,
	SYS_NET_EPIPE           = 32,
	SYS_NET_EAGAIN          = 35,
	SYS_NET_EWOULDBLOCK     = SYS_NET_EAGAIN,
	SYS_NET_EINPROGRESS     = 36,
	SYS_NET_EALREADY        = 37,
	SYS_NET_EDESTADDRREQ    = 39,
	SYS_NET_EMSGSIZE        = 40,
	SYS_NET_EPROTOTYPE      = 41,
	SYS_NET_ENOPROTOOPT     = 42,
	SYS_NET_EPROTONOSUPPORT = 43,
	SYS_NET_EOPNOTSUPP      = 45,
	SYS_NET_EPFNOSUPPORT    = 46,
	SYS_NET_EAFNOSUPPORT    = 47,
	SYS_NET_EADDRINUSE      = 48,
	SYS_NET_EADDRNOTAVAIL   = 49,
	SYS_NET_ENETDOWN        = 50,
	SYS_NET_ENETUNREACH     = 51,
	SYS_NET_ECONNABORTED    = 53,
	SYS_NET_ECONNRESET      = 54,
	SYS_NET_ENOBUFS         = 55,
	SYS_NET_EISCONN         = 56,
	SYS_NET_ENOTCONN        = 57,
	SYS_NET_ESHUTDOWN       = 58,
	SYS_NET_ETOOMANYREFS    = 59,
	SYS_NET_ETIMEDOUT       = 60,
	SYS_NET_ECONNREFUSED    = 61,
	SYS_NET_EHOSTDOWN       = 64,
	SYS_NET_EHOSTUNREACH    = 65,
};

static constexpr sys_net_error operator-(sys_net_error v)
{
	return sys_net_error{-+v};
}

// Socket types (prefixed with SYS_NET_)
enum lv2_socket_type : s32
{
	SYS_NET_SOCK_STREAM     = 1,
	SYS_NET_SOCK_DGRAM      = 2,
	SYS_NET_SOCK_RAW        = 3,
	SYS_NET_SOCK_DGRAM_P2P  = 6,
	SYS_NET_SOCK_STREAM_P2P = 10,
};

// Socket options (prefixed with SYS_NET_)
enum lv2_socket_option : s32
{
	SYS_NET_SO_SNDBUF       = 0x1001,
	SYS_NET_SO_RCVBUF       = 0x1002,
	SYS_NET_SO_SNDLOWAT     = 0x1003,
	SYS_NET_SO_RCVLOWAT     = 0x1004,
	SYS_NET_SO_SNDTIMEO     = 0x1005,
	SYS_NET_SO_RCVTIMEO     = 0x1006,
```

## 🔗 依赖头文件

- `#include "Utilities/bit_set.h"`
- `#include "Utilities/mutex.h"`
- `#include "Emu/Memory/vm_ptr.h"`
- `#include "Emu/Cell/ErrorCodes.h"`
- `#include <vector>`
- `#include <utility>`
- `#include <functional>`
- `#include <queue>`
