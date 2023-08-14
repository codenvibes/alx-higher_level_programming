#!/usr/bin/python3
# Author: Terrence M.K
# File: 0-print_list_integer.py
# A function that prints all integers of a list

def print_list_integer(my_list=[]):
    list_len = len(my_list)
    for i in range(list_len):
        print("{:d}".format(my_list[i]))
