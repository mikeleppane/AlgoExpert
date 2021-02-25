#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def isValidSubsequence(array: List[int], sequence: List[int]):
    running_index = 0
    for index, value in enumerate(sequence):
        if value not in array[running_index:]:
            return False
        if value == array[running_index]:
            running_index += 1
            continue
        while array[running_index] != value:
            running_index += 1
    return True


if __name__ == "__main__":
    array = [1, 1, 6, 1]
    sequence = [1, 1, 1, 6]
    print(isValidSubsequence(array, sequence))
