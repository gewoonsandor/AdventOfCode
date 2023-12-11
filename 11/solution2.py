from math import *
with open("input.txt", "r") as f:
    space = f.readlines()

galaxies = []
emptyLines = []
emptycols = []

for y, line in enumerate(space):
    if line.count('#') == 0:
        emptyLines.append(y)
        continue
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append((x, y))
        
for x in range(len(space[0])):
    empty = True
    for y in range(len(space)):
        if space[y][x] == '#':
            empty = False
            break
    if empty:
        emptycols.append(x)

def distance(chords1, chords2):
    extra = 0
    extrax = 0
    extray = 0
    for i in range(min(chords1[1], chords2[1]), max(chords1[1], chords2[1])):
        if i in emptyLines:
            extra += 1000000
            extray += 1
    for i in range(min(chords1[0], chords2[0]), max(chords1[0], chords2[0])):
        if i in emptycols:
            extra += 1000000
            extrax += 1
    return (abs(chords1[0] - chords2[0]) - extrax) + ((abs(chords1[1] - chords2[1]) - extray) + extra) 
        
result = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        result += distance(galaxies[i], galaxies[j])
    
print(result)