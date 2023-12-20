import queue
with open("input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

#broadcast = ["ns", "pj", "xz", "sg"
broadcast = ["ns", "pj", "xz", "sg"]

modules = {}
for line in input:
    if line.strip().startswith("b"):
        broadcast = [x.strip() for x in line.split(" -> ")[1].split(', ') if x.strip()]
        continue
    name, links = line.split(" -> ")
    modtype, name = (name[0], name[1:])
    links = links.split(", ")
    if modtype == "%":
        modules[name] = [modtype, links, False]
    else:
        modules[name] = [modtype, links, dict()]

for module in modules.keys():
    if modules[module][0] == "&":
        for modulekey in modules.keys():
            if module in modules[modulekey][1]:
                modules[module][2][modulekey] = False

q = queue.Queue()

lowp = 0
highp = 0

def pulse():
    global lowp, highp
    for module in broadcast:    
        q.put((module, False))
    while not q.empty():
        module = q.get()
        if module[1]: highp += 1
        else: lowp += 1
        
        if module[0] not in modules: continue
        
        if modules[module[0]][0] == "%":
            if not module[1]:
                modules[module[0]][2] = not modules[module[0]][2]
                for link in modules[module[0]][1]:
                    q.put((link, modules[module[0]][2], module[0]))
        else:
            modules[module[0]][2][module[2]] = module[1]
            #print(module, modules[module[0]][2])
            high = True
            for puls in modules[module[0]][2].keys():
                high &= modules[module[0]][2][puls]
            
            for link in modules[module[0]][1]:
                q.put((link, not high, module[0]))


for i in range(1000):
    lowp += 1
    pulse()

print(lowp * highp)