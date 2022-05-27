N,K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 2 ** 60
for i in range(N-K+1):
    diff = A[i+K-1] - A[i]
    ans = min(ans, diff)

print(ans)