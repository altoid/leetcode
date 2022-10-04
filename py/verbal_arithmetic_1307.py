#!/usr/bin/env python

# https://leetcode.com/problems/verbal-arithmetic-puzzle/
import string
import unittest
from pprint import pprint
import random
from itertools import permutations


def solution_1(addends, result):
    # tests 1-6 run in around 10.5 seconds total.

    # find all the unique letters
    mashup = ''.join(addends) + result
    unique_letters = sorted(list(set(mashup)))

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

        ttable = dict(zip(unique_letters, p))
        sum_int = int(''.join([ttable[x] for x in result]))
        addends_int = [int(''.join([ttable[x] for x in y])) for y in addends]
        if sum(addends_int) == sum_int:
            print("###########################")
            print(unique_letters)
            print(p)
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


def make_crypto_sum():
    letters = ''.join(random.sample(string.ascii_uppercase, 10))
    print(letters)
    digits = ''.join([str(x) for x in range(10)])
    print(digits)
    naddends = 2
    addends = [random.randint(100, 10000) for _ in range(naddends)]
    result = sum(addends)
    print(addends, result)
    ttable = str.maketrans(digits, letters)
    addends_str = [x.translate(ttable) for x in list(map(str, addends))]
    result_str = str(result).translate(ttable)
    print(addends_str)
    print(result_str)
    return addends_str, result_str


#
# NOTES
#
# idea:  determine which letters are independent vs dependent variables.
# traverse top down, right to left:
#
#     S   E   N   D    |
#     M   O   R   E    |
# ------------------   |
# M   O   N   E   Y    V
#  <----------------
#
# if the first appearance of a letter is in an addend, it can be independent.
# if the first appearance is in the sum, no way is it independent.
# if there is one unvisited letter in a column, and it's exclusively in an addend, then that letter is dependent.
#
# we should test by generating random numbers, adding them, mapping all the digits to the letters, then
# feeding it to the solver.
#
# up to 5 addends.
#
# independent - we can pick the value
# nonzero
# dependent
# deduced - we can determine a unique value for this, even if it's independent.
#
# cases to look for
#
#   ***A
#   ***B
#   ====
#  ****B    ==> only works if A == 0 (when this is the rightmost column)
#
#   ***A
#   ***A
#   ====
#  ****A   A = 0
#
# in both cases we'll consider A to be dependent since we can't pick it.

class LetterState(object):
    def __init__(self):
        self.digit = None

        # not set during initialization
        self.visited = False

        # fixed means we can determine the digit a letter maps to before we traverse all the letters.
        self.fixed = False

        # only set by examining the first letter of each addend/result, not by deduction of values
        self.can_be_zero = True
        self.dependent = None  # remaining None means we couldn't determine

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return self.__repr__()


class SolutionGraph(object):
    def __init__(self, addends, result):
        self.addends = addends
        self.result = result
        self.letters_to_letter_states = {}
        self.columns = []

        # reverse all of the addend and result strings so that the indexing arithmetic is easier
        addends_reversed = [x[::-1] for x in addends[::-1]]
        result_reversed = result[::-1]

        # find all the unique letters
        unique_letters = set(''.join(addends) + result)

        # find the first letters of all of the addends and result
        first_letters = set([x[0] for x in addends + [result]])

        pprint(unique_letters)
        pprint(first_letters)

        for l in unique_letters:
            self.letters_to_letter_states[l] = LetterState()
        for l in first_letters:
            self.letters_to_letter_states[l].can_be_zero = False

        # if we have a single-digit addend, allow it to be mapped to zero.
        for a in addends_reversed:
            if len(a) == 1:
                self.letters_to_letter_states[a[0]].can_be_zero = True

        if len(result_reversed) == 1:
            self.letters_to_letter_states[result_reversed[0]].can_be_zero = True

        # build the columns.  first element in a column is the sum digit; the addends are after.
        # easiest way to distinguish sums from addends.

        i = 0
        while i < len(result_reversed):
            column = []
            column.append(result_reversed[i])
            for a in addends_reversed:
                if i < len(a):
                    column.append(a[i])
            self.columns.append(column)
            i += 1

        print(addends_reversed)
        print(result_reversed)
        pprint(self.columns)

        # traverse the first column, start with the sum digit
        c0 = self.columns[0]
        self.letters_to_letter_states[c0[0]].dependent = True

        # now the rest of the first column.  these are the cases:
        #
        # 1. X = X + X   => X = 0
        # 2. Y = X + X   => X is independent
        # 3. Y = X + Y   => X = 0
        # 4. Z = X + Y   => X and Y are independent

        if c0[1] == c0[2]:
            if c0[0] == c0[1]:
                # case 1
                self.letters_to_letter_states[c0[0]].fixed = True
                self.letters_to_letter_states[c0[0]].digit = 0
            else:
                # case 2
                self.letters_to_letter_states[c0[1]].dependent = False
        else:
            if c0[1] == c0[0]:
                # case 3
                self.letters_to_letter_states[c0[2]].fixed = True
                self.letters_to_letter_states[c0[2]].dependent = False
                self.letters_to_letter_states[c0[2]].digit = 0
            elif c0[2] == c0[0]:
                # also case 3
                self.letters_to_letter_states[c0[1]].fixed = True
                self.letters_to_letter_states[c0[1]].dependent = False
                self.letters_to_letter_states[c0[1]].digit = 0
            else:
                self.letters_to_letter_states[c0[1]].dependent = False
                self.letters_to_letter_states[c0[2]].dependent = False

        pprint(self.letters_to_letter_states)


if __name__ == '__main__':
    addends = ["SEND", "MORE"]
    result = "MONEY"
    s = SolutionGraph(addends, result)


class SGTest(unittest.TestCase):
    def test_1(self):
        addends = ["X", "X"]
        result = "X"
        s = SolutionGraph(addends, result)

        c0 = s.columns[0]
        self.assertEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[1]])
        self.assertEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[2]])
        self.assertTrue(s.letters_to_letter_states[c0[0]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[0]].dependent)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)
        self.assertEqual(0, s.letters_to_letter_states[c0[0]].digit)
        for x in c0:
            pprint(s.letters_to_letter_states[x])

    def test_2(self):
        addends = ["X", "X"]
        result = "Y"
        s = SolutionGraph(addends, result)

        c0 = s.columns[0]
        self.assertNotEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[1]])
        self.assertEqual(s.letters_to_letter_states[c0[1]], s.letters_to_letter_states[c0[2]])
        self.assertFalse(s.letters_to_letter_states[c0[0]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertFalse(s.letters_to_letter_states[c0[1]].fixed)
        self.assertFalse(s.letters_to_letter_states[c0[1]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[1]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[1]].can_be_zero)

    def test_3(self):
        addends = ["X", "Y"]
        result = "Y"
        s = SolutionGraph(addends, result)

        c0 = s.columns[0]
        self.assertEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[1]])
        self.assertNotEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[2]])

        self.assertFalse(s.letters_to_letter_states[c0[0]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertTrue(s.letters_to_letter_states[c0[2]].fixed)
        self.assertFalse(s.letters_to_letter_states[c0[2]].dependent)
        self.assertEqual(0, s.letters_to_letter_states[c0[2]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[2]].can_be_zero)

    def test_3_5(self):
        addends = ["Y", "X"]
        result = "Y"
        s = SolutionGraph(addends, result)

        c0 = s.columns[0]
        self.assertEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[2]])
        self.assertNotEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[1]])

        self.assertFalse(s.letters_to_letter_states[c0[0]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertTrue(s.letters_to_letter_states[c0[1]].fixed)
        self.assertFalse(s.letters_to_letter_states[c0[1]].dependent)
        self.assertEqual(0, s.letters_to_letter_states[c0[1]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[1]].can_be_zero)

    def test_4(self):
        addends = ["X", "Y"]
        result = "Z"
        s = SolutionGraph(addends, result)

        c0 = s.columns[0]
        self.assertNotEqual(s.letters_to_letter_states[c0[0]], s.letters_to_letter_states[c0[1]])
        self.assertNotEqual(s.letters_to_letter_states[c0[1]], s.letters_to_letter_states[c0[2]])
        self.assertNotEqual(s.letters_to_letter_states[c0[2]], s.letters_to_letter_states[c0[0]])

        self.assertFalse(s.letters_to_letter_states[c0[0]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertFalse(s.letters_to_letter_states[c0[1]].fixed)
        self.assertFalse(s.letters_to_letter_states[c0[1]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[1]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[1]].can_be_zero)

        self.assertFalse(s.letters_to_letter_states[c0[2]].fixed)
        self.assertFalse(s.letters_to_letter_states[c0[2]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[2]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[2]].can_be_zero)


class MyTest(unittest.TestCase):
    def test_1(self):
        addends = ["SEND", "MORE"]
        result = "MONEY"

        self.assertTrue(solution(addends, result))

    def test_2(self):
        addends = ["SHIRT", "TSHIRT"]
        result = "CLOTHES"

        self.assertTrue(solution(addends, result))

    def test_3(self):
        addends = ["SKIRT", "TSHIRT"]
        result = "CLOTHES"

        self.assertTrue(solution(addends, result))

    def test_4(self):
        addends = ["GHANA", "GABON", "BHUTAN"]
        result = "ALBANIA"

        self.assertTrue(solution(addends, result))

    def test_5(self):
        addends = ["SEAL", "SNAIL", "MONKEY"]
        result = "ANIMALS"

        self.assertTrue(solution(addends, result))

    def test_6(self):
        addends = ["RICH", "POOR", "HAPPY"]
        result = "PEOPLE"

        self.assertTrue(solution(addends, result))

    def test_7(self):
        addends = ["LEET", "CODE"]
        result = "POINT"

        self.assertFalse(solution(addends, result))
