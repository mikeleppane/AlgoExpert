#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

def check_sum_bruteforce(numbers, n):
    sums = []
    for number in numbers:
        for sum_ in sums[:]:
            new_sum = sum_ + number
            if new_sum == n:
                return True
            sums.append(new_sum)
        sums.append(number)
    return False


def nonConstructibleChange(coins: List[int]):
    coins.sort()
    starting_coin = 1
    while True:
        if starting_coin not in coins:
            if not check_sum_bruteforce(coins, starting_coin):
                return starting_coin
        starting_coin += 1

if __name__ == "__main__":
    coins = [1,2,5]
    print(nonConstructibleChange(coins))
