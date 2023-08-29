#!/usr/bin/python3
# Auth: Terrence M.K
# File: 3-safe_print_division.py
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
