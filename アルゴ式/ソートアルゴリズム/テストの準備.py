N = int(input())
A = list(map(int, input().split()))

B = sorted(set(A), reverse=True)
# 辞書型に順位を保存
C = {v:i for i, v in enumerate(B)}

for a in A:
    print(C[a])