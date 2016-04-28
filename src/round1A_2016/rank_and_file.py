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


def solve_matrix(n, soldier_lists):
    solution = []
    used_edges = []

    for iteration in xrange(n):
        valid_soldiers = [(i, l) for i, l in enumerate(soldier_lists) if i not in used_edges]
        # print valid_soldiers

        top_left = min([min([x for j, x in enumerate(l) if j >= iteration]) for i, l in valid_soldiers])
        #print("top: {}".format(top_left))
        edges = [l for i, l in valid_soldiers if l[iteration] == top_left]
        used_edges += [i for i, l in valid_soldiers if l[iteration] == top_left]

        if len(edges) == 2:
            edge_heights = edges[0] + edges[1]
            # print edge_heights
            for soldiers in soldier_lists:
                value = soldiers[iteration]
                # print "value: " + str(value)
                edge_heights.remove(value)
            solution.append(edge_heights[0])
            used_edges
        else:
            solution.append(edges[0][iteration])

    return ' '.join([str(x) for x in solution])

#------------------------------------------------------------------------------


def solve():
    n = read_int()
    num_lists = 2 * n - 1
    soldier_lists = [read_int_multi() for _ in xrange(num_lists)]
    line = solve_matrix(n, soldier_lists)
    return line

#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
