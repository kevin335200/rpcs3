# KeyboardHandler.h - Keyboard Input Handler

## Overview
Provides keyboard input infrastructure for RPCS3. Supports multiple keyboards, key mapping, modifier tracking, and layout support (101-key ANSI, etc.).

## Global Constants

```cpp
// Maximum keyboard limit (from Keyboard.h)
CELL_KB_MAX_KEYBOARDS    // Max simultaneous keyboards
CELL_KB_MAX_KEYCODES     // Max keys in single report
```

## Enumerations

### QtKeys
Qt framework key codes (for GUI input):

```cpp
enum QtKeys {
    Key_Shift      = 0x01000020,
    Key_Control    = 0x01000021,
    Key_Meta       = 0x01000022,
    Key_Alt        = 0x01000023,
    Key_CapsLock   = 0x01000024,
    Key_NumLock    = 0x01000025,
    Key_ScrollLock = 0x01000026,
    Key_Super_L    = 0x01000053,
    Key_Super_R    = 0x01000054
};
```

Used when receiving GUI key events.

### native_key
Platform-specific key codes:

**Windows (VK codes + extended bits):**
```cpp
ctrl_l = 0x001D,   shift_l = 0x002A,   alt_l = 0x0038,
ctrl_r = 0xE01D,   shift_r = 0x0036,   alt_r = 0xE038,
meta_l = 0xE05B,   meta_r = 0xE05C,
```

**macOS (kVK codes):**
```cpp
ctrl_l = 0x3B,   shift_l = 0x38,   alt_l = 0x3A,
ctrl_r = 0x3E,   shift_r = 0x3C,   alt_r = 0x3D,
meta_l = 0x37,   meta_r = 0x36,
```

**Linux (X11 keycodes):**
```cpp
ctrl_l = 0x0025,   shift_l = 0x0032,   alt_l = 0x0040,
ctrl_r = 0x0069,   shift_r = 0x003E,   alt_r = 0x006C,
meta_l = 0x0085,   meta_r = 0x0086,
```

## Data Structures

### KbInfo
System information about connected keyboards.

```cpp
struct KbInfo {
    u32 max_connect = 0;                        // Max possible connections
    u32 now_connect = 0;                        // Currently connected count
    u32 info = 0;                               // System info flags
    bool is_null_handler = false;               // Using null input mode
    std::array<u8, CELL_KB_MAX_KEYBOARDS> status{}; // Status per keyboard
};
```

**Fields:**
- `max_connect`: Maximum keyboards (typically 1-4)
- `now_connect`: Currently connected keyboards
- `info`: System flags
- `status[]`: Per-keyboard connection status (connected/disconnected)
- `is_null_handler`: True if no physical keyboard available

### KbButton
Represents a single key press.

```cpp
struct KbButton {
    u32 m_keyCode = 0;          // Input key code
    u32 m_outKeyCode = 0;       // Output key code (after mapping)
    bool m_pressed = false;     // Currently pressed

    KbButton() = default;
    KbButton(u32 keyCode, u32 outKeyCode, bool pressed = false);
};
```

**Fields:**
- `m_keyCode`: Native/raw key code
- `m_outKeyCode`: Mapped key code (after user remapping)
- `m_pressed`: True if key is down

### KbData
Current keyboard input state.

```cpp
struct KbData {
    u32 led = 0;                                    // LED state
    u32 mkey = 0;                                  // Active modifiers
    s32 len = 0;                                   // Number of keys pressed
    std::array<KbButton, CELL_KB_MAX_KEYCODES> buttons{};  // Key states
};
```

**Fields:**
- `led`: LED state bitmask (caps lock, num lock, scroll lock)
- `mkey`: Modifier keys state (shift, ctrl, alt, etc.)
- `len`: Number of pressed keys (0 = no keys, negative = error)
- `buttons[]`: Array of pressed keys

**LED Bits (typical):**
```cpp
LED_SCROLL_LOCK = 0x01
LED_NUM_LOCK    = 0x02
LED_CAPS_LOCK   = 0x04
```

**Modifier Bits (mkey):**
```cpp
MOD_SHIFT   = 0x02
MOD_CTRL    = 0x01
MOD_ALT     = 0x04
MOD_META    = 0x08
```

### KbExtraData
Additional keyboard tracking.

```cpp
struct KbExtraData {
    std::set<std::u32string> pressed_keys{};  // Unicode key names
};
```

**Purpose:** Track pressed keys for text input

### KbConfig
Keyboard configuration parameters.

```cpp
struct KbConfig {
    u32 arrange = CELL_KB_MAPPING_101;          // Keyboard layout
    u32 read_mode = CELL_KB_RMODE_INPUTCHAR;    // Read mode
    u32 code_type = CELL_KB_CODETYPE_ASCII;     // Character encoding
};
```

**Arrange (Layout) Options:**
```cpp
CELL_KB_MAPPING_101    // US 101-key ANSI
CELL_KB_MAPPING_106    // Japanese 106-key
CELL_KB_MAPPING_DVORAK // Dvorak layout
// Others for international layouts
```

**Read Mode:**
```cpp
CELL_KB_RMODE_INPUTCHAR  // Character mode (ASCII text)
CELL_KB_RMODE_INPUTKEY   // Key mode (raw key codes)
```

**Code Type:**
```cpp
CELL_KB_CODETYPE_ASCII   // ASCII character codes
CELL_KB_CODETYPE_RAW     // Raw key codes
```

## Key Mapping

### Supported Layouts
- **US 101-key** (ANSI): Standard US layout
- **Japanese 106-key**: Japanese specific keys
- **Dvorak**: Alternative key arrangement
- **International**: Various country-specific layouts

### Keyboard Events

**Key Down:**
1. User presses key
2. Key code captured
3. Mapping applied based on layout
4. Key added to pressed keys list
5. LED state updated if applicable

**Key Up:**
1. User releases key
2. Key removed from pressed keys
3. Modifier state updated
4. No key code generated (only on down)

### Modifier Keys

Modifiers affect interpretation:
- **Shift**: Changes case (letters) or access alternate symbols
- **Ctrl**: Combined with other keys for commands
- **Alt**: Alternate mappings
- **Meta** (Windows/Command): OS-specific commands

## Text Input vs Key Input

### Character Mode (INPUTCHAR)
- Returns ASCII/Unicode characters
- Respects keyboard layout
- Modifier keys applied
- Suitable for text entry

### Key Mode (INPUTKEY)
- Returns raw key codes
- Ignores layout
- Each key has unique code
- Suitable for games and remapping

## Connection Status

```cpp
enum {
    CELL_KB_STATUS_DISCONNECTED = 0,
    CELL_KB_STATUS_CONNECTED = 1,
};
```

## Multi-Keyboard Support

RPCS3 supports multiple keyboards:
- Each keyboard in separate port
- Independent key tracking
- Useful for multi-player text entry
- Separate LED control per keyboard

## Common Keyboard Events

### Typical Key Codes
```cpp
// Letter keys
'A' to 'Z' (0x41-0x5A) or custom codes

// Number keys
'0' to '9' (0x30-0x39)

// Function keys
F1-F12 (varies by platform)

// Special keys
Return, Space, Backspace, Escape, Tab
Shift, Control, Alt, Caps Lock
Home, End, PageUp, PageDown
Arrow Keys, Insert, Delete
```

## LED Indicators

Keyboards can report LED state:
- **Caps Lock**: Capital letter mode
- **Num Lock**: Numeric keypad mode
- **Scroll Lock**: Screen scroll mode

These may be controllable from PS3 application.

## Error Handling

**KbData.len interpretation:**
- `len > 0`: Number of pressed keys
- `len = 0`: No keys pressed
- `len < 0`: Error condition

## Integration with Input System

Keyboard handler integrates with:
- Main input dispatcher
- Configuration/remapping system
- Text input handling
- UI event routing

## Platform-Specific Notes

### Windows
- Uses Raw Input API
- Supports all standard layouts
- Key codes via VK_* constants

### Linux
- Uses X11/Wayland events
- evdev for raw input
- XKB for layout handling

### macOS
- Uses IOKit or Quartz
- NSEvent-based input
- Keyboard layout from system

## Null Handler Mode

When `is_null_handler = true`:
- No physical keyboard
- Used for testing
- All keys return "not pressed"
- Status shows disconnected

## Usage Pattern

1. Game calls cellKbGetInfo() → get KbInfo
2. Game configures layout via cellKbSetConfig()
3. Game enters input loop:
   - Game calls cellKbRead()
   - Get KbData with current keys
   - Process key states
   - Generate character/key codes
4. Repeat until game exit

## Text Input Example

```cpp
// User types "Hello"
// Sequence of events:
// - H key pressed -> character 'H'
// - e key pressed -> character 'e'
// - l key pressed -> character 'l'
// - l key pressed -> character 'l'
// - o key pressed -> character 'o'
```

## Key Remapping

Supports remapping keys:
- `m_keyCode`: Original key
- `m_outKeyCode`: Remapped key
- Used for game-specific controls
- Configuration stored in settings

## Performance

- **Polling**: 60Hz typical
- **Latency**: <5ms typical
- **CPU Usage**: <0.1%
- **Memory**: Per-key overhead minimal

## Notes

- Key repeat handled at OS level
- Macro keys may be limited
- Some platforms restrict certain keys (security)
- IME (Input Method Editor) for Asian languages
- Copy/Paste via Ctrl+C/V typically unavailable
