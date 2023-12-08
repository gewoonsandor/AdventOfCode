from itertools import cycle
from math import lcm

with open('input.txt', 'r') as f:
    instruc, location = f.read().split('\n\n')

links = dict()
for line in location.split('\n'):
    line.strip()
    start, lr = line.split(' = ')
    lr = lr.strip()[1:-1]
    links[start] = [x.strip() for x in lr.split(', ')]

def solve(loc):
    steps = 0
    for step in cycle(instruc):
        loc = links[loc][0 if step == 'L' else 1]
        steps += 1
        if loc.endswith("Z"):
            break
    return steps

locs = [x for x in links.keys() if x.endswith("A")]
dists = []
for loc in locs:
    dists.append(solve(loc))

print(lcm(*dists))