#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Problem B. Tidy Numbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
# ==============================================================================


def find_fault(n):
    """Find and return the index of the faulty one."""
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            return i
    return None


def solve():
    """Problem solution implementation."""
    n = list(str(int(input().strip())))  # str(int()) to remove any leading zeros
    n = [int(d) for d in n]
    f = find_fault(n)
    while f is not None:
        n[f - 1] -= 1
        for i in range(f, len(n)):
            n[i] = 9
        f = find_fault(n)
    return str(int(''.join(str(d) for d in n)))


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
