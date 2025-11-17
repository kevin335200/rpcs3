# rpcn_client.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/rpcn_client.h`
- **Type**: Header File
- **Lines**: 471

## Description
C++ Source/Header File

## Includes
- `unordered_map`
- `chrono`
- `thread`
- `semaphore`
- `Utilities/mutex.h`
- `Emu/localized_string_id.h`
- `winsock2.h`
- `ws2tcpip.h`
- `sys/socket.h`
- `netinet/in.h`
- `arpa/inet.h`
- `Emu/Cell/Modules/sceNp.h`
- `Emu/Cell/Modules/sceNp2.h`
- `Emu/Cell/Modules/sceNpTus.h`
- `flatbuffers/flatbuffers.h`
- ... and 2 more

## Namespaces
- `rpcn`

## Classes & Structures
### rpcn_client
```cpp
cn::rpcn_state state); void print_error(rpcn::CommandType command, rpcn::ErrorTy
```

### vec_stream
```cpp
ID_SIZE = COMMUNICATION_ID_COMID_COMPONENT_SIZE + COMMUNICATION_ID_SUBID_COMPONE
```

### friend_data
```cpp
r_title; std::string pr_status; std::string pr_comment; std::vector<u8> pr_data;
```

### recvn_result
```cpp
nput(); bool handle_output(); void add_packet(std::vector<u8> packet); private: 
```

### message_cb_t
```cpp
riend_online_data> presence_updates; // npid / presence data // Messages struct 
```

### friend_online_data
```cpp
(void* param, const shared_ptr<std::pair<std::string, message_data>> new_msg, u6
```


## Enumerations
- `recvn_result`

## Key Functions
- `get_room_list_gui()`
- `handle_friend_notification()`
- `tus_get_multiuser_variable()`
- `tus_delete_multislot_data()`
- `leave_room_gui()`
- `set_room_info_gui()`
- `get_roomdata_external_list()`
- `handle_input()`
- `leave_room()`
- `send_packet()`
- `ping_room_owner()`
- `get_string()`
- `update_local_addr()`
- `tus_delete_multislot_variable()`
- `tus_add_and_get_variable()`
