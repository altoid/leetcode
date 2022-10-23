#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def to_number(s):
    arr = list(map(int, list(s)))
    result = 0
    for b in arr:
        result *= 2
        result += b
    return result


def solution(s, n):
    l = (len(s) * (len(s) + 1)) // 2

    if n > l:
        return False

    l = len(s)

    substrings_to_numbers = {}
    if '0' in s:
        substrings_to_numbers["0"] = 0
    if '1' in s:
        substrings_to_numbers["1"] = 1

    # convert substrings to numbers

    for i in range(l):
        if s[i] == "0":
            continue

        for substring_length in range(1, l - i + 1):
            substring = s[i:i + substring_length]
#            print(substring)
            if substring in substrings_to_numbers:
                continue

            x = substrings_to_numbers[substring[:-1]] * 2
            if substring[-1] == "1":
                x += 1
            substrings_to_numbers[substring] = x

    all_values = set(substrings_to_numbers.values())
    for i in range(1, n + 1):
        if i not in all_values:
            return False

    return True


if __name__ == '__main__':
    solution("abcde", 1)


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, to_number("0"))
        self.assertEqual(1, to_number("1"))
        self.assertEqual(366, to_number("101101110"))

    def test_2(self):
        s = "11111110011110011001001100000001101101000000111100111110001101101011010110001001100011111001111011011001111110111100010110100011101000101011101101000111111000110001011000010000100000111000111001111000010010101110000010011001011111101110001001000110101110001011111010111010101101011100010011010111110010100101010011011010001100100001011011111000001001111101111010000111110010000001010000011000001101111111011100011101000011000010100000000100010010101011111000110001100001100011011010011011000011000111"
        n = 25

    def test_3(self):
        s = "001111111000111011100110001001011100001101011001000100000001111100100001101100010010100111111100010101000000001010101011111001010111100000001110000001111000100001101010011010111101101000101101001110011000110110000110010111011100100101111000010011111001000001001000011011000111110010001010110101110011010000101001110000010111100001111011110000100000011000111111011101001011110111001110000011100100101001100001100111010010111111111000011110001110100010001000000101110000010100100111100010001111111110100001111000101001111110000011000001000001110011011011100010101010111110101110101110010111000110111110"
        n = 30
        print(len(s))

    def test_4(self):
        s = "0"
        n = 1