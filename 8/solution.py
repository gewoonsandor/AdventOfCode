with open('input.txt', 'r') as f:
    instruc, location = f.read().split('\n\n')

links = dict()
for line in location.split('\n'):
    line.strip()
    start, lr = line.split(' = ')
    lr = lr.strip()[1:-1]
    links[start] = [x.strip() for x in lr.split(', ')]


loc = "AAA"
steps = 0
while(loc != "ZZZ"):
    for step in instruc:
        loc = links[loc][0 if step == 'L' else 1]
        steps += 1
        if loc == "ZZZ":
            break

print(steps)