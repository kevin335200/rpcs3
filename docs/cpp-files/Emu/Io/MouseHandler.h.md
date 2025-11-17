# MouseHandler.h - Mouse Input Handler

## Overview
Provides structures and enumerations for handling mouse input in RPCS3. Supports multiple mice, button input, movement tracking, and wheel/tilt controls.

## Global Constants

```cpp
static const u32 MAX_MICE = 127;           // Maximum connected mice
static const u32 MOUSE_MAX_DATA_LIST_NUM = 8;  // Max buffered data points
static const u32 MOUSE_MAX_CODES = 64;     // Max raw data size
```

## Enumerations

### CELL_MOUSE_INFO Flags

**Tablet Support:**
```cpp
CELL_MOUSE_INFO_TABLET_NOT_SUPPORTED = 0;
CELL_MOUSE_INFO_TABLET_SUPPORTED = 1;
```

**Mode:**
```cpp
CELL_MOUSE_INFO_TABLET_MOUSE_MODE = 1;    // Standard mouse mode
CELL_MOUSE_INFO_TABLET_TABLET_MODE = 2;   // Tablet/touchpad mode
```

**Interception:**
```cpp
CELL_MOUSE_INFO_INTERCEPTED = 1;  // System intercepting input
```

### MousePortStatus
```cpp
enum MousePortStatus {
    CELL_MOUSE_STATUS_DISCONNECTED = 0x00000000,
    CELL_MOUSE_STATUS_CONNECTED    = 0x00000001,
};
```

Connection status of mouse port.

### MouseDataUpdate
```cpp
enum MouseDataUpdate {
    CELL_MOUSE_DATA_UPDATE = 1,  // New data available
    CELL_MOUSE_DATA_NON    = 0,  // No new data
};
```

Indicates whether mouse state changed since last read.

### MouseButtonCodes

```cpp
enum MouseButtonCodes {
    CELL_MOUSE_BUTTON_1 = 0x00000001,  // Left button
    CELL_MOUSE_BUTTON_2 = 0x00000002,  // Right button
    CELL_MOUSE_BUTTON_3 = 0x00000004,  // Middle button
    CELL_MOUSE_BUTTON_4 = 0x00000008,  // Extra button 1
    CELL_MOUSE_BUTTON_5 = 0x00000010,  // Extra button 2
    CELL_MOUSE_BUTTON_6 = 0x00000020,  // Extra button 3
    CELL_MOUSE_BUTTON_7 = 0x00000040,  // Extra button 4
    CELL_MOUSE_BUTTON_8 = 0x00000080,  // Extra button 5
};
```

Bit flags for 8 button mouse. Multiple buttons can be pressed simultaneously.

## Helper Functions

### get_mouse_button_code()
```cpp
static inline MouseButtonCodes get_mouse_button_code(int i)
```

**Purpose:** Convert button index (0-7) to button code
**Parameters:** i - Button index
**Returns:** Corresponding MouseButtonCodes value
**Throws:** Exception if index > 7

**Example:**
```cpp
MouseButtonCodes left = get_mouse_button_code(0);   // CELL_MOUSE_BUTTON_1
MouseButtonCodes right = get_mouse_button_code(1);  // CELL_MOUSE_BUTTON_2
```

## Data Structures

### MouseInfo
Describes available mice and system state.

```cpp
struct MouseInfo {
    u32 max_connect = 0;                    // Max possible connections
    u32 now_connect = 0;                    // Currently connected count
    u32 info = 0;                           // System info flags
    u32 mode[MAX_MICE]{};                   // Mouse mode per device
    u32 tablet_is_supported[MAX_MICE]{};    // Tablet support per device
    u16 vendor_id[MAX_MICE]{};              // USB vendor ID
    u16 product_id[MAX_MICE]{};             // USB product ID
    u8 status[MAX_MICE]{};                  // Port status (connected/disconnected)
    bool is_null_handler = false;           // Using null handler (no input)
};
```

**Usage:** Queried by game to discover available mice and features

### MouseRawData
Raw report data from mouse.

```cpp
struct MouseRawData {
    s32 len = 0;                    // Actual data length
    u8 data[MOUSE_MAX_CODES]{};     // Raw HID report (up to 64 bytes)
};
```

**Purpose:** Direct HID data for advanced mouse implementations

### MouseData
Processed mouse input state.

```cpp
struct MouseData {
    u8 update = 0;          // Data update flag (1 if changed)
    u8 buttons = 0;         // Button state (bitmask of CELL_MOUSE_BUTTON_*)
    s8 x_axis = 0;          // Relative X movement (-127 to 127)
    s8 y_axis = 0;          // Relative Y movement (-127 to 127)
    s8 wheel = 0;           // Scroll wheel (-127 to 127)
    s8 tilt = 0;            // Tilt/horizontal scroll (-127 to 127)

    s32 pixel_x = 0;        // Absolute X position (pixel coordinates)
    s32 pixel_y = 0;        // Absolute Y position (pixel coordinates)
    // (Additional fields in actual implementation)
};
```

**Fields:**
- `update`: 1 if any field changed since last read, 0 otherwise
- `buttons`: Combination of CELL_MOUSE_BUTTON_* flags
- `x_axis`/`y_axis`: Movement delta since last read (relative)
- `wheel`: Scroll wheel rotation (positive=up, negative=down)
- `tilt`: Horizontal scroll or tilt (for some mice)
- `pixel_x`/`pixel_y`: Absolute screen position

**Note:** Relative movement is primary; absolute position supplementary

## Input Range

- **Buttons**: 0-8 simultaneously
- **Movement**: -127 to +127 per frame
- **Wheel**: -127 to +127 per frame
- **Tilt**: -127 to +127 per frame

## Mouse Support Features

### Supported Mice Types
1. **Standard USB Mice**: Movement + 3 buttons
2. **Gaming Mice**: Extra buttons, high-speed tracking
3. **Wireless Mice**: Via USB receiver
4. **Trackpads**: Absolute positioning + relative movement
5. **Multi-button Mice**: Up to 8 buttons

### Supported Actions
- Button press/release
- Movement tracking (relative)
- Scroll wheel up/down
- Tilt/horizontal scroll
- Absolute positioning (for tablets)

## Multi-Mouse Support

RPCS3 can handle up to 127 mice:
- Each mouse gets dedicated port (0-126)
- Independent button/movement tracking
- Separate status per port
- Useful for mice-based games

## Mode Selection

### Mouse Mode
Standard relative movement mode:
- Reports movement deltas
- Suitable for games with crosshair
- Provides button and wheel input
- Typical for FPS/action games

### Tablet Mode
Absolute positioning mode (when supported):
- Reports absolute coordinates
- Suitable for drawing/UI
- May include pressure sensitivity
- Varies by device

## Update Semantics

The `update` field indicates change:
- `1`: Any field changed since last read
- `0`: No changes (same state as last frame)

Games can optimize by skipping unchanged data.

## Button Mapping

Typical mapping:
- Button 1 (0x01): Left/Primary button
- Button 2 (0x02): Right/Context button
- Button 3 (0x04): Middle/Wheel press
- Buttons 4-8: Extra buttons if available

## Platform Considerations

### Windows
- Uses raw input or DirectInput
- Good support for most mice
- USB device enumeration available

### Linux
- Uses evdev interface
- Supports standard mice
- Trackpad support varies

### macOS
- IOKit-based implementation
- Magic Mouse special handling
- Trackpad as mouse option

## Typical Usage Flow

1. Game calls cellMouseGetInfo() → get MouseInfo
2. Game calls cellMouseGetData() → get MouseData
3. Update loop reads mouse state every frame
4. Game responds to button presses and movement
5. Repeat from step 2

## Performance Characteristics

- **Polling**: 60Hz typical (synced with game)
- **Latency**: <2ms typical
- **CPU Usage**: <0.1% for mouse handling
- **Memory**: ~8KB per mouse

## Error Handling

- Invalid mouse index returns error
- Invalid button index throws exception
- Disconnected mouse marked in status
- Failed reads return update=0

## Null Handler

When `is_null_handler = true`:
- No actual mouse input available
- Used for testing/headless mode
- All data fields return defaults
- Status shows disconnected

## Extensions

The header mentions TODO items for future improvements:
- Tablet mode full support
- Pressure sensitivity (for drawing apps)
- Extended button mapping
- High-DPI support

## Integration

Integrated with:
- Main input system
- PAD mapping (mouse as pad)
- Configuration system
- Save/load state

## Notes

- Relative movement is frame-based (delta since last read)
- Absolute positioning supplementary (not primary interface)
- Button presses are sticky within a frame
- Multiple reads within frame return same data
- Movement accumulates if not read frequently
