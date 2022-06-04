# 入力
N,K = map(int, input().split())
S = [tuple(map(int, input().split())) for _ in range(N)]

# ソート
S.sort()

# K個になるまで繰り返し
ans = 0
for (A,B) in S:
    # 買う個数
    num = min(K, B)

    # 買う
    K -= num

    # 金額を足す
    ans += A * num

print(ans)