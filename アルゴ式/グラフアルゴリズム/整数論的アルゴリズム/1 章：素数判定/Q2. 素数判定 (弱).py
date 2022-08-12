# 素数かどうかを判定する関数
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 入力
N = int(input())

# 出力
if is_prime(N):
    print("Yes")
else:
    print("No")
