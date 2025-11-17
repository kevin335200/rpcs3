# state_tracker.hpp

**路径**: `GL/glutils/state_tracker.hpp`  
**类型**: 头文件  
**大小**: 9693 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **driver_state**
- **command_context**
- **fence**

### 枚举

- `op`
- `zfail`
- `property`
- `mode`
- `target`
- `face`
- `zpass`
- `func`
- `cap`
- `fail`

## 主要函数

- `glDisable()`
- `color_maski()`
- `enablei()`
- `depth_mask()`
- `stencil_mask()`
- `stencil_back_func()`
- `clear_stencil()`
- `disable()`
- `glDisablei()`
- `stencil_func()`
- `clear_color()`
- `test_and_set_property()`
- `stencil_op()`
- `disablei()`
- `stencil_back_op()`
- `clear_depth()`
- `depth_func()`
- `depth_range()`
- `stencil_back_mask()`
- `enable()`

## 依赖关系

### 包含的头文件

```cpp
#include <capabilities.h>
#include <Utilities/geometry.h>
#include <unordered_map>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 447
- 类/结构体数量: 3
- 函数数量: 21
- 枚举数量: 10

## 相关文件

*无直接关联文件*

