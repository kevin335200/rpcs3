# RSXIOMap.hpp

**路径**: `Core/RSXIOMap.hpp`  
**类型**: 头文件  
**大小**: 2092 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 核心功能实现**。

## 主要组件

### 类/结构体

- **io_lock**
- **rsx_iomap_table**

## 主要函数

- `unlock()`
- `get_addr()`
- `lock()`
- `try_lock()`
- `constexpr()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/mutex.h>
#include <Emu/CPU/CPUThread.h>
```

### 命名空间

- `iomap_helper`
- `rsx`

## 代码统计

- 总行数: 119
- 类/结构体数量: 2
- 函数数量: 5
- 枚举数量: 0

## 相关文件

*无直接关联文件*

