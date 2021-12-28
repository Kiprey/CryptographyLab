#include "LFSR.h"

/*
初始化反馈系数

c：反馈系数数组； key：密钥

LFSR没有定义怎么用密钥得到密钥流
******初始化反馈系数是我自己想的******
①key四个字符为一组，各组异或结果的最低位（0或1）为四个系数初始值；
②不足四个字符的密钥：最低位重复填充四个系数；
③密钥按四个字符一组分组后剩下的字符：最低位依次和四个系数或，然后赋值给系数
*/
void coefInit(unsigned char *c, string key)
{
    unsigned int len=key.length();
    for(int i=0;i<4;i++)   //先用前四个字符最低位填充四个系数
    {
        c[i]=(key[i%len])&0x01;
    }
    if(len>4)   //如果密钥字符数大于4
    {
        int number=len/4;
        for(int i=1;i<number;i++) //按四个字符分组并异或
        {
            for(int j=0;j<4;j++)
            c[i]=(c[i]^key[i*4+j])&0x01;
        }
        for(int i=number*4;i<len;i++)//分组后剩余字符异或
        {
            c[i%4]=(c[i%4]^key[i])&0x01;
        }
    }
}

/*
更新密钥流输出序列并返回一位流密钥
c：反馈系数数组； k:密钥流输出序列（4个寄存器）
*/
static unsigned char kUpdata(unsigned char *c,unsigned char *k)
{
    unsigned char result=k[0]; //返回结果为k[0]，即第一个寄存器的值
    unsigned char kn=0x00;//即将加入输出序列的值
    for(int i=0;i<4;i++)
    {
        kn=(k[i]*c[i])^kn;  //计算即将加入输出序列的值：异或各个反馈系数*寄存器
    }

    //更新密钥流输出序列
    for(int i=1;i<4;i++)
        k[i]=k[i-1]; 
    k[3]=kn;

    return result;
}

/*
JK触发器
j、k：JK触发器的输入； last_state：上一时刻状态
*/
static unsigned char JK(unsigned char j,unsigned char k,unsigned char last_state)
{
    unsigned char result=0;
    if(j==0)
    {
        if(k==0)
        result=last_state;
        else if(k==1)
        result=0;
    }
    else if(j==1)
    {
        if(k==0)
        result=1;
        else if(k==1)
        result=1-last_state;
    }
    return result;
}

/*
加解密算法
data：待加密或解密的数据； c：反馈序列系数
*/
string LFSR(string data,unsigned char *c)
{
    unsigned len=data.length();
    string LFSR_result=data;   //解密或解密后的结果
    unsigned char k1[4]={0,0,1,1};//初始输出序列1
    unsigned char k2[4]={1,0,0,1};//初始输出序列2
    unsigned char last_state=0;  //jk触发器上一状态
    unsigned char state=0; //jk触发器当前状态
    for(int i=0;i<len;i++)//待处理数据每一位与密钥流异或
    {
        bitset<8> bits = bitset<8>(data[i]);
        string bit=bits.to_string();
        for(int j=0;j<8;j++)
        {
            state=JK(kUpdata(c,k1),kUpdata(c,k2),last_state);
            bit[j]=bit[j]^state;
            last_state=state;
        }      
        unsigned int temp=0;
        for(int j=0;j<8;j++)
        {
            if(bit[j]=='1')
            temp=temp*2+1;
            else
            temp*=2;
        }
        LFSR_result[i]=(char)temp;  
    }
    
    return LFSR_result;  //返回异或后的字符串
}

