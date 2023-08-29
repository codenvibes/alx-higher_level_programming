#!/usr/bin/python3
# Auth: Terrence M.K
# File: 1-safe_print_integer.py
def safe_print_integer(value):
    try:
        value = int(value)
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
