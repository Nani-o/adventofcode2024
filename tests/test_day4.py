#!/usr/bin/env python

import pytest
from aoc.day4 import part1, part2

def test_part1():
    input = """MMMSXXMASM
               MSAMXMSMSA
               AMXSXMAAMM
               MSAMASMSMX
               XMASAMXAMM
               XXAMMXXAMA
               SMSMSASXSS
               SAXAMASAAA
               MAMMMXMMMM
               MXMXAXMASX"""
    solution = part1(input)
    assert solution == 18

def test_part2():
    input = """MMMSXXMASM
               MSAMXMSMSA
               AMXSXMAAMM
               MSAMASMSMX
               XMASAMXAMM
               XXAMMXXAMA
               SMSMSASXSS
               SAXAMASAAA
               MAMMMXMMMM
               MXMXAXMASX"""
    solution = part2(input)
    assert solution == 9