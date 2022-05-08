n = int(input())
a = list(map(int, input().split()))

count = 0
for i in a:
    flg = True
    if i == 1:
        flg = False
    else:
        for j in range(2, i):
            if i % j == 0:
                flg = False
        if flg:
            count += 1

print(count)