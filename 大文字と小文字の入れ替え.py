str = input()
for i in range(len(str)):
    a = str[i]
    if a.islower():
        print(a.upper(), end='')
    elif a.isupper():
        print(a.lower(), end='')
    else:
        print(a, end='')
print()

# or
str = input()
for i in str:
    if i.islower():
        print(i.upper(), end='')
    elif i.isupper():
        print(i.lower(), end='')
    else:
        print(i, end='')
print()

# or
str = input()
print(str.swapcase())
