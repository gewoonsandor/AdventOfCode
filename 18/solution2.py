from math import *
from funcy import pairwise

with open("input.txt") as f:
    directs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    instruct = [(directs[line.strip().split(" ")[-1][7]], int(line.strip().split(" ")[-1][2:7], 16)) for line in f.readlines() if line.strip()]

def area(instruct):
    chords, length = vertices(instruct)
    chords = [(int(z.real), int(z.imag)) for z in chords]
    area = abs(polygonArea(chords))
    return int(area - length / 2 + 1) + length

def vertices(instruct):
    chords, length = [0], 0

    for (direc, dist) in instruct:
        length += dist
        match direc:
            case "R":
                chords.append(chords[-1] - dist)
            case "L":
                chords.append(chords[-1] + dist)
            case "U":
                chords.append(chords[-1] - dist * 1j)
            case "D":
                chords.append(chords[-1] + dist * 1j)
    return chords, length

def polygonArea(chords):
    area = 0
    for (x1, y1), (x2, y2) in pairwise(chords + [chords[0]]):
        area += x1 * y2 - x2 * y1
    return area / 2

print(area(instruct))