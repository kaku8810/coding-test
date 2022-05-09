# 入力
L,R = map(int, input().split())

# L以上R以下の繰り返し
count = 0
for i in range(L,R+1):
    x = str(i)
    n = len(x)
    flg = True
    for j in range(n):
        if x[j] != x[(n-1)-j]:
            flg = False
    if flg:
        count += 1
print(count)
            