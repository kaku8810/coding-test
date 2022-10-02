# 入力
N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# 最も友達の多い人を求める
C = 0  # 最も友達の多い人の番号
for i in range(N):
    if len(G[i]) > len(G[C]):
        C = i

# 小さい順に出力
G[C].sort()
print(*G[C])
