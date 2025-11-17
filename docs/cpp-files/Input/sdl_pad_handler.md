# sdl_pad_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/sdl_pad_handler.h`
- **Type**: Header File
- **Lines**: 192

## Description
C++ Source/Header File

## Includes
- `Emu/Io/PadHandler.h`
- `SDL3/SDL.h`

## Classes & Structures
### touch_point
```cpp
_MSC_VER #pragma GCC diagnostic pop #endif class SDLDevice : public PadDevice { 
```

### touchpad
```cpp
PadDevice { public: struct touch_point { int index = 0; int x = 0; int y = 0; };
```

### SDLDevice
```cpp
style-cast" #endif #include "SDL3/SDL.h" #ifndef _MSC_VER #pragma GCC diagnostic
```

### sdl_pad_handler
```cpp
d_is_on = true; bool led_is_blinking = false; steady_clock::time_point led_times
```

### sdl_info
```cpp
t y = 0; }; struct touchpad { int index = 0; std::vector<touch_point> fingers; }
```


## Enumerations
- `SDLKeyCodes`

## Key Functions
- `enumerate_devices()`
- `get_battery_level()`
- `get_motion_sensors()`
- `apply_pad_data()`
- `get_battery_color()`
- `button_to_string()`
- `process()`
- `get_extended_info()`
- `get_is_right_stick()`
- `axis_to_string()`
- `init_config()`
- `get_is_touch_pad_motion()`
- `get_is_left_trigger()`
- `get_is_right_trigger()`
- `get_is_left_stick()`
