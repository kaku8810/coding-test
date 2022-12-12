N = int(input())
A = list(map(int, input().split()))

for k in range(N - 1):
    # k以降で最小値のインデックスを求める
    min_index = A[k:].index(min(A[k:])) + k
    # kとminを入れ替える
    A[k], A[min_index] = A[min_index], A[k]

    print(*A)
