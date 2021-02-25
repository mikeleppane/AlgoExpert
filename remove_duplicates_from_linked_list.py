#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def removeDuplicatesFromLinkedList(linkedList: LinkedList):
    current_node = linkedList
    while True:
        current_value = current_node.value
        next_node = current_node.next
        while next_node is not None and current_value == next_node.value:
            next_node = next_node.next
        current_node.next = next_node
        current_node = next_node
        if next_node is None:
            break
    return linkedList

if __name__ == "__main__":
    test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
    expected = LinkedList(1).addMany([3, 4, 5, 6])
    actual = removeDuplicatesFromLinkedList(test)
    print(f"expected: {expected.getNodesInArray()}")
    print(f"actual: {actual.getNodesInArray()}")
