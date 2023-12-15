with open("input.txt", "r") as f:
    input = [part.strip() for part in f.read().strip().split(',') if part.strip() != ""]

def algorithm(part):
    curr = 0
    for char in part:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

print(sum([algorithm(part) for part in input]))