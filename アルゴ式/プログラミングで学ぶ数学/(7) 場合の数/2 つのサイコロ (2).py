X, Y = map(int, input().split())

ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        sum = i + j
        if sum == X or sum == Y:
            ans += 1

print(ans)
