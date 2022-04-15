w = input()
n = 0
while True:
    words = input()
    if words == 'END_OF_TEXT':
        break
    words = words.lower().split()
    for i in words:
        if i == w:
            n += 1
print(n)
