# 入力
N = int(input())
A = list(map(int, input().split()))

# 集計
nums = [0] * N
for a in A:
    nums[a] += 1

students = [i for i in range(N) ]
# ソート
students.sort(key=lambda x: nums[x], reverse=True)

# 出力
for i in students:
    print(i, nums[i])