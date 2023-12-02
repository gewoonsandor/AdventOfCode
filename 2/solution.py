with open("input.txt", 'r') as f:
    games = f.readlines()

global result
result = 0

def checkGame(game):
    global result
    id, turns = game.split(':')
    id = int(id.split(' ')[1])
    turns = turns.strip().split(';')
    for turn in turns:
        turn = turn.strip()
        for move in turn.split(','):
            move = move.strip()
            cubes, color = move.split(' ')
            if color == 'green':
                if int(cubes) > 13:
                    return
            if color == 'red':
                if int(cubes) > 12:
                    return
            if color == 'blue':
                if int(cubes) > 14:
                    return
    result += id

for game in games:
    checkGame(game)

print(result)