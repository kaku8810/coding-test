L, R = map(int, input().split())

ans = 0
for i in range(L, R + 1):
    ans += (2 * i - 1) ** 2

print(ans)
