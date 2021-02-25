#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


branch_sums = list()

def calculate_branch_sum(node: BinaryTree, branch_sum: int):
    branch_sum += node.value
    if isinstance(node.left, BinaryTree):
        calculate_branch_sum(node.left, branch_sum)
    if isinstance(node.right, BinaryTree):
        calculate_branch_sum(node.right, branch_sum)
    if node.left is None and node.right is None:
        branch_sums.append(branch_sum)
        return

def branchSums(root):
    branch_sum = root.value
    if isinstance(root.left, BinaryTree):
        calculate_branch_sum(root.left, branch_sum)
    if isinstance(root.right, BinaryTree):
        calculate_branch_sum(root.right, branch_sum)

if __name__ == "__main__":
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    branchSums(tree)
    print(branch_sums)
