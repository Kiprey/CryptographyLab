# RC4加密算法
## 算法
1. 初始化S盒

 - S[256]：S盒是char型数组，大小为256，填充[0,255]
 - k[256]：不断重复密钥填充数组k，k[i] = key[i % len]
 - 对于i=0-255：j = (j + S[i] + k[i]) % 256，交换s[i]和s[j]

2. 伪随机序列的生成

- 创建两个计数器i,j，初始值为0
- i = (i + 1) % 256,j = (j + s[i]) % 256，交换s[i]和s[j]
- 下标t = (s[i] + s[j]) % 256

2. 加密/解密

- s[t]^data

## 说明
可加密任意字符串，密钥为任意字符串