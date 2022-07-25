# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# 最も友達が多い生徒を求める
student, max_num = -1, -1
for i in range(N):
    num = len(G[i])
    # max_numより大きい場合は更新
    if num > max_num:
        student, max_num = i, num

# 出力
G[student].sort()
print(*G[student])
