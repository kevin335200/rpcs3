# texture_cache_types.h

**路径**: `Common/texture_cache_types.h`  
**类型**: 头文件  
**大小**: 3275 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**RSX 模块的公共工具和数据结构**。

## 主要组件

### 类/结构体

- **component_order**
- **invalidation_cause**
- **enum_type**

### 枚举

- `invalidation_chain_direction`
- `component_order`
- `memory_read_flags`
- `flags`
- `enum_type`
- `invalidation_chain_policy`

## 主要函数

- `undefer()`
- `invalidation_cause()`
- `flag_bits_from_cause()`
- `defer()`

### 命名空间

- `rsx`

## 代码统计

- 总行数: 134
- 类/结构体数量: 3
- 函数数量: 4
- 枚举数量: 6

## 相关文件

- **实现文件**: [texture_cache_types.cpp](texture_cache_types.md)

