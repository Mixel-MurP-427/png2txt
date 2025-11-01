### PNG file signature
- Decimal: `137 80 78 71 13 10 26 10`
- Ascii/hex: `0x89 P N G 0xd 0xa 0x1a 0xa`
### Chunk 1
- **Chunk length:** *h* `00 00 00 0d`, or 13 bytes.
- **Chunk type:** *a* `IHDR`
- **Chunk data:**  
*h* `00 00 00 01 00 00 00 01 08 06 00 00 00`
    - Image width: *h* `00 00 00 01` or 1 pixels.
    - Image height: *h* `00 00 00 01` or 1 pixels.
    - Bit depth: *h* `08`
    - Color type: *h* `06`
    - Compression method: *h* `00`
    - Filter method: *h* `00`
    - Interlace method: *h* `00`
- **Chunk CRC:** *h* `1f 15 c4 89`
### Chunk 2
- **Chunk length:** *h* `00 00 00 0d`, or 13 bytes.
- **Chunk type:** *a* `IDAT`
- **Chunk data:**  
*h* `78 01 62 fa cf c0 f0 1f 00 00 00 ff ff`
- **Chunk CRC:** *h* `03 73 8d 13`
### Chunk 3
- **Chunk length:** *h* `00 00 00 06`, or 6 bytes.
- **Chunk type:** *a* `IDAT`
- **Chunk data:**  
*h* `03 00 05 0a 02 01`
- **Chunk CRC:** *h* `c9 1a 4c 9e`
### Chunk 4
- **Chunk length:** *h* `00 00 00 00`, or 0 bytes.
- **Chunk type:** *a* `IEND`
- **Chunk data:**  
*h* ``
- **Chunk CRC:** *h* `ae 42 60 82`
## The PNG image:
![the png image](1x1.png)