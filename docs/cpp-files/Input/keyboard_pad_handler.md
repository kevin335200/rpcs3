# keyboard_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/keyboard_pad_handler.h`
- **Type**: Header File
- **Lines**: 152

## Description
Unique button names for the config files and our pad settings dialog

## Includes
- `util/types.hpp`
- `Emu/Io/PadHandler.h`
- `QWindow`
- `QKeyEvent`
- `string`
- `vector`
- `unordered_map`

## Classes & Structures
### keyboard_pad_handler
```cpp
}, { mouse::wheel_left , "Wheel Left" }, { mouse::wheel_right , "Wheel Right" },
```


## Enumerations
- `mouse`

## Key Functions
- `process()`
- `keyPressEvent()`
- `release_all_keys()`
- `get_mouse_lock_state()`
- `native_scan_code_to_string()`
- `bindPadToDevice()`
- `processKeyEvent()`
- `mouseMoveEvent()`
- `mouseWheelEvent()`
- `keyReleaseEvent()`
- `mouseReleaseEvent()`
- `init_config()`
- `eventFilter()`
- `native_scan_code_from_string()`
- `mousePressEvent()`
