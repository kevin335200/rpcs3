# swapchain_unix.hpp

**路径**: `VK/vkutils/swapchain_unix.hpp`  
**类型**: 头文件  
**大小**: 4169 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **swapchain_X11** (继承自: `native_swapchain_base`)

## 主要函数

- `create()`
- `present()`
- `destroy()`
- `make_WSI_surface()`
- `init()`
- `ensure()`
- `constexpr()`

## 依赖关系

### 包含的头文件

```cpp
#include <swapchain_core.h>
#include <X11/Xutil.h>
```

### 命名空间

- `vk`

## 代码统计

- 总行数: 172
- 类/结构体数量: 1
- 函数数量: 7
- 枚举数量: 0

## 相关文件

*无直接关联文件*

