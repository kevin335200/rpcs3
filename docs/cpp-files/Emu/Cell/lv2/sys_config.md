# sys_config.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_config.h`
- **类型**: 头文件
- **行数**: 423 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 类/结构体

- `lv2_config`
- `lv2_config_handle`
- `lv2_config_service`
- `lv2_config_service_event`
- `lv2_config_service_listener`
- `service_event_id`
- `sys_config_padmanager_data_t`
- `sys_config_service_event_t`

### 系统调用

- `sys_config_add_service_listener()`
- `sys_config_close()`
- `sys_config_get_io_event()`
- `sys_config_get_service_event()`
- `sys_config_open()`
- `sys_config_register_io_error_listener()`
- `sys_config_register_service()`
- `sys_config_remove_service_listener()`
- `sys_config_service_event_t()`
- `sys_config_unregister_io_error_listener()`
- `sys_config_unregister_service()`

## 💻 代码片段

```cpp
#pragma once

#include "util/atomic.hpp"
#include "util/shared_ptr.hpp"
#include "Emu/Cell/timers.hpp"

/*
 * sys_config is a "subscription-based data storage API"
 *
 * It has the concept of services and listeners. Services provide data, listeners subscribe to registration/unregistration events from specific services.
 *
 * Services are divided into two classes: LV2 services (positive service IDs) and User services (negative service IDs).
 * LV2 services seem to be implictly "available", probably constructed on-demand with internal LV2 code generating the data. An example is PadManager (service ID 0x11).
 * User services may be registered through a syscall, and have negative IDs. An example is libPad (service ID 0x8000'0000'0000'0001).
 * Note that user-mode *cannot* register positive service IDs.
 *
 * To start with, you have to get a sys_config handle by calling sys_config_open and providing an event queue.
 * This event queue will be used for sys_config notifications if a subscribed config event is registered.
 *
 * With a sys_config handle, listeners can be added to specific services using sys_config_add_service_listener.
 * This syscall returns a service listener handle, which can be used to close the listener and stop further notifications.
 * Once subscribed, any matching past service registrations will be automatically sent to the supplied queue (thus the "data storage").
 *
 * Services exist "implicitly", and data may be registered *onto* a service by calling sys_config_register_service.
 * You can remove config events by calling sys_config_unregister_service and providing the handle returned when registering a service.
 *
 * If a service is registered (or unregistered) and matches any active listener, that listener will get an event sent to the event queue provided in the call to sys_config_open.
 *
 * This event will contain the type of config event ("service event" or "IO event", in event.source),
 * the corresponding sys_config handle (event.data1), the config event ID (event.data2 & 0xffff'ffff),
 * whether the service was registered or unregistered ('data2 >> 32'), and what buffer size will be needed to read the corresponding service event (event.data3).
 *
 * NOTE: if multiple listeners exist, each gets a separate event ID even though all events are the same!
 *
 * After receiving such an event from the event queue, the user should allocate enough buffer and call sys_config_get_service_event
 * (or sys_config_io_event) with the given event ID, in order to obtain a sys_config_service_event_t (or sys_config_io_event_t) structure
 * with the contents of the service that was (un)registered.
 */

class lv2_config_handle;
class lv2_config_service;
class lv2_config_service_listener;
class lv2_config_service_event;


// Known sys_config service IDs
enum sys_config_service_id : s64 {
	SYS_CONFIG_SERVICE_PADMANAGER  = 0x11,
	SYS_CONFIG_SERVICE_PADMANAGER2 = 0x12, // lv2 seems to send padmanager events to both 0x11 and 0x12
	SYS_CONFIG_SERVICE_0x20        = 0x20,
	SYS_CONFIG_SERVICE_0x30        = 0x30,

	SYS_CONFIG_SERVICE_USER_BASE     = static_cast<s64>(UINT64_C(0x8000'0000'0000'0000)),
	SYS_CONFIG_SERVICE_USER_LIBPAD   = SYS_CONFIG_SERVICE_USER_BASE +      1,
	SYS_CONFIG_SERVICE_USER_LIBKB    = SYS_CONFIG_SERVICE_USER_BASE +      2,
	SYS_CONFIG_SERVICE_USER_LIBMOUSE = SYS_CONFIG_SERVICE_USER_BASE +      3,
	SYS_CONFIG_SERVICE_USER_0x1000   = SYS_CONFIG_SERVICE_USER_BASE + 0x1000,
	SYS_CONFIG_SERVICE_USER_0x1010   = SYS_CONFIG_SERVICE_USER_BASE + 0x1010,
	SYS_CONFIG_SERVICE_USER_0x1011   = SYS_CONFIG_SERVICE_USER_BASE + 0x1011,
	SYS_CONFIG_SERVICE_USER_0x1013   = SYS_CONFIG_SERVICE_USER_BASE + 0x1013,
	SYS_CONFIG_SERVICE_USER_0x1020   = SYS_CONFIG_SERVICE_USER_BASE + 0x1020,
	SYS_CONFIG_SERVICE_USER_0x1030   = SYS_CONFIG_SERVICE_USER_BASE + 0x1030,
};

enum sys_config_service_listener_type : u32 {
	SYS_CONFIG_SERVICE_LISTENER_ONCE      = 0,
	SYS_CONFIG_SERVICE_LISTENER_REPEATING = 1
};

enum sys_config_event_source : u64 {
	SYS_CONFIG_EVENT_SOURCE_SERVICE = 1,
	SYS_CONFIG_EVENT_SOURCE_IO      = 2
};


/*
 * Dynamic-sized struct to describe a sys_config_service_event
 * We never allocate it - the guest does it for us and provides a pointer
 */
struct sys_config_service_event_t {
```

## 🔗 依赖头文件

- `#include "util/atomic.hpp"`
- `#include "util/shared_ptr.hpp"`
- `#include "Emu/Cell/timers.hpp"`
