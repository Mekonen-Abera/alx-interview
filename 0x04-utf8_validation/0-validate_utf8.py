#!/usr/bin/python3
"""UTF-8 Encoding Validation"""

def count_leading_ones(num):
    """Returns the number of leading 1 bits in the binary representation."""
    leading_ones = 0
    mask = 1 << 7  # Start with the highest bit
    while mask & num:
        leading_ones += 1
        mask >>= 1  # Shift mask right to check the next bit
    return leading_ones

def is_valid_utf8(data):
    """Checks if the given data set represents valid UTF-8 encoding."""
    bytes_remaining = 0  # Number of bytes expected for the current character
    for byte in data:
        if bytes_remaining == 0:
            bytes_remaining = count_leading_ones(byte)
            # Check for valid UTF-8 byte formats
            if bytes_remaining == 0:
                continue  # 1-byte character (0xxxxxxx)
            if bytes_remaining == 1 or bytes_remaining > 4:
                return False  # Invalid byte count
        else:
            # Ensure the byte follows the 10xxxxxx format
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        bytes_remaining -= 1  # Decrease the count of remaining bytes
    return bytes_remaining == 0  # Ensure all bytes are accounted for

