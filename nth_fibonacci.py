#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def getNthFib(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return sum([getNthFib(n-1), getNthFib(n-2)])


if __name__ == "__main__":
    n = 8
    print(getNthFib(n))
