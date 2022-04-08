n = int(input())
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for l in range(n):
    b, f, r, v = 3, 4, 5, 6
    count[b][f][r] = v
print(v)
