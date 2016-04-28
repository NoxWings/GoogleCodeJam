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
    n = read_int()
    bff = [x - 1 for x in read_int_multi()]

    longest_cycle = 0
    chains = {}

    for child in xrange(n):
        used_child = [False] * n
        current = child
        while not used_child[current]:
            used_child[current] = True
            current = bff[current]

        count = used_child.count(True)

        # Close cycle
        if child == current:
            longest_cycle = max(longest_cycle, count)

        # Open chain
        if bff[bff[current]] == current:
            max_current = chains[current] if current in chains else 0
            chains[current] = max(max_current, count)

    longest_chain_cycle = sum(chains.itervalues()) - len(chains)
    return max(longest_cycle, longest_chain_cycle)


#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
