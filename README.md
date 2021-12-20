# CryptographyLab

## 编译方式

使用 `cmake . -B build` 创建 Makefile。
编译结果将保存在 build 文件夹下。

Cmake 可选参数：

```bash
-DASAN_ENABLE=True           # 启动漏洞检测机制，在检测到越界读写等开发漏洞时，立即 abort
-DCMAKE_BUILD_TYPE=Release   # 发行版编译，启动优化技术
```

调试开发时，个人推荐使用以下命令进行编译：

```bash
cmake . -B build -DASAN_ENABLE=True -DCMAKE_BUILD_TYPE=Debug
cd build
make
```