# 入力
A = list(map(int, input().split()))

# 縦横4マスの二次元配列を宣言
dp = [[0 for _ in range(4)] for _ in range(4)]

# 初期値を設定
dp[0][0] = A[0]
dp[0][1] = A[1]
dp[0][2] = A[2]
dp[0][3] = A[3]

# 順に計算
for i in range(1, 4):
    for j in range(4):
        # 真上のマスを足す
        dp[i][j] += dp[i - 1][j]
        # 左上のマスを足す
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        # 右上のマスを足す
        if j + 1 < 4:
            dp[i][j] += dp[i - 1][j + 1]

# 出力
print(dp[3][3])
