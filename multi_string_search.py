#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def multiStringSearch(bigString: str, smallStrings: List[str]):
    matches = [False] * len(smallStrings)
    for index, small_string in enumerate(smallStrings):
        small_string_length = len(small_string)
        for bs_index in range(len(bigString)):
            if bigString[bs_index:bs_index + small_string_length] == small_string:
                matches[index] = True
                break
    return matches


if __name__ == "__main__":
    big_string = "this is a big string"
    small_strings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    print(multiStringSearch(big_string, small_strings))
