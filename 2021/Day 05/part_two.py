"""
Advent of Code 2021
Day 5: Hydrothermal Venture (Part Two)
"""

import numpy as np

with open("./input.txt", encoding="utf-8") as file:
    data = [[int(i) for i in j.split(",")] for j in file.read().replace(" -> ", ",").splitlines()]

shape = (1000, 1000)
grid = np.zeros(shape)

for vec in data:
    if vec[0] == vec[2]:
        if vec[1] < vec[3]:
            step = 1
        else:
            step = -1
        for n in range(vec[1], vec[3] + step, step):
            grid[vec[0]][n] += 1
    elif vec[1] == vec[3]:
        index = 0
        if vec[0] < vec[2]:
            step = 1
        else:
            step = -1
        for n in range(vec[0], vec[2] + step, step):
            grid[n][vec[1]] += 1
    else:
        if vec[0] < vec[2]:
            step_x = 1
        else:
            step_x = -1
        if vec[1] < vec[3]:
            step_y = 1
        else:
            step_y = -1
        x = range(vec[0], vec[2] + step_x, step_x)
        y = range(vec[1], vec[3] + step_y, step_y)
        for i in range(len(x)):
            grid[x[i]][y[i]] += 1

result = (grid > 1).sum()

print("Result =", result)
