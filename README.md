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

## SSL 使用

首先，使用 openssl 分别创建证书：

```bash
# 生成服务端私钥
# openssl genrsa -aes128 -out server.key 1024 (带加密的密钥生成)
openssl genrsa -out server.key

# 生成服务端证书签名请求文件
openssl req -new -key server.key -out server.csr

# 生成客户端私钥
# openssl genrsa -aes128 -out client.key 1024 (带加密的密钥生成)
openssl genrsa -out client.key

# 生成客户端证书签名请求文件
openssl req -new -key client.key -out client.csr

# 生成 CA 签名文件
# openssl genrsa -aes128 -out ca.key 1024 (带加密的密钥生成)
openssl genrsa -out ca.key

# 生成 CA 自签名证书
openssl req -new -x509 -key ca.key -out ca.crt

# 使用 CA 对服务端和客户端签名请求文件进行签名，创建对应的证书
#   -CA               用于签名的 CA CRT 证书
#   -CAkey            用于签名的 CA 密钥
#   -CAcreateserial   序列号文件不存在时自动生成
#   -in               等待被签名的 签名请求文件
#   -out              签名后生成的证书
openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt
openssl x509 -req -days 3650 -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt

# 证书验证
openssl verify -verbose -x509_strict -CAfile ca.crt server.crt
openssl verify -verbose -x509_strict -CAfile ca.crt client.crt
```

之后，执行 SSL_test 并根据输出进行输入即可正常使用。

## 运行 prequires

python版本为3.9.2，依赖安装：

````bash
# 项目Ui基于PySide6
pip install --user PySide6
# pwn-tools开启线程
pip install --user pwn-tools
# 调用c++库
pip install --user ctypes
````

安装完成后在 `CryptographyLab/src/Modern_GUI_PyDracula_PySide6_or_PyQt6` 目录下运行 `main.py`

如果遇到Asian问题,执行

````bash
export ASAN_OPTIONS=verify_asan_link_order=0
````
