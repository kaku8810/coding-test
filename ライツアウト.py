# 差分を表す配列
dx = [0, 1, 0, -1, 0]
dy = [0, 0, 1, 0, -1]

# 入力
H,W = map(int, input().split())

# 二次元配列に記録
grid = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '#':
            grid[i][j] = 1

# クエリ処理
Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    query_type,p,q = query[0],query[1],query[2]

    # Pushクエリ
    if query_type == 0:
        # 5マス分繰り返し
        for j in range(5):
            # 座標を決める
            x = p + dx[j]
            y = q + dy[j]
            # 座標が盤面内ならば反転
            if 0 <= x < W and 0 <= y < H:
                grid[x][y] = 1 - grid[x][y]

    # Getクエリ
    else:
        count = 0
        for j in range(5):
            # 座標を決める
            x = p + dx[j]
            y = q + dy[j]
            # 座標が盤面内ならばカウント
            if 0 <= x < H and 0 <= y < W:
                count += grid[x][y]
        print(count)