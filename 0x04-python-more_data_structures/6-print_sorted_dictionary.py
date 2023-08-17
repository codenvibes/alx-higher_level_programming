#!/usr/bin/python3
# Author: Terrence M.K
# File: 6-print_sorted_dictionary.py
def print_sorted_dictionary(a_dictionary):
    """Prints a sorted dictionary"""
    sorted_items = sorted(a_dictionary.items())

    for key, value in sorted_items:
        print(key, ":", value)
