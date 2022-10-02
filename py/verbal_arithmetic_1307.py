#!/usr/bin/env python

# https://leetcode.com/problems/verbal-arithmetic-puzzle/

import unittest
from pprint import pprint
import random
from itertools import permutations


def solution_1(addends, result):
    # tests 1-6 run in around 10.5 seconds total.

    # find all the unique letters
    mashup = ''.join(addends) + result
    unique_letters = ''.join(sorted(list(set(mashup))))

    # find the first letters of all of the addends and result
    first_letters = set([x[0] for x in addends + [result]])
    pprint(first_letters)
    first_letter_index = {}
    for l in first_letters:
        first_letter_index[l] = unique_letters.index(l)

    digits = [str(x) for x in range(10)]
    pprint(first_letter_index)
    for p in permutations(digits, len(unique_letters)):
        # map each permutation to the digits.
        usable = True
        for v in first_letter_index.values():
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


def solution_2(addends, result):
    # idea:  identify letters that cannot be 0.  find all permutations that map to these letters.
    # for each of these permutations, permute the rest of the digits

    # fuck:  takes much longer than solution_1, 15-20 s.

    # find all the unique letters
    unique_letters = set(''.join(addends) + result)

    # find the first letters of all of the addends and result
    first_letters = set([x[0] for x in addends + [result]])

    other_letters = unique_letters - first_letters

    letters_string = ''.join(list(first_letters)) + ''.join(list(other_letters))

    all_digits = {str(x) for x in range(10)}
    nonzero_digits = {str(x) for x in range(1, 10)}
    nunused = len(unique_letters) - len(first_letters)

    for nzp in permutations(nonzero_digits, len(first_letters)):
        nz_used = set(nzp)
        unused = all_digits - nz_used
        nzp_string = ''.join(nzp)
        for zp in permutations(unused, nunused):
            digits_to_map = nzp_string + ''.join(zp)

            ttable = str.maketrans(letters_string, digits_to_map)
            sum_int = int(result.translate(ttable))
            addends_int = [int(x.translate(ttable)) for x in addends]
            if sum(addends_int) == sum_int:
                print("###########################")
                print(unique_letters)
                print(digits_to_map)
                print(addends, addends_int)
                print(result, sum_int)
                return True

    return False


def solution(addends, result):
    return solution_1(addends, result)

if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_1(self):
        addends = ["SEND", "MORE"]
        sum = "MONEY"

        self.assertTrue(solution(addends, sum))

    def test_2(self):
        addends = ["SHIRT", "TSHIRT"]
        sum = "CLOTHES"

        self.assertTrue(solution(addends, sum))

    def test_3(self):
        addends = ["SKIRT", "TSHIRT"]
        sum = "CLOTHES"

        self.assertTrue(solution(addends, sum))

    def test_4(self):
        addends = ["GHANA", "GABON", "BHUTAN"]
        sum = "ALBANIA"

        self.assertTrue(solution(addends, sum))

    def test_5(self):
        addends = ["SEAL", "SNAIL", "MONKEY"]
        sum = "ANIMALS"

        self.assertTrue(solution(addends, sum))

    def test_6(self):
        addends = ["RICH", "POOR", "HAPPY"]
        sum = "PEOPLE"

        self.assertTrue(solution(addends, sum))
