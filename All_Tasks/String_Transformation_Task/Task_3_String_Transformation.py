def transform_string(s):
    length = len(s)
    
    if length % 15 == 0:
        reversed_string = s[::-1]
        ascii_codes = ' '.join(str(ord(c)) for c in reversed_string)
        return ascii_codes
    elif length % 5 == 0:
        ascii_codes = ' '.join(str(ord(c)) for c in s)
        return ascii_codes
    elif length % 3 == 0:
        reversed_string = s[::-1]
        return reversed_string
    else:
        return s

# Example usage:
print(transform_string("Hamburger"))
print(transform_string("Pizza"))
print(transform_string("Chocolate Chip Cookie"))