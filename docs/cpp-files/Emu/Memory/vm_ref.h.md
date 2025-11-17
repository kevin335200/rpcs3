# vm_ref.h - Virtual Memory References

## Overview
Provides reference wrapper class for PS3 virtual memory objects. References provide value-semantic access to data stored in PS3 memory space with automatic endianness conversion.

## Core Class: _ref_base

### Purpose
Reference wrapper storing a PS3 address and providing transparent access to the referenced object. Similar to C++ references but backed by virtual memory address.

### Template Parameters
- `T`: Referenced type (cannot be pointer, reference, function, or void)
- `AT`: Address type (usually u32 or BE u32)

### Constructor and Address Access
```cpp
_ref_base(const _ref_base&) = default;  // Copy constructor (allowed)
_ref_base(vm::addr_t addr);             // From address

addr_type addr() const;                 // Get stored address
```

### Dereferencing
```cpp
T& get_ref() const;                     // Get reference to data
operator std::common_type_t<T>() const; // Implicit conversion
operator T&() const;                    // Reference conversion
```

### Assignment Operations
```cpp
T& operator=(const _ref_base& right);
T& operator=(const std::common_type_t<T>& right) const;
```

### Pointer Conversion
```cpp
vm::_ptr_base<T, u32> ptr() const;  // Convert reference to pointer
```

## Arithmetic Operations

### Increment/Decrement
```cpp
decltype(auto) operator++(int) const;   // Post-increment
decltype(auto) operator++() const;      // Pre-increment
decltype(auto) operator--(int) const;   // Post-decrement
decltype(auto) operator--() const;      // Pre-decrement
```

### Compound Assignment
```cpp
template<typename T2>
decltype(auto) operator+=(const T2& right);

template<typename T2>
decltype(auto) operator-=(const T2& right);

template<typename T2>
decltype(auto) operator*=(const T2& right);

template<typename T2>
decltype(auto) operator/=(const T2& right);

template<typename T2>
decltype(auto) operator%=(const T2& right);

template<typename T2>
decltype(auto) operator&=(const T2& right);

template<typename T2>
decltype(auto) operator|=(const T2& right);

template<typename T2>
decltype(auto) operator^=(const T2& right);

template<typename T2>
decltype(auto) operator<<=(const T2& right);

template<typename T2>
decltype(auto) operator>>=(const T2& right);
```

## Reference Type Aliases

### Endianness-aware References
```cpp
// Native endianness reference to LE data
template<typename T, typename AT = u32> using refl = _ref_base<to_le_t<T>, AT>;

// Native endianness reference to BE data
template<typename T, typename AT = u32> using refb = _ref_base<to_be_t<T>, AT>;

// BE reference to LE data
template<typename T, typename AT = u32> using brefl = _ref_base<to_le_t<T>, to_be_t<AT>>;

// BE reference to BE data
template<typename T, typename AT = u32> using brefb = _ref_base<to_be_t<T>, to_be_t<AT>>;

// LE reference to LE data
template<typename T, typename AT = u32> using lrefl = _ref_base<to_le_t<T>, to_le_t<AT>>;

// LE reference to BE data
template<typename T, typename AT = u32> using lrefb = _ref_base<to_be_t<T>, to_le_t<AT>>;
```

### PS3-specific Aliases (in ps3_ namespace)
```cpp
// Default reference for PS3 HLE functions
template<typename T, typename AT = u32> using ref = refb<T, AT>;

// Default reference for PS3 structures (BE reference to BE data)
template<typename T, typename AT = u32> using bref = brefb<T, AT>;
```

## Key Design Characteristics

### Value Semantics
- References behave like values
- Assignment copies the data
- Pass-by-reference is transparent
- No reference binding semantics

### Endianness Handling
- Automatic conversion via `to_be_t<T>`
- Works with integer types, structs, arrays
- Bit-level operations on BE data

### Address Independence
- References can be copied freely
- Each copy maintains address
- No aliasing issues like C++ references

### Read-Write Access
- Full access to referenced data
- Can modify through assignment
- Operator overloads forward to referenced data

## Usage Examples

### Basic Reference Usage
```cpp
struct PSConfig {
    be_t<u32> magic;
    be_t<u16> version;
};

vm::ref<PSConfig> config{0x10000};
config.ref().magic = 0x12345678;  // Modify via reference
u32 ver = config.ref().version;   // Read via reference

// Or using implicit conversion
PSConfig copy = config;  // Implicit conversion operator
```

### Arithmetic on References
```cpp
vm::ref<u32> counter{0x20000};
counter++;           // Increment value
counter += 10;       // Add 10
counter -= 5;        // Subtract 5
*counter *= 2;       // Multiply reference value

// Using operators directly
++counter;           // Pre-increment
```

### Pointer Conversion
```cpp
vm::ref<u32> ref{0x30000};
auto ptr = ref.ptr();  // Convert to pointer
*ptr = 42;             // Same effect
```

## Formatting Restrictions

References cannot be formatted directly:
```cpp
// This will cause a compile-time error
fmt::print("{}", ref);  // Error: ambiguous format argument
```

Use `.ptr()` or `.get_ref()` to get formattable representations:
```cpp
fmt::print("{}", ref.ptr());       // Format as pointer
fmt::print("{}", (T)ref);          // Format as value
```

## Endianness Conversion

### Example: BE Structure in Memory
```cpp
struct NetworkPacket {
    be_t<u16> length;
    be_t<u32> sequence;
};

// Access big-endian packet at address 0x10000
vm::ref<NetworkPacket> packet{0x10000};
u32 seq = (u32)packet.ref().sequence;  // Automatic BE->native conversion
```

### Example: Mixed Endianness
```cpp
// Reference to little-endian data
vm::refl<u32> le_value{0x20000};
// le_value automatically converts LE to native endianness
```

## Thread Safety

References are **not** thread-safe:
- No synchronization primitives
- Suitable for single-threaded access
- For shared data, use `vm::ptr` with `try_read`/`try_write`

## Memory Safety

### Address Validation
- No validation of address validity
- Dereferencing invalid address causes crash/undefined behavior
- Use `vm::ptr::try_read()` for safe access

### Object Lifetime
- Reference doesn't manage object lifetime
- Referenced data must remain valid
- No automatic cleanup

## Differences from C++ References

| Feature | C++ Reference | vm::_ref_base |
|---------|---------------|---------------|
| Rebinding | Not allowed | Allowed |
| Nullability | None | Can be "null" (addr 0) |
| Assignment | Rebinds? | Copies value |
| Address | Stack/heap | 32-bit virtual |
| Copying | Not allowed | Allowed |
| Lifetime | Bound to object | Independent |

## Type Conversions

References support implicit conversions through `operator T()` and `operator T&()`:
```cpp
vm::ref<u32> ref{0x10000};
u32 val = ref;          // Implicit conversion to value
u32& rref = ref;        // Implicit conversion to reference
```

## Debugging and Inspection

### Get Raw Address
```cpp
vm::ref<u32> ref{0x10000};
u32 address = ref.addr();  // Get 32-bit address
```

### Get Actual Reference
```cpp
T& actual_ref = ref.get_ref();  // Get actual C++ reference
```

## Performance Considerations

- Lightweight wrapper (just stores address)
- Dereference involves memory access at address
- No caching of values
- Each operation may trigger memory access

## Common Patterns

### Array Access via References
```cpp
vm::ref<u32[]> array{0x10000};
for (size_t i = 0; i < count; i++) {
    u32 element = *(vm::ref<u32>{0x10000 + i * 4});
}
```

### Structure Field References
```cpp
struct Data { u32 field; };
vm::ref<Data> data{0x10000};
vm::ref<u32> field = {data.addr() + offsetof(Data, field)};
```

### Callback Parameter References
```cpp
void process(vm::ref<DataStruct>& param) {
    // param is a reference to PS3 data
    // Use like normal C++ reference
}
```

## Notes

- References are preferable to pointers for value semantics
- Use pointers when address manipulation needed
- Endianness handling is transparent
- Perfect for HLE function parameters
