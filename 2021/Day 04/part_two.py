"""
Advent of Code 2021
Day 4: Giant Squid (Part Two)
"""

import re
import numpy as np

with open("./input.txt", encoding="utf-8") as file:
    data = list(filter(''.__ne__, file.read().splitlines()))


class Board:
    def __init__(self, data):
        self.data = data
        self.shape = (5, 5)
        self.called = np.zeros(self.shape)

    def call(self, value):
        found = np.argwhere(self.data == value)
        if len(found) != 0:
            self.called[found[0][0]][found[0][1]] = 1
        check = self.check()
        return check

    def check(self):
        for i in range(self.shape[0]):
            if np.sum(self.called[i]) == self.shape[0]:
                return True
            if np.sum(self.called.T[i]) == self.shape[0]:
                return True
        return False

    def get_all(self, marked=False):
        x = 0
        if marked:
            x = 1
        values = np.extract(self.called == x, self.data)
        return values


out = [int(i) for i in data[0].split(",")]
boards = []

for i in range(1, len(data)-1, 5):
    temp = []
    for j in range(i, i+5):
        temp.append([
            int(k) for k in re.sub(r"\s+", ",", data[j].strip()).split(",")
        ])
    boards.append(Board(np.array(temp)))

result = -1
incomplete = list(range(len(boards)))
for value in out:
    rm = []
    for index in incomplete:
        if boards[index].call(value):
            last = [boards[index], value]
            rm.append(index)
    for index in rm:
        incomplete.remove(index)

result = (sum(last[0].get_all()))*last[1]

print("Result =", result)
