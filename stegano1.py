import os
import sys

def extract_lsb_bytes(input_file):
    with open(input_file, 'rb') as f:
        f.seek(100)
        lsb_bytes = []
        byte = f.read(1)
        while byte:
            lsb = byte[-1] & 0x01
            lsb_bytes.append(str(lsb))
            byte = f.read(1)

    # Convert indicator_sequence to a list of strings for comparison
    indicator_sequance = [str(bit) for bit in [1, 0, 1, 0, 0, 1, 0, 1] * 8]

    # Corrected the range to iterate over the entire lsb_bytes
    for i in range(len(lsb_bytes) - len(indicator_sequance) + 1):
        compare = lsb_bytes[i:i+len(indicator_sequance)]
        if compare == indicator_sequance:
            size_bytes = [int(bit) for bit in lsb_bytes[64:91]]
            reverse_size = size_bytes[::-1]
            binary_string = ''.join(map(str, reverse_size))
            decimal_size = int(binary_string, 2)
            conversion_data = ''.join(lsb_bytes[91:91 + decimal_size * 8])
            data = bytes(
                int(conversion_data[i:i+8][::-1], 2)
                for i in range(0, len(conversion_data), 8)
            )
            output_file = "result.pdf"
            with open(output_file, "wb") as f:
                f.write(data)
            return decimal_size

    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: ./your_prog input_file output_file")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    decimal_size = extract_lsb_bytes(input_file)

    if decimal_size is not None:
        print("Hidden data extracted successfully.")
    else:
        print("No hidden data found.")
    # input_file = '/Users/siddarthboreddy/Documents/Semester2/Compsec/PA2/aliceStego.bmp'
    # decimal_size = extract_lsb_bytes(input_file)

    if decimal_size is not None:
        print("Hidden data extracted successfully.")
    else:
        print("No hidden data found.")

if __name__ == '__main__':
    main()
