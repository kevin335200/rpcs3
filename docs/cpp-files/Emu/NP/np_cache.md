# np_cache.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/np_cache.h`
- **Type**: Header File
- **Lines**: 86

## Description
C++ Source/Header File

## Includes
- `map`
- `optional`
- `Utilities/mutex.h`
- `Emu/Cell/Modules/sceNp.h`
- `Emu/Cell/Modules/sceNp2.h`

## Namespaces
- `np`

## Classes & Structures
### room_cache
```cpp
nfo_cache { bool with_password = false; SceNpMatching2SessionPassword password{}
```

### memberbin_cache
```cpp
std::optional<SceNpOnlineName> onlineName; std::optional<SceNpAvatarUrl> avatarU
```

### cache_manager
```cpp
s; std::map<SceNpMatching2RoomMemberId, member_cache> members; bool owner = fals
```

### member_cache
```cpp
n); SceNpMatching2AttributeId id; CellRtcTick updateDate; std::vector<u8> data; 
```

### password_info_cache
```cpp
ching2FlagAttr flagAttr; std::map<SceNpMatching2AttributeId, memberbin_cache> bi
```

### userinfo_cache
```cpp
" #include "Emu/Cell/Modules/sceNp.h" #include "Emu/Cell/Modules/sceNp2.h" names
```


## Key Functions
- `add_member()`
- `update_password()`
- `update()`
- `insert_room()`
- `del_member()`
