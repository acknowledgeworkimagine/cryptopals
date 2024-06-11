
import string


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

#Print a list of binary data in hex
def lists_to_binary_hex(lists):
    for sublist in lists:
        binary_hex_list = [hex(item) for item in sublist]
        print(binary_hex_list)
        


# Expected frequency of characters in English text
# Values are taken from https://en.wikipedia.org/wiki/Letter_frequency
expected_frequency = {
    ' ': 0.13000, 'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507,
    'i': 0.06966, 'n': 0.06749, 's': 0.06327, 'h': 0.06094, 'r': 0.05987,
    'd': 0.04253, 'l': 0.04025, 'c': 0.02782, 'u': 0.02758, 'm': 0.02406,
    'w': 0.02360, 'f': 0.02228, 'g': 0.02015, 'y': 0.01974, 'p': 0.01929,
    'b': 0.01492, 'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.00150,
    'q': 0.00095, 'z': 0.00074
}


#This function takes a block of bytes and XORs each byte with a single-byte key.
# The bytes(byte ^ key for byte in block) line performs the XOR operation for each byte in the block.
def xor_single_byte(block, key):
    return bytes(byte ^ key for byte in block)

def evaluate_histogram(data):
    # Calculate the frequency of each ASCII character
    total_characters = len(data)
    histogram = {char: data.count(bytes([ord(char)])) / total_characters for char in string.printable}
    return histogram

def find_repeating_key_xor_key(blocks):
    key = b''
    for block in blocks:
        #In Python, float('inf') represents positive infinity, which is a special floating-point value 
        #that is greater than any other real number. This is commonly used as an initial value for variables
        #that need to be initialized with the maximum possible value, particularly in scenarios where you want
        #to find the minimum value among a set of values.
        
        best_score = float('inf')
        best_key = None
        for possible_key in range(256):
            xored_block = xor_single_byte(block, possible_key)
            histogram = evaluate_histogram(xored_block)
            # Calculate the sum of squared differences between expected and observed frequencies
            score = sum((histogram[char] - expected_frequency.get(char, 0)) ** 2 for char in string.printable)
            if score < best_score: #The less discrepancy the better.
                best_score = score
                best_key = possible_key
        key += bytes([best_key])
    return key