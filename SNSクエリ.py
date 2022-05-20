# 入力
N,Q = map(int,input().split())

# クエリ実行
User = [[] for i in range(N)]
for i in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    # Followクエリの処理
    if query_type == 0:
        x = query[1]
        y = query[2]
        User[x].append(y)
    # GetFollowersクエリの処理
    else:
        followers = []
        z = query[1]
        for j in range(N):
            if z in User[j]:
                followers.append(j)
        if followers:
            print(*followers)
        else:
            print('No')