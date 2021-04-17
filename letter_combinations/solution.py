#!/usr/bin/env python

# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3701/

mapping = {
    2: ('a', 'b', 'c'),
    3: ('d', 'e', 'f'),
    4: ('g', 'h', 'i'),
    5: ('j', 'k', 'l'),
    6: ('m', 'n', 'o'),
    7: ('p', 'q', 'r', 's'),
    8: ('t', 'u', 'v'),
    9: ('w', 'x', 'x', 'z')
    }
    
def generate(arr):
    if len(arr) == 1:
        for i in mapping[arr[0]]:
            yield i

    if len(arr) >= 2:
        for i in mapping[arr[0]]:
            for j in generate(arr[1:]):
                yield i + j
                
if __name__ == '__main__':
    arr = [7, 2, 3]
    for i in generate(arr):
        print i,
    print
    
    
