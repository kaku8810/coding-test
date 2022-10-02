# 入力
N, M, X = map(int, input().split())

# 友達関係を表すグラフ
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
