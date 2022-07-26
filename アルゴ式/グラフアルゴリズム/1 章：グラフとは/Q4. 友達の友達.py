# 入力
N, M, X = map(int, input().split())

# 友達関係を記録
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# 友達を重複なしで列挙
friends = set(G[X])

# 友達の友達を重複なしで列挙
result = set()
for i in G[X]:
    for j in G[i]:
        # XとG[X]に含まれるものは除外
        if j != X and j not in friends:
            result.add(j)
# 出力
print(len(result))
