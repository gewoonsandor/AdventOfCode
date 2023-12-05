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

def find_route(seed, seq, seedlen):
    output = []
    seq = seq[:]
    while len(seq) > 1:
        a = seq.pop(0)
        b = seq[0]
        maps = mapping[a, b]
        
        new = None

        for dest, source, leng in maps:
            if source <= seed < source + leng:
                if source + leng > seed + seedlen:
                    dist = seed - source
                    new = dist + dest
                else:
                    cutdis = (seed + seedlen) - (source + leng + 1)
                    inputseq = [a] + seq
                    output += find_route(seed + cutdis, inputseq, cutdis)
                    seedlen = seedlen - cutdis 
                    dist = seed - source
                    new = dist + dest
            if seed < source < seed + seedlen:
                inputseq = [a] + seq
                output += find_route(source, inputseq, (seed + seedlen) - source)
                seedlen = source - seed

        if new == None:
            new = seed

        seed = new

    output += [seed]
    return output 

out = float('inf')
while(len(seeds) > 0):
    a = seeds.pop(0)
    b = seeds.pop(0)
    out = min(out, min(find_route(a, seq, b)))

print(out)