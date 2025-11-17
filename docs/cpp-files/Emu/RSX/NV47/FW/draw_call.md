# draw_call.hpp

**路径**: `NV47/FW/draw_call.hpp`  
**类型**: 头文件  
**大小**: 7675 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**NVIDIA NV47 硬件模拟**。

## 主要组件

### 类/结构体

- **instanced_draw_config_t**
- **draw_clause**
- **mutable**
- **classify_mode**
- **context**
- **context**

## 主要函数

- `append()`
- `end()`
- `insert_draw_command()`
- `get_range()`
- `compile()`
- `check_trivially_instanced()`
- `post_execute_cleanup()`
- `empty()`
- `reset()`
- `begin()`
- `execute_pipeline_dependencies()`
- `is_single_draw()`
- `next()`
- `min_index()`
- `insert_command_barrier()`
- `append_draw_command()`
- `classify_mode()`
- `get_elements_count()`
- `operator()`
- `pass_count()`

## 依赖关系

### 包含的头文件

```cpp
#include <draw_call.inc.h>
#include <Emu/RSX/Common/simple_array.hpp>
#include <Emu/RSX/gcm_enums.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 312
- 类/结构体数量: 6
- 函数数量: 20
- 枚举数量: 0

## 相关文件

- **实现文件**: [draw_call.cpp](draw_call.md)

