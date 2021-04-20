#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3713/

import unittest


def combination_sum(arr, target):
    # numbers in arr are distinct

    # for each n in arr, return combination_sum(arr, target - n)

    # enumerate, don't generate

    if target == 1:
        if target in arr:
            return 1
        return 0

    result = 0
    if target in arr:
        result = 1
    
    for n in arr:
        if target - n < 1:
            continue

        result += combination_sum(arr, target - n)

    return result



class MyTest(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 3]
        target = 4
        self.assertEqual(7, combination_sum(arr, target))

    def test2(self):
        arr = [1, 2]
        target = 2
        self.assertEqual(2, combination_sum(arr, target))

        
