# np_gui_cache.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/np_gui_cache.h`
- **Type**: Header File
- **Lines**: 55

## Description
C++ Source/Header File

## Includes
- `map`
- `Utilities/mutex.h`
- `Emu/Cell/Modules/sceNp.h`

## Namespaces
- `np`

## Classes & Structures
### gui_room_member
```cpp
td::memcmp(a.handle.data, b.handle.data, sizeof(a.handle.data)) < 0); } }; names
```

### gui_cache_manager
```cpp
ool owner; }; struct gui_room_cache { std::map<SceNpId, gui_room_member> members
```

### gui_room_cache
```cpp
; } }; namespace np { struct gui_room_member { SceNpUserInfo info; bool owner; }
```

### std
```cpp
#include <map> #include "Utilities/mutex.h" #include "Emu/Cell/Modules/sceNp.h" 
```


## Key Functions
- `add_member()`
- `del_room()`
- `add_room()`
- `operator()`
- `del_member()`
