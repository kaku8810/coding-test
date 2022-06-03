import re
# 入力
S = 'RRLL'
A = 'bw'

# S繰り返し
for i in range(len(S)):
    if i % 2 == 0 and S[i] == 'R':
        A.append('b')
        # 同じ文字で挟まれている場合は、その文字を挟んでいる文字に変更
    elif i % 2 == 1 and S[i] == 'R':
        A.append('w')
    elif i % 2 == 0 and S[i] == 'L':
        A.insert(0,'b')
    elif i % 2 == 1 and S[i] == 'L':
        A.insert(0,'w')

# countして出力
print(A.count('b'),A.count('w'))