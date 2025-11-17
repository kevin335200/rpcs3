# texture_cache_checker.h

**路径**: `Common/texture_cache_checker.h`  
**类型**: 头文件  
**大小**: 6523 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **tex_cache_checker_t**
- **per_page_info_t**

## 主要函数

- `remove()`
- `reset_refcount()`
- `check_unprotected()`
- `set_protection()`
- `verify()`
- `prot_to_str()`
- `get_minimum_number_of_sections()`
- `discard()`
- `index_to_rsx_address()`
- `add()`

## 依赖关系

### 包含的头文件

```cpp
#include <../rsx_utils.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 217
- 类/结构体数量: 2
- 函数数量: 10
- 枚举数量: 0

## 相关文件

*无直接关联文件*

