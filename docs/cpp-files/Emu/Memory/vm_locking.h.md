# vm_locking.h - Virtual Memory Locking

## Overview
Provides synchronization primitives for memory access control and range locking. Implements writer locks and passive locking mechanisms to coordinate concurrent memory access between multiple CPU threads.

## Enumerations

### range_lock_flags

Bit flags for memory range locking:

```cpp
enum range_lock_flags : u64 {
    // Access permission flags (bits 61-63, 3 bits total)
    range_writable = 4ull << 61,      // Write permission
    range_readable = 2ull << 61,      // Read permission
    range_reserved = 1ull << 61,      // Reserved flag
    range_full_mask = 7ull << 61,     // All permission bits

    // Special flag combinations
    range_locked = 4ull << 61,        // Exclusively locked (R+W)
    range_allocation = 0,             // Allocation in progress

    range_pos = 61,                   // Bit position
    range_bits = 3,                   // Number of flag bits
};
```

**Flag Meanings:**
- `range_readable`: Allows read operations on locked range
- `range_writable`: Allows write operations on locked range
- `range_locked`: Combination meaning exclusive access
- `range_allocation`: No safe access, shared memory may change

## Global Variables

```cpp
extern atomic_t<u64, 64> g_range_lock_bits[2];  // Allocation bits for locks (2 sets)
extern atomic_t<u64> g_shmem[];                 // Shared memory pointers
extern thread_local atomic_t<cpu_thread*>* g_tls_locked;  // Current lock owner
```

## Core Functions

### Range Lock Management

#### alloc_range_lock()
```cpp
atomic_t<u64, 64>* alloc_range_lock();
```
**Purpose:** Allocate a range lock slot from the pool
**Returns:** Pointer to allocated lock
**Usage:** Typically used internally; one allocation per operation

#### free_range_lock()
```cpp
void free_range_lock(atomic_t<u64, 64>*) noexcept;
```
**Purpose:** Release an allocated range lock
**Parameters:** Lock pointer from `alloc_range_lock()`
**Safety:** Must match corresponding allocation

#### range_lock_internal()
```cpp
void range_lock_internal(atomic_t<u64, 64>* range_lock, u32 begin, u32 size);
```
**Purpose:** Internal lock implementation with waiting
**Parameters:**
- `range_lock`: Lock pointer from `alloc_range_lock()`
- `begin`: Start address of range
- `size`: Size of range to lock
**Details:**
- Waits for conflicting locks
- Triggers page faults if needed
- Suspends conflicting threads
- Uses performance monitoring

#### range_lock()
```cpp
template <uint Size = 0>
FORCE_INLINE void range_lock(atomic_t<u64, 64>* range_lock, u32 begin, u32 _size)
```
**Purpose:** Lock memory range (optimistic path with fallback)
**Features:**
- Optimistic locking attempt
- Checks alignment and page validity
- Falls back to slow path if needed
- Skips locking for local memory (RSX)

### Passive Locking

#### passive_lock()
```cpp
void passive_lock(cpu_thread& cpu);
```
**Purpose:** Register CPU thread for passive waiting
**Usage:** Called when thread needs to wait for memory operations
**Effects:**
- Registers thread lock
- Sets wait flag
- Allows background CPU work

#### passive_unlock()
```cpp
void passive_unlock(cpu_thread& cpu);
```
**Purpose:** Unregister CPU thread from passive waiting
**Usage:** Called when thread resumes
**Effects:**
- Clears lock registration
- Removes memory flag

#### temporary_unlock()
```cpp
bool temporary_unlock(cpu_thread& cpu) noexcept;
void temporary_unlock() noexcept;
```
**Purpose:** Temporarily release lock with state preservation
**Returns:** true if state changed
**Usage:** Allow other threads while maintaining context

## Writer Lock Class

```cpp
struct writer_lock final {
    atomic_t<u64, 64>* range_lock;

    writer_lock(const writer_lock&) = delete;
    writer_lock& operator=(const writer_lock&) = delete;

    writer_lock() noexcept;
    writer_lock(u32 addr, atomic_t<u64, 64>* range_lock = nullptr,
                u32 size = 128, u64 flags = range_locked) noexcept;
    ~writer_lock() noexcept;
};
```

### Purpose
Implements RAII exclusive memory access lock. Constructor acquires, destructor releases.

### Constructors

#### Default Constructor
```cpp
writer_lock() noexcept;
```
**Effect:** Acquires global memory lock (0, nullptr, 1)
**Usage:** Simple global synchronization

#### Parameterized Constructor
```cpp
writer_lock(u32 addr, atomic_t<u64, 64>* range_lock = nullptr,
            u32 size = 128, u64 flags = range_locked) noexcept;
```
**Parameters:**
- `addr`: Starting address to lock
- `range_lock`: Optional pre-allocated range lock
- `size`: Size of range (default 128 bytes)
- `flags`: Lock flags (default exclusive)

**Behavior:**
- If range_lock is null: acquires global lock
- If range_lock provided: uses for range
- Suspends conflicting threads
- Updates CPU memory state flags

### Usage Pattern

```cpp
{
    vm::writer_lock lock(0x10000, nullptr, 4096);
    // Exclusive access to [0x10000, 0x10FFF]
    // All other threads waiting
}
// Lock released when exiting scope
```

## Optimization: range_lock Template

```cpp
template <uint Size = 0>
FORCE_INLINE void range_lock(atomic_t<u64, 64>* range_lock, u32 begin, u32 _size)
```

**Optimization Technique:**
1. **Fast path:** Optimistically store range and check alignment
2. **Medium path:** Check memory protection flags
3. **Slow path:** Full `range_lock_internal()` if needed
4. **Inline assembly:** Tiny barrier on non-MSVC platforms

**Size Template Parameter:**
- `Size = 0`: Runtime size (flexible)
- `Size = 1`: Single-byte (optimized)
- `Size = N`: Fixed N-byte (pre-checked)

## Lock Ordering

Memory locking uses hierarchical ordering:
1. **Global Lock**: Highest level (all memory)
2. **Range Locks**: Per-range (64 concurrent slots)
3. **Passive Locks**: Per-thread (waiters)
4. **Atomic Operations**: Lock-free primitives

## Synchronization Guarantees

**Mutually Exclusive Access:**
- Only one writer lock active per range
- Readers can coexist with proper flags
- Range locks prevent new operations

**Progress Guarantees:**
- Busy-wait with yielding prevents starvation
- Locks eventually released
- No deadlock with proper ordering

## Memory Layout

**Lock Storage:**
- `g_range_lock_bits[0]`: Exclusive range allocation bits
- `g_range_lock_bits[1]`: Shared range allocation bits
- `g_range_lock_set[0..63]`: Storage for 64 range locks

**Lock Entry Format:**
```
Bits 0-31:   Start address
Bits 32-63:  Size (shifted)
Bits 61-63:  Flags (readable/writable/reserved)
```

## Performance Characteristics

- **Contention-free case**: Fast path, minimal overhead
- **Contention case**: Busy-wait/yield, higher latency
- **Lock pool**: 64 concurrent ranges (limit)
- **Memory**: 512 bytes per lock entry

## Thread Safety Properties

**Acquire Semantics:**
- Blocks until all conflicts resolved
- Synchronizes CPU state
- Updates reservation timestamps

**Release Semantics:**
- Visible to all waiting threads
- Clears busy bits
- Allows blocked threads to proceed

## Platform-Specific Notes

### x86-64
- Uses memory barriers in inline assembly
- Respects cache coherency

### ARM/Generic
- Portable atomic operations
- No architecture-specific optimizations

## Integration with Other Systems

**Reservation System:**
- Works with `vm_reservation.h` for atomic ops
- Coordinates with reservation timestamps

**CPU Thread System:**
- Communicates with `cpu_flag` states
- Manages thread suspension

**Range Lock Bits:**
- Tracks active locks globally
- Prevents duplicate range registrations

## Error Handling

**Asserts (Debug):**
- `AUDIT(cpu)`: CPU thread validation
- Range lock validity checks

**Exceptions (Release):**
- "Out of range lock bits": No free lock slots
- "Invalid range lock": Pointer out of bounds

## Usage Patterns

### Simple Global Lock
```cpp
vm::writer_lock lock;  // Acquire global lock
// Protected code
```  // Auto-release

### Range Lock
```cpp
auto range_lock = vm::alloc_range_lock();
try {
    vm::range_lock(range_lock, addr, size);
    // Protected code
} finally {
    vm::free_range_lock(range_lock);
}
```

### Passive Wait
```cpp
cpu->state += cpu_flag::wait;
vm::passive_lock(*cpu);
// CPU can do background work
vm::passive_unlock(*cpu);
```

## Constants

- **Lock Count**: 64 concurrent range locks
- **Min Byte Lock Size**: 1 (single byte)
- **Min Page Lock Size**: 4096 (4KB)
- **Max Continuous Lock**: 512 MB
