# sys_trace.h

## 📄 文件信息

- **路径**: `rpcs3/Emu/Cell/lv2/sys_trace.h`
- **类型**: 头文件
- **行数**: 15 行

## 🎯 功能概述

PS3 LV2 系统调用实现。

## 📋 主要内容

### 系统调用

- `sys_trace_allocate_buffer()`
- `sys_trace_attach_process()`
- `sys_trace_create()`
- `sys_trace_create2()`
- `sys_trace_destroy()`
- `sys_trace_drain()`
- `sys_trace_free_buffer()`
- `sys_trace_start()`
- `sys_trace_stop()`
- `sys_trace_update_top_index()`

## 💻 代码片段

```cpp
#pragma once

#include "util/types.hpp"

// SysCalls
s32 sys_trace_create();
s32 sys_trace_start();
s32 sys_trace_stop();
s32 sys_trace_update_top_index();
s32 sys_trace_destroy();
s32 sys_trace_drain();
s32 sys_trace_attach_process();
s32 sys_trace_allocate_buffer();
s32 sys_trace_free_buffer();
s32 sys_trace_create2();

```

## 🔗 依赖头文件

- `#include "util/types.hpp"`
