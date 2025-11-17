# pad_thread.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Input/pad_thread.h`
- **Type**: Header File
- **Lines**: 110

## Description
void * instead of QThread * and QWindow * because of include in emucore

## Includes
- `util/types.hpp`
- `util/atomic.hpp`
- `Emu/Io/pad_types.h`
- `Emu/Io/pad_config.h`
- `Emu/Io/pad_config_types.h`
- `Utilities/mutex.h`
- `map`
- `mutex`
- `string_view`
- `string`

## Namespaces
- `pad`

## Classes & Structures
### PadHandlerBase
```cpp
Utilities/mutex.h" #include <map> #include <mutex> #include <string_view> #inclu
```

### pad_thread
```cpp
clude <map> #include <mutex> #include <string_view> #include <string> class PadH
```


## Key Functions
- `set_enabled()`
- `reset()`
- `open_home_menu()`
- `lock()`
- `operator()`
- `apply_copilots()`
- `update_pad_states()`
