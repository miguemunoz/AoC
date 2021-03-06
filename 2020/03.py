#!/usr/bin/env python3

"""
    AoC2020, 3rd day ( https://adventofcode.com/2020/day/3 )
"""

from functools import reduce

def aoc2020d3(filename, first_star):
    
    slopes = [(3,1)] if first_star else [(3,1), (1,1),(5,1),(7,1),(1,2)]
    
    solution = []
    
    geomap =  [list(x.strip()) * 3300 for x in open(filename)]
    
    for i,j in slopes:
    
        x, y = 0, 0 # start position
        
        trees = 0 # number of trees found for the slope
        
        while y < len(geomap):
            if geomap[y][x] == '.':
                geomap[y][x] = 'O'
            elif geomap[y][x] == '#':
                geomap[y][x] = 'X'
                trees += 1
            x += i
            y += j
        
        solution.append(trees)
    
    return reduce((lambda x, y: x * y), solution)

if __name__ == "__main__":
    print(f'aoc2020d3s1: {aoc2020d3("input.txt", True)}')
    print(f'aoc2020d3s2: {aoc2020d3("input.txt", False)}')
