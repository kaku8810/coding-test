N = int(input())
S = [input() for i in range(N)]

flg = False
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            flg = True

if flg:
    print('Yes')
else:
    print('No')