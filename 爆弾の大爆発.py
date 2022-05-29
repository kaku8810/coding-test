# 入力
H,W = map(int, input().split())

# マス目記録
grid = [[0 for j in range(W)] for i in range(H)]

# 爆発する列を書き換え
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == '#':
            for k in range(W):
                grid[i][k] = 1
            for l in range(H):
                grid[l][j] = 1
            

# 数えて出力
ans = sum(map(sum, grid))
print(ans)