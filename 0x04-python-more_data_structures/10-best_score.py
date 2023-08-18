#!/usr/bin/python3
# Author: terrence M.K
# File: 10-best_score.py
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary is None or a_dictionary == {}:
        return None

    max_value = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_value
