# vport0.h

## File Information
- **Location**: `/home/user/rpcs3/rpcs3/Emu/NP/vport0.h`
- **Type**: Header File
- **Lines**: 28

## Description
VPort 0 is invalid for sys_net so we use it for:

## Includes
- `vector`
- `winsock2.h`
- `netinet/in.h`
- `Emu/Cell/lv2/sys_net/nt_p2p_port.h`

## Enumerations
- `VPORT_0_SUBSET`

## Key Functions
- `send_packet_from_p2p_port_ipv4()`
- `send_packet_from_p2p_port_ipv6()`
