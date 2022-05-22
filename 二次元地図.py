# 入力
H,W = map(int, input().split())

# 二次元配列に保存
a = []
for i in range(H):
    S = list(input())
    a.append(S)

# カウント
p,q = map(int, input().split())
count = 0
for i in range(W):
    if a[p][i] == '#':
        count += 1

for i in range(H):
    if a[i][q] == '#':
        count += 1

if a[p][q] == '#':
    count -= 1

# 出力
print(count)