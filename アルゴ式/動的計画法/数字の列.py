# 入力
N, X, Y = map(int, input().split())

# 計算の舞台となる配列を宣言
A = [0] * N

# 初期値を定める
A[0], A[1] = X, Y

# 順に計算していく
for i in range(2, N):
    A[i] = (A[i-2] + A[i-1]) % 100

print(A[-1])