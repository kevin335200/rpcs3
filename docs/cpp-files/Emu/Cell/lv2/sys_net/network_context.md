# network_context.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_net/network_context.h`
- **类型**: 头文件
- **行数**: 48 行

## 🎯 功能概述

Cell Broadband Engine 相关实现。

## 📋 主要内容

### 类/结构体

- `base_network_thread`
- `network_thread`
- `p2p_thread`

### 关键函数

- `add_ppu_to_awake()`
- `bind_sce_np_port()`
- `create_p2p_port()`
- `del_ppu_to_awake()`
- `operator()`
- `wake_threads()`

## 💻 代码片段

```cpp
#pragma once

#include <vector>
#include <map>
#include "Utilities/mutex.h"
#include "Emu/Cell/PPUThread.h"

#include "nt_p2p_port.h"

struct base_network_thread
{
	void add_ppu_to_awake(ppu_thread* ppu);
	void del_ppu_to_awake(ppu_thread* ppu);

	shared_mutex mutex_ppu_to_awake;
	std::vector<ppu_thread*> ppu_to_awake;

	void wake_threads();
};

struct network_thread : base_network_thread
{
	shared_mutex mutex_thread_loop;
	atomic_t<u32> num_polls = 0;

	static constexpr auto thread_name = "Network Thread";

	void operator()();
};

struct p2p_thread : base_network_thread
{
	shared_mutex list_p2p_ports_mutex;
	std::map<u16, nt_p2p_port> list_p2p_ports;
	atomic_t<u32> num_p2p_ports = 0;

	static constexpr auto thread_name = "Network P2P Thread";

	p2p_thread();

	void create_p2p_port(u16 p2p_port);

	void bind_sce_np_port();
	void operator()();
};

using network_context = named_thread<network_thread>;
using p2p_context = named_thread<p2p_thread>;

```

## 🔗 依赖头文件

- `#include <vector>`
- `#include <map>`
- `#include "Utilities/mutex.h"`
- `#include "Emu/Cell/PPUThread.h"`
- `#include "nt_p2p_port.h"`
