#!/usr/bin/python3
# Author: Terrence M.K
# File: 2-replace_in_list.py
# A function that replaces an element of a list

def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < (len(my_list)):
        my_list[idx] = element
    return (my_list)
