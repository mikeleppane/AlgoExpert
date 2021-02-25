#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import defaultdict

def tournamentWinner(competitions: List[List[str]], results: List[int]):
    poinst = {}
    for competition, result in zip(competitions, results):
        team = competition[abs(result - 1)]
        if team not in poinst:
            poinst[team] = 3
        else:
            poinst[team] += 3
    return sorted(poinst.items(), key=lambda item: item[1], reverse=True)[0][0]


if __name__ == "__main__":
    competitions = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [0, 1, 1]
    print(tournamentWinner(competitions, results))
