# VKProgramPipeline.h

**路径**: `VK/VKProgramPipeline.h`  
**类型**: 头文件  
**大小**: 6438 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **bound_sampler**
- **bound_buffer**
- **push_constant_ref**
- **program_input**
- **shader**
- **descriptor_table_t**
- **program**

### 枚举

- `program_input_type`
- `binding_set_index`

## 主要函数

- `link()`
- `init()`
- `create()`
- `bind_uniform()`
- `has_uniform()`
- `as_push_constant()`
- `destroy()`
- `create_descriptor_pool()`
- `load_uniforms()`
- `validate()`
- `get_uniform_location()`
- `as_sampler()`
- `make()`
- `create_descriptor_set_layout()`
- `bind()`
- `notify_descriptor_slot_updated()`
- `get_handle()`
- `commit()`
- `as_buffer()`
- `create_descriptor_template()`

## 依赖关系

### 包含的头文件

```cpp
#include <VulkanAPI.h>
#include <Emu/RSX/Program/GLSLTypes.h>
#include <vkutils/descriptors.h>
#include <vkutils/ex.h>
#include <string>
#include <vector>
#include <variant>
```

### 命名空间

- `vk`
- `glsl`

## 代码统计

- 总行数: 219
- 类/结构体数量: 7
- 函数数量: 25
- 枚举数量: 2

## 相关文件

- **实现文件**: [VKProgramPipeline.cpp](VKProgramPipeline.md)

