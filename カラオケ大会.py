N,M = map(int, input().split())

# 正しい音程を記録
h = []
for i in range(M):
    h.append(int(input()))

# 音程データ記録
a = [[] for i in range(N)]
# N人繰り返し
for i in range(N):
    # M行繰り返し
    for j in range(M):
        a[i].append(int(input()))

# 得点計算
score = [100] * N
for i in range(N):
    for j in range(M):
        diff = h[j] - a[i][j]
        if diff < 0:
            diff = -diff
        if diff <= 5:
            score[i] = score[i]
        elif diff <= 10:
            score[i] -= 1
        elif diff <= 20:
            score[i] -= 2
        elif diff <= 30:
            score[i] -= 3
        else:
            score[i] -= 5

# 出力
if max(score) < 0:
    print(0)
else:
    print(max(score))
