# Key Vault - Cryptographic Key Management

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/key_vault.h, key_vault.cpp
- **类型**: 头文件 + 源文件
- **行数**: 350+ (combined)

## 🎯 功能概述

密钥保管库类，管理 PS3 系统的所有加密密钥：
- SELF 文件加密密钥（LV0/LV1/LV2/APP）
- PKG 文件解密密钥
- NPDRM (Network PlayDRM) 密钥
- 许可证密钥（Klicensee）
- RAP 文件密钥

## 📋 主要内容

### 结构体

```cpp
enum SELF_KEY_TYPE {
    KEY_LV0 = 1,    // Level 0 (最低级)
    KEY_LV1,        // Level 1
    KEY_LV2,        // Level 2
    KEY_APP,        // 应用程序级
    KEY_ISO,        // ISO 镜像
    KEY_LDR,        // 加载器
    KEY_UNK7,       // 未知类型
    KEY_NPDRM       // 网络 PlayDRM
};

struct SELF_KEY {
    u64 version_start;      // 支持的起始版本
    u64 version_end;        // 支持的结束版本
    u16 revision;           // 修订号
    u32 self_type;          // SELF 类型
    u8 erk[0x20];          // 加密根密钥（32 字节）
    u8 riv[0x10];          // 加密初始化向量（16 字节）
    u8 pub[0x28];          // 公钥（40 字节）
    u8 priv[0x15];         // 私钥（21 字节）
    u32 curve_type;         // ECC 曲线类型
};

class KeyVault {
    std::vector<SELF_KEY> sk_LV0_arr;
    std::vector<SELF_KEY> sk_LV1_arr;
    std::vector<SELF_KEY> sk_LV2_arr;
    std::vector<SELF_KEY> sk_APP_arr;
    std::vector<SELF_KEY> sk_ISO_arr;
    std::vector<SELF_KEY> sk_LDR_arr;
    std::vector<SELF_KEY> sk_UNK7_arr;
    std::vector<SELF_KEY> sk_NPDRM_arr;
    u8 klicensee_key[16];   // 许可证密钥
};
```

### 函数列表

```cpp
KeyVault();
SELF_KEY FindSelfKey(u32 type, u16 revision, u64 version);
void SetKlicenseeKey(const u8* key);
const u8* GetKlicenseeKey() const;
```

### 内置密钥常量

#### 系统密钥
```cpp
// SCE ISO 系列密钥
SC_ISO_SERIES_KEY_1[16]
SC_ISO_SERIES_KEY_2[16]

// SC 主密钥
SC_KEY_FOR_MASTER_1[16]
SC_KEY_FOR_MASTER_2[16]
```

#### PKG 密钥
```cpp
PKG_AES_KEY[16]         // PS3 PKG 密钥
PKG_AES_KEY2[16]        // 备用 PS3 PKG 密钥
PKG_AES_KEY_IDU[16]     // IDU 变体

// PS Vita 密钥
PKG_AES_KEY_VITA_1[16]
PKG_AES_KEY_VITA_2[16]
PKG_AES_KEY_VITA_3[16]
```

#### NPDRM 密钥
```cpp
NP_IDPS[16]            // IDPS（设备标识）
NP_KLIC_FREE[16]       // 免费许可证
NP_OMAC_KEY_2[16]      // OMAC 密钥
NP_OMAC_KEY_3[16]
NP_KLIC_KEY[16]        // KLIC 许可证密钥
NP_RIF_KEY[16]         // RIF 文件密钥
```

#### PSP/PSX 密钥
```cpp
NP_PSP_KEY_1[16]       // PSP Minis 密钥
NP_PSP_KEY_2[16]       // PSP 重制版密钥
NP_PSX_KEY[16]         // PSX 兼容密钥
```

#### 授权 ID (PAID)
```
PAID_01-91: 各种系统和应用程序的授权 ID
例如：
PAID_06 = lv2_kernel.self
PAID_43 = bdp_bdmv.self
PAID_71 = psp_emulator.self
```

#### RAP 文件处理
```cpp
RAP_KEY[16]            // RAP 文件解密密钥
RAP_PBOX[16]           // RAP 替换盒
RAP_E1[16]、RAP_E2[16] // RAP 扩展密钥
```

#### EDAT 密钥
```cpp
EDAT_KEY_0[16]，EDAT_KEY_1[16]  // EDAT 加密密钥
EDAT_HASH_0[16]，EDAT_HASH_1[16] // EDAT 哈希密钥
EDAT_IV[16]                       // 初始化向量
```

### 版本相关密钥

```cpp
// SCEPKG 密钥
SCEPKG_ERK[32]         // 加密根密钥
SCEPKG_RIV[16]         // 初始化向量

// PUP（系统更新）
PUP_KEY[64]            // 固件更新密钥

// VSH 曲线参数（椭圆曲线）
VSH_CURVE_P, VSH_CURVE_A, VSH_CURVE_B
VSH_CURVE_N, VSH_CURVE_GX, VSH_CURVE_GY
VSH_PUB[40]            // VSH 公钥
```

## 💻 代码分析

### 密钥查找流程

```cpp
SELF_KEY FindSelfKey(u32 type, u16 revision, u64 version)
{
    // 1. 根据类型选择密钥数组
    // 2. 遍历数组查找匹配的版本/修订号
    // 3. 返回匹配的密钥
    // 4. 优先级：精确版本 > 版本范围 > 默认
}
```

### 关键功能

1. **多个密钥数组**：按 SELF 类型分类
2. **版本范围支持**：处理多个固件版本
3. **快速查找**：O(n) 线性搜索
4. **单 Klicensee 密钥**：整个系统共享

## 🔗 相关文件

- `aes.h` - AES 加密
- `ec.h` - 椭圆曲线
- `unself.h` - SELF 解密
- `unpkg.h` - PKG 处理
- `unedat.h` - EDAT 解密

## 用途

RPCS3 中用于：
- SELF 可执行文件解密
- PKG 游戏包处理
- 许可证认证
- 系统固件验证
- NPDRM 内容解密

## 密钥分类

| 类型 | 目的 | 用途 |
|------|------|------|
| LV0 | 最低级系统 | 固件核心 |
| LV1 | 系统服务 | OS 组件 |
| LV2 | 应用框架 | 应用基础 |
| APP | 应用程序 | 游戏 |
| NPDRM | 网络 DRM | 许可证 |
| ISO | 光盘镜像 | PS2 兼容 |
| LDR | 加载器 | 引导程序 |

## 学习要点

- 密钥分层管理
- 版本相关的密钥控制
- 多种密钥类型的处理
- 硬编码密钥的安全问题
- 授权 ID 系统
