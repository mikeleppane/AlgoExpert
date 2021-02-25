a#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node_depths = []


def _find_node_depth(tree: BinaryTree, running_node_depth: int):
    if tree.left is None and tree.right is None:
        return
    if tree.left is not None:
        node_depths.append(running_node_depth + 1)
        _find_node_depth(tree.left, running_node_depth + 1)
    if tree.right is not None:
        node_depths.append(running_node_depth + 1)
        _find_node_depth(tree.right, running_node_depth + 1)


def nodeDepths(root: BinaryTree):
    running_node_depth = 0
    _find_node_depth(root, running_node_depth)
    return sum(node_depths)


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    actual = nodeDepths(root)
