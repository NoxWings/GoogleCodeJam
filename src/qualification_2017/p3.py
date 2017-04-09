#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Problem C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
# ==============================================================================
from collections import OrderedDict
from decimal import ROUND_HALF_UP, Decimal, getcontext


def next_split(length):
    """Find next split numbers."""
    d = (length - 1) / Decimal(2)
    d_max = d.to_integral_value()
    d_min = int(d)
    return [d_max, d_min]


def solve():
    """Problem solution implementation."""
    n, k = [int(x) for x in input().split()]
    # optimization
    if k == n:
        return '0 0'
    # processing
    c = OrderedDict({n: 1})
    while c.keys() and k > 1:
        length = next(iter(c))  # First key == largest key
        update_val = min(c[length], k - 1)
        # Update the number of steps taken
        k -= update_val
        # Update the lengths
        new_lengths = filter(lambda x: x > 0, next_split(length))
        for nl in new_lengths:
            c[nl] = c.get(nl, 0) + update_val
        # Delete obsolete keys to save memory
        c[length] -= update_val
        if c[length] == 0:
            del c[length]

    l_r = next_split(next(iter(c)))
    return '{} {}'.format(max(l_r), min(l_r))


# ==============================================================================
if __name__ == '__main__':
    getcontext().rounding = ROUND_HALF_UP
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
