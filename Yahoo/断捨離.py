# 入力
n,k = map(int,input().split())
a = []
for i in range(n):
    s = input().split()
    a.append((s[0],int(s[1])))

# 優先度がk以上ならば、出力
for i in a:
    if i[1] >= k:
        print(i[0])