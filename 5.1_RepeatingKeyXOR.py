
from Crypto.Util.strxor import strxor


print("-----------------------Declaration-----------------------")

data = b"Burning 'em, if you ain't quick and nimble \
I go crazy when I hear a cymbal"
print("the data: ", data)
print("data type: ", type(data))
print("data length: ", len(data))

original_key = b"ICE"
print("the key: ", original_key)
print("original_key type:", type(original_key))
print("original_key length:", len(original_key))


# Repeat the original key until it reaches or exceeds the desired length

# This calculates the number of times you need to repeat the original_key to 
# reach or exceed the desired length (desired_length).

print("-----------------------Operations-----------------------")

desired_length = len(data)
print("Desired length:",desired_length )
rep_times=(desired_length // len(original_key)) # The // operator in Python is the floor division operator. 
                                                # It performs division where the result is rounded down to the nearest whole number.

print("Times to repeat ICE:", rep_times, type(rep_times))

# This extracts a portion of the original_key from the beginning up to the index given
# by desired_length % len(original_key). In other words, it takes the first few bytes
# of the original_key equal to the remainder obtained from the division of desired_length
# by the length of the original_key.

completion_str=original_key[:desired_length % len(original_key)] 

print("Pending strings from ICE to complete the length:",completion_str, type(completion_str))

repeated_key = original_key * rep_times + completion_str

# Print the repeated key
print("Repeated key to length:", repeated_key)
xor = strxor(repeated_key, data)

# You can convert a bytes object back to a hexadecimal string in Python using 
# the bytes.hex() method. 
# bytes.hex(): Returns a string containing the hexadecimal representation of
# the bytes object.
print("-----------------------Result-----------------------")
result = xor.hex()
print("Encrypted message:", result)

# This slicing operation is commonly used in Python for extracting substrings or 
# portions of sequences like strings, lists, or bytes objects. It's versatile and
# widely used in various applications, including data manipulation, text processing, 
# and cryptography, among others.

print("-----------------------Misc-----------------------")

print("Example of slicing the byte:", \
    "\n", original_key[:0], \
    "\n", original_key[:1], \
    "\n", original_key[:3], \
    "\n", original_key[:4], \
)
