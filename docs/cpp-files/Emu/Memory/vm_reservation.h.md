# vm_reservation.h - Virtual Memory Reservations and Atomic Operations

## Overview
Implements PS3's Load-Linked/Store-Conditional (LL/SC) style reservation system with transactional memory (RTM) optimizations on x86-64. Enables atomic operations on memory-mapped data with lock-free synchronization when possible.

## Enumerations

### Reservation Lock Masks
```cpp
enum : u64 {
    rsrv_lock_mask = 127,       // Lower 7 bits used for synchronization
    rsrv_unique_lock = 64,      // Exclusive lock bit
    rsrv_putunc_flag = 32,      // Atomic put-unconditional flag
};
```

**Field Meanings:**
- `rsrv_lock_mask`: Synchronization bits for lock/update count
- `rsrv_unique_lock`: Exclusive lock indicator (bit 6)
- `rsrv_putunc_flag`: Flag for unconditional stores (bit 5)

## Global Arrays

```cpp
extern std::array<atomic_t<reservation_waiter_t>, ...> g_resrv_waiters_count;
extern u8 g_reservations[65536 / 128 * 64];  // Reservation state array
```

**Layout:**
- 64-bit entries aligned every 128 bytes
- Each 128-byte region has one reservation entry
- Maximum 65536 simultaneous reservations

## Structures

### reservation_waiter_t
```cpp
struct reservation_waiter_t {
    u32 wait_flag;      // Odd = waiting, even = not waiting
    u32 waiters_count;  // Number of threads waiting
};
```

**Purpose:** Track waiters for notification on reservation updates
**wait_flag:** Parity used for notification deduplication

## Core Functions

### Reservation Acquisition

#### reservation_acquire()
```cpp
inline atomic_t<u64>& reservation_acquire(u32 addr)
```
**Purpose:** Get reservation state for address
**Returns:** Reference to reservation atomic
**Details:**
- Calculates reservation location from address
- Uses (addr & 0xff80) / 2 for indexing
- Provides atomic access to reservation

#### try_reservation_update()
```cpp
std::pair<bool, u64> try_reservation_update(u32 addr)
```
**Purpose:** Atomically update reservation timestamp
**Returns:**
- bool: Success/failure
- u64: Current reservation time
**Behavior:**
- Fails if unique lock held
- Increments timestamp by 128 on success
- Non-blocking

#### reservation_update()
```cpp
void reservation_update(u32 addr)
```
**Purpose:** Update reservation with notifications
**Blocking:** Retries until successful
**Side Effects:**
- Notifies waiting threads
- Updates CPU state for waits
- May check CPU stopped condition

### Locking Functions

#### reservation_try_lock()
```cpp
inline bool reservation_try_lock(atomic_t<u64>& res, u64 rtime)
```
**Purpose:** Try to acquire exclusive reservation lock
**Parameters:**
- `res`: Reservation atomic reference
- `rtime`: Current reservation timestamp
**Returns:** true if locked, false if failed
**Implementation:** Single CAS operation

#### reservation_lock()
```cpp
inline std::pair<atomic_t<u64>&, u64> reservation_lock(u32 addr)
```
**Purpose:** Lock reservation for exclusive access
**Returns:**
- Reference to reservation atomic
- Timestamp for lock tracking
**Behavior:**
- Fast path: Try immediate lock
- Slow path: Call `reservation_lock_internal()` on failure
- Returns no_lock on memory error

#### reservation_lock_internal()
```cpp
u64 reservation_lock_internal(u32 addr, atomic_t<u64>& res)
```
**Purpose:** Lock with heavy-weight fallback
**Returns:** Timestamp (umax on memory error)
**Behavior:**
- Busy-wait with exponential backoff
- Yields after 15 iterations
- Checks CPU state for pauses

#### reservation_shared_lock_internal()
```cpp
void reservation_shared_lock_internal(atomic_t<u64>& res)
```
**Purpose:** Acquire shared (reader) lock
**Semantics:** Multiple readers, mutual exclusion with writers
**Implementation:** Increment counter, prevent unique lock

### Notification System

#### reservation_notifier()
```cpp
static inline atomic_t<reservation_waiter_t>* reservation_notifier(u32 raddr, u64 rtime)
```
**Purpose:** Find waiter notification slot for address
**Parameters:**
- `raddr`: Reservation address
- `rtime`: Reservation timestamp
**Returns:** Pointer to waiter tracking structure
**Optimization:**
- Uses address bit patterns to distribute waiters
- 64 slots per address/time combination
- Efficient bit manipulation

#### reservation_notifier_count()
```cpp
static inline u32 reservation_notifier_count(u32 raddr, u64 rtime)
```
**Purpose:** Get number of waiters
**Returns:** Count from waiter structure

#### reservation_notifier_begin_wait()
```cpp
static inline std::pair<atomic_t<reservation_waiter_t>*, u32>
reservation_notifier_begin_wait(u32 raddr, u64 rtime)
```
**Purpose:** Register thread as waiter
**Returns:**
- Pointer to waiter structure
- Current wait flag
**Effects:** Increments waiter count

#### reservation_notifier_end_wait()
```cpp
static inline void reservation_notifier_end_wait(atomic_t<reservation_waiter_t>& waiter)
```
**Purpose:** Unregister thread as waiter
**Effects:**
- Decrements waiter count
- Clears wait flag on last waiter

#### reservation_notifier_notify()
```cpp
atomic_t<u32>* reservation_notifier_notify(u32 raddr, u64 rtime, bool postpone = false)
```
**Purpose:** Notify waiting threads
**Parameters:**
- `raddr`: Reservation address
- `rtime`: Reservation timestamp
- `postpone`: Delay actual notification
**Returns:** Pointer for deferred notification (if postponed)
**Behavior:**
- Toggles wait flag from odd to even
- Calls notify_all() on condition variable
- Enables postponement for optimization

## Main API: Atomic Operations

### reservation_op()
```cpp
template <bool Ack = false, typename CPU, typename T, typename AT = u32, typename F>
inline SAFE_BUFFERS(auto) reservation_op(CPU& cpu, _ptr_base<T, AT> ptr, F op)
```

**Purpose:** Execute atomic operation with three-stage fallback

**Requirements:**
- Type size <= 128 bytes
- Type alignment == size
- Type is trivially copyable

**Stages:**

1. **Stage 1: Optimistic RTM** (x86-64 only)
   - Single RTM transaction attempt
   - No other locking
   - Fast success path

2. **Stage 2: Lightened RTM**
   - After Stage 1 fails
   - Pre-lock acquired
   - Multiple transaction attempts
   - Time-bounded

3. **Stage 3: Heavyweight Lock**
   - Suspends all other threads
   - Writer lock acquired
   - Guaranteed success
   - Slowest but safest

**Parameters:**
- `Ack`: Send acknowledgment notifications
- `cpu`: CPU thread performing operation
- `ptr`: Pointer to data
- `op`: Lambda/function returning bool or void

**Lambda Semantics:**
```cpp
// Returns bool (true = success, false = failed)
bool op(T& data);

// Returns void (always succeeds)
void op(T& data);
```

**Example:**
```cpp
vm::reservation_op<false>(cpu, ptr, [](MyStruct& data) {
    if (data.counter < 100) {
        data.counter++;
        return true;
    }
    return false;
});
```

### peek_op()
```cpp
template <typename CPU, typename T, typename AT = u32, typename F>
inline SAFE_BUFFERS(auto) peek_op(CPU&& cpu, _ptr_base<T, AT> ptr, F op)
```

**Purpose:** Read operation without modification (non-atomic read)
**Semantics:**
- Observes data value
- Verifies no concurrent updates
- Repeats if updates detected
- Non-blocking

**Usage:** Check conditions without locking

### light_op()
```cpp
template <bool Ack = false, typename T, typename F>
inline SAFE_BUFFERS(auto) light_op(T& data, F op)
```

**Purpose:** Lightweight operation on real memory data
**Parameters:**
- `data`: Real memory reference (not VM)
- `op`: Operation function
**Returns:** Operation result

**Behavior:**
- Works on actual host memory
- Uses reservation acquire for index
- Shared lock if not held
- Suitable for native data structures

### atomic_op()
```cpp
template <bool Ack = false, typename T, typename F>
inline SAFE_BUFFERS(auto) atomic_op(T& data, F op)
```

**Purpose:** Atomic operation on data with built-in atomic_op method
**Implementation:** Wrapper around `light_op()`

### fetch_op()
```cpp
template <bool Ack = false, typename T, typename F>
inline SAFE_BUFFERS(auto) fetch_op(T& data, F op)
```

**Purpose:** Fetch-modify operation on atomic data
**Implementation:** Wrapper around `light_op()`

## Reservation Escape

### reservation_escape_internal()
```cpp
[[noreturn]] void reservation_escape_internal()
```

**Purpose:** Emergency exit from reservation deadlock
**Behavior:**
- SPU: Uses spu_runtime::g_escape()
- PPU: TODO (not implemented)
- Generic: thread_ctrl::emergency_exit()

**Usage:** Called when CPU stopped during reservation

## RTM Integration (x86-64)

### RTM Status Codes
```cpp
_xbegin();   // Start transaction, returns status
_xend();     // End transaction
```

**Status Values:**
- `0xFFFFFFFF` (umax): Transaction succeeded
- Other values: Failure code with reason bits

### Transaction Benefits
- **Speed**: No locks in success case
- **Concurrency**: Multiple readers
- **Automatic**: Hardware handles synchronization

### Transaction Limitations
- **Capacity**: Limited transaction size
- **Conflicts**: Retry on shared data access
- **Time-bound**: g_rtm_tx_limit2 controls duration

## Performance Characteristics

**Best Case (Optimistic RTM):**
- Single transaction attempt
- Minimal latency
- No thread synchronization

**Good Case (Lightened RTM):**
- Partial lock + transactions
- Multiple attempts possible
- Improved concurrency vs heavyweight

**Fallback (Heavyweight):**
- Suspends all threads
- Guaranteed progress
- Highest latency, maximum isolation

## Memory Ordering Guarantees

**Acquire-Release Semantics:**
- Successful op: Release semantics
- Failed op: Acquire semantics
- Notification: Full synchronization

## Integration with Memory System

**Reservation Tracking:**
- One reservation per 128-byte block
- Address range [addr, addr+127] shares reservation
- Timestamp increments on update

**CPU State Interaction:**
- Integrates with `cpu_flag::wait`
- Respects `cpu_flag::stopped`
- Updates memory synchronization flags

**RSX Notification:**
- Atomic ops may trigger RSX updates
- Reservation changes notify RSX thread
- Prevents graphics coherency issues

## Usage Patterns

### Simple Counter Increment
```cpp
vm::ptr<u32> counter{0x10000};
vm::reservation_op<true>(cpu, counter, [](u32& value) {
    value++;
});
```

### Conditional Update
```cpp
vm::ptr<MyData> data{0x20000};
bool updated = vm::reservation_op(cpu, data, [](MyData& d) {
    if (d.ready) {
        d.value = 42;
        return true;
    }
    return false;
});
```

### No-wait Peek
```cpp
vm::peek_op(cpu, ptr, [](const MyData& d) {
    if (d.magic != 0x12345678) {
        // Handle invalid data
    }
});
```

## Debugging

**Breakpoint Support:**
- Works with memory breakpoints
- Pauses on atomic operation boundaries
- Shows detailed lock state

**Logging:**
- Performance meter: "SUSPEND", "RHW_LOCK"
- Memory debug output
- CPU state tracking

## Notes

- Reservations are 128-byte aligned blocks
- Timestamps use 64-bit counters
- Waiter notification is probabilistic for performance
- RTM fallback is transparent to application
- Lock-free when possible, locks when necessary
