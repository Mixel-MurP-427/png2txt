#this file sorts the bytes inside a PNG file and writes a markdown outline of them

file_header = b'\x89PNG\r\n\x1a\n'
asciiLetterRange = set(range(65, 91)) | set(range(97, 123))


# We got some nice type conversions here :-)
def hex_print(hpBytes: bytes):
    return ' '.join(str(hex(byte)[2:]).zfill(2) for byte in hpBytes)

def dec_print(dpBytes: bytes):
    return ' '.join(str(int(byte)) for byte in dpBytes)

def ascii_print(apBytes: bytes):
    output = []
    for byte in apBytes:
        if not byte in asciiLetterRange:
            raise ValueError(f'The numeric byte value "{byte}" is not a letter A-Z or a-z in ascii.')
        output.append(chr(byte))
    return ''.join(output)


# Sorts the bytes inside a PNG file into chunks, and sorts chunks into length, type, data, and CRC sections.
#returns the sorted bytes, plus the length of the file
def organize_bytes(filepath):
    with open(filepath, 'rb') as myFile:
        file_bytes = myFile.read()
    if file_bytes[:8] != file_header:
        raise ValueError('filepath must be to a png file.')
    
    chunks = []
    byte_index = 8
    #find all chunks
    while byte_index < len(file_bytes):
        #create new dictionary for new chunk
        chunks.append({})
        #get chunk length and type
        chunks[-1]['length'] = file_bytes[byte_index:byte_index+4]
        chunks[-1]['type'] = file_bytes[byte_index+4:byte_index+8]
        byte_index += 8
        #get chunk data
        chunks[-1]['data'] = file_bytes[byte_index : byte_index + int.from_bytes(chunks[-1]['length'])]
        byte_index += int.from_bytes(chunks[-1]['length'])
        #get chunk CRC
        chunks[-1]['CRC'] = file_bytes[byte_index:byte_index+4]
        byte_index += 4
    
    return chunks, len(file_bytes)

def organize_IHDR(IHDR_bytes):
    if type(IHDR_bytes) != bytes:
        raise TypeError(f'organize_IHDR() argument must be bytes, not "{type(IHDR_bytes)}".')
    if len(IHDR_bytes) != 13:
        raise ValueError(f'organize_IHDR() argument must be 13 bytes. Are you sure this is from an IHDR chunk?')
    return {
        'width': IHDR_bytes[:4],
        'height': IHDR_bytes[4:8],
        'depth': IHDR_bytes[8:9],
        'color': IHDR_bytes[9:10],
        'compression': IHDR_bytes[10:11],
        'filter': IHDR_bytes[11:12],
        'interlace': IHDR_bytes[12:],
    }

def write_analysis(imagepath):

    chunks, filesize = organize_bytes(imagepath)

    #begin writing to the markdown file
    with open('png_bytes_analysis.md', 'w') as md_output:

        #PNG file header
        md_output.write(f'### File size: {filesize} bytes\n')
        md_output.write('### PNG file signature\n- Decimal: `137 80 78 71 13 10 26 10`\n- Ascii/hex: `0x89 P N G 0xd 0xa 0x1a 0xa`\n')

        #go through all chunks
        for i, chunk in enumerate(chunks):
            md_output.write(f'### Chunk {i+1}\n')

            #chunk length
            md_output.write(f'- **Chunk length:** *h* `{hex_print(chunk['length'])}`, or {int.from_bytes(chunk['length'])} bytes.\n')

            #chunk type
            md_output.write(f'- **Chunk type:** *a* `{ascii_print(chunk['type'])}`\n')
            

            #chunk data
            md_output.write(f'- **Chunk data:**  \n*h* `{hex_print(chunk['data'])}`\n')

            if ascii_print(chunk['type']) == 'IHDR':
                IHDR_data = organize_IHDR(chunk['data'])
                #TODO include explanation of each value.
                md_output.write(  f'    - Image width: *h* `{hex_print(IHDR_data["width"])}` or {int.from_bytes(IHDR_data["width"])} pixels.\n' \
                                  f'    - Image height: *h* `{hex_print(IHDR_data["height"])}` or {int.from_bytes(IHDR_data["height"])} pixels.\n' \
                                  f'    - Bit depth: *h* `{hex_print(IHDR_data["depth"])}`\n' \
                                  f'    - Color type: *h* `{hex_print(IHDR_data["color"])}`\n' \
                                  f'    - Compression method: *h* `{hex_print(IHDR_data["compression"])}`\n' \
                                  f'    - Filter method: *h* `{hex_print(IHDR_data["filter"])}`\n' \
                                  f'    - Interlace method: *h* `{hex_print(IHDR_data["interlace"])}`\n'
                                )

            #chunk CRC checksum
            md_output.write(f'- **Chunk CRC:** *h* `{hex_print(chunk['CRC'])}`\n')

        #attach image at bottom
        md_output.write(f'## The PNG image:\n![the png image]({imagepath})')


my_file_path = '1x1.png'
write_analysis(my_file_path)