import zlib, struct

def calcCrcZlib(type_bytes: bytes, data_bytes: bytes) -> bytes:
    """
    Calculates the CRC for a PNG chunk in Python using the zlib module.

    Args:
        chunk_type_bytes: The 4-byte chunk type (e.g., b'IHDR').
        chunk_data_bytes: The data contained within the chunk.

    Returns:
        The 4-byte CRC checksum in big-endian (network) byte order.
    """
    # The CRC is computed over the chunk type and chunk data (not length or CRC field)
    crcData = type_bytes + data_bytes
    
    # Calculate the CRC-32 checksum
    # zlib.crc32 returns a signed or unsigned integer depending on the platform,
    # but the value is correct for the PNG spec (which uses the standard CRC-32 polynomial)
    crc_int = zlib.crc32(crcData) & 0xFFFFFFFF
    
    # PNG uses network byte order (big-endian) for all integer fields.
    # struct.pack('>I', ...) converts the unsigned integer to 4 big-endian bytes.
    return struct.pack('>I', crc_int)

print(calcCrcZlib(bytes(input("Chunk type: ").encode('utf-8')), bytes.fromhex(input("Hex string: ").replace(" ", "").strip())).hex())
# print(type(int("IDAT".encode('utf-8').hex(), 16)))
# buffer = [int("IDAT".encode('utf-8').hex(), 16)] + [0x78, 0x01, 0x62, 0xfa, 0xcf, 0xc0, 0xf0, 0x1f, 0x0, 0x0, 0x0, 0xff, 0xff]
# print(struct.pack('>I', calcCrc(buffer, len(buffer)-1, table)).hex())
