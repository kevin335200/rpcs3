# raw_mouse_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/raw_mouse_handler.h`
- **Type**: Header File
- **Lines**: 128

## Description
C++ Source/Header File

## Includes
- `Emu/Io/MouseHandler.h`
- `Emu/RSX/display.h`
- `Utilities/Config.h`
- `Utilities/mutex.h`
- `Utilities/Thread.h`

## Classes & Structures
### mouse_button
```cpp
void set_index(u32 index); void request_reload() { m_reload_requested = true; } 
```

### raw_mouse_handler
```cpp
.h" #include "Utilities/Config.h" #include "Utilities/mutex.h" #include "Utiliti
```

### raw_mouse
```cpp
.h" #include "Utilities/Config.h" #include "Utilities/mutex.h" #include "Utiliti
```


## Key Functions
- `handle_native_event()`
- `update_devices()`
- `is_for_gui()`
- `reload_config()`
- `key_press_callback()`
- `update_values()`
- `set_key_press_callback()`
- `get_now_connect()`
- `update_window_handle()`
- `register_raw_input_devices()`
- `set_index()`
- `index()`
- `unregister_raw_input_devices()`
- `set_mouse_press_callback()`
- `center_cursor()`
