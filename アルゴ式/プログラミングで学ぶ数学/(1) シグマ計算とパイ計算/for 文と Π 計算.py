N = int(input())
A = list(map(int, input().split()))

ans = 1 
for i in range(N):
    # 1の位のだけでよいので10で割る
    ans = ans * A[i] % 10

print(ans)
