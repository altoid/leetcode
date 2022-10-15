#!/usr/bin/env python

# https://leetcode.com/problems/dinner-plate-stacks/

import unittest
from pprint import pprint
import random
import heapq


def solution():
    pass


class DinnerPlates:
    # never allow the rightmost stack to become empty.  if we clear it out, remove it.

    # we'll maintain indices of stacks with capacity in a heap.  for a stack with no remaining
    # capacity, remove it from the heap.  requires O(n) scan + remove + heapify.

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.available_stacks = []

    def push(self, val):
        if len(self.available_stacks) == 0:
            newstack = [val]
            if len(newstack) < self.capacity:
                new_index = len(self.stacks)
                heapq.heappush(self.available_stacks, new_index)
            self.stacks.append(newstack)
        else:
            available = self.stacks[self.available_stacks[0]]
            available.append(val)
            if len(available) == self.capacity:
                heapq.heappop(self.available_stacks)

    def pop(self):
        index = len(self.stacks) - 1
        if index < 0:
            return -1

        stack = self.stacks[-1]

        if len(stack) == self.capacity:
            heapq.heappush(self.available_stacks, index)

        result = stack.pop()

        # remove all rightmost empty stacks
        while self.stacks and len(self.stacks[-1]) == 0:
            try:
                last_index = len(self.stacks) - 1
                self.available_stacks.remove(last_index)
            except ValueError:
                pass
            finally:
                self.stacks.pop()

        heapq.heapify(self.available_stacks)

        return result

    def popAtStack(self, index):
        if index == len(self.stacks) - 1:
            return self.pop()

        stack = self.stacks[index]
        if len(stack) == 0:
            return -1

        if len(stack) == self.capacity:
            heapq.heappush(self.available_stacks, index)

        return stack.pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


if __name__ == '__main__':
    pass


class MyTest(unittest.TestCase):
    def test_push_and_pop(self):
        d = DinnerPlates(3)
        self.assertEqual(-1, d.pop())

        for i in range(1, 10):
            d.push(i)

        self.assertEqual(3, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

        d.push(10)

        self.assertEqual(4, len(d.stacks))
        self.assertEqual(3, d.available_stacks[0])
        self.assertEqual(1, len(d.available_stacks))

        for i in range(10, 0, -1):
            result = d.pop()
            self.assertEqual(i, result)

        self.assertEqual(-1, d.pop())

    def test_pop_at_stack(self):
        # create 5 stacks.  empty out the middle 3.  then see what pop does.
        # make sure pop correctly removes all empty rightmost stacks.

        d = DinnerPlates(3)
        self.assertEqual(-1, d.pop())

        for i in range(1, 16):
            d.push(i)

        for _ in range(d.capacity):
            d.popAtStack(1)

        for _ in range(d.capacity):
            d.popAtStack(2)

        for _ in range(d.capacity):
            d.popAtStack(3)

        self.assertEqual(3, len(d.available_stacks))
        self.assertEqual(1, d.available_stacks[0])

        self.assertEqual(-1, d.popAtStack(1))
        self.assertEqual(-1, d.popAtStack(2))
        self.assertEqual(-1, d.popAtStack(3))

        self.assertEqual(15, d.pop())
        self.assertEqual(14, d.pop())
        self.assertEqual(13, d.pop())

        self.assertEqual(1, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

        self.assertEqual(3, d.pop())
        self.assertEqual(2, d.pop())
        self.assertEqual(1, d.pop())
        self.assertEqual(-1, d.pop())

        self.assertEqual(0, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

    def test_push(self):
        # make sure push fills holes

        d = DinnerPlates(3)
        self.assertEqual(-1, d.pop())

        for i in range(1, 16):
            d.push(i)

        for _ in range(d.capacity):
            d.popAtStack(1)

        for _ in range(d.capacity):
            d.popAtStack(2)

        for _ in range(d.capacity):
            d.popAtStack(3)

        for i in range(100, 1000, 100):
            d.push(i)

        self.assertEqual(5, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

        d.push(666)

        self.assertEqual(6, len(d.stacks))
        self.assertEqual(1, len(d.available_stacks))
        self.assertEqual(5, d.available_stacks[0])

        check = [666, 15, 14, 13, 900, 800, 700, 600, 500, 400, 300, 200, 100, 3, 2, 1]
        for i in check:
            self.assertEqual(i, d.pop())

        self.assertEqual(-1, d.pop())

    def test_capacity_1(self):
        d = DinnerPlates(1)

        for i in range(1, 21):
            d.push(i)

        self.assertEqual(20, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

        p = d.pop()

        self.assertEqual(20, p)
        self.assertEqual(19, len(d.stacks))
        self.assertEqual(0, len(d.available_stacks))

        p = d.popAtStack(10)

        self.assertEqual(11, p)
        self.assertEqual(1, len(d.available_stacks))
        self.assertEqual(10, d.available_stacks[0])
