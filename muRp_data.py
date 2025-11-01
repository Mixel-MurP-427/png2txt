#this code is currently an identical copy of crc.py

import zlib, struct

def calcCrc4png(input_bytes: bytes) -> bytes: #accepts bytes of png type + data, returns 4 big-endian bytes
    crc_int = zlib.crc32(input_bytes) & 0xFFFFFFFF # Calculate the CRC-32 checksum
    return struct.pack('>I', crc_int) # convert from signed/unsigned int to 4 big-endian bytes

#print(calcCrc4png(bytes(input("Chunk type: ").encode('utf-8')) + bytes.fromhex(input("Hex string: ").replace(" ", "").strip())).hex())

mynewchunk = 'muRp'