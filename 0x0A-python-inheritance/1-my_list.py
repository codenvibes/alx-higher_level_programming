#!/usr/bin/python3
"""
This module defines a custom list class.
"""


class MyList(list):
    """
    A custom list class that inherites from the built-in list class.

    This class adds a method to print the elements of the list in sorted
    order.
    """
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method creates a copy of the list, sorts the copy, and then
        prints it.
        """
        copy_of_list = self[:]
        print(sorted(copy_of_list))
