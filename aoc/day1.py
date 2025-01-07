#!/usr/bin/env python

import math

def part1(puzzle_input):
    #first_list = list(map(int, [x.split(' ')[0] for x in puzzle_input.split('\n')]))
    first_list, second_list = get_lists(puzzle_input)
    distances = []
    while len(first_list) > 0:
        min1 = min(first_list)
        min2 = min(second_list)
        distance = abs(min1 - min2)
        distances.append(distance)
        first_list.remove(min1)
        second_list.remove(min2)
    return sum(distances)

def part2(puzzle_input):
    first_list, second_list = get_lists(puzzle_input)
    similarity_scores = []
    for value in first_list:
        matches = [x for x in second_list if x == value]
        similarity_scores.append(value * len(matches))
    return sum(similarity_scores)


def get_lists(puzzle_input):
    full_list = list(map(int, puzzle_input.split()))
    first_list = full_list[::2]
    second_list = full_list[1::2]
    return first_list, second_list