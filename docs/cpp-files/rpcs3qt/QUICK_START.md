# RPCS3 Qt Module Documentation - Quick Start Guide

## Documentation Location
`/home/user/rpcs3/docs/cpp-files/rpcs3qt/`

## Quick Navigation

### Start Here
1. **[README.md](README.md)** - Complete overview of all 247 files
2. **[DOCUMENTATION_SUMMARY.md](DOCUMENTATION_SUMMARY.md)** - Summary of what's been documented

### Core Documentation

#### Main Application Files
- [main_window.md](main-application/main_window.md) - Main GUI window
- [gui_application.md](main-application/gui_application.md) - Application controller  
- [gs_frame.md](main-application/gs_frame.md) - Game rendering window
- [gl_gs_frame.md](main-application/gl_gs_frame.md) - OpenGL implementation

#### Settings System
- [emu_settings.md](settings-config/emu_settings.md) - Emulation settings manager

#### Game Library
- [game_list_frame.md](game-list/game_list_frame.md) - Game list widget

#### Debugging
- [debugger_frame.md](debugger-tools/debugger_frame.md) - Debugger interface

## Module Overview

### Total Files: 247
- **C++ Headers:** ~128 files
- **C++ Sources:** ~119 files  
- **UI Files:** ~15 files
- **Total Lines:** ~150,000+ estimated

### File Categories (12)
1. Main Application (4 files)
2. Settings & Configuration (8 files)
3. Game List (9 files)
4. Debugger & Analysis (13 files)
5. Dialogs (40+ files)
6. Input Devices (10 files)
7. Toys to Life (4 files)
8. Media Handlers (7 files)
9. Custom Widgets (15 files)
10. Utilities (15 files)
11. Logging (3 files)
12. Shortcuts (4 files)

## Key Architectural Patterns

### Qt Integration
- **Signals/Slots:** Event-driven communication
- **MOC:** Meta-Object Compiler for Qt features
- **UI Forms:** Qt Designer .ui files
- **Stylesheets:** Custom theming support

### RPCS3 Patterns
- **Settings Hierarchy:** Global + per-game configs
- **Widget Enhancement:** Auto-connect UI to settings
- **Async Operations:** Background threading
- **Dockable Widgets:** Flexible UI layout

## Common Use Cases

### For Developers

#### Understanding a File
1. Check [README.md](README.md) for quick description
2. Find detailed doc if available (8 files)
3. Review signals/slots
4. Check dependencies

#### Adding New Features
1. Review similar existing files
2. Follow Qt conventions
3. Use enhance pattern for settings
4. Document signals/slots

#### Debugging Issues
1. Identify category in README
2. Check related files
3. Review signal connections
4. Test in isolation

### For Code Reviewers

#### Reviewing Changes
1. Verify Qt best practices
2. Check signal/slot connections
3. Review settings integration
4. Test UI responsiveness

## File Size References

### Largest Files
- **settings_dialog.cpp** - 115 KB
- **main_window.cpp** - 127 KB
- **game_list_frame.cpp** - 93 KB

### Largest UI Files
- **settings_dialog.ui** - 176 KB
- **pad_settings_dialog.ui** - 108 KB

### Largest Headers  
- **tooltips.h** - 53 KB
- **localized_emu.h** - 38 KB

## Qt Specific Features

### Signal/Slot Examples
```cpp
// Emitter
Q_SIGNALS:
    void RequestBoot(const game_info& game);

// Receiver
public Q_SLOTS:
    void Boot(const std::string& path);

// Connection
connect(game_list, &game_list_frame::RequestBoot,
        main_window, &main_window::Boot);
```

### Widget Enhancement
```cpp
// Auto-connect UI widget to setting
emu_settings->EnhanceComboBox(
    renderer_combo,
    emu_settings_type::Renderer
);
```

## Platform Notes

### Windows
- Raw mouse input
- USB device notifications
- Taskbar progress

### Linux  
- X11 integration
- DBus notifications

### macOS
- Menu bar integration
- Retina display support

## Build System

### CMake Integration
- Qt package detection
- MOC/UIC/RCC processing
- Platform-specific sources

## Next Steps

1. Read [README.md](README.md) for complete overview
2. Review detailed docs for core files
3. Explore category relevant to your work
4. Use code examples as templates

## Questions?

- Check DOCUMENTATION_SUMMARY.md for statistics
- Review architecture patterns in README
- Look at code examples in detailed docs
- Compare with similar existing files

---

**Created:** 2025-11-17  
**Total Documentation:** 10 files  
**Coverage:** 8 detailed + 247 summarized
