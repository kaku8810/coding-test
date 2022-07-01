# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 計算
dp = [[False] * M for _ in range(N)]
dp[0][0] = True
for i in range(N):
    for j in range(M):
        # 1つ上のマスがTrueならTrueにする
        if i - 1 >= 0 and dp[i - 1][j]:
            dp[i][j] = True
        # 1つ上、A[i]つ左のマスがTrueならTrueにする
        if

# 出力
