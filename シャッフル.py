from re import A


while True:
    w = input()
    if w == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        a = w[0:h]
        b = w[h:]
        w = b + a
    print(w)
