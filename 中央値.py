n = int(input())
a = list(map(int, input().split()))
a.sort()
if n % 2 == 1:
    print(a[(n-1) // 2])
else:
    print((a[n//2 - 1] + a[n//2]) / 2)
