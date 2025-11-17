# garbage_collector.h

**路径**: `VK/vkutils/garbage_collector.h`  
**类型**: 头文件  
**大小**: 1032 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **disposable_t**
- **garbage_collector**

## 主要函数

- `disposable_t()`
- `get_gc()`
- `dispose()`
- `add_exit_callback()`
- `make()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <functional>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 58
- 类/结构体数量: 2
- 函数数量: 5
- 枚举数量: 0

## 相关文件

*无直接关联文件*

