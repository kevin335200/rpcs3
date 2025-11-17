# np_contexts.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/np_contexts.h`
- **Type**: Header File
- **Lines**: 316

## Description
Used By Score and Tus

## Includes
- `optional`
- `condition_variable`
- `thread`
- `variant`
- `Utilities/mutex.h`
- `Emu/Memory/vm_ptr.h`
- `Emu/Cell/Modules/sceNp.h`
- `Emu/Cell/Modules/sceNp2.h`
- `Emu/Cell/Modules/sceNpCommerce2.h`
- `Emu/Cell/Modules/sceNpTus.h`
- `Utilities/Thread.h`

## Classes & Structures
### commerce2_ctx
```cpp
ookup_transaction_context(s32 lt_ctx); bool destroy_lookup_transaction_context(s
```

### tdata_record_score_data
```cpp
Info> boardInfo; }; struct tdata_record_score { vm::ptr<SceNpScoreRankNumber> tm
```

### tdata_get_score_data
```cpp
; struct tdata_record_score_data { u32 game_data_size = 0; std::vector<u8> game_
```

### lookup_transaction_ctx
```cpp
cptr<SceNpCommunicationId> communicationId); bool destroy_lookup_title_context(s
```

### score_transaction_ctx
```cpp
vm::cptr<SceNpCommunicationPassphrase> passphrase); bool destroy_score_context(s
```

### tdata_tus_get_data
```cpp
Variable; }; struct tdata_tus_set_data { u32 tus_data_size; std::vector<u8> tus_
```

### tus_transaction_ctx
```cpp
, vm::cptr<SceNpCommunicationPassphrase> passphrase); bool destroy_tus_context(s
```

### tdata_tus_get_datastatus_generic
```cpp
vm::ptr<SceNpTusDataStatus> dataStatus; vm::ptr<void> data; std::vector<u8> tus_
```

### match2_ctx
```cpp
r<score_ctx>& score); bool destroy_score_transaction_context(s32 ctx_id); // Mat
```

### tdata_get_score_generic
```cpp
ize = 0; vm::ptr<void> score_data; u32 game_data_size = 0; std::vector<u8> game_
```

### score_ctx
```cpp
ared_ptr<tus_ctx>& tus); bool destroy_tus_transaction_context(s32 ctx_id); // Sc
```

### tdata_tus_set_data
```cpp
Num; }; struct tdata_tus_get_variable_generic { vm::ptr<SceNpTusVariable> outVar
```

### tdata_invalid
```cpp
eNpCommunicationPassphrase passphrase; u64 timeout; std::thread thread; u32 idm_
```

### generic_async_transaction_context
```cpp
nclude "Emu/Cell/Modules/sceNpTus.h" #include "Utilities/Thread.h" // Used By Sc
```

### tus_ctx
```cpp
status_generic { vm::ptr<SceNpTusDataStatus> statusArray; s32 arrayNum; }; // TU
```


## Key Functions
- `create_lookup_title_context()`
- `create_tus_context()`
- `create_signaling_context()`
- `destroy_signaling_context()`
- `destroy_score_transaction_context()`
- `abort_transaction()`
- `queue_callback()`
- `create_score_transaction_context()`
- `destroy_tus_context()`
- `create_lookup_transaction_context()`
- `create_matching_context()`
- `destroy_lookup_transaction_context()`
- `destroy_lookup_title_context()`
- `destroy_matching_context()`
- `set_result_and_wake()`
