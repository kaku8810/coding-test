# 入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# dp用意
dp = [[0] * N for _ in range(N)]
dp[0][0] = A[0][0]

# 順に計算
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        # 上のマスがなかったら左のマスだけ足す
        if i - 1 < 0:
            dp[i][j] = dp[i][j - 1] + A[i][j]
        # 左のマスがなかったら上のマスだけ足す
        elif j - 1 < 0:
            dp[i][j] = dp[i - 1][j] + A[i][j]
        # 上と左のマスがあったら最大値を足す
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + A[i][j]

# 出力
print(dp[-1][-1])
