
from functionsc6 import hamming_dist, lists_to_binary_hex, find_repeating_key_xor_key
import base64

from Crypto.Util.strxor import strxor, strxor_c

#https://pypi.org/project/langdetect/
from langdetect import detect, detect_langs

print("---------- Find the key size ----------")

ascii_characters = [ord(chr) for chr in map(chr, range(128))] #ascii characters as int strings
#print(ascii_characters) #print ascii characters as int strings

max_value = 40
min_value = 2
KEYSIZES = list()
count = 0
for lengths in range(max_value-1):
        length = min_value + count
        KEYSIZES.append(length)
        count += 1
print("Guess size min:", min_value, ", Guess size max:", min_value, ", Number of keys to try",len(KEYSIZES)+1)

strA = "this is a test"
strB = "wokka wokka!!!"
byte_arrayA = strA.encode('utf-8')
byte_arrayB = strB.encode('utf-8')
print("Hamming distance test:",   hamming_dist(byte_arrayA,byte_arrayB),"---> Ok")

fname_r = "6.txt"
fh = open(fname_r)
data=fh.read()
data=data.strip()
cipher_texts=base64.b64decode(data)

print("Decode base64 to Hex Binary Data: Ok")

division = list()
values = dict()

for keysize in KEYSIZES:
    i=1
    parts=list()
    for i in range(i,len(cipher_texts)+1):
        #print(i+KEYSIZES[i])
        shifterb1=i*keysize
        keys_block1 = cipher_texts[shifterb1:keysize+(shifterb1)]
        keys_block2=  cipher_texts[(i+1)*keysize:keysize+((i+1)*keysize)]
        
        if len(keys_block1)==0 or len(keys_block2)==0:
            pass
        else:
            #print("---1st", keys_block1, "length:",len(keys_block1) )
            #print("---2nd", keys_block2, "length:",len(keys_block2) )

            distance = hamming_dist(keys_block1,keys_block2)
            #print("---dist", distance)
            division = distance/keysize
            #print("---divNorm",division, "length:", keysize)
            #print("--------------------------")
            parts.append(division)
    values[keysize] = sum(parts)/len(parts)
    
sorted_dict = sorted(values.items(), key=lambda x: x[1])
#print(sorted_dict)

key = min(values, key=values.get)
print("Keysize length found:", key, "---> Ok")


print("---------- Find the key ----------")


blocks = list() #List of 29bytes blocks

for i in range(0,len(cipher_texts),key):
    block_bytes = cipher_texts[i:i+key]
    if len(block_bytes)<key:
        break
    #print(block_bytes, len(block_bytes), type(block_bytes))
    blocks.append(block_bytes)

# for i in range(0,len(blocks)):
#     print("Blocks of keysize = 29 generated--->", "--->", i, blocks[i], len(blocks[i]))

# Convert each data block to a list of bytes
byte_lists = [list(data_block) for data_block in blocks]
print("Make the lists of 29 blocks > 1 byte size blocks")        
#lists_to_binary_hex(byte_lists[0:1])

# Transpose the bytes 
transposed_data = list(zip(*byte_lists))

print("Transpose the blocks")        
#lists_to_binary_hex(transposed_data[0:2])

#Convert each inner list to byte literal
byte_literals = [bytes(inner_list) for inner_list in transposed_data]
print("Convert each list to byte literal")        
#print(byte_literals[0:2])

repeating_key = find_repeating_key_xor_key(byte_literals)
print("Repeating-key XOR key:", repeating_key)

