#!/usr/bin/env python

# https://leetcode.com/problems/verbal-arithmetic-puzzle/
import string
import unittest
from pprint import pprint
import random
from itertools import permutations
import string

# consider this for generating permutations with constraints
#
# https://arxiv.org/pdf/1311.3813.pdf


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


def make_crypto_sum(a1_digits, a2_digits):
    """
    pick two random numbers with the given number of digits.  compute their sum.  map the digits
    in addends and sum to random letters.  return the addends and the sum.  the result
    will be a cryptarithm that will always have a solution.
    """
    letters = ''.join(random.sample(string.ascii_uppercase, 10))
    digits = ''.join([str(x) for x in range(10)])
    naddends = 2
    a1 = random.randint(10 ** (a1_digits - 1), 10 ** a1_digits - 1)
    a2 = random.randint(10 ** (a2_digits - 1), 10 ** a2_digits - 1)
    addends = [a1, a2]
    result = sum(addends)
    ttable = str.maketrans(digits, letters)
    decoder = {chr(k): int(chr(v)) for k, v in str.maketrans(letters, digits).items()}
    addends_str = [x.translate(ttable) for x in list(map(str, addends))]
    result_str = str(result).translate(ttable)
    return addends_str, result_str, addends, result, decoder


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

        # fixed means we can determine the digit a letter maps to before we traverse all the letters.
        self.fixed = False

        # only set by examining the first letter of each addend/result, not by deduction of values
        self.can_be_zero = True
        self.dependent = None  # remaining None means we couldn't determine

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return self.__repr__()


class Column(object):
    def __init__(self, column=None):
        # the full set of digits in one column of the sum, starting with the sum digit and going upward.
        self.column = column if column else []

        # map each digit to the number of times it appears in the column, including as the sum digit
        self.unique_digits = {}
        for c in self.column:
            if c not in self.unique_digits:
                self.unique_digits[c] = 0
            self.unique_digits[c] += 1

    def __iter__(self):
        for c in self.column:
            yield c

    def __len__(self):
        return len(self.column)

    def __getitem__(self, item):
        return self.column[item]

    def __str__(self):
        return str(self.column)

    def num_unique_digits(self):
        return len(self.unique_digits)

    def append(self, c):
        if c not in self.unique_digits:
            self.unique_digits[c] = 0
        self.unique_digits[c] += 1
        self.column.append(c)


class SolutionGraph(object):
    def __init__(self, addends, result):
        self.addends = addends
        self.result = result
        self.letters_to_letter_states = {}
        self.columns = []
        self.solvable = True

        # maps digits to the letters that got mapped to them.
        self.digit_mapping = dict(zip(range(10), [False] * 10))

        # print("addends = %s" % addends)
        # print("result = '%s'" % result)

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
            column = Column()
            column.append(result_reversed[i])
            for a in addends_reversed:
                if i < len(a):
                    column.append(a[i])
            self.columns.append(column)
            i += 1

        # pprint(self.columns)

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
            self.assign_digit(1, result[0])
            state.dependent = True

        # traverse the first column, start with the sum digit.  be careful to consider
        # whether any of X, Y, Z is 1.

        c0 = self.columns[0]

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
                self.assign_digit(0, c0[0])
                self.letters_to_letter_states[c0[1]].dependent = True
            else:
                # case 2
                if self.letters_to_letter_states[c0[1]].dependent is None:
                    # it's not already 1
                    self.letters_to_letter_states[c0[1]].dependent = False
                if self.letters_to_letter_states[c0[0]].dependent is None:
                    # it's not already 1
                    self.letters_to_letter_states[c0[0]].dependent = True

        else:
            if c0[0] == c0[1]:
                # case 3
                self.letters_to_letter_states[c0[2]].fixed = True
                self.letters_to_letter_states[c0[2]].dependent = True
                self.assign_digit(0, c0[2])
                if self.letters_to_letter_states[c0[0]].dependent is None:
                    self.letters_to_letter_states[c0[0]].dependent = False
            elif c0[0] == c0[2]:
                # also case 3
                self.letters_to_letter_states[c0[1]].fixed = True
                self.letters_to_letter_states[c0[1]].dependent = True
                self.assign_digit(0, c0[1])
                if self.letters_to_letter_states[c0[0]].dependent is None:
                    self.letters_to_letter_states[c0[0]].dependent = False
            else:
                # case 4
                if self.letters_to_letter_states[c0[0]].digit is None:
                    # Z was not set as the leftmost 1 of the sum.  but one of x or y could be.
                    self.letters_to_letter_states[c0[0]].dependent = True
                    if self.letters_to_letter_states[c0[1]].digit is None and self.letters_to_letter_states[
                        c0[2]].digit is None:
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
                # we haven't encountered this letter yet.  if the first time we are seeing it is
                # in the sum, it is dependent UNLESS it also appears in the addends.
                if col.unique_digits[col[0]] == 1:
                    self.letters_to_letter_states[col[0]].dependent = True
                else:
                    self.letters_to_letter_states[col[0]].dependent = False

            # now look at the addend digits

            if len(col) == 1:
                # leftmost digit in sum is all alone
                continue
            elif len(col) == 2:
                if self.letters_to_letter_states[col[1]].dependent is None:
                    self.letters_to_letter_states[col[1]].dependent = False
                continue

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
                    if self.letters_to_letter_states[col[0]].dependent is None:
                        self.letters_to_letter_states[col[0]].dependent = False
                    elif self.letters_to_letter_states[col[2]].dependent is None:
                        self.letters_to_letter_states[col[2]].dependent = not self.letters_to_letter_states[
                            col[0]].dependent
                elif col[0] == col[2]:
                    # also case 3
                    if self.letters_to_letter_states[col[0]].dependent is None:
                        self.letters_to_letter_states[col[0]].dependent = False
                    elif self.letters_to_letter_states[col[1]].dependent is None:
                        self.letters_to_letter_states[col[1]].dependent = not self.letters_to_letter_states[
                            col[0]].dependent
                else:
                    # case 4
                    if self.letters_to_letter_states[col[1]].dependent is None:
                        self.letters_to_letter_states[col[1]].dependent = False
                    if self.letters_to_letter_states[col[2]].dependent is None:
                        self.letters_to_letter_states[col[2]].dependent = False

        self.sanity_check()

    def assign_digit(self, digit, letter):
        self.digit_mapping[digit] = letter
        self.letters_to_letter_states[letter].digit = digit

    def unassign_digit(self, digit):
        assigned_to = self.digit_mapping[digit]
        self.digit_mapping[digit] = None
        self.letters_to_letter_states[assigned_to].digit = None

    def unmapped_letters(self, col):
        # for this column, return a list of the unique letters that aren't mapped to any digits.

        result = []
        for k in col.unique_digits.keys():
            if self.letters_to_letter_states[k].digit is None:
                result.append(k)

        return result

    def sanity_check(self):
        # dependent is set for every letter, and at least one is independent.
        # renders the problem not solvable if, after initializing, we won't be able to find a solution.

        found_independent = False
        for k, v in self.letters_to_letter_states.items():
            if v.dependent is None:
                # raise ValueError("digit dependence not determined:  %s" % k)
                self.solvable = False
                return

            if not v.dependent:
                found_independent = True

        if not found_independent:
            # this is ok for the case X+X=X.  but no others.
            if len(self.letters_to_letter_states) > 1:
                # raise ValueError("no independent digits")
                self.solvable = False

    def sum_of_addends(self, col):
        # TODO make this more pythonic
        total = 0
        for c in col[1:]:
            if self.letters_to_letter_states[c].digit is not None:
                total += self.letters_to_letter_states[c].digit
        return total

    def unwind_mapping(self):
        for k in self.letters_to_letter_states.keys():
            ls = self.letters_to_letter_states[k]
            if not ls.fixed and ls.digit is not None:
                self.unassign_digit(ls.digit)

    def decrypt_letter_string(self, w):
        result = [self.letters_to_letter_states[x].digit for x in list(w)]
        return int(''.join(list(map(str, result))))

    def candidate_digits(self, column, carry, unmapped_letter):
        # determine the digits that we can map to the unmapped letter in this column.
        # return the result as a list of (digit, carry) tuples.  return []
        # if we can't match anything.

        # cases:
        # 1.  unset digit is the sum digit
        # 2.  unset digit is in the addends
        # 3.  unset digit is in both places

        sum_letter = column[0]
        if self.letters_to_letter_states[sum_letter].digit is None:
            sum_letter_count = column.unique_digits[sum_letter]
            if sum_letter_count == 1:
                # case 1
                column_sum = self.sum_of_addends(column) + carry
                new_carry, missing_digit = divmod(column_sum, 10)
                if self.digit_mapping[missing_digit]:
                    # we've already used this digit, permutation is no good
                    return []

                return [(missing_digit, new_carry)]

            # case 3:  unset digit is in the sum and in the addends.  we have work to do.
            # column looks like X - - X - X - -
            # try all the unused digits one by one
            candidates = []
            for k in self.digit_mapping.keys():
                if self.digit_mapping[k]:
                    continue

                column_sum = self.sum_of_addends(column) + (sum_letter_count - 1) * k + carry
                new_carry, missing_digit = divmod(column_sum, 10)
                if missing_digit == k:
                    candidates.append((k, new_carry))
            return candidates

        # case 2.  unset digit is in the addends.  it might appear more than once.
        # there can be multiple unused digits that would work.  try all possibilities.

        candidates = []
        missing_digit_count = column.unique_digits[unmapped_letter]
        for k in self.digit_mapping.keys():
            if self.digit_mapping[k]:
                continue

            if (missing_digit_count * k) % 10 == (
                    self.letters_to_letter_states[sum_letter].digit - carry - self.sum_of_addends(column)) % 10:
                column_sum = self.sum_of_addends(column) + missing_digit_count * k + carry
                new_carry = column_sum // 10
                candidates.append((k, new_carry))
        return candidates

    def resolve_columns(self, columns, carry):
        # return winning (digit, carry) tuple, or None

        column = columns[0]
        unmapped_letters = self.unmapped_letters(column)
        if len(unmapped_letters) > 1:
            raise ValueError("too many unmapped letters in column:  %s" % column)

        unmapped_letter = None
        if len(unmapped_letters) == 0:
            # don't have to determine a missing digit!  but see if this adds up.
            column_sum = self.sum_of_addends(column) + carry
            carry, digit = divmod(column_sum, 10)
            if digit != self.letters_to_letter_states[column[0]].digit:
                return None

            candidates = [(digit, carry)]
        else:
            unmapped_letter = unmapped_letters[0]
            candidates = self.candidate_digits(column, carry, unmapped_letters[0])

        if len(candidates) == 0:
            return None

        result = None
        if len(columns[1:]) == 0:
            # this is the last column.  if there are multiple candidates, look for
            # one with a 0 carry.  if there isn't one, lose.
            winners = list(filter(lambda x: x[1] == 0, candidates))
            if len(winners) == 0:
                return None
            winner = winners[0]
            if unmapped_letter:
                self.assign_digit(winner[0], unmapped_letter)
            return winner

        for d, c in candidates:
            if unmapped_letter:
                self.assign_digit(d, unmapped_letter)
            result_subsequent = self.resolve_columns(columns[1:], c)
            if result_subsequent is not None:
                result = (d, c)
                break

            if unmapped_letter:
                self.unassign_digit(d)

        # TODO - need to undo prior digit assignments in recursive calls if this one doesn't work.

        return result

    def permutation_works(self, letters_to_digits):
        if 0 in letters_to_digits.values():
            digits_to_letters = {v: k for k, v in letters_to_digits.items()}
            zeroletter = digits_to_letters[0]
            if not self.letters_to_letter_states[zeroletter].can_be_zero:
                # print("%s cannot map to 0, trying another" % zeroletter)
                return False

        for l in letters_to_digits.keys():
            self.assign_digit(letters_to_digits[l], l)

        result = self.resolve_columns(self.columns, 0)

        if not bool(result):
            # shit, revert this permutation
            self.unwind_mapping()

        return bool(result)

    def solution(self):
        # identify all of the independent letters.  eliminate 1 and 0 if these have already been determined.
        # this should work for > 2 addends.

        # returns the decrypted numbers if a solution exists, otherwise None.  if there are multiple solutions,
        # we'll never know.

        if not self.solvable:
            return None

        independent = dict(filter(lambda x: x[1].dependent == False, self.letters_to_letter_states.items()))

        independent_letters = list(independent.keys())
        # pprint(independent_letters)
        digits = {x for x in range(10)}
        for k in self.letters_to_letter_states.keys():
            if self.letters_to_letter_states[k].fixed:
                digits.remove(self.letters_to_letter_states[k].digit)

        for p in permutations(digits, len(independent_letters)):
            letters_to_digits = dict(zip(independent_letters, p))
            if self.permutation_works(letters_to_digits):
                addends = [self.decrypt_letter_string(a) for a in self.addends]
                result = self.decrypt_letter_string(self.result)
                if sum(addends) != result:
                    print("it don't add up")
                    print(p, independent_letters)
                    print(self.addends)
                    print(self.result)
                    print(addends)
                    print(result)
                    pprint(self.letters_to_letter_states)
                    return None
                return addends, result


def solution(addends, result):
    s = SolutionGraph(addends, result)
    answer = s.solution()
    return bool(answer)


if __name__ == '__main__':
    # addends = ["SEND", "MORE"]
    # result = "MONEY"
    # s = SolutionGraph(addends, result)

    # for _ in range(10):
    #     addends, result = make_crypto_sum(3, 3)
    #
    #     s = SolutionGraph(addends, result)

    for _ in range(111):
        addends_str, result_str, addends, result, decoder = make_crypto_sum(3, 5)
        s = SolutionGraph(addends_str, result_str)
        random_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(10)])
        solution_test = "test_%s_solution" % random_name
        perm_test = "test_%s_permutation" % random_name
        permutation = {}
        for letter in s.letters_to_letter_states:
            if not s.letters_to_letter_states[letter].dependent:
                permutation[letter] = decoder[letter]
        try:
            result = s.solution()
            if not result:
                print("######## incorrectly determined to be not solvable")
                print("""
    ########################
    # python -m unittest verbal_arithmetic_1307.SolveTest.%(perm_test)s
    def %(perm_test)s(self):
        addends_str = %(addends_str)s  # %(addends)s
        result_str = '%(result_str)s'  # %(result)s

        s = SolutionGraph(addends_str, result_str)
        works = s.permutation_works(%(permutation)s)
        self.assertTrue(works)

    # python -m unittest verbal_arithmetic_1307.SolveTest.%(solution_test)s
    def %(solution_test)s(self):
        addends_str = %(addends_str)s  # %(addends)s
        result_str = '%(result_str)s'  # %(result)s

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    ########################
            """ % {
                    "solution_test": solution_test,
                    "perm_test": perm_test,
                    "addends_str": addends_str,
                    "result_str": result_str,
                    "addends": addends,
                    "result": result,
                    "permutation": permutation
                }
                      )
                pprint(decoder)
                pprint(s.letters_to_letter_states)
                pprint(permutation)
                break
        except:
            print("######## exception!")
            print("""
    ########################
    # python -m unittest verbal_arithmetic_1307.SolveTest.%(perm_test)s
    def %(perm_test)s(self):
        addends_str = %(addends_str)s  # %(addends)s
        result_str = '%(result_str)s'  # %(result)s
    
        s = SolutionGraph(addends_str, result_str)
        works = s.permutation_works(%(permutation)s)
        self.assertTrue(works)
    
    # python -m unittest verbal_arithmetic_1307.SolveTest.%(solution_test)s
    def %(solution_test)s(self):
        addends_str = %(addends_str)s  # %(addends)s
        result_str = '%(result_str)s'  # %(result)s
    
        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)
    
    ########################
        """ % {
                "solution_test": solution_test,
                "perm_test": perm_test,
                "addends_str": addends_str,
                "result_str": result_str,
                "addends": addends,
                "result": result,
                "permutation": permutation
            }
                  )
            pprint(decoder)
            pprint(s.letters_to_letter_states)
            pprint(permutation)
            break


class SolveTest(unittest.TestCase):
    ########################
    # python -m unittest verbal_arithmetic_1307.SolveTest.test_zplfmliedy_permutation
    def test_zplfmliedy_permutation(self):
        addends_str = ['YW', 'MI']  # [70, 63]
        result_str = 'KII'  # 133

        s = SolutionGraph(addends_str, result_str)
        works = s.permutation_works({'M': 6, 'I': 3, 'Y': 7})
        self.assertTrue(works)

    # python -m unittest verbal_arithmetic_1307.SolveTest.test_zplfmliedy_solution
    def test_zplfmliedy_solution(self):
        addends_str = ['YW', 'MI']  # [70, 63]
        result_str = 'KII'  # 133

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    ########################
    # python -m unittest verbal_arithmetic_1307.SolveTest.test_fgxabreoii_permutation
    def test_fgxabreoii_permutation(self):
        addends_str = ['EELV', 'WOLX']  # [3346, 8041]
        result_str = 'XXEWA'  # 11387

        s = SolutionGraph(addends_str, result_str)
        works = s.permutation_works({'O': 0, 'V': 6, 'L': 4})
        self.assertTrue(works)

    # python -m unittest verbal_arithmetic_1307.SolveTest.test_fgxabreoii_solution
    def test_fgxabreoii_solution(self):
        addends_str = ['EELV', 'WOLX']  # [3346, 8041]
        result_str = 'XXEWA'  # 11387

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    # python -m unittest verbal_arithmetic_1307.SolveTest.test_exhxqvuwhg
    def test_exhxqvuwhg(self):
        addends_str = ['GE', 'QT']  # [60, 71]
        result_str = 'TMT'  # 131

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    # python -m unittest verbal_arithmetic_1307.SolveTest.test_fksztyrdsl
    def test_fksztyrdsl(self):
        addends_str = ['GL', 'AR']  # [40, 61]
        result_str = 'RLR'  # 101

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    def test_6_permutation(self):
        addends_str = ['VG', 'WG']  # [97, 27]
        result_str = 'JWM'  # 124

        s = SolutionGraph(addends_str, result_str)
        permutation = {'W': 2, 'G': 7}
        works = s.permutation_works(permutation)
        self.assertTrue(works)

    def test_6_solution(self):
        addends_str = ['VG', 'WG']  # [97, 27]
        result_str = 'JWM'  # 124

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    def test_5(self):
        addends_str = ['ZM', 'ZU']  # [29, 25]
        result_str = 'UQ'  # 54

        s = SolutionGraph(addends_str, result_str)
        permutation = dict(zip(['U', 'Z', 'M'], (1, 5, 9)))
        works = s.permutation_works(permutation)
        self.assertFalse(works)

        s = SolutionGraph(addends_str, result_str)
        answer = s.solution()
        self.assertIsNotNone(answer)

    def test_4(self):
        addends_str = ["ZQ", "RF"]  # 18, 93
        result_str = "ZZZ"  # 111

        s = SolutionGraph(addends_str, result_str)
        permutation = dict(zip(['F', 'R'], (3, 9)))
        works = s.permutation_works(permutation)
        self.assertTrue(works)

    def test_3(self):
        addends = ["GD", "JS"]
        result = "CGH"

        s = SolutionGraph(addends, result)
        self.assertIsNotNone(s.solution())

    def test_3_5(self):
        addends = ["GD", "JS"]
        result = "CGH"

        s = SolutionGraph(addends, result)
        permutation = dict(zip(['D', 'S', 'G'], (2, 3, 9)))
        works = s.permutation_works(permutation)
        self.assertFalse(works)

    def test_2(self):
        addends = ["TQ", "CW"]  # 86, 37
        result = "NFC"  # 123

        s = SolutionGraph(addends, result)
        permutation = dict(zip(['W', 'T', 'Q'], (7, 8, 6)))
        works = s.permutation_works(permutation)
        self.assertTrue(works)

    def test_1(self):
        addends = ["HY", "CV"]
        result = "VRS"

        s = SolutionGraph(addends, result)
        result = s.solution()
        self.assertIsNotNone(result)

    def test_0(self):
        addends = ["SEND", "MORE"]
        result = "MONEY"

        s = SolutionGraph(addends, result)
        result = s.solution()
        self.assertIsNotNone(result)


class InitializationTest(unittest.TestCase):
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


class ColumnTest(unittest.TestCase):
    def test_1(self):
        col = Column(['Y', 'E', 'D', 'E'])
        col.append('D')

        self.assertEqual(['Y', 'E', 'D', 'E', 'D'], [x for x in col])
        self.assertEqual('E', col[1])
        self.assertEqual('D', col[-1])
        self.assertEqual(5, len(col))
        self.assertEqual(3, col.num_unique_digits())
        self.assertEqual(2, col.unique_digits['D'])
        self.assertEqual(1, col.unique_digits['Y'])
        self.assertEqual("""['Y', 'E', 'D', 'E', 'D']""", str(col))

    def test_2(self):
        col = Column()

        for c in ['Y', 'E', 'D', 'E', 'D']:
            col.append(c)

        self.assertEqual(['Y', 'E', 'D', 'E', 'D'], [x for x in col])
        self.assertEqual('E', col[1])
        self.assertEqual('D', col[-1])
        self.assertEqual(5, len(col))
        self.assertEqual(3, col.num_unique_digits())
        self.assertEqual(2, col.unique_digits['D'])
        self.assertEqual(1, col.unique_digits['Y'])


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

    @unittest.skip
    def test_4(self):
        addends = ["GHANA", "GABON", "BHUTAN"]
        result = "ALBANIA"

        self.assertTrue(solution(addends, result))

    @unittest.skip
    def test_5(self):
        addends = ["SEAL", "SNAIL", "MONKEY"]
        result = "ANIMALS"

        self.assertTrue(solution(addends, result))

    @unittest.skip
    def test_6(self):
        addends = ["RICH", "POOR", "HAPPY"]
        result = "PEOPLE"

        self.assertTrue(solution(addends, result))

    def test_7(self):
        addends = ["LEET", "CODE"]
        result = "POINT"

        self.assertFalse(solution(addends, result))
