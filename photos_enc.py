#!/usr/bin/env python
# coding: utf-8

# In[51]:


from Crypto.Cipher import AES
from Crypto import Random


# In[52]:


# key = Random.new().read(AES.block_size)
# iv = Random.new().read(AES.block_size)
# print(key, iv)
# key = b'\xb1p\x9c|3\xe7\xbc:\xe5j\x1e\x86]\xca\xb0\xc0'
# iv = b'O\t4\xb5\x11O\xd6\xf6\x0e\xe6<\xbax\xeb{k'


# In[53]:


def encrypt(input_data):
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    enc_file = open("out_e.enc", "wb")
    enc_file.write(enc_data)
    enc_file.close()


# In[54]:


def decrypt(encrypted_data):
    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(encrypted_data)

    output_file = open("out_d.jpg", "wb")
    output_file.write(plain_data)
    output_file.close()


# In[1]:


def main():
    flag = int(input('Print 0 to encrypt or 1 to decrypt: '))
    
    key_file = open('key.enc', 'rb')
    key = key_file.read()
    key_file.close()

    iv_file = open('iv.enc', 'rb')
    iv = iv_file.read()
    iv_file.close()
    
    if flag == 0:
        input_file = open("photo.jpg", "rb")
        input_data = input_file.read()
        input_file.close()
        encrypt(input_data)
    elif flag == 1:
        enc_file = open("out_e.enc", "rb")
        encrypted_data = enc_file.read()
        enc_file.close()
        decrypt(encrypted_data)
    else:
        print('Err')
#         exit()
main()

