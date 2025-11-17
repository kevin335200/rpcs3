# main.cpp - RPCS3 程序入口点

## 概述
`main.cpp` 是 RPCS3 模拟器的主程序入口点。该文件包含主函数，是应用程序启动的起点。

## 文件位置
- `/home/user/rpcs3/rpcs3/main.cpp`

## 关键功能

### main() 函数
```cpp
int main(int argc, char** argv)
{
    const int exit_code = run_rpcs3(argc, argv);
    sys_log.notice("RPCS3 terminated with exit code %d", exit_code);
    return exit_code;
}
```

**功能说明：**
- 接收命令行参数 `argc` 和 `argv`
- 调用 `run_rpcs3()` 函数处理所有启动逻辑
- 记录 RPCS3 的退出代码
- 返回退出代码给操作系统

### 日志记录
- 使用 `LOG_CHANNEL(sys_log, "SYS")` 定义系统日志通道
- 通过 `sys_log.notice()` 记录退出信息

## 依赖项
1. **stdafx.h** - 预编译头文件，包含常用头文件
2. **rpcs3.h** - RPCS3 主程序头文件，声明 `run_rpcs3()` 函数

## 控制流
1. 程序启动 → main() 函数
2. main() → run_rpcs3(argc, argv)
3. run_rpcs3() 处理完成 → 返回退出码
4. main() 记录退出信息 → 程序结束

## 简单性设计
这个文件的设计非常简洁，只包含最少的必要代码。所有复杂的初始化和主程序逻辑都被委托给 `run_rpcs3()` 函数处理，这样做的好处是：
- 清晰的程序结构
- 易于维护和调试
- 主函数保持最小化

## 相关文件
- `/home/user/rpcs3/rpcs3/rpcs3.h` - 声明 run_rpcs3() 函数
- `/home/user/rpcs3/rpcs3/rpcs3.cpp` - 实现 run_rpcs3() 函数的所有逻辑
