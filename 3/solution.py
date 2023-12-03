with open("input.txt", "r") as f:
    engine = f.readlines()

symbols = "!@#$%^&*()_-+={}[],;<>/"
numbers = [str(x) for x in range(10)]
sum = 0

def checkadjacent(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                if engine[i][j] in symbols:
                    return True
            except IndexError:
                continue
    return False

for j, line in enumerate(engine):
    i = 0
    while i < len(line):
        if line[i] in numbers:
            addnum = False
            num = ""
            while (line[i] in numbers):
                addnum |= checkadjacent(j, i)
                num += line[i]
                i += 1
            if addnum:
                sum += int(num)
        i += 1

print(sum)