def custom_ascii(letter):
    # tipo
    if not isinstance(letter, str):
        raise TypeError("input must be a string")

    # lunghezza
    if len(letter) != 1:
        raise ValueError("input must be a single character")

    ascii_code = ord(letter)

    # ASCII stampabile
    if ascii_code < 32 or ascii_code > 126:
        raise ValueError("character is not a printable ASCII character")

    return ascii_code