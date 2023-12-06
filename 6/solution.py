with open("./input.txt", "r") as f:
    file = f.readlines()

lens, dists = [[int(x.strip()) for x in line.split(":")[1].strip().split(" ") if x.strip() != ""] for line in file]

def upperLower(duration, length):
    i = 0
    while ((length - i) * i < duration):
        i += 1
    low = i 
    while ((length - i) * i > duration):
        i += 1
    upper = i
    return upper - low

output = 1
for x, y in zip(lens, dists):
    output *= upperLower(y, x)

print(output)