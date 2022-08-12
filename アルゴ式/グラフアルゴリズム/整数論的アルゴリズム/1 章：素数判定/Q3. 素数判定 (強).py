# 入力
N = int(input())

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


# 出力
if is_prime(N):
    print("Yes")
else:
    print("No")
