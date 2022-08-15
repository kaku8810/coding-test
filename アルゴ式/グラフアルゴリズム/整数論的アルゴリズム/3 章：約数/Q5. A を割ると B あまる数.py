# 入力
A, B = map(int, input().split())

count = 0
for i in range(1, A + 1):
    if A % i == B:
        count += 1

# 出力
print(count)
