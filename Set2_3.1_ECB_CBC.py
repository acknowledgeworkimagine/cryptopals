from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad
from functionsc6 import detect_AES
key16Bytes = Random.get_random_bytes(16)
message_jibber = b'A'*50
print(len(message_jibber))
print(key16Bytes)

def encryption_oracle(key,message, mode=None, block_size=16):
    padded_msg = pad(message,block_size)
    print(padded_msg)
    print(len(padded_msg))
    header  = pad(Random.get_random_bytes(randint(5,10)),block_size)
    footer  = pad(Random.get_random_bytes(randint(5,10)),block_size)
    to_encrypt = header + padded_msg + footer 
    
    if mode==None:
        mode = Random.random.choice(['ECB', 'CBC'])
    if mode == 'ECB':
        cipherECB = AES.new(key,AES.MODE_ECB)
        print("ECB mode encrypted")
        return cipherECB.encrypt(to_encrypt)
    if mode == 'CBC':
        cipherCBC = AES.new(key,AES.MODE_CBC)
        print("CBC mode encrypted")
        return cipherCBC.encrypt(to_encrypt)

def decryption_oracle(cipherthext, keysize=16):
    blocks = list() #List of 16bytes blocks
    for i in range(0,len(cipherthext),keysize):
        block_bytes = cipherthext[i:i+keysize]
        if len(block_bytes)<keysize:
            break
        blocks.append(block_bytes) 
        
    if detect_AES(blocks) == True:
        print("ECB mode detected")
    else:
        print("CBC mode detected")
    
encrypted_text = encryption_oracle(key16Bytes,message_jibber)
decryption_oracle(encrypted_text)