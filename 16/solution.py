with open("input.txt", "r") as f:
    field = [line.strip() for line in f.readlines() if line != '']

sameroute = {}
queue = [(-1, 0, 3)]

while(queue):
    x, y, dir = queue.pop(0)
    if dir == 0:
        nextX = x 
        nextY = y + 1
    if dir == 1:
        nextX = x - 1 
        nextY = y  
    if dir == 2:
        nextX = x  
        nextY = y - 1
    if dir == 3:
        nextX = x + 1
        nextY = y 
    
    if (nextX < 0 or nextY < 0 or nextX >= len(field[0]) or nextY >= len(field)):
        continue
        
    if (nextX, nextY) in sameroute:
        if dir in sameroute[nextX, nextY]:
            continue
        else:
            sameroute[nextX, nextY].append(dir)
    else:
        sameroute[nextX, nextY] = [dir]

    if field[nextY][nextX] == '/':
        if dir == 1 or dir == 3:
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
    elif field[nextY][nextX] == '\\':
        if dir == 2 or dir == 0:
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
    elif field[nextY][nextX] == '|':
        if dir == 1 or dir == 3:
            dir = (dir + 1) % 4
            queue.append((nextX, nextY, (dir + 2 ) % 4))
    elif field[nextY][nextX] == '-':
        if dir == 0 or dir == 2:
            dir = (dir + 1) % 4
            queue.append((nextX, nextY, (dir + 2 ) % 4))
        
    queue.append((nextX, nextY, dir))
 
print(len(sameroute.keys()))
