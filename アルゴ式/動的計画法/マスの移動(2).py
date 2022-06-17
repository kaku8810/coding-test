# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 初期値
INF = 1000000
T = [INF] * N
T[0] = 0

# 計算
for i in range(1, N):
    for j in range(1, M + 1):
        if i - j >= 0:
            T[i] = min(T[i], T[i - j] + A[i] * j)

# 出力
print(T[-1])
