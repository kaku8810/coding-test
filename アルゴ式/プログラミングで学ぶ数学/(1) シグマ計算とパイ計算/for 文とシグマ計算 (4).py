N = int(input())

ans = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        ans += i * j

print(ans)

