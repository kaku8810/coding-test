# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))

# dp用意
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][0] = True

# 順に計算
for i in range(N):
    for j in range(M + 1):
        if not dp[i][j]:
            continue
        dp[i + 1][j] = True
        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = True

# 出力
if dp[-1][-1]:
    print("Yes")
else:
    print("No")
