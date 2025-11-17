# shared.h

**路径**: `VK/vkutils/shared.h`  
**类型**: 头文件  
**大小**: 901 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 宏定义

```cpp
#define CHECK_RESULT
#define CHECK_RESULT_EX
```

## 主要函数

- `BreakCallback()`
- `die_with_error()`

## 依赖关系

### 包含的头文件

```cpp
#include <../VulkanAPI.h>
#include <string>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 21
- 类/结构体数量: 0
- 函数数量: 2
- 枚举数量: 0

## 相关文件

- **实现文件**: [shared.cpp](shared.md)

