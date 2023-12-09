from itertools import pairwise
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [[int(x) for x in line.strip().split(" ")] for line in lines]

output = 0

for line in lines:
    preditcion = []
    preditcion.append(line)
    while(not all(x == 0 for x in preditcion[-1])):
        preditcion.append([b - a for a, b in pairwise(preditcion[-1])])
    outcome = preditcion[-2][-1]
    preditcion = list(reversed(preditcion))
    preditcion.pop(0)
    preditcion.pop(0)
    for line in preditcion:
        outcome = line[-1] + outcome 
    output += outcome
print(output)