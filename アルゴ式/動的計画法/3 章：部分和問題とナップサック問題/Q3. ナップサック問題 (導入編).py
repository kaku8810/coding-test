# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp用意
dp = [[-1] * M for _ in range(N)]

# 初期値
dp[0][0] = 0

# より大きい値で更新していく
for i in range(N - 1):
    for j in range(M):
        # 到達不可能なら更新しない
        if dp[i][j] == -1:
            continue
        # 真下のマスにコマを渡す
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 右下のマスにコマを渡す
        if j + A[i] < M:
            dp[i + 1][j + A[i]] = max(dp[i + 1][j + A[i]], dp[i][j] + B[i])

# 出力
print(dp[-1][-1])
