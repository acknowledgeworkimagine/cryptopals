from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'

fname_r = "7.txt"
fh = open(fname_r)
data=fh.read()
data=data.strip()
cipher_text=base64.b64decode(data)

cipher = AES.new(key,AES.MODE_ECB)

plaintext = cipher.decrypt(cipher_text) # returns a byte string
string_text = plaintext.decode('utf-8') #  Decoding the bytes to a string
lines = string_text.split('\n') # Splitting the text by newline character

for line in lines:
    print(line)