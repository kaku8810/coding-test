# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

# 計算
count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != T[i][j]:
            count += 1

# 出力
print(count)
