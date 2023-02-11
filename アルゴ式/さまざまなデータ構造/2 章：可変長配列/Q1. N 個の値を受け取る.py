# 入力
N, k = map(int, input().split())
A = list(map(int, input().split()))

# 出力
print(A[k])
print(A[-(k + 1)])
