#include <dlfcn.h>
#include <cassert>
#include <iostream>

using namespace std;

typedef void(*void__cons_ch_ptr)(const char*);
typedef const char*(*cons_char_cons_char_ptr)(const char*);

void DES_test(void* handle, const string m, const string key) {
    void__cons_ch_ptr des_gen_keys = (void__cons_ch_ptr) dlsym(handle, "DES_generateKeys");
    cons_char_cons_char_ptr des_enc = (cons_char_cons_char_ptr) dlsym(handle, "DES_encrypt");
    cons_char_cons_char_ptr des_dec = (cons_char_cons_char_ptr) dlsym(handle, "DES_decrypt");

    assert(des_gen_keys && des_enc && des_dec);

    des_gen_keys(key.c_str());
    const char* cipher = des_enc(m.c_str());
    const char* plain = des_dec(cipher);

    cout << "============ DES TEST ============" << endl;
    cout << "origin plain: " << m << endl;
    cout << "key: " << key << endl;
    cout << "cipher: " << cipher << endl;
    cout << "decrypt_plain: " << plain << endl;
    cout << endl;
}

int main() {
    void* handle = dlopen("./libcryptolab.so", RTLD_LAZY);
    assert(handle);

    // DES
    DES_test(handle, "It's a secret?", "12345678");


    dlclose(handle);

    return 0;
}