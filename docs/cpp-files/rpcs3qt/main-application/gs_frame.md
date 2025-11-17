# gs_frame.h/cpp

## Overview
The game screen frame class manages the rendering window for RPCS3, handling display, input, fullscreen transitions, mouse behavior, and video recording.

## Class Hierarchy
```
QWindow (Qt)
    └── gs_frame
            └── GSFrameBase (RPCS3)
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/gs_frame.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/gs_frame.cpp`

## Class Declaration
```cpp
class gs_frame : public QWindow, public GSFrameBase
{
    Q_OBJECT
public:
    explicit gs_frame(QScreen* screen, const QRect& geometry,
                     const QIcon& appIcon,
                     std::shared_ptr<gui_settings> gui_settings,
                     bool force_fullscreen);
    ~gs_frame();
    // ...
};
```

## Key Features

### 1. Qt Features
- **Multiple Inheritance**: Inherits from both QWindow and GSFrameBase
- **Q_OBJECT**: Uses Qt's Meta-Object system
- **Event Handling**: Overrides paint, show, mouse events

### 2. Rendering Context Management
```cpp
draw_context_t make_context() override;
void set_current(draw_context_t context) override;
void delete_context(draw_context_t context) override;
```

### 3. Display Modes
```cpp
enum class Visibility
{
    Windowed,
    Fullscreen,
    Hidden
};

Visibility m_last_visibility = Visibility::Windowed;
Visibility m_visibility = Visibility::Windowed;

void toggle_fullscreen() override;
```

## Mouse Management

### Mouse Configuration
```cpp
private:
    atomic_t<bool> m_show_mouse = true;
    bool m_disable_mouse = false;
    bool m_disable_kb_hotkeys = false;
    bool m_mouse_hide_and_lock = false;
    bool m_show_mouse_in_fullscreen = false;
    bool m_lock_mouse_in_fullscreen = true;
    bool m_hide_mouse_after_idletime = false;
    u32 m_hide_mouse_idletime = 2000; // ms
```

### Mouse Control Methods
```cpp
bool get_mouse_lock_state();
void toggle_mouselock();
void update_cursor();
void handle_cursor(Visibility visibility, bool visibility_changed,
                  bool active_changed, bool start_idle_timer);
```

### Mouse Hide Timer
```cpp
private:
    QTimer m_mousehide_timer;

private Q_SLOTS:
    void mouse_hide_timeout();
```

## Taskbar Progress

### Progress Indicator
```cpp
private:
    std::unique_ptr<progress_indicator> m_progress_indicator;

public:
    void progress_reset(bool reset_limit = false);
    void progress_set_value(int value);
    void progress_increment(int delta);
    void progress_set_limit(int limit);
```

Usage in operations like:
- Shader compilation
- Game loading
- PPU/SPU cache building

## Frame Presentation

### Frame Display
```cpp
bool can_consume_frame() const override;
void present_frame(std::vector<u8>&& data, u32 pitch, u32 width,
                  u32 height, bool is_bgra) const override;
void take_screenshot(std::vector<u8>&& data, u32 sshot_width,
                    u32 sshot_height, bool is_bgra) override;
```

### Flip Control
```cpp
void flip(draw_context_t context, bool skip_frame = false) override;
bool m_flip_showed_frame = false;
```

## Video Recording

### Video Encoder
```cpp
private:
    std::shared_ptr<utils::video_encoder> m_video_encoder{};

    void toggle_recording();
```

## Shortcut Handling

### Keyboard Shortcuts
```cpp
private:
    shortcut_handler* m_shortcut_handler = nullptr;

    void update_shortcuts();

private Q_SLOTS:
    void handle_shortcut(gui::shortcuts::shortcut shortcut_key,
                        const QKeySequence& key_sequence);
```

Shortcuts support:
- Fullscreen toggle
- Screenshot capture
- Video recording
- Mouse lock toggle

## Window Geometry

### Geometry Management
```cpp
private:
    QRect m_initial_geometry;

public:
    int client_width() override;
    int client_height() override;
    f64 client_display_rate() override;
```

## Window State

### Lifecycle Management
```cpp
protected:
    void close() override;
    void reset() override;
    bool shown() override;
    void hide() override;
    void show() override;

private:
    atomic_t<bool> m_is_closing = false;
    bool m_ignore_stop_events = false;
    bool m_start_games_fullscreen = false;
```

## Event Handling

### Qt Events
```cpp
protected:
    void paintEvent(QPaintEvent *event) override;
    void showEvent(QShowEvent *event) override;
    void mouseDoubleClickEvent(QMouseEvent* ev) override;
    bool event(QEvent* ev) override;
```

## Display Information

### Display Properties
```cpp
display_handle_t handle() const override;
f64 client_display_rate() override;
bool has_alpha() override;
```

## Frame Statistics

### Performance Tracking
```cpp
private:
    u64 m_frames = 0;
    std::string m_window_title;
```

## Settings Integration

### GUI Settings
```cpp
private:
    std::shared_ptr<gui_settings> m_gui_settings;

    void load_gui_settings();
```

Loaded settings include:
- Mouse behavior
- Fullscreen preferences
- Display options
- Shortcut configurations

## Renderer Type

### Video Renderer
```cpp
protected:
    video_renderer m_renderer;

public:
    video_renderer renderer() const { return m_renderer; }
```

Supports:
- Null renderer (no display)
- OpenGL renderer
- Vulkan renderer

## Special Features

### Hide on Close
```cpp
private:
    void hide_on_close();

public:
    void ignore_stop_events() { m_ignore_stop_events = true; }
```

Used for emulation suspension instead of complete shutdown.

## Usage Example

```cpp
// Create game screen frame
QScreen* screen = QApplication::primaryScreen();
QRect geometry(100, 100, 1280, 720);
QIcon appIcon(":/rpcs3.ico");
auto gui_settings = std::make_shared<gui_settings>();

gs_frame* frame = new gs_frame(screen, geometry, appIcon,
                               gui_settings, false);
frame->show();

// Configure mouse behavior
frame->get_mouse_lock_state(); // Lock mouse if needed

// Show progress during loading
frame->progress_set_limit(100);
frame->progress_set_value(50);

// Toggle fullscreen
frame->toggle_fullscreen();

// Take screenshot
// (called internally by emulator)
```

## Dependencies

### Qt Modules
- QtCore (QWindow, QTimer)
- QtGui (QPaintEvent, QScreen)

### RPCS3 Modules
- GSFrameBase (rendering backend)
- gui_settings
- shortcut_handler
- progress_indicator
- video_encoder (media utils)

## Notes
- Base class for OpenGL and Vulkan frame implementations
- Manages window visibility and display state
- Handles mouse locking for FPS games
- Supports video recording to file
- Provides taskbar progress feedback
- Implements fullscreen transitions
- Auto-hides cursor after idle time
- Double-click for fullscreen toggle
