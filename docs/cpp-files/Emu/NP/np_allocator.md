# np_allocator.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/np_allocator.h`
- **Type**: Header File
- **Lines**: 127

## Description
C++ Source/Header File

## Includes
- `map`
- `Emu/Memory/vm_ptr.h`
- `Utilities/mutex.h`
- `util/asm.hpp`
- `util/logs.hpp`

## Namespaces
- `np`

## Classes & Structures
### memory_allocator
```cpp
lude "util/asm.hpp" #include "util/logs.hpp" LOG_CHANNEL(np_mem_allocator); name
```


## Key Functions
- `shrink_allocation()`
- `release()`
- `lock()`
- `allocate()`
- `free()`
- `save()`
- `setup()`
