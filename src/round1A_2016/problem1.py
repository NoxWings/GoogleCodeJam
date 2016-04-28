#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
from __future__ import unicode_literals


#===============================================================================
def read_input(strip=True):
    return raw_input().strip() if strip else raw_input()


def read_input_multi(strip=True):
    return read_input(strip).split()


def read_int():
    return int(read_input())


def read_int_multi():
    return [int(s) for s in read_input_multi()]


def print_solution(i, solution):
    print('Case #{}: {}'.format(i, solution))
#===============================================================================


def solve():
    word = read_input()
    last_word = []
    for l in word:
        if last_word:
            if (ord(l) >= ord(last_word[0])):
                last_word.insert(0, l)
            else:
                last_word.append(l)
        else:
            last_word.append(l)
    return ''.join(last_word)

#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
