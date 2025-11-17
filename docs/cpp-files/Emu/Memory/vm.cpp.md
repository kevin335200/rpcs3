# vm.cpp - Virtual Memory Management Implementation

## Overview
This is the implementation file for RPCS3's virtual memory system. It contains the core logic for memory allocation, deallocation, page management, protection, locking, and reservation tracking.

## Key Implementation Details

### Memory Initialization

The memory system reserves 4GB of contiguous virtual address space:
- Uses `memory_reserve_4GiB()` to find suitable address ranges
- Creates multiple memory regions for different purposes
- Initializes page tracking arrays
- Sets up shared memory mapping arrays

### Memory Locations

Seven predefined memory locations initialized in `init()`:
1. **Main (0x00010000)**: 256MB, 64KB pages, pre-allocated
2. **User64k**: User-managed, 64KB page size
3. **User1m**: User-managed, 1MB page size
4. **RSX Context**: RSX graphics context
5. **Video (0xC0000000)**: 256MB, 64KB pages, pre-allocated
6. **Stack (0xD0000000)**: 256MB, 4KB pages, guarded, pre-allocated
7. **SPU (0xE0000000)**: 512MB, 64KB pages

### Core Functions

#### Memory Allocation/Deallocation

**`block_t::try_alloc()`**
- Checks if area is already mapped
- Handles stack guard pages
- Calculates page protection flags
- Maps memory through `_page_map()`
- Fills stack guards with pattern

**`block_t::alloc()`**
- Validates size and alignment
- Creates or imports shared memory
- Searches for appropriate placement
- Returns allocated address

**`block_t::falloc()`**
- Attempts fixed address allocation
- Validates address boundaries
- Aligns address and size properly
- Calls `try_alloc()` for actual mapping

**`block_t::dealloc()`**
- Finds allocated region by address
- Validates shared memory match
- Unmaps memory through `_page_unmap()`
- Clears guard pages
- Removes entry from mapping

#### Page Management

**`_page_map()`**
- Maps physical pages to virtual address
- Updates page protection flags
- Notifies RSX of valid memory ranges
- Locks range during mapping
- Supports shared memory mapping

**`_page_unmap()`**
- Unmaps physical pages
- Clears page flags
- Notifies RSX of invalid ranges
- Deregisters PPU HLE instructions
- Handles memory decommit

**`page_protect()`**
- Changes protection flags for range
- Validates current page state
- Updates OS page protection
- Protects range locks from changes

**`check_addr()`**
- Validates address range against flags
- Checks for 4GB overflow
- Respects different page sizes (4K, 64K, 1M)
- Returns false on invalid access

#### Range Locking

**`alloc_range_lock()`**
- Allocates lock slot from pool
- Uses bit manipulation for efficiency
- Returns atomic lock pointer

**`range_lock_internal()`**
- Acquires lock for memory range
- Waits for other locks to clear
- Triggers page faults if needed
- Suspends conflicting threads

**`free_range_lock()`**
- Releases range lock
- Updates allocation bits

**`_lock_main_range_lock()`**
- Main locking operation
- Handles global memory synchronization
- Waits for overlapping ranges

#### Reservation System

**`try_reservation_update()`**
- Atomic reservation timestamp update
- Prevents locked reservations
- Returns success status and timestamp

**`reservation_update()`**
- Full reservation update with notifications
- Handles CPU state transitions
- Notifies all waiters

**`reservation_lock_internal()`**
- Locks reservation for exclusive access
- Implements busy-wait with yielding
- Respects CPU state

**`reservation_shared_lock_internal()`**
- Multiple readers, single writer pattern
- Increments shared lock count

**`reservation_op_internal()`**
- Atomic operation on reserved region
- Suspends other CPUs during operation
- Updates reservation on success/failure

#### Locking Primitives

**`passive_lock()`**
- Locks CPU for memory operations
- Enables CPU to wait in background
- Handles global lock coordination

**`passive_unlock()`**
- Releases passive lock
- Clears memory access flag

**`temporary_unlock()`**
- Temporarily unlocks CPU
- Preserves lock state for later

**`writer_lock::writer_lock()`**
- Acquires exclusive memory access
- Suspends other threads
- Waits for all reservations

### Serialization

**`block_t::save()`**
- Saves block metadata
- Serializes allocated regions
- Compresses memory using bitmap
- Skips memory matching executable

**`block_t::block_t(utils::serial&)`**
- Reconstructs block from save data
- Restores memory contents
- Handles preallocated memory

**`serialize_memory_bytes()`**
- Optimized memory serialization
- Uses 128-byte block bitmap
- Handles both write and read phases

### Utility Functions

**`check_cache_line_zero()`**
- Checks if 128-byte cache line is all zeros
- Uses SIMD operations

**`read_string()`**
- Safely reads null-terminated string
- Respects page boundaries
- Validates null-termination

**`try_access()`**
- Safe read/write with range locking
- Validates address protection
- Atomic operations for aligned data

## Thread Safety Mechanisms

### Locking Hierarchy
1. **Writer Lock**: Highest priority, exclusive access
2. **Range Locks**: Per-range synchronization
3. **Atomic Operations**: Lock-free for small data
4. **Passive Locks**: Thread registration for waits

### Synchronization Details

- **g_locks array**: Per-CPU lock registration
- **g_tls_locked**: Thread-local lock tracking
- **g_range_lock_bits**: Bit allocation for active locks
- **g_range_lock_set**: Storage for range lock data

## Performance Optimizations

1. **Reservation System**: Uses RTM (Restricted Transactional Memory) on x86-64
2. **Busy-wait Loops**: Yield after threshold to prevent starvation
3. **Cache Optimization**: Prefetch on range lock structures
4. **Memory Compression**: Skip zero blocks during serialization
5. **Page Size Granularity**: Different strategies for 4K/64K/1M pages

## Important Data Structures

### reservation_waiter_t
```cpp
struct reservation_waiter_t {
    u32 wait_flag;      // Odd=waiting, even=not waiting
    u32 waiters_count;  // Number of threads waiting
};
```

### Memory Layout Constants
- **Page Size**: 4KB for tracking (g_pages array)
- **Range Lock Slots**: 64 concurrent range locks
- **Reservation Entries**: 128 bytes apart (65536 entries)
- **Shared Memory Entries**: 65536 64KB page entries

## Error Handling

- Throws exceptions for:
  - Invalid size/alignment parameters
  - Memory already mapped
  - Concurrent access conflicts
  - Out of range allocations
  - Memory mapping failures

## Platform-Specific Code

### Windows
- Uses VirtualProtect for memory protection
- Special handling for sudo memory unmapping
- Hook area reversal for cleanup

### Linux/Unix
- Uses mprotect for memory protection
- Memory decommit via madvise

## Notes

- Main memory blocks are limited to 512MB concurrent locks
- Range locks must be page-aligned or 1-byte aligned
- Shared memory requires special handling for serialization
- Stack guard pages contain "STACKGRD" and "UNDERFLO" patterns
- RSX thread notifications prevent invalid graphics operations

## Dependencies

- Utilities/Thread.h: Thread management
- Utilities/address_range.h: Address range utilities
- Emu/CPU/CPUThread.h: CPU thread interface
- Emu/RSX/RSXThread.h: RSX graphics thread
- util/vm.hpp, asm.hpp, simd.hpp: Low-level utilities
