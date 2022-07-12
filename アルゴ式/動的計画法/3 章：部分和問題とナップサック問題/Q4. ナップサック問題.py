# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

# dp用意
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

# より大きい値で更新していく
for i in range(N):
    for j in range(M + 1):
        # 到達不可能なら更新しない
        if dp[i][j] == -1:
            continue
        # ボールを入れない場合
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # ボールを入れる場合
        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = max(dp[i + 1][j + W[i]], dp[i][j] + V[i])

# 出力
print(max(dp[-1]))
