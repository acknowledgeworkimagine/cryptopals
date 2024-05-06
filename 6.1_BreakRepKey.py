
from functionsc6 import hamming_dist
import base64

max_value = 40
min_value = 2
KEYSIZES = list()
count = 0
for lengths in range(max_value-1):
        length = min_value + count
        KEYSIZES.append(length)
        count += 1
print("KEYSIZES:", KEYSIZES)
print("KEYSIZES LENGTH:",len(KEYSIZES))

strA = "this is a test"
strB = "wokka wokka!!!"
byte_arrayA = strA.encode('utf-8')
byte_arrayB = strB.encode('utf-8')
print("Hamming distance test:",   hamming_dist(byte_arrayA,byte_arrayB),"--- Ok")

fname_r = "6.txt"
fh = open(fname_r)
cipher_texts = list()
for line in fh:
    #line = line.rstrip()
    data=base64.b64decode(line)
    cipher_texts.append(data)
#print(cipher_texts)
#print(len(data))
#print(len(cipher_texts))



fname_w = "6decoded.txt"
fh_w = open(fname_w,"w")
for item in cipher_texts:
    fh_w.write(str(item) + "\n")

parts=list()
division = list()
for cipher in cipher_texts:
    for i in range(0,len(KEYSIZES)):
        #print(i+KEYSIZES[i])
        keys_block1 = cipher[0:KEYSIZES[i]]
        keys_block2=  cipher[i+2:KEYSIZES[i]*2]
        #print("---1st", keys_block1, "length:",len(keys_block1) )
        #print("---2nd", keys_block2, "length:",len(keys_block2) )
        #print(cipher[2:4]) # 2,4 3,6, 4,8, 5, 10
        #print(keys_worth)
        distance = hamming_dist(keys_block1,keys_block2)
        #print(distance)
        division = distance/KEYSIZES[i]
        #print("---div",division, "length:", KEYSIZES[i])
        #parts.append(keys_block1)
        #parts.append(keys_block2)
        parts.append(division)
print("--------------------------->", min(parts))   
    
print(len(parts))
#print(type(parts[0:2]))
#print(parts[0:39])

total= list()
for i in range(0,len(parts),39):
    print(parts[i-39:i])
    values = parts[i-39:i]
    for sub, i in zip(values, range(0,39)):
        total[i] = sub+total[i]
        
        
            

# for i in range(0,38*64,38): # range(0,len(KEYSIZES)*len(cipher_texts),len(KEYSIZES))
#     print(i)


# dist=list()
# for i in range(0,39): #0,39 -- > 39,78
#     first = parts[i*2]

#     second = parts[i*2+1]

#     distance = hamming_dist(first,second)
#     print("---1st",first)
#     print("---2nd",second)
#     print("Hamming Distance ---", distance)

#     dist.append(distance)
    
# print("Distances: ", dist)
# print(len(dist))
# norm=list()
# key_normdist =dict()
# for i in range(39):
#     div = dist[i]/KEYSIZES[i]
#     norm.append(div)
#     key_normdist = {KEYSIZES[i]:div}
#     print(key_normdist)  
       
       
    