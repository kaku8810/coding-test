# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# dp用意
dp = [[False] * M for _ in range(N)]
dp[0][0] = True

# 順に計算
for i in range(N - 1):
    for j in range(M):
        if not dp[i][j]:
            continue
        # 真下のマスにコマを渡す
        dp[i + 1][j] = True
        # 右下のマスにコマを渡す
        if j + A[i] < M:
            dp[i + 1][j + A[i]] = True

# 出力
print(sum(dp[-1]))
