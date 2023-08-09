#!/usr/bin/python3
def islower(i):
    """Check for lowercase characters."""
    if ord(i) >= 97 and ord(i) <= 122:
        return True
    else:
        return False
