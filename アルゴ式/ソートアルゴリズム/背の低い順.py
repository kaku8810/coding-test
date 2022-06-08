# 入力
N, X = map(int, input().split())
A = []
for i in range(N):
    a = input().split()
    A.append((i, a[0], int(a[1])))

#　並び替え
A.sort(key=lambda x: (x[2], x[0]))

# 出力
for i in range(len(A)):
    if A[i][0] == X:
        print(A[i-1][1])
        print(A[i+1][1])