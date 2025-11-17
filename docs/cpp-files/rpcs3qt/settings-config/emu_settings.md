# emu_settings.h/cpp

## Overview
Manages emulation-specific settings that control PS3 emulation behavior. This class handles loading, saving, and validating settings from config.yml files.

## Class Hierarchy
```
QObject (Qt)
    └── emu_settings
```

## Location
- Header: `/home/user/rpcs3/rpcs3/rpcs3qt/emu_settings.h`
- Source: `/home/user/rpcs3/rpcs3/rpcs3qt/emu_settings.cpp`
- Type Definitions: `/home/user/rpcs3/rpcs3/rpcs3qt/emu_settings_type.h`

## Class Declaration
```cpp
class emu_settings : public QObject
{
    Q_OBJECT
public:
    emu_settings();
    bool Init();
    void LoadSettings(const std::string& title_id = "",
                     bool create_config_from_global = true);
    void SaveSettings() const;
    // ...
};
```

## Key Features

### 1. Settings Types
Uses `emu_settings_type` enum for type-safe setting access. Categories include:
- CPU settings (PPU/SPU)
- GPU settings (renderer, resolution)
- Audio settings
- Input/Output settings
- System settings
- Network settings
- Debug settings

### 2. Widget Enhancement
Automatically connects Qt widgets to settings:

```cpp
// Combo boxes
void EnhanceComboBox(QComboBox* combobox, emu_settings_type type,
                    bool is_ranged = false, bool use_max = false,
                    int max = 0, bool sorted = false, bool strict = true);

// Check boxes
void EnhanceCheckBox(QCheckBox* checkbox, emu_settings_type type);

// Spin boxes
void EnhanceSpinBox(QSpinBox* spinbox, emu_settings_type type,
                   const QString& prefix = "", const QString& suffix = "");
void EnhanceDoubleSpinBox(QDoubleSpinBox* spinbox, emu_settings_type type,
                         const QString& prefix = "", const QString& suffix = "");

// Sliders
void EnhanceSlider(QSlider* slider, emu_settings_type type);

// Line edits
void EnhanceLineEdit(QLineEdit* edit, emu_settings_type type);

// Button groups
void EnhanceRadioButton(QButtonGroup* button_group, emu_settings_type type);

// Date/time
void EnhanceDateTimeEdit(QDateTimeEdit* date_time_edit, emu_settings_type type,
                        const QString& format, bool use_calendar,
                        bool as_offset_from_now, int offset_update_time=0);
```

## YAML Configuration

### Settings Storage
```cpp
private:
    YAML::Node m_default_settings; // Default settings
    YAML::Node m_current_settings; // Current settings
    std::string m_title_id;        // Per-game config
```

Settings hierarchy:
1. **Global config**: `config.yml`
2. **Per-game config**: `config/[TITLE_ID]/config.yml`

## Settings Management

### Get/Set Methods
```cpp
// Get setting value
std::string GetSetting(emu_settings_type type) const;

// Set setting value
void SetSetting(emu_settings_type type, const std::string& val) const;

// Get default value
std::string GetSettingDefault(emu_settings_type type) const;

// Get available options
static std::vector<std::string> GetSettingOptions(emu_settings_type type);
static QStringList GetQStringSettingOptions(emu_settings_type type);
```

### Localization
```cpp
QString GetLocalizedSetting(const QString& original,
                           emu_settings_type type,
                           int index, bool strict) const;
```

Converts internal config values to localized display strings.

## Library Management

### HLE Module Control
```cpp
std::vector<std::string> GetLibrariesControl();
void SaveSelectedLibraries(const std::vector<std::string>& libs);
```

Controls which PS3 libraries to:
- Load (LLE - Low Level Emulation)
- Auto-load
- Manual-load

## Hardware Creators

### Device Enumeration
```cpp
render_creator* m_render_creator = nullptr;
microphone_creator m_microphone_creator;
midi_creator m_midi_creator;
```

Enumerates available:
- Rendering backends (Vulkan, OpenGL, Null)
- Microphone devices
- MIDI devices

## Validation

### Settings Validation
```cpp
bool ValidateSettings(bool cleanup);
void OpenCorrectionDialog(QWidget* parent = Q_NULLPTR);
```

**Broken Settings Tracking:**
```cpp
std::set<emu_settings_type> m_broken_types;
```

Detects and fixes:
- Invalid values
- Deprecated settings
- Incompatible combinations

## Type Finding

### Node Mapping
```cpp
emu_settings_type FindSettingsType(const cfg::_base* node) const;
```

Maps YAML nodes back to setting types.

## Restore Defaults

### Reset Settings
```cpp
void RestoreDefaults();

Q_SIGNALS:
    void RestoreDefaultsSignal();
```

Resets all settings to defaults and updates connected widgets.

## Usage Example

```cpp
// Create settings manager
emu_settings settings;
settings.Init();

// Load settings (global or per-game)
settings.LoadSettings("BLUS12345");

// Create UI widget and connect to setting
QComboBox* renderer_combo = new QComboBox();
settings.EnhanceComboBox(renderer_combo,
                        emu_settings_type::Renderer);

// Get/set values programmatically
std::string renderer = settings.GetSetting(emu_settings_type::Renderer);
settings.SetSetting(emu_settings_type::Renderer, "Vulkan");

// Save changes
settings.SaveSettings();

// Validate configuration
if (!settings.ValidateSettings(false))
{
    settings.OpenCorrectionDialog(parent_widget);
}
```

## Settings Categories

### CPU Settings
- PPU Decoder (Interpreter, Recompiler, LLVM)
- SPU Decoder
- Thread Scheduler
- Debug options

### GPU Settings
- Renderer (Vulkan, OpenGL, Null)
- Resolution Scale
- Aspect Ratio
- Frame Limit
- VSync
- Shader options

### Audio Settings
- Audio Backend
- Output Device
- Buffering
- Volume

### I/O Settings
- Keyboard Handler
- Mouse Handler
- Camera
- Microphone
- Pad Handler

### System Settings
- Language
- Console Time
- Firmware
- Enter Button Assignment

### Network Settings
- Network Status
- IP/DNS Settings
- PSN Status

## Dependencies

### Qt Modules
- QtCore (QObject, QVariant)
- QtWidgets (QComboBox, QCheckBox, etc.)

### RPCS3 Modules
- YAML library
- Configuration system
- Hardware creators

## Notes
- Central configuration management for emulation
- Supports per-game configuration overrides
- Type-safe setting access via enums
- Automatic widget synchronization
- Settings validation and correction
- Localization support for display values
