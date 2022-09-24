#!/usr/bin/env python3

"""Generate and print random numbers in some range.

Works like GNU's `shuf` util.

Usage: random_numbers.py -i LO-HI -n count

-i, --input-range=LO-HI
        treat each number LO through HI as an input line

-n, --head-count=COUNT
        output at most COUNT lines
"""

from random import sample
from sys import argv
from utils import print_list_stdout

if __name__ == '__main__':
    if (len(argv) != 4):
        raise RuntimeError("Usage: " + argv[0] + " min max count")
    min: int = int(argv[1])
    max: int = int(argv[2])
    count: int = int(argv[3])
    assert min <= max
    assert count > 0 and count <= max - min
    print_list_stdout(sample(range(min, max), count))
