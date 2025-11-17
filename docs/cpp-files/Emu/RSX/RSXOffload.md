# RSXOffload.h

**路径**: `RSXOffload.h`  
**类型**: 头文件  
**大小**: 2062 字节

## 文件描述

该文件是 RPCS3 RSX (Reality Synthesizer) 图形模拟器的一部分。

## 主要组件

### 类/结构体

- **named_thread**
- **dma_manager**
- **transport_packet**
- **offload_thread**

### 枚举

- `op`

## 主要函数

- `emulate_as_indexed()`
- `is_current_thread()`
- `set_mem_fault_flag()`
- `backend_ctrl()`
- `get_fault_range()`
- `join()`
- `copy()`
- `init()`
- `clear_mem_fault_flag()`
- `sync()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <Utilities/address_range.h>
#include <gcm_enums.h>
#include <vector>
```

### 命名空间

- `rsx`

## 代码统计

- 总行数: 88
- 类/结构体数量: 4
- 函数数量: 10
- 枚举数量: 1

## 相关文件

- **实现文件**: [RSXOffload.cpp](RSXOffload.md)

