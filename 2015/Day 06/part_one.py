"""
Advent of Code 2015
Day 6: Probably a Fire Hazard (Part One)
"""

import numpy as np

with open("./input.txt", encoding="utf-8") as file:
    data = [(i[:i.index("through")-1], i[i.index("through"):]) for i in file.read().splitlines()]

grid = np.zeros((1000, 1000))

for command in data:
    v1 = [int(i) for i in command[0][command[0].rindex(" ")+1:].split(",")]
    v2 = [int(i) for i in command[1][command[1].rindex(" ")+1:].split(",")]
    if command[0].startswith("turn on"):
        for x in range(v1[0], v2[0]+1):
            for y in range(v1[1], v2[1]+1):
                grid[x][y] = 1
    elif command[0].startswith("turn off"):
        for x in range(v1[0], v2[0]+1):
            for y in range(v1[1], v2[1]+1):
                grid[x][y] = 0
    else:
        for x in range(v1[0], v2[0]+1):
            for y in range(v1[1], v2[1]+1):
                grid[x][y] = abs(grid[x][y] - 1)

unique, counts = np.unique(grid, return_counts=True)
dic = dict(zip(unique, counts))

print("Result =", dic[1])
