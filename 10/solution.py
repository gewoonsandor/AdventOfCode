with open("input.txt", "r") as f:
    grid = f.readlines()

for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == "S":
            x, y = i, j

y += 1
steps = 1

dir = "S"
i, j = x, y
while (grid[y][x] != "S"):
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

print(steps / 2)