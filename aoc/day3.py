#!/usr/bin/env python

import re

def part1(puzzle_input):
    pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    matches = re.findall(pattern, puzzle_input)
    result = 0
    for match in matches:
        mul = list(map(int, match.split('(')[1].strip(')').split(',')))
        result += mul[0] * mul[1]
    return result

def part2(puzzle_input):
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, puzzle_input)
    result = 0
    mul_enabled = True
    for match in matches:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif mul_enabled:
            mul = list(map(int, match.split('(')[1].strip(')').split(',')))
            result += mul[0] * mul[1]
    return result
