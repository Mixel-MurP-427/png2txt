def view_png_bytes(file_path):
    try:
        with open(file_path, 'rb') as f:
            png_bytes = f.read()
            # Print the hexadecimal representation of the bytes
            for i, byte in enumerate(png_bytes):
                print(f"{byte:02x}", end=" ")
                if (i + 1) % 16 == 0:  # Newline every 16 bytes for readability
                    print()
            print()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_image.png' with the actual path to your PNG file
view_png_bytes("C:/Users/jodim/OneDrive/Documents/Connor_Coding/portal2-voice-lines/Portal2_lines/64x64_Portal_favicon.png")