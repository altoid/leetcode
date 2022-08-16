#!/usr/bin/env python

def reverse_int(x):
    ax = int(str(abs(x))[::-1])
    if ax > 2 ** 31:
        return 0
    if x < 0:
        ax = -ax
    return ax

print 2 ** 32
print 2 ** 31
#print reverse_int(123)
#print reverse_int(-123)
#print reverse_int(2 ** 34)
#
    
print reverse_int(1563847412)
