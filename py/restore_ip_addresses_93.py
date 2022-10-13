#!/usr/bin/env python

# https://leetcode.com/problems/restore-ip-addresses/

import unittest
from pprint import pprint
import random


# rules
#
# each octet [0..255]
# no leading 0
# all digits used

# use backtracking


def is_valid(octet):
    if not bool(octet):
        return False

    b = int(octet)
    if b > 255:
        return False

    if b == 0 and len(octet) > 1:
        return False

    if b > 0 and octet[0] == '0':
        return False

    return True


def helper(s, level):
    if not s:
        return None

    if level == 1:
        if is_valid(s):
            return [[s]]
        return None

    result = []
    for i in range(1, 4):
        if len(s) < i:
            continue

        octet_str = s[:i]
        if not is_valid(octet_str):
            continue
        restof = s[i:]
        partial = helper(restof, level - 1)
        if not partial:
            continue
        for p in partial:
            result.append(p + [octet_str])
    return result


def solution(s):
    result = helper(s, 4)
    answer = set()
    for r in result:
        rr = '.'.join(r[::-1])
        answer.add(rr)
    return list(answer)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_level_1(self):
        self.assertIsNone(helper("", 1))
        self.assertIsNone(helper("00", 1))
        self.assertIsNone(helper("012", 1))
        self.assertIsNone(helper("258", 1))

        self.assertIsNotNone(helper("123", 1))
        self.assertIsNotNone(helper("0", 1))
        self.assertIsNotNone(helper("10", 1))
        self.assertIsNotNone(helper("255", 1))

    def test_level_2_1(self):
        result = helper("123", 2)

        answer = set()
        for r in result:
            rr = '.'.join(r[::-1])
            answer.add(rr)

        expected = {'1.23', '12.3'}
        self.assertEqual(expected, answer)

    def test_level_2_2(self):
        result = helper("120", 2)

        answer = set()
        for r in result:
            rr = '.'.join(r[::-1])
            answer.add(rr)

        expected = {'1.20', '12.0'}
        self.assertEqual(expected, answer)

    def test_1(self):
        result = set(solution("25525511135"))
        self.assertEqual({"255.255.11.135", "255.255.111.35"}, result)

    def test_2(self):
        result = set(solution("101023"))
        expecting = {"1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"}
        self.assertEqual(expecting, result)

    def test_3(self):
        result = set(solution("0000"))
        expecting = {"0.0.0.0"}
        self.assertEqual(expecting, result)

    def test_4(self):
        result = solution("00000")
        self.assertEqual([], result)

    def test_5(self):
        result = solution("9999999999999")
        self.assertEqual([], result)

    def test_6(self):
        result = set(solution("19216811"))
        expecting = {"192.168.1.1"}
        self.assertTrue(expecting.issubset(result))
