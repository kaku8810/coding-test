N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(0, N):
    for j in range(0, M):
        ans += A[i] + B[j]

print(ans)
