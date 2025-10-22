def read_png_bytes(file_path):
    output = ''

    with open(file_path, 'rb') as myFile:
        png_bytes = myFile.read()
    # Print the hexadecimal representation of the bytes
    for i, byte in enumerate(png_bytes):
        output += f"{byte:02x} "
        if (i + 1) % 16 == 0:  # Newline every 16 bytes for readability
            output += '\n'

    return output
    


# Replace 'your_image.png' with the actual path to your PNG file
a_png_path = 'pixil-frame-0.png'
other_png_path = "C:/Users/jodim/OneDrive/Documents/Connor_Coding/portal2-voice-lines/Portal2_lines/64x64_Portal_favicon.png"
text = read_png_bytes(a_png_path)
with open('hex_bytes.txt', 'w') as myFile:
    myFile.write(text)