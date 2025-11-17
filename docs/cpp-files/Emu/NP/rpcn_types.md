# rpcn_types.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/rpcn_types.h`
- **Type**: Header File
- **Lines**: 158

## Description
C++ Source/Header File

## Includes
- `util/types.hpp`

## Namespaces
- `rpcn`

## Classes & Structures
### CommandType
```cpp
#pragma once #include "util/types.hpp" namespace rpcn { enum class CommandType :
```

### PacketType
```cpp
e, failure_id_password, failure_id_token, failure_protocol, failure_other, }; en
```

### NotificationType
```cpp
FlagGUI, SetRoomInfoGUI, GetRoomInfoGUI, QuickMatchGUI, SearchJoinRoomGUI, }; en
```

### ErrorType
```cpp
enum class PacketType : u8 { Request, Reply, Notification, ServerInfo, }; enum c
```

### rpcn_state
```cpp
omDisappearedGUI, RoomOwnerChangedGUI, UserKickedGUI, QuickMatchCompleteGUI, }; 
```


## Enumerations
- `CommandType`
- `PacketType`
- `NotificationType`
- `ErrorType`
- `rpcn_state`
