# 入力
N, A, B = map(int, input().split())
S = [input() for i in range(N)]

# 出力
if S[A][B] == "o":
    print("YES")
else:
    print("NO")
