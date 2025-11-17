# mm_joystick_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/mm_joystick_handler.h`
- **Type**: Header File
- **Lines**: 149

## Description
Unique names for the config files and our pad settings dialog

## Includes
- `util/types.hpp`
- `Emu/Io/PadHandler.h`
- `Windows.h`
- `mmsystem.h`
- `string`
- `vector`
- `memory`
- `unordered_map`

## Classes & Structures
### MMJOYDevice
```cpp
oy_u_pos, "U+" }, { joy_u_neg, "U-" }, { joy_v_pos, "V+" }, { joy_v_neg, "V-" },
```

### mm_joystick_handler
```cpp
<mmsystem.h> #include <string> #include <vector> #include <memory> #include <uno
```


## Enumerations
- `mmjoy_axis`

## Key Functions
- `enumerate_devices()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
