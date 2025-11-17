# objdump.cpp - JIT 代码反汇编注入工具

## 概述
`objdump.cpp` 是一个 Linux perf 分析工具的支持程序，用于对 RPCS3 中 JIT 生成的代码进行反汇编。在性能分析时，允许 Linux perf 工具正确地注释和显示 JIT 编译的代码。

## 文件位置
- `/home/user/rpcs3/objdump.cpp`（根目录）

## 设计目的

### 问题背景
在 Linux 上，perf 工具用于代码分析和性能调试。但是 perf 不能自动反汇编运行时生成的 JIT 代码（RPCS3 的 JIT 编译器生成的 x86-64 代码）。

### 解决方案
通过 perf 的 `--objdump` 选项覆盖，用自定义的 objdump 替代品来处理 RPCS3 的 JIT 代码。

## 工作原理

### 1. 缓存结构
```
~/.cache/rpcs3/ASMJIT/
├── .objects        (索引文件 + 数据)
└── *.o             (缓存的对象文件)
```

**文件说明：**
- `.objects`：包含索引（entry 数组）和实际代码数据
- 索引格式（entry）：
  ```cpp
  struct entry {
      std::uint64_t addr;    // JIT 地址
      std::uint32_t size;    // 代码大小
      std::uint32_t off;     // 数据偏移
  };
  ```

### 2. 处理流程

#### 初始化
```cpp
int fd = open((home + ".objects").c_str(), O_RDONLY);
const auto data = mmap(nullptr, 0x10000'0000, PROT_READ, MAP_SHARED, fd, 0);
const auto index = static_cast<const entry*>(data);
```

- 打开 `.objects` 文件
- 内存映射 4GB（RPCS3 JIT 地址空间）
- 指针指向索引开始

#### 参数处理
```cpp
for (int i = 0; i < argc; i++)
{
    std::string arg = argv[i];

    if (arg.find("--start-address=0x") == 0)
    {
        // 解析 JIT 代码地址
        std::uint64_t addr = -1;
        std::from_chars(arg.data() + ("--start-address=0x"sv).size(),
                        arg.data() + arg.size(), addr, 16);

        // 在索引中查找地址
        for (int j = 0; j < 0x100'0000; j++)
        {
            if (index[j].addr == 0)
                break;

            if (index[j].addr == addr)
            {
                found = index + j;
                break;
            }
        }
    }
    // ... 其他参数处理 ...
}
```

**关键步骤：**
1. 检测 `--start-address=0x` 参数
2. 提取十六进制地址
3. 在索引中线性搜索匹配的地址
4. 保存找到的条目

#### 代码提取
```cpp
if (found)
{
    const char* name = static_cast<char*>(data) + found->off + found->size;

    const int fd2 = open(out_file.c_str(),
        O_WRONLY | O_CREAT | O_EXCL, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);

    if (fd2 > 0)
    {
        write(fd2, static_cast<char*>(data) + found->off, found->size);
        close(fd2);
    }

    args.emplace_back("--adjust-vma=" + to_hex(addr));
}
```

**功能：**
1. 获取对象文件名
2. 创建临时文件（O_EXCL 防止覆盖）
3. 写入 JIT 代码数据
4. 添加 `--adjust-vma` 参数调整虚拟内存地址

#### objdump 调用
```cpp
args[0] = "/usr/bin/objdump";

// ... 构建命令行 ...

// 如果找到 JIT 代码，修改参数
if (found)
{
    args.pop_back();
    args.emplace_back("-b");
    args.emplace_back("binary");
    args.emplace_back("-m");
    args.emplace_back("i386:x86-64");
    args.emplace_back(std::move(out_file));
}

// fork 并执行 objdump
if (found)
{
    // 父进程：读取 objdump 输出
    int fds[2];
    pipe(fds);
    if (fork() > 0)
    {
        close(fds[1]);
        // 读取管道，过滤 \0 字符
        while (read(fds[0], &c, 1) != 0)
        {
            if (c) buf += c;
            // ...
        }
        return 0;
    }
    else
    {
        // 子进程：执行 objdump
        dup2(fds[1], STDOUT_FILENO);
        // fallthrough
    }
}

return execv(new_argv[0], new_argv.data());
```

## 主要功能函数

### to_hex()
```cpp
std::string to_hex(std::uint64_t value, bool prfx = true)
{
    char buf[20]{}, *ptr = buf + 19;
    do *--ptr = "0123456789abcdef"[value % 16], value /= 16; while (value);
    if (!prfx) return ptr;
    *--ptr = 'x';
    *--ptr = '0';
    return ptr;
}
```

- 将 64 位数字转换为十六进制字符串
- `prfx=true` 时返回 "0x" 前缀

### 字符过滤
```cpp
while (read(fds[0], &c, 1) != 0)
{
    if (c)  // 过滤 \0 字符
    {
        buf += c;
        if (c == '\n')
        {
            write(STDOUT_FILENO, buf.data(), buf.size());
            buf.clear();
        }
    }
    c = 0;
}
```

过滤来自 objdump 的空字符

## 使用流程

### 1. 准备环境
```bash
# 确保缓存目录存在
mkdir -p ~/.cache/rpcs3/ASMJIT
```

### 2. 编译工具
```bash
g++-11 objdump.cpp -o objdump
```

### 3. 运行 perf 记录
```bash
perf record -b -p `pgrep rpcs3`
```

### 4. 使用 objdump 查看结果
```bash
perf report --objdump=./objdump --gtk
```

## 地址空间

- **JIT 地址空间**：4GB (0x0 - 0x100000000)
- **索引大小**：最多 0x100'0000 个条目
- **内存映射**：mmap 整个 4GB 区域用于 JIT 代码

## 参数修改

工具会根据是否找到 JIT 代码修改参数：

### 找到 JIT 代码
- 移除 `--stop-address` 参数
- 将 `-d` 改为 `-D` (反汇编所有)
- 将 `-l` 改为 `-Mintel,x86-64`
- 添加 `-b binary -m i386:x86-64 <temp_file>`
- 添加 `--adjust-vma=<address>`

### 未找到 JIT 代码
- 参数保持不变
- 调用标准 objdump

## 进程管理

### 使用 fork/exec
```cpp
if (fork() > 0)  // 父进程
{
    // 读取 objdump 输出，过滤处理
}
else  // 子进程
{
    // 执行 objdump
    execv(new_argv[0], new_argv.data());
}
```

**目的**：
- 父进程可以处理子进程的输出
- 过滤特殊字符（\0）
- 改进输出格式

## 特点

### 1. 零开销
- 仅在需要 JIT 代码反汇编时才启用
- 标准代码反汇编使用正常流程

### 2. 灵活
- 支持任意 objdump 参数
- 自动检测和处理 JIT 代码

### 3. 兼容性
- 与现有 perf 工具集成
- 不修改 RPCS3 代码

### 4. 性能
- 内存映射避免读取整个文件
- 线性搜索索引（最坏情况但可接受）

## 技术细节

### 十六进制解析
```cpp
std::from_chars(arg.data() + start, arg.data() + arg.size(), addr, 16);
```
- C++17 高效十六进制解析
- 比 sscanf 更快

### 内存映射大小
```cpp
mmap(nullptr, 0x10000'0000, ...)  // 4GB
```
- RPCS3 使用 4GB JIT 地址空间
- 整个空间映射用于索引和代码

### 编译优化
编译时应使用优化标志：
```bash
g++-11 -O3 objdump.cpp -o objdump
```

## 限制

1. **仅限 Linux**：使用 POSIX API（fork, exec, mmap）
2. **仅限 perf**：专为 Linux perf 工具设计
3. **x86-64 only**：固定假设 x86-64 架构

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - RPCS3 主程序
- JIT 编译器（在 Emu 目录中）

## 参考资源
- Linux perf 文档
- objdump 手册
- RPCS3 JIT 编译器实现
