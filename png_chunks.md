A PNG file starts with an 8-byte signature, followed by a series of chunks, each containing a 4-byte length, a 4-byte chunk type, the chunk data, and a 4-byte CRC checksum. The first chunk must be `IHDR`, which contains metadata like image width, height, bit depth, and color type. The image data itself is in one or more IDAT chunks, and the file ends with the `IEND` chunk.

## Byte-by-byte structure
1. **PNG Signature** (8 bytes)
    - This is a fixed sequence of bytes that identifies the file as a PNG.
    - **Bytes 1-4:** `137, 80, 78, 71` *(0x89,0x50,0x4E,0x47)*. The first byte is deliberately non-ASCII to avoid being recognized as a text file.
    - **Bytes 5-6:** `13, 10` *(0x0D,0x0A)*. These are carriage return and line feed characters.
    - **Bytes 7-8:** `26, 10` *(0x1A,0x0A)*. The `0x1A` (Ctrl-Z) byte is an end-of-file marker for DOS, and the `0x0A` is another line feed.
    - The entire signature acts as a check to ensure the file has not been corrupted by a bad transfer.
2. **Chunks** (Variable length)
    - A PNG file is a sequence of chunks. Each chunk has the following four parts:
    - **Length (4 bytes):** An unsigned integer that specifies the number of bytes in the chunk's data field.
    - **Chunk Type Code (4 bytes):** A fixed code that identifies the type of data in the chunk (e.g., `IHDR`, `IDAT`, `IEND`).
    - **Chunk Data (variable):** The actual data for that chunk type.
    - **CRC (4 bytes):** A Cyclic Redundancy Check calculated on the bytes for the chunk type and chunk data. This is used to detect corruption.

## Key chunks
- **`IHDR` (Image Header):** This is the first chunk and contains the image's essential properties.
    - **Width (4 bytes):** The image width in pixels.
    - **Height (4 bytes):** The image height in pixels.
    - **Bit depth (1 byte):** The number of bits per color channel.
    - **Color type (1 byte):** Specifies the pixel format (e.g., grayscale, truecolor, indexed color).
    - **Compression method (1 byte):** Always 0 for PNG.
    - **Filter method (1 byte):** Always 0 for PNG.
    - **Interlace method (1 byte):** 0 for no interlace, 1 for Adam7 interlace.
- **`IDAT` (Image Data):** This chunk contains the compressed pixel data for the image. An image can have multiple `IDAT` chunks to allow for streaming generation.
- **`IEND` (Image End):** This is the final chunk in a PNG file. It contains no data (its length is 0) and marks the end of the file.
## Example of a chunk:
- `0000000D` (Length = 13 bytes)
- `49484452` (Type = `IHDR`)
- `00000004000000040802000000` (Data = width, height, bit depth, etc.)
- `26930929` (CRC checksum)