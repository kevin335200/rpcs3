# fsr_pass.h

**路径**: `GL/upscalers/fsr_pass.h`  
**类型**: 头文件  
**大小**: 1734 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **fsr_pass** (继承自: `compute_task`)
- **easu_pass** (继承自: `fsr_pass`)
- **rcas_pass** (继承自: `fsr_pass`)
- **fsr_upscale_pass** (继承自: `upscaler`)

## 主要函数

- `dispose_images()`
- `bind_resources()`
- `configure()`
- `initialize_image()`
- `scale_output()`
- `run()`

## 依赖关系

### 包含的头文件

```cpp
#include <../glutils/buffer_object.h>
#include <../glutils/state_tracker.hpp>
#include <../GLCompute.h>
#include <upscaling.h>
```

### 命名空间

- `gl`
- `FidelityFX`

## 代码统计

- 总行数: 76
- 类/结构体数量: 4
- 函数数量: 6
- 枚举数量: 0

## 相关文件

*无直接关联文件*

