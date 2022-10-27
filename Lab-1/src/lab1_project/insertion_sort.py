#!/usr/bin/env python3

"""Insertion sort.

Works like GNU's `sort` util.

This script reads, sorts and prints elements that can be sorted.
An element can be sorted if it implements a comparison operation.

Insertion sort overview: https://en.wikipedia.org/wiki/Insertion_sort
"""

from utils import read_sort_print
from sorts import insertion_sort

if __name__ == "__main__":
    read_sort_print(insertion_sort)
