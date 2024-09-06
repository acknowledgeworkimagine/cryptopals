from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad
import base64

fname_r = "10.txt"
fh = open(fname_r)
data=fh.read()
data=data.strip()
byte_string=base64.b64decode(data)

print(byte_string)

def aes_in_ecb_mode(byte_string: bytes, key: bytes, encrypt: bool = False) -> bytes:
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    if encrypt:
        return cipher.encrypt(byte_string)
    else:
        return cipher.decrypt(byte_string)

# Type Annotations:
# byte_string: bytes: This annotation specifies that the byte_string parameter is expected to be of type bytes.
# key: bytes: Similarly, this annotation indicates that the key parameter should be of type bytes.
# encrypt: bool: This annotation specifies that the encrypt parameter should be of type bool.

# Default Parameter Values:
# encrypt: bool = False: This part of the parameter declaration does two things:
# It sets the type of the parameter (bool).
# It provides a default value (False), meaning that if the caller does not provide a value for encrypt,
# it will default to False. Default values make the function more flexible and easier to use because 
# not all arguments need to be provided every time the function is called.

# Return Type Annotation:
# -> bytes: This indicates that the function returns a value of type bytes.
# This is part of Python's type hinting system, which helps with readability and static analysis,
# but is not enforced at runtime.

# Benefits of These Practices:
# Readability: Type annotations make the function signature more descriptive,
# so someone reading the code can quickly understand what types of arguments the function expects and what it returns.
# 
# Error Checking: Tools like linters and type checkers can use these annotations to detect potential issues before running the code.
# 
# Documentation: Annotations serve as a form of documentation, making it clear to other developers
# (or to yourself in the future) what types the function works with.
# 
# Flexibility with Defaults: Default parameter values allow for flexible function calls.
# In this case, if encrypt is not specified, it defaults to False, simplifying function calls when the default behavior is desired.

def cbc_mode(byte_string: bytes,key:bytes, iv:bytes, encrypt: bool = True) -> bytes:
    if encrypt:
        previous_block=iv
        cipher_text = b''
        for i in range(0,len(byte_string),len(key)):
            #print(pad(byte_string[i:i+len(key)],len(key)))
            plain_text = strxor(byte_string[i:i+len(key)],
                                previous_block)
            previous_block = aes_in_ecb_mode(plain_text,key,encrypt=True)
            cipher_text += previous_block
        return cipher_text
    else:
        previous_block = iv
        plain_text = b''
        for i in range(0,len(byte_string),len(key)):
            cipher_text = byte_string[i:i+len(key)]
            plain_text += strxor(aes_in_ecb_mode(cipher_text,key,encrypt=False),previous_block)
            previous_block = cipher_text
        return plain_text
    
decrypted_text = cbc_mode(byte_string, b'YELLOW SUBMARINE', b'\x00'*16, encrypt=False)
print(decrypted_text)

string_text = decrypted_text.decode('utf-8') #  Decoding the bytes to a string
lines = string_text.split('\n') # Splitting the text by newline character

for line in lines:
    print(line)

encrypted_text = cbc_mode(decrypted_text, b'YELLOW SUBMARINE', b'\x00'*16, encrypt=True)
print(encrypted_text)
