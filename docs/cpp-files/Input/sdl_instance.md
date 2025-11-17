# sdl_instance.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/sdl_instance.h`
- **Type**: Header File
- **Lines**: 28

## Description
C++ Source/Header File

## Includes
- `mutex`

## Classes & Structures
### sdl_instance
```cpp
#pragma once #ifdef HAVE_SDL3 #include <mutex> struct sdl_instance { public: sdl
```


## Key Functions
- `initialize_impl()`
- `set_hint()`
- `initialize()`
- `pump_events()`
