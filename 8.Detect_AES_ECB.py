from Crypto.Cipher import AES
import base64
from functionsc6 import find_repeats, find_string_in_file

key = b'YELLOW SUBMARINE'

fname_r = "8.txt"
fh = open(fname_r)
data=fh.read()
data=data.strip()
cipher_text=bytes.fromhex(data)
key_size = 16
fh.close()


#print(cipher_text)

blocks = list() #List of 16bytes blocks

for i in range(0,len(cipher_text),key_size):
    block_bytes = cipher_text[i:i+key_size]
    if len(block_bytes)<key_size:
        break
    blocks.append(block_bytes)

#print(blocks)
rep = find_repeats(blocks)[0]
repHex = bytes.hex(rep)
print("16 bytes repeating key:", repHex)
        
find_string_in_file("8.txt",repHex)