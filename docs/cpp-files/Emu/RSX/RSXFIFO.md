# RSXFIFO.h

**路径**: `RSXFIFO.h`  
**类型**: 头文件  
**大小**: 3910 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**FIFO 命令队列处理**。

## 主要组件

### 类/结构体

- **RsxDmaControl**
- **thread**
- **rsx_iomap_table**
- **state**
- **interrupt_hint**
- **register_pair**
- **flattening_helper**
- **FIFO_control**

### 枚举

- `interrupt_hint`
- `register_props`
- `state`
- `optimization_hint`
- `internal_commands`
- `flatten_op`

## 主要函数

- `read_unsafe()`
- `skip_methods()`
- `last_cmd()`
- `get_current_arg_ptr()`
- `get_remaining_args_count()`
- `get_pos()`
- `read_put()`
- `fetch_u32()`
- `abort()`
- `test()`
- `reset()`
- `inc_get()`
- `get_primitive()`
- `evaluate_performance()`
- `restore_state()`
- `read()`
- `sync_get()`
- `force_disable()`
- `invalidate_cache()`
- `set()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Emu/RSX/gcm_enums.h>
#include <span>
```

### 命名空间

- `rsx`
- `FIFO`

## 代码统计

- 总行数: 178
- 类/结构体数量: 8
- 函数数量: 23
- 枚举数量: 6

## 相关文件

- **实现文件**: [RSXFIFO.cpp](RSXFIFO.md)

