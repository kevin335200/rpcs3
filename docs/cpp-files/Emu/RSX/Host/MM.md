# MM.h

**路径**: `Host/MM.h`  
**类型**: 头文件  
**大小**: 710 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**主机内存管理**。

## 主要组件

### 类/结构体

- **MM_block**

### 枚举

- `mm_backend_ctrl`

## 主要函数

- `overlaps()`
- `mm_flush_lazy()`
- `mm_flush()`
- `mm_protect()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <util/vm.hpp>
#include <Emu/RSX/Common/simple_array.hpp>
#include <Utilities/address_range.h>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 37
- 类/结构体数量: 1
- 函数数量: 4
- 枚举数量: 1

## 相关文件

- **实现文件**: [MM.cpp](MM.md)

