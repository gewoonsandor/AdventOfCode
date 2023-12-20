with open("input.txt", "r") as f: 
    inputfile = f.read().split("\n\n")

instruct = inputfile[0].split("\n")
flows = {}
for item in instruct:
    id, cond = item.split("{")
    cond = cond[:-1].split(",")
    flows[id] = cond
items = inputfile[1].split("\n")

def run(item):
    curr_flow = "in"
    while True:
        for i in flows[curr_flow]:
            if ":" in i: 
                cond, act = i.split(":")
                if ">" in cond:
                    a, b = cond.split(">")
                    if item[a] > int(b):
                        if act == "A":
                            return True
                        if act == "R":
                            return False
                        curr_flow = act
                        break
                if "<" in cond:
                    a, b = cond.split("<")
                    if item[a] < int(b):
                        if act == "A":
                            return True
                        if act == "R":
                            return False
                        curr_flow = act
                        break
            if i == "A":
                return True
            if i == "R":
                return False
            curr_flow = i

result = 0
for i in items:
    item = {}
    for j in i[1:-1].split(","):
        print(j)
        k, v = j.split("=")
        item[k] = int(v)
    if run(item):
        result += sum(item.values())
print(result)
