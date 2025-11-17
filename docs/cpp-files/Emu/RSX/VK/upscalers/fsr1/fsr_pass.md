# fsr_pass.cpp

**路径**: `VK/upscalers/fsr1/fsr_pass.cpp`  
**类型**: 实现文件  
**大小**: 13388 字节

## 文件描述

该文件是 RPCS3 RSX 模块的一部分，负责**Vulkan 图形 API 后端实现**。

## 主要组件

### 宏定义

```cpp
#define A_CPU
#define SAMPLE_EASU
#define SAMPLE_RCAS
#define SAMPLE_BILINEAR
#define SAMPLE_SLOW_FALLBACK
#define SAMPLE_RCAS
#define SAMPLE_EASU
#define SAMPLE_BILINEAR
#define SAMPLE_SLOW_FALLBACK
```

## 依赖关系

### 包含的头文件

```cpp
#include <../../vkutils/barriers.h>
#include <../../VKHelpers.h>
#include <../../VKResourceManager.h>
#include <../fsr_pass.h>
#include <3rdparty/GPUOpen/include/ffx_a.h>
#include <3rdparty/GPUOpen/include/ffx_fsr1.h>
#include <Emu/RSX/Program/Upscalers/FSR1/fsr_ubershader.glsl>
#include <Emu/RSX/Program/Upscalers/FSR1/fsr_ffx_a_flattened.inc>
#include <Emu/RSX/Program/Upscalers/FSR1/fsr_ffx_fsr1_flattened.inc>
```

### 命名空间

- `FidelityFX`
- `vk`

## 代码统计

- 总行数: 407
- 类/结构体数量: 0
- 函数数量: 0
- 枚举数量: 0

## 相关文件

*无直接关联文件*

