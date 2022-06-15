# 入力
N = int(input())

# *Nの配列を用意して、その段までに何通りあるかを計算する。
T = [0] * N
T[0], T[1] = 1

for i in range(2, N):
    T[i] = T[i - 1] + T[i - 2]


# 出力
print(T[-1])
