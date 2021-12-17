"""
Advent of Code 2021
Day 2: Sonar Sweep (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = [int(i) for i in file.read().splitlines()]

previous = sum(data[:3])
increases = 0

for index in range(1, len(data)):
    measurement = sum(data[index:index+3])
    if measurement > previous:
        increases += 1
    previous = measurement

print("Result =", increases)
