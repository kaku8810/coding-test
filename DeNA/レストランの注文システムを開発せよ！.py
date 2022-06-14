import sys

def main(lines):
    step = lines[0]

    if step == "1":
        menu = []
        order = []
        M = int(lines[1])
        for i, v in enumerate(lines):
            # M行を読み込む
            if i > 1 and i <= M + 1:
                menu.append(list(map(int, v.split())))
            # 最後の行まで読み込む
            elif i > M + 1:
                a = (v.split())
                order.append([a[0], int(a[1]), int(a[2]), int(a[3])])

        # 注文処理
        # i[0] = 文字列, i[1] = 席番号, i[2] = 料理番号, i[3] = 注文数, j[0] = 料理番号, j[1] = 在庫数, j[2] = 価格
        for i in order:
            for j in menu:
                if i[2] == j[0]:
                    if i[3] <= j[1]:
                        j[1] -= i[3]
                        for k in range(i[3]):
                            print('received order', i[1], i[2])
                    else:
                        print('sold out', i[1])
    elif step == "2":
        menu = []
        order = []
        M, K = map(int, lines[1].split())
        for i,v in enumerate(lines):
            if i > 1 and i <= M + 1:
                menu.append(list(map(int, v.split())))
            elif i > M + 1:
                order.append(v.split())
        cooking = []
        waiting = []
        for i in order:
            # 注文
            if i[0] == 'received' and len(cooking) < K:
                cooking.append(i[3])
                print(i[3])
            elif

        
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
