# main_window.h/cpp

## Overview
The main window class is the central GUI component of RPCS3, providing the primary user interface and coordinating all major application features.

## Class Hierarchy
```
QMainWindow (Qt)
    └── main_window
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/main_window.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/main_window.cpp`
- UI File: `/home/user/rpcs3/rpcs3/rpcs3qt/main_window.ui`

## Class Declaration
```cpp
class main_window : public QMainWindow
{
    Q_OBJECT
public:
    explicit main_window(std::shared_ptr<gui_settings> gui_settings,
                        std::shared_ptr<emu_settings> emu_settings,
                        std::shared_ptr<persistent_settings> persistent_settings,
                        QWidget *parent = nullptr);
    ~main_window();
    bool Init(bool with_cli_boot);
    // ...
};
```

## Key Features

### 1. Qt Features
- **Signals and Slots**: Implements Qt's signal/slot mechanism for GUI event handling
- **UI Form**: Uses `Ui::main_window` from main_window.ui
- **MOC**: Requires Q_OBJECT macro for Meta-Object Compiler

### 2. Dockable Widgets
The main window manages several dockable widget frames:
- `log_frame` - Log output display
- `debugger_frame` - Debugger interface
- `game_list_frame` - Game library display
- `kernel_explorer` - System kernel inspection
- `system_cmd_dialog` - System command interface

### 3. Settings Management
Maintains three types of settings:
- `gui_settings` - GUI-specific settings
- `emu_settings` - Emulation settings
- `persistent_settings` - Persistent application data

## Important Signals

```cpp
Q_SIGNALS:
    void RequestLanguageChange(const QString& language);
    void RequestGlobalStylesheetChange();
    void RequestDialogRepaint();
    void NotifyEmuSettingsChange();
    void NotifyWindowCloseEvent(bool closed);
    void NotifyShortcutHandlers();
```

## Public Slots

### Emulation Control
```cpp
void OnEmuStop();
void OnEmuRun(bool start_playtime);
void OnEmuResume() const;
void OnEmuPause() const;
void OnEmuReady() const;
```

### Disc Operations
```cpp
void OnEnableDiscEject(bool enabled) const;
void OnEnableDiscInsert(bool enabled) const;
```

### Debugger
```cpp
void OnAddBreakpoint(u32 addr) const;
```

### UI Updates
```cpp
void RepaintGui();
void RetranslateUI(const QStringList& language_codes, const QString& language_code);
```

## Private Slots

### Boot Operations
```cpp
void Boot(const std::string& path, const std::string& title_id = "",
         bool direct = false, bool refresh_list = false,
         cfg_mode config_mode = cfg_mode::custom,
         const std::string& config_path = "");
void BootElf();
void BootTest();
void BootGame();
void BootVSH();
void BootSavestate();
void BootRsxCapture(std::string path = "");
```

### Cache Management
```cpp
void RemoveHDD1Caches();
void RemoveAllCaches();
void RemoveSavestates();
void CleanUpGameList();
void RemoveFirmwareCache();
void CreateFirmwareCache();
```

### UI Management
```cpp
void SaveWindowState() const;
void SetIconSizeActions(int idx) const;
void ResizeIcons(int index);
```

## Drag & Drop Support

The main window supports drag and drop operations for:

### Drop Types
```cpp
enum class drop_type
{
    drop_error,
    drop_rap_edat_pkg,  // License/package files
    drop_pup,           // PlayStation Update Package
    drop_psf,           // PlayStation Save File
    drop_dir,           // Directory
    drop_game,          // Game executable
    drop_rrc            // RSX Replay Capture
};
```

### Event Handlers
```cpp
protected:
    void dropEvent(QDropEvent* event) override;
    void dragEnterEvent(QDragEnterEvent* event) override;
    void dragMoveEvent(QDragMoveEvent* event) override;
    void dragLeaveEvent(QDragLeaveEvent* event) override;
```

## Recent Games Management

Maintains two lists of recent items:
```cpp
struct recent_game_wrapper
{
    q_pair_list entries;
    QList<QAction*> actions;
};
recent_game_wrapper m_recent_game {};  // Recent games
recent_game_wrapper m_recent_save {};  // Recent savestates
```

## Key Private Methods

### Installation
```cpp
bool InstallPackages(QStringList file_paths = {}, bool from_boot = false);
void InstallPup(QString file_path = "");
bool HandlePackageInstallation(QStringList file_paths, bool from_boot);
void HandlePupInstallation(const QString& file_path, const QString& dir_path = "");
```

### Extraction
```cpp
void ExtractPup();
void ExtractTar();
void ExtractMSELF();
void DecryptSPRXLibraries();
```

### Configuration
```cpp
void ConfigureGuiFromSettings();
void RepaintToolBarIcons();
void RepaintThumbnailIcons();
void CreateActions();
void CreateConnects();
void CreateDockWindows();
void EnableMenus(bool enabled) const;
```

## Member Variables

### Icons
```cpp
QIcon m_app_icon;
QIcon m_icon_play;
QIcon m_icon_pause;
QIcon m_icon_restart;
QIcon m_icon_fullscreen_on;
QIcon m_icon_fullscreen_off;
```

### UI State
```cpp
bool m_is_list_mode = true;
bool m_save_slider_pos = false;
bool m_requested_show_logs_on_exit = false;
int m_other_slider_pos = 0;
```

### Action Groups
```cpp
QActionGroup* m_icon_size_act_group = nullptr;
QActionGroup* m_list_mode_act_group = nullptr;
QActionGroup* m_category_visible_act_group = nullptr;
```

## Dependencies

### Qt Modules
- QtCore (QMainWindow, QIcon, QUrl, etc.)
- QtWidgets (UI components)
- QtGui (Graphics and input handling)

### RPCS3 Modules
- Update Manager
- Settings System
- Shortcut Handler
- Game List Frame
- Debugger Frame
- Log Frame

## Usage Example

```cpp
// Initialize main window
auto gui_settings = std::make_shared<gui_settings>();
auto emu_settings = std::make_shared<emu_settings>();
auto persistent_settings = std::make_shared<persistent_settings>();

main_window window(gui_settings, emu_settings, persistent_settings);
if (window.Init(false))
{
    window.show();
}
```

## Notes
- The main window is the application's central hub
- Manages all dockable widget frames
- Handles file installation (PKG, PUP, etc.)
- Coordinates emulation start/stop
- Supports multiple boot methods
- Provides drag & drop functionality
- Manages recent games and savestates
