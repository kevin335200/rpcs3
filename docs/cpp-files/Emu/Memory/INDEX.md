# RPCS3 Emu/Memory Module Documentation Index

## Module Overview

The Memory module (`rpcs3/Emu/Memory/`) provides comprehensive virtual memory management for the PS3 emulator. It handles:

- **Virtual Memory Management**: 4GB address space emulation
- **Memory Allocation**: Block-based allocation with different page sizes
- **Page Protection**: Readable/Writable/Executable flags per page
- **Address Translation**: Conversion between PS3 addresses and host pointers
- **Atomic Operations**: Lock-free synchronization using RTM on x86-64
- **Locking & Synchronization**: Range locks, writer locks, passive locking
- **Reservation System**: Load-Linked/Store-Conditional style atomics
- **Serialization**: Save state support

## File Documentation

### Core Virtual Memory System

#### [vm.h](./vm.h.md)
**Main virtual memory interface header**
- Global memory bases (g_base_addr, g_sudo_addr, g_exec_addr, etc.)
- Memory location enum (main, video, stack, SPU, etc.)
- Page information flags and block flags
- Memory allocation/deallocation functions
- Memory block class (block_t)
- Address translation functions
- Memory access primitives (read8/16/32/64, write8/16/32/64)
- String reading and safe memory access

**Key Classes:** `block_t`
**Key Functions:** `alloc()`, `falloc()`, `dealloc()`, `map()`, `unmap()`, `page_protect()`, `check_addr()`

#### [vm.cpp](./vm.cpp.md)
**Virtual memory implementation**
- Memory initialization and cleanup
- Page mapping and unmapping with RSX synchronization
- Page protection changes
- Block allocation and deallocation logic
- Serialization of memory state for save states
- Range lock operations
- Reservation update and notification
- Passive lock management
- Memory compression for serialization

**Key Implementations:** Page management, memory locking, serialization, CPU coordination

### Memory Pointers

#### [vm_ptr.h](./vm_ptr.h.md)
**Smart pointer wrapper for PS3 virtual memory**
- `_ptr_base<T, AT>`: Generic pointer template storing 32-bit address
- Pointer arithmetic (++, --, +, -)
- Member pointer access (ptr(), ref() on struct members)
- Type conversion and casting
- Function pointer specialization
- Endianness-aware pointer aliases (ptrl, ptrb, bptrl, etc.)
- Safe memory access (try_read, try_write)
- Alignment checking

**Key Types:** `ptr<T>`, `cptr<T>`, `bptr<T>`, `pptr<T>`, etc.
**Key Features:** Type-safe address storage, automatic endianness, pointer arithmetic

### Memory References

#### [vm_ref.h](./vm_ref.h.md)
**Reference wrapper for PS3 virtual memory**
- `_ref_base<T, AT>`: Reference storing 32-bit address
- Implicit value conversions
- Arithmetic operations (++, --, +=, -=, etc.)
- Compound assignments (*=, /=, &=, |=, ^=, etc.)
- Pointer conversion (ref.ptr())
- Endianness-aware reference aliases (refl, refb, brefb, etc.)

**Key Types:** `ref<T>`, `bref<T>`
**Key Features:** Value semantics, transparent endianness, arithmetic operations

### Memory Variables

#### [vm_var.h](./vm_var.h.md)
**RAII memory variable wrapper**
- `_var_base<T, A>`: Scalar variable template with allocator
- `_var_base<T[], A>`: Array variable specialization
- `page_allocator`: Allocates from memory location with 64KB alignment
- `stack_allocator`: Allocates from CPU thread stack
- `gvar<T>`: Global variable with fixed allocation parameters
- Factory functions: `make_var()`, `make_str()`
- Endianness variants (varl, varb)

**Key Types:** `var<T>`, `gvar<T>`, `make_var()`, `make_str()`
**Key Features:** Automatic allocation/deallocation, RAII pattern, allocator support

### Memory Locking & Synchronization

#### [vm_locking.h](./vm_locking.h.md)
**Memory access synchronization primitives**
- `writer_lock`: RAII exclusive memory access lock
- Range lock functions for coordinated access
- Passive locking for thread waiting
- Temporary lock/unlock for yielding
- Range lock flags (readable, writable, locked)
- Lock pool management (64 concurrent range locks)

**Key Classes:** `writer_lock`
**Key Functions:** `alloc_range_lock()`, `free_range_lock()`, `range_lock()`, `passive_lock()`, `passive_unlock()`

#### [vm_reservation.h](./vm_reservation.h.md)
**Atomic operations and reservation system**
- `reservation_op()`: Main atomic operation with RTM fallback
- `peek_op()`: Non-blocking read without modification
- `light_op()`: Lightweight operation on real memory
- Reservation locking and state tracking
- Waiter notification system
- Three-stage execution (RTM optimistic, lightened RTM, heavyweight lock)
- RTM integration on x86-64 (xbegin/xend)
- CPU state management

**Key Functions:** `reservation_op()`, `peek_op()`, `light_op()`, `reservation_lock()`
**Key Features:** Lock-free atomics, RTM optimization, three-stage fallback

## Memory Layout

PS3 Virtual Address Space:
```
0x00000000 - 0x00010000  (Reserved)
0x00010000 - 0x0FFF0000  (Main Memory - 256MB)
0x10000000 - 0xC0000000  (User Allocations - 2GB+)
0xC0000000 - 0xCFFFFFFF  (Video Memory - 256MB)
0xD0000000 - 0xDFFFFFFF  (Stack - 256MB with guards)
0xE0000000 - 0xFFFFFFFF  (SPU Reserved - 512MB)
```

Host Memory Regions:
```
g_base_addr      → [0x0000...0000 - 0xFFFF...FFFF]  (4GB emulated VM)
g_sudo_addr      → g_base_addr + 0x1'0000'0000     (Unprotected mirror)
g_exec_addr      → Next 3GB (executable areas)
g_hook_addr      → Next 8GB (hooks for R/W interception)
g_stat_addr      → Next 4GB (debugging statistics)
g_free_addr      → g_stat_addr + 0x1'0000'0000    (SPU usage)
```

## Page Management

- **Page Size**: 4KB (4096 bytes) for tracking
- **Page Granularity**: Different page sizes supported (4K, 64K, 1M)
- **Page Info**: Flags stored in atomic u8 per page
- **Page Tracking**: 256 million entries (one per 4KB)
- **Protection Flags**: Readable, Writable, Executable, Allocated, etc.

## Key Concepts

### Memory Blocks (block_t)
- Represent regions with consistent allocation policies
- Each location (main, stack, video, etc.) has one block
- Manage internal allocation map
- Support shared memory for serialization

### Address Translation
- PS3 32-bit addresses → Host pointer via g_base_addr
- Automatic endianness conversion for data
- Safe access checks before dereference

### Endianness Handling
- PS3 is big-endian (BE)
- Automatic conversion via `to_be_t<T>`
- Different pointer/reference variants for LE/BE data

### Atomic Operations
- Reservation per 128-byte block
- RTM (Restricted Transactional Memory) on x86-64
- Fallback to writer locks when needed
- Enables lock-free concurrency

### Thread Synchronization
- Writer locks for exclusive access
- Range locks for per-range synchronization
- Passive locks for waiting threads
- Reservation notifications for atomic op completion

## Thread Safety

- Memory allocation/deallocation: Thread-safe (writer lock)
- Memory access: Protected by range locks if needed
- Atomic operations: Lock-free or lock-based depending on RTM
- Pointer/Reference: Not inherently thread-safe (use atomic operations for sharing)

## Performance Characteristics

- **Fast Path**: RTM transaction succeeds → ~20 cycles
- **Medium Path**: RTM fails, lightened lock → ~100-500 cycles
- **Slow Path**: Heavyweight lock, suspend all → ~1000+ cycles
- **Memory Overhead**: ~10% for tracking structures

## Common Usage Patterns

### Allocating Temporary Memory
```cpp
u32 addr = vm::alloc(1024, vm::main);
// Use memory at addr
vm::dealloc(addr);
```

### HLE Function with Local Variables
```cpp
vm::var<u32> local_var;
*local_var = 42;
```

### Atomic Counter Increment
```cpp
vm::ptr<u32> counter{0x10000};
vm::reservation_op(cpu, counter, [](u32& val) {
    val++;
});
```

### Safe Memory Read
```cpp
u32 value = 0;
vm::try_access(0x10000, &value, sizeof(value), false);
```

## Integration Points

- **CPU Threads**: Coordinate through locks, register/unregister
- **RSX Graphics**: Notified of memory changes via callbacks
- **PPU/SPU**: Use memory primitives for communication
- **Save States**: Memory serialization for persistence

## Dependencies

- **util/types.hpp**: Type definitions
- **util/atomic.hpp**: Atomic primitives
- **util/to_endian.hpp**: Endianness conversion
- **Emu/CPU/CPUThread.h**: Thread management
- **Emu/RSX/RSXThread.h**: Graphics coordination

## Architecture Notes

- **32-bit Address Space**: Matches PS3 architecture
- **64-bit Host Compatibility**: Works on 32/64-bit hosts
- **NUMA-aware**: Thread-local locking for scalability
- **Reservation-based Atomics**: Matches PowerPC LL/SC model

## Future Improvements

1. Reduce lock contention in high-concurrency scenarios
2. Improve RTM transaction length detection
3. Optimize page protection change performance
4. Better memory fragmentation handling

---

**Last Updated**: 2025-11-17
**Coverage**: All 7 files in Memory module (vm.h, vm.cpp, vm_ptr.h, vm_ref.h, vm_var.h, vm_locking.h, vm_reservation.h)
