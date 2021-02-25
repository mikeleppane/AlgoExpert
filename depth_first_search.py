#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Node:
    def __init__(self, name):
        self.children: List[Node] = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array: List[str]):
        self.array = list(array)
        self.array.append(self.name)
        for node in self.children:
            self._search(node)
        return self.array

    def _search(self, node: "Node"):
        self.array.append(node.name)
        for child in node.children:
            self._search(child)


if __name__ == "__main__":
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    actual = graph.depthFirstSearch([])
    print(actual == expected)
