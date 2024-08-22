#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""

    # keeps track of how many bytes we expect for the current UTF-8 character
    num_bytes = 0

    # check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # mask is initialized to 10000000 (128 in decimal)
        # to start checking the leading bits of the current byte.
        mask = 1 << 7

        # we're at the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1
            while mask & num:
                # how many bytes long the UTF-8 character is supposed to be.
                num_bytes += 1
                # count how many leading 1s there are by using the mask and
                # shifting it right until the mask no longer matches a 1.
                mask >>= 1

            # 1-byte character (0xxxxxxx), so we move on to the next byte.
            if num_bytes == 0:
                continue

            # we're in the middle of checking a multi-byte character.
            # The current byte should be 1 and the second bit should be 0.
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check if the next byte is of the form 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If num_bytes is not 0, then there are missing bytes
    return num_bytes == 0
