"""
Advent of Code 2015
Day 3: Perfectly Spherical Houses in a Vacuum (Part Two)
"""

with open("./input.txt", encoding="utf-8") as file:
    data = file.read()


class Houses:
    def __init__(self) -> None:
        self._grid = {}
        self._x = 0
        self._y = 0

    def _add(self) -> None:
        try:
            self._grid[f"{self._x}:{self._y}"] += 1
        except KeyError:
            self._grid[f"{self._x}:{self._y}"] = 0

    def deliver(self, movement) -> None:
        self._add()
        if movement == "^":
            self._y += 1
        elif movement == "v":
            self._y -= 1
        elif movement == ">":
            self._x += 1
        else:
            self._x -= 1
        self._add()

    def visited(self) -> set:
        return set(self._grid.keys())


houses = Houses()
robo = Houses()

for index in range(0, len(data), 2):
    move_1 = data[index]
    move_2 = data[index+1]
    houses.deliver(move_1)
    robo.deliver(move_2)

result = len(houses.visited().union(robo.visited()))

print("Result =", result)
