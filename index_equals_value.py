#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from bisect import bisect_left, bisect_right
from operator import sub


def indexEqualsValue(array: List[int]):
    if not array:
        return -1
    index = bisect_left(list(map(sub, array, list(range(len(array))))), 0)
    if index >= len(array):
        return -1
    if index == array[index]:
        return index
    return -1



if __name__ == "__main__":
    array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    print(indexEqualsValue(array))
