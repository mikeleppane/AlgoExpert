#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def absolute_difference(num1: int, num2: int) -> int:
    return abs(num1 - num2)


def smallest_difference(array_one: List[int], array_two: List[int]):
    array_one.sort()
    array_two.sort()
    array_one_index = 0
    array_two_index = 0
    min_difference = float("inf")
    output_values = []
    while array_one_index < len(array_one) and array_two_index < len(array_two):
        value_1 = array_one[array_one_index]
        value_2 = array_two[array_two_index]
        abs_difference = absolute_difference(value_1, value_2)
        if absolute_difference(value_1, value_2) <= min_difference:
            min_difference = abs_difference
            output_values = [value_1, value_2]
        if min_difference == 0:
            return output_values
        if value_2 < value_1:
            array_two_index += 1
        if value_1 < value_2:
            array_one_index += 1
    return output_values


if __name__ == "__main__":
    array_one = [-1, 5, 10, 20, 28, 3]
    array_two = [26, 134, 135, 15, 17]
    print(smallest_difference(array_one, array_two))
