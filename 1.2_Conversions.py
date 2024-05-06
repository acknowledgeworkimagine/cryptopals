
import binascii
print("---------------------------Exercise results #1------------------------------")

# Other types/methods of conversion
# https://medium.com/analytics-vidhya/crypto-basics-fixed-xor-implementation-python-9cfba54f4661

# 1. Converting HEX to integer:

hex = "CAFEBABE"
base = 16
b16 = int(hex, base)
print("Base16 value :", b16)

# 1. Converting integer to binary:

decimal = bin(3405691582)
print(decimal)
hexadecimal = bin(0xCAFEBABE)
print(hexadecimal)
octal = bin(0o31277535276)
print(octal)

# 3- Converting binary to desired format

print ("Simple conversion :")

# bin() function is used to convert integers into binary strings
# but it's not directly applicable to binary data represented as bytes.

print( bin(0) )
print( bin(15) )

print ("Skip the first two digits in the list :")
print( bin(0)[2:] )
print( bin(15)[2:] )

# Do you want a desired binary length?
print ("Adjust the length: ")
binNum1 = bin(0)[2:]
binNum1 = binNum1.zfill(0)
binNum2 = bin(15)[2:]
binNum2 = binNum2.zfill(8)
print(binNum1)
print(binNum2)



print("---------------------------Exercise results #2------------------------------")
# Convert Binary to HEX?


# In Python, a bytes literal starts with a lowercase 'b' prefix followed by single quotes (b'...'). 
# It represents a sequence of bytes, where each byte is represented by a hexadecimal escape sequence

binary_data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F' #is a bytes literal in Python.

print(type(binary_data))
lst_of_bytes = list()
print(type(lst_of_bytes))
for byte in binary_data:
    binary_string = format(byte,'08b')
    lst_of_bytes.append(binary_string)
print("A list of binaries coming from a bytes hex literal: \n", lst_of_bytes )

print("---------------------------Exercise results #3------------------------------")

binary_string = ' '.join(format(byte,'08b') for byte in binary_data)

print("Bytes literal \n", binary_data)
print("Binary string:\n", binary_string)

hexnumber = b'\x01'
simple_hex = format(int.from_bytes(hexnumber, byteorder='big'), '08b')
print("Simple conversion:\n", simple_hex)

