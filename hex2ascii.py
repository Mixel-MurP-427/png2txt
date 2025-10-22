hex_string = "48656c6c6f20576f726c64"  # Hexadecimal representation of "Hello World"

# Convert hex string to bytes
byte_data = bytes.fromhex(hex_string)

# Decode bytes to ASCII string
ascii_string = byte_data.decode("ascii")

print(ascii_string)