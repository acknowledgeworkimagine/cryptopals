import base64

# Method 1. using base64 class
# https://www.delftstack.com/howto/python/convert-hex-to-base64-python/
# https://blog.finxter.com/python-convert-hex-to-base64/

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# hex string -> base64 string
b64 = base64.b64encode(bytes.fromhex(hex)).decode()

# base64 string -> hex string
#s2 = base64.b64decode(b64.encode()).hex()

print("Hex value :",  hex)
print("Base64 value :", b64)
