"""
Advent of Code 2021
Day 3: Binary Diagnostic (Part One)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read().splitlines()

gamma = ""
epsilon = ""
bit_size = range(len(data[0]))
data_size = range(len(data))
count = {i: 0 for i in bit_size}

for b in data_size:
    for bit in bit_size:
        count[bit] += int(data[b][bit])

for bit in bit_size:
    if count[bit] > (len(data)/2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

result = int(gamma, 2) * int(epsilon, 2)

print("Result =", result)
