# 入力
N = int(input())

# 配列用意
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

# 計算
for i in range(N):
    for j in range(N):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]

# 出力
print(dp[-1][-1])
