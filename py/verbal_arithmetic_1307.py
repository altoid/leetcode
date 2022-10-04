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


def make_crypto_sum(low, high):
    """
    pick two random numbers in the range [low .. high].  compute their sum.  map the digits
    in addends and sum to random letters.  return the addends and the sum.  the result
    will be a cryptarithm that will always have a solution.
    """
    letters = ''.join(random.sample(string.ascii_uppercase, 10))
    digits = ''.join([str(x) for x in range(10)])
    naddends = 2
    addends = [random.randint(low, high) for _ in range(naddends)]
    result = sum(addends)
    ttable = str.maketrans(digits, letters)
    addends_str = [x.translate(ttable) for x in list(map(str, addends))]
    result_str = str(result).translate(ttable)
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

        print("addends = %s" % addends)
        print("result = '%s'" % result)

        # reverse all of the addend and result strings so that the indexing arithmetic is easier
        addends_reversed = [x[::-1] for x in addends[::-1]]
        result_reversed = result[::-1]

        # find all the unique letters
        unique_letters = set(''.join(addends) + result)

        # find the first letters of all of the addends and result
        first_letters = set([x[0] for x in addends + [result]])

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

        #pprint(self.columns)

        # deal with the special case where the sum is longer than either of the two addends.
        # we have to look at this first.
        # in that case we know that its leftmost digit is a 1.  but it makes the initialization
        # very messy, because we would have to modify all the cases above to consider whether
        # any of X, Y, Z are already known to be 1.
        #
        # case 1:  can't happen, no way X could be 1
        # case 2:  Y could not be 1; it has to be even
        # case 3:  X still has to be 0, it could never be 1.
        # case 4:  if Z is the 1, then one of X, Y has to be dependent.  if X or Y is 1, then neither of X or Y
        #          is independent.

        if len(result_reversed) > max(map(len, addends_reversed)):
            state = self.letters_to_letter_states[result[0]]
            state.fixed = True
            state.digit = 1
            state.dependent = True

        # traverse the first column, start with the sum digit.  be careful to consider
        # whether any of X, Y, Z is 1.

        c0 = self.columns[0]
        if self.letters_to_letter_states[c0[0]].dependent is None:
            self.letters_to_letter_states[c0[0]].dependent = True

        # now the rest of the first column.  these are the cases:
        #
        # 1. X = X + X   => X = 0
        # 2. Y = X + X   => X is independent
        # 3. Y = X + Y   => X = 0, Y is independent
        # 4. Z = X + Y   => X and Y are independent

        if c0[1] == c0[2]:
            if c0[0] == c0[1]:
                # case 1
                self.letters_to_letter_states[c0[0]].fixed = True
                self.letters_to_letter_states[c0[0]].digit = 0
            else:
                # case 2
                if self.letters_to_letter_states[c0[1]].dependent is None:
                    # it's not already 1
                    self.letters_to_letter_states[c0[1]].dependent = False
        else:
            if c0[0] == c0[1]:
                # case 3
                self.letters_to_letter_states[c0[2]].fixed = True
                self.letters_to_letter_states[c0[2]].dependent = True
                self.letters_to_letter_states[c0[2]].digit = 0
                self.letters_to_letter_states[c0[0]].dependent = False
            elif c0[0] == c0[2]:
                # also case 3
                self.letters_to_letter_states[c0[1]].fixed = True
                self.letters_to_letter_states[c0[1]].dependent = True
                self.letters_to_letter_states[c0[1]].digit = 0
                self.letters_to_letter_states[c0[0]].dependent = False
            else:
                # case 4
                if self.letters_to_letter_states[c0[0]].digit is None:
                    # Z was not set as the leftmost 1 of the sum.  but one of x or y could be.
                    if self.letters_to_letter_states[c0[1]].digit is None and self.letters_to_letter_states[c0[2]].digit is None:
                        self.letters_to_letter_states[c0[1]].dependent = False
                        self.letters_to_letter_states[c0[2]].dependent = False
                    elif self.letters_to_letter_states[c0[1]].digit is None:
                        # Y is the 1
                        self.letters_to_letter_states[c0[1]].dependent = False
                    else:
                        # X is the 1
                        self.letters_to_letter_states[c0[2]].dependent = False
                else:
                    # then the addend digits are not the same.  pick one to be dependent
                    self.letters_to_letter_states[c0[1]].dependent = False
                    self.letters_to_letter_states[c0[2]].dependent = True

        # next columns
        for col in self.columns[1:]:
            if self.letters_to_letter_states[col[0]].dependent is None:
                # we haven't encountered this letter yet.  but if the first time we are seeing it is in the sum,
                # it's definitely dependent
                self.letters_to_letter_states[col[0]].dependent = True

            # now look at the addend digits

            if len(col) == 1:
                # leftmost digit in sum is all alone
                continue
            elif len(col) == 2:
                if self.letters_to_letter_states[col[1]].dependent is None:
                    self.letters_to_letter_states[col[1]].dependent = False

            if col[1] == col[2]:
                if col[0] == col[1]:
                    # case 1
                    pass
                # case 2
                if self.letters_to_letter_states[col[1]].dependent is None:
                    self.letters_to_letter_states[col[1]].dependent = False
            else:
                if col[0] == col[1]:
                    # case 3
                    self.letters_to_letter_states[c0[0]].dependent = False
                elif col[0] == col[2]:
                    # also case 3
                    self.letters_to_letter_states[c0[0]].dependent = False
                else:
                    # case 4
                    if self.letters_to_letter_states[col[1]].dependent is None and self.letters_to_letter_states[col[2]].dependent is None:
                        self.letters_to_letter_states[col[1]].dependent = False
                        self.letters_to_letter_states[col[2]].dependent = False
                    elif self.letters_to_letter_states[col[1]].dependent is None:
                        self.letters_to_letter_states[col[1]].dependent = True
                    elif self.letters_to_letter_states[col[2]].dependent is None:
                        self.letters_to_letter_states[col[2]].dependent = True

        pprint(self.letters_to_letter_states)
        self.sanity_check()

    def sanity_check(self):
        # dependent is set for every letter, and at least one is independent
        found_independent = False
        for k, v in self.letters_to_letter_states.items():
            if v.dependent is None:
                raise ValueError("digit dependence not determined:  %s" % v)
            if not v.dependent:
                found_independent = True

        if not found_independent:
            # this is ok for the case X+X=X.  but no others.
            if len(self.letters_to_letter_states) > 1:
                raise ValueError("no independent digits")

        # # all the digits in the sum are dependent
        # for c in self.result:
        #     if not self.letters_to_letter_states[c].dependent:
        #         raise ValueError("independent digit in sum:  %s" % c)


if __name__ == '__main__':
    # addends = ["SEND", "MORE"]
    # result = "MONEY"
    # s = SolutionGraph(addends, result)

    for _ in range(1000):
        addends, result = make_crypto_sum(100, 999)

        s = SolutionGraph(addends, result)

class SGTest(unittest.TestCase):
    def test_8(self):
        addends = ["BJJ", "YPJ"]
        result = "BJPJ"

        s = SolutionGraph(addends, result)

    def test_7(self):
        addends = ["UPQ", "PPQ"]
        result = "ECTQ"

        s = SolutionGraph(addends, result)

    def test_6(self):
        addends = ["OQ", "OY"]
        result = "QX"

        s = SolutionGraph(addends, result)

    def test_5(self):
        addends = ["HY", "CV"]
        result = "VRS"

        s = SolutionGraph(addends, result)

        self.assertFalse(s.letters_to_letter_states['Y'].dependent)
        self.assertFalse(s.letters_to_letter_states['H'].dependent)
        self.assertFalse(s.letters_to_letter_states['C'].dependent)
        self.assertTrue(s.letters_to_letter_states['V'].dependent)
        self.assertTrue(s.letters_to_letter_states['R'].dependent)
        self.assertTrue(s.letters_to_letter_states['S'].dependent)


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
        self.assertFalse(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertTrue(s.letters_to_letter_states[c0[2]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[2]].dependent)
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
        self.assertFalse(s.letters_to_letter_states[c0[0]].dependent)
        self.assertIsNone(s.letters_to_letter_states[c0[0]].digit)
        self.assertTrue(s.letters_to_letter_states[c0[0]].can_be_zero)

        self.assertTrue(s.letters_to_letter_states[c0[1]].fixed)
        self.assertTrue(s.letters_to_letter_states[c0[1]].dependent)
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
