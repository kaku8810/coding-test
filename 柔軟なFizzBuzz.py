# 空白区切りで配列に入力を受け取る
data = '5:go 3:san 2:ni 1'
list = data.split()
n = len(list)
# 最後の要素以外をコロンで区切って辞書型に保存する
dict = {}
for i in range(n):
    if i == n - 1:
        m = int(list[i])
    else:
        a,s = list[i].split(':')
        a = int(a)
        dict[a]= s
# 条件分岐
ans =''
for i in sorted(dict.keys()):
    if m % i == 0:
        ans += dict[i]
if not ans:
    print(m)
else:
    print(ans)