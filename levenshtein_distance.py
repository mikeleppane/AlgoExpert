#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def levenshteinDistance(str1: str, str2: str):
    chars_1 = list(str1)
    chars_2 = list(str2)
    edits = 0
    if not chars_1:
        return len(chars_2)
    if not chars_2:
        return len(chars_1)
    for index, char in enumerate(chars_2):
        if index < len(chars_1):
            if char == chars_1[index]:
                continue
            elif char in chars_1 and char != chars_1[index]:
                edits += 1
            elif char not in chars_1:
                edits += 1
    if len(chars_1) > len(chars_2):
        edits += len(chars_1) - len(chars_2)
    return edits


if __name__ == "__main__":
    str_1 = "abc"
    str_2 = "yabd"
    print(levenshteinDistance(str_1, str_2))
