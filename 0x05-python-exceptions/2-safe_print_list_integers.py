#!/usr/bin/python3
# Auth: Terrence M.K
# File: 2-safe_print_list_integers.py
def safe_print_list_integers(my_list=[], x=0):
    try:
        number_of_elements = 0
        for index in range(x):
            if type(my_list[index]) is int:
                print("{:d}".format(my_list[index]), end="")
                number_of_elements += 1
    except (ValueError):
        pass

    print()
    return (number_of_elements)
