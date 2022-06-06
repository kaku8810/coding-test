# 入力
N = int(input())
A = [input().split() for _ in range(N)]
A = [(a[0], int(a[1]), int(a[2])) for a in A]

# 並び替え
A.sort(key=lambda x: (-x[1], x[1]+x[2]))

# 出力
for i in A:
    print(i[0], i[1], i[2])