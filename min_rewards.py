#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def minRewards(scores: List[int]):
    idx_min = scores.index(min(scores))
    left_index = idx_min
    right_index = idx_min
    rewards = 0
    current_left_index = left_index
    while left_index > 0:
        while left_index > 0 and scores[left_index - 1] > scores[left_index]:
            left_index -= 1
        if current_left_index != left_index:
            rewards += sum(range(abs(current_left_index - left_index) + 2))
            current_left_index = left_index
        while left_index > 0 and scores[left_index - 1] < scores[left_index]:
            left_index += 1
        if current_left_index != left_index:
            rewards += sum(range(abs(current_left_index - left_index) + 1))
            current_left_index = left_index
    if rewards > 0:
        rewards -= 1
    current_right_index = right_index
    print(rewards)
    while right_index < len(scores) - 1:
        while right_index < len(scores) - 1 and scores[right_index + 1] > scores[right_index]:
            right_index += 1
        if current_right_index != right_index:
            rewards += sum(range(abs(current_right_index - right_index) + 2))
            current_right_index = right_index
        print(rewards)
        while right_index < len(scores) - 1 and scores[right_index + 1] < scores[right_index]:
            right_index += 1
        if current_right_index != right_index:
            rewards += sum(range(abs(current_right_index - right_index) + 1))
            current_right_index = right_index
        print(rewards)
    return rewards

if __name__ == "__main__":
    scores = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
    print(minRewards(scores))
