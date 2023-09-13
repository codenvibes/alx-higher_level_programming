#!/usr/bin/python3
# Auth: Terrence M.K
# File: 1-my_list.py
"""
This module defines a custom list class.
"""


class MyList(list):
    """
    A custom list class that inherites from the built-in list class.
    """
    
    def print_sorted(self):
        """
        This method creates a copy of the list, sorts the copy, and then
        prints it.
        """
        print(sorted(self))
