#!/usr/bin/python3
"""
UTF8 - Validation
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    # Number of bytes in the current character
    num_bytes = 0

    for num in data:
        # Check if the current number is a valid leading byte
        if num_bytes == 0:
            # Count the number of leading ones (MSB)
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # If no leading ones, it's a single-byte character
            if num_bytes == 0:
                continue

            # Invalid leading byte
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the current number is a valid continuation byte
            if not (num >> 6) == 0b10:
                return False

        # Decrease the remaining bytes to process for the current character
        num_bytes -= 1

    # All bytes were validated
    return num_bytes == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
