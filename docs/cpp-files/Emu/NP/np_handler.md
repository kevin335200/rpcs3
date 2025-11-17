# np_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/np_handler.h`
- **Type**: Header File
- **Lines**: 536

## Description
C++ Source/Header File

## Includes
- `queue`
- `map`
- `unordered_map`
- `Emu/Memory/vm_ptr.h`
- `Emu/Cell/Modules/sceNp.h`
- `Emu/Cell/Modules/sceNp2.h`
- `Emu/Cell/Modules/cellSysutil.h`
- `Emu/NP/rpcn_client.h`
- `Emu/NP/np_allocator.h`
- `Emu/NP/np_cache.h`
- `Emu/NP/np_gui_cache.h`
- `Emu/NP/np_event_data.h`
- `Emu/NP/np_contexts.h`
- `Emu/NP/upnp_handler.h`

## Namespaces
- `np`

## Classes & Structures
### custom_menu_action
```cpp
p_remove_port_mapping(u16 internal_port, std::string_view protocol); // For cust
```

### np_handler
```cpp
p_gui_cache.h" #include "Emu/NP/np_event_data.h" #include "Emu/NP/np_contexts.h"
```

### ticket
```cpp
ST_ID_HIGH : u16 { MISC = 0x3333, SCORE = 0x3334, TUS = 0x3335, GUI = 0x3336, };
```

### basic_event
```cpp
ata; bool parse_success = false; u32 version{}; std::vector<ticket_data> nodes; 
```

### player_history
```cpp
_u64{}; std::vector<u8> data_vec; std::vector<ticket_data> data_nodes; } data; }
```

### gui_notification
```cpp
ing_helper(vec_stream& noti); void notif_room_message_received(vec_stream& noti)
```

### REQUEST_ID_HIGH
```cpp
Info_SIZE = sizeof(SceNpMatchingSearchJoinRoomInfo) + MAX_SceNpMatchingAttr_list
```

### callback_info
```cpp
void handle_TusDataStatusResponse(u32 req_id, rpcn::ErrorType error, vec_stream&
```

### ticket_data
```cpp
ST_ID_HIGH : u16 { MISC = 0x3333, SCORE = 0x3334, TUS = 0x3335, GUI = 0x3336, };
```


## Enumerations
- `REQUEST_ID_HIGH`

## Key Functions
- `reply_record_score_data()`
- `abort_request()`
- `terminate_NP()`
- `tus_get_multiuser_variable()`
- `reply_create_join_room()`
- `reply_set_roomdata_internal()`
- `parse()`
- `tus_delete_multislot_data()`
- `get_req_id()`
- `notif_user_joined_room()`
- `reply_get_score_data()`
- `init_NP()`
- `get_roomdata_external_list()`
- `notif_room_disappeared_gui()`
- `leave_room()`
