N = int(input())
# 1からNまでの数を格納するリスト
A = list(range(1, N + 1))

# 最後の1つになるまで1つおきに削除する
while len(A) > 1:
    # 1つ目の要素を削除
    A.pop(0)
    # 2つ目の要素を削除して、末尾に追加
    A.append(A.pop(0))

# 最後に残った要素を出力
print(A[0])
