#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def firstDuplicateValue(array: List[int]):
    found_duplicates = {}
    for value in array:
        if value not in found_duplicates:
            found_duplicates[value] = 1
        else:
            return value
    return -1


if __name__ == "__main__":
    array = [7, 6, 5, 3, 6, 4, 3, 5, 2]
    print(firstDuplicateValue(array))
