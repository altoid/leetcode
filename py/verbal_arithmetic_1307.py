#!/usr/bin/env python

# https://leetcode.com/problems/verbal-arithmetic-puzzle/

import unittest
from pprint import pprint
import random
from itertools import permutations


def solution_godawful(addends, result):
    # find all the unique letters
    mashup = ''.join(addends) + result
    unique_letters = ''.join(sorted(list(set(mashup))))

    # find the first letters of all of the addends and result
    first_letters = list(set([x[0] for x in addends + [result]]))
    pprint(first_letters)
    first_letter_index = {}
    for l in first_letters:
        first_letter_index[l] = unique_letters.index(l)

    digits = [str(x) for x in range(10)]
    pprint(first_letter_index)
    for p in permutations(digits, len(unique_letters)):
        # map each permutation to the digits.
        usable = True
        for k, v in first_letter_index.items():
            if p[v] == '0':
                usable = False
                break

        if not usable:
            continue

        s = ''.join(p)
        ttable = str.maketrans(unique_letters, s)
        sum_int = int(result.translate(ttable))
        addends_int = [int(x.translate(ttable)) for x in addends]
        if sum(addends_int) == sum_int:
            print("###########################")
            print(unique_letters)
            print(s)
            print(addends, addends_int)
            print(result, sum_int)
            return True

    return False


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        addends = ["SEND", "MORE"]
        sum = "MONEY"

        self.assertTrue(solution_godawful(addends, sum))

    def test_2(self):
        addends = ["SHIRT", "TSHIRT"]
        sum = "CLOTHES"

        self.assertTrue(solution_godawful(addends, sum))

    def test_3(self):
        addends = ["SKIRT", "TSHIRT"]
        sum = "CLOTHES"

        self.assertTrue(solution_godawful(addends, sum))

    def test_4(self):
        addends = ["GHANA", "GABON", "BHUTAN"]
        sum = "ALBANIA"

        self.assertTrue(solution_godawful(addends, sum))

    def test_5(self):
        addends = ["SEAL", "SNAIL", "MONKEY"]
        sum = "ANIMALS"

        self.assertTrue(solution_godawful(addends, sum))

    def test_6(self):
        addends = ["RICH", "POOR", "HAPPY"]
        sum = "PEOPLE"

        self.assertTrue(solution_godawful(addends, sum))
