N,K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = A[1] - A[0]
for i in range(1, N-1):
    s = A[i+1] - A[i]
    if s < ans:
        ans = s

print(ans)