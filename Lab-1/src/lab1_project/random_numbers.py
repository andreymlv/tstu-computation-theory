#!/usr/bin/env python3
from random import sample
from sys import argv
from utils import print_list_stdout


def main(argv: list[str]) -> None:
    if (len(argv) != 4):
        raise RuntimeError("Usage: " + argv[0] + " min max count")
    min: int = int(argv[1])
    max: int = int(argv[2])
    count: int = int(argv[3])
    assert min <= max
    assert count > 0 and count <= max - min
    print_list_stdout(sample(range(min, max), count))


if __name__ == '__main__':
    main(argv)
