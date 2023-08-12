#!/usr/bin/python3
# Author: Terrence M.K
# File: 100-my_calculator.py

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv) - 1

    if argc == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        operators = ['+', '-', '*', '/']

        if operator in operators:
            if operator == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            if operator == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            if operator == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            if operator == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
