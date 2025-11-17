# gui_pad_thread.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/gui_pad_thread.h`
- **Type**: Header File
- **Lines**: 103

## Description
C++ Source/Header File

## Includes
- `util/types.hpp`
- `util/atomic.hpp`
- `Emu/Io/pad_types.h`
- `Emu/Io/pad_config.h`
- `Emu/Io/pad_config_types.h`
- `Utilities/Timer.h`
- `Utilities/Thread.h`

## Classes & Structures
### gui_settings
```cpp
ig_types.h" #include "Utilities/Timer.h" #include "Utilities/Thread.h" class Pad
```

### mouse_wheel
```cpp
id process_input(); enum class mouse_button { none, left, right, middle }; enum 
```

### mouse_button
```cpp
{ m_reset = true; } protected: bool init(); void run(); void process_input(); en
```

### gui_pad_thread
```cpp
"Utilities/Timer.h" #include "Utilities/Thread.h" class PadHandlerBase; class gu
```

### PadHandlerBase
```cpp
clude "Emu/Io/pad_config_types.h" #include "Utilities/Timer.h" #include "Utiliti
```


## Enumerations
- `mouse_button`
- `mouse_wheel`

## Key Functions
- `send_mouse_button_event()`
- `send_mouse_wheel_event()`
- `reset()`
- `process_input()`
- `init()`
- `emit_event()`
- `send_mouse_move_event()`
- `run()`
- `send_key_event()`
- `update_settings()`
