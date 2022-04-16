str = input()
n = int(input())
for i in range(n):
    m = input().split()
    o = m[0]
    a = int(m[1])
    b = int(m[2])
    if o == 'print':
        print(str[a:b+1])
    elif o == 'reverse':
        le = str[:a]
        mid = str[a:b+1]
        ri = str[b+1:]
        mid = mid[::-1]
        str = le + mid + ri
    else:
        p = m[3]
        le = str[:a]
        mid = str[a:b+1]
        ri = str[b+1:]
        mid = p
        str = le + mid + ri
