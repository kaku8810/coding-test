N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

for i in range(N):
    G[i].sort()
    print(*G[i])
