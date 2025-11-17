# signaling_handler.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/signaling_handler.h`
- **Type**: Header File
- **Lines**: 147

## Description
User seen from that peer

## Includes
- `Emu/Cell/Modules/sceNp.h`
- `Emu/Cell/Modules/sceNp2.h`
- `Utilities/Thread.h`
- `Utilities/mutex.h`
- `unordered_map`
- `chrono`
- `optional`

## Classes & Structures
### signaling_packet
```cpp
32>('G') << 8 | static_cast<u32>('N')); static constexpr le_t<u32> SIGNALING_VER
```

### queued_packet
```cpp
gnalingCommand> command; le_t<u32> sent_addr; le_t<u16> sent_port; SceNpId npid;
```

### signaling_info
```cpp
#include "Utilities/mutex.h" #include <unordered_map> #include <chrono> #include
```

### signaling_handler
```cpp
ignal_connect_ack, signal_confirm, signal_finished, signal_finished_ack, signal_
```


## Enumerations
- `SignalingCommand`

## Key Functions
- `send_signaling_packet()`
- `update_si_status()`
- `signal_ext_sig_callback()`
- `add_match2_ctx()`
- `update_si_mapped_addr()`
- `remove_sig_ctx()`
- `set_self_sig_info()`
- `get_always_conn_id()`
- `signal_sig_callback()`
- `retire_all_packets()`
- `process_incoming_messages()`
- `update_ext_si_status()`
- `get_micro_timestamp()`
- `stop_sig()`
- `clear_sig_ctx()`
