#!/usr/bin/python3
# Author: Terrence M.K
# File: 2-uniq_add.py
def uniq_add(my_list=[]):
    """Add all unique values in a list"""
    my_set = set(my_list)
    return (sum(my_set))
