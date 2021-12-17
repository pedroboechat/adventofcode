"""
Advent of Code 2021
Day 6 - Lanternfish (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = [int(i) for i in file.read().split(",")]

lanternfishes = {
    0: data.count(0),
    1: data.count(1),
    2: data.count(2),
    3: data.count(3),
    4: data.count(4),
    5: data.count(5),
    6: data.count(6),
    7: data.count(7),
    8: data.count(8)
}

for i in range(256):
    parents = int(lanternfishes[0])

    lanternfishes = {
        0: lanternfishes[1],
        1: lanternfishes[2],
        2: lanternfishes[3],
        3: lanternfishes[4],
        4: lanternfishes[5],
        5: lanternfishes[6],
        6: lanternfishes[7],
        7: lanternfishes[8],
        8: lanternfishes[0]
    }

    if parents > 0:
        lanternfishes[6] += parents

result = 0
for fishes in lanternfishes.values():
    result += fishes

print("Result =", result)
