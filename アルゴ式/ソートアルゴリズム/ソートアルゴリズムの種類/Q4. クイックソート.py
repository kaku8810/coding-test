N = int(input())
A = list(map(int, input().split()))


# クイックソート本体
def quick_sort(v):
    # 配列が空の場合は何も起こらない
    if len(v) == 0:
        return []

    # v[X] の値を軸に配列を分割する
    X = len(v) // 2
    L, R = [], []
    for i, element in enumerate(v):
        if i == X:
            continue
        if element < v[X]:
            L.append(element)
        else:
            R.append(element)

    print(L, R)
    # L, R を再帰的にソートする
    L = quick_sort(L)
    R = quick_sort(R)

    # L, v[X], R をこの順につなげ、もとの配列を更新する
    L.append(v[X])
    L.extend(R)
    return L


# クイックソート
A = quick_sort(A)

# 配列の中身を出力する
print(*A)
