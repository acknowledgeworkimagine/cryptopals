
from Crypto.Util.Padding import pad, unpad

block = b"YELLOW SUBMARINE"

padded_block = pad(block,20)

block_size = 20
plaintext_length = len(block)

# This is how padding the padding value is calculated
paddingHex = hex(block_size - (plaintext_length % block_size))

print(f"Padding value: {paddingHex}")

print(padded_block)