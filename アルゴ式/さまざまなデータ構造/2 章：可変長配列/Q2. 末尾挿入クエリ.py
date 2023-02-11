# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# クエリ処理
for _ in range(Q):
    query_type, n = map(int, input().split())
    if query_type == 0:
        if n >= len(A):
            print("Error")
        else:
            print(A[n])
    else:
        A.append(n)
