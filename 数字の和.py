while True:
    s = input()
    if int(s) == 0:
        break
    sum = 0
    for i in s:
        sum += int(i)
    print(sum)
