"""
Advent of Code 2021
Day 7: The Treachery of Whales (Part Two)
"""

import numpy as np

with open("./input.txt", encoding="utf-8") as file:
    data = np.array([int(i) for i in file.read().split(",")])

def fuel_calc(n):
    return ((1+n)*n)/2

start = min(data)
end = max(data)

fuel = np.inf

for pos in range(start, end+1):
    displacement = sum(map(fuel_calc, np.absolute(data - pos)))
    if displacement < fuel:
        fuel = displacement

print("Result =", fuel)
