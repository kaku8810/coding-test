# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# クエリ処理
for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 0:
        v = query[1]
        A.append(v)
    else:
        if len(A) > 0:
            print(A.pop())
        else:
            print("Error")
