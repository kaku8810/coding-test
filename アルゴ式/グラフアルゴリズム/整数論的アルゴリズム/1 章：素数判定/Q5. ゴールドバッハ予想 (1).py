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
result = -1
for i in range(2, N + 1):
    if is_prime(i) and is_prime(N - i):
        result = i
        break
print(result)
