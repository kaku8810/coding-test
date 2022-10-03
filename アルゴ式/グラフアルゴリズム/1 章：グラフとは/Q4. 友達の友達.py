# 入力
N, M, X = map(int, input().split())

# 友達関係を表すグラフ
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# X の友達の友達を列挙
friends = set(G[X])

# X の友達の友達の友達を列挙
ans = set()
for i in friends:
    for j in G[i]:
        if j != X and j not in friends:
            ans.add(j)

# 友達の友達の人数を出力
print(len(ans))
