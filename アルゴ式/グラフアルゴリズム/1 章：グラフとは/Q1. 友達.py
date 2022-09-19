N, A, B = map(int, input().split())

G = [input() for _ in range(N)]

if G[A][B] == "o":
    print("Yes")
else:
    print("No")
