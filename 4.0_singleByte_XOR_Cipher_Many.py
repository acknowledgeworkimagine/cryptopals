
from Crypto.Util.strxor import strxor, strxor_c

#https://pypi.org/project/langdetect/
from langdetect import detect, detect_langs

ascii_characters = [ord(chr) for chr in map(chr, range(128))] #ascii characters as int strings
#print(ascii_characters) #print ascii characters as int strings

fname = "4.txt"
fh = open(fname)
for line in fh:
    hex_byte_array = line.rstrip()
    #print(hex_byte_array)
    byte_arrayA = bytes.fromhex(hex_byte_array)
    #print(byte_arrayA)
    
    for values in ascii_characters:
        xor_byte = strxor_c(byte_arrayA, values)
        #print("Key", chr(int), "Message", xor_byte)
        
        try:
            text = xor_byte.decode('ascii')
        except UnicodeDecodeError:
            continue  # Ignore decoding errors
        try:
            result = detect_langs(text)
        #print(result)
            for item in result:
                #print(f"{item.lang}: {item.prob}")
                if ((item.lang =="en") and item.prob >= 0.999997):  
                    #print(f"{item.lang}: {item.prob}")
                    print("--en-->",text, "--key-->", chr(values), "--lan-->", item.lang, "score:", item.prob)
                else:
                    continue   
        except:
            continue
    #print(xored_list)

    #print(english_to_key('ETAOIN'))

    #b:bytes
    #print(key_to_english(b'\x00\x00\x00\x00\x00\x00\x00\x01')) #
    #print(key_to_english(b'00000000')) # b'00000001'  :  ascii values -> Char 0:Hex 30, Char 1:Hex 31
    #print(key_to_english(b'66666666'))

