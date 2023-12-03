with open("input.txt", "r") as f:
    engine = f.readlines()

numbers = [str(x) for x in range(10)]
sum = 0

def checkadjacent(x, y):
    output = {}
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            try:
                if engine[i][j] not in numbers:
                    continue
            except IndexError:
                print("indexError", i, j)
                continue
            current = engine[i][j]
            minmax = [j, j]
            iter = j - 1
            while(iter >= 0 and engine[i][iter] in numbers):
                current = engine[i][iter] + current
                minmax[0] = iter
                iter -= 1 
            iter = j + 1
            while(iter < len(engine[i]) and engine[i][iter] in numbers): 
                current = current + engine[i][iter]
                minmax[1] = iter
                iter += 1
            output[f'{i}{minmax[0]}{minmax[1]}'] = current
    if len(output) == 2:
        result = 1
        for key in output:
            result *= int(output[key])
        return result
    return 0

for y, line in enumerate(engine):
    for x, char in enumerate(line):
        if char == '*':
            sum += checkadjacent(x, y)

print(sum)