#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random
from collections import deque


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # assume values are unique.  fix later if this is not correct.

    def insert(self, root, node):
        if not root:
            return

        if node.val < root.val:
            if root.left:
                self.insert(root.left, node)
            else:
                root.left = node
            return

        if node.val > root.val:
            if root.right:
                self.insert(root.right, node)
            else:
                root.right = node
            return

        raise ValueError("oops, values can be dups")

    def serialize(self, root):
        """Encodes a tree to a single string.
        """

        d = deque()
        serialization = []
        if root:
            d.append(root)
        while len(d) > 0:
            n = d.popleft()
            serialization.append(str(n.val))
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)

        s = "[" + ','.join(serialization) + "]"
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """

        s = data.strip("[]")
        nums = None
        if s:
            nums = s.split(",")

        if not nums:
            return None

        nums = list(map(int, nums))

        root = TreeNode(nums[0])
        for n in nums[1:]:
            node = TreeNode(n)
            self.insert(root, node)

        return root


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