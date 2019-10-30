#!/usr/bin/env python

import unittest


def dedup(arr):
    """
    Given a sorted array nums, remove the duplicates in-place such
    that duplicates appeared at most twice and return the new length.

    Do not allocate extra space for another array, you must do this
    by modifying the input array in-place with O(1) extra memory.

    :param arr:
    :return:  length of de-duped array
    """

    if len(arr) < 3:
        return len(arr)

    current_value = arr[0]
    cv_count = 1
    i = 1
    array_len = len(arr)
    while i < array_len:
        if arr[i] != current_value:
            current_value = arr[i]
            cv_count = 1
        else:
            cv_count += 1
            if cv_count > 2:
                # find the next value not equal to the one we are pointing at.
                # from there to the end of the array, slide everything over (if
                # we can).
                j = i + 1
                while j < array_len:
                    if arr[j] != current_value:
                        break
                    j += 1
                k = i
                while j < array_len:
                    arr[k] = arr[j]
                    k += 1
                    j += 1
                array_len = k
        i += 1

    return array_len


class MyTest(unittest.TestCase):
    def test_mono(self):
        arr = [1]
        result = 1
        self.assertEqual(result, dedup(arr))
        self.assertEqual([1], arr[:result])

        arr = [1, 1]
        result = 2
        self.assertEqual(result, dedup(arr))
        self.assertEqual([1, 1], arr[:result])

        arr = [1, 1, 1]
        result = 2
        self.assertEqual(result, dedup(arr))
        self.assertEqual([1, 1], arr[:result])

    def test1(self):
        arr = [1, 1, 1, 2, 2, 3]
        result = 5
        self.assertEqual(result, dedup(arr))
        self.assertEqual([1, 1, 2, 2, 3], arr[:result])

    def test2(self):
        arr = [0, 0, 0, 1, 1, 1, 1, 2, 3, 3]
        result = 7
        self.assertEqual(result, dedup(arr))
        self.assertEqual([0, 0, 1, 1, 2, 3, 3], arr[:result])

