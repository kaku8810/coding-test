c = [0 for i in range(26)]
while True:
    try:
        s = input().lower()
    except EOFError:
        break
    for i in s:
        n = ord(i) - ord('a')
        if n >= 0 and n < 26:
            c[n] += 1
for i in range(26):
    print(chr(ord('a')+i), ':', c[i])
