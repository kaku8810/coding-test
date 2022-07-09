# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

# dp用意
dp = [[0] * (M + 1) for _ in range(N + 1)]

# より大きい値で更新していく
for i in range(N):
    for j in range(M + 1):
        

# 出力
