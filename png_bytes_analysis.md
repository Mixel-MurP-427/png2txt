### PNG file signature
- Decimal: `137 80 78 71 13 10 26 10`
- Ascii/hex: `0x89 P N G 0xd 0xa 0x1a 0xa`
### Chunk 1
- **Chunk length:** *h* `0 0 0 d`, or 13 bytes.
- **Chunk type:** *a* `IHDR`
- **Chunk data:**
    - Image width: *h* `0 0 0 8` or 8 pixels.
    - Image height: *h* `0 0 0 8` or 8 pixels.
    - Bit depth: *h* `8`
    - Color type: *h* `6`
    - Compression method: *h* `0`
    - Filter method: *h* `0`
    - Interlace method: *h* `0`
- **Chunk CRC:** *h* `c4 f be 8b`
### Chunk 2
- **Chunk length:** *h* `0 0 0 51`, or 81 bytes.
- **Chunk type:** *a* `IDAT`
- **Chunk data:**  
*h* `78 1 7c 8f 51 e c0 20 8 43 1f 5c dc dd 9c 95 2e f3 c3 a8 84 92 17 b a8 9 54 ab 66 20 92 94 25 75 83 fc 73 a6 c7 db 8f 0 b 10 7e 25 f0 86 50 57 f8 26 58 39 db a8 9e 50 d9 71 72 30 fe f3 ac 47 df 18 5a 31 60 c7 7e 3 97 78 1 0 0 ff ff`
- **Chunk CRC:** *h* `89 c5 35 51`
### Chunk 3
- **Chunk length:** *h* `0 0 0 6`, or 6 bytes.
- **Chunk type:** *a* `IDAT`
- **Chunk data:**  
*h* `3 0 ab ab 36 f9`
- **Chunk CRC:** *h* `b4 58 9c 26`
### Chunk 4
- **Chunk length:** *h* `0 0 0 0`, or 0 bytes.
- **Chunk type:** *a* `IEND`
- **Chunk data:**  
*h* ``
- **Chunk CRC:** *h* `ae 42 60 82`
## The PNG image:
![the png image](8x8.png)