#!/usr/bin/python3
"""
Author: Terrence M.K
File: 3-infinite_add.py
"""
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = 0

    for i in range(1, argc + 1):
        result += int(sys.argv[i])
    print(result)
