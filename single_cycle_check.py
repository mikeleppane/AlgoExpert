#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def get_next_index(current_index: int, array: List[int]) -> int:
    next_index = array[current_index]
    if next_index < 0:
        steps = [-1] * abs(next_index)
    else:
        steps = [1] * abs(next_index)
    for step in steps:
        current_index += step
        if current_index >= len(array):
            current_index = 0
        elif current_index < 0:
            current_index = len(array) - 1
    return current_index

def hasSingleCycle(array: List[int]) -> bool:
    starting_index = 0
    visited_indices = set()
    visited_indices.add(0)
    current_index = 0
    while True:
        current_index = get_next_index(current_index, array)
        if current_index == starting_index:
            return len(visited_indices) == len(array)
        else:
            if current_index in visited_indices:
                return False
        visited_indices.add(current_index)

if __name__ == "__main__":
    array = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycle(array))
