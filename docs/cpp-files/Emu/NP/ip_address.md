# ip_address.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/ip_address.h`
- **Type**: Header File
- **Lines**: 87

## Description
C++ Source/Header File

## Includes
- `array`
- `unordered_map`
- `flatbuffers/vector.h`
- `util/types.hpp`
- `Utilities/mutex.h`
- `winsock2.h`
- `WS2tcpip.h`
- `sys/socket.h`
- `netinet/in.h`
- `netdb.h`

## Namespaces
- `np`

## Classes & Structures
### ip_address_translator
```cpp
er(byte) + 0x9e3779b9 + (hash << 6) + (hash >> 2); } return hash; } }; namespace
```

### IPV6_SUPPORT
```cpp
6>> ipv4_to_ipv6; }; u32 register_ip(const flatbuffers::Vector<std::uint8_t>* ve
```

### std
```cpp
#ifdef _WIN32 using socket_type = uptr; #else using socket_type = int; #endif te
```


## Enumerations
- `IPV6_SUPPORT`

## Key Functions
- `is_ipv6()`
- `is_ipv6_supported()`
- `set_socket_non_blocking()`
- `register_ipv6()`
- `register_ip()`
- `close_socket()`
- `operator()`
- `sendto_possibly_ipv6()`
