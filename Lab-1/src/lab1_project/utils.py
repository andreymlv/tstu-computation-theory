from sys import stdin
from timeit import timeit
from typing import Callable


def read_list_stdin() -> list[int]:
    input: list[int] = []
    for line in stdin:
        input.append(int(line))
    return input


def print_list_stdout(sequence: list) -> None:
    for x in sequence:
        print(x)


def read_sort_print(sort_strategy: Callable[[list], list]) -> None:
    print_list_stdout(sort_strategy(read_list_stdin()))


def execution_time_seconds(function: Callable, args: list) -> float:
    return timeit(lambda: function(args), number=1)
