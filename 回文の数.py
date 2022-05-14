# 入力
n = int(input())

# 全探索
count = 0
for i in range(n):
    s = input()
    # 回分かどうか
    flg = True
    m = len(s)
    for j in range(m):
        if s[j] != s[(m-1)-j]:
            flg = False
    if flg:
        count += 1

# 出力
print(count)