H, W, x, y = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        print(S[i][j], end="")
    print()
