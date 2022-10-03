#!/usr/bin/env python3

"""GUI application shows how much time is need to sort lists of numbers.

Usage: gui.py
"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from utils import execution_time_seconds
from sorts import selection_sort, insertion_sort


def generate_random_sequences(data, step=1) -> list[list]:
    result: list[list] = []
    for i in range(step, size, step):
        temp = data[0:i]
        np.random.shuffle(temp)
        result.append(temp)
    return result


def time_for_sort(data: list[list], strategy_sort: Callable[[list], list]) -> list[float]:
    result: list[float] = []
    for d in data:
        result.append(execution_time_seconds(strategy_sort, d))
    return result


if __name__ == '__main__':
    size = 1024
    x = np.linspace(0, size, size - 1)

    # time_selection = time_for_sort(generate_random_sequences(x.copy()), selection_sort)
    time_insertion = time_for_sort(generate_random_sequences(x.copy()), insertion_sort)
    time_built_in = time_for_sort(generate_random_sequences(x.copy()), sorted)

    plt.plot(x, time_built_in, label='built-in sorted()')
    plt.plot(x, time_insertion, label='insertion sort')
    # plt.plot(x, time_selection, label='selection sort')
    plt.grid(True)
    plt.xlabel('elements')
    plt.ylabel('time')
    plt.legend(title='Sorts:')
    plt.title('Sorts comparison')
    plt.show()
