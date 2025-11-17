# vm_var.h - Virtual Memory Variables and Allocators

## Overview
Provides RAII wrappers for managing dynamically allocated variables in PS3 virtual memory. Includes allocator templates and variable specializations for both scalar types and arrays.

## Allocator Templates

### page_allocator
Allocates memory from a specific memory location using 0x10000 (64KB) alignment.

```cpp
template <memory_location_t Location = vm::main>
struct page_allocator {
    static inline std::pair<vm::addr_t, u32> alloc(u32 size, u32 align);
    static inline void dealloc(u32 addr, u32 size) noexcept;
};
```

**Features:**
- Ensures minimum 64KB alignment
- Supports custom memory location selection
- Returns both address and size from allocation

### stack_allocator
Allocates from CPU thread stack using stack push/pop operations.

```cpp
template <typename T>
struct stack_allocator {
    static inline std::pair<vm::addr_t, u32> alloc(u32 size, u32 align);
    static inline void dealloc(u32 addr, u32 size) noexcept;
};
```

**Features:**
- Uses thread's stack allocation primitives
- Maintains stack frame semantics
- Requires push/pop pairing

## Core Class: _var_base

### Scalar Variables
```cpp
template <typename T, typename A>
class _var_base final : public _ptr_base<T, const u32>
```

**Features:**
- RAII memory management (allocates in constructor, frees in destructor)
- Unmoveable (move operations deleted)
- Non-copyable (copy operations deleted)
- Inherits from `_ptr_base` for pointer-like interface

**Constructor Variants:**
```cpp
_var_base();                      // Default allocate and default-construct
_var_base(const T& right);        // Allocate and copy-construct
```

**Member Variables:**
- `m_mem_size`: Total allocated memory size

### Array Variables
```cpp
template <typename T, typename A>
class _var_base<T[], A> final : public _ptr_base<T, const u32>
```

**Features:**
- Dynamic array allocation
- Destructor safely deallocates entire array
- STL-compatible iterators
- Count-based access

**Constructor Variants:**
```cpp
_var_base(u32 count);                              // Allocate array
template <typename I>
_var_base(u32 count, I&& it);                     // Initialize from iterator
```

**Key Methods:**
```cpp
u32 get_count() const;      // Get element count
auto begin() const;         // STL iterator
auto end() const;           // STL iterator
T& operator[](u32 index);   // Deleted: use pointer arithmetic
```

**Member Variables:**
- `m_mem_size`: Total allocated memory
- `m_size`: Total data size (count * sizeof(T))

## Type Aliases

### Endianness-aware Variables
```cpp
// LE variable
template <typename T, typename A>
using varl = _var_base<to_le_t<T>, A>;

// BE variable
template <typename T, typename A>
using varb = _var_base<to_be_t<T>, A>;
```

### PS3-specific Aliases (in ps3_ namespace)
```cpp
// Default BE variable with stack allocator
template <typename T, typename A = stack_allocator<ppu_thread>>
using var = varb<T, A>;

// Factory functions
template <typename T, typename A = stack_allocator<ppu_thread>>
[[nodiscard]] auto make_var(const T& value);

template <typename A = stack_allocator<ppu_thread>>
[[nodiscard]] auto make_str(const std::string& str);
```

## Global Variable Class

### gvar
Provides statically-sized global variables with known memory location.

```cpp
template <typename T, uint Count = 1>
struct gvar final : ptr<T> {
    static constexpr u32 alloc_size{sizeof(T) * Count};
    static constexpr u32 alloc_align{std::max<u32>(alignof(T), 16)};
};
```

**Features:**
- Inherits from `ptr<T>` for pointer interface
- Pre-computed allocation size and alignment
- Suitable for static PS3 memory locations
- Can be used with multiple elements

**Example Usage:**
```cpp
struct GlobalData {
    u32 counter;
    u64 timestamp;
};

gvar<GlobalData> g_global_data;  // 16-byte aligned, at fixed location
```

## Helper Functions

### make_var
Factory function for creating initialized variables.

```cpp
template <typename T, typename A = stack_allocator<ppu_thread>>
[[nodiscard]] auto make_var(const T& value)
{
    return varb<T, A>(value);  // Allocate and copy
}
```

**Example:**
```cpp
auto my_var = make_var<u32>(42);  // Allocates, copies 42
```

### make_str
Converts std::string to PS3 char array.

```cpp
template <typename A = stack_allocator<ppu_thread>>
[[nodiscard]] auto make_str(const std::string& str)
{
    return _var_base<char[], A>(size32(str) + 1, str.c_str());
}
```

**Example:**
```cpp
auto ps3_str = make_str("Hello");  // Allocates with null terminator
```

## Lifecycle

### Allocation
1. Constructor calls allocator's `alloc()`
2. Receives address and size
3. Stores both for later deallocation
4. Object becomes usable

### Access
- Use like pointer: `*var`, `var->member`, `var[index]`
- Get address: `var.addr()`
- Pointer operations: `var + 1`, `++var`

### Deallocation
1. Destructor calls allocator's `dealloc()`
2. Passes address and original size
3. Memory is freed
4. Object destroyed

## Memory Safety Features

1. **RAII Pattern**: Automatic cleanup via destructor
2. **No Moves**: Prevents dangling pointers
3. **No Copies**: Prevents aliasing issues
4. **Type Safety**: Endianness conversions explicit
5. **Size Tracking**: Allocator remembers size for cleanup

## Usage Patterns

### Stack-allocated Variable
```cpp
void some_hle_function(ppu_thread& ppu) {
    vm::var<u32> count;         // Allocates on stack
    *count = 10;
    // ... use count ...
}  // Automatically freed when exiting scope
```

### Global Data Structure
```cpp
struct Config {
    be_t<u32> version;
    be_t<u16> flags;
};

gvar<Config> g_config;  // Fixed global location
```

### String Allocation
```cpp
void print_string(ppu_thread& ppu, const std::string& msg) {
    auto ps3_str = make_str(msg);
    // Call PS3 code with ps3_str.addr()
}
```

### Array Allocation
```cpp
vm::var<u32[]> buffer(1024);  // 1024 u32 elements
buffer[0] = 0x12345678;
for (auto it = buffer.begin(); it != buffer.end(); ++it) {
    // Process elements
}
```

## Default Allocators

### Stack Allocator (Default for HLE)
- Uses CPU thread's stack
- Automatic stack frame alignment
- LIFO semantics
- Fast allocation

### Page Allocator
- Uses main memory location
- 64KB alignment
- Suitable for large allocations
- More fragmentation

## Thread Safety

Variables are **not** thread-safe:
- Each CPU thread has its own stack
- Use stack_allocator for thread-local variables
- page_allocator requires manual synchronization for sharing

## Notes

- Variables use const address type (`const u32`) preventing address modification
- Enable bitcopy inheritance disable to prevent shallow copies
- All variables are moveable but use `= delete` to prevent mistakes
- Suitable for PS3 HLE function parameters and local variables
