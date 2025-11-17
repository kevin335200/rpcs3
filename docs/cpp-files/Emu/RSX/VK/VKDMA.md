# VKDMA.h

**路径**: `VK/VKDMA.h`  
**类型**: 头文件  
**大小**: 1698 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **dma_block**
- **dma_block_EXT** (继承自: `dma_block`)

## 主要函数

- `head()`
- `allocate()`
- `init()`
- `set_parent()`
- `unmap()`
- `map_dma()`
- `end()`
- `flush_dma()`
- `start()`
- `map_range()`
- `unmap_dma()`
- `get()`
- `free()`
- `size()`
- `flush()`
- `extend()`
- `load()`
- `load_dma()`
- `clear_dma_resources()`

## 依赖关系

### 包含的头文件

```cpp
#include <vkutils/buffer_object.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 66
- 类/结构体数量: 2
- 函数数量: 19
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKDMA.cpp](VKDMA.md)

