# RSXZCULL.h

**路径**: `RSXZCULL.h`  
**类型**: 头文件  
**大小**: 8167 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Z-Cull 遮挡查询**。

## 主要组件

### 类/结构体

- **thread**
- **occlusion_query_info**
- **queued_report_write**
- **query_search_result**
- **query_stat_counter**
- **sync_hint_payload_t**
- **MMIO_page_data_t** (继承自: `rsx::ref_counted`)
- **ZCULL_control**
- **for**
- **conditional_render_eval**

### 枚举

- `sync_control`
- `constants`

## 主要函数

- `set_active()`
- `clear()`
- `is_query_result_urgent()`
- `end_occlusion_query()`
- `classify_location()`
- `begin_occlusion_query()`
- `on_access_violation()`
- `allocate_new_query()`
- `check_occlusion_query_status()`
- `check_state()`
- `copy_reports_to()`
- `read_report()`
- `retire()`
- `on_sync_hint()`
- `free_query()`
- `has_pending()`
- `find_query()`
- `on_draw()`
- `read_barrier()`
- `on_report_completed()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/types.hpp>
#include <util/vm.hpp>
#include <Emu/Memory/vm.h>
#include <Utilities/mutex.h>
#include <rsx_utils.h>
#include <vector>
#include <stack>
#include <unordered_map>
```

### 命名空间

- `rsx`
- `reports`

## 代码统计

- 总行数: 246
- 类/结构体数量: 10
- 函数数量: 28
- 枚举数量: 2

## 相关文件

- **实现文件**: [RSXZCULL.cpp](RSXZCULL.md)

