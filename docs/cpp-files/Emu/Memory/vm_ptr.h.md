# vm_ptr.h - Virtual Memory Pointers

## Overview
Provides template classes for safely handling pointers in PS3 virtual memory space. Enables transparent conversion between host pointers and 32-bit PS3 addresses with proper type safety and endianness handling.

## Core Class: _ptr_base

### Purpose
Generic pointer wrapper that stores a PS3 address instead of host pointer. Supports automatic conversion, arithmetic operations, and type-safe access.

### Template Parameters
- `T`: Pointed-to type (cannot be pointer or reference)
- `AT`: Address type (usually u32 or BE u32)

### Key Features

#### Constructors
```cpp
_ptr_base() = default;              // Null pointer
_ptr_base(vm::addr_t addr);         // From address
static _ptr_base make(addr_type);   // Static factory
```

#### Address Access
```cpp
addr_type addr() const;     // Get stored address
void set(addr_type addr);   // Set address
explicit operator bool();   // Check if null
```

#### Pointer-like Operations
```cpp
T& operator*() const;                    // Dereference
T* operator->() const;                   // Member access
T& operator[](u32 index) const;         // Array indexing
_ptr_base operator+(u32 count) const;   // Pointer arithmetic
_ptr_base operator-(u32 count) const;   // Reverse arithmetic
s32 operator-(const _ptr_base& right);  // Pointer difference

_ptr_base& operator++();    // Pre-increment
_ptr_base operator++(int);  // Post-increment
_ptr_base& operator--();    // Pre-decrement
_ptr_base operator--(int);  // Post-decrement

_ptr_base& operator+=(s32 count);
_ptr_base& operator-=(s32 count);
```

#### Struct Member Access
```cpp
template <typename MT, typename T2> requires PtrComparable<T, T2>
_ptr_base<MT, u32> ptr(MT T2::*const mptr) const;

template <typename MT, typename T2> requires PtrComparable<T, T2>
_ptr_base<MT, u32> ptr(MT T2::*const mptr, u32 index) const;

template <typename MT, typename T2> requires PtrComparable<T, T2>
_ref_base<MT, u32> ref(MT T2::*const mptr) const;

template <typename MT, typename T2> requires PtrComparable<T, T2>
_ref_base<MT, u32> ref(MT T2::*const mptr, u32 index) const;
```

#### Type Conversion
```cpp
T* get_ptr<bool Strict = false>() const;  // Get host pointer
operator _ptr_base<T2, AT2>() const;      // Convert to compatible type

// Reference conversion
_ref_base<T, u32> ref() const;
```

#### Alignment and Size
```cpp
bool aligned(u32 align = alignof(T)) const;  // Test alignment
static constexpr u32 size() noexcept;        // Type size
static constexpr u32 align() noexcept;       // Type alignment
```

#### Safe Memory Access
```cpp
std::pair<bool, T> try_read() const;    // Try read with validity check
bool try_read(T& out) const;            // Try read to reference
bool try_write(const T& in) const;      // Try write with protection check
```

### Function Pointer Specialization

```cpp
template<typename AT, typename RT, typename... T>
class _ptr_base<RT(T...), AT>
{
    // Function pointer wrapper
    RT operator()(ppu_thread& ppu, T... args) const;
    const ppu_func_opd_t& opd() const;
};
```

## Pointer Type Aliases

### Endianness-aware Pointers
```cpp
// Native endianness pointer to LE data
template<typename T, typename AT = u32> using ptrl = _ptr_base<to_le_t<T>, AT>;
template<typename T, typename AT = u32> using cptrl = ptrl<const T, AT>;

// Native endianness pointer to BE data
template<typename T, typename AT = u32> using ptrb = _ptr_base<to_be_t<T>, AT>;
template<typename T, typename AT = u32> using cptrb = ptrb<const T, AT>;

// BE pointer to LE data
template<typename T, typename AT = u32> using bptrl = _ptr_base<to_le_t<T>, to_be_t<AT>>;

// BE pointer to BE data
template<typename T, typename AT = u32> using bptrb = _ptr_base<to_be_t<T>, to_be_t<AT>>;

// LE pointer to LE data
template<typename T, typename AT = u32> using lptrl = _ptr_base<to_le_t<T>, to_le_t<AT>>;

// LE pointer to BE data
template<typename T, typename AT = u32> using lptrb = _ptr_base<to_be_t<T>, to_le_t<AT>>;
```

### PS3-specific Aliases (in ps3_ namespace)
```cpp
// Default pointer type for PS3 HLE functions
template<typename T, typename AT = u32> using ptr = ptrb<T, AT>;
template<typename T, typename AT = u32> using cptr = ptr<const T, AT>;

// Pointer to pointer
template<typename T, typename AT = u32, typename AT2 = u32> using pptr = ptr<ptr<T, AT2>, AT>;
template<typename T, typename AT = u32, typename AT2 = u32> using cpptr = pptr<const T, AT, AT2>;

// BE pointer types (for PS3 structures)
template<typename T, typename AT = u32> using bptr = bptrb<T, AT>;
template<typename T, typename AT = u32> using bcptr = bptr<const T, AT>;

// BE pointer to pointer
template<typename T, typename AT = u32, typename AT2 = u32> using bpptr = bptr<ptr<T, AT2>, AT>;
template<typename T, typename AT = u32, typename AT2 = u32> using bcpptr = bpptr<const T, AT, AT2>;
```

## Pointer Casting Functions

```cpp
// Static cast between compatible pointer types
template <typename CT, typename T, typename AT>
inline _ptr_base<to_be_t<CT>, u32> static_ptr_cast(const _ptr_base<T, AT>& other);

// Const cast
template <typename CT, typename T, typename AT>
inline _ptr_base<to_be_t<CT>, u32> const_ptr_cast(const _ptr_base<T, AT>& other);

// Reinterpret cast
template <typename CT, typename T, typename AT>
inline _ptr_base<to_be_t<CT>, u32> unsafe_ptr_cast(const _ptr_base<T, AT>& other);
```

## Comparison Operators

```cpp
template<typename T1, typename T2, typename AT1, typename AT2> requires PtrComparable<T1, T2>
bool operator==(const _ptr_base<T1, AT1>& left, const _ptr_base<T2, AT2>& right);

template<typename T1, typename T2, typename AT1, typename AT2> requires PtrComparable<T1, T2>
bool operator<(const _ptr_base<T1, AT1>& left, const _ptr_base<T2, AT2>& right);

template<typename T1, typename T2, typename AT1, typename AT2> requires PtrComparable<T1, T2>
bool operator<=(const _ptr_base<T1, AT1>& left, const _ptr_base<T2, AT2>& right);

template<typename T1, typename T2, typename AT1, typename AT2> requires PtrComparable<T1, T2>
bool operator>(const _ptr_base<T1, AT1>& left, const _ptr_base<T2, AT2>& right);

template<typename T1, typename T2, typename AT1, typename AT2> requires PtrComparable<T1, T2>
bool operator>=(const _ptr_base<T1, AT1>& left, const _ptr_base<T2, AT2>& right);
```

## null_t Null Pointer

```cpp
struct null_t {
    template<typename T, typename AT>
    operator _ptr_base<T, AT>() const;

    template<typename T, typename AT>
    constexpr bool operator==(const _ptr_base<T, AT>& ptr) const;

    template<typename T, typename AT>
    constexpr bool operator<(const _ptr_base<T, AT>& ptr) const;
};

constexpr null_t null{};  // Global null pointer
```

## Formatting Support

The file provides fmt support for:
- `vm::_ptr_base<const void, u32>`: Generic pointer formatting
- `vm::_ptr_base<char, u32>`: String pointer formatting (shows the actual string)
- Char array specializations

## Important Design Decisions

1. **Address Type Parameter**: Allows different endianness for the address itself
2. **Type Safety**: Concepts prevent invalid conversions
3. **Endianness Handling**: Automatic conversion through `to_be_t`/`to_le_t`
4. **Memory Protection**: `try_read()`/`try_write()` validate access
5. **Struct Member Access**: Member pointers supported via pointer arithmetic
6. **Serialization**: Bitwise serialization enabled for persistence

## Usage Examples

### Basic Pointer Usage
```cpp
vm::ptr<u32> addr{0x10000};      // Pointer to BE u32 at 0x10000
u32 val = *addr;                  // Dereference
*addr = 0x12345678;               // Write
addr++;                            // Arithmetic
```

### Struct Member Access
```cpp
struct MyStruct { u32 field1; u16 field2; };
vm::ptr<MyStruct> obj{0x20000};
vm::ptr<u32> field = obj.ptr(&MyStruct::field1);
```

### Safe Access
```cpp
auto [ok, val] = addr.try_read();
if (ok) { /* use val */ }
```

## Type Safety

The `PtrComparable` concept ensures:
- Only comparisons between compatible types are allowed
- Prevents comparing pointers to incompatible types
- Compiler enforces at template instantiation
