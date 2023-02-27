N = int(input())
A = list(map(int, input().split()))

# 全体から好きな数以外で構成される場合の数を引く
ans = 10 ** 3 - (10 - N) ** 3
print(ans)
