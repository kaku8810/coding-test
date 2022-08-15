# 入力
N = int(input())

# N + 1は必ずある
res = N + 1
for i in range(2, N + 1):
    # √Nで打ち切り
    if i * i > N:
        break

    # 約数でなければスキップ
    if N % i != 0:
        continue

    # 約数でより小さいものがあれば更新
    res = min(res, i + N // i)

print(res)
