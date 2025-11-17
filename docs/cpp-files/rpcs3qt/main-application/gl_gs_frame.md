# gl_gs_frame.h/cpp

## Overview
The OpenGL game screen frame class provides OpenGL-specific rendering context management for the game window.

## Class Hierarchy
```
QWindow (Qt)
    └── gs_frame
            └── gl_gs_frame
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/gl_gs_frame.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/gl_gs_frame.cpp`

## Class Declaration
```cpp
class gl_gs_frame : public gs_frame
{
public:
    explicit gl_gs_frame(QScreen* screen, const QRect& geometry,
                        const QIcon& appIcon,
                        std::shared_ptr<gui_settings> gui_settings,
                        bool force_fullscreen);

    void reset() override;
    draw_context_t make_context() override;
    void set_current(draw_context_t ctx) override;
    void delete_context(draw_context_t ctx) override;
    void flip(draw_context_t context, bool skip_frame = false) override;
};
```

## OpenGL Context

### GLContext Structure
```cpp
struct GLContext
{
    QSurface *surface = nullptr;
    QOpenGLContext *handle = nullptr;
    bool owner = false;
};
```

**Members:**
- `surface` - Qt surface for rendering
- `handle` - OpenGL context handle
- `owner` - Whether this context owns the handle

## Member Variables

### Surface Format
```cpp
private:
    QSurfaceFormat m_format;
```

Defines OpenGL context attributes:
- OpenGL version
- Profile (Core/Compatibility)
- Color depth
- Depth/stencil buffer
- Double buffering
- V-Sync

### Primary Context
```cpp
private:
    GLContext *m_primary_context = nullptr;
```

The main rendering context for the window.

## Override Methods

### Reset
```cpp
void reset() override;
```

Resets the OpenGL frame:
- Destroys existing contexts
- Resets surface format
- Reinitializes rendering

### Context Management

#### Make Context
```cpp
draw_context_t make_context() override;
```

Creates a new OpenGL context:
- Allocates GLContext structure
- Creates QOpenGLContext
- Configures surface format
- Returns context handle

#### Set Current
```cpp
void set_current(draw_context_t ctx) override;
```

Makes an OpenGL context current:
- Binds context to surface
- Makes context active for rendering
- Thread-safe context switching

#### Delete Context
```cpp
void delete_context(draw_context_t ctx) override;
```

Destroys an OpenGL context:
- Releases OpenGL resources
- Destroys QOpenGLContext
- Frees GLContext structure

### Frame Flip
```cpp
void flip(draw_context_t context, bool skip_frame = false) override;
```

Swaps buffers:
- Presents rendered frame
- Handles V-Sync
- Supports frame skipping

## OpenGL Surface Format Configuration

Typical format setup:
```cpp
QSurfaceFormat format;
format.setVersion(4, 3);              // OpenGL 4.3
format.setProfile(QSurfaceFormat::CoreProfile);
format.setDepthBufferSize(24);
format.setStencilBufferSize(8);
format.setRedBufferSize(8);
format.setGreenBufferSize(8);
format.setBlueBufferSize(8);
format.setAlphaBufferSize(8);
format.setSwapBehavior(QSurfaceFormat::DoubleBuffer);
format.setSwapInterval(1);            // V-Sync on
```

## Context Sharing

OpenGL contexts can be shared for:
- Texture sharing between threads
- Shader program sharing
- Buffer object sharing

## Usage Example

```cpp
// Create OpenGL frame
QScreen* screen = QApplication::primaryScreen();
QRect geometry(100, 100, 1280, 720);
QIcon appIcon(":/rpcs3.ico");
auto gui_settings = std::make_shared<gui_settings>();

gl_gs_frame* gl_frame = new gl_gs_frame(screen, geometry, appIcon,
                                        gui_settings, false);
gl_frame->show();

// Create rendering context
draw_context_t ctx = gl_frame->make_context();

// Make context current for rendering
gl_frame->set_current(ctx);

// ... OpenGL rendering code ...

// Swap buffers
gl_frame->flip(ctx);

// Cleanup
gl_frame->delete_context(ctx);
```

## Integration with GLGSRender

The gl_gs_frame works with the GLGSRender backend:

```cpp
// In GLGSRender initialization
draw_context_t context = frame->make_context();
frame->set_current(context);

// Initialize OpenGL state
glEnable(GL_DEPTH_TEST);
glEnable(GL_BLEND);
// ...

// In render loop
frame->set_current(context);
// Render frame
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
// Draw geometry
frame->flip(context);
```

## Thread Safety

- Context creation/deletion is thread-safe
- `set_current()` binds context to calling thread
- Multiple contexts can exist simultaneously
- Only one context can be current per thread

## Dependencies

### Qt Modules
- QtCore (QSurface)
- QtGui (QOpenGLContext, QSurfaceFormat)

### RPCS3 Modules
- gs_frame (base class)
- gui_settings

## Platform-Specific Behavior

### Windows
- Uses WGL (Windows OpenGL) backend
- Supports desktop OpenGL

### Linux
- Uses GLX (X11) or EGL
- Supports desktop OpenGL

### macOS
- Uses NSOpenGL/CGL
- Limited to OpenGL 4.1 (deprecated)
- Consider Vulkan via MoltenVK

## Performance Considerations

1. **Context Switching**
   - Minimize context switches
   - Batch rendering operations

2. **V-Sync**
   - Controlled by swap interval
   - Can be disabled for performance

3. **Double Buffering**
   - Prevents tearing
   - Standard for game rendering

4. **Buffer Sizes**
   - 24-bit depth buffer standard
   - 8-bit stencil sufficient for most cases

## Notes
- Specializes gs_frame for OpenGL rendering
- Manages QOpenGLContext lifecycle
- Supports context sharing for multi-threaded rendering
- Handles surface format configuration
- Platform-independent OpenGL setup
- Works with GLGSRender backend
