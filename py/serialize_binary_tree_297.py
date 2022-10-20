#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random
from collections import deque
import pickle


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DecoratedTreeNode:
    def __init__(self, x):
        self.val = x
        self.order = None
        self.left = None
        self.right = None


def make_test_tree(n):
    # make a complete binary tree with n nodes.
    arr = []
    for i in range(n + 1):
        node = TreeNode(i)
        arr.append(node)

    for i in range(1, n + 1):
        li = 2 * i
        ri = 2 * i + 1

        if li < n + 1:
            arr[i].left = arr[li]
        if ri < n + 1:
            arr[i].right = arr[ri]

    return arr[1]


class Codec:

    # assume values are unique.  fix later if this is not correct.

    def insert(self, root, node):
        if not root:
            return

        if node.order < root.order:
            if root.left:
                self.insert(root.left, node)
            else:
                root.left = node
            return

        if node.order > root.order:
            if root.right:
                self.insert(root.right, node)
            else:
                root.right = node
            return

    def clone_original(self, root):
        if root is None:
            return None

        newnode = DecoratedTreeNode(root.val)
        newnode.left = self.clone_original(root.left)
        newnode.right = self.clone_original(root.right)

        return newnode

    def clone_decorated(self, root):
        if root is None:
            return None

        newnode = TreeNode(root.val)
        newnode.left = self.clone_decorated(root.left)
        newnode.right = self.clone_decorated(root.right)

        return newnode

    def decorate(self, root, initial):
        if not root:
            return initial

        counter = self.decorate(root.left, initial)
        root.order = counter
        counter = self.decorate(root.right, counter + 1)

        return counter

    def serialize(self, root):
        """Encodes a tree to a single string.
        """

        dtree = self.clone_original(root)
        self.decorate(dtree, 1)

        d = deque()
        serialization = []
        if dtree:
            d.append(dtree)
        while len(d) > 0:
            n = d.popleft()
            serialization.append((n.val, n.order))
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)

        return pickle.dumps(serialization)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """

        serialization = pickle.loads(data)
        if not serialization:
            return None

        toop = serialization[0]
        root = DecoratedTreeNode(toop[0])
        root.order = toop[1]
        for d in serialization[1:]:
            node = DecoratedTreeNode(d[0])
            node.order = d[1]
            self.insert(root, node)

        new_root = self.clone_decorated(root)

        return new_root


def solution():
    pass


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [1, 7, 2, 4, 6, 8, 0]
        root = TreeNode(arr[0])
        codec = Codec()

        for a in arr[1:]:
            node = TreeNode(a)
            codec.insert(root, node)

        print(root.val)

        result = codec.serialize(root)
        print(result)

        new_root = codec.deserialize(result)
        print(new_root.val)

    def test_2(self):
        arr = []
        root = None
        codec = Codec()
        result = codec.serialize(root)
        print(result)

        new_root = codec.deserialize(result)
        print(new_root)

    def test_3(self):
        ttree = make_test_tree(12)
        codec = Codec()

        pkl = codec.serialize(ttree)
        serialization = pickle.loads(pkl)
        pprint(serialization)

        dser = codec.deserialize(pkl)

        tree_copy = codec.clone_decorated(dser)

        print(tree_copy.val)
        print(tree_copy.left.val)

    def test_4(self):
        root = make_test_tree(12)
        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(root))

        print(ans.val)
        print(ans.left.val)