# VKMemAlloc.cpp

**路径**: `VK/VKMemAlloc.cpp`  
**类型**: 实现文件  
**大小**: 1869 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 类/结构体

- **VmaRWMutex**

### 宏定义

```cpp
#define VMA_IMPLEMENTATION
#define VMA_VULKAN_VERSION
#define VMA_ATOMIC_UINT32
#define VMA_ATOMIC_UINT64
#define compare_exchange_strong
#define compare_exchange_weak
#define VMA_RW_MUTEX
#define VMA_MUTEX
```

## 主要函数

- `UnlockRead()`
- `Unlock()`
- `LockRead()`
- `LockWrite()`
- `Lock()`
- `TryLockRead()`
- `UnlockWrite()`
- `TryLock()`
- `TryLockWrite()`

## 依赖关系

### 包含的头文件

```cpp
#include <util/atomic.hpp>
#include <Utilities/mutex.h>
#include <atomic>
#include <thread>
#include <memory>
#include <mutex>
#include <vk_mem_alloc.h>
```

## 代码统计

- 总行数: 63
- 类/结构体数量: 1
- 函数数量: 9
- 枚举数量: 0

## 相关文件

*无直接关联文件*

