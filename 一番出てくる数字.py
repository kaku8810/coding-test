# 入力を受け取る
n = int(input())
a = list(map(int, input().split()))

# 線形探索（集計）
count = [0]*9
for i in a:
    count[i-1] += 1

# 線形探索（最大値）
index = 0
for i in range(9):
    if count[i] > count[index]:
        index = i

# 答えを出力する
ans = index + 1
print(ans)