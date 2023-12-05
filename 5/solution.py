with open("input.txt", "r") as f:
    almanac = f.read()
    almanac = almanac.split("\n\n")

seeds = [int(x) for x in almanac[0].split(":")[1].strip().split(" ")]
mapping = {}

for group in almanac[1:]:
    lines = group.splitlines()

    ranges = []
    for line in lines[1:]:
        ranges.append(tuple(map(int, line.split())))

    key = lines[0].split(" ")[0]
    key, key2 = key.split("-to-")
    mapping[key, key2] = ranges



seq = ["seed"]
current = "seed"

while current != "location":
    next = None
    for a, b in mapping:
        if a == current:
            next = b
    seq.append(next)
    current = next

def find_route(seed, seq):
    seq = seq[:]
    while len(seq) > 1:
        a = seq.pop(0)
        b = seq[0]
        maps = mapping[a, b]
        
        new = None

        for dest, source, leng in maps:
            if source <= seed < source + leng:
                dist = seed - source
                new = dist + dest
        
        if new == None:
            new = seed

        seed = new

    return seed

output = float('inf')
while len(seeds) != 0:
    start = seeds.pop(0)
    length = seeds.pop(0)
    for i in range(start, start + length):
        output = min(output, find_route(i, seq))

print(output)