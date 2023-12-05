#!/usr/bin/python3
# AUTH: codenvibes
"""
This module provides a function to find a peak in a list of integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of integers.

    Parameters:
    - list_of_integers (list): A list of integers.

    Returns:
    - int or None: The peak value if found, None if the list is empty.
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])