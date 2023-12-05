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



seq = ["location"]
current = "location"

while current != "seed":
    next = None
    for b, a  in mapping:
        if a == current:
            next = b
    seq.append(next)
    current = next

def find_route(seed, seq):
    seq = seq[:]
    while len(seq) > 1:
        a = seq.pop(0)
        b = seq[0]
        maps = mapping[b, a]
        
        new = None

        for dest, source, leng in maps:
            if dest <= seed < dest + leng:
                dist = seed - dest
                new = dist + source
        
        if new == None:
            new = seed

        seed = new

    return seed

i = 0
while True:
    seedscopy = seeds
    out = find_route(i, seq)
    while len(seedscopy) > 0:
        start = seedscopy.pop(0)
        leng = seedscopy.pop(0)
        if start <= out < start + leng:
            print(i)
            exit()