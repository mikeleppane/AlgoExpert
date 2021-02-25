#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def threeNumberSum(array: List[int], targetSum: int):
    sums = list()
    for index, value in enumerate(array):
        running_sum = targetSum - value
        for second_value in array:
            if value != second_value:
                third_value = running_sum - second_value
                if third_value in array and third_value not in (value, second_value):
                    new_sum = [value, second_value, third_value]
                    new_sum.sort()
                    if new_sum not in sums:
                        sums.append(new_sum)

    return sorted(sums, key=lambda item: (item[0],item[1], item[2]))


if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    target_sum = 0
    print(threeNumberSum(array, target_sum))
