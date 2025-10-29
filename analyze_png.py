#use `hex()` to convert to hexadecimal and `chr()` to convert to ascii
#for the markdown, prefix the code sections with 'd', 'b', 'h', or 'a'

def hex_print(dec_bytes):
    return ' '.join(hex(byte)[2:] for byte in dec_bytes)

def organize_bytes(filepath):
    with open(filepath, 'rb') as myFile:
        file_bytes = myFile.read()
    if file_bytes[:8] != b'\x89PNG\r\n\x1a\n':
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
    
    return chunks


def write_analysis(filepath):

    with open(filepath, 'rb') as myFile:
        file_bytes = myFile.read()

    int_bytes = tuple(byte for byte in file_bytes) #list of decimal integer values for each byte in the file
    str_bytes = tuple(str(byte) for byte in int_bytes) #TODO check if uses of this actually get the math right
    byte_index = 0
    chunk_index = 0

    #begin writing to the markdown file
    with open('png_bytes_analysis.md', 'w') as md_output:

        #PNG file header
        md_output.write(f'### PNG file signature\n- Decimal: `{" ".join(str_bytes[:8])}`\n')
        string_soon = []
        for byte in int_bytes[:8]:
            if byte in range(32, 127):
                string_soon.append(chr(byte))
            else:
                string_soon.append(hex(byte))
        md_output.write(f'- Ascii/hex: `{" ".join(string_soon)}`\n')
        byte_index += 8

        #go through all chunks
        while byte_index < len(int_bytes):
            chunk_index += 1
            md_output.write(f'### Chunk {chunk_index}\n')

            #chunk length
            hex_len = hex_print(int_bytes[byte_index:byte_index+4])
            dec_len = int(''.join(str_bytes[byte_index:byte_index+4]))
            byte_index += 4
            md_output.write(f'- **Chunk length:** *h* `{hex_len}`, or {dec_len} bytes.\n')

            #chunk type
            try: #TODO remove this try thing
                name = ''.join(chr(byte) for byte in int_bytes[byte_index:byte_index+4])
                byte_index += 4
                md_output.write(f'- **Chunk type:** *a* `{name}`\n')
            except UnicodeEncodeError:
                print('this ain\'t a chunk title!')

            #chunk data
            data = hex_print(int_bytes[byte_index:byte_index + dec_len])
            byte_index += dec_len
            md_output.write(f'- **Chunk data:**  \n*h* `{data}`\n')

            #chunk CRC checksum
            crc = hex_print(int_bytes[byte_index:byte_index + 4])
            byte_index += 4
            md_output.write(f'- **Chunk CRC:** *h* `{crc}`\n')

        #attach image at bottom
        md_output.write(f'## The PNG image:\n![the png image]({filepath})')


#write_analysis('8x8.png')
print(organize_bytes('8x8.png'))