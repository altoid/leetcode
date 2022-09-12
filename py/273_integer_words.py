#!/usr/bin/env python

# url for problem here

import unittest
from pprint import pprint
import random


def one_digit_phrase(n):
    assert len(n) == 1

    if n == '1':
        return ['One']
    if n == '2':
        return ['Two']
    if n == '3':
        return ['Three']
    if n == '4':
        return ['Four']
    if n == '5':
        return ['Five']
    if n == '6':
        return ['Six']
    if n == '7':
        return ['Seven']
    if n == '8':
        return ['Eight']
    if n == '9':
        return ['Nine']

    return []


def two_digit_phrase(n):
    assert len(n) <= 2

    if len(n) < 2:
        return one_digit_phrase(n)

    if n == '10':
        return ['Ten']
    if n == '11':
        return ['Eleven']
    if n == '12':
        return ['Twelve']
    if n == '13':
        return ['Thirteen']
    if n == '14':
        return ['Fourteen']
    if n == '15':
        return ['Fifteen']
    if n == '16':
        return ['Sixteen']
    if n == '17':
        return ['Seventeen']
    if n == '18':
        return ['Eighteen']
    if n == '19':
        return ['Nineteen']

    phrase = []
    if n.startswith('2'):
        phrase.append('Twenty')
    elif n.startswith('3'):
        phrase.append('Thirty')
    elif n.startswith('4'):
        phrase.append('Forty')
    elif n.startswith('5'):
        phrase.append('Fifty')
    elif n.startswith('6'):
        phrase.append('Sixty')
    elif n.startswith('7'):
        phrase.append('Seventy')
    elif n.startswith('8'):
        phrase.append('Eighty')
    elif n.startswith('9'):
        phrase.append('Ninety')
    elif n.startswith('0'):
        pass

    if not n.endswith('0'):
        phrase += one_digit_phrase(n[1:])

    return phrase


def three_digit_phrase(n):
    """
    n is a string representing a number of up to 3 digits.
    """
    assert 1 <= len(n) <= 3

    if len(n) == 1:
        return one_digit_phrase(n)

    if len(n) == 2:
        return two_digit_phrase(n)

    if n == '000':
        return []

    phrase = []

    if not n.startswith('0'):
        phrase += one_digit_phrase(n[0])
        phrase.append('Hundred')

    phrase += two_digit_phrase(n[1:])

    return phrase


# 2,147,483,647
def solution(n: int):
    if n == 0:
        return 'Zero'

    magnitudes = ['Billion', 'Million', 'Thousand', '']
    n_str = str(n)
    ncommas = (len(n_str) - 1) // 3
    n_str_rev = n_str[::-1]
    splits = []
    for i in range(-1, -len(n_str) - 1, -3):
        splits.append(n_str[i:i - 3:-1])
    splits = splits[::-1]
    splits = [x[::-1] for x in splits]

    phrase = []
    m = len(magnitudes) - len(splits)
    for s in splits:
        snippet = three_digit_phrase(s)
        if snippet:
            snippet += [magnitudes[m]]
            # print("%s %s" % (snippet, magnitudes[m]))
            phrase += snippet

        m += 1

    return ' '.join(phrase).strip()


if __name__ == '__main__':
    # 1 - 99 without zero padding
    # for i in range(1, 100):
    #     s = str(i)
    #     phrase = ' '.join(two_digit_phrase(s))
    #     print("%s: %s" % (s, phrase))
    # for i in range(100, 200):
    #     s = str(i)
    #     phrase = ' '.join(three_digit_phrase(s))
    #     print("%s: %s" % (s, phrase))

    # while True:
    #     n = random.randint(1, 999)
    #     s = str(n)
    #     #print("trying %s" % s)
    #     phrase = ' '.join(three_digit_phrase(s))
    #     print("%s: %s" % (s, phrase))

    print(solution(2147483647))
    pass


class MyTest(unittest.TestCase):
    def test_powers_of_10(self):
        self.assertEqual("Zero", solution(0))
        self.assertEqual("One", solution(1))
        self.assertEqual("Ten", solution(10))
        self.assertEqual("One Hundred", solution(100))
        self.assertEqual("One Thousand", solution(1000))
        self.assertEqual("Ten Thousand", solution(10000))
        self.assertEqual("One Hundred Thousand", solution(100000))
        self.assertEqual("One Million", solution(1000000))
        self.assertEqual("Ten Million", solution(10000000))
        self.assertEqual("One Hundred Million", solution(100000000))
        self.assertEqual("One Billion", solution(1000000000))

    def test_2(self):
        self.assertEqual("One Hundred One", solution(101))
        self.assertEqual("One Million Ten", solution(1000010))
        self.assertEqual("One Million One Hundred One", solution(1000101))

    def test_3(self):
        self.assertEqual("Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven", solution(2 ** 31 - 1))