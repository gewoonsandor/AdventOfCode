with open("input.txt", "r") as f:
    input = [part.strip() for part in f.read().strip().split(',') if part.strip() != ""]

maping = {}
for i in range(256):
    maping[i] = list()

def checkBox(part, box):
    if "=" in part:
        label = part.split("=")[0]
        lens = [s for s in maping[box] if label in s]
        if not len(lens):
            maping[box].append(part.replace("="," "))
        else:
            maping[box][maping[box].index(lens[0])] = part.replace("="," ")
    elif "-" in part:
        lens = [s for s in maping[box] if part[:-1] == s[:-2]]
        if len(lens) > 0:
            maping[box].remove(lens[0])

def algorithm(part):
    curr = 0
    if "=" in part:
        checkpart = part[:-2]
    if '-' in part:
        checkpart = part[:-1]
            
    for char in checkpart:
        curr += ord(char)
        curr *= 17
        curr %= 256
    checkBox(part, curr)


for part in input:
    algorithm(part)

print(sum([sum([(key + 1) * int(item[-1]) * (i + 1) for i, item in enumerate(maping[key])]) for key in maping.keys() if len(maping[key])]))