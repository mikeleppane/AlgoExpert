#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def moveElementToEnd(array: List[int], toMove: int):
    how_many_elements = array.count(toMove)
    array = [value for value in array if value != toMove]
    array.extend([toMove] * how_many_elements)
    return array


if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array, toMove))
