from functools import cache
with open("input.txt", "r") as f:
    lines = [(x, tuple(map(int, n.split(",")))) for x, n in [x.split() for x in f.read().strip().split("\n")]]

@cache
def solve(spring, sizes, done=0):
    if not spring:
        return not sizes and not done
    result = 0
    option = [".", "#"] if spring[0] == "?" else spring[0]
    for char in option:
        if char == "#":
            result += solve(spring[1:], sizes, done + 1)
        else:
            if done:
                if sizes and sizes[0] == done:
                    result += solve(spring[1:], sizes[1:])
            else:
                result += solve(spring[1:], sizes)
    return result

print(sum(solve("?".join([group] * 5) + ".", sizes * 5) for group, sizes in lines))