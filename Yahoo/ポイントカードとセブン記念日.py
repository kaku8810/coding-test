# 入力
a,b,n = map(int,input().split())

# 出力
point = a
index = 1

# 初日にnポイントを超えてたら
if point >= n:
    print(0)
else:
    # nポイントを超えるまで繰り返し
    while True:
        # indexに'7'が含まれていたらbポイントを加算
        if str(index) in '7':
            point += a + b
        else:
            point += a
        # pointがnを超えたら終了
        if point >= n:
            print(index)
            break
        index += 1