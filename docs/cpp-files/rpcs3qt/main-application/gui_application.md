# gui_application.h/cpp

## Overview
The GUI application class is the main application controller for RPCS3, extending QApplication and managing the entire GUI lifecycle, settings, and system callbacks.

## Class Hierarchy
```
QApplication (Qt)
    └── gui_application
            └── main_application (interface)
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/gui_application.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/gui_application.cpp`

## Class Declaration
```cpp
class gui_application : public QApplication, public main_application
{
    Q_OBJECT
public:
    gui_application(int& argc, char** argv);
    ~gui_application();

    bool Init() override;
    std::unique_ptr<gs_frame> get_gs_frame();

    main_window* m_main_window = nullptr;
    // ...
};
```

## Key Features

### 1. Qt Features
- **Multiple Inheritance**: Inherits from both QApplication and main_application
- **Native Event Filtering**: Implements QAbstractNativeEventFilter for low-level events
- **Translation Support**: Dynamic language switching with QTranslator

### 2. Application Mode Configuration
```cpp
void SetShowGui(bool show_gui = true);
void SetUseCliStyle(bool use_cli_style = false);
void SetWithCliBoot(bool with_cli_boot = false);
void SetStartGamesFullscreen(bool start_games_fullscreen = false);
void SetGameScreenIndex(int screen_index = -1);
```

## Important Signals

### Emulation Control Signals
```cpp
Q_SIGNALS:
    void OnEmulatorRun(bool start_playtime);
    void OnEmulatorPause();
    void OnEmulatorResume(bool start_playtime);
    void OnEmulatorStop();
    void OnEmulatorReady();
    void OnEnableDiscEject(bool enabled);
    void OnEnableDiscInsert(bool enabled);
```

### Thread Communication
```cpp
Q_SIGNALS:
    void RequestCallFromMainThread(std::function<void()> func,
                                   atomic_t<u32>* wake_up);
```

## Private Slots

### UI Updates
```cpp
private Q_SLOTS:
    void OnChangeStyleSheetRequest();
    void OnShortcutChange();
    void OnAppStateChanged(Qt::ApplicationState state);
    static void CallFromMainThread(const std::function<void()>& func,
                                   atomic_t<u32>* wake_up);
```

## Native Event Filter

### Platform-Specific Event Handling
```cpp
class native_event_filter : public QAbstractNativeEventFilter
{
public:
    bool nativeEventFilter(const QByteArray& eventType,
                          void* message,
                          qintptr* result) override;
} m_native_event_filter;
```

The native event filter handles:
- Raw input events
- System messages
- Platform-specific notifications

## Translation System

### Language Management
```cpp
private:
    QTranslator m_translator;
    QString m_language_code;
    static s32 m_language_id;

    void SwitchTranslator(QTranslator& translator,
                         const QString& filename,
                         const QString& language_code);
    void LoadLanguage(const QString& language_code);
    static QStringList GetAvailableLanguageCodes();
```

### Language ID
```cpp
static s32 get_language_id();
```

## Playtime Tracking

### Timer Management
```cpp
private:
    QTimer m_timer;
    QElapsedTimer m_timer_playtime;

    void StartPlaytime(bool start_playtime);
    void UpdatePlaytime();
    void StopPlaytime();
```

## Sound Effects

### Audio Management
```cpp
private:
    std::deque<std::unique_ptr<QSoundEffect>> m_sound_effects{};
```

## Settings Management

### Three-Tier Settings System
```cpp
private:
    std::shared_ptr<emu_settings> m_emu_settings;
    std::shared_ptr<gui_settings> m_gui_settings;
    std::shared_ptr<persistent_settings> m_persistent_settings;
```

## Pause on Focus Loss

### Focus Management
```cpp
private:
    u64 m_pause_amend_time_on_focus_loss = umax;
    u64 m_pause_delayed_tag = 0;
    typename Emulator::stop_counter_t m_emu_focus_out_emulation_id{};
    bool m_is_pause_on_focus_loss_active = false;
```

## Application Flags

### Configuration Flags
```cpp
private:
    bool m_show_gui = true;
    bool m_use_cli_style = false;
    bool m_with_cli_boot = false;
    bool m_start_games_fullscreen = false;
    int m_game_screen_index = -1;
```

## Windows-Specific Features

### Device Notification (Windows Only)
```cpp
#ifdef _WIN32
    void register_device_notification(WId window_id);
    void unregister_device_notification();
    HDEVNOTIFY m_device_notification_handle {};
#endif
```

Handles:
- USB device insertion/removal
- Controller connection/disconnection
- Storage device changes

## Initialization

### Callbacks Setup
```cpp
private:
    void InitializeCallbacks();
    void InitializeConnects();
```

## Style Management

### Default Style Preservation
```cpp
private:
    QString m_default_style;
```

## Thread Management

### Main Thread Access
```cpp
private:
    QThread* get_thread() override
    {
        return thread();
    }
```

## Typical Usage Flow

```cpp
// 1. Create application instance
gui_application app(argc, argv);

// 2. Configure application
app.SetShowGui(true);
app.SetStartGamesFullscreen(false);

// 3. Initialize
if (!app.Init())
{
    return -1;
}

// 4. Run event loop
return app.exec();
```

## Key Responsibilities

1. **Application Lifecycle**
   - Initialization
   - Event loop management
   - Shutdown handling

2. **Settings Management**
   - Load and save settings
   - Coordinate between different settings types
   - Apply settings changes

3. **UI Coordination**
   - Create and manage main window
   - Handle style changes
   - Manage translations

4. **Emulation Events**
   - Forward emulation state changes
   - Handle pause/resume
   - Track playtime

5. **Platform Integration**
   - Native event filtering
   - Device notifications
   - System integration

## Dependencies

### Qt Modules
- QtCore (QApplication, QTimer, etc.)
- QtMultimedia (QSoundEffect)
- QtWidgets (QApplication base)

### RPCS3 Modules
- Emulator System
- Raw Mouse Handler
- Main Window
- Settings System

## Notes
- Central application controller
- Bridges Qt framework with RPCS3 emulator
- Handles cross-platform abstractions
- Manages application-wide state
- Coordinates GUI and emulation threads
- Supports both GUI and CLI modes
