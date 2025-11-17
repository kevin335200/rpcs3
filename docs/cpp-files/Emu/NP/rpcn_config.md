# rpcn_config.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/rpcn_config.h`
- **Type**: Header File
- **Lines**: 42

## Description
not const because it can save if npid is requested and it has never been set

## Includes
- `Utilities/Config.h`

## Classes & Structures
### cfg_rpcn
```cpp
#pragma once #include "Utilities/Config.h" struct cfg_rpcn : cfg::node { cfg::ui
```


## Key Functions
- `get_ipv6_support()`
- `set_ipv6_support()`
- `del_host()`
- `load()`
- `get_password()`
- `add_host()`
- `get_path()`
- `generate_npid()`
- `set_hosts()`
- `set_host()`
- `get_npid()`
- `get_host()`
- `set_token()`
- `set_npid()`
- `set_password()`
