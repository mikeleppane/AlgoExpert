#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from bisect import bisect_left

def findThreeLargestNumbers(array: List[int]):
    three_largest_numbers = array[0:3]
    three_largest_numbers.sort()
    for value in array[3:]:
        new_index = bisect_left(three_largest_numbers, value)
        if new_index:
            three_largest_numbers.pop(0)
            three_largest_numbers.insert(new_index - 1, value)
    return three_largest_numbers


if __name__ == "__main__":
    array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
    print(findThreeLargestNumbers(array))
