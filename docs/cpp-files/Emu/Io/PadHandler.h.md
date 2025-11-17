# PadHandler.h - Game Controller Input Handler

## Overview
This header provides the base class and infrastructure for handling game controller input devices in RPCS3. It supports standard PS3 controllers and specialized devices like motion controllers, light guns, and music game controllers.

## Key Classes

### PadDevice
Base class representing a physical input device connected to the emulator.

**Members:**
- `config`: Configuration pointer (cfg_pad)
- `player_id`: Player number (0-6 for up to 7 devices)
- `large_motor`: Rumble motor intensity (0-255)
- `small_motor`: Secondary vibration intensity (0-255)
- `new_output_data`: Flag indicating new output available
- `last_output`: Timestamp of last output update
- `trigger_code_left`/`trigger_code_right`: Trigger key mappings
- `axis_code_left`/`axis_code_right`: Analog stick mappings (4 per side)
- `color_override`/`color_override_active`: LED override settings
- `enable_player_leds`: Allow player number LED indication
- `update_player_leds`: Update LED on next cycle
- `ahrs`: Quaternion calculator for motion data
- `last_ahrs_update_time_us`: Last sensor update time

**Key Methods:**
- `update_orientation()`: Calculate orientation from IMU data
- `reset_orientation()`: Reset motion tracking

### pad_ensemble
Groups related pad data together for easier management.

**Members:**
- `pad`: Shared pointer to main Pad data
- `device`: Shared pointer to physical device
- `buddy_device`: Optional buddy device (for dual-control setups)

### pad_list_entry
Registry entry for available input devices.

**Members:**
- `name`: Human-readable device name
- `is_buddy_only`: Whether device can only be used as secondary

### pad_capabilities
Describes hardware capabilities of a device.

**Capabilities:**
- `has_led`: LED lighting support
- `has_mono_led`: Single-color LED
- `has_player_led`: Player number indication LEDs
- `has_battery_led`: Battery status LED
- `has_rumble`: Force feedback/vibration
- `has_accel`: Accelerometer sensor
- `has_gyro`: Gyroscope sensor
- `has_pressure_sensitivity`: Analog pressure on buttons

## PadHandlerBase

Abstract base class for input device handlers.

### Enumerations

#### connection
```cpp
enum class connection {
    no_data,      // No data available
    connected,    // Device is connected
    disconnected  // Device was disconnected
};
```

#### trigger_recognition_mode
```cpp
enum class trigger_recognition_mode {
    any,             // All trigger modes supported
    one_directional, // Trigger treated as press (0-100%)
    two_directional  // Trigger as axis like stick
};
```

### Button Enums

Standard PS3 controller buttons:
- **D-Pad**: up, down, left, right
- **Face Buttons**: cross, square, circle, triangle
- **Shoulder Buttons**: L1, L2, L3, R1, R2, R3
- **Center Buttons**: select, start, ps
- **Analog Sticks**:
  - Left: ls_left, ls_right, ls_down, ls_up
  - Right: rs_left, rs_right, rs_down, rs_up

### Callback Types

#### pad_callback
```cpp
using pad_callback = std::function<void(
    u16 button_value,           // Button state
    std::string button_name,    // Button name
    std::string pad_name,       // Device name
    u32 battery_level,          // Battery percentage
    pad_preview_values,         // 6-value preview array
    pad_capabilities            // Device capabilities
)>;
```

#### pad_fail_callback
```cpp
using pad_fail_callback = std::function<void(std::string pad_name)>;
```

Triggered when device disconnects or fails.

#### motion_callback
```cpp
using motion_callback = std::function<void(
    std::string pad_name,              // Device name
    motion_preview_values preview      // 4-value motion preview
)>;
```

#### motion_fail_callback
```cpp
using motion_fail_callback = std::function<void(
    std::string pad_name,
    motion_preview_values preview
)>;
```

## Input Processing

### Motion/IMU Support

The handler supports motion controllers with accelerometer and gyroscope data:

**AHRS (Attitude and Heading Reference System):**
- Uses FusionAhrs library for quaternion calculation
- Converts raw accelerometer/gyro data to orientation
- Tracks update timestamps in microseconds
- Supports full 6-DOF (6 degrees of freedom) motion

**Motion Preview:**
- 4-element array for motion preview display
- Typically: accel_x, accel_y, gyro_z, other_data

### Rumble Support

- `large_motor`: Main rumble/haptic feedback
- `small_motor`: Secondary vibration pattern
- Different patterns for different actions

### LED Control

- **Player LEDs**: Indicate player number (1-7)
- **Color Override**: Custom LED color (RGB)
- **Battery LED**: Show charging/low battery
- **Mono LED**: Simple on/off indicator

## Trigger Mapping

Controllers can map trigger axes in different ways:

1. **One-directional**: L2/R2 as press buttons (0 or full)
2. **Two-directional**: L2/R2 as analog axes like sticks

## Configuration System

Device configuration includes:
- Button remapping
- Sensitivity settings for analog sticks
- Trigger behavior (one-way vs two-way)
- Motion sensitivity
- LED preferences
- Battery monitoring

## Device Types

### Standard Controllers
- PS3 Sixaxis/DualShock 3
- Dualshock 4
- Generic HID gamepads

### Specialized Devices
- Motion controllers (PS Move)
- Light guns (GunCon3, Top Shot Elite)
- Music game controllers (RB3 drums/guitar/keyboard)
- Arena/Sports controllers (Skateboard, DJ turntable)
- Unique devices (Skylanders Portal, Disney Infinity)

## Pressure Sensitivity

Some advanced controllers support pressure-sensitive buttons:
- Can measure button press force
- Useful for racing games (acceleration)
- Fighting games (punch/kick strength)

## Player Identification

- **Player ID 0-6**: 7 supported players maximum
- Maps to PS3 system player slots
- LED indication of player number
- Important for multiplayer games

## Buddy Device Support

Some input methods use dual devices:
- Primary device: Main control
- Buddy device: Secondary input
- Example: Two Move controllers for games like Sports Champions

## Battery Management

Wireless devices track battery:
- Battery percentage (0-100)
- Low battery warnings
- Charging state indicators
- Display in UI callbacks

## Integration Notes

- Inherits from LOG_CHANNEL for logging
- Uses std::shared_ptr for device lifecycle management
- Thread-safe callbacks for UI updates
- Supports hot-plug/hot-unplug
- Compatible with event-driven architecture

## Key Design Patterns

1. **Strategy Pattern**: Different handlers for different device types
2. **Observer Pattern**: Callbacks for state changes
3. **Factory Pattern**: Device discovery and creation
4. **RAII**: Shared pointers manage device lifetime
5. **Virtual Methods**: Polymorphic device behavior

## Common Usage

### Adding a New Device
1. Create handler subclass inheriting from PadHandlerBase
2. Implement device enumeration
3. Implement state reading
4. Set up event callbacks
5. Register with input system

### Handling Input
1. Enumerate connected devices
2. Read button/axis states
3. Convert to PS3 format
4. Trigger callbacks
5. Apply feedback (rumble, LED)

## Performance Characteristics

- **Input Polling**: 60Hz standard (synced with emulation)
- **Latency**: Minimized through efficient polling
- **CPU Impact**: <1% for typical controller handling
- **Memory**: Minimal overhead per device

## Platform Support

- **Windows**: Direct Input, XInput, DualShock 4 native
- **Linux**: evdev, DualShock 4 native, generic HID
- **macOS**: IOKit, DualShock 4 native

## Future Enhancements

1. Support for more specialized devices
2. Pressure sensitivity in more games
3. Improved motion detection accuracy
4. Wireless latency optimization
5. Voice/mic input support

## Dependencies

- `pad_types.h`: Button/axis type definitions
- `pad_config.h`: Configuration system
- `Fusion/FusionAhrs.h`: Motion calculations
- `util/types.hpp`: Type utilities

## Notes

- Callbacks must be non-blocking
- Device enumeration happens at startup
- Hot-plug detection platform-dependent
- Motion sensor filtering essential for accuracy
- Rumble patterns configurable per game
