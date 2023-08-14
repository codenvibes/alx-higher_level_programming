#!/usr/bin/python3
# Author: Terrence M.K
# File: 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples"""
    element1 = tuple_a + (0, 0)
    element2 = tuple_b + (0, 0)

    results1 = 0
    results2 = 0

    results1 += element1[0] + element2[0]
    results2 += element1[1] + element2[1]

    return (results1, results2)
