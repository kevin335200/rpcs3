# sampler.h

**路径**: `VK/vkutils/sampler.h`  
**类型**: 头文件  
**大小**: 3043 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **border_color_t**
- **sampler**
- **sampler_pool_key_t**
- **cached_sampler_object_t** (继承自: `vk::sampler, public rsx::ref_counted`)
- **sampler_pool_t**

## 主要函数

- `find()`
- `matches()`
- `compute_storage_key()`
- `emplace()`
- `clear()`

## 依赖关系

### 包含的头文件

```cpp
#include <device.h>
#include <shared.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 96
- 类/结构体数量: 5
- 函数数量: 5
- 枚举数量: 0

## 相关文件

- **实现文件**: [sampler.cpp](sampler.md)

