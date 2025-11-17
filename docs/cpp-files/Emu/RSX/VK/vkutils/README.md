# vkutils - Vulkan 工具库

Vulkan 辅助工具类和封装。

## 核心工具

| 文件 | 描述 |
|------|------|
| [device.cpp](device.md) / [.h](device.md) | Vulkan 设备管理 |
| [instance.cpp](instance.md) / [.h](instance.md) | Vulkan 实例管理 |
| [shared.cpp](shared.md) / [.h](shared.md) | 共享工具 |
| [ex.cpp](ex.md) / [.h](ex.md) | 异常处理 |

## 内存管理

| 文件 | 描述 |
|------|------|
| [memory.cpp](memory.md) / [.h](memory.md) | 内存分配器 |
| [data_heap.cpp](data_heap.md) / [.h](data_heap.md) | 数据堆 |
| [garbage_collector.h](garbage_collector.md) | 垃圾回收器 |

## 资源对象

| 文件 | 描述 |
|------|------|
| [buffer_object.cpp](buffer_object.md) / [.h](buffer_object.md) | 缓冲对象 |
| [image.cpp](image.md) / [.h](image.md) | 图像对象 |
| [image_helpers.cpp](image_helpers.md) / [.h](image_helpers.md) | 图像辅助函数 |
| [sampler.cpp](sampler.md) / [.h](sampler.md) | 采样器 |
| [unique_resource.cpp](unique_resource.md) / [.h](unique_resource.md) | 唯一资源 |

## 命令和同步

| 文件 | 描述 |
|------|------|
| [commands.cpp](commands.md) / [.h](commands.md) | 命令缓冲 |
| [barriers.cpp](barriers.md) / [.h](barriers.md) | 内存屏障 |
| [sync.cpp](sync.md) / [.h](sync.md) | 同步原语 |

## 管线和描述符

| 文件 | 描述 |
|------|------|
| [descriptors.cpp](descriptors.md) / [.h](descriptors.md) | 描述符集 |
| [pipeline_binding_table.h](pipeline_binding_table.md) | 管线绑定表 |
| [graphics_pipeline_state.hpp](graphics_pipeline_state.md) | 图形管线状态 |

## 渲染资源

| 文件 | 描述 |
|------|------|
| [framebuffer_object.hpp](framebuffer_object.md) | 帧缓冲对象 |
| [swapchain.cpp](swapchain.md) / [.h](swapchain.md) | 交换链 |
| [swapchain_core.h](swapchain_core.md) | 交换链核心 |
| [swapchain_win32.hpp](swapchain_win32.md) | Windows 交换链 |
| [swapchain_unix.hpp](swapchain_unix.md) | Unix/Linux 交换链 |
| [swapchain_macos.hpp](swapchain_macos.md) | macOS 交换链 |
| [swapchain_android.hpp](swapchain_android.md) | Android 交换链 |

## 其他工具

| 文件 | 描述 |
|------|------|
| [chip_class.cpp](chip_class.md) / [.h](chip_class.md) | GPU 芯片类别检测 |
| [scratch.cpp](scratch.md) / [.h](scratch.md) | 临时缓冲 |
| [query_pool.hpp](query_pool.md) | 查询池 |

## 返回

[返回 VK 目录](../README.md)
