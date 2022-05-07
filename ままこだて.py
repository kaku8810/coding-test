n = int(input())
a = list(range(1,n+1))

# 最後の1つになるまで1つおきに取り除く
while len(a) > 1:
    a.pop(0)
    a.append(a[0])
    a.pop(0)

# 最後の1つを出力する
print(a[0])