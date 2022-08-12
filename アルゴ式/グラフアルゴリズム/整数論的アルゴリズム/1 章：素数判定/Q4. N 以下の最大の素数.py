# 素数かどうかを判定する関数
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# 入力
N = int(input())

# 出力
for i in range(N, 1, -1):
    if is_prime(i):
        print(i)
        break
