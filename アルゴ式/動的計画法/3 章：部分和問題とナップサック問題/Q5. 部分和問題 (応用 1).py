# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))

# dp用意
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

# 計算
for i in range(N):
    for j in range(M):
        # 到達不可能なら更新しない
        if dp[i][j] == -1:
            continue


# 出力
