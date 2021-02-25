#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def classPhotos(redShirtHeights: List[int], blueShirtHeights: List[int]):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    max_blue = max(blueShirtHeights)
    max_red = max(redShirtHeights)
    if max_blue > max_red:
        return all((blue > red for blue, red in zip(blueShirtHeights, redShirtHeights)))
    else:
        return all((blue < red for blue, red in zip(blueShirtHeights, redShirtHeights)))


if __name__ == "__main__":
    reds = [6]
    blues = [6]
    print(classPhotos(reds, blues))
