# 入力
list = input().split()
n = len(list)

# 辞書型に保存
dict = {}
for i in range(n):
    # 最後の要素はmに代入
    if i == n - 1:
        m = int(list[i])
    else:
        a,s = list[i].split(':')
        a = int(a)
        dict[a]= s

ans =''
# keyで並び替えたものをループ
for i in sorted(dict.keys()):
    # 割り切れたら連結
    if m % i == 0:
        ans += dict[i]

# 出力
if ans:
    print(ans)
else:
    print(m)