#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _find_closest_value(tree: BST, target: int, closest_value: float):
    if tree.value == target:
        return tree.value
    if abs(closest_value - target) > abs(tree.value - target):
        closest_value = tree.value
    if tree.left is not None and tree.right is not None:
        if target > tree.value:
            tree.left = None
            closest_value = _find_closest_value(tree.right, target, closest_value)
        elif target < tree.value:
            tree.right = None
            closest_value = _find_closest_value(tree.left, target, closest_value)
    if tree.left is not None and tree.right is None:
        closest_value = _find_closest_value(tree.left, target, closest_value)
    if tree.left is None and tree.right is not None:
        closest_value = _find_closest_value(tree.right, target, closest_value)
    return closest_value


def findClosestValueInBst(tree: BST, target: int):
    closest_value = float("inf")
    _find_closest_value(tree, target, closest_value)


if __name__ == "__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    expected = 13
    findClosestValueInBst(root, 12)
