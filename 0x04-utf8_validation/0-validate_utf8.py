#!/usr/bin/python3
"""
UTF8 - Validation
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num >> 6) == 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
