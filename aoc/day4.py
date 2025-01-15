#!/usr/bin/env python

import math

def part1(puzzle_input):
    matrix = [list(x.strip()) for x in puzzle_input.strip().split('\n')]
    matches = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 'X':
                matches += search_for_xmas_word(matrix, x, y)
    return matches

def part2(puzzle_input):
    matrix = [list(x.strip()) for x in puzzle_input.strip().split('\n')]
    matches = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 'M' or matrix[x][y] == 'S':
                if search_mas_in_x_shape(matrix, x, y):
                    matches += 1
    return matches

def search_for_xmas_word(matrix, startx, starty):
    xmas_matches = 0
    # vertical
    try:
        if matrix[startx][starty + 1] == 'M' and \
           matrix[startx][starty + 2] == 'A' and \
           matrix[startx][starty + 3] == 'S':
            xmas_matches += 1
            print('vertical match : {},{} => {},{}'.format(startx, starty, startx, starty + 3))
    except IndexError:
        pass
    # vertical reverse
    try:
        if matrix[startx][starty - 1] == 'M' and \
           matrix[startx][starty - 2] == 'A' and \
           matrix[startx][starty - 3] == 'S' and \
           starty - 3 >= 0:
            xmas_matches += 1
            print('vertical reverse match : {},{} => {},{}'.format(startx, starty, startx, starty -3))
    except IndexError:
        pass
    # horizontal
    try:
        if matrix[startx + 1][starty] == 'M' and \
           matrix[startx + 2][starty] == 'A' and \
           matrix[startx + 3][starty] == 'S':
            xmas_matches += 1
            print('horizontal match : {},{} => {},{}'.format(startx, starty, startx + 3, starty))            
    except IndexError:
        pass
    # horizontal reverse
    try:
        if matrix[startx - 1][starty] == 'M' and \
           matrix[startx - 2][starty] == 'A' and \
           matrix[startx - 3][starty] == 'S' and \
           startx - 3 >= 0:
            xmas_matches += 1
            print('horizontal reverse match : {},{} => {},{}'.format(startx, starty, startx - 3, starty))
    except IndexError:
        pass
    # diagonal right down
    try:
        if matrix[startx + 1][starty + 1] == 'M' and \
           matrix[startx + 2][starty + 2] == 'A' and \
           matrix[startx + 3][starty + 3] == 'S':
            xmas_matches += 1
            print('diagonal right down match : {},{} => {},{}'.format(startx, starty, startx +3, starty + 3))
    except IndexError:
        pass
    # diagonal right up
    try:
        if matrix[startx - 1][starty + 1] == 'M' and \
           matrix[startx - 2][starty + 2] == 'A' and \
           matrix[startx - 3][starty + 3] == 'S' and \
           startx - 3 >= 0:
            xmas_matches += 1
            print('diagonal right up match : {},{} => {},{}'.format(startx, starty, startx - 3, starty + 3))
    except IndexError:
        pass
    # diagonal left down
    try:
        if matrix[startx + 1][starty - 1] == 'M' and \
           matrix[startx + 2][starty - 2] == 'A' and \
           matrix[startx + 3][starty - 3] == 'S' and \
           starty - 3 >= 0:
            xmas_matches += 1
            print('diagonal left down match : {},{} => {},{}'.format(startx, starty, startx + 3, starty - 3))
    except IndexError:
        pass
    # diagonal left up
    try:
        if matrix[startx - 1][starty - 1] == 'M' and \
           matrix[startx - 2][starty - 2] == 'A' and \
           matrix[startx - 3][starty - 3] == 'S' and \
           startx - 3 >= 0 and starty - 3 >= 0:
            xmas_matches += 1
            print('diagonal left up match : {},{} => {},{}'.format(startx, starty, startx -3, starty - 3))
    except IndexError:
        pass

    return xmas_matches

def search_mas_in_x_shape(matrix, startx, starty):

    # M.S
    # .A.
    # M.S

    try:
        if matrix[startx][starty] == 'M' and \
           matrix[startx + 1][starty + 1] == 'A' and \
           matrix[startx + 2][starty + 2] == 'S' and \
           matrix[startx + 2][starty] == 'M' and \
           matrix[startx][starty + 2] == 'S':
            return True
    except IndexError:
        pass

    # S.S
    # .A.
    # M.M

    try:
        if matrix[startx][starty] == 'S' and \
           matrix[startx + 1][starty + 1] == 'A' and \
           matrix[startx + 2][starty + 2] == 'M' and \
           matrix[startx + 2][starty] == 'M' and \
           matrix[startx][starty + 2] == 'S':
            return True
    except IndexError:
        pass
    # S.M
    # .A.
    # S.M

    try:
        if matrix[startx][starty] == 'S' and \
           matrix[startx + 1][starty + 1] == 'A' and \
           matrix[startx + 2][starty + 2] == 'M' and \
           matrix[startx + 2][starty] == 'S' and \
           matrix[startx][starty + 2] == 'M':
            return True
    except IndexError:
        pass     
    
    # M.M
    # .A.
    # S.S

    try:
        if matrix[startx][starty] == 'M' and \
           matrix[startx + 1][starty + 1] == 'A' and \
           matrix[startx + 2][starty + 2] == 'S' and \
           matrix[startx + 2][starty] == 'S' and \
           matrix[startx][starty + 2] == 'M':
            return True
    except IndexError:
        pass