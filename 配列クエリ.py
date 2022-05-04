a = [3,1,4,1,5,9,2,6,5,3]

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    k = query[1]
    if query[0] == 0:
        print(a[k])
    else:
        v = query[2]
        a[k] = v
