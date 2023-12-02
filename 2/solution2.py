with open("input.txt", 'r') as f:
    games = f.readlines()

global result
result = 0

def checkGame(game):
    global result
    id, turns = game.split(':')
    id = int(id.split(' ')[1])
    turns = turns.strip().split(';')
    maxg = 0
    maxr = 0
    maxb = 0
    for turn in turns:
        turn = turn.strip()
        for move in turn.split(','):
            move = move.strip()
            cubes, color = move.split(' ')
            turn *= int(cubes)
            if color == 'green':
                maxg = max(maxg, int(cubes))
            if color == 'red':
                maxr = max(maxr, int(cubes))
            if color == 'blue':
                maxb = max(maxb, int(cubes))
    result += (maxg * maxr * maxb)

for game in games:
    checkGame(game)

print(result)