# 入力
N, M = map(int, input().split())

# フォロー関係を記録
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

# 出力
for i in range(N):
    G[i].sort()
    print(" ".join(map(str, G[i])))
