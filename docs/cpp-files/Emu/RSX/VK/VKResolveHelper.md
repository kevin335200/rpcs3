# VKResolveHelper.h

**路径**: `VK/VKResolveHelper.h`  
**类型**: 头文件  
**大小**: 12414 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **cs_resolve_base**
- **cs_resolve_task**
- **cs_unresolve_task**
- **depth_resolve_base** (继承自: `overlay_pass`)
- **depthonly_resolve**
- **depthonly_unresolve**
- **stencilonly_resolve**
- **stencilonly_unresolve**
- **depthstencil_resolve_EXT**
- **depthstencil_unresolve_EXT**

## 主要函数

- `emit_geometry()`
- `reset_resolve_resources()`
- `get_dynamic_state_entries()`
- `bind_resources()`
- `update_sample_configuration()`
- `clear_resolve_helpers()`
- `update_uniforms()`
- `get_inputs()`
- `run()`
- `get_fragment_inputs()`
- `build()`

## 依赖关系

### 包含的头文件

```cpp
#include <VKCompute.h>
#include <VKOverlays.h>
#include <vkutils/image.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 388
- 类/结构体数量: 10
- 函数数量: 11
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKResolveHelper.cpp](VKResolveHelper.md)

