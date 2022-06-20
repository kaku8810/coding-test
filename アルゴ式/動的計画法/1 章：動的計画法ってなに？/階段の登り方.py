# 入力
N = int(input())

# 計算の土台となる配列を作成
T = [0] * (N + 1)

# 初期値を設定
T[0] = 1

# 計算
for i in range(1, N + 1):
    if i - 1 >= 0:
        T[i] += T[i - 1]
    if i - 2 >= 0:
        T[i] += T[i - 2]
    if i - 3 >= 0:
        T[i] += T[i - 3]

# 出力
print(T[N])
