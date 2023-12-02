with open ("input.txt", "r") as f:
    wordlist = f.readlines()

numbers = [str(i) for i in range(10)]

digits = []

for word in wordlist:
    current = ""
    i = 0 
    while (word[i] not in numbers):
        i += 1
    current += word[i]
    
    i = len(word) - 1
    while (word[i] not in numbers):
        i -= 1
    current += word[i]

    digits.append(current)

print(sum([int(x) for x in digits]))
