#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def minimumWaitingTime(queries: List[int]):
    if not queries:
        return 0
    queries.sort()
    total_waiting_time = 0
    for index in range(1, len(queries)):
        total_waiting_time += sum(queries[:index])
    return total_waiting_time


if __name__ == "__main__":
    queries = [3, 2, 1, 2, 6]
    print(minimumWaitingTime(queries))
