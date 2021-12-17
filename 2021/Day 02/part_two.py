"""
Advent of Code 2021
Day 2: Dive! (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().splitlines()

aim = 0
horizontal = 0
depth = 0

for measurement in data:
    command, amount = measurement.split(" ")
    amount = int(amount)
    if command == "forward":
        horizontal += amount
        depth += aim * amount
    elif command == "down":
        aim += amount
    else:
        aim -= amount

result = horizontal * depth

print("Result =", result)
