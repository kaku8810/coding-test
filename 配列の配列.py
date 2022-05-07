N,T = input().split()
N = int(N)

student_color = [[] for i in range(N)]
for i in range(N):
    info = list(input().split())
    M = int(info[0])

    for j in range(1, M + 1):
        student_color[i].append(info[j])

ans = 0
for i in range(N):
    for j in student_color[i]:
        if j == T:
            ans += 1

print(ans)
