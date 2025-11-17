# sync.hpp

**路径**: `GL/glutils/sync.hpp`  
**类型**: 头文件  
**大小**: 2109 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**OpenGL 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **fence**

### 枚举

- `flags`
- `err`

## 主要函数

- `is_empty()`
- `check_signaled()`
- `create()`
- `destroy()`
- `wait_for_signal()`
- `server_wait_sync()`
- `reset()`

## 依赖关系

### 包含的头文件

```cpp
#include <common.h>
```

### 命名空间

- `gl`

## 代码统计

- 总行数: 129
- 类/结构体数量: 1
- 函数数量: 7
- 枚举数量: 2

## 相关文件

*无直接关联文件*

