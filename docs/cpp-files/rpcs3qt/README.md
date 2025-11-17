# RPCS3 Qt GUI Module Documentation

## Overview
The `rpcs3qt` module is the graphical user interface (GUI) for RPCS3, built using the Qt framework. It consists of approximately 247 C++ source and header files organized into functional categories.

**Module Location:** `/home/user/rpcs3/rpcs3/rpcs3qt/`

## Architecture

### Qt Framework Integration
- **Base Framework:** Qt 5/6
- **Key Modules:** QtCore, QtWidgets, QtGui, QtMultimedia, QtNetwork
- **UI Forms:** Uses `.ui` files compiled by Qt UIC
- **MOC:** Requires Meta-Object Compiler for signals/slots
- **Stylesheets:** Custom Qt stylesheets for theming

### Design Patterns
- **Signal/Slot**: Event-driven communication
- **MVC**: Model-View-Controller separation
- **Dockable Widgets**: Flexible UI layout
- **Settings Management**: Persistent configuration

---

## File Categories

## 1. Main Application (4 files)

Core application files that manage the entire GUI lifecycle.

### Core Files

#### main_window.h/cpp
**Location:** [main-application/main_window.md](main-application/main_window.md)
- **Purpose:** Main application window
- **Inherits:** QMainWindow
- **Key Features:**
  - Central UI hub
  - Menu and toolbar management
  - Dockable widget coordination
  - Drag & drop support
  - Boot operations
  - Package installation
- **Signals:** RequestLanguageChange, NotifyEmuSettingsChange
- **Slots:** OnEmuRun, OnEmuStop, OnEmuPause, Boot methods

#### gui_application.h/cpp
**Location:** [main-application/gui_application.md](main-application/gui_application.md)
- **Purpose:** Application controller
- **Inherits:** QApplication, main_application
- **Key Features:**
  - Application lifecycle management
  - Settings coordination
  - Translation system
  - Native event filtering
  - Playtime tracking
  - Cross-platform integration
- **Signals:** OnEmulatorRun, OnEmulatorStop
- **Platform:** Windows device notifications

#### gs_frame.h/cpp
**Location:** [main-application/gs_frame.md](main-application/gs_frame.md)
- **Purpose:** Game screen window
- **Inherits:** QWindow, GSFrameBase
- **Key Features:**
  - Rendering window management
  - Fullscreen transitions
  - Mouse lock/hide control
  - Taskbar progress display
  - Video recording support
  - Screenshot capture
  - Shortcut handling
- **Context:** Abstract base for OpenGL/Vulkan

#### gl_gs_frame.h/cpp
**Location:** [main-application/gl_gs_frame.md](main-application/gl_gs_frame.md)
- **Purpose:** OpenGL rendering window
- **Inherits:** gs_frame
- **Key Features:**
  - OpenGL context management
  - QOpenGLContext integration
  - Surface format configuration
  - Buffer swapping

---

## 2. Settings & Configuration (8 files)

Manages application and emulation settings.

### Core Settings

#### emu_settings.h/cpp
**Location:** [settings-config/emu_settings.md](settings-config/emu_settings.md)
- **Purpose:** Emulation settings manager
- **Type:** YAML-based configuration
- **Key Features:**
  - Per-game configurations
  - Widget enhancement (auto-connect)
  - Settings validation
  - Library (HLE) management
  - Hardware device enumeration
  - Localization support
- **File:** config.yml
- **Categories:** CPU, GPU, Audio, I/O, System, Network, Debug

#### gui_settings.h/cpp
- **Purpose:** GUI-specific settings
- **Inherits:** settings (QSettings wrapper)
- **Key Features:**
  - Window geometry
  - Column visibility/width
  - Icon sizes
  - Color schemes
  - Recent files
  - UI preferences
- **Storage:** Platform-specific (registry/config files)

#### settings.h/cpp
- **Purpose:** Base settings class
- **Type:** QSettings wrapper
- **Features:** Simplified QSettings interface

#### settings_dialog.h/cpp
- **Purpose:** Settings dialog window
- **UI File:** settings_dialog.ui (176KB - large dialog)
- **Tabs:**
  - CPU
  - GPU
  - Audio
  - I/O
  - System
  - Network
  - Advanced
  - Debug
  - Emulator

#### persistent_settings.h/cpp
- **Purpose:** Application-wide persistent data
- **Features:**
  - Last used paths
  - Window states
  - User preferences

#### config_adapter.h/cpp
- **Purpose:** Configuration adaptation layer
- **Features:** Bridge between UI and config system

#### config_checker.h/cpp
- **Purpose:** Configuration validation
- **Features:** Check for invalid/incompatible settings

#### emu_settings_type.h
- **Purpose:** Setting type enumerations
- **Size:** ~21KB of type definitions
- **Usage:** Type-safe setting access

---

## 3. Game List (9 files)

Game library display and management.

#### game_list_frame.h/cpp
- **Purpose:** Main game list widget
- **Inherits:** custom_dock_widget
- **Features:**
  - Game library scanning
  - List/Grid view modes
  - Search/filter functionality
  - Category filtering
  - Context menu operations
  - Icon loading/caching
  - Compatibility display
  - Batch operations (cache creation, deletion)
- **Signals:** RequestBoot, NotifyGameSelection

#### game_list_table.h/cpp
- **Purpose:** Table view for games
- **Inherits:** game_list_base
- **Columns:** Icon, Name, Serial, Firmware, Version, Category, etc.

#### game_list_grid.h/cpp
- **Purpose:** Grid view for games
- **Inherits:** game_list_base
- **Features:** Thumbnail display, hover effects

#### game_list_grid_item.h/cpp
- **Purpose:** Individual grid item
- **Features:** Game icon, title, compatibility badge

#### game_list.h/cpp
- **Purpose:** Game info container
- **Data:** Game metadata, paths, icons

#### game_list_base.h/cpp
- **Purpose:** Base class for list/grid
- **Features:** Common functionality

#### game_list_delegate.h/cpp
- **Purpose:** Custom item rendering
- **Features:** Progress bars, icons

#### game_compatibility.h/cpp
- **Purpose:** Compatibility database
- **Features:** Fetch/cache compatibility info
- **Source:** RPCS3 compatibility database

#### gui_game_info.h/cpp
- **Purpose:** Game information structure
- **Data:** Title, serial, version, etc.

---

## 4. Debugger & Analysis Tools (13 files)

Debugging and system analysis tools.

#### debugger_frame.h/cpp
- **Purpose:** Main debugger window
- **Features:**
  - Assembly view
  - Register display
  - Breakpoint management
  - Step execution
  - Call stack
  - Thread list

#### rsx_debugger.h/cpp
- **Purpose:** RSX (Graphics) debugger
- **Features:**
  - Command buffer inspection
  - Texture viewer
  - Shader analysis
  - Performance counters

#### memory_viewer_panel.h/cpp
- **Purpose:** Memory inspection
- **Features:**
  - Hex/ASCII view
  - Memory editing
  - Search functionality
  - Address navigation

#### memory_string_searcher.cpp
- **Purpose:** Memory string search
- **Features:** Text pattern search in memory

#### kernel_explorer.h/cpp
- **Purpose:** PS3 kernel inspection
- **Features:**
  - Thread viewer
  - Mutex/Semaphore list
  - Event queue monitoring
  - Memory pools

#### instruction_editor_dialog.h/cpp
- **Purpose:** Assembly instruction editing
- **Features:** Edit instructions at runtime

#### register_editor_dialog.h/cpp
- **Purpose:** Register editing
- **Features:** Modify CPU registers

#### breakpoint_handler.h/cpp
- **Purpose:** Breakpoint management
- **Features:** Add/remove/manage breakpoints

#### breakpoint_list.h/cpp
- **Purpose:** Breakpoint display
- **Features:** List active breakpoints

#### call_stack_list.h/cpp
- **Purpose:** Call stack display
- **Features:** Stack trace visualization

#### debugger_list.h/cpp
- **Purpose:** Debugger list widget
- **Features:** Thread/module listing

#### debugger_add_bp_window.h/cpp
- **Purpose:** Add breakpoint dialog

#### cg_disasm_window.h/cpp
- **Purpose:** Cg shader disassembly
- **Features:** Graphics shader inspection

---

## 5. Dialogs (40+ files)

Various dialog windows for different purposes.

### Save Data Management

#### save_manager_dialog.h/cpp
- **Purpose:** Save data browser
- **Features:** Import/export/delete saves

#### save_data_dialog.h/cpp
- **Purpose:** Save data selection (cellSaveData callback)

#### save_data_info_dialog.h/cpp
- **Purpose:** Save data details

#### save_data_list_dialog.h/cpp
- **Purpose:** Save data list view

#### savestate_manager_dialog.h/cpp
- **Purpose:** Savestate management
- **Features:** Load/save/delete savestates

### Trophy Management

#### trophy_manager_dialog.h/cpp
- **Purpose:** Trophy viewer
- **Features:**
  - Trophy list
  - Progress tracking
  - Unlock times
  - Trophy sync

#### trophy_notification_frame.h/cpp
- **Purpose:** Trophy unlock notification
- **Features:** Popup notification

#### trophy_notification_helper.h/cpp
- **Purpose:** Trophy notification coordination

### User Management

#### user_manager_dialog.h/cpp
- **Purpose:** PSN user account management
- **Features:** Create/delete users, set avatars

#### user_account.h/cpp
- **Purpose:** User account data structure

### Screenshot Management

#### screenshot_manager_dialog.h/cpp
- **Purpose:** Screenshot browser

#### screenshot_preview.h/cpp
- **Purpose:** Screenshot preview widget

#### screenshot_item.h/cpp
- **Purpose:** Screenshot item data

### Package Installation

#### pkg_install_dialog.h/cpp
- **Purpose:** PKG package installer
- **Features:** Progress tracking, multi-file install

### System Dialogs

#### vfs_dialog.h/cpp
- **Purpose:** Virtual File System configuration
- **Features:** Map emulated paths to host paths

#### vfs_dialog_tab.h/cpp
- **Purpose:** VFS tab container

#### vfs_dialog_path_widget.h/cpp
- **Purpose:** Path mapping widget

#### vfs_dialog_usb_tab.h/cpp
- **Purpose:** USB device configuration

#### vfs_dialog_usb_input.h/cpp
- **Purpose:** USB device input

#### vfs_tool_dialog.h/cpp
- **Purpose:** VFS utility operations
- **UI File:** vfs_tool_dialog.ui

#### system_cmd_dialog.h/cpp
- **Purpose:** System command console
- **Features:** Execute system commands

### Patch & Cheat

#### patch_manager_dialog.h/cpp
- **Purpose:** Game patch management
- **Features:**
  - Enable/disable patches
  - Import patch files
  - Edit patches
- **UI File:** patch_manager_dialog.ui

#### patch_creator_dialog.h/cpp
- **Purpose:** Create custom patches
- **UI File:** patch_creator_dialog.ui

#### cheat_manager.h/cpp
- **Purpose:** Cheat code management
- **Features:** Memory cheats, search

### Network Dialogs

#### rpcn_settings_dialog.h/cpp
- **Purpose:** RPCN (PSN replacement) settings
- **Features:** Account management, server selection

### Message Dialogs (cellOsk, cellMsg)

#### msg_dialog_frame.h/cpp
- **Purpose:** System message dialog (cellMsgDialog)
- **Features:** PS3 message dialog emulation

#### osk_dialog_frame.h/cpp
- **Purpose:** On-screen keyboard (cellOskDialog)
- **Features:** Text input emulation

#### recvmessage_dialog_frame.h/cpp
- **Purpose:** Receive message dialog

#### sendmessage_dialog_frame.h/cpp
- **Purpose:** Send message dialog

### Utility Dialogs

#### welcome_dialog.h/cpp
- **Purpose:** First-run welcome screen
- **UI File:** welcome_dialog.ui

#### about_dialog.h/cpp
- **Purpose:** About RPCS3 dialog
- **UI File:** about_dialog.ui (17KB)

#### fatal_error_dialog.h/cpp
- **Purpose:** Fatal error display

#### input_dialog.h/cpp
- **Purpose:** Generic input dialog

#### find_dialog.h/cpp
- **Purpose:** Find/search dialog

#### custom_dialog.h/cpp
- **Purpose:** Custom dialog base class

#### progress_dialog.h/cpp
- **Purpose:** Progress indicator dialog

#### dimensions_dialog.h/cpp
- **Purpose:** Disney Infinity portal emulation
- **Features:** Figure management

#### music_player_dialog.h/cpp
- **Purpose:** Music player (experimental)
- **UI File:** music_player_dialog.ui

#### elf_memory_dumping_dialog.h/cpp
- **Purpose:** Dump ELF from memory

---

## 6. Input Devices (10 files)

Controller and input device configuration.

#### pad_settings_dialog.h/cpp
- **Purpose:** Controller configuration
- **UI File:** pad_settings_dialog.ui (108KB - very large)
- **Features:**
  - Button mapping
  - Analog stick configuration
  - Vibration settings
  - Multiple handler support
  - Profile management

#### pad_led_settings_dialog.h/cpp
- **Purpose:** Controller LED configuration
- **UI File:** pad_led_settings_dialog.ui
- **Features:** DualShock 4 LED color

#### pad_motion_settings_dialog.h/cpp
- **Purpose:** Motion control settings
- **UI File:** pad_motion_settings_dialog.ui
- **Features:** Sixaxis configuration

#### pad_device_info.h
- **Purpose:** Device information structure

#### emulated_pad_settings_dialog.h/cpp
- **Purpose:** Emulated DualShock 3 advanced settings

#### emulated_logitech_g27_settings_dialog.h/cpp
- **Purpose:** Logitech G27 racing wheel configuration

#### basic_mouse_settings_dialog.h/cpp
- **Purpose:** Basic mouse handler settings

#### raw_mouse_settings_dialog.h/cpp (Windows only)
- **Purpose:** Raw input mouse configuration

#### ps_move_tracker_dialog.h/cpp
- **Purpose:** PlayStation Move controller tracking
- **UI File:** ps_move_tracker_dialog.ui

#### camera_settings_dialog.h/cpp
- **Purpose:** PlayStation Eye camera settings
- **UI File:** camera_settings_dialog.ui

---

## 7. Toys to Life (4 files)

Emulation for toys-to-life game accessories.

#### skylander_dialog.h/cpp
- **Purpose:** Skylanders Portal emulation
- **Features:** Figure management, portal simulation

#### infinity_dialog.h/cpp
- **Purpose:** Disney Infinity Base emulation
- **Features:** Figure management

#### dimensions_dialog.h/cpp
- **Purpose:** LEGO Dimensions Toy Pad emulation

#### kamen_rider_dialog.h/cpp
- **Purpose:** Kamen Rider toys emulation

---

## 8. Media Handlers (7 files)

Audio/video/camera device handlers using Qt.

#### qt_camera_handler.h/cpp
- **Purpose:** Camera device handler
- **Features:** Qt Multimedia camera integration

#### qt_camera_video_sink.h/cpp
- **Purpose:** Camera video sink
- **Features:** Frame capture for cellCamera

#### qt_music_handler.h/cpp
- **Purpose:** Music playback handler
- **Features:** Background music for cellMusic

#### qt_video_source.h/cpp
- **Purpose:** Video source abstraction

#### microphone_creator.h/cpp
- **Purpose:** Microphone device enumeration
- **Features:** List available microphones

#### midi_creator.h/cpp
- **Purpose:** MIDI device enumeration
- **Features:** List MIDI devices for music games

#### render_creator.h/cpp
- **Purpose:** Renderer backend enumeration
- **Features:** List Vulkan/OpenGL/Null renderers

---

## 9. Custom Widgets (15 files)

Reusable Qt widgets for the application.

#### custom_dock_widget.h
- **Purpose:** Enhanced QDockWidget
- **Features:** Custom title bars, styling

#### custom_table_widget_item.h/cpp
- **Purpose:** Custom QTableWidgetItem
- **Features:** Custom sorting, display

#### custom_tree_widget.h
- **Purpose:** Enhanced QTreeWidget

#### flow_layout.h/cpp
- **Purpose:** Flow layout manager
- **Features:** Responsive grid layout (like CSS flexbox)

#### flow_widget.h/cpp
- **Purpose:** Flow layout container

#### flow_widget_item.h/cpp
- **Purpose:** Flow layout item

#### table_item_delegate.h/cpp
- **Purpose:** Table item custom rendering

#### richtext_item_delegate.h
- **Purpose:** Rich text rendering in items

#### progress_indicator.h/cpp
- **Purpose:** Taskbar progress integration
- **Platform:** Windows, Linux, macOS

#### video_label.h/cpp
- **Purpose:** Video playback label

#### movie_item.h/cpp
- **Purpose:** Movie/GIF item wrapper

#### movie_item_base.h/cpp
- **Purpose:** Base class for movie items

#### numbered_widget_item.h
- **Purpose:** Item with numeric sorting

#### hex_validator.h
- **Purpose:** Hexadecimal input validator

---

## 10. Utilities (15 files)

Helper classes and utilities.

#### qt_utils.h/cpp
- **Purpose:** Qt utility functions
- **Features:**
  - Color utilities
  - String conversions
  - Widget helpers
  - Image processing

#### localized.h/cpp
- **Purpose:** Localized string helpers

#### localized_emu.h/cpp
- **Purpose:** Emulation-specific localization
- **Large file:** 38KB of translations

#### tooltips.h/cpp
- **Purpose:** Tooltip text database
- **Large file:** 53KB of tooltip strings

#### stylesheets.h
- **Purpose:** Qt stylesheet definitions
- **Features:** Dark theme, custom styles

#### uuid.h/cpp
- **Purpose:** UUID generation/parsing

#### downloader.h/cpp
- **Purpose:** File downloader
- **Features:** HTTP downloads, progress tracking

#### curl_handle.h/cpp
- **Purpose:** libcurl wrapper

#### update_manager.h/cpp
- **Purpose:** Auto-update system
- **Features:** Check for updates, download, install

#### category.h
- **Purpose:** Game category definitions

#### _discord_utils.h/cpp
- **Purpose:** Discord Rich Presence integration
- **Optional:** Compiled with -DWITH_DISCORD_RPC

#### syntax_highlighter.h/cpp
- **Purpose:** Syntax highlighting for code/logs

---

## 11. Logging (3 files)

Log viewing and management.

#### log_frame.h/cpp
- **Purpose:** Main log window
- **Features:**
  - Log level filtering
  - Search
  - Export
  - Color coding

#### log_viewer.h/cpp
- **Purpose:** Log viewer widget
- **Features:** Text viewing, filtering

---

## 12. Shortcuts (4 files)

Keyboard shortcut management.

#### shortcut_handler.h/cpp
- **Purpose:** Shortcut event handler
- **Features:** Global shortcut processing

#### shortcut_settings.h/cpp
- **Purpose:** Shortcut configuration storage

#### shortcut_dialog.h/cpp
- **Purpose:** Shortcut configuration UI
- **UI File:** shortcut_dialog.ui

#### shortcut_utils.h/cpp
- **Purpose:** Shortcut utility functions

---

## Qt-Specific Features

### Signals and Slots

Most widgets use Qt's signal/slot mechanism for communication:

```cpp
// Typical signal definitions
Q_SIGNALS:
    void RequestBoot(const game_info& game);
    void NotifyGameSelection(const game_info& game);
    void GameListFrameClosed();

// Typical slot definitions
public Q_SLOTS:
    void Refresh(bool from_drive = false);
    void SetListMode(bool is_list);

private Q_SLOTS:
    void OnColClicked(int col);
    void ShowContextMenu(const QPoint& pos);
```

### UI Files

Many dialogs use Qt Designer `.ui` files:
- **settings_dialog.ui** - 176KB (extensive settings)
- **pad_settings_dialog.ui** - 108KB (complex input mapping)
- **main_window.ui** - 40KB (main menu/toolbar)
- **patch_manager_dialog.ui** - 12KB
- And many others

### MOC (Meta-Object Compiler)

All classes with `Q_OBJECT` macro require MOC processing:
- Enables signals/slots
- Provides runtime type information
- Enables property system

---

## Build Integration

### CMake Configuration

Location: `/home/user/rpcs3/rpcs3/rpcs3qt/CMakeLists.txt`

Key aspects:
- Qt5/Qt6 package finding
- MOC/UIC/RCC invocation
- Resource compilation
- Platform-specific sources

---

## File Statistics

- **Total Files:** ~247 (.h and .cpp)
- **Header Files:** ~128
- **Source Files:** ~119
- **UI Files:** ~15
- **Largest Source:** settings_dialog.cpp, main_window.cpp (100KB+)
- **Largest Header:** gui_settings.h, localized_emu.h, tooltips.h

---

## Key Design Patterns

### 1. Enhance Pattern (emu_settings)
```cpp
// Automatically connect widgets to settings
emu_settings->EnhanceComboBox(combo, emu_settings_type::Renderer);
```

### 2. Signal/Slot Communication
```cpp
// Decoupled event handling
connect(game_list, &game_list_frame::RequestBoot,
        main_window, &main_window::Boot);
```

### 3. Custom Dock Widgets
```cpp
// Flexible, dockable UI components
class game_list_frame : public custom_dock_widget
```

### 4. Settings Hierarchy
```cpp
// Global vs per-game configuration
settings->LoadSettings("BLUS12345"); // Per-game
settings->LoadSettings();             // Global
```

---

## Common Qt Classes Used

### Widgets
- QMainWindow, QDialog, QWidget
- QTableWidget, QTreeWidget, QListWidget
- QComboBox, QCheckBox, QSpinBox
- QLabel, QPushButton, QLineEdit

### Layouts
- QVBoxLayout, QHBoxLayout, QGridLayout
- Custom flow_layout

### Graphics
- QIcon, QPixmap, QImage
- QPainter (for custom rendering)

### Utilities
- QSettings (settings storage)
- QTimer (periodic tasks)
- QString, QByteArray
- QFuture, QFutureWatcher (async operations)

---

## Platform-Specific Code

### Windows
- Raw input mouse handler
- Device notification (USB)
- Taskbar progress (COM)

### Linux
- X11 integration
- DBus notifications

### macOS
- NSOpenGL integration
- macOS menu integration

---

## Internationalization (i18n)

### Translation System
- Qt's translation framework (`QTranslator`)
- .ts/.qm files for translations
- Runtime language switching

### Localized Strings
- `localized.h/cpp` - General translations
- `localized_emu.h/cpp` - Emulation-specific
- `tooltips.h` - Tooltip translations

---

## Performance Considerations

### Asynchronous Operations
- Game list refresh (QFutureWatcher)
- Icon loading (threaded)
- Compatibility download (background)

### Caching
- Icon caching
- Game info caching
- Compatibility data caching

### Lazy Loading
- Load game icons on demand
- Defer heavy initialization

---

## Testing Entry Points

### Key Dialogs
```cpp
// Test settings dialog
settings_dialog dlg(gui_settings, emu_settings, 0, parent);
dlg.exec();

// Test pad configuration
pad_settings_dialog dlg(parent, gui_settings, emu_settings);
dlg.exec();
```

---

## Future Development

### Potential Improvements
1. Qt 6 migration
2. Improved async/await patterns
3. Better separation of concerns
4. More unit tests
5. Accessibility improvements

---

## See Also

- [Main Application Documentation](main-application/)
- [Settings & Configuration Documentation](settings-config/)
- [Debugger Tools Documentation](debugger-tools/)
- [Game List Documentation](game-list/)
- [Custom Widgets Documentation](custom-widgets/)

---

## Contributing

When adding new files to rpcs3qt:
1. Follow Qt naming conventions
2. Use Q_OBJECT macro for signals/slots
3. Add .ui file if needed
4. Update CMakeLists.txt
5. Document signals and slots
6. Add to appropriate category

---

**Last Updated:** 2025-11-17
**Total Lines of Code:** ~150,000+ (estimated)
**Primary Language:** C++ with Qt
