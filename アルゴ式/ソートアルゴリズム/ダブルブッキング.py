# 入力
N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]

# ソート
S.sort()

# Rが次のL以下であるか
flg = True
for i in range(N-1):
    if S[i][1] > S[i+1][0]:
        flg = False
        break

if flg:
    print('Yes')
else:
    print('No')