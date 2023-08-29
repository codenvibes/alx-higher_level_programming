#!/usr/bin/python3
# Auth: Terrence M.K
# File: 0-safe_print_list.py
def safe_print_list(my_list=[], x=0):
    try:
        number_of_elements = 0
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            number_of_elements += 1
    except IndexError:
        pass
    finally:
        print()
        return (number_of_elements)
