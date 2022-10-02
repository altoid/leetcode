#!/usr/bin/env python

# https://leetcode.com/problems/verbal-arithmetic-puzzle/

import unittest
from pprint import pprint
import random
from itertools import permutations

def solution(addends, result):
    # find all the unique letters
    mashup = ''.join(addends) + result
    unique_letters = ''.join(sorted(list(set(mashup))))

    # find the first letters of all of the addends and result
    first_letters = list(set([x[0] for x in addends + [result]]))
    pprint(first_letters)

    digits = [str(x) for x in range(10)]

    for p in permutations(digits, len(unique_letters)):
        break

        # map each permutation to the digits.
        s = ''.join(p)
        ttable = str.maketrans(unique_letters, s)
        sum_int = int(result.translate(ttable))
        addends_int = [int(x.translate(ttable)) for x in addends]
        if sum(addends_int) == sum_int:
            print("###########################")
            print(addends, addends_int)
            print(result, sum_int)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        addends = ["SEND", "MORE"]
        sum = "MONEY"

        solution(addends, sum)

