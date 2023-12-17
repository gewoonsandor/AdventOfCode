import queue
with open('input.txt', 'r') as f:
    field = [[int(x) for x in s if x.strip()] for s in f.readlines()]

q = queue.PriorityQueue()
q.put((0, 0, 1, (0, 1), 1))
q.put((0, 1, 0, (1, 0), 1))

result = float('inf')
rows = len(field) - 1
cols = len(field[0]) - 1

visited = set()

while not q.empty():
    heat, x, y, dir, sameDir = q.get()
    
    if x == cols and y == rows:
        result = min(result, heat + field[rows][cols])
    
    if ((x, y, dir, sameDir)) in visited: continue
    visited.add((x, y, dir, sameDir))
    
    if dir in [(0, -1), (0, 1)]:
        if x + 1 <= cols: q.put((heat + field[y][x], x + 1, y, (1, 0), 1))
        if x - 1 >= 0: q.put((heat + field[y][x], x - 1, y, (-1, 0), 1))  
    else:
        if y + 1 <= rows: q.put((heat + field[y][x], x, y + 1, (0, 1), 1))
        if y - 1 >= 0: q.put((heat + field[y][x], x, y - 1, (0, -1), 1))

    if sameDir >= 3: continue
        
    if 0 <= y + dir[1] <= rows and  0 <= x + dir[0] <= cols: 
        q.put((heat + field[y][x], x + dir[0], y + dir[1], dir, sameDir + 1))

print(result)