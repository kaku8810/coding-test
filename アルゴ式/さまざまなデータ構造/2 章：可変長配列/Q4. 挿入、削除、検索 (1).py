# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# クエリ処理
for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 0:
        # insert
        k, v = query[1], query[2]
        A.insert(k, v)
    elif query_type == 1:
        # erase
        k = query[1]
        A.pop(k)
    else:
        # count
        v = query[1]
        print(A.count(v))
