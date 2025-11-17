# Common - RSX 公共工具和数据结构

该目录包含 RSX 模块使用的公共工具类、数据结构和算法。

## 主要组件

### 缓冲管理

| 文件 | 描述 |
|------|------|
| [BufferUtils.cpp](BufferUtils.md) / [.h](BufferUtils.md) | 缓冲区工具函数 |
| [buffer_stream.hpp](buffer_stream.md) | 缓冲流处理 |
| [ring_buffer_helper.h](ring_buffer_helper.md) | 环形缓冲区辅助 |
| [io_buffer.h](io_buffer.md) | I/O 缓冲区 |

### 纹理处理

| 文件 | 描述 |
|------|------|
| [TextureUtils.cpp](TextureUtils.md) / [.h](TextureUtils.md) | 纹理工具函数 |
| [texture_cache.cpp](texture_cache.md) / [.h](texture_cache.md) | 纹理缓存核心 |
| [texture_cache_types.cpp](texture_cache_types.md) / [.h](texture_cache_types.md) | 纹理缓存类型定义 |
| [texture_cache_checker.h](texture_cache_checker.md) | 纹理缓存检查器 |
| [texture_cache_helpers.h](texture_cache_helpers.md) | 纹理缓存辅助函数 |
| [texture_cache_predictor.h](texture_cache_predictor.md) | 纹理缓存预测器 |
| [texture_cache_utils.h](texture_cache_utils.md) | 纹理缓存工具 |
| [tiled_dma_copy.hpp](tiled_dma_copy.md) | 平铺 DMA 复制 |

### 表面管理

| 文件 | 描述 |
|------|------|
| [surface_store.cpp](surface_store.md) / [.h](surface_store.md) | 表面存储 |
| [surface_utils.h](surface_utils.md) | 表面工具 |
| [surface_cache_dma.hpp](surface_cache_dma.md) | 表面缓存 DMA |

### 数据结构

| 文件 | 描述 |
|------|------|
| [bitfield.hpp](bitfield.md) | 位域操作 |
| [expected.hpp](expected.md) | Expected 类型（错误处理） |
| [ranged_map.hpp](ranged_map.md) | 范围映射 |
| [reverse_ptr.hpp](reverse_ptr.md) | 反向指针 |
| [simple_array.hpp](simple_array.md) | 简单数组 |
| [unordered_map.hpp](unordered_map.md) | 无序映射 |

### 工具类

| 文件 | 描述 |
|------|------|
| [profiling_timer.hpp](profiling_timer.md) | 性能分析计时器 |
| [time.hpp](time.md) | 时间工具 |

## 返回

[返回 RSX 主页](../README.md)
