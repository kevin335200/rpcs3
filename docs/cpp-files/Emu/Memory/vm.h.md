# vm.h - Virtual Memory Management Header

## Overview
This is the main header file for RPCS3's virtual memory management system. It provides a comprehensive interface for managing PS3 virtual memory space, including memory allocation, protection, page management, and address translation.

## Key Global Variables

### Memory Base Addresses
- `g_base_addr`: Base address of emulated virtual memory (4GB allocated)
- `g_sudo_addr`: Unprotected virtual memory mirror (g_base_addr + 0x1'0000'0000)
- `g_exec_addr`: Auxiliary virtual memory for executable areas
- `g_stat_addr`: Statistics and debugging memory
- `g_free_addr`: Free memory for SPU usage
- `g_reservations`: Reservation statistics array (65KB)

### Memory Pages and Mapping
- `g_pages`: Global page information array (256 million entries, one per 4KB page)
- `g_locations`: Vector of memory blocks
- `g_shmem`: Pointers to shared memory or zeros

### Synchronization
- `g_tls_locked`: Thread-local variable tracking memory lock ownership
- `g_locks`: Array of atomic locks for CPU threads
- `g_range_lock_bits`: Bit allocation for range locks
- `g_range_lock_set`: Memory range lock slots

## Enumerations

### `memory_location_t`
Defines memory region types:
- `main`: Main memory (0x00010000 - 0x0FFF0000)
- `user64k`: User 64KB pages
- `user1m`: User 1MB pages
- `rsx_context`: RSX context memory
- `video`: Video memory (0xC0000000 - 0xCFFFFFFF)
- `stack`: Stack memory (0xD0000000 - 0xDFFFFFFF)
- `spu`: SPU reserved (0xE0000000 - 0xFFFFFFFF)

### `page_info_t`
Bit flags for page information:
- `page_readable` (0x01): Page is readable
- `page_writable` (0x02): Page is writable
- `page_executable` (0x04): Page is executable
- `page_fault_notification` (0x08): Enable fault notification
- `page_no_reservations` (0x10): No reservations allowed
- `page_64k_size` (0x20): 64KB page size
- `page_1m_size` (0x40): 1MB page size
- `page_allocated` (0x80): Page is allocated

### `block_flags_3`
Block allocation flags:
- `page_size_4k` (0x100): 4KB page size
- `page_size_64k` (0x200): 64KB page size
- `page_size_1m` (0x400): 1MB page size
- `stack_guarded` (0x10): Stack guard pages
- `preallocated` (0x20): Non-shareable pre-allocated

### `alloc_flags`
Memory protection flags:
- `alloc_hidden` (0x1000): Memory not readable
- `alloc_unwritable` (0x2000): Memory not writable
- `alloc_executable` (0x4000): Memory is executable

## Core Classes

### `block_t`
Represents a memory block within a specific location. Manages allocations within constant bounds.

**Key Methods:**
- `alloc()`: Search and map memory with alignment
- `falloc()`: Try to map memory at fixed location
- `dealloc()`: Unmap memory at specified location
- `peek()`: Get memory info at address
- `used()`: Get allocated memory count
- `save()/block_t(utils::serial&)`: Serialization support

**Key Members:**
- `addr`: Start address (const)
- `size`: Total size (const)
- `flags`: Block flags

### Memory Conversion Functions

#### Address Translation
- `try_get_addr()`: Convert host pointer to PS3 address (returns pair with bool validity)
- `get_addr()`: Unsafe conversion (assumes 4GiB alignment)
- `cast()`: Template function for flexible address casting
- `base()`: Convert PS3 virtual address to host pointer

#### Memory Access Functions
- `read8()`: Read 8-bit value from address
- `write8()`: Write 8-bit value (with optional breakpoint support)
- `read16()`: Read 16-bit BE value
- `write16()`: Write 16-bit BE value
- `read32()`: Read 32-bit BE value
- `write32()`: Write 32-bit BE value
- `read64()`: Read 64-bit BE value
- `write64()`: Write 64-bit BE value
- `read_string()`: Read null-terminated string safely
- `try_access()`: Safe memory read/write with protection checking

#### Super Memory Access
- `get_super_ptr()`: Get pointer bypassing memory protection
- `_ptr()`: Pointer conversion template
- `_ref()`: Reference conversion template

## Public API Functions

### Memory Allocation and Deallocation
```cpp
// Search and allocate memory in location (min alignment 0x10000)
u32 alloc(u32 size, memory_location_t location, u32 align = 0x10000);

// Map memory at specific address
bool falloc(u32 addr, u32 size, memory_location_t location = any,
            const std::shared_ptr<utils::shm>* src = nullptr);

// Unmap memory and return size
u32 dealloc(u32 addr, memory_location_t location = any,
            const std::shared_ptr<utils::shm>* src = nullptr);
```

### Memory Block Management
```cpp
// Create memory block at address
std::shared_ptr<block_t> map(u32 addr, u32 size, u64 flags = 0);

// Find and map at arbitrary position
std::shared_ptr<block_t> find_map(u32 size, u32 align, u64 flags = 0);

// Unmap and delete block
std::pair<std::shared_ptr<block_t>, bool> unmap(u32 addr, bool must_be_empty = false,
                                                const std::shared_ptr<block_t>* ptr = nullptr);

// Get block by location or address
std::shared_ptr<block_t> get(memory_location_t location, u32 addr = 0);

// Reserve or allocate segment
std::shared_ptr<block_t> reserve_map(memory_location_t location, u32 addr,
                                     u32 area_size, u64 flags = page_size_64k);
```

### Memory Protection
```cpp
// Change memory protection of region
bool page_protect(u32 addr, u32 size, u8 flags_test = 0,
                  u8 flags_set = 0, u8 flags_clear = 0);

// Check address flags safely
bool check_addr(u32 addr, u8 flags, u32 size);

template <u32 Size = 1>
bool check_addr(u32 addr, u8 flags = page_readable);
```

### Miscellaneous
```cpp
void lock_sudo(u32 addr, u32 size);
void init();
void close();
void save(utils::serial& ar);
void load(utils::serial& ar);
u32 get_shm_addr(const std::shared_ptr<utils::shm>& shared);
```

## Memory Layout

The virtual memory system uses the following layout:
- **Main Memory (0x00010000 - 0x0FFF0000)**: 256MB user accessible memory
- **User Allocations (0x10000000 - 0xC0000000)**: Dynamic allocation region
- **Video Memory (0xC0000000 - 0xCFFFFFFF)**: RSX video memory (256MB)
- **Stack (0xD0000000 - 0xDFFFFFFF)**: Thread stacks (256MB)
- **SPU Reserved (0xE0000000 - 0xFFFFFFFF)**: SPU local memory access

## Conditional Features

### Memory Breakpoints
When `RPCS3_HAS_MEMORY_BREAKPOINTS` is defined:
- Write operations can trigger breakpoint notifications
- PPU thread pauses on breakpoint
- Debug logging available

## Dependencies
- `util/types.hpp`: Type definitions
- `util/atomic.hpp`: Atomic utilities
- `util/auto_typemap.hpp`: Type mapping
- `util/to_endian.hpp`: Endianness conversion
- `ppu_thread`: PPU thread class

## Key Design Patterns

1. **RAII Memory Management**: Memory blocks use shared_ptr for automatic cleanup
2. **Lock-free Operations**: Atomic operations for synchronization without mutexes
3. **Range Locking**: Prevent concurrent access to memory ranges
4. **Page-based Tracking**: 4KB page granularity for protection
5. **Big-Endian Data**: PS3 uses BE, conversion utilities provided

## Thread Safety

The memory system provides several synchronization mechanisms:
- **Writer Lock**: `vm::writer_lock` for exclusive access
- **Passive Locks**: For thread synchronization
- **Range Locks**: For concurrent range operations
- **Reservation System**: For atomic operations

## Notes

- Default page size is aligned to 0x10000 (64KB)
- Memory addresses are 32-bit PS3 addresses
- Super memory (g_sudo_addr) provides unprotected access for debugging
- Shared memory objects support serialization for save states
