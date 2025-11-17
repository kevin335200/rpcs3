# sys_net_helpers.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_net/sys_net_helpers.h`
- **类型**: 头文件
- **行数**: 32 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_net_addr_to_native_addr()`

## 💻 代码片段

```cpp

#ifdef _WIN32
#include <winsock2.h>
#include <WS2tcpip.h>
#else
#ifdef __clang__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wold-style-cast"
#endif
#include <sys/socket.h>
#include <netinet/in.h>
#ifdef __clang__
#pragma GCC diagnostic pop
#endif
#endif

#include "Emu/Cell/lv2/sys_net.h"

int get_native_error();
sys_net_error convert_error(bool is_blocking, int native_error, bool is_connecting = false);
sys_net_error get_last_error(bool is_blocking, bool is_connecting = false);
sys_net_sockaddr native_addr_to_sys_net_addr(const ::sockaddr_storage& native_addr);
::sockaddr_in sys_net_addr_to_native_addr(const sys_net_sockaddr& sn_addr);
bool is_ip_public_address(const ::sockaddr_in& addr);
u32 network_clear_queue(ppu_thread& ppu);
void clear_ppu_to_awake(ppu_thread& ppu);
be_t<u32> resolve_binding_ip();

#ifdef _WIN32
void windows_poll(std::vector<pollfd>& fds, unsigned long nfds, int timeout, std::vector<bool>& connecting);
#endif

```

## 🔗 依赖头文件

- `#include <winsock2.h>`
- `#include <WS2tcpip.h>`
- `#include <sys/socket.h>`
- `#include <netinet/in.h>`
- `#include "Emu/Cell/lv2/sys_net.h"`
