
# https://www.pycryptodome.org/src/util/util#module-Crypto.Util.strxor


from Crypto.Util.strxor import strxor

hex_strA = "1c0111001f010100061a024b53535009181c"
hex_strB = "686974207468652062756c6c277320657965"

# bytes.fromhex() is a method in Python that creates a bytes object from a hexadecimal string. 
# It takes a string containing hexadecimal digits (with or without spaces between them) and 
# converts it into a bytes object where each pair of hexadecimal digits represents a byte.

byte_arrayA = bytes.fromhex(hex_strA)
byte_arrayB = bytes.fromhex(hex_strB)

print(byte_arrayA)
print(byte_arrayB)

xor = strxor(byte_arrayA, byte_arrayB)

# You can convert a bytes object back to a hexadecimal string in Python using 
# the bytes.hex() method. 
# bytes.hex(): Returns a string containing the hexadecimal representation of
# the bytes object.

result = xor.hex()
print(result)
