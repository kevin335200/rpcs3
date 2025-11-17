# Binary Decryption Orchestration

## 📄 文件信息
- **路径**: /home/user/rpcs3/rpcs3/Crypto/decrypt_binaries.h, decrypt_binaries.cpp
- **类型**: 头文件 + 源文件

## 🎯 功能概述

协调多个二进制文件的解密。用于批量处理加密的游戏可执行文件。功能：
- 顺序处理多个文件
- 跟踪进度
- 支持可选的 KLIC（许可证密钥）
- 访问已解密文件

## 📋 主要内容

### 结构体

```cpp
class decrypt_binaries_t {
    std::vector<u128> m_klics;          // KLIC 密钥列表
    std::vector<std::string> m_modules; // 模块路径列表
    usz m_index;                        // 当前索引

public:
    decrypt_binaries_t(std::vector<std::string> modules) noexcept;

    usz decrypt(std::string_view klic_input = {});

    bool done() const {
        return m_index >= m_modules.size();
    }

    const std::string& operator[](usz index) const {
        return ::at32(m_modules, index);
    }
};
```

## 💻 代码分析

### 批量解密流程

```
1. 初始化
   ├─ 接收模块路径列表
   └─ 初始化索引

2. 遍历解密
   ├─ 对每个模块
   │  ├─ 读取文件
   │  ├─ 确定加密类型
   │  ├─ 获取或推导 KLIC
   │  ├─ 调用 SELF/EDAT 解密器
   │  └─ 保存解密文件
   └─ 更新索引

3. 进度跟踪
   ├─ 报告已处理文件数
   ├─ 指示剩余工作
   └─ 支持早期退出

4. 访问解密文件
   └─ 通过操作符[] 获取路径
```

## 🔗 相关文件

- `unself.h` - SELF 解密
- `unedat.h` - EDAT 解密
- `key_vault.h` - 密钥管理
- `utils.h` - 工具函数

## 用途

RPCS3 中用于：
- 批量导入游戏文件
- 启动时初始化二进制文件
- 支持多个加密格式
- 管理解密进度

## 学习要点

- 多文件处理设计
- 状态机流程
- 资源管理
- 模块化架构
