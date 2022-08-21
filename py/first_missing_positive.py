#!/usr/bin/env python

# https://leetcode.com/problems/first-missing-positive/

import unittest
from pprint import pprint


# easy way is to use a heap
#
# r = 1
# while x = top of heap
#     if r == x
#         r += 1
#     else:
#         return r
#
# but we require O(n) time and O(1) space.
#
# mm = min
# mp = min positive
# mx = max
# mr = largest positive number that is <= the size of the array.
# n  = size of the array
#
# if mx < 1
#     return 1
# if mp > 1
#     return 1
#
# at this point we know the max in the array is positive and 1 is
# present.
#
# for each value < min_positive, change it to min_positive.
#
# for each value > n, change it to mr.
#
# so now the values in the array are in the range [1 .. mr]
#
# lemma
#
# the value we are looking for is in the range 2 .. n+1, where n is the
# size of the array.
#
# proof
#
#     suppose that the actual answer is n+2.  that would mean that the array
#     has all the values 1 .. n+1 inclusive.  but there are just n values in
#     the array.  therefore the array cannot have all the values in the
#     range 1 .. n+1 and one of those values is not present.  so it must be
#     that the missing number is in the range 1 .. n+1.  QED
#
# does changing each value > n to mr change the answer?
# if we didn't do this, would the answer be > mr?
#
# suppose this is the case.  that is, the answer is > mr.  for this to
# be the case, the array contains all the values 1 .. mr and some number
# x > mr.
#
# 1 2 3 4 4 4 5
#
# then the answer is <= x.  if x = mr + 1, then the largest +ive number
# in the array <= n should be x.  so it cannot be that mr is the largest
# +ive number <= n.
#
# 1 2 3 4 4 7 19
#
# if x > n, then x - mr > 1 and it has to be that y = mr + 1 is the
# answer.  since y isn't in the array (remember, it is missing), changing x to mr
# doesn't change the fact that y satisfies the condition of being the
# missing positive.
#
# so changing every number > mr to mr will not change the answer.


def solution(arr):
    # we are guaranteed that the array is nonempty.
    mx = max(arr)
    mn = min(arr)
    if mx < 1:
        return 1
    if mn > 1:
        return 1

    mp = mx
    for x in arr:
        if x < 1:
            continue
        mp = min(x, mp)
    n = len(arr)
    mr = mp
    for x in arr:
        if x > n:
            continue
        if x < mr:
            continue
        mr = max(mr, x)

    # we should really make a copy of the list but the constraints are to have O(1) storage.
    i = 0
    while i < n:
        arr[i] = max(mp, arr[i])
        arr[i] = min(arr[i], mr)
        i += 1

    pprint(arr)

    # pretend everything is 1-based
    i = 4  # actually position 3
    j = i - 1
    print("i = %s, j = %s" % (i, j))
    while arr[j] != 0:
        i = arr[j]
        arr[j] = 0
        j = i - 1
        print("i = %s, j = %s" % (i, j))

    pprint(arr)



class Solution:
    pass


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_1(self):
        arr = [-5, -3, -1, 1, 3, 5, 7, 9, 11]
        solution(arr)

    def test_2(self):
        arr = [1, 6, 7, 3, 3, 4, 2]
        solution(arr)
