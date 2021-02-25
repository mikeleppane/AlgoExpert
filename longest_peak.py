#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def longestPeak(array: List[int]):
    array_length = len(array)
    if array_length < 3:
        return 0
    longest_peak = 0
    current_index = 1
    while current_index < array_length - 1:
        is_peak = array[current_index - 1] < array[current_index] and array[current_index] > array[current_index + 1]
        if is_peak:
            peak = [array[current_index]]
            down_index = current_index - 1
            up_index = current_index + 1
            current_up_value = peak[0]
            current_down_value = peak[0]
            while array[down_index] < current_down_value and down_index >= 0:
                current_down_value = array[down_index]
                down_index -= 1
                peak.append(current_down_value)
            while up_index < len(array) and array[up_index] < current_up_value:
                current_up_value = array[up_index]
                up_index += 1
                peak.append(current_up_value)
            longest_peak = max(longest_peak, len(peak))
            print(longest_peak)
            current_index = up_index
            #if current_index == array_length - 1:
            #    return longest_peak
        else:
            current_index += 1
    return longest_peak



if __name__ == "__main__":
    array = [5, 4, 3, 2, 1, 2, 1]
    longestPeak(array)
