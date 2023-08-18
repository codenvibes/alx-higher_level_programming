#!/usr/bin/python3
# Author: Terrence M.K
# File: 9-multiply_by_2.py
def multiply_by_2(a_dictionary):
    """return a new dictionary all values multiplied by 2"""
    new_dictionary = a_dictionary.copy()
    for value in new_dictionary:
        new_dictionary[value] *= 2
    return new_dictionary
