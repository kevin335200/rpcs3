# chip_class.h

**路径**: `VK/vkutils/chip_class.h`  
**类型**: 头文件  
**大小**: 2074 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **chip_class**
- **driver_vendor**
- **chip_family_table**
- **default_**
- **family**
- **family**
- **find**
- **get_chip_family**
- **get_chip_family**
- **chip**
- **chip**
- **chip**

### 枚举

- `driver_vendor`
- `chip_class`

## 主要函数

- `get_driver_vendor()`
- `find()`
- `is_AMD()`
- `get_chip_family()`
- `add()`
- `is_INTEL()`
- `is_NVIDIA()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <unordered_map>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 86
- 类/结构体数量: 12
- 函数数量: 7
- 枚举数量: 2

## 相关文件

- **实现文件**: [chip_class.cpp](chip_class.md)

