N = int(input())
A = list(map(int, input().split()))

for k in range(1, N):
    while k and A[k - 1] > A[k]:
        A[k - 1], A[k] = A[k], A[k - 1]
        k -= 1

    print(*A)
