#!/usr/bin/env python

# https://leetcode.com/problems/validate-binary-search-tree/

import unittest
from pprint import pprint
import random


def solution():
    pass


class Solution:
    def subtree_minmax(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root.val, root.val

        left_minmax = self.subtree_minmax(root.left)
        right_minmax = self.subtree_minmax(root.right)

        this_min = root.val
        this_max = root.val

        if left_minmax:
            this_min = min(this_min, left_minmax[0])
            this_max = max(this_max, left_minmax[1])

        if right_minmax:
            this_min = min(this_min, right_minmax[0])
            this_max = max(this_max, right_minmax[1])

        return this_min, this_max

    def isValidBST(self, root):
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if not self.isValidBST(root.right):
            return False

        left_minmax = self.subtree_minmax(root.left)
        right_minmax = self.subtree_minmax(root.right)

        if left_minmax:
            if left_minmax[0] >= root.val or left_minmax[1] >= root.val:
                return False

        if right_minmax:
            if right_minmax[0] <= root.val or right_minmax[1] <= root.val:
                return False

        return True


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        pass
