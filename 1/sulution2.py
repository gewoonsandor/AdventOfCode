with open ("input.txt", "r") as f:
    wordlist = f.readlines()

numbers = [str(i) for i in range(10)]
numberd = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
}

digits = []

for word in wordlist:
    current = ""
    i = 0 
    loop = True
    while (loop):
        for number in numbers:
            if word[i:].startswith(number):
                current += number
                loop = False
                break
        if not loop: break
        for number in numberd:
            if word[i:].startswith(number):
                current += numberd[number]
                loop = False
                break
        i += 1
    i = len(word)
    loop = True
    while (loop):
        for number in numbers:
            if word[:i].endswith(number):
                current += number
                loop = False
                break
        if not loop: break
        for number in numberd:
            if word[:i].endswith(number):
                current += numberd[number]
                loop = False
                break
        i -= 1
    digits.append(current)

print(sum([int(x) for x in digits]))
