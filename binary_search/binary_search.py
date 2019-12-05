# utilities for binary search of an array

import unittest


def search_helper(arr, target, left, right):
    if right < left:
        return None

    m = (left + right) / 2
    if arr[m] == target:
        return m

    if target < arr[m]:
        return search_helper(arr, target, left, m - 1)

    return search_helper(arr, target, m + 1, right)


def search(arr, target):
    """

    :param arr:
    :param target:
    :return: the index of target in the array.  None if not found.  if the target appears more than once
    in the array, the index returned is indeterminate; it will point to the target value but which occurrence
    is not defined.
    """

    if len(arr) == 0:
        return None

    return search_helper(arr, target, 0, len(arr) - 1)


def search_leftmost(arr, target, left, right):
    """
    return the index of the leftmost occurrence of <target> in <arr>.  returns None if target is not in array.

    :param arr:
    :param target:
    :param left:
    :param right:
    :return:
    """
    if right < left:
        return None

    m = (left + right) / 2
    if arr[m] == target:
        lefter = search_leftmost(arr, target, left, m - 1)
        return m if lefter is None else lefter

    if arr[m] < target:
        return search_leftmost(arr, target, m + 1, right)

    return search_leftmost(arr, target, left, m - 1)


def search_rightmost(arr, target, left, right):
    """
    return the index of the rightmost occurrence of <target> in <arr>.  returns None if target is not in array.

    :param arr:
    :param target:
    :param left:
    :param right:
    :return:
    """
    if right < left:
        return None

    m = (left + right) / 2
    if arr[m] == target:
        righter = search_rightmost(arr, target, m + 1, right)
        return m if righter is None else righter

    if arr[m] > target:
        return search_rightmost(arr, target, left, m - 1)

    return search_rightmost(arr, target, m + 1, right)


def search_range(arr, target):
    """

    :param arr:
    :param target:
    :return:  pair of values indicating left and right indices of the subrange of values that are ==
    target.  returns None if target not found.
    """

    if len(arr) == 0:
        return None

    # look for the leftmost occurrence of target
    left = search_leftmost(arr, target, 0, len(arr) - 1)
    right = search_rightmost(arr, target, 0, len(arr) - 1)

    if left is not None and right is not None:
        return left, right


def search_loc_helper(arr, target, left, right):
    if right < left:
        # TODO:  will this ever happen?
        return None

    m = (left + right) / 2
    if right - left < 2:
        if arr[m] < target:
            return m + 1

        return m

    if arr[m] == target:
        return m

    if target < arr[m]:
        return search_loc_helper(arr, target, left, m - 1)

    return search_loc_helper(arr, target, m + 1, right)


def search_loc(arr, target):
    """
    :param arr:
    :param target:
    :return: the index of where target would reside in arr if we were to insert it.
    """

    if len(arr) == 0:
        return 0

    return search_loc_helper(arr, target, 0, len(arr) - 1)


def search_largest_less_than(arr, target):
    # give me the (leftmost) index of the largest value in a that is strictly less than target.
    # binary search into the array for where target would go if we were to insert it.

    here = search_loc(arr, target)
    lefter = search_leftmost(arr, target, 0, here - 1)
    if lefter is not None:
        here = lefter

    if here > 0:
        # see if there is an occurrence of target that is to the left of <here>
        return here - 1


def search_smallest_greater_than(arr, target):
    # give me the (rightmost) index of the smallest value in a that is strictly greater than target
    here = search_loc(arr, target)
    righter = search_rightmost(arr, target, here + 1, len(arr) - 1)
    if righter is not None:
        here = righter

    if arr[here] != target:
        return here

    if here < len(arr) - 1:
        return here + 1


class BSTest(unittest.TestCase):

    def test_search_degenerate(self):
        self.assertIsNone(search([], 42))

    def test_search_exists(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(search(a, 3), 2)
        self.assertEqual(search(a, 1), 0)
        self.assertEqual(search(a, 6), 5)

    def test_search_not_exists(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertIsNone(search(a, 33))

    def test_search_range_degenerate(self):
        self.assertIsNone(search_range([], 42))

    def test_search_leftmost(self):
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertEqual(0, search_leftmost(a, 1, 0, len(a) - 1))
        self.assertEqual(1, search_leftmost(a, 2, 0, len(a) - 1))
        self.assertEqual(3, search_leftmost(a, 3, 0, len(a) - 1))
        self.assertEqual(6, search_leftmost(a, 4, 0, len(a) - 1))
        self.assertIsNone(search_leftmost(a, 42, 0, len(a) - 1))

    def test_search_rightmost(self):
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertEqual(0, search_rightmost(a, 1, 0, len(a) - 1))
        self.assertEqual(2, search_rightmost(a, 2, 0, len(a) - 1))
        self.assertEqual(5, search_rightmost(a, 3, 0, len(a) - 1))
        self.assertEqual(9, search_rightmost(a, 4, 0, len(a) - 1))
        self.assertIsNone(search_rightmost(a, 42, 0, len(a) - 1))

    def test_search_range(self):
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertEqual((0, 0), search_range(a, 1))
        self.assertEqual((1, 2), search_range(a, 2))
        self.assertEqual((3, 5), search_range(a, 3))
        self.assertEqual((6, 9), search_range(a, 4))
        self.assertIsNone(search_range(a, 11))

    def test_largest_less_than(self):
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertIsNone(search_largest_less_than(a, 1))
        self.assertEqual(0, search_largest_less_than(a, 2))
        self.assertEqual(2, search_largest_less_than(a, 3))
        self.assertEqual(5, search_largest_less_than(a, 4))
        self.assertEqual(9, search_largest_less_than(a, 5))

    def test_search_loc_degenerate(self):
        a = []
        self.assertEqual(search_loc(a, 3), 0)

    def test_search_loc(self):
        a = [1, 3, 5, 7, 9, 11, 13]

        self.assertEqual(search_loc(a, 0), 0)
        self.assertEqual(search_loc(a, 1), 0)
        self.assertEqual(search_loc(a, 2), 1)
        self.assertEqual(search_loc(a, 3), 1)
        self.assertEqual(search_loc(a, 8), 4)
        self.assertEqual(search_loc(a, 13), 6)
        self.assertEqual(search_loc(a, 111), 7)

    def test_largest_less_than_no_target(self):
        a = [1, 3, 5, 7, 9, 11, 13]

        self.assertIsNone(search_largest_less_than(a, 1))
        self.assertEqual(3, search_largest_less_than(a, 8))
        self.assertEqual(6, search_largest_less_than(a, 111))

    def test_smallest_greater_than(self):
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertEqual(1, search_smallest_greater_than(a, 1))
        self.assertEqual(3, search_smallest_greater_than(a, 2))
        self.assertEqual(6, search_smallest_greater_than(a, 3))
        self.assertEqual(10, search_smallest_greater_than(a, 4))
        self.assertIsNone(search_smallest_greater_than(a, 5))

    def test_smallest_greater_than_no_target(self):
        a = [1, 3, 5, 7, 9, 11, 13]

        self.assertIsNone(search_smallest_greater_than(a, 13))
        self.assertEquals(4, search_smallest_greater_than(a, 8))
        self.assertEquals(0, search_smallest_greater_than(a, 0))

    def test_smallest_greater_than_no_target_II(self):
        a = [19, 34]

        self.assertEquals(0, search_smallest_greater_than(a, 18.5))
