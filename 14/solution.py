with open("input.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]

def replace(x, y, char):
    if x < len(grid) - 1:
        grid[y] = grid[y][:x] + char + grid[y][x+1:]
    else:
        grid[y] = grid[y][:x] + char 

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O": 
            for y2 in range(y, -1, -1):
                if y == y2: continue
                if grid[y2][x] == "#" or grid[y2][x] == "O":
                    replace(x, y, ".")
                    replace(x, y2 + 1, "O")
                    break
                if y2 == 0:
                    replace(x, y, ".")
                    replace(x, y2, "O")

result = 0
for i in range(len(grid)):
    result += grid[i].count("O") * (len(grid[i]) - i)

print(result)