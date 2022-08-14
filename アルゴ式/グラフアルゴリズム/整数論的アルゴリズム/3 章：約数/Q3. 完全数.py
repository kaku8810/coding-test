# Nの約数を全て求める関数
def calc_divisors(N):
    # 答えを格納するリスト
    divisors = []

    # 各整数がNの約数かどうかを判定する
    for i in range(1, N + 1):
        # √Nで打ち切り
        if i * i > N:
            break

        # iが約数出ない場合はスキップ
        if N % i != 0:
            continue

        # 約数の場合は追加
        divisors.append(i)

        # N ÷ iも約数である
        if N // i != i:
            divisors.append(N // i)

    # 小さい順に並び替えて返す
    divisors.sort()
    return divisors


# 入力
N = int(input())

# 完全数かどうかを判定
if sum(calc_divisors(N)) == N * 2:
    print("Yes")
else:
    print("No")
