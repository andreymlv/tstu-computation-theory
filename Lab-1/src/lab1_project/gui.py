#!/usr/bin/env python3

"""GUI application shows how many time is need to sort lists of numbers.

Usage: gui.py
"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from random import sample
from utils import execution_time_seconds
from sorts import selection_sort, insertion_sort


def generate_random_sequences(size, step) -> list[list]:
    """
    >>> generate_random_sequences(100, 12)
    [
        [12 random values from -size to size], 
        [24 random values from -size to size],
        ...,
        [96 random values from -size to size]
    ]
    """
    result: list[list] = []
    for i in range(step, size, step):
        result.append(sample(range(-size, size), i))
    return result


def time_for_sort(input: list[list], strategy_sort: Callable[[list], list]) -> list[float]:
    result: list[float] = []
    for l in input:
        result.append(execution_time_seconds(strategy_sort, l))
    return result


if __name__ == '__main__':
    size = 1000
    x = np.linspace(0, size, size)

    data: list[list] = generate_random_sequences(size+1, 1)
    time_selection: list[float] = time_for_sort(data, selection_sort)
    time_insertion: list[float] = time_for_sort(data, insertion_sort)
    time_built_in: list[float] = time_for_sort(data, sorted)

    _, ax_built_in = plt.subplots()
    ax_selection = ax_built_in.twinx()
    ax_insertion = ax_built_in.twinx()
    ax_built_in.plot(x, time_built_in, color='blue', label='sorted()')
    ax_selection.plot(x, time_selection, color='red', label='selection()')
    ax_insertion.plot(x, time_insertion, color='green', label='insertion()')
    ax_built_in.legend(loc=2)
    ax_selection.legend(loc=4)
    ax_insertion.legend(loc=5)
    plt.show()
