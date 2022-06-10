# 入力
N = int(input())
A = list(map(int, input().split()))

# 集計
B = []
for i in range(N):
    B.append((i, A.count(i)))

# ソート
B.sort(key=lambda x: (x[1]), reverse=True)

# 出力
for i in B:
    print(i[0], i[1])