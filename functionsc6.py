# bit-wise hamming distance

def hamming_dist(bytesA, bytesB):

    def bytes_to_bits(byte_block):
    # Initialize an empty string to store the binary representation
        bit_string = ""
    
    # Iterate through each byte in the byte string
        for byte in byte_block:
        # Convert each byte to its binary representation
        # and concatenate it to the bit string
            bit_string += format(byte, '08b')
    
        return bit_string

    #print(bytesA, len(bytesA))
    #print(bytesB, len(bytesB))
    
    max_len = max(len(bytesA), len(bytesB))
    bytesA = bytesA.ljust(max_len, b'\x00')
    bytesB = bytesB.ljust(max_len, b'\x00')
    straA_10 = bytes_to_bits(bytesA)
    straB_10 = bytes_to_bits(bytesB)


    #print(straA_10, len(straA_10))
    #print(straB_10, len(straB_10))

    count = 0
    for i in range(len(straA_10)):
    #print(straA_10[i],straB_10[i],straA_10[i] != straB_10[i])
        if  straA_10[i] != straB_10[i]:
            count += 1
    #print(count)
    return count
