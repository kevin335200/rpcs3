# evdev_joystick_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/evdev_joystick_handler.h`
- **Type**: Header File
- **Lines**: 430

## Description
C++ Source/Header File

## Includes
- `util/types.hpp`
- `Utilities/File.h`
- `Emu/Io/PadHandler.h`
- `libevdev/libevdev.h`
- `memory`
- `unordered_map`
- `array`
- `vector`
- `ctime`

## Classes & Structures
### evdev_sensor
```cpp
of a regular axis and 1 in case of a reverse axis int type = 0; // EV_KEY or EV_
```

### positive_axis
```cpp
clude <memory> #include <unordered_map> #include <array> #include <vector> #incl
```

### EvdevButton
```cpp
}, { ABS_Z , "Z" }, { ABS_RX , "RX" }, { ABS_RY , "RY" }, { ABS_RZ , "RZ" }, }; 
```

### axis_event_wrapper
```cpp
public input_event_wrapper { key_event_wrapper() { type = EV_KEY; } u16 value{};
```

### input_event_wrapper
```cpp
struct evdev_sensor : public EvdevButton { bool mirrored = false; s32 shift = 0;
```

### EvdevDevice
```cpp
rection (negative = true) bool is_trigger{}; int min{}; int max{}; int flat{}; }
```

### evdev_joystick_handler
```cpp
{ this, "ABS_MT_TOOL_Y", false }; bool load(); void save() const; bool exist() c
```

### key_event_wrapper
```cpp
ruct input_event_wrapper { int type{}; // EV_KEY or EV_ABS bool is_initialized{}
```


## Key Functions
- `close_devices()`
- `apply_pad_data()`
- `get_device_name()`
- `load()`
- `check_button_set()`
- `check_button_sets()`
- `bindPadToDevice()`
- `exist()`
- `get_is_left_stick()`
- `get_mapping()`
- `get_is_right_stick()`
- `init_config()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_motion_sensors()`
