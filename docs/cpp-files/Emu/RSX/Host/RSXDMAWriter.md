# RSXDMAWriter.h

**路径**: `Host/RSXDMAWriter.h`  
**类型**: 头文件  
**大小**: 2741 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**主机内存管理**。

## 主要组件

### 类/结构体

- **host_gpu_context_t**
- **host_gpu_write_op_t**
- **host_dispatch_handler_t**
- **RSXDMAWriter**

## 主要函数

- `update()`
- `deregister_handler()`
- `enqueue()`
- `in_flight_commands_completed()`
- `register_handler()`
- `drain_label_queue()`
- `inc_counter()`
- `on_texture_load_acquire()`
- `on_texture_load_release()`
- `texture_loads_completed()`
- `needs_label_release()`
- `has_unflushed_texture_loads()`
- `on_label_release()`
- `on_label_acquire()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <unordered_map>
#include <functional>
#include <deque>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 115
- 类/结构体数量: 4
- 函数数量: 14
- 枚举数量: 0

## 相关文件

- **实现文件**: [RSXDMAWriter.cpp](RSXDMAWriter.md)

