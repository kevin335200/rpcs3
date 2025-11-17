# VKDataHeapManager.h

**路径**: `VK/VKDataHeapManager.h`  
**类型**: 头文件  
**大小**: 745 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **data_heap**

## 主要函数

- `register_ring_buffer()`
- `register_ring_buffers()`
- `reset()`
- `restore_snapshot()`
- `get_heap_snapshot()`
- `reset_heap_allocations()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <unordered_map>
```

### 命名空间

- `vk`
- `data_heap_manager`

## 代码统计

- 总行数: 33
- 类/结构体数量: 1
- 函数数量: 6
- 枚举数量: 0

## 相关文件

- **实现文件**: [VKDataHeapManager.cpp](VKDataHeapManager.md)

