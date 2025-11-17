# pad_types.h - Pad Button Types and Controller Definitions

## Overview
Defines controller button enumerations, button/axis utilities, PS3 controller types, and port status information. Core type definitions for the input system.

## Button Enumeration

### pad_button
Comprehensive enumeration of all controller buttons and axes.

```cpp
enum class pad_button : u8 {
    // D-Pad
    dpad_up = 0,
    dpad_down,
    dpad_left,
    dpad_right,

    // Center buttons
    select,
    start,
    ps,

    // Face buttons
    triangle,
    circle,
    square,
    cross,

    // Shoulder buttons
    L1, R1,
    L2, R2,
    L3, R3,

    // Analog sticks (virtual buttons for cardinal directions)
    ls_up, ls_down, ls_left, ls_right,
    ls_x, ls_y,  // Axis values
    rs_up, rs_down, rs_left, rs_right,
    rs_x, rs_y,  // Axis values

    pad_button_max_enum,  // Sentinel value

    // Special mouse buttons (for mouse-to-pad mapping)
    mouse_button_1 through mouse_button_8,
};
```

**Layout (Standard PS3 Controller):**
```
                  Triangle
    Square       Circle
                  Cross

    L1 L2        R1 R2

       D-Pad

    L3 (Stick)   R3 (Stick)

         Select Start
              PS
```

## Utility Functions

### pad_button_offset()
```cpp
u32 pad_button_offset(pad_button button);
```

**Purpose:** Get register offset for button in PS3 pad data
**Parameters:** Button enum value
**Returns:** Offset in CellPadData structure
**Usage:** Internal mapping to hardware structure

### pad_button_keycode()
```cpp
u32 pad_button_keycode(pad_button button);
```

**Purpose:** Get HID/keyboard code for button
**Parameters:** Button enum value
**Returns:** Hardware keycode value
**Usage:** Interface with lower-level input systems

## Axis Handling

### axis_direction
```cpp
enum class axis_direction : u8 {
    both = 0,        // Bidirectional axis
    negative,        // Only negative range
    positive,        // Only positive range
};
```

### get_axis_keycode()
```cpp
u32 get_axis_keycode(u32 offset, u16 value);
```

**Purpose:** Convert analog axis value to keycode
**Parameters:**
- `offset`: Axis offset (left stick/right stick)
- `value`: Axis value (0-255 or specific range)
**Returns:** Keycode representation
**Usage:** Map axis to button for games

## Port Control Flags

### PortStatus
```cpp
enum PortStatus {
    CELL_PAD_STATUS_DISCONNECTED = 0x00000000,  // Not connected
    CELL_PAD_STATUS_CONNECTED = 0x00000001,     // Currently connected
    CELL_PAD_STATUS_ASSIGN_CHANGES = 0x00000002, // Assignment changed
    CELL_PAD_STATUS_CUSTOM_CONTROLLER = 0x00000004, // Custom device type
};
```

**Usage:** Returned by cellPadGetInfo() to indicate port state

### PortSettings
```cpp
enum PortSettings {
    CELL_PAD_SETTING_LDD = 0x00000001,           // Speculative setting
    CELL_PAD_SETTING_PRESS_ON = 0x00000002,      // Pressure sensitivity on
    CELL_PAD_SETTING_SENSOR_ON = 0x00000004,     // Motion sensors on

    CELL_PAD_SETTING_PRESS_OFF = 0x00000000,     // Pressure sensitivity off
    CELL_PAD_SETTING_SENSOR_OFF = 0x00000000,    // Motion sensors off
};
```

**Features:**
- **LDD**: Large Device Driver (custom controller type)
- **PRESS**: Pressure-sensitive button support
- **SENSOR**: Motion control (accelerometer/gyroscope)

## Button State Flags

### Digital1Flags (D-Pad and Primary Buttons)
```cpp
enum Digital1Flags : u32 {
    CELL_PAD_CTRL_SELECT = 0x00000001,   // Select button
    CELL_PAD_CTRL_L3     = 0x00000002,   // Left stick click
    CELL_PAD_CTRL_R3     = 0x00000004,   // Right stick click
    CELL_PAD_CTRL_START  = 0x00000008,   // Start button
    CELL_PAD_CTRL_UP     = 0x00000010,   // D-Pad up
    CELL_PAD_CTRL_RIGHT  = 0x00000020,   // D-Pad right
    CELL_PAD_CTRL_DOWN   = 0x00000040,   // D-Pad down
    CELL_PAD_CTRL_LEFT   = 0x00000080,   // D-Pad left
    CELL_PAD_CTRL_PS     = 0x00000100,   // PS button
};
```

First digital register of CellPadData.

### Digital2Flags (Shoulder and Face Buttons)
```cpp
enum Digital2Flags : u32 {
    CELL_PAD_CTRL_L2       = 0x00000001,  // L2 shoulder
    CELL_PAD_CTRL_R2       = 0x00000002,  // R2 shoulder
    CELL_PAD_CTRL_L1       = 0x00000004,  // L1 shoulder
    CELL_PAD_CTRL_R1       = 0x00000008,  // R1 shoulder
    CELL_PAD_CTRL_TRIANGLE = 0x00000010,  // Triangle button
    CELL_PAD_CTRL_CIRCLE   = 0x00000020,  // Circle button
    CELL_PAD_CTRL_CROSS    = 0x00000040,  // Cross button
    CELL_PAD_CTRL_SQUARE   = 0x00000080,  // Square button
};
```

Second digital register of CellPadData.

### Custom Controller LDD Button
```cpp
CELL_PAD_CTRL_LDD_PS = 0x00000001;  // LDD controller PS button
```

## Capability Flags

### DeviceCapability
```cpp
enum DeviceCapability {
    CELL_PAD_CAPABILITY_PS3_CONFORMITY = 0x00000001,
    CELL_PAD_CAPABILITY_PRESS_MODE = 0x00000002,
    CELL_PAD_CAPABILITY_SENSOR_MODE = 0x00000004,
    CELL_PAD_CAPABILITY_HP_ANALOG_STICK = 0x00000008,
    CELL_PAD_CAPABILITY_ACTUATOR = 0x00000010,
};
```

**Capabilities:**
- **PS3_CONFORMITY**: Meets PS3 controller standards
- **PRESS_MODE**: Pressure sensitivity available
- **SENSOR_MODE**: Motion control available
- **HP_ANALOG_STICK**: High-precision analog sticks
- **ACTUATOR**: Force feedback/rumble support

## Device Types

### DeviceType
```cpp
enum DeviceType {
    CELL_PAD_DEV_TYPE_STANDARD = 0,      // Standard PS3 controller
    CELL_PAD_DEV_TYPE_BD_REMOCON = 4,    // Blu-ray remote control
    CELL_PAD_DEV_TYPE_LDD = 5,           // Large Device Driver (custom)
};
```

### Controller Classes (PCLASS)
```cpp
enum {
    CELL_PAD_PCLASS_TYPE_STANDARD   = 0x00,   // Regular pad
    CELL_PAD_PCLASS_TYPE_GUITAR     = 0x01,   // Guitar controller
    CELL_PAD_PCLASS_TYPE_DRUM       = 0x02,   // Drum controller
    CELL_PAD_PCLASS_TYPE_DJ         = 0x03,   // DJ turntable
    CELL_PAD_PCLASS_TYPE_DANCEMAT   = 0x04,   // Dance game mat
    CELL_PAD_PCLASS_TYPE_NAVIGATION = 0x05,   // Navigation controller
    CELL_PAD_PCLASS_TYPE_SKATEBOARD = 0x8001, // Skateboard controller

    // Special "fake" types for non-pad input
    CELL_PAD_FAKE_TYPE_FIRST = 0xa000,
    CELL_PAD_FAKE_TYPE_GUNCON3 = 0xa000,      // Light gun
    // ... other fake types
};
```

**Special Types:**
- **GUITAR**: Rock Band/Guitar Hero controller
- **DRUM**: Rock Band drums
- **DJ**: Dance games with turntable interface
- **NAVIGATION**: PlayStation Move Navigation controller
- **SKATEBOARD**: Skate game board
- **GUNCON3**: Light gun simulation

## System Information

### SystemInfo Flags
```cpp
enum SystemInfo {
    CELL_PAD_INFO_INTERCEPTED = 0x00000001,  // System intercepting input
};
```

Indicates whether system (XMB, recovery, etc.) is intercepting pad input.

## Data Organization

CellPadData structure uses these flags:

```
// Digital1 (flags)
Bit 0: SELECT
Bit 1: L3
Bit 2: R3
Bit 3: START
Bits 4-7: D-Pad (up, right, down, left)
Bit 8: PS

// Digital2 (flags)
Bits 0-3: L2, R2, L1, R1
Bits 4-7: Triangle, Circle, Cross, Square
```

## Button Pressure Sensitivity

Supported on advanced controllers:
- **L2, R2**: Analog values (0-255)
- **Face Buttons**: Per-button pressure (optional)
- **Sticks**: Pressure at stick base (optional)

## Motion/Sensor Data

For controllers with sensors:
- **Accelerometer**: X, Y, Z axes
- **Gyroscope**: Rotation rates
- **Magnetometer**: Compass heading (on some)

## Analog Stick Mapping

**Left Stick:**
- ls_x: Horizontal axis (0=left, 128=neutral, 255=right)
- ls_y: Vertical axis (0=up, 128=neutral, 255=down)
- ls_left/ls_right/ls_up/ls_down: Virtual buttons

**Right Stick:**
- rs_x: Horizontal axis
- rs_y: Vertical axis
- rs_left/rs_right/rs_up/rs_down: Virtual buttons

## Virtual Buttons for Sticks

Games can map stick movement to buttons:
- Stick pushed up → "Up" button press
- Stick pushed right → "Right" button press
- Threshold: Typically 50% stick displacement

## Trigger Mapping

Triggers (L2/R2) can be:
1. **Binary**: 0 (not pressed) or 255 (pressed)
2. **Analog**: 0-255 range pressure values
3. **Dual**: Can register both press and analog

## Mouse Button Integration

Special enumeration for mouse-to-pad mapping:
- mouse_button_1 through mouse_button_8
- Useful for games that accept both pad and mouse
- Buttons map to D-Pad or face buttons typically

## System Information Flags

**CELL_PAD_INFO_INTERCEPTED:**
- Set when XMB/system menu active
- Game may disable input handling
- Used to pause game on system menu

## Controller Assignment

Each port can be assigned a controller type:
- Standard Pad
- Motion controller
- Guitar/Drum
- Special device
- Empty (disconnected)

## Pressure Sensitivity Constants

Analog button range: 0-255
- 0: Not pressed
- 1-127: Light pressure
- 128-254: Medium to hard pressure
- 255: Maximum pressure

## Notes

- All flags are 32-bit aligned
- Uses little-endian byte order
- CellPadData pads to 64 bytes
- One structure per controller port
- Updates every game frame (60Hz)

## Compatibility

- Maintains PS3 SDK compatibility
- Extensions for new device types
- Backward-compatible enumerations
- Network-safe flag sizes

## Integration Points

- Used by cellPad* syscalls
- Referenced by controller mapping
- Input device enumeration
- Game input processing

## Common Button Combinations

**Game Menu:** PS + Select
**XMB Menu:** PS button
**System Settings:** PS + Start (some games)
**Screenshot:** PS + Triangle
**Recovery:** PS + Power (at boot)
