"""
Advent of Code 2021
Day 4 - Giant Squid (Part One)
"""

import re
import numpy as np

with open("./input.txt", encoding="utf-8") as file:
    data = list(filter(''.__ne__, file.read().splitlines()))


class Board:
    def __init__(self, data):
        self.data = data
        self.shape = self.data.shape
        self.called = np.zeros(self.shape)

    def call(self, value):
        found = np.where(self.data == value)
        if len(found[0]) > 0:
            self.called[found[0][0]][found[1][0]] = 1
        check = self.check()
        return check

    def check(self):
        for i in range(self.shape[0]):
            if np.count_nonzero(self.called[i] == 1) == self.shape[0]:
                return True
            if np.count_nonzero(self.called.T[i] == 1) == self.shape[0]:
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
for value in out:
    for board in boards:
        if board.call(value):
            result = sum(board.get_all())*value
            break
    if result != -1:
        break

print("Result =", result)
