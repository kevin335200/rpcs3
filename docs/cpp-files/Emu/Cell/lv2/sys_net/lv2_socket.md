# lv2_socket.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_net/lv2_socket.h`
- **类型**: 头文件
- **行数**: 156 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `lv2_socket`
- `sockopt_cache`

### 关键函数

- `abort_socket()`
- `accept()`
- `close()`
- `connect()`
- `getsockname()`
- `handle_events()`
- `poll()`
- `queue_wake()`
- `recvfrom()`
- `save()`
- `sendmsg()`
- `set_connecting()`
- `set_lv2_id()`
- `setsockopt()`
- `shutdown()`

## 💻 代码片段

```cpp
#pragma once

#include <functional>
#include <optional>

#include "Utilities/mutex.h"
#include "Emu/IdManager.h"
#include "Emu/Cell/lv2/sys_net.h"
#include "Emu/NP/ip_address.h"

#ifdef _WIN32
#include <winsock2.h>
#include <WS2tcpip.h>
#else
#ifdef __clang__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wold-style-cast"
#endif
#include <poll.h>
#ifdef __clang__
#pragma GCC diagnostic pop
#endif
#endif

enum class thread_state : u32;

class lv2_socket
{
public:
	// Poll events
	enum class poll_t
	{
		read,
		write,
		error,

		__bitset_enum_max
	};

	union sockopt_data
	{
		char ch[128];
		be_t<s32> _int = 0;
		sys_net_timeval timeo;
		sys_net_linger linger;
	};

	struct sockopt_cache
	{
		sockopt_data data{};
		s32 len = 0;
	};

public:
	SAVESTATE_INIT_POS(7); // Dependency on RPCN

	lv2_socket(lv2_socket_family family, lv2_socket_type type, lv2_ip_protocol protocol);
	lv2_socket(utils::serial&) {}
	lv2_socket(utils::serial&, lv2_socket_type type);
	static std::function<void(void*)> load(utils::serial& ar);
	void save(utils::serial&, bool save_only_this_class = false);
	virtual ~lv2_socket() noexcept;
	lv2_socket& operator=(thread_state s) noexcept;

	std::unique_lock<shared_mutex> lock();

	void set_lv2_id(u32 id);
	bs_t<poll_t> get_events() const;
	void set_poll_event(bs_t<poll_t> event);
	void poll_queue(shared_ptr<ppu_thread> ppu, bs_t<poll_t> event, std::function<bool(bs_t<poll_t>)> poll_cb);
	u32 clear_queue(ppu_thread*);
	void handle_events(const pollfd& native_fd, bool unset_connecting = false);
	void queue_wake(ppu_thread* ppu);

	lv2_socket_family get_family() const;
	lv2_socket_type get_type() const;
	lv2_ip_protocol get_protocol() const;
	std::size_t get_queue_size() const;
	socket_type get_socket() const;
#ifdef _WIN32
```

## 🔗 依赖头文件

- `#include <functional>`
- `#include <optional>`
- `#include "Utilities/mutex.h"`
- `#include "Emu/IdManager.h"`
- `#include "Emu/Cell/lv2/sys_net.h"`
- `#include "Emu/NP/ip_address.h"`
- `#include <winsock2.h>`
- `#include <WS2tcpip.h>`
- `#include <poll.h>`
