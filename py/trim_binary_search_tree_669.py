#!/usr/bin/env python

# https://leetcode.com/problems/trim-a-binary-search-tree/

import unittest
from pprint import pprint
import random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(subtree, destination):
    if subtree.val < destination.val:
        if destination.left is None:
            destination.left = subtree
            return
        insert(subtree, destination.left)
        return

    # all elements in tree are unique, no need to check ==
    if destination.right is None:
        destination.right = subtree
        return
    insert(subtree, destination.right)


def helper(node, low, high):
    if not node:
        return None

    left = node.left
    if left:
        if not left.left and not left.right:
            if not (low <= left.val <= high):
                node.left = None

    left = helper(node.left, low, high)

    right = node.right
    if right:
        if not right.left and not right.right:
            if not (low <= right.val <= high):
                node.right = None

    right = helper(node.right, low, high)

    if low <= node.val <= high:
        node.left = left
        node.right = right
        return node

    if not right and not left:
        return None

    if right and not left:
        return right

    if left and not right:
        return left

    # left and right must fight it out
    # insert the left subtree into the right subtree
    insert(left, right)
    return right


def solution(root, low, high):
    return helper(root, low, high)


def insertval(root, v):
    if not root:
        return

    if v < root.val:
        if not root.left:
            n = TreeNode(v)
            root.left = n
            return
        insertval(root.left, v)
    else:
        if not root.right:
            n = TreeNode(v)
            root.right = n
            return
        insertval(root.right, v)


def buildtree(arr):
    if not arr:
        return None

    root = TreeNode(val=arr[0])
    for a in arr[1:]:
        insertval(root, a)

    return root


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [1, 0, 2]
        root = buildtree(arr)
        solution(root, 1, 2)
