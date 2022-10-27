#!/usr/bin/env python3

"""Selection sort.

Works like GNU's `sort` util.

This script reads, sorts and prints elements that can be sorted.
An element can be sorted if it implements a comparison operation.

Selection sort overview: https://en.wikipedia.org/wiki/Selection_sort
"""

from utils import read_sort_print
from sorts import selection_sort

if __name__ == "__main__":
    read_sort_print(selection_sort)
