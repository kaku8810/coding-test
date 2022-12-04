N = int(input())
A = list(map(int, input().split()))

# N回ループすれば、必ず最大値が最後に来る
for _ in range(N):
    flag = False
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            flag = True

    if flag:
        print(*A)
    else:
        break
