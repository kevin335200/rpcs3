# RSX 图形系统模块

## 📌 模块概述

RSX (Reality Synthesizer) 是 PlayStation 3 的图形处理单元，基于 NVIDIA G70/G71 架构（类似 GeForce 7800）。RPCS3 通过 OpenGL 和 Vulkan 后端模拟 RSX 的功能。

**位置**: `/rpcs3/Emu/RSX/`

## 🎮 RSX 硬件特性

```
RSX Reality Synthesizer
├── 基于 NVIDIA G70/G71 架构
├── 550 MHz 核心频率
├── 256 MB GDDR3 显存
├── 支持 OpenGL ES 1.1 + 扩展
├── 固定功能 + 可编程管线
└── 最高 1080p 输出
```

## 📂 目录结构

```
rpcs3/Emu/RSX/
├── RSXThread.h/cpp         # RSX 主线程
├── GSRender.h/cpp          # 图形渲染器基类
├── RSXFIFO.cpp             # 命令 FIFO 队列
├── RSXZCULL.cpp            # Z-Cull 优化
├── RSXDisAsm.h/cpp         # RSX 命令反汇编
├── GCM.h                   # GCM (Graphics Command Memory)
├── gcm_enums.h             # GCM 枚举定义
├── rsx_utils.cpp           # RSX 工具函数
│
├── Common/                 # 通用代码
│   ├── texture_cache.h/cpp      # 纹理缓存
│   ├── surface_store.h/cpp      # 表面存储
│   ├── BufferUtils.h/cpp        # 缓冲区工具
│   ├── TextureUtils.h/cpp       # 纹理工具
│   ├── io_buffer.h              # IO 缓冲区
│   └── ring_buffer_helper.h     # 环形缓冲区辅助
│
├── Core/                   # 核心状态管理
│   ├── RSXContext.cpp           # RSX 上下文
│   ├── RSXDisplay.cpp           # 显示管理
│   ├── RSXDrawCommands.h/cpp    # 绘制命令
│   ├── RSXDriverState.h         # 驱动状态
│   ├── RSXFrameBuffer.h         # 帧缓冲
│   └── RSXVertexTypes.h         # 顶点类型
│
├── GL/                     # OpenGL 后端
│   ├── GLGSRender.h/cpp         # OpenGL 渲染器
│   ├── GLTexture.cpp            # OpenGL 纹理
│   ├── GLVertexProgram.cpp      # OpenGL 顶点着色器
│   ├── GLFragmentProgram.cpp    # OpenGL 片段着色器
│   └── glutils/                 # OpenGL 工具
│
├── VK/                     # Vulkan 后端
│   ├── VKGSRender.h/cpp         # Vulkan 渲染器
│   ├── VKTexture.cpp            # Vulkan 纹理
│   ├── VKVertexProgram.cpp      # Vulkan 顶点着色器
│   ├── VKFragmentProgram.cpp    # Vulkan 片段着色器
│   └── vkutils/                 # Vulkan 工具
│
├── Program/                # 着色器程序
│   ├── RSXVertexProgram.h       # 顶点程序
│   ├── RSXFragmentProgram.h     # 片段程序
│   └── GLSLInterpreter/         # GLSL 解释器
│
├── Overlays/               # 界面覆盖层
│   ├── overlay_manager.h/cpp    # 覆盖层管理器
│   ├── overlay_message.h/cpp    # 消息框
│   └── HomeMenu/                # 主菜单
│
└── Capture/                # 帧捕获和回放
    ├── rsx_trace.h              # RSX 跟踪
    └── rsx_replay.h             # RSX 回放
```

## 🎯 核心类详解

### 1. RSXThread - RSX 主线程

```cpp
class thread : public named_thread<GCM_context>
{
public:
    // RSX 命令 FIFO
    std::unique_ptr<FIFO> fifo_ctrl;

    // 当前显示缓冲区
    u32 display_buffers_count = 0;
    u32 current_display_buffer = 0;

    // 后端配置
    backend_configuration backend_config;

    // 执行 RSX 命令
    void task();

    // 处理中断
    void on_notify(u32 interrupt_bits);

    // 提交绘制调用
    virtual void begin();
    virtual void end();
    virtual void execute_nop_draw();
};
```

### 2. GSRender - 图形渲染器基类

所有渲染后端的抽象基类。

```cpp
class GSRender : public thread
{
public:
    // 后端类型
    enum backend_type
    {
        OpenGL,
        Vulkan,
        Null
    };

    // 纹理缓存
    std::unique_ptr<texture_cache> m_texture_cache;

    // 顶点输入状态
    rsx::vertex_input_layout vertex_layout;

    // 当前渲染目标
    rsx::gcm_framebuffer_info current_framebuffer;

    // 纯虚函数 - 在派生类中实现
    virtual void clear_surface(u32 mask) = 0;
    virtual void draw_command(rsx::draw_command_t cmd) = 0;
    virtual void flip(const rsx::display_flip_info_t& info) = 0;
};
```

### 3. backend_configuration - 后端配置

```cpp
struct backend_configuration
{
    bool supports_multidraw;              // 批量绘制调用
    bool supports_hw_a2c;                 // 硬件 Alpha to Coverage
    bool supports_hw_msaa;                // 硬件多重采样
    bool supports_hw_conditional_render;  // 条件渲染
    bool supports_asynchronous_compute;   // 异步计算
    bool supports_host_gpu_labels;        // GPU 标签同步
    bool supports_normalized_barycentrics; // 归一化重心坐标
};
```

### 4. 中断原因枚举

```cpp
enum eng_interrupt_reason : u32
{
    backend_interrupt       = 0x0001,  // 后端相关中断
    memory_config_interrupt = 0x0002,  // 内存配置改变
    display_interrupt       = 0x0004,  // 显示处理
    pipe_flush_interrupt    = 0x0008,  // 管线刷新
    dma_control_interrupt   = 0x0010,  // DMA 中断

    all_interrupt_bits = memory_config_interrupt |
                        backend_interrupt |
                        display_interrupt |
                        pipe_flush_interrupt
};
```

## 🖼️ 纹理系统

### 纹理缓存 (texture_cache)
```cpp
class texture_cache
{
public:
    // 查找或创建纹理
    texture_handle find_texture(const rsx::gcm_texture_format& format,
                                u32 address,
                                u32 width, u32 height);

    // 上传纹理数据
    void upload_texture(texture_handle tex, const void* data);

    // 失效纹理
    void invalidate(u32 address, u32 size);

    // 刷新缓存
    void flush();
};
```

### GCM 纹理格式
```cpp
enum gcm_texture_format : u8
{
    CELL_GCM_TEXTURE_B8        = 0x81, // 8 位
    CELL_GCM_TEXTURE_A8R8G8B8  = 0x85, // 32 位 ARGB
    CELL_GCM_TEXTURE_R5G6B5    = 0x86, // 16 位 RGB
    CELL_GCM_TEXTURE_COMPRESSED_DXT1 = 0x8C, // DXT1 压缩
    CELL_GCM_TEXTURE_COMPRESSED_DXT3 = 0x8E, // DXT3 压缩
    CELL_GCM_TEXTURE_COMPRESSED_DXT5 = 0x8F, // DXT5 压缩
    // ... 更多格式
};
```

## 🎨 着色器系统

### 顶点程序
```cpp
struct RSXVertexProgram
{
    // 顶点着色器指令
    std::vector<u32> instructions;

    // 输入属性
    struct input_attrib
    {
        u8 location;           // 属性位置
        u8 frequency;          // 频率
        vertex_base_type type; // 类型
    };

    // 输出属性
    struct output_attrib
    {
        u8 location;
        std::string name;
    };

    std::vector<input_attrib> inputs;
    std::vector<output_attrib> outputs;
};
```

### 片段程序
```cpp
struct RSXFragmentProgram
{
    // 片段着色器指令
    std::vector<u32> instructions;

    // 纹理维度
    u32 textures_alpha_kill;
    u32 textures_zfunc;

    // 输出目标
    u32 output_color_count;

    // 控制标志
    bool back_color_enabled;
    bool front_color_enabled;
};
```

## 🔧 OpenGL 后端

### GLGSRender - OpenGL 渲染器
```cpp
class GLGSRender : public GSRender
{
public:
    // OpenGL 上下文
    GLContext gl_context;

    // VAO (Vertex Array Object)
    GLuint m_vao;

    // FBO (Framebuffer Object)
    std::unique_ptr<gl::framebuffer_holder> m_draw_fbo;

    // 实现虚函数
    void clear_surface(u32 mask) override;
    void draw_command(rsx::draw_command_t cmd) override;
    void flip(const rsx::display_flip_info_t& info) override;

private:
    // 编译着色器
    void compile_shader(GLuint shader, const std::string& source);

    // 链接程序
    void link_program(GLuint program);
};
```

### OpenGL 状态管理
```cpp
namespace gl
{
    class state_tracker
    {
        // 跟踪 OpenGL 状态避免冗余调用
        GLenum current_blend_func_src;
        GLenum current_blend_func_dst;
        bool depth_test_enabled;
        bool blend_enabled;

    public:
        void enable_blend() {
            if (!blend_enabled) {
                glEnable(GL_BLEND);
                blend_enabled = true;
            }
        }

        void set_blend_func(GLenum src, GLenum dst) {
            if (current_blend_func_src != src ||
                current_blend_func_dst != dst)
            {
                glBlendFunc(src, dst);
                current_blend_func_src = src;
                current_blend_func_dst = dst;
            }
        }
    };
}
```

## 🌋 Vulkan 后端

### VKGSRender - Vulkan 渲染器
```cpp
class VKGSRender : public GSRender
{
public:
    // Vulkan 设备
    vk::device* m_device;

    // 交换链
    vk::swapchain* m_swapchain;

    // 命令缓冲区
    vk::command_buffer* m_current_command_buffer;

    // 描述符集
    vk::descriptor_set_pool* m_descriptor_pool;

    // 管线缓存
    vk::pipeline_cache m_pipeline_cache;

    // 实现虚函数
    void clear_surface(u32 mask) override;
    void draw_command(rsx::draw_command_t cmd) override;
    void flip(const rsx::display_flip_info_t& info) override;

private:
    // 创建管线
    VkPipeline create_graphics_pipeline(
        const rsx::vertex_program& vp,
        const rsx::fragment_program& fp);
};
```

### Vulkan 同步
```cpp
namespace vk
{
    struct fence_manager
    {
        VkDevice device;
        std::vector<VkFence> fences;

        // 等待栅栏
        void wait(VkFence fence, u64 timeout = UINT64_MAX)
        {
            vkWaitForFences(device, 1, &fence, VK_TRUE, timeout);
        }

        // 重置栅栏
        void reset(VkFence fence)
        {
            vkResetFences(device, 1, &fence);
        }
    };
}
```

## 📊 绘制命令

### draw_command_t
```cpp
struct draw_command_t
{
    draw_command command_type;  // 绘制类型
    u32 first_count_commands;   // 第一个计数命令
    u32 vertex_count;            // 顶点数量
    u32 index_count;             // 索引数量

    union
    {
        struct
        {
            u32 start;
            u32 count;
        } inline_vertex_array;

        struct
        {
            rsx::index_array_type type;
            u32 offset;
        } indexed_array;
    };
};
```

### 绘制类型
```cpp
enum class draw_command : u8
{
    none,
    arrays,              // 顶点数组绘制
    indexed,             // 索引绘制
    inlined_array,       // 内联数组
};
```

## 🖥️ 显示管理

### 帧缓冲信息
```cpp
struct gcm_framebuffer_info
{
    u32 address;          // 帧缓冲地址
    u32 pitch;            // 行距
    u16 width;            // 宽度
    u16 height;           // 高度
    u8 color_format;      // 颜色格式
    u8 depth_format;      // 深度格式
    u8 target;            // 渲染目标索引
    u8 aa_mode;           // 抗锯齿模式
};
```

### 显示翻转
```cpp
struct display_flip_info_t
{
    u32 buffer;                // 显示缓冲区索引
    u64 timestamp;             // 时间戳
    u32 stats;                 // 统计信息
    u32 async_flip;            // 异步翻转标志
};
```

## 🎓 学习要点

### 1. 图形管线流程
```
顶点数据
    ↓
[顶点着色器] → 转换顶点
    ↓
[图元装配] → 组装三角形
    ↓
[光栅化] → 生成片段
    ↓
[片段着色器] → 计算颜色
    ↓
[深度/模板测试]
    ↓
[混合]
    ↓
帧缓冲区
```

### 2. 纹理映射流程
```
PS3 纹理地址
    ↓
[解码格式] → 识别 GCM 格式
    ↓
[上传到 GPU] → OpenGL/Vulkan 纹理
    ↓
[缓存] → 避免重复上传
    ↓
[采样] → 在着色器中使用
```

### 3. 命令处理
```
GCM 命令队列 (FIFO)
    ↓
[RSXThread 读取]
    ↓
[命令解码] → 识别命令类型
    ↓
[状态更新] → 更新 RSX 状态
    ↓
[提交绘制] → 调用后端渲染
```

## 💡 实际代码示例

### 示例 1: 创建 OpenGL 纹理
```cpp
void upload_texture_gl(const rsx::gcm_texture& tex)
{
    GLuint gl_tex;
    glGenTextures(1, &gl_tex);
    glBindTexture(GL_TEXTURE_2D, gl_tex);

    // 设置纹理参数
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // 上传纹理数据
    GLenum format = get_gl_format(tex.format);
    glTexImage2D(GL_TEXTURE_2D, 0, format,
                 tex.width, tex.height, 0,
                 format, GL_UNSIGNED_BYTE, tex.data);
}
```

### 示例 2: Vulkan 绘制调用
```cpp
void VKGSRender::draw_command(rsx::draw_command_t cmd)
{
    // 绑定管线
    vkCmdBindPipeline(m_current_command_buffer,
                      VK_PIPELINE_BIND_POINT_GRAPHICS,
                      m_current_pipeline);

    // 绑定描述符集
    vkCmdBindDescriptorSets(m_current_command_buffer,
                            VK_PIPELINE_BIND_POINT_GRAPHICS,
                            m_pipeline_layout,
                            0, 1, &m_descriptor_set, 0, nullptr);

    // 绘制
    if (cmd.command_type == draw_command::indexed)
    {
        vkCmdDrawIndexed(m_current_command_buffer,
                         cmd.index_count, 1, 0, 0, 0);
    }
    else
    {
        vkCmdDraw(m_current_command_buffer,
                  cmd.vertex_count, 1, 0, 0);
    }
}
```

### 示例 3: 着色器编译
```cpp
std::string convert_vertex_program_to_glsl(const RSXVertexProgram& vp)
{
    std::string source = "#version 430\n";

    // 添加输入
    for (const auto& input : vp.inputs)
    {
        source += fmt::format("layout(location = %d) in vec4 in_%s;\n",
                             input.location, input.name);
    }

    // 添加输出
    for (const auto& output : vp.outputs)
    {
        source += fmt::format("out vec4 %s;\n", output.name);
    }

    // 主函数
    source += "void main() {\n";
    // ... 转换 VP 指令为 GLSL
    source += "}\n";

    return source;
}
```

## 🔍 调试技巧

### 1. 帧捕获
```cpp
// 捕获单帧进行分析
if (g_user_asked_for_frame_capture)
{
    frame_capture.start_capture();
    // 执行一帧
    frame_capture.end_capture();
    frame_capture.save_to_file("frame_capture.rrc");
}
```

### 2. 命令日志
```cpp
// 记录 RSX 命令
void log_gcm_command(u32 cmd, u32 args_count)
{
    rsx_log.trace("GCM Command: 0x%08X, args=%d", cmd, args_count);
}
```

### 3. 性能分析
```cpp
// 性能计时器
profiling_timer timer;
timer.start();

// 执行渲染
render_frame();

timer.stop();
rsx_log.notice("Frame time: %.2f ms", timer.duration_ms());
```

## 📊 性能优化

### 1. 批量绘制
- 合并多个小的绘制调用
- 减少驱动开销

### 2. 纹理缓存
- 避免重复上传相同纹理
- 使用 LRU 策略淘汰旧纹理

### 3. 着色器缓存
- 缓存编译好的着色器
- 避免运行时重新编译

### 4. 异步上传
- 使用单独的线程上传纹理
- 减少主线程等待时间

## 🔗 相关模块

- **CPU**: PPU 线程调用 RSX 命令
- **Memory**: RSX 访问主内存和显存
- **Cell/lv2**: sys_rsx 系统调用

---

## 📚 下一步

- [返回总览](./01-RPCS3-项目总览.md)
- [上一章: CPU 模拟](./03-CPU-模拟.md)
- [下一章: Cell 处理器](./05-Cell-处理器.md)

---

**提示**: RSX 图形系统非常复杂。建议先理解基本的图形管线概念，然后再深入具体的 OpenGL/Vulkan 实现。
