
from Crypto.Util.strxor import strxor, strxor_c

#https://pypi.org/project/langdetect/
from langdetect import detect, detect_langs

hex_byte_array ="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

byte_arrayA = bytes.fromhex(hex_byte_array)

ascii_characters = [ord(chr) for chr in map(chr, range(128))] #ascii characters as int strings
#print(ascii_characters) #print ascii characters as int strings

xored_list = list()
for values in ascii_characters:
    xor_byte = strxor_c(byte_arrayA, values)
    #print("Key", chr(int), "Message", xor_byte)
    text = xor_byte.decode('ascii')
    try:
        result = detect_langs(text)
        #print(result)
        for item in result:
            #print(f"{item.lang}: {item.prob}")
            if ((item.lang =="en") and item.prob >= 0.99999):  
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
