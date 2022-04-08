n = int(input())
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for l in range(n):
    b, f, r, v = map(int, input().split())
    count[b-1][f-1][r-1] += v
for building in range(4):
    for floor in range(3):
        for room in range(10):
            print(count[building][floor][room], end=' ')
        print()
    print("#"*20)
