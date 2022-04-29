s = list(input())
n,m = map(int, input().split())
v = s[n-1]
s[n-1] = s[m-1]
s[m-1] = v
print(''.join(s))