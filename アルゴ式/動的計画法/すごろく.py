# 入力
N, M = map(int, input().split())
D = list(map(int, input().split()))

# 動的計画法の舞台となる配列を作成
T = [False] * (N + 1)
# マス0は最初からたどり着いているので、Trueにする
T[0] = True

# 動的計画法を計算
for i in range(1, N + 1):
    for j in range(M):
        if i - D[j] >= 0 and 