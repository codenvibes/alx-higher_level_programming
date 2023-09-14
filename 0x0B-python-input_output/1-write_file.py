#!/usr/bin/python3
# Auth: codenvibes
"""
This module provides a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there is an issue writing to the file.

    Example:
        To write "Hello, World!" to a file named "example.txt":
        >>> write_file("example.txt", "Hello, World!")

    Note:
        This function will create the file if it doesn't exist, and it will
        overwrite the file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
