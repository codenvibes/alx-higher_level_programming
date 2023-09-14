#!/usr/bin/python3
# Auth: codenvibes
"""
This module defines a function for reading and printing the contents
of a file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        filename (str): The name of the file to be read. Defaults to an
        empty string.

    Returns:
        None

    This function opens the specified file, reads its contents, and prints
    them to the standard output.

    Example:
        >>> read_file("example.txt")
        This is an example file.
        It contains some text.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
