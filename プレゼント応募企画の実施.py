n, x, y = map(int, input().split())
for i in range(n):
    a = i + 1
    if a % x == 0 and a % y == 0:
        print('AB')
    elif a % x == 0:
        print('A')
    elif a % y == 0:
        print('B')
    else:
        print('N')
