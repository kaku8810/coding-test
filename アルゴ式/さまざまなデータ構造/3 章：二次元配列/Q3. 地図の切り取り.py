# 入力
H, W, x, y = map(int, input().split())
S = [input() for _ in range(H)]

# 出力
for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        print(S[i][j], end="")
    print()

"""スライスを使うともっと簡単に書ける
H, W, x, y = list(map(int, input().split()))
S = [input() for _ in range(H)]

for i in range(x - 1, x + 2):
    print(S[i][y - 1 : y + 2])
"""
