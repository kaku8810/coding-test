# 入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# dp用意
dp = [[10000000000000] * N for _ in range(N)]
dp[0][-1] = A[0][-1]

# 計算
for i in range(N):
    for j in reversed(range(N)):
        # 上から来る場合
        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j])
        # 右から来る場合
        if j + 1 < N:
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + A[i][j])

# 出力
print(dp[-1][0])
