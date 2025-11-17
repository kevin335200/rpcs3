# GLCompute.h

**路径**: `GL/GLCompute.h`  
**类型**: 头文件  
**大小**: 10136 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **compute_task**
- **cs_shuffle_base**
- **cs_shuffle_16**
- **cs_shuffle_32**
- **cs_shuffle_32_16**
- **cs_shuffle_d32fx8_to_x8d24f**
- **cs_shuffle_x8d24f_to_d32fx8**
- **cs_fconvert_task**
- **cs_deswizzle_3d**
- **pixel_buffer_layout**
- **cs_image_to_ssbo** (继承自: `compute_task`)
- **cs_d24x8_to_ssbo**
- **cs_rgba8_to_ssbo**
- **cs_ssbo_to_color_image**
- **T**

## 主要函数

- `build()`
- `declare_f16_expansion()`
- `create()`
- `initialize()`
- `set_parameters()`
- `run()`
- `bind_resources()`
- `constexpr()`
- `declare_f16_contraction()`
- `destroy()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/IdManager.h>
#include <GLHelpers.h>
#include <glutils/program.h>
#include <../rsx_utils.h>
#include <unordered_map>
#include <../Program/GLSLSnippets/GPUDeswizzle.glsl>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 397
- 类/结构体数量: 15
- 函数数量: 10
- 枚举数量: 0

## 相关文件

- **实现文件**: [GLCompute.cpp](GLCompute.md)

