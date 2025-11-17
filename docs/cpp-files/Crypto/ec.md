# Elliptic Curve Cryptography (ECC)

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/ec.h, ec.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

椭圆曲线密码学实现，用于 ECDSA 签名验证。提供：
- 椭圆曲线参数设置
- 公钥/私钥配置
- ECDSA 签名验证

## 📋 主要内容

### 函数列表

```cpp
void ecdsa_set_curve(const u8* p, const u8* a, const u8* b,
                     const u8* N, const u8* Gx, const u8* Gy);
void ecdsa_set_pub(const u8* Q);
void ecdsa_set_priv(const u8* k);
bool ecdsa_verify(const u8* hash, u8* R, u8* S);
```

### 曲线参数

- **p**: 曲线定义的素数
- **a, b**: 曲线方程系数 (y^2 = x^3 + ax + b)
- **N**: 基点的阶
- **Gx, Gy**: 生成点坐标
- **Q**: 公钥点
- **k**: 私钥

## 💻 代码分析

ECDSA 验证过程：
1. 验证签名向量 (R, S) 有效性
2. 计算 w = S^(-1) mod N
3. 计算 u1 = hash*w mod N, u2 = R*w mod N
4. 计算点 (x,y) = u1*G + u2*Q
5. 验证 R == x mod N

## 用途

RPCS3 中用于：
- SELF 可执行文件 ECDSA 签名验证
- 系统固件验证
- 内容真实性检查

## 学习要点

- Weierstrass 曲线形式
- 有限域运算
- ECDSA 签名算法
- 点倍增和点加算法
