#include "DES.h"
#include "DH.h"
#include "network.h"

extern "C" {
    // DES 协议相关
    void DES_generateKeys(const char* k){
        string key = k;
        generateKeys(key);
    }
    const char* DES_encrypt(const char* s) {
        string msg = s;
        static string ret;
        ret = encrypt(msg);
        return ret.c_str();
    }
    const char* DES_decrypt(const char *s) {
        string msg = s;
        static string ret;
        ret = decrypt(msg);
        return ret.c_str();
    }

    // DH 协议相关
    void* Auth_DH_new(int fd) {
        Auth_DH* dh = new Auth_DH(fd);
        return dh;
    }
    void Auth_DH_free(void* ptr) {
        delete (Auth_DH*) ptr;
    }

    bool Auth_DH_server_exch_key(void* ptr) {
        return ((Auth_DH*)ptr)->server_exchange_key();
    }
    
    bool Auth_DH_client_exch_key(void* ptr) {
        return ((Auth_DH*)ptr)->client_exchange_key();
    }

    bool Auth_DH_send(void* ptr, const char* msg){
        string str = msg;
        return ((Auth_DH*)ptr)->send(str);
    }
    const char* Auth_DH_recv(void* ptr) {
        static string msg;
        if(!((Auth_DH*)ptr)->recv(msg))
            return NULL;
        return msg.c_str();
    }

    // SSL 相关
    
}