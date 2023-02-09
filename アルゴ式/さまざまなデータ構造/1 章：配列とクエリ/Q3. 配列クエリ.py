# 初期値
A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 0:
        k = query[1]
        print(A[k])
    else:
        k, v = query[1], query[2]
        A[k] = v
