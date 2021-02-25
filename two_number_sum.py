#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def twoNumberSum(array: List[int], targetSum: int):
    arrayMap = dict.fromkeys(array)
    for value in array:
        if (targetSum - value) != value and (targetSum - value) in arrayMap:
            return [value, targetSum - value]
    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))
