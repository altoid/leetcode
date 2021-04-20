#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3713/

import unittest


class Solution(object):
    def __init__(self):
        self.state = {}
        
    def combination_sum(self, arr, target):
        # numbers in arr are distinct
    
        # for each n in arr, return combination_sum(arr, target - n)
    
        # enumerate, don't generate

        if target not in self.state:
            result = 0
            if target == 1:
                if target not in arr:
                    return 0
                result = 1
            else:
                if target in arr:
                    result = 1
                
                for n in arr:
                    if target - n < 1:
                        continue
            
                    result += self.combination_sum(arr, target - n)
    
            self.state[target] = result

        return self.state[target]


class MyTest(unittest.TestCase):
    def test1(self):
        soln = Solution()
        arr = [1, 2, 3]
        target = 4
        self.assertEqual(7, soln.combination_sum(arr, target))

    def test2(self):
        soln = Solution()
        arr = [1, 2]
        target = 2
        self.assertEqual(2, soln.combination_sum(arr, target))

        
