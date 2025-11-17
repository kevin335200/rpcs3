# VKCompute.h

**路径**: `VK/VKCompute.h`  
**类型**: 头文件  
**大小**: 16331 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **compute_task**
- **cs_shuffle_base**
- **cs_shuffle_16**
- **cs_shuffle_32**
- **cs_shuffle_32_16**
- **cs_shuffle_d24x8_f32**
- **cs_shuffle_se_f32_d24x8**
- **cs_shuffle_se_d24x8**
- **cs_interleave_task**
- **cs_gather_d24x8**
- **cs_gather_d32x8**
- **cs_scatter_d24x8**
- **cs_scatter_d32x8**
- **cs_fconvert_task**
- **cs_deswizzle_base**

### 枚举

- `RSX_detiler_op`

## 主要函数

- `load_program()`
- `bind_resources()`
- `destroy()`
- `declare_f16_contraction()`
- `create()`
- `declare_f16_expansion()`
- `constexpr()`
- `get_inputs()`
- `run()`
- `set_parameters()`
- `build()`

## 依赖关系

### 包含的头文件

```cpp
#include <Emu/RSX/VK/VKProgramPipeline.h>
#include <vkutils/descriptors.h>
#include <vkutils/buffer_object.h>
#include <Emu/IdManager.h>
#include <Utilities/StrUtil.h>
#include <util/asm.hpp>
#include <unordered_map>
#include <../Program/GLSLSnippets/GPUDeswizzle.glsl>
#include <../Program/GLSLSnippets/RSXMemoryTiling.glsl>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 678
- 类/结构体数量: 20
- 函数数量: 11
- 枚举数量: 1

## 相关文件

- **实现文件**: [VKCompute.cpp](VKCompute.md)

