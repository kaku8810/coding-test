# 入力
N, X = map(int, input().split())
A = list(map(int, input().split()))
# Aは1から始まるのでダミーを追加
A.insert(0, -1)

count = 0
# 箱0まで移動
while X != 0:
    count += 1
    X = A[X]

# 出力
print(count)
