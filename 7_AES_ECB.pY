from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'

fname_r = "7.txt"
fh = open(fname_r)
data=fh.read()
data=data.strip()
cipher_text=base64.b64decode(data)

cipher = AES.new(key,AES.MODE_ECB)

plaintext = cipher.decrypt(cipher_text)

print(plaintext)