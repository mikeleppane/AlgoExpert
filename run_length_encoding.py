#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def runLengthEncoding(string: str) -> str:
    strings = list(string)
    encodings = ""
    index = 0
    while index < len(strings):
        char = strings[index]
        count = 0
        while index < len(strings) and char == strings[index] and count < 9:
            count += 1
            index += 1
        encodings += f"{str(count) + char}"
    return encodings

if __name__ == "__main__":
    string = "AABBCC"
    print(runLengthEncoding(string))
