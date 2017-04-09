#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0
# ==============================================================================


def clean_unused(p):
    """Remove happy start."""
    while p and p[0]:
        p = p[1:]
    return p


def count_flips(s, k):
    """Count the flips and return the solution."""
    c = 0
    s = clean_unused(s)
    while s:
        if k > len(s):
            return 'IMPOSSIBLE'
        for x in range(k):
            s[x] = not s[x]
        c += 1
        s = clean_unused(s)
    return str(c)


def solve():
    """Problem solution implementation."""
    s, k = input().strip().split()
    s, k = [x == '+' for x in s], int(k)
    return count_flips(s, k)


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
