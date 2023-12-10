from math import *
with open("input.txt", "r") as f:
    grid = f.readlines()

for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == "S":
            x, y = i, j

chords = [(x, y)]
y += 1
steps = 1

def strReplace(x, y, char):
    data = list(grid[y])
    data[x] = char
    grid[y] = "".join(data)
dir = "S"

while (grid[y][x] != "S"):
    chords.append((x, y))
    i, j = x, y
    if grid[y][x] == "L":
        if dir == "S":
            x += 1
            dir = "E"
        elif dir == "W":
            y -= 1
            dir = "N"
    elif grid[y][x] == "J":
        if dir == "S":
            x -= 1
            dir = "W"
        elif dir == "E":
            y -= 1
            dir = "N"
    elif grid[y][x] == "7":
        if dir == "N":
            x -= 1
            dir = "W"
        elif dir == "E":
            y += 1
            dir = "S"
    elif grid[y][x] == "F": 
        if dir == "N":
            x += 1
            dir = "E"
        elif dir == "W":
            y += 1
            dir = "S"
    elif grid[y][x] == "-":	
        if dir == "W":
            x -= 1
        elif dir == "E":
            x += 1
    elif grid[y][x] == "|":
        if dir == "N":
            y -= 1
        elif dir == "S":
            y += 1
    steps += 1

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (x, y ) not in chords:
            strReplace(x, y, '.')

insiders = 0

for y, line in enumerate(grid):
    inside = False
    for x, char in enumerate(line):
        if char in "|JL":
            inside = not inside
        elif char == '.':
            insiders += inside

print(insiders)