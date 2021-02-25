#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def traverse_to_list(depth: int, array: List[int]) -> int:
    sum = 0
    for value in array:
        if isinstance(value, list):
            sum += traverse_to_list(depth + 1, value)
        else:
            sum += value
    return depth * sum


def productSum(array: List[int]):
    sum = 0
    for value in array:
        if isinstance(value, list):
            sum += traverse_to_list(2, value)
        else:
            sum += value
    return sum


if __name__ == "__main__":
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print(productSum(array))
