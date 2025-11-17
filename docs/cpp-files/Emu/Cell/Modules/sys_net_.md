# sys_net_.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/Modules/sys_net_.h`
- **类型**: 头文件
- **行数**: 40 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `sys_net_initialize_parameter_t`
- `sys_net_sockinfo_ex_t`
- `sys_net_sockinfo_t`

## 💻 代码片段

```cpp
#pragma once

#include "Emu/Cell/lv2/sys_net.h"

struct sys_net_sockinfo_t
{
	be_t<s32> s;
	be_t<s32> proto;
	be_t<s32> recv_queue_length;
	be_t<s32> send_queue_length;
	sys_net_in_addr local_adr;
	be_t<s32> local_port;
	sys_net_in_addr remote_adr;
	be_t<s32> remote_port;
	be_t<s32> state;
};

struct sys_net_sockinfo_ex_t
{
	be_t<s32> s;
	be_t<s32> proto;
	be_t<s32> recv_queue_length;
	be_t<s32> send_queue_length;
	sys_net_in_addr local_adr;
	be_t<s32> local_port;
	sys_net_in_addr remote_adr;
	be_t<s32> remote_port;
	be_t<s32> state;
	be_t<s32> socket_type;
	be_t<s32> local_vport;
	be_t<s32> remote_vport;
	be_t<s32> reserved[8];
};

struct sys_net_initialize_parameter_t
{
	vm::bptr<void> memory;
	be_t<s32> memory_size;
	be_t<s32> flags;
};

```

## 🔗 依赖头文件

- `#include "Emu/Cell/lv2/sys_net.h"`
