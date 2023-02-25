N = int(input())

ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == N:
            ans += 1
print(ans)
