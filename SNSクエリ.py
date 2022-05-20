# 入力
N,Q = map(int,input().split())

# クエリ実行
User = [[] for i in range(N)]
for i in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    # Followクエリの処理
    if query_type == 0:

    # GetFollowersクエリの処理
    else: